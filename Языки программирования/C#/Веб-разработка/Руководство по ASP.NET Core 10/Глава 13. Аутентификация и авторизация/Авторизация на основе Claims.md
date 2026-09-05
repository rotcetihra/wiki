# Авторизация на основе Claims

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10|Руководство по ASP.NET Core 10]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 13. Аутентификация и авторизация|Глава 13. Аутентификация и авторизация]] / Авторизация на основе Claims

[[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 13. Аутентификация и авторизация/Авторизация по ролям|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 13. Аутентификация и авторизация|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 13. Аутентификация и авторизация/Создание ограничений для авторизации|Вперёд]]

**Дата написания:** 05.09.2026

## Авторизация на основе Claims

Последнее обновление: 12.01.2022




-

-

-














Атрибут Authorize легко позволяет разграничить доступ в зависимости от роли, однако для создания авторизации
функциональности ролей бывает недостаточно. Например, что если мы хотим разграничить доступ на основе
возраста пользователя или каких-то других признаков. Для этого применяется авторизация на основе claims. Собственно авторизация на основе ролей фактически представляет
частный случай авторизации на основе claims, так как роль это тот же объект Claim, имеющий тип `ClaimsIdentity.DefaultRoleClaimType`.


Для авторизации на основе claims используются политики (policy). Политика представляет набор ограничений, которым должен соответствовать
пользователь для доступа к ресурсу.


Все применяемые политики добавляются в приложение с помощью метода `builder.Services.AddAuthorization()`.
Этот метод устанавливает политики с помощью объекта AuthorizationOptions. Например:

```

builder.Services.AddAuthorization(opts => {

 opts.AddPolicy("OnlyForMicrosoft", policy => {
 policy.RequireClaim("company", "Microsoft");
 });
});

```


В данном случае добавляется политика с именем "OnlyForMicrosoft". И она требует обязательной установки для текущего пользователя объекта Claim с
типом "company" и значением "Microsoft". Если для пользователя не будет установлено подобного объекта Claim, то такой пользователь не будет соответствовать политике.


Для управления политиками в классе AuthorizationOptions определены следующие свойства и методы:


-

DefaultPolicy: возвращает политику по умолчанию, которая используется, когда атрибут Authorize применяется без параметров

-

AddPolicy(name, policyBuilder): добавляет политику

-

GetPolicy(name): возвращает политику по имени


Ключевым методом здесь является `AddPolicy()`. Первый параметр метода представляет название политики, а второй - делегат, который с помощью
объекта AuthorizationPolicyBuilder позволяет создать политику по определенным условиям. Для создания политики могут применяться
следующие методы класса AuthorizationPolicyBuilder:


-

RequireAuthenticatedUser(): пользователь обязательно должен быть аутентифицирован для соответствия политике

-

RequireClaim(type): для пользователя должен быть установлен claim с типом type. Причем не важно, какое значение будет иметь этот claim, главное, его наличие

-

RequireClaim(type, values): для пользователя должен быть установлен claim с типом type. Но теперь claim должен в качестве значения иметь одно из значений из массива values.

-

RequireRole(roles): пользователь должен принадлежать к одной из ролей из массива roles

-

RequireUserName(name): для соответствия политике пользователь должен иметь ник (логин) name

-

RequireAssertion(handler): запрос должен соответствовать условию, которое устанавливается с помощью делегата handler

-

AddRequirements(requirement): позволяет добавить кастомное ограничение requirement, если имеющихся недостаточно


Фактически данные методы задают ограничения, которым должен соответствовать пользователь, обращающийся к приложению. После установки ограничений политики в
атрибуте Authorize можем их применять для разграничения доступа:

```
[Authorize(Policy = "OnlyForMicrosoft")]
```


Для установки политики у атрибута AuthorizeAttribute применяется свойство Policy. Оно указывает на название политики, которой
должны соответствовать пользователи.


### Применение авторизации на основе Claims


Допустим, у нас есть следующий класс, который представляет пользователя:

```

record class Person(string Email, string Password, string City, string Company);

```


У класса Person кроме свойств для хранения email и пароля также определено свойство City для хранения города и свойство Company для хранения компании
пользователя.


Определим в приложении авторизацию на основе свойств City и Company. Для этого изменим код файла Program.cs следующим
образом:

```

using Microsoft.AspNetCore.Authentication.Cookies;
using System.Security.Claims;
using Microsoft.AspNetCore.Authentication;
using Microsoft.AspNetCore.Authorization;

var people = new List<Person>
{
 new Person("tom@gmail.com", "12345", "London", "Microsoft"),
 new Person("bob@gmail.com", "55555", "Лондон", "Google"),
 new Person("sam@gmail.com", "11111", "Berlin", "Microsoft")
};

var builder = WebApplication.CreateBuilder();
builder.Services.AddAuthentication(CookieAuthenticationDefaults.AuthenticationScheme)
 .AddCookie(options =>
 {
 options.LoginPath = "/login";
 options.AccessDeniedPath = "/login";
 });
builder.Services.AddAuthorization(opts => {

 opts.AddPolicy("OnlyForLondon", policy => {
 policy.RequireClaim(ClaimTypes.Locality, "Лондон", "London");
 });
 opts.AddPolicy("OnlyForMicrosoft", policy => {
 policy.RequireClaim("company", "Microsoft");
 });
});

var app = builder.Build();

app.UseAuthentication();
app.UseAuthorization();

app.MapGet("/login", async (HttpContext context) =>
{
 context.Response.ContentType = "text/html; charset=utf-8";
 // html-форма для ввода логина/пароля
 string loginForm = @"<!DOCTYPE html>
 <html>
 <head>
 <meta charset='utf-8' />
 <title>METANIT.COM</title>
 </head>
 <body>
 <h2>Login Form</h2>
 <form method='post'>
 <p>
 <label>Email</label><br />
 <input name='email' />
 </p>
 <p>
 <label>Password</label><br />
 <input type='password' name='password' />
 </p>
 <input type='submit' value='Login' />
 </form>
 </body>
 </html>";
await context.Response.WriteAsync(loginForm);
});

app.MapPost("/login", async (string? returnUrl, HttpContext context) =>
{
 // получаем из формы email и пароль
 var form = context.Request.Form;
 // если email и/или пароль не установлены, посылаем статусный код ошибки 400
 if (!form.ContainsKey("email") || !form.ContainsKey("password"))
 return Results.BadRequest("Email и/или пароль не установлены");
 string email = form["email"];
 string password = form["password"];

 // находим пользователя
 Person? person = people.FirstOrDefault(p => p.Email == email && p.Password == password);
 // если пользователь не найден, отправляем статусный код 401
 if (person is null) return Results.Unauthorized();
 var claims = new List<Claim>
 {
 new Claim(ClaimTypes.Name, person.Email),
 new Claim(ClaimTypes.Locality, person.City),
 new Claim("company", person.Company)
 };
 var claimsIdentity = new ClaimsIdentity(claims, "Cookies");
 var claimsPrincipal = new ClaimsPrincipal(claimsIdentity);
 await context.SignInAsync(claimsPrincipal);
 return Results.Redirect(returnUrl ?? "/");
});
// доступ только для City = London
app.Map("/london", [Authorize(Policy = "OnlyForLondon")]() => "You are living in London");

// доступ только для Company = Microsoft
app.Map("/microsoft", [Authorize(Policy = "OnlyForMicrosoft")]() => "You are working in Microsoft");

app.Map("/", [Authorize](HttpContext context) =>
{
 var login = context.User.FindFirst(ClaimTypes.Name);
 var city = context.User.FindFirst(ClaimTypes.Locality);
 var company = context.User.FindFirst("company");
 return $"Name: {login?.Value}\nCity: {city?.Value}\nCompany: {company?.Value}";
});
app.MapGet("/logout", async (HttpContext context) =>
{
 await context.SignOutAsync(CookieAuthenticationDefaults.AuthenticationScheme);
 return "Данные удалены";
});

app.Run();

record class Person(string Email, string Password, string City, string Company);

```


Здесь для тестирования механизма авторизации на основе Claims определена условная бд - список пользователей people:

```

var people = new List<Person>
{
 new Person("tom@gmail.com", "12345", "London", "Microsoft"),
 new Person("bob@gmail.com", "55555", "Лондон", "Google"),
 new Person("sam@gmail.com", "11111", "Berlin", "Microsoft")
};

```


Для настройки авторизации в зависимости от данных пользователя в делегате в методе AddAuthorization устанавливаются две политики доступа - "OnlyForLondon" и "OnlyForMicrosoft":

```

builder.Services.AddAuthorization(opts => {

 opts.AddPolicy("OnlyForLondon", policy => {
 policy.RequireClaim(ClaimTypes.Locality, "Лондон", "London");
 });
 opts.AddPolicy("OnlyForMicrosoft", policy => {
 policy.RequireClaim("company", "Microsoft");
 });
});

```


Политика "OnlyForLondon" требует, чтобы claim с типом `ClaimTypes.Locality` имел значение "London" или "Лондон".
Если значений много, то мы их можем перечислить через запятую. Вторая политика - "OnlyForMicrosoft" требует наличия Claim с типом
"company" и значением "Microsoft".


Для входа пользователей в приложение определена конечная точка `app.MapGet("/login")`, которая обрабатывает
GET-запросы по пути "/login" и отправляет пользователям форму для ввода логина и пароля.


После заполнения и отправки формы логина данные в POST-запросе получает конечная точка `app.MapPost("/login")`,
которая получает логин и пароль и по них находит пользователя в списке people. Значения свойств найденного пользователя добавляются в список claims:

```

var claims = new List<Claim>
{
 new Claim(ClaimTypes.Name, person.Email),
 new Claim(ClaimTypes.Locality, person.City),
 new Claim("company", person.Company)
};
var claimsIdentity = new ClaimsIdentity(claims, "Cookies");
var claimsPrincipal = new ClaimsPrincipal(claimsIdentity);

```


Благодаря этому инфраструктура ASP.NET Core сможет получить значения claims с типами `ClaimTypes.Locality` и
`"company"` (то есть соответственно город и компанию пользователей) и на их основе решить, предоставлять ли доступ пользователю к ресурсам приложения,
которые используют политику доступа на основе этих Claim.


Для тестирования политик доступа определены две конечных точки:

```

// доступ только для City = London
app.Map("/london", [Authorize(Policy = "OnlyForLondon")]() => "You are living in London");

// доступ только для Company = Microsoft
app.Map("/microsoft", [Authorize(Policy = "OnlyForMicrosoft")]() => "You are working in Microsoft");

```


Здесь доступ по пути `"/london"` имеют только те пользователи, которые удовлетворяют политике "OnlyForLondon".
А ресурс `"/microsoft"` доступен только для пользователей, соответствующих политике "OnlyForMicrosoft".


Запустим проект и залогинимся, используя данные одного из пользователей из списка people:
![Авторизация на основе Claims в ASP.NET Core и C#](https://metanit.com./pics/13.19.png)


И если пользователь живет в Лондоне, то он имеет доступ по пути "/london". Аналогично если пользователь работает в Microsoft,
он имеет доступ по пути "/microsoft":
![Claims based authorization in ASP.NET Core и C#](https://metanit.com./pics/13.20.png)










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

**Источник:** [https://metanit.com/sharp/aspnet6/13.8.php](https://metanit.com/sharp/aspnet6/13.8.php)
