# JWT-токены

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET 5 Core|Руководство по ASP.NET 5 Core]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET 5 Core/Глава 21. Аутентификация и авторизация|Глава 21. Аутентификация и авторизация]] / JWT-токены

[[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET 5 Core/Глава 21. Аутентификация и авторизация/Создание ограничений для политики авторизации|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET 5 Core/Глава 21. Аутентификация и авторизация|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET 5 Core/Глава 22. ASP.NET Core Identity/Введение в ASP.NET Core Identity|Вперёд]]

**Дата написания:** 05.09.2026

## Авторизация с помощью JWT-токенов


Данное руководство устарело. Актуальное руководство: [Руководство по ASP.NET Core 7](https://metanit.com/sharp/aspnet6/)Последнее обновление: 27.12.2019




-

-

-














Общие подходы к авторизации и аутентификации в ASP.NET Core Web API несколько отличаются от того, что мы имеем в MVC. В частности, в Web API механизм авторизации полагается преимущественно
на JWT-токены. Что такое JWT-токен?


JWT (или JSON Web Token) представляет собой веб-стандарт, который определяет способ передачи данных о пользователе в формате JSON в зашифрованном виде.


JWT-токен состоит из трех частей:


-

Header - объект JSON, который содержит информацию о типе токена и алгоритме его шифрования

-

Payload - объект JSON, который содержит данные, нужные для авторизации пользователя

-

Signature - строка, которая создается с помощью секретного кода, Headera и Payload. Эта строка служит для верификации токена


Для использования JWT-токенов создадим новый проект ASP.NET Core по типу Empty.
![JWT Token in ASP.NET Core Web API](https://metanit.com./pics/jwttoken1.png)


Далее добавим в проект папку Models, в которой определим новый класс Person:

```

public class Person
{
 public string Login { get; set; }
 public string Password { get; set; }
 public string Role { get; set; }
}

```


Этот класс будет описывать учетные записи пользователей в приложении.


Для работы с JWT-токенами установим через Nuget пакет Microsoft.AspNetCore.Authentication.JwtBearer.


Также добавим в проект специальный класс AuthOptions, который будет описывать ряд свойств, нужных для генерации токена:

```

using Microsoft.IdentityModel.Tokens;
using System.Text;

namespace TokenApp
{
 public class AuthOptions
 {
 public const string ISSUER = "MyAuthServer"; // издатель токена
 public const string AUDIENCE = "MyAuthClient"; // потребитель токена
 const string KEY = "mysupersecret_secretkey!123"; // ключ для шифрации
 public const int LIFETIME = 1; // время жизни токена - 1 минута
 public static SymmetricSecurityKey GetSymmetricSecurityKey()
 {
 return new SymmetricSecurityKey(Encoding.ASCII.GetBytes(KEY));
 }
 }
}

```


Константа ISSUER представляет издателя токена. Здесь можно определить любое название. AUDIENCE представляет потребителя токена - опять же может быть любая строка,
но в данном случае указан адрес текущего приложения.


Константа KEY хранит ключ, который будет применяться для создания токена.


Для встраивания функциональности JWT-токенов в конвейер обработки запроса используется компонент `JwtBearerAuthenticationMiddleware`.
Так, изменим класс Startup следующим образом:

```

using Microsoft.AspNetCore.Builder;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.AspNetCore.Authentication.JwtBearer;
using Microsoft.IdentityModel.Tokens;

namespace TokenApp
{
 public class Startup
 {
 public void ConfigureServices(IServiceCollection services)
 {
 services.AddAuthentication(JwtBearerDefaults.AuthenticationScheme)
 .AddJwtBearer(options =>
 {
 options.RequireHttpsMetadata = false;
 options.TokenValidationParameters = new TokenValidationParameters
 {
 // укзывает, будет ли валидироваться издатель при валидации токена
 ValidateIssuer = true,
 // строка, представляющая издателя
 ValidIssuer = AuthOptions.ISSUER,

 // будет ли валидироваться потребитель токена
 ValidateAudience = true,
 // установка потребителя токена
 ValidAudience = AuthOptions.AUDIENCE,
 // будет ли валидироваться время существования
 ValidateLifetime = true,

 // установка ключа безопасности
 IssuerSigningKey = AuthOptions.GetSymmetricSecurityKey(),
 // валидация ключа безопасности
 ValidateIssuerSigningKey = true,
 };
 });
 services.AddControllersWithViews();
 }

 public void Configure(IApplicationBuilder app)
 {
 app.UseDeveloperExceptionPage();

 app.UseDefaultFiles();
 app.UseStaticFiles();

 app.UseRouting();

 app.UseAuthentication();
 app.UseAuthorization();

 app.UseEndpoints(endpoints =>
 {
 endpoints.MapDefaultControllerRoute();
 });
 }
 }
}

```


Для установки аутентификации с помощью токенов в методе ConfigureServices в вызов services.AddAuthentication передается значение JwtBearerDefaults.AuthenticationScheme. Далее с помощью метода AddJwtBearer() добавляется конфигурация токена.


Для конфигурации токена применяется объект JwtBearerOptions, который позволяет с помощью свойств настроить работу с токеном. В данном случае использованы следующие свойства:


-

RequireHttpsMetadata: если равно false, то SSL при отправке токена не используется. Однако данный вариант установлен
только дя тестирования. В реальном приложении все же лучше использовать передачу данных по протоколу https.

-

TokenValidationParameters: параметры валидации токена - сложный объект, определяющий, как токен будет валидироваться. Этот объект
в свою очередь имеет множество свойств, которые позволяют настроить различные аспекты валидации токена. Но наиболее важные свойства:
IssuerSigningKey - ключ безопасности, которым подписывается токен, и ValidateIssuerSigningKey - надо ли валидировать ключ безопасности.
Ну и кроме того, можно установить ряд других свойств, таких как нужно ли валидировать издателя и потребителя токена, срок жизни токена, можно установить
название claims для ролей и логинов пользователя и т.д.


Теперь мы можем использовать авторизацию на основе токенов. Однако в прокте пока не предусмотрена генерация токенов. По умолчанию в ASP.NET Core отсутствуют встроенные
возможности для создания токена. И в данном случае мы можем либо воспользоваться сторонними решениями (например,
[IdentityServer](https://github.com/IdentityServer/IdentityServer4) или
[OpenIdDict](https://github.com/openiddict)), либо же создать свой механизм. Выберем второй способ.


Создадим в проекте новую папку Controllers и добавим в нее новый контроллер AccountController:

```

using System;
using System.Collections.Generic;
using System.Linq;
using Microsoft.AspNetCore.Mvc;
using Microsoft.IdentityModel.Tokens;
using System.IdentityModel.Tokens.Jwt;
using System.Security.Claims;
using TokenApp.Models; // класс Person

namespace TokenApp.Controllers
{
 public class AccountController : Controller
 {
 // тестовые данные вместо использования базы данных
 private List<Person> people = new List<Person>
 {
 new Person {Login="admin@gmail.com", Password="12345", Role = "admin" },
 new Person { Login="qwerty@gmail.com", Password="55555", Role = "user" }
 };

 [HttpPost("/token")]
 public IActionResult Token(string username, string password)
 {
 var identity = GetIdentity(username, password);
 if (identity == null)
 {
 return BadRequest(new { errorText = "Invalid username or password." });
 }

 var now = DateTime.UtcNow;
 // создаем JWT-токен
 var jwt = new JwtSecurityToken(
 issuer: AuthOptions.ISSUER,
 audience: AuthOptions.AUDIENCE,
 notBefore: now,
 claims: identity.Claims,
 expires: now.Add(TimeSpan.FromMinutes(AuthOptions.LIFETIME)),
 signingCredentials: new SigningCredentials(AuthOptions.GetSymmetricSecurityKey(), SecurityAlgorithms.HmacSha256));
 var encodedJwt = new JwtSecurityTokenHandler().WriteToken(jwt);

 var response = new
 {
 access_token = encodedJwt,
 username = identity.Name
 };

 return Json(response);
 }

 private ClaimsIdentity GetIdentity(string username, string password)
 {
 Person person = people.FirstOrDefault(x => x.Login == username && x.Password == password);
 if (person != null)
 {
 var claims = new List<Claim>
 {
 new Claim(ClaimsIdentity.DefaultNameClaimType, person.Login),
 new Claim(ClaimsIdentity.DefaultRoleClaimType, person.Role)
 };
 ClaimsIdentity claimsIdentity =
 new ClaimsIdentity(claims, "Token", ClaimsIdentity.DefaultNameClaimType,
 ClaimsIdentity.DefaultRoleClaimType);
 return claimsIdentity;
 }

 // если пользователя не найдено
 return null;
 }
 }
}

```


Для упрощения ситуации данные пользователей определены в виде простого списка. Для поиска пользователя в этом списке по логину и паролю определен метод
`GetIdentity()`, который возвращает объект ClaimsIdentity.


Принцип создания ClaimsIdentity здесь тот же, что и при аутентификации с помощью кук: создается набор объектов Claim, которые включают различные данные о пользователе,
например, логин, роль и т.д.


Для обработки запроса в контроллере создан метод Token, который сопоставлен с маршрутом "/token". Этот метод обрабатывает запросы POST и через
параметры принимает логин и пароль пользователя.


Сам токен представляет объект JwtSecurityToken, для инициализации которого применяются все те же константы и ключ безопасности,
которые определены в классе AuthOptions и которые использовались в классе Startup для настройки JwtBearerAuthenticationMiddleware. Важно, чтобы эти значения совпадали.


С помощью параметра `claims: identity.Claims` в токен добавляются набор объектов Claim, которые содержат информацию о логине и роли пользователя.


Далее посредством метода `JwtSecurityTokenHandler().WriteToken(jwt)` создается Json-представление токена. И в конце он сериализуется и отправляет клиенту с помощью метода `Json()`.


Таким образом генерируется токен.


Для тестирования токена создадим простенький контроллер ValuesController:

```

using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Authorization;

namespace TokenApp.Controllers
{
 [ApiController]
 [Route("api/[controller]")]
 public class ValuesController : Controller
 {
 [Authorize]
 [Route("getlogin")]
 public IActionResult GetLogin()
 {
 return Ok($"Ваш логин: {User.Identity.Name}");
 }

 [Authorize(Roles = "admin")]
 [Route("getrole")]
 public IActionResult GetRole()
 {
 return Ok("Ваша роль: администратор");
 }
 }
}

```


И в конце добавим в проект для статических файлов папку wwwroot, а в нее - новый файл index.html:

```

<!DOCTYPE html>
<html>
<head>
 <meta charset="utf-8" />
 <title>JWT в ASP.NET Core Web API</title>
</head>
<body>
 <div id="userInfo" style="display:none;">
 <p>Вы вошли как: <span id="userName"></span></p>
 <input type="button" value="Выйти" id="logOut" />
 </div>
 <div id="loginForm">
 <h3>Вход на сайт</h3>
 <label>Введите email</label><br />
 <input type="email" id="emailLogin" /> <br /><br />
 <label>Введите пароль</label><br />
 <input type="password" id="passwordLogin" /><br /><br />
 <input type="submit" id="submitLogin" value="Логин" />
 </div>
 <div>
 <input type="submit" id="getDataByLogin" value="Данные по логину" />
 </div>
 <div>
 <input type="submit" id="getDataByRole" value="Данные по роли" />
 </div>

 <script>
 var tokenKey = "accessToken";

 // отпавка запроса к контроллеру AccountController для получения токена
 async function getTokenAsync() {

 // получаем данные формы и фомируем объект для отправки
 const formData = new FormData();
 formData.append("grant_type", "password");
 formData.append("username", document.getElementById("emailLogin").value);
 formData.append("password", document.getElementById("passwordLogin").value);

 // отправляет запрос и получаем ответ
 const response = await fetch("/token", {
 method: "POST",
 headers: {"Accept": "application/json"},
 body: formData
 });
 // получаем данные
 const data = await response.json();

 // если запрос прошел нормально
 if (response.ok === true) {

 // изменяем содержимое и видимость блоков на странице
 document.getElementById("userName").innerText = data.username;
 document.getElementById("userInfo").style.display = "block";
 document.getElementById("loginForm").style.display = "none";
 // сохраняем в хранилище sessionStorage токен доступа
 sessionStorage.setItem(tokenKey, data.access_token);
 console.log(data.access_token);
 }
 else {
 // если произошла ошибка, из errorText получаем текст ошибки
 console.log("Error: ", response.status, data.errorText);
 }
 };
 // отправка запроса к контроллеру ValuesController
 async function getData(url) {
 const token = sessionStorage.getItem(tokenKey);

 const response = await fetch(url, {
 method: "GET",
 headers: {
 "Accept": "application/json",
 "Authorization": "Bearer " + token // передача токена в заголовке
 }
 });
 if (response.ok === true) {

 const data = await response.json();
 alert(data)
 }
 else
 console.log("Status: ", response.status);
 };

 // получаем токен
 document.getElementById("submitLogin").addEventListener("click", e => {

 e.preventDefault();
 getTokenAsync();
 });

 // условный выход - просто удаляем токен и меняем видимость блоков
 document.getElementById("logOut").addEventListener("click", e => {

 e.preventDefault();
 document.getElementById("userName").innerText = "";
 document.getElementById("userInfo").style.display = "none";
 document.getElementById("loginForm").style.display = "block";
 sessionStorage.removeItem(tokenKey);
 });


 // кнопка получения имя пользователя - /api/values/getlogin
 document.getElementById("getDataByLogin").addEventListener("click", e => {

 e.preventDefault();
 getData("/api/values/getlogin");
 });

 // кнопка получения роли - /api/values/getrole
 document.getElementById("getDataByRole").addEventListener("click", e => {

 e.preventDefault();
 getData("/api/values/getrole");
 });
 </script>
</body>
</html>

```


Первый блок на странице выводит информацию о вошедшем пользователе и ссылку для выхода. Второй блок содержит форму для логина.


После нажатия кнопки на форме логина запрос будет отправляться методом POST на адрес "/token". Поскольку за обработку запросов по этому маршруту
отвечает метод Token контроллера AccountController, по результатам работы которого будет формироваться токен.


Ответом сервера в случае удачной аутентификации будет примерно следующий объект:

```

{
 access_token : "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93
 cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1lIjoicXdlcnR5IiwiaHR0cDovL3NjaGVtYXMub
 Wljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2NsYWltcy9yb2xlIjoidXNlciIsIm5iZi
 I6MTQ4MTYzOTMxMSwiZXhwIjoxNDgxNjM5MzcxLCJpc3MiOiJNeUF1dGhTZXJ2ZXIiLCJhdWQiOiJ
 odHRwOi8vbG9jYWxob3N0OjUxODg0LyJ9.dQJF6pALUZW3wGBANy_tCwk5_NR0TVBwgnxRbblp5Ho",
 username: "qwerty@gmail.com"
}

```


Параметр `access_token` как раз и будет представлять токен доступа. Также в объекте передается дополнительная информация о нике
пользователя.


Для того, чтобы в коде js данный токен в дальнейшем был доступен, то он сохраняется в хранилище sessionStorage.


Последние два блока предназначены для отправки запросов к методам ValuesController. Чтобы отправить токен в запросе, нам нужно настроить в запросе заголовок Authorization:

```

headers: {
 "Accept": "application/json",
 "Authorization": "Bearer " + token // передача токена в заголовке
}

```


В итоге весь проект будет выглядеть следующим образом:
![JWT в ASP.NET Core Web API](https://metanit.com./pics/jwttoken2.png)


По ранее сохраненному ключу получаем из хранилища sessionStorage токен и формируем заголовок.


Теперь после получения токена мы можем осуществить запрос к методам контроллера ValuesController:
![Роли в токене JWT в ASP.NET Core Web API](https://metanit.com./pics/jwttoken3.png)


В то же время если мы попробуем обратиться к тем же методам без токена или с токеном с истекшим сроком, то получим ошибку 401 (Unauthorized).










- Глава 1. Введение в ASP.NET Core


 - [ASP.NET Core - новая эпоха в развитии ASP.NET](//metanit.com/sharp/aspnet5/1.1.php)

 - [Начало работы с ASP.NET Core](//metanit.com/sharp/aspnet5/1.2.php)

 - [Проект ASP.NET Core в Visual Studio for Mac](//metanit.com/sharp/aspnet5/1.3.php)



- Глава 2. Основы ASP.NET Core


 - [Запуск приложения. Класс Program](//metanit.com/sharp/aspnet5/2.13.php)

 - [Класс Startup](//metanit.com/sharp/aspnet5/2.1.php)

 - [Конвейер обработки запроса и middleware](//metanit.com/sharp/aspnet5/2.2.php)

 - [Методы Use, Run и делегат RequestDelegate](//metanit.com/sharp/aspnet5/2.3.php)

 - [Методы Map и MapWhen](//metanit.com/sharp/aspnet5/2.22.php)

 - [Создание компонентов middleware](//metanit.com/sharp/aspnet5/2.4.php)

 - [Конвейер обработки запроса](//metanit.com/sharp/aspnet5/2.18.php)

 - [IWebHostEnvironment и окружение](//metanit.com/sharp/aspnet5/2.21.php)

 - [Статические файлы](//metanit.com/sharp/aspnet5/2.5.php)

 - [Работа со статическими файлами](//metanit.com/sharp/aspnet5/2.14.php)

 - [Обработка ошибок](//metanit.com/sharp/aspnet5/17.1.php)

 - [Работа с HTTPS](//metanit.com/sharp/aspnet5/18.6.php)



- Глава 3. Сервисы и Dependency Injection


 - [Сервисы и метод ConfigureServices](//metanit.com/sharp/aspnet5/6.1.php)

 - [Создание своих сервисов](//metanit.com/sharp/aspnet5/2.19.php)

 - [Передача зависимостей](//metanit.com/sharp/aspnet5/6.4.php)

 - [Жизненный цикл зависимостей](//metanit.com/sharp/aspnet5/6.2.php)

 - [Применение сервисов в middleware](//metanit.com/sharp/aspnet5/2.20.php)

 - [Singleton-объекты и scoped-сервисы](//metanit.com/sharp/aspnet5/6.5.php)



- Глава 4. Конфигурация


 - [Основы конфигурации](//metanit.com/sharp/aspnet5/2.6.php)

 - [Нефайловые провайдеры конфигурации](//metanit.com/sharp/aspnet5/2.16.php)

 - [Файловые провайдеры конфигурации](//metanit.com/sharp/aspnet5/2.12.php)

 - [Объединение конфигураций и установка сервиса IConfiguration](//metanit.com/sharp/aspnet5/2.23.php)

 - [Работа с конфигурацией](//metanit.com/sharp/aspnet5/2.17.php)

 - [Создание провайдера конфгурации](//metanit.com/sharp/aspnet5/2.15.php)

 - [Проекция конфигурации на классы](//metanit.com/sharp/aspnet5/2.9.php)

 - [Передача конфигурации через IOptions](//metanit.com/sharp/aspnet5/6.3.php)



- Глава 5. Состояние приложения. Куки. Сессии


 - [HttpContext.Items](//metanit.com/sharp/aspnet5/2.11.php)

 - [Куки](//metanit.com/sharp/aspnet5/2.25.php)

 - [Сессии](//metanit.com/sharp/aspnet5/2.26.php)



- Глава 6. Логгирование


 - [Ведение лога и ILogger](//metanit.com/sharp/aspnet5/2.10.php)

 - [Фабрика логгера и провайдеры логгирования](//metanit.com/sharp/aspnet5/2.29.php)

 - [Конфигурация и фильтрация логгирования](//metanit.com/sharp/aspnet5/2.28.php)

 - [Создание провайдера логгирования](//metanit.com/sharp/aspnet5/2.27.php)



- Глава 7. Маршрутизация


 - [Основы маршрутизации в ASP.NET Core](//metanit.com/sharp/aspnet5/11.1.php)

 - [RouterMiddleware](//metanit.com/sharp/aspnet5/11.12.php)

 - [Определение маршрутов](//metanit.com/sharp/aspnet5/11.2.php)

 - [Работа с маршрутами](//metanit.com/sharp/aspnet5/11.4.php)

 - [Ограничения маршрутов](//metanit.com/sharp/aspnet5/11.3.php)

 - [Создание ограничений маршрутов](//metanit.com/sharp/aspnet5/11.7.php)

 - [Создание своего маршрута](//metanit.com/sharp/aspnet5/11.8.php)



- Глава 8. ASP.NET Core MVC


 - [Введение в ASP.NET Core MVC](//metanit.com/sharp/aspnet5/3.1.php)

 - [Добавление MVC в пустой проект](//metanit.com/sharp/aspnet5/3.6.php)

 - [Первое приложение. Добавление моделей и базы данных](//metanit.com/sharp/aspnet5/3.2.php)

 - [Создание контроллера и инициализатора базы данных](//metanit.com/sharp/aspnet5/3.3.php)

 - [Добавление методов контроллера и представлений](//metanit.com/sharp/aspnet5/3.4.php)

 - [Добавление мастер-страницы и стилизации](//metanit.com/sharp/aspnet5/3.5.php)



- Глава 9. Контроллеры


 - [Контроллеры и их действия](//metanit.com/sharp/aspnet5/5.1.php)

 - [Передача данных в контроллер](//metanit.com/sharp/aspnet5/5.2.php)

 - [Результаты действий](//metanit.com/sharp/aspnet5/5.3.php)

 - [ContentResult и JsonResult](//metanit.com/sharp/aspnet5/5.4.php)

 - [Переадресация](//metanit.com/sharp/aspnet5/5.5.php)

 - [Отправка статусных кодов](//metanit.com/sharp/aspnet5/5.6.php)

 - [Отправка файлов](//metanit.com/sharp/aspnet5/5.7.php)

 - [Переопределение контроллеров](//metanit.com/sharp/aspnet5/5.8.php)

 - [Контекст контроллера](//metanit.com/sharp/aspnet5/5.9.php)

 - [Передача зависимостей в контроллер](//metanit.com/sharp/aspnet5/5.10.php)



- Глава 10. Представления


 - [Введение в представления](//metanit.com/sharp/aspnet5/7.1.php)

 - [Движок представлений Razor](//metanit.com/sharp/aspnet5/7.2.php)

 - [Передача данных в представление](//metanit.com/sharp/aspnet5/7.3.php)

 - [Мастер-страницы](//metanit.com/sharp/aspnet5/7.4.php)

 - [Файл _ViewImports.cshtml](//metanit.com/sharp/aspnet5/7.9.php)

 - [Частичные представления](//metanit.com/sharp/aspnet5/7.5.php)

 - [Внедрение зависимостей в представления](//metanit.com/sharp/aspnet5/7.7.php)

 - [Работа с формами](//metanit.com/sharp/aspnet5/7.8.php)

 - [Создание движка представлений](//metanit.com/sharp/aspnet5/7.10.php)



- Глава 11. Маршрутизация в ASP.NET Core MVC


 - [Маршрутизация в MVC с помощью конечных точек](//metanit.com/sharp/aspnet5/11.5.php)

 - [Маршрутизация с помощью RouterMiddleware. Метод UseMvc](//metanit.com/sharp/aspnet5/11.13.php)

 - [Атрибуты маршрутизации](//metanit.com/sharp/aspnet5/11.6.php)

 - [Области](//metanit.com/sharp/aspnet5/11.9.php)



- Глава 12. Модели


 - [Модели в ASP.NET Core MVC](//metanit.com/sharp/aspnet5/8.1.php)

 - [Модели представления View Model](//metanit.com/sharp/aspnet5/8.2.php)

 - [Привязка модели](//metanit.com/sharp/aspnet5/8.3.php)

 - [Передача данных в контроллер](//metanit.com/sharp/aspnet5/8.4.php)

 - [Управление привязкой](//metanit.com/sharp/aspnet5/8.5.php)

 - [Создание привязчика модели](//metanit.com/sharp/aspnet5/8.6.php)



- Глава 13. HTML-хелперы


 - [Создание HTML-хелперов](//metanit.com/sharp/aspnet5/9.1.php)

 - [HTML-хелперы элементов форм](//metanit.com/sharp/aspnet5/9.2.php)

 - [Строго типизированные хелперы](//metanit.com/sharp/aspnet5/9.3.php)

 - [Шаблонные хелперы](//metanit.com/sharp/aspnet5/9.4.php)

 - [Генерация ссылок](//metanit.com/sharp/aspnet5/9.5.php)

 - [URL-хелперы](//metanit.com/sharp/aspnet5/11.11.php)



- Глава 14. Tag-хелперы


 - [Введение в tag-хелперы](//metanit.com/sharp/aspnet5/10.1.php)

 - [AnchorTagHelper](//metanit.com/sharp/aspnet5/10.2.php)

 - [LinkTagHelper и ScriptTagHelper](//metanit.com/sharp/aspnet5/10.3.php)

 - [Tag-хелперы форм](//metanit.com/sharp/aspnet5/10.4.php)

 - [EnvironmentTagHelper](//metanit.com/sharp/aspnet5/10.6.php)

 - [CacheTagHelper](//metanit.com/sharp/aspnet5/10.7.php)

 - [Создание tag-хелперов](//metanit.com/sharp/aspnet5/10.8.php)

 - [Управление выводом tag-хелпера](//metanit.com/sharp/aspnet5/10.10.php)

 - [Контекст хелпера и получение зависимостей](//metanit.com/sharp/aspnet5/10.11.php)

 - [Атрибут HtmlTargetElement](//metanit.com/sharp/aspnet5/10.12.php)

 - [Tag-хелперы и сложные объекты и коллекции](//metanit.com/sharp/aspnet5/10.9.php)



- Глава 15. View Component


 - [Определение компонента представлений](//metanit.com/sharp/aspnet5/7.6.php)

 - [Передача данных в View Component](//metanit.com/sharp/aspnet5/7.11.php)

 - [Генерация контента в View Component](//metanit.com/sharp/aspnet5/7.12.php)

 - [ViewViewComponentResult и представления](//metanit.com/sharp/aspnet5/7.13.php)

 - [Асинхронные операции в View Component](//metanit.com/sharp/aspnet5/7.14.php)

 - [ViewComponentContext](//metanit.com/sharp/aspnet5/7.15.php)



- Глава 16. Метаданные и валидация модели


 - [Основы валидации](//metanit.com/sharp/aspnet5/19.1.php)

 - [Атрибуты валидации](//metanit.com/sharp/aspnet5/19.2.php)

 - [Валидация на стороне сервера](//metanit.com/sharp/aspnet5/19.3.php)

 - [Валидация на стороне клиента](//metanit.com/sharp/aspnet5/19.4.php)

 - [Tag-хелперы валидации](//metanit.com/sharp/aspnet5/10.5.php)

 - [Создание атрибута валидации. Самовалидация модели](//metanit.com/sharp/aspnet5/19.5.php)

 - [Аннотации данных](//metanit.com/sharp/aspnet5/19.6.php)



- Глава 17. Работа с данными в Entity Framework в MVC


 - [Подключение и создание базы данных в Entity Framework Core](//metanit.com/sharp/aspnet5/12.1.php)

 - [Операции с моделями. Создание и вывод](//metanit.com/sharp/aspnet5/12.2.php)

 - [Операции с моделями. Редактирование и удаление](//metanit.com/sharp/aspnet5/12.3.php)

 - [Сортировка](//metanit.com/sharp/aspnet5/12.4.php)

 - [Создание tag-хелпера сортировки](//metanit.com/sharp/aspnet5/12.5.php)

 - [Фильтрация](//metanit.com/sharp/aspnet5/12.6.php)

 - [Постраничная навигация](//metanit.com/sharp/aspnet5/12.7.php)

 - [Tag-хелпер для постраничной навигации](//metanit.com/sharp/aspnet5/12.8.php)

 - [Объединение сортировки, фильтрации и пагинации](//metanit.com/sharp/aspnet5/12.9.php)

 - [Tag-хелпер пагинации с сортировкой и фильтрацией](//metanit.com/sharp/aspnet5/12.10.php)



- Глава 18. Razor Pages


 - [Введение в Razor Pages](//metanit.com/sharp/aspnet5/29.1.php)

 - [Добавление RazorPages в пустой проект](//metanit.com/sharp/aspnet5/29.2.php)

 - [Обработка запросов. Передача форм](//metanit.com/sharp/aspnet5/29.3.php)

 - [Привязка свойств RazorPage к параметрам запроса](//metanit.com/sharp/aspnet5/29.4.php)

 - [Параметры маршрутов в Razor Pages](//metanit.com/sharp/aspnet5/29.5.php)

 - [Обработчики страницы](//metanit.com/sharp/aspnet5/29.6.php)

 - [Возвращение результата](//metanit.com/sharp/aspnet5/29.7.php)

 - [Переадресация и создание ссылок](//metanit.com/sharp/aspnet5/29.8.php)

 - [Подключение к базе данных](//metanit.com/sharp/aspnet5/29.9.php)

 - [Создание и вывод объектов из базы данных](//metanit.com/sharp/aspnet5/29.10.php)

 - [Изменение и удаление в базе данных](//metanit.com/sharp/aspnet5/29.11.php)



- Глава 19. Web API


 - [Введение в Web API](//metanit.com/sharp/aspnet5/23.1.php)

 - [Создание контроллера](//metanit.com/sharp/aspnet5/23.2.php)

 - [Тестирование контроллера](//metanit.com/sharp/aspnet5/23.3.php)

 - [Создание клиента для WEB API](//metanit.com/sharp/aspnet5/23.4.php)

 - [Валидация в Web API](//metanit.com/sharp/aspnet5/23.5.php)

 - [Content negotiation](//metanit.com/sharp/aspnet5/23.6.php)



- Глава 20. Фильтры


 - [Введение в фильтры](//metanit.com/sharp/aspnet5/18.1.php)

 - [Передача параметров в фильтры и установка зависимостей](//metanit.com/sharp/aspnet5/18.5.php)

 - [Фильтры ресурсов](//metanit.com/sharp/aspnet5/18.2.php)

 - [Фильтры действий](//metanit.com/sharp/aspnet5/18.3.php)

 - [Фильтры результатов](//metanit.com/sharp/aspnet5/18.4.php)

 - [Фильтры исключений](//metanit.com/sharp/aspnet5/17.2.php)

 - [Фильтры RazorPages](//metanit.com/sharp/aspnet5/18.7.php)



- Глава 21. Аутентификация и авторизация


 - [Аутентификация на основе куки. Часть 1](//metanit.com/sharp/aspnet5/15.1.php)

 - [Аутентификация на основе куки. Часть 2](//metanit.com/sharp/aspnet5/15.2.php)

 - [Авторизация](//metanit.com/sharp/aspnet5/15.3.php)

 - [ClaimPrincipal и объекты Claim](//metanit.com/sharp/aspnet5/15.4.php)

 - [Авторизация по ролям](//metanit.com/sharp/aspnet5/15.5.php)

 - [Авторизация на основе Claims](//metanit.com/sharp/aspnet5/15.6.php)

 - [Пример авторизации на основе Claims](//metanit.com/sharp/aspnet5/15.7.php)

 - [Создание ограничений для политики авторизации](//metanit.com/sharp/aspnet5/15.8.php)

 - [JWT-токены](//metanit.com/sharp/aspnet5/23.7.php)



- Глава 22. ASP.NET Core Identity


 - [Введение в ASP.NET Core Identity](//metanit.com/sharp/aspnet5/16.1.php)

 - [Основные классы в ASP.NET Core Identity](//metanit.com/sharp/aspnet5/16.11.php)

 - [Добавление Identity в проект с нуля](//metanit.com/sharp/aspnet5/16.2.php)

 - [Регистрация и создание пользователей в Identity](//metanit.com/sharp/aspnet5/16.3.php)

 - [Авторизация пользователей в Identity](//metanit.com/sharp/aspnet5/16.4.php)

 - [Управление пользователями](//metanit.com/sharp/aspnet5/16.7.php)

 - [Изменение пароля](//metanit.com/sharp/aspnet5/16.8.php)

 - [Валидация пароля](//metanit.com/sharp/aspnet5/16.9.php)

 - [Валидация пользователя](//metanit.com/sharp/aspnet5/16.10.php)

 - [Управление ролями](//metanit.com/sharp/aspnet5/16.13.php)

 - [Инициализация БД ролями и пользователями](//metanit.com/sharp/aspnet5/16.12.php)



- Глава 23. Клиентская разработка


 - [Бандлинг и минификация](//metanit.com/sharp/aspnet5/13.6.php)

 - [Менеджер Libman](//metanit.com/sharp/aspnet5/13.7.php)

 - [Пакетный менеджер NPM](//metanit.com/sharp/aspnet5/13.5.php)

 - [Gulp](//metanit.com/sharp/aspnet5/13.1.php)

 - [Grunt](//metanit.com/sharp/aspnet5/13.2.php)

 - [Препроцессоры Less и Sass](//metanit.com/sharp/aspnet5/13.4.php)



- Глава 24. Производительность и кэширование


 - [Кэширование с помощью MemoryCache](//metanit.com/sharp/aspnet5/14.1.php)

 - [Атрибут ResponseCache](//metanit.com/sharp/aspnet5/14.2.php)

 - [Сжатие ответа](//metanit.com/sharp/aspnet5/14.3.php)

 - [Кэширование статических файлов](//metanit.com/sharp/aspnet5/14.4.php)



- Глава 25. Сервер и публикация приложения


 - [Сервер](//metanit.com/sharp/aspnet5/2.7.php)

 - [Публикация на IIS](//metanit.com/sharp/aspnet5/20.1.php)

 - [Установка приложения в виде службы Windows](//metanit.com/sharp/aspnet5/20.2.php)



- Глава 26. Тестирование


 - [Введение в юнит-тесты](//metanit.com/sharp/aspnet5/22.1.php)

 - [Создание проекта юнит-тестов. Добавление xUnit](//metanit.com/sharp/aspnet5/22.2.php)

 - [Создание юнит-тестов](//metanit.com/sharp/aspnet5/22.3.php)

 - [Фреймворк Moq и moq-объекты](//metanit.com/sharp/aspnet5/22.4.php)

 - [Тестирование контроллера](//metanit.com/sharp/aspnet5/22.5.php)



- Глава 27. URL Rewriting


 - [Введение в URL Rewriting](//metanit.com/sharp/aspnet5/24.1.php)

 - [Правила IIS для URL Rewriting](//metanit.com/sharp/aspnet5/24.2.php)

 - [Применение правил для Apache](//metanit.com/sharp/aspnet5/24.3.php)

 - [Создание правил URL Rewriting](//metanit.com/sharp/aspnet5/24.4.php)



- Глава 28. Глобализация и локализация


 - [Определение культуры](//metanit.com/sharp/aspnet5/28.1.php)

 - [RequestLocalizationMiddleware](//metanit.com/sharp/aspnet5/28.2.php)

 - [Локализация строк. IStringLocalizer](//metanit.com/sharp/aspnet5/28.3.php)

 - [Ресурсы и локализация в контроллерах](//metanit.com/sharp/aspnet5/28.4.php)

 - [Локализация представлений](//metanit.com/sharp/aspnet5/28.5.php)

 - [Локализация аннотаций данных](//metanit.com/sharp/aspnet5/28.6.php)

 - [Переключение языка приложения](//metanit.com/sharp/aspnet5/28.7.php)

 - [Общие ресурсы локализации](//metanit.com/sharp/aspnet5/28.8.php)

 - [Хранение ресурсов в базе данных](//metanit.com/sharp/aspnet5/28.9.php)



- Глава 29. SignalR Core


 - [SignalR Core. Первое приложение](//metanit.com/sharp/aspnet5/30.1.php)

 - [Создание и конфигурация хабов](//metanit.com/sharp/aspnet5/30.2.php)

 - [Клиент javascript](//metanit.com/sharp/aspnet5/30.3.php)

 - [Контекст хаба, подключение и отключение клиентов](//metanit.com/sharp/aspnet5/30.4.php)

 - [Взаимодействие с клиентами](//metanit.com/sharp/aspnet5/30.5.php)

 - [IHubContext](//metanit.com/sharp/aspnet5/30.6.php)

 - [Отправка сложных объектов](//metanit.com/sharp/aspnet5/30.7.php)

 - [Аутентификация и авторизация на основе куки](//metanit.com/sharp/aspnet5/30.8.php)

 - [Аутентификация и авторизация с помощью токенов](//metanit.com/sharp/aspnet5/30.9.php)

 - [Пользователи](//metanit.com/sharp/aspnet5/30.10.php)

 - [Группы](//metanit.com/sharp/aspnet5/30.11.php)

 - [Клиент на Xamarin Forms](//metanit.com/sharp/aspnet5/30.12.php)



- Глава 30. CORS и кросс-доменные запросы


 - [Начало работы с CORS](//metanit.com/sharp/aspnet5/31.1.php)

 - [Конфигурация CORS](//metanit.com/sharp/aspnet5/31.2.php)

 - [Политики CORS](//metanit.com/sharp/aspnet5/31.3.php)

 - [Глобальная и локальная настройка CORS](//metanit.com/sharp/aspnet5/31.5.php)

 - [CORS в MVC](//metanit.com/sharp/aspnet5/31.4.php)



- Глава 31. Dapper


 - [Работа с Dapper в ASP.NET Core](//metanit.com/sharp/aspnet5/26.1.php)



- Глава 32. React.JS


 - [Подключение React в ASP.NET Core](//metanit.com/sharp/aspnet5/25.1.php)

 - [Взаимодействие React.JS и ASP.NET Core](//metanit.com/sharp/aspnet5/25.2.php)



- Глава 33. Дополнительные статьи


 - [Отправка email в ASP.NET Core](//metanit.com/sharp/aspnet5/21.1.php)

 - [Загрузка файлов на сервер](//metanit.com/sharp/aspnet5/21.3.php)










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

**Источник:** [https://metanit.com/sharp/aspnet5/23.7.php](https://metanit.com/sharp/aspnet5/23.7.php)
