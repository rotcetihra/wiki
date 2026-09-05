# Кэширование ответа и OutputCache

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10|Руководство по ASP.NET Core 10]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 17. Кэширование|Глава 17. Кэширование]] / Кэширование ответа и OutputCache

[[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 17. Кэширование/Кэширование статических файлов|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 17. Кэширование|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 18. Мониторинг работоспособности приложения/Health Check Middleware|Вперёд]]

**Дата написания:** 05.09.2026

## Кэширование ответа и OutputCache

Последнее обновление: 25.08.2023




-

-

-














ASP.NET позволяет кэшировать ответ приложения, и для этого применяет сервис IOutputCacheStore и middleware OutputCacheMiddleware.
Рассмотрим, как их использовать в приложении.


Для кэширования ответа приложения нам надо прежде всего сконфигурировать приложения. Для этого следует выполнить два шага. Прежде всего, добавить в коллекцию
сервисов приложения все необходимые сервисы с помощью метода AddOutputCache()

```

var builder = WebApplication.CreateBuilder(args);
builder.Services.AddOutputCache();

```


Во-вторых, надо добить в конвейер приложения middleware `OutputCacheMiddleware` с помощью метода UseOutputCache():

```

var app = builder.Build();
app.UseOutputCache();

```


После этого можно применять кэширование. Рассмотрим простейший пример:

```

var users = new List<string> { "Tom", "Bob", "Sam" };

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddOutputCache(); // добавляем сервисы

var app = builder.Build();

app.UseOutputCache(); // добавляем OutputCacheMiddleware

app.MapGet("/", async () =>
{
 await Task.Delay(5000); // имитация долгой обработки
 return users;
}).CacheOutput(); // применяем кэширование к результату обработки метода app.MapGet("/")

app.Run();

```


Здесь при обращении по адресу "/" приложение будет отдавать список users.

```

app.MapGet("/", async () =>
{
 await Task.Delay(5000); // имитация долгой обработки
 return users;
}).CacheOutput();

```


Для упрощения задачи здесь данные определены локально в виде списка, но в реальности это могут быть данные,
которые приходят из базы данных, с другого сервера с помощью дополнительного сетевого запроса и т.д. А для искусственной имитации долгой обработки запроса я добавил задержку в 5 секунд.
И чтобы при всех последующих обращениях приложение не обрабатывало повторно запрос, применяем кэширование. Для этого к методу `app.MapGet` по цепочке добавляем вызов метода CacheOutput().


### Применение кэширования


Чтобы применить кэширование к результату определенного метода, можно использовать два способа:


-

Вызов метода CacheOutput(), которые определен как метод расширения для типа `IEndpointConventionBuilder`. То есть, как в примере выше, мы можем его
вызвать по цепочке после метода Map/MapGet/MapPost/MapPut/MapDelete/MapPatch и т.д.:

```

app.MapGet("/", () => users).CacheOutput(); // применяем кэширование

```


-

Применение атрибута [CacheOutput] к обработчику конечной точки:

```

using Microsoft.AspNetCore.OutputCaching; // для атрибута [OutputCache]
.....................
app.MapGet("/", [OutputCache]() => users);

```


### Ограничения кэширования


Одна из перегруженных версий метода `AddOutputCache` принимает делегат Action<OutputCacheOptions>, параметр которого - объект OutputCacheOptions с помощью свойств позволяет настроить предельные значения кэширования:


-

SizeLimit: максимальный размер кэш-хранилища. При достижении этого предела новые ответы не будут кэшироваться до тех пор, пока старые записи не будут удалены. Значение по умолчанию — 100 МБ

-

MaximumBodySize: максимальный размер отдельного объекта, помещаемого в кэш. Если ответ превышает этот предел, он не будет кэшироваться. Значение по умолчанию — 64 МБ

-

DefaultExpirationTimeSpan: срок действия, который применяется, если он не указан политикой. Значение по умолчанию — 60 секунд


Пример применения:

```

using Microsoft.AspNetCore.OutputCaching;

var users = new List<string> { "Tom", "Bob", "Sam" };

var builder = WebApplication.CreateBuilder(args);

// переустанавливаем ограничения кэширования
builder.Services.AddOutputCache(o=>
{
 o.MaximumBodySize = 4 * 1024 * 1024; // 4 Мб
 o.SizeLimit = 64 * 1024 * 1024; // 64 Мб
 o.DefaultExpirationTimeSpan = TimeSpan.FromMinutes(2); // 2 минуты
});

var app = builder.Build();

app.UseOutputCache();
app.MapGet("/", () => users).CacheOutput();

app.Run();

```


### Настройка кэширования


Метод `CacheOutput()` имеет ряд перегрузок, которые позволяют настроить кэширование. Рассмотрим одну из них:

```

CacheOutput (Action<Microsoft.AspNetCore.OutputCaching.OutputCachePolicyBuilder> policy)

```


В данную перегрузку в метод передается делегат, который с помощью методов параметра OutputCachePolicyBuilder настраивает опции кэширования. В частности,
мы можем использовать следующие методы OutputCachePolicyBuilder:


-

`Expire (TimeSpan expiration)`: устанавливает время кэширования в виде объекта TimeSpan. После истечения этого времени кэш сбрасывается

-

`SetVaryByHeader (string[] headerNames)`: для каждого набора заголовков, переданных в метод, устанавливает свою версию кэша

-

`SetVaryByHost (bool enabled)`: если в метод передается значение `true`, то для каждого хоста устанавливается своя версия кэша.

-

`SetVaryByQuery (string[] queryKeys)`: устанавливает свою версию кэша для набора параметров строки запроса, которые передаются в метод

-

`SetVaryByRouteValue (string[] routeValueNames)`: : устанавливает свою версию кэша для набора параметров маршрута, которые передаются в метод


Так, в первом примере из статьи кэш сохранялся на протяжении всего приложения, что не очень хорошо, поскольку данные могут измениться. Изменим
код приложения, установив время кэширования:

```

var users = new List<string> { "Tom", "Bob", "Sam" };

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddOutputCache(); // добавляем сервисы

var app = builder.Build();

app.UseOutputCache(); // добавляем OutputCacheMiddleware

// добавляем в список строку, которая передается через параметр маршрута name
app.MapGet("/add/{name}", (string name) =>
{
 users.Add(name);
 return $"{name} has been added";
});

app.MapGet("/", () => users)
 .CacheOutput(t => t.Expire(TimeSpan.FromMinutes(2))); // время кэширования 2 минуты

app.Run();

```


Для тестирования также определена еще одна конечная точка, которая обрабатывает запрос по путь "/add/{name}" - через параметр name передается строка, которая добавляется в список users:

```

app.MapGet("/add/{name}", (string name) =>
{
 users.Add(name);
 return $"{name} has been added";
});

```


Также устанавливаем для кэша время действия в 2 минуты

```

app.MapGet("/", () => users)
 .CacheOutput(t => t.Expire(TimeSpan.FromMinutes(2)));

```


Запустим приложение и сначала обратимся по пути "/", чтобы получить и закэшировать список:
![Установка кэширования ответа и метод OutputCache в ASP.NET Core в C#](https://metanit.com./pics/17.9.png)


И затем, пока идет время кэширования, обратимся по пути "add/Alice", добавив строку "Alice" в список:
![Установка времени кэширования ответа и метод OutputCache в ASP.NET Core в C#](https://metanit.com./pics/17.10.png)


Если время кэширования НЕ истекло, то при повторном обращении по пути "/" мы получим ранее закешированный список без добавленного элемента.
![Установка кэширования ответа и метод OutputCache в ASP.NET Core в C#](https://metanit.com./pics/17.9.png)


После завершения времени кэширования, которое в примере выше равно 2 минутам, мы получим список с уже добавленным элементом, и этот обновленный список также будет закэшировна на 2 минуты
![Установка времени кэширования и метод OutputCache в ASP.NET Core в C#](https://metanit.com./pics/17.11.png)


Подобным образом можно устанавливать и другие параметры кэширования. Например, разграничим кэш для разных значений параметра "username" в строке запроса:

```

app.MapGet("/", () => users)
 .CacheOutput(t => t.SetVaryByQuery("username"));

```


#### Настройка кэширования с помощью атрибута OutputCache


Аналогичную настройку кэширования можно выполнить с помощью свойств атрибута [OutputCache]:


-

`int Duration`: устанавливает время кэширования в секундах

-

`string[]? VaryByHeaderNames`: устанавливает набор заголовоков, для которых создается кэш

-

`string[]? VaryByQueryKeys`: устанавливает набор параметров строки запроса, для которых создается кэш

-

`string[]? VaryByRouteValueNames`: устанавливает набор параметров маршрута, для которых создается кэш


Например, установки кэширования на 2 минуты:

```
app.MapGet("/", [OutputCache(Duration = 120)] () => users);
```


### Метка кэширования и сброс кэша


Метод Tag() типа OutputCachePolicyBuilder позволяет задать для закешированного результата определенную метку:

```

app.MapGet("/", () => users)
 .CacheOutput(t=>
 {
 t.Expire(TimeSpan.FromMinutes(2)); // время кэширования - 2 минуты
 t.Tag("users"); // метка "users"
 });

```


С помощью метки мы сможем удалить кэш в произвольный момент времени:

```

using Microsoft.AspNetCore.OutputCaching;

var users = new List<string> { "Tom", "Bob", "Sam" };

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddOutputCache();

var app = builder.Build();

app.UseOutputCache();

app.MapGet("/add/{name}", (string name) =>
{
 users.Add(name);
 return $"{name} has been added";
});
app.MapGet("/", () => users)
 .CacheOutput(t=>
 {
 t.Expire(TimeSpan.FromMinutes(2));
 t.Tag("users");
 });

// сбрасываем кэш
app.MapGet("/reset", async (IOutputCacheStore cache) =>
{
 // удаляем кэшированный объект с меткой "users"
 await cache.EvictByTagAsync("users", new CancellationToken());
 return "Cache Reset";
});

app.Run();

```


Для удаления из кэша объекта с меткой "users" получаем из коллекции сервисов сервис IOutputCacheStore и у него вызываем метод EvictByTagAsync().
Этот метод в качестве первого параметра принимает метку объекта в кэше, а в качестве второго токен отмены CancellationToken:

```

app.MapGet("/reset", async (IOutputCacheStore cache) =>
{
 // удаляем кэшированный объект с меткой "users"
 await cache.EvictByTagAsync("users", new CancellationToken());
 return "Cache Reset";
});

```


### Установка политики кэширования


Если в приложении множество конечных точек, для которых надо применять одни и те же параметры кэширования, то лучше подобные параметры выделить в отдельную политику.
При этом мы можем настроить одну базовую политику, которая будет действовать глобально и
задать отдельные именованные политики, которые будут применяться при необходимости. Для этого в метод AddOutputCache() передается делегат
`Action<OutputCacheOptions>`. Объект OutputCacheOptions имеет два метода: `AddBasePolicy()` (настраивает базовую политику) и
`AddPolicy` (настраивает именованную политику). Все эти методы в качестве параметра принимают делегат с параметром OutputCachePolicyBuilder, методы которого выше уже были рассмотрены.


#### Настройка базовой политики


По умолчанию в приложении уже определена базовая политика кэширования, которая предусматривает, что


-

Кэшируются только ответы со статусным кодом 200

-

Кэшируются только ответы на запросы типа GET и HEAD

-

Если в ответе устанавливаются куки, то ответ не кэшируется

-

Ответы на аутентифицированные запросы не кэшируются


Настроим базовую политику, например, установим время кэширования в 1 минуту:

```

var users = new List<string> { "Tom", "Bob", "Sam" };

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddOutputCache(options =>
{
 options.AddBasePolicy(builder => builder.Expire(TimeSpan.FromMinutes(1)));
});

var app = builder.Build();

app.UseOutputCache();

app.MapGet("/", () => users).CacheOutput();

app.Run();

```


#### Именованные политики


Наряду с базовой политикой можно определить и именнованные политики:

```

var users = new List<string> { "Tom", "Bob", "Sam" };

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddOutputCache(options =>
{
 options.AddBasePolicy(builder => builder.Expire(TimeSpan.FromMinutes(1)));
 options.AddPolicy("Expire2", builder => builder.Expire(TimeSpan.FromMinutes(2)));
 options.AddPolicy("Expire3", builder =>builder.Expire(TimeSpan.FromMinutes(3)));
});

var app = builder.Build();

app.UseOutputCache();
app.MapGet("/", () => users).CacheOutput("Expire2"); // применяем политику "Expire2"

app.Run();

```


Здесь определены две именнованные политики - "Expire2" и "Expire3", которые устанавливают время действия кэша в 2 и 3 секунду соответственно. Для применения именованной политики
можно использовать специальную перегрузку метода CacheOutput(), которая принимает имя политики. В этом случае именованная политика переопределяет действие базовой.


Также можно установить нужную политику при использовании атрибута OutputCache. Для этого у атрибута есть свойство PolicyName, которое принимает имя
политики:

```
app.MapGet("/", [OutputCache(PolicyName ="Expire2")] () => users);
```












- Глава 1. Введение в ASP.NET Core


 - [Что такое ASP.NET Core](//metanit.com/sharp/aspnet6/1.1.php)

 - [Первое приложение на ASP.NET Core с .NET CLI](//metanit.com/sharp/aspnet6/1.3.php)

 - [Первое приложение в Visual Studio](//metanit.com/sharp/aspnet6/1.2.php)



- Глава 2. Основы в ASP.NET Core


 - [Создание и запуск приложения. WebApplication и WebApplicationBuilder](//metanit.com/sharp/aspnet6/2.1.php)

 - [Конвейер обработки запроса и middleware](//metanit.com/sharp/aspnet6/2.2.php)

 - [Метод Run и определение терминального middleware](//metanit.com/sharp/aspnet6/2.3.php)

 - [HttpResponse. Отправка ответа](//metanit.com/sharp/aspnet6/2.4.php)

 - [HttpRequest. Получение данных запроса](//metanit.com/sharp/aspnet6/2.5.php)

 - [Отправка файлов](//metanit.com/sharp/aspnet6/2.6.php)

 - [Отправка форм](//metanit.com/sharp/aspnet6/2.8.php)

 - [Переадресация](//metanit.com/sharp/aspnet6/2.9.php)

 - [Отправка и получение json](//metanit.com/sharp/aspnet6/2.10.php)

 - [Создание простейшего API](//metanit.com/sharp/aspnet6/2.11.php)

 - [Загрузка файлов на сервер](//metanit.com/sharp/aspnet6/2.12.php)

 - [Метод Use](//metanit.com/sharp/aspnet6/2.7.php)

 - [Создание ветки конвейера. UseWhen и MapWhen](//metanit.com/sharp/aspnet6/2.13.php)

 - [Метод Map](//metanit.com/sharp/aspnet6/2.14.php)

 - [Классы middleware](//metanit.com/sharp/aspnet6/2.15.php)

 - [Построение конвейера обработки запроса](//metanit.com/sharp/aspnet6/2.16.php)

 - [IWebHostEnvironment и окружение](//metanit.com/sharp/aspnet6/2.17.php)



- Глава 3. Dependency Injection


 - [Внедрение зависимостей и IServiceCollection](//metanit.com/sharp/aspnet6/4.1.php)

 - [Создание сервисов](//metanit.com/sharp/aspnet6/4.2.php)

 - [Получение зависимостей](//metanit.com/sharp/aspnet6/4.3.php)

 - [Жизненный цикл зависимостей](//metanit.com/sharp/aspnet6/4.4.php)

 - [Применение сервисов в классах middleware](//metanit.com/sharp/aspnet6/4.5.php)

 - [Scoped-сервисы в singleton-объектах](//metanit.com/sharp/aspnet6/4.6.php)

 - [Множественная регистрация сервисов](//metanit.com/sharp/aspnet6/4.7.php)



- Глава 4. Маршрутизация


 - [Конечные точки. Метод Map](//metanit.com/sharp/aspnet6/3.1.php)

 - [Параметры маршрута](//metanit.com/sharp/aspnet6/3.2.php)

 - [Ограничения маршрутов](//metanit.com/sharp/aspnet6/3.3.php)

 - [Создание ограничений маршрутов](//metanit.com/sharp/aspnet6/3.4.php)

 - [Передача зависимостей в конечные точки](//metanit.com/sharp/aspnet6/3.5.php)

 - [Сопоставление запроса с конечной точкой](//metanit.com/sharp/aspnet6/3.6.php)

 - [Сочетание конечных точек с другими middleware](//metanit.com/sharp/aspnet6/3.7.php)

 - [Получение параметров строки запроса](//metanit.com/sharp/aspnet6/3.8.php)



- Глава 5. Статические файлы


 - [Установка каталога статических файлов. UseStaticFiles](//metanit.com/sharp/aspnet6/5.1.php)

 - [Работа со статическими файлами](//metanit.com/sharp/aspnet6/5.2.php)

 - [Статические файлы и MapStaticAssets](//metanit.com/sharp/aspnet6/5.3.php)



- Глава 6. Конфигурация


 - [Основы конфигурации](//metanit.com/sharp/aspnet6/6.1.php)

 - [Нефайловые провайдеры конфигурации](//metanit.com/sharp/aspnet6/6.2.php)

 - [Конфигурация в файлах JSON, XML и Ini](//metanit.com/sharp/aspnet6/6.3.php)

 - [Конфигурация по умолчанию и объединение конфигураций](//metanit.com/sharp/aspnet6/6.4.php)

 - [Анализ конфигурации](//metanit.com/sharp/aspnet6/6.5.php)

 - [Создание провайдера конфгурации](//metanit.com/sharp/aspnet6/6.6.php)

 - [Проекция конфигурации на классы](//metanit.com/sharp/aspnet6/6.7.php)

 - [Передача конфигурации через IOptions](//metanit.com/sharp/aspnet6/6.8.php)



- Глава 7. Логгирование


 - [Ведение лога и ILogger](//metanit.com/sharp/aspnet6/7.1.php)

 - [Фабрика логгера и провайдеры логгирования](//metanit.com/sharp/aspnet6/7.2.php)

 - [Конфигурация и фильтрация логгирования](//metanit.com/sharp/aspnet6/7.3.php)

 - [Создание провайдера логгирования](//metanit.com/sharp/aspnet6/7.4.php)



- Глава 8. Состояние приложения. Куки. Сессии


 - [HttpContext.Items](//metanit.com/sharp/aspnet6/8.1.php)

 - [Куки](//metanit.com/sharp/aspnet6/8.2.php)

 - [Сессии](//metanit.com/sharp/aspnet6/8.3.php)



- Глава 9. Обработка ошибок


 - [Обработка исключений](//metanit.com/sharp/aspnet6/9.1.php)

 - [Обработка ошибок HTTP](//metanit.com/sharp/aspnet6/9.2.php)



- Глава 10. Results API


 - [Введение в Results API](//metanit.com/sharp/aspnet6/10.1.php)

 - [Отправка текста и json в Results API](//metanit.com/sharp/aspnet6/10.2.php)

 - [Переадресация в Results API](//metanit.com/sharp/aspnet6/10.3.php)

 - [Отправка статусных кодов в Results API](//metanit.com/sharp/aspnet6/10.4.php)

 - [Отправка файлов в Results API](//metanit.com/sharp/aspnet6/10.5.php)

 - [Определение своего типа IResult](//metanit.com/sharp/aspnet6/10.6.php)



- Глава 11. Web API


 - [Пример приложения Web API](//metanit.com/sharp/aspnet6/11.1.php)



- Глава 12. Работа с базой данных и Entity Framework


 - [Подключение Entity Framework](//metanit.com/sharp/aspnet6/12.1.php)

 - [Основные операции с данными в Entity Framework Core](//metanit.com/sharp/aspnet6/12.2.php)



- Глава 13. Аутентификация и авторизация


 - [Введение в аутентификацию и авторизацию](//metanit.com/sharp/aspnet6/13.1.php)

 - [Аутентификация с помощью JWT-токенов](//metanit.com/sharp/aspnet6/13.2.php)

 - [Авторизация с помощью JWT-токенов в клиенте JavaScript](//metanit.com/sharp/aspnet6/13.3.php)

 - [Аутентификация с помощью куки](//metanit.com/sharp/aspnet6/13.4.php)

 - [HttpContext.User, ClaimPrincipal и ClaimsIdentity](//metanit.com/sharp/aspnet6/13.5.php)

 - [ClaimPrincipal и объекты Claim](//metanit.com/sharp/aspnet6/13.6.php)

 - [Авторизация по ролям](//metanit.com/sharp/aspnet6/13.7.php)

 - [Авторизация на основе Claims](//metanit.com/sharp/aspnet6/13.8.php)

 - [Создание ограничений для авторизации](//metanit.com/sharp/aspnet6/13.9.php)



- Глава 14. CORS и кросс-доменные запросы


 - [Подключение CORS в приложении](//metanit.com/sharp/aspnet6/14.1.php)

 - [Конфигурация CORS](//metanit.com/sharp/aspnet6/14.2.php)

 - [Политики CORS](//metanit.com/sharp/aspnet6/14.3.php)

 - [Глобальная и локальная настройка CORS](//metanit.com/sharp/aspnet6/14.4.php)



- Глава 15. URL Rewriting


 - [Введение в URL Rewriting](//metanit.com/sharp/aspnet6/15.1.php)

 - [Правила IIS для URL Rewriting](//metanit.com/sharp/aspnet6/15.2.php)

 - [Применение правил Apache для URL Rewriting](//metanit.com/sharp/aspnet6/15.3.php)

 - [Создание правил URL Rewriting](//metanit.com/sharp/aspnet6/15.4.php)



- Глава 16. Клиентская разработка


 - [Бандлинг и минификация](//metanit.com/sharp/aspnet6/16.1.php)

 - [Пакетный менеджер Libman](//metanit.com/sharp/aspnet6/16.2.php)

 - [Пакетный менеджер NPM](//metanit.com/sharp/aspnet6/16.3.php)



- Глава 17. Кэширование


 - [Кэширование с помощью MemoryCache](//metanit.com/sharp/aspnet6/17.1.php)

 - [Распределенное кэширование. Redis](//metanit.com/sharp/aspnet6/17.2.php)

 - [Сжатие ответа](//metanit.com/sharp/aspnet6/17.3.php)

 - [Кэширование статических файлов](//metanit.com/sharp/aspnet6/17.4.php)

 - [Кэширование ответа и OutputCache](//metanit.com/sharp/aspnet6/17.5.php)



- Глава 18. Мониторинг работоспособности приложения


 - [Health Check Middleware](//metanit.com/sharp/aspnet6/18.1.php)










 [Настройки](//metanit.com/settings.php)




 Помощь сайту


 [Помощь сайту](https://yoomoney.ru/to/410011174743222)



 Юмани:
 410011174743222



 Номер карты:
 4048415020898850











[Вконтакте](https://vk.com/metanit)|
[МАКС](https://max.ru/metanit)|
[Донаты/Помощь сайту](https://metanit.com/donations.php)


Contacts: metanit22@mail.ru


Copyright © Евгений Попов, metanit.com, 2026. Все права защищены.

---

**Источник:** [https://metanit.com/sharp/aspnet6/17.5.php](https://metanit.com/sharp/aspnet6/17.5.php)
