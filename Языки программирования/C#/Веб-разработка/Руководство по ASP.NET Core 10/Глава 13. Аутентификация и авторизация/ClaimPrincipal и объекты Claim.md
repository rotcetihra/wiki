# ClaimPrincipal и объекты Claim

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10|Руководство по ASP.NET Core 10]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 13. Аутентификация и авторизация|Глава 13. Аутентификация и авторизация]] / ClaimPrincipal и объекты Claim

[[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 13. Аутентификация и авторизация/HttpContext.User, ClaimPrincipal и ClaimsIdentity|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 13. Аутентификация и авторизация|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 13. Аутентификация и авторизация/Авторизация по ролям|Вперёд]]

**Дата написания:** 05.09.2026

## ClaimPrincipal и объекты Claim

Последнее обновление: 11.01.2022




-

-

-














В прошлой теме был рассмотрен объект `HttpContext.User`, который представляет класс ClaimsPrincipal и который хранит данные пользователя в
свойстве `Identity` в виде объекта `ClaimsIdentity`. Но что представляют сами данные пользователя? Для
хранения различных данных пользователя во фреймворке ASP.NET Core определяются объекты claim.


Объекты claim представляют некоторую информацию о пользователе, которую мы можем использовать для авторизации в приложении. Например,
у пользователя может быть определенный возраст, город, страна проживания, любимая музыкальная группа и прочие признаки. И все эти признаки могут представлять
отдельные объекты claim. И в зависимости от значения этих claim мы можем предоставлять пользователю доступ к тому или иному ресурсу. Таким образом,
claims представляют более общий механизм авторизации нежели стандартные логины или роли, которые привязаны лишь к одному определенному признаку пользователя.


Каждый объект claim представляет класс Claim из пространства имен `System.Security.Claims`, который определяет следующие свойства:


-

Issuer: "издатель" или название системы, которая выдала данный claim

-

Subject: возвращает информацию о пользователе в виде объекта ClaimsIdentity

-

Type: возвращает тип объекта claim

-

Value: возвращает значение объекта claim


### Создание Claim


Для создания объекта Claim определено множество конструкторов, но чаще всего применяется следующая версия конструктора:

```
public Claim(string type, string value)
```


В качестве первого параметра в конструктор передается тип claima - это некоторая строка, которая, как правило, описывает назначение claima.
В качестве второго параметра передается значение этого claima. Например, простейшее создание claima:

```
var usernameClaim = new Claim(ClaimTypes.Name, "Tom");
```


В качестве типов можно использовать встроенные константы, типа `ClaimTypes.Name`,
которая имеет значение "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/name" и которая обычно применяется для установки имени пользователя (то, что потом мы
сможем получить через свойство HttpContext.User.Identity.Name). И в данном случае этот claim будет иметь значение "Tom".


Все объекты claim, которые описывают пользователя, затем можно передать в виде коллекции в конструктор ClaimsIdentity:

```

var usernameClaim = new Claim(ClaimTypes.Name, "Tom");
var claims = new List<Claim> { usernameClaim };
var claimsIdentity = new ClaimsIdentity(claims, "Cookies");

```


Рассмотрим на небольшом примере:

```

using Microsoft.AspNetCore.Authentication.Cookies;
using System.Security.Claims;
using Microsoft.AspNetCore.Authentication;

var builder = WebApplication.CreateBuilder();

builder.Services.AddAuthentication(CookieAuthenticationDefaults.AuthenticationScheme)
 .AddCookie();

var app = builder.Build();

app.UseAuthentication();

app.MapGet("/login/{username}", async (string username, HttpContext context) =>
{
 var claims = new List<Claim> { new (ClaimTypes.Name, username) };
 var claimsIdentity = new ClaimsIdentity(claims, "Cookies");
 var claimsPrincipal = new ClaimsPrincipal(claimsIdentity);
 await context.SignInAsync(claimsPrincipal);
 return $"Установлено имя {username}";
});
app.Map("/", (HttpContext context) =>
{
 var user = context.User.Identity;
 if (user is not null && user.IsAuthenticated)
 return $"UserName: {user.Name}";
 else return "Пользователь не аутентифицирован.";
});
app.MapGet("/logout", async (HttpContext context) =>
{
 await context.SignOutAsync(CookieAuthenticationDefaults.AuthenticationScheme);
 return "Данные удалены";
});

app.Run();

```


В данном примере в конечной точке `app.MapGet("/login/{username}")` через параметр "username" получаем некоторое условное имя
пользователя, создаем из него Claim, передаем его в ClaimsIdentity. В итоге после этот claim будет сохранен в аутентификационных куках. И
когда в следующем запросе приложение получит эти аутентификационные куки, оно сможет извлечь эти данные и использовать их при создании объекта ClaimsPrincipal.
![Установка Claim и HttpContext.User.Identity.Name в ASP.NET Core и C#](https://metanit.com./pics/13.13.png)


Следует отметить, что по умолчанию значение claim с типом `ClaimTypes.Name` (либо `ClaimsIdentity.DefaultNameClaimType`)
передается свойству HttpContext.User.Identity.Name.


### Управление объектами Claim


Для работы с объектами Claim в классе ClaimsPrincipal есть следующие свойства и методы:


-

Claims: свойство, которое возвращает набор ассоциированных с пользователем объектов claim

-

FindAll(type) / FindAll(predicate): возвращает все объекты claim, которые соответствуют определенному типу или условию

-

FindFirst(type) / FindFirst(predicate): возвращает первый объект claim, который соответствуют определенному типу или условию

-

HasClaim(type, value) / HasClaim(predicate): возвращает значение `true`, если пользователь имеет claim определенного типа с определенным значением

-

IsInRole(name): возвращает значение `true`, если пользователь принадлежит роли с названием name


С помощью объекта ClaimsIdentity, который возвращается свойством `User.Identity`, мы можем управлять объектами claim у текущего пользователя.
В частности, класс ClaimsIdentity определяет следующие свойства и методы:


-

Claims: свойство, которое возвращает набор ассоциированных с пользователем объектов claim

-

AddClaim(claim): добавляет для пользователя объект claim

-

AddClaims(claims): добавляет набор объектов claim

-

FindAll(type) / FindAll(predicate): возвращает все объекты claim, которые соответствуют определенному типу или условию

-

FindFirst(type) / FindFirst(predicate): возвращает первый объект claim, который соответствуют определенному типу или условию

-

HasClaim(predicate): возвращает значение `true`, если пользователь имеет claim, соответствующий определенному условию

-

RemoveClaim(claim): удаляет объект claim

-

TryRemoveClaim(claim): удаляет объект claim и возвращает true при успешном удалении


Например, определим у пользователя несколько объектов claim:

```

using Microsoft.AspNetCore.Authentication.Cookies;
using System.Security.Claims;
using Microsoft.AspNetCore.Authentication;

var builder = WebApplication.CreateBuilder();

builder.Services.AddAuthentication(CookieAuthenticationDefaults.AuthenticationScheme)
 .AddCookie();

var app = builder.Build();

app.UseAuthentication();

app.MapGet("/login", async (HttpContext context) =>
{
 var username = "Tom";
 var company = "Microsoft";
 var phone = "+12345678901";

 var claims = new List<Claim>
 {
 new Claim (ClaimTypes.Name, username),
 new Claim ("company", company),
 new Claim(ClaimTypes.MobilePhone,phone)
 };
 var claimsIdentity = new ClaimsIdentity(claims, "Cookies");
 var claimsPrincipal = new ClaimsPrincipal(claimsIdentity);
 await context.SignInAsync(claimsPrincipal);
 return Results.Redirect("/");
});
app.Map("/", (HttpContext context) =>
{
 // аналогично var username = context.User.Identity.Name
 var username = context.User.FindFirst(ClaimTypes.Name);
 var phone = context.User.FindFirst(ClaimTypes.MobilePhone);
 var company = context.User.FindFirst("company");
 return $"Name: {username?.Value}\nPhone: {phone?.Value}\nCompany: {company?.Value}";
});
app.MapGet("/logout", async (HttpContext context) =>
{
 await context.SignOutAsync(CookieAuthenticationDefaults.AuthenticationScheme);
 return "Данные удалены";
});

app.Run();

```


В конечной точке `app.MapGet("/login")` в куки сохраняются объект ClaimsPrincipal с тремя объектами claims. Они представляют имя, компанию и телефон пользователя.
Причем для добавления некоторых claim мы можем воспользоваться встроенными типами, как для имени или телефона пользователя:

```
new Claim(ClaimTypes.MobilePhone,phone)
```


Для других данных мы можем определить свои типы, просто передав какую-нибудь строку, как в случае с компанией:

```
new Claim ("company", company),
```


Затем в приложении при обработке запроса мы можем получить эти данные. Как в примере выше в конечной точке `app.Map("/")`:

```

var phone = context.User.FindFirst(ClaimTypes.MobilePhone);
var company = context.User.FindFirst("company");

```


В метод `FindFirst` передается тип claim. Стоит учитывать, что этот метод возвращает объект `Claim?`, то есть результатом метода
может быть значение null (например, если пользователь не аутентифицирован или объект claim не установлен).
Соответственно при обращении к значению claim необходимо проверять его на null.


Таким образом, после обращения по пути "/login" в куках будут сохранены данные пользователя:
![установка и получение Claim у ClaimsPrincipal в ASP.NET Core и C#](https://metanit.com./pics/13.14.png)


Если мы динамически решим добавить новый claim или удалить существующий, то после изменения claim необходимо заново пересоздавать объект ClaimsPrincipal и
перезаписывать аутентификационные куки или jwt-токен, где эти данные храняться.

```

using Microsoft.AspNetCore.Authentication.Cookies;
using System.Security.Claims;
using Microsoft.AspNetCore.Authentication;

var builder = WebApplication.CreateBuilder();

builder.Services.AddAuthentication(CookieAuthenticationDefaults.AuthenticationScheme)
 .AddCookie();

var app = builder.Build();

app.UseAuthentication();
// Добавление возраста
app.MapGet("/addage", async (HttpContext context) =>
{
 if(context.User.Identity is ClaimsIdentity claimsIdentity)
 {
 claimsIdentity.AddClaim(new Claim("age", "37"));
 var claimsPrincipal = new ClaimsPrincipal(claimsIdentity);
 await context.SignInAsync(claimsPrincipal);
 }
 return Results.Redirect("/");
});
// удаление телефона
app.MapGet("/removephone", async (HttpContext context) =>
{
 if (context.User.Identity is ClaimsIdentity claimsIdentity)
 {
 var phoneClaim = claimsIdentity.FindFirst(ClaimTypes.MobilePhone);
 // если claim успешно удален
 if(claimsIdentity.TryRemoveClaim(phoneClaim))
 {
 var claimsPrincipal = new ClaimsPrincipal(claimsIdentity);
 await context.SignInAsync(claimsPrincipal);
 }
 }
 return Results.Redirect("/");
});
app.MapGet("/login", async (HttpContext context) =>
{
 var username = "Tom";
 var company = "Microsoft";
 var phone = "+12345678901";

 var claims = new List<Claim>
 {
 new Claim (ClaimTypes.Name, username),
 new Claim ("company", company),
 new Claim(ClaimTypes.MobilePhone,phone)
 };
 var claimsIdentity = new ClaimsIdentity(claims, "Cookies");
 var claimsPrincipal = new ClaimsPrincipal(claimsIdentity);
 await context.SignInAsync(claimsPrincipal);
 return Results.Redirect("/");
});
app.Map("/", (HttpContext context) =>
{
 var username = context.User.FindFirst(ClaimTypes.Name);
 var phone = context.User.FindFirst(ClaimTypes.MobilePhone);
 var company = context.User.FindFirst("company");
 var age = context.User.FindFirst("age");
 return $"Name: {username?.Value}\nPhone: {phone?.Value}\n" +
 $"Company: {company?.Value}\nAge: {age?.Value}";
});
app.MapGet("/logout", async (HttpContext context) =>
{
 await context.SignOutAsync(CookieAuthenticationDefaults.AuthenticationScheme);
 return "Данные удалены";
});

app.Run();

```


В данном случае конечная точка `app.MapGet("/removephone")` удаляет телефон, а `app.MapGet("/addage")` добавляет возвраст в claims


Если нам надо сохранить набор значений, то все они передаются по одному типу. Затем с помощью метода `FindAll()` можно получить список этих значений.
Например, сохраним для пользователя набор иностранных языков:

```

using Microsoft.AspNetCore.Authentication.Cookies;
using System.Security.Claims;
using Microsoft.AspNetCore.Authentication;

var builder = WebApplication.CreateBuilder();

builder.Services.AddAuthentication(CookieAuthenticationDefaults.AuthenticationScheme)
 .AddCookie();

var app = builder.Build();

app.UseAuthentication();

app.MapGet("/login", async (HttpContext context) =>
{
 var claims = new List<Claim>
 {
 new Claim (ClaimTypes.Name, "Tom"),
 new Claim ("languages", "English"),
 new Claim ("languages", "German"),
 new Claim ("languages", "Spanish")
 };
 var claimsIdentity = new ClaimsIdentity(claims, "Cookies");
 var claimsPrincipal = new ClaimsPrincipal(claimsIdentity);
 await context.SignInAsync(claimsPrincipal);
 return Results.Redirect("/");
});
app.Map("/", (HttpContext context) =>
{
 var username = context.User.FindFirst(ClaimTypes.Name);
 var languages = context.User.FindAll("languages");
 // объединяем список claims в строку
 var languagesToString = "";
 foreach (var l in languages)
 languagesToString = $"{languagesToString} {l.Value}";
 return $"Name: {username?.Value}\nLanguages: {languagesToString}";
});
app.MapGet("/logout", async (HttpContext context) =>
{
 await context.SignOutAsync(CookieAuthenticationDefaults.AuthenticationScheme);
 return "Данные удалены";
});

app.Run();

```

![сохранение в Claim массивов в ASP.NET Core и C#](https://metanit.com./pics/13.15.png)










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

**Источник:** [https://metanit.com/sharp/aspnet6/13.6.php](https://metanit.com/sharp/aspnet6/13.6.php)
