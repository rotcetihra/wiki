# HttpContext.User, ClaimPrincipal и ClaimsIdentity

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10|Руководство по ASP.NET Core 10]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 13. Аутентификация и авторизация|Глава 13. Аутентификация и авторизация]] / HttpContext.User, ClaimPrincipal и ClaimsIdentity

[[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 13. Аутентификация и авторизация/Аутентификация с помощью куки|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 13. Аутентификация и авторизация|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 13. Аутентификация и авторизация/ClaimPrincipal и объекты Claim|Вперёд]]

**Дата написания:** 05.09.2026

## HttpContext.User, ClaimPrincipal и ClaimsIdentity

Последнее обновление: 11.01.2022




-

-

-














### Классы ClaimPrincipal и ClaimsIdentity и их роль в аутентификации


Одной из задач аутентификации в приложении ASP.NET Core является установка пользователя, который представлен в приложении свойством
User класса HttpContext:

```
public abstract System.Security.Claims.ClaimsPrincipal User { get; set; }
```


Данное свойство предоставляет класс ClaimsPrincipal из пространства имен System.Security.Claims


Непосредственно данные, которые идентифицируют пользователя (его идентичность) хранятся в свойстве Identity класса ClaimPrincipal:

```

public virtual System.Security.Principal.IIdentity? Identity { get; }

```


Это свойство представляет основную идентичность текущего пользователя. Но поскольку с одним пользователем может быть связан набор идентичностей, то также в классе определено свойство Identities:

```

public virtual IEnumerable<ClaimsIdentity> Identities { get; }

```


Свойство Identity представляет интерфейс IIdentity, и, как правило, в качестве такой реализации применяется класс
ClaimsIdentity.


Объект `IIdentity`, в свою очередь, предоставляет информацию о текущем пользователе через следующие свойства:


-

AuthenticationType: тип аутентификации в строковом виде

-

IsAuthenticated: возвращает `true`, если пользователь аутентифицирован

-

Name: возвращает имя пользователя. Обычно в качестве подобного имени используется логин, по которому пользователь входит в приложение


Для создания объекта ClaimsIdentity можно применять ряд конструкторов, но, для того, чтобы пользователь был аутентифицирован, необходимо, как минимум, предоставить
тип аутентификации, которая передается через конструктор. Тип аутентификации представляет произвольную строку, которая описывает некоторым образом способ аутентификации. Например:

```
var identity = new ClaimsIdentity("Cookies");
```


В данном случае в тип аутентификации называется "Cookies".


Для установки идентичности пользователя объект ClaimsIdentity можно передать в ClaimsPrincipal либо через конструктор, либо через метод AddIdetity():

```

var identity = new ClaimsIdentity("Undefined");
var principal = new ClaimsPrincipal(identity);

```


На примере аутентификации куки посмотрим на применение ClaimsPrincipal и ClaimsIdentity:

```

using Microsoft.AspNetCore.Authentication.Cookies;
using System.Security.Claims;
using Microsoft.AspNetCore.Authentication;

var builder = WebApplication.CreateBuilder();

// аутентификация с помощью куки
builder.Services.AddAuthentication(CookieAuthenticationDefaults.AuthenticationScheme)
 .AddCookie();

var app = builder.Build();

app.UseAuthentication();

app.MapGet("/login", async (HttpContext context) =>
{
 var claimsIdentity = new ClaimsIdentity("Undefined");
 var claimsPrincipal = new ClaimsPrincipal(claimsIdentity);
 // установка аутентификационных куки
 await context.SignInAsync(claimsPrincipal);
 return Results.Redirect("/");
});

app.MapGet("/logout", async (HttpContext context) =>
{
 await context.SignOutAsync(CookieAuthenticationDefaults.AuthenticationScheme);
 return "Данные удалены";
});
app.Map("/", (HttpContext context) =>
{
 var user = context.User.Identity;
 if (user is not null && user.IsAuthenticated)
 {
 return $"Пользователь аутентифицирован. Тип аутентификации: {user.AuthenticationType}";
 }
 else
 {
 return "Пользователь НЕ аутентифицирован";
 }
});

app.Run();

```


Здесь в конечной точке `app.MapGet("/login")` создается идентичность claimsIdentity - объект ClaimsIdentity с типом аутентификации "Undefined".
Далее создается объект ClaimsPrincipal, который принимает идентичность claimsIdentity. Созданный объект claimsPrincipal затем передается в метод `context.SignInAsync()`,
который, используя этот объект, устанавливает аутентификационные куки. И в конце происходит редирект на путь "/".


Конечная точка `app.Map("/")` получает через механизм внедрения зависимостей текущего пользователя через свойство
`context.User`. Фактически это тот самый объект ClaimsPrincipal, созданный выше и сохраненный в куках. И когда приходит запрос к приложению,
инфраструктура ASP.NET Core дешифрует и десериализует данные запроса и создает по ним объект ClaimsPrincipal, который хранится в свойстве context.User.
Если используется аутентификация на основе куки (как в примере выше), то данные о пользователе будут извлекаться из аутентификационных кук.
Если применяются jwt-токены, то данные берутся из полученного токена. Причем даже если аутентификационных куки или токена в запросе нет, то объект
ClaimsPrincipal все равно будет создаваться.


Получив идентичность пользователя, мы можем получить различную информацию о нем. Например, проверить, аутентифирован ли он, получить тип аутентификации,
получить другую связанную с ним информацию.


Таким образом, при первом обращении к приложению, когда у нас не установлено никаких аутентификационных кук, пользователь из context.User не аутентифицирован:
![ClaimsPrincipal и ClaimsIdentity в ASP.NET Core и C#](https://metanit.com./pics/13.11.png)


Но после перехода по пути "/login" будут созданы объекты ClaimsPrincipal и ClaimsIdentity и по ним будут установлены аутентификационные куки. Соответственно при повторном переходе по пути "/"
пользователь будет аутентифицирован:
![установка HttpContext.User и ClaimsPrincipal и ClaimsIdentity в ASP.NET Core и C#](https://metanit.com./pics/13.12.png)


### Получение ClaimsPrincipal


Поскольку объект HttpContext доступен через механизм внедрения зависимостей в любой точке приложения, то мы можем через этот объект получить
пользователя, как в примере выше. Однако, если нам нужно только свойство User, а не весь объект HttpContext, то мы можем также через механизм внедрения
зависимостей получить сервис ClaimsPrincipal, который будет аналогичен свойству context.User:

```

app.Map("/", (ClaimsPrincipal claimsPrincipal) =>
{
 var user = claimsPrincipal.Identity;
 if (user is not null && user.IsAuthenticated)
 return "Пользователь аутентифицирован";
 else return "Пользователь не аутентифицирован";
});

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

**Источник:** [https://metanit.com/sharp/aspnet6/13.5.php](https://metanit.com/sharp/aspnet6/13.5.php)
