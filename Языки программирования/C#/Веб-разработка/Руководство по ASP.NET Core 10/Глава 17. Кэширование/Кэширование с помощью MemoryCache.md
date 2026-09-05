# Кэширование с помощью MemoryCache

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10|Руководство по ASP.NET Core 10]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 17. Кэширование|Глава 17. Кэширование]] / Кэширование с помощью MemoryCache

[[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 16. Клиентская разработка/Пакетный менеджер NPM|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 17. Кэширование|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 17. Кэширование/Распределенное кэширование. Redis|Вперёд]]

**Дата написания:** 05.09.2026

## Кэширование с помощью MemoryCache

Последнее обновление: 30.11.2022




-

-

-














### Основы кэширования


Кэширование представляет собой сохранение данных в специальном месте для более быстрого доступа к ним в будущем. Применение кэширование
может значительно повысить производительность приложения ASP.NET, существенно уменьшая количество обращений к источникам данных, например, к базам данных.


Когда надо кэшировать данные?


-

Когда данные являются внешними по отношению к приложению (например, приходят из базы данных или другого внешнего источника)

-

Когда данные не часто обновляются, относительно постоянны

-

Когда данные часто используются в приложении


При этом речь не идет о кэшировании всей таблицы базы данных или нескольких таблиц. Это может быть часть таблицы или срез данных, которые попадают под вышеописанные критерии.


Распространенные причины кэширования


-

Кэширование результатов запросов к бд, поскольку обращения к базе данных, как правило, являются узким местом приложения

-

Кэширование при высокой латентности сети. Когда приложение располагается в такой сетевой конфигурации, в которой некоторые аспекты сети замедляют работу приложения.
(например, приложение располагается за файерволом, и валидация входящих и исходящих запросов занимает некоторое время). В этом случае кэш обычно располагается на другом хосте, где подобная
латентность снижается к минимуму.

-

Кэширование для управления состоянием. Кэш может представлять некоторое общее состояние, которое могут использовать различные экземпляры приложений или части одного приложения.


Стратегии кэширования

-

Прекэширование (Pre-caching). Путем анализа разработчик определяет наиболее часто запрашиваемые или данные, которые могут сильно снизить производительность приложения. Подобные данные кэшируются
при старте приложения. Затем после запуска приложения берет подобные данные из кэша вместо запрашивания из внешнего источника. Минус подобного подхода - необходимость
синхронизации с внешним источником данных в случае их обновления, особенно когда приложение и база данных управляются разными командами разработчиков/разными компаниями

-

Кэширование по запросу (On-demand caching). Когда данные необходимы, приложение сначала обращается в кэш, если кэше найдены соответствующие данные,
то они используются (это называется cache hit). Если данные в кэше отстуствуют (это называется cache miss), то приложение извлекает из
базы данных и кэшируют для последующих запросов. Минус стратегии - необходимость делать запрос к бд, который снижает производительность приложения.


### MemoryCache


Самым простым способом кэширования в ASP.NET Core предствляет использование объекта
Microsoft.Extensions.Caching.Memory.IMemoryCache, который позволяет сохранять данные в кэше на сервере. Применяя методы интефейса IMemoryCache, мы можем управлять кэшем:


-

bool TryGetValue(object key, out object value): пытаемся получить элемент по ключу key. При успешном получении параметр
value заполняется полученным элементом, а метод возвращает true

-

object Get(object key): дополнительный метод расширения, который получает по ключу key элемент и возвращает его

-

void Remove(object key): удаляет из кэша элемент по ключу key

-

object Set(object key, object value, MemoryCacheEntryOptions options): добавляет в кэш элемент с ключом key и значением
value, применяя опции кэширования MemoryCacheEntryOptions

-

ICacheEntry CreateEntry(object key): добавляет в кэш или перезаписывает запись с ключом key. Возвращает новую запись


ASP.NET Core предоставляет встроенную реализацию интерфейса IMemoryCache - класс MemoryCache, который используется как реализация по умолчанию для сервиса
IMemoryCache и который инкапсулирует все объекты кэша в виде словаря Dictionary.


Для рассмотрения механизма кэширования возьмем какую-нибудь простенькую задачу. Допустим, нам надо кэшировать профиль пользователя или некоторую информацию
о пользователе, которая может не изменяться в течение более долгого периода времени, и поэтому эту информацию мы можем кэшировать, чтобы в будущем
избежать лишних обращений к бд.


Для простоты и демонстрации в качестве базы данных будем использовать базу данных SQLite, с которой будем работать через Entity Framework.
Поэтому добавим в проект через Nuget пакет Microsoft.EntityFrameworkCore.Sqlite.


Далее определим в файле Program.cs следующий код приложения:

```

using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.Caching.Memory;

var builder = WebApplication.CreateBuilder(args);

// внедрение зависимости Entity Framework
builder.Services.AddDbContext<ApplicationContext>(options => options.UseSqlite("Data Source=usercacheapp.db"));
// внедрение зависимости UserService
builder.Services.AddTransient<UserService>();
// добавление кэширования
builder.Services.AddMemoryCache();
var app = builder.Build();

app.MapGet("/user/{id}", async (int id, UserService userService) =>
{
 User? user = await userService.GetUser(id);
 if (user != null) return $"User {user.Name} Id={user.Id} Age={user.Age}";
 return "User not found";
});
app.MapGet("/", () => "Hello World!");

app.Run();


public class User
{
 public int Id { get; set; }
 public string Name { get; set; } = "";
 public int Age { get; set; }
}
public class ApplicationContext : DbContext
{
 public DbSet<User> Users { get; set; } = null!;
 public ApplicationContext(DbContextOptions<ApplicationContext> options) : base(options) =>
 Database.EnsureCreated();
 protected override void OnModelCreating(ModelBuilder modelBuilder)
 {
 // инициализация БД начальными данными
 modelBuilder.Entity<User>().HasData(
 new User { Id = 1, Name = "Tom", Age = 23 },
 new User { Id = 2, Name = "Alice", Age = 26 },
 new User { Id = 3, Name = "Sam", Age = 28 }
 );
 }
}
public class UserService
{
 ApplicationContext db;
 IMemoryCache cache;
 public UserService(ApplicationContext context, IMemoryCache memoryCache)
 {
 db = context;
 cache = memoryCache;
 }
 public async Task<User?> GetUser(int id)
 {
 // пытаемся получить данные из кэша
 cache.TryGetValue(id, out User? user);
 // если данные не найдены в кэше
 if (user == null)
 {
 // обращаемся к базе данных
 user = await db.Users.FirstOrDefaultAsync(p => p.Id == id);
 // если пользователь найден, то добавляем в кэш - время кэширования 5 минут
 if (user != null)
 {
 Console.WriteLine($"{user.Name} извлечен из базы данных");
 cache.Set(user.Id, user, new MemoryCacheEntryOptions().SetAbsoluteExpiration(TimeSpan.FromMinutes(5)));
 }
 }
 else
 {
 Console.WriteLine($"{user.Name} извлечен из кэша");
 }
 return user;
 }
}

```


Вкратце рассмотрим кода. Прежде всего определяем класс User, который будет описывать используемые данные и объекты которого будут храниться в базе данных SQLite:

```

public class User
{
 public int Id { get; set; }
 public string Name { get; set; } = "";
 public int Age { get; set; }
}

```


Для взаимодействия с базой данных применяется класс контекста данных ApplicationContext:

```

public class ApplicationContext : DbContext
{
 public DbSet<User> Users { get; set; } = null!;
 public ApplicationContext(DbContextOptions<ApplicationContext> options) : base(options) =>
 Database.EnsureCreated();
 protected override void OnModelCreating(ModelBuilder modelBuilder)
 {
 // инициализация БД начальными данными
 modelBuilder.Entity<User>().HasData(
 new User { Id = 1, Name = "Tom", Age = 23 },
 new User { Id = 2, Name = "Alice", Age = 26 },
 new User { Id = 3, Name = "Sam", Age = 28 }
 );
 }
}

```


Для тестирования в методе `OnModelCreating()` инициализируем базу данных тремя объектами.


Для взаимодействия с контекстом данных и кэшем определен класс UserService:

```

public class UserService
{
 ApplicationContext db;
 IMemoryCache cache;
 public UserService(ApplicationContext context, IMemoryCache memoryCache)
 {
 db = context;
 cache = memoryCache;
 }
 public async Task<User?> GetUser(int id)
 {
 // пытаемся получить данные из кэша
 cache.TryGetValue(id, out User? user);
 // если данные не найдены в кэше
 if (user == null)
 {
 // обращаемся к базе данных
 user = await db.Users.FindAsync(id);
 // если пользователь найден, то добавляем в кэш - время кэширования 5 минут
 if (user != null)
 {
 Console.WriteLine($"{user.Name} извлечен из базы данных");
 cache.Set(user.Id, user, new MemoryCacheEntryOptions().SetAbsoluteExpiration(TimeSpan.FromMinutes(5)));
 }
 }
 else
 {
 Console.WriteLine($"{user.Name} извлечен из кэша");
 }
 return user;
 }
}

```


Данный сервис через встроенный механизм внедрения зависимостей будет получать контекст данных и использовать его для взаимодействия с бд. Кроме того,
данный класс реализует логику кэширования - также через механизм внедрения зависимостей в конструкторе мы можем получить объект кэша IMemoryCache.


В методе `GetUser()` сервис UserService получает объект User по id. При получении объекта вначале пытаемся найти этот объект в кэше:

```
cache.TryGetValue(id, out User? user);
```


Здесь ключами элементов в кэше являются значения id, а значения элементов - объекты User. Если ключ в кэше был найден, то в объект user передается извлекаемое из кэша значение, а метод `TryGetValue()` возвращает true


Если в кэше не оказалось объекта, то извлекаем его и бд и затем добавляем в кэш.

```

user = await db.Users.FindAsync(id);
if (user != null)
{
 Console.WriteLine($"{user.Name} извлечен из базы данных");
 cache.Set(user.Id, user, new MemoryCacheEntryOptions().SetAbsoluteExpiration(TimeSpan.FromMinutes(5)));
}

```


Для добавления в кэш в метод `Set()` передаем ключ объекта - его Id, затем передаем само кэшируемое значение - извлеченный из БД объект User. И в конце
для установки времени кэширования применяется метод SetAbsoluteExpiration объекта MemoryCacheEntryOptions, который в данном случае таже устанавливает 5 минут.


#### Регистрация IMemoryCache


Чтобы получить сервис IMemoryCache в приложении его необходимо добавить в коллекцию сервисов с помощью вызова:

```
builder.Services.AddMemoryCache();
```


По сути этот сервис устанавливает зависимость для IMemoryCache, создавая объект синглтон:

```

builder.Services.TryAdd(ServiceDescriptor.Singleton<IMemoryCache, MemoryCache>());

```


И для тестирования определим конечную точку, где клиент передает id через параметр маршрута, и сервис UserService по этому id пытается найти в базе данных и кэше нужный объект User:

```

app.MapGet("/user/{id}", async (int id, UserService userService) =>
{
 User? user = await userService.GetUser(id);
 if (user != null) return $"User {user.Name} Id={user.Id} Age={user.Age}";
 return "User not found";
});

```


Запустим приложение и обратимся по адресу `https://localhost:xxxx/user/1` (то есть для получения объекта User с id=1). В итоге при первом обращении к приложению данные будут извлекаться из базы данных и сохраняться в кэш. При всех последующих обращениях в пределах времени кэширования
(в данном случае в течение 5 минут) данные будут извлекаться из кэша:
![IMemoryCache и кэширование в приложении ASP.NET Core на C#](https://metanit.com./pics/17.1.png)


### MemoryCacheEntryOptions


Для установки параметров кэширования в метод Set() в качестве третьего параметра передается объект MemoryCacheEntryOptions,
который устанавливает настройки кэширования объекта с помощью ряда свойств:


-

`AbsoluteExpiration`: возвращает или задает абсолютную дату окончания кэширования

-

`AbsoluteExpirationRelativeToNow`: возвращает или задает абсолютную дату окончания кэширования относительно текущего момента

-

`ExpirationTokens`: возвращает токены в виде объектов IChangeToken, которые приводят к истечению срока действия записи в кэше.

-

`PostEvictionCallbacks`: возвращает или задает колбеки, которые вызываются после удаления записи из кэша.

-

`Priority`: возвращает или задает приоритет сохранения записи в кэше во время очистки, активируемой при нехватке памяти. Представляет одно из значений перечисления CacheItemPriority.
Значение по умолчанию — `Normal`. Другие значения - High, Low и NeverRemove

-

`Size`: возвращает или задает размер значения записи в кэше.

-

`SlidingExpiration`: возвращает или задает время, в течение которого запись кэша может быть неактивной (то есть к ней нет обращений), прежде чем она будет удалена.
Это значение не увеличивает время существования записи сверх абсолютного срока действия (если он задан).


Применим ряд этих свойств. Для этого изменим в классе UserService следующим образом:

```

public async Task<User?> GetUser(int id)
{
 // пытаемся получить данные из кэша
 cache.TryGetValue(id, out User? user);

 // если данные не найдены в кэше
 if (user == null)
 {
 // обращаемся к базе данных
 user = await db.Users.FindAsync(id);
 // если пользователь найден, то добавляем в кэш
 if (user != null)
 {
 Console.WriteLine($"{user.Name} извлечен из базы данных");

 // определяем параметры кэширования
 var cacheOptions = new MemoryCacheEntryOptions()
 {
 // кэширование в течение 1 минуты
 AbsoluteExpirationRelativeToNow = TimeSpan.FromMinutes(1),
 // низкий приоритет
 Priority = 0,
 };
 // определяем коллбек при удалении записи из кэша
 var callbackRegistration = new PostEvictionCallbackRegistration();
 callbackRegistration.EvictionCallback =
 (object key, object? value, EvictionReason reason, object? state) => Console.WriteLine($"запись {id} устарела");
 cacheOptions.PostEvictionCallbacks.Add( callbackRegistration );

 cache.Set(user.Id, user, cacheOptions);
 }
 }
 else
 {
 Console.WriteLine($"{user.Name} извлечен из кэша");
 }
 return user;
}

```


Стоит отметить, что коллбек вызывается не сразу после окончания срока кэширования записи, а при первом после завершении кэширования обращении к кэшу











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

**Источник:** [https://metanit.com/sharp/aspnet6/17.1.php](https://metanit.com/sharp/aspnet6/17.1.php)
