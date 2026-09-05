# Авторизация с помощью JWT-токенов в клиенте JavaScript

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10|Руководство по ASP.NET Core 10]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 13. Аутентификация и авторизация|Глава 13. Аутентификация и авторизация]] / Авторизация с помощью JWT-токенов в клиенте JavaScript

[[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 13. Аутентификация и авторизация/Аутентификация с помощью JWT-токенов|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 13. Аутентификация и авторизация|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 13. Аутентификация и авторизация/Аутентификация с помощью куки|Вперёд]]

**Дата написания:** 05.09.2026

## Авторизация с помощью JWT-токенов в клиенте JavaScript

Последнее обновление: 10.01.2022




-

-

-














В прошлой статье был рассмотрен процесс конфигурации и генерации JWT-токенов. Теперь посмотрим, как мы можем применить
JWT-токен для авторизации в приложении. Для этого определим в файле Program.cs следующий код:

```

using Microsoft.AspNetCore.Authentication.JwtBearer;
using Microsoft.AspNetCore.Authorization;
using Microsoft.IdentityModel.Tokens;
using System.IdentityModel.Tokens.Jwt;
using System.Security.Claims;
using System.Text;

// условная бд с пользователями
var people = new List<Person>
 {
 new Person("tom@gmail.com", "12345"),
 new Person("bob@gmail.com", "55555")
};

var builder = WebApplication.CreateBuilder();

builder.Services.AddAuthorization();
builder.Services.AddAuthentication(JwtBearerDefaults.AuthenticationScheme)
 .AddJwtBearer(options =>
 {
 options.TokenValidationParameters = new TokenValidationParameters
 {
 ValidateIssuer = true,
 ValidIssuer = AuthOptions.ISSUER,
 ValidateAudience = true,
 ValidAudience = AuthOptions.AUDIENCE,
 ValidateLifetime = true,
 IssuerSigningKey = AuthOptions.GetSymmetricSecurityKey(),
 ValidateIssuerSigningKey = true
 };
});
var app = builder.Build();

app.UseDefaultFiles();
app.UseStaticFiles();

app.UseAuthentication();
app.UseAuthorization();

app.MapPost("/login", (Person loginData) =>
{
 // находим пользователя
 Person? person = people.FirstOrDefault(p => p.Email == loginData.Email && p.Password == loginData.Password);
 // если пользователь не найден, отправляем статусный код 401
 if(person is null) return Results.Unauthorized();

 var claims = new List<Claim> {new Claim(ClaimTypes.Name, person.Email) };
 // создаем JWT-токен
 var jwt = new JwtSecurityToken(
 issuer: AuthOptions.ISSUER,
 audience: AuthOptions.AUDIENCE,
 claims: claims,
 expires: DateTime.UtcNow.Add(TimeSpan.FromMinutes(2)),
 signingCredentials: new SigningCredentials(AuthOptions.GetSymmetricSecurityKey(), SecurityAlgorithms.HmacSha256));
 var encodedJwt = new JwtSecurityTokenHandler().WriteToken(jwt);

 // формируем ответ
 var response = new
 {
 access_token = encodedJwt,
 username = person.Email
 };

 return Results.Json(response);
});
app.Map("/data", [Authorize] () => new { message= "Hello World!" });

app.Run();

public class AuthOptions
{
 public const string ISSUER = "MyAuthServer"; // издатель токена
 public const string AUDIENCE = "MyAuthClient"; // потребитель токена
 const string KEY = "mysupersecret_secretsecretsecretkey!123"; // ключ для шифрации
 public static SymmetricSecurityKey GetSymmetricSecurityKey() =>
 new SymmetricSecurityKey(Encoding.UTF8.GetBytes(KEY));
}

record class Person(string Email, string Password);

```


Для предствления пользователя в приложении здесь определен record-класс Person, который имеет два свойства: email и пароль. И для упрощения ситуации
вместо базы данных все пользователи приложения хранятся в списке `people`. Условно говоря у нас есть два пользователя.


Для описания некоторых настроек генерации токена, как и в прошлой теме, в коде определен специальный класс AuthOptions, и также,
как и в прошлой теме, с помощью метода AddJwtBearer() в приложение добавляется конфигурация токена.


В конечной точке "\login", которая обрабатывает POST-запросы, получаем отправленные клиентом аутентификационные данные опять же для простоты в виде объекта Person:

```

app.MapPost("/login", (Person loginData) =>

```


Используя полученные данные, пытаемся найти в списке people пользователя:

```
Person? person = people.FirstOrDefault(p => p.Email == loginData.Email && p.Password == loginData.Password);
```


Если пользователь не найден, то есть переданы некорректные email и/или пароль, то оправляем статусный код 401, который говорит о том, что доступ запрещен:

```
if(person is null) return Results.Unauthorized();
```


Если пользователь найден, то создается список объектов Claim с одним Claim, который представляет email пользователя. Генерируем jwt-токен:

```

var claims = new List<Claim> {new Claim(ClaimTypes.Name, person.Email) };
var jwt = new JwtSecurityToken(
 issuer: AuthOptions.ISSUER,
 audience: AuthOptions.AUDIENCE,
 claims: claims,
 expires: DateTime.UtcNow.Add(TimeSpan.FromMinutes(2)), // действие токена истекает через 2 минуты
 signingCredentials: new SigningCredentials(AuthOptions.GetSymmetricSecurityKey(), SecurityAlgorithms.HmacSha256));
var encodedJwt = new JwtSecurityTokenHandler().WriteToken(jwt);

```


Далее формирует ответ клиенту. Он отправляется в виде объекта в формате json, который содержит два свойства: `access_token` - собственно токен и
`username` - email аутентифицированного пользователя
var response = new
{
 access_token = encodedJwt,
 username = person.Email
};
return Results.Json(response);

```


Еще одна конечная точка - "/data" использует атрибут Authorize, поэтому для обращения к ней необходимо в запросе отправлять
полученный jwt-токен.

```
app.Map("/data", [Authorize] (HttpContext context) => $"Hello World!");
```


### Создание клиента на javascript


Теперь определим клиент для тестирования авторизации с помощью токена. Итак, в коде приложения определено подключение статических файлов по умолчанию:

```

app.UseDefaultFiles();
app.UseStaticFiles();

```


В качестве веб-страницы по умолчанию добавим в проект для статических файлов папку wwwroot, а в нее - новый файл
index.html:
![Определение клиента для тестирования авторизации с помощью Jwt-токена в ASP.NET Core и C#](https://metanit.com./pics/13.4.png)


В файле index.html определим следующий код:

```

<!DOCTYPE html>
<html>
<head>
 <meta charset="utf-8" />
 <title>METANIT.COM</title>
</head>
<body>
 <div id="userInfo" style="display:none;">
 <p>Добро пожаловать <span id="userName"></span>!</p>
 <input type="button" value="Выйти" id="logOut" />
 </div>
 <div id="loginForm">
 <h3>Вход на сайт</h3>
 <p>
 <label>Введите email</label><br />
 <input type="email" id="email" />
 </p>
 <p>
 <label>Введите пароль</label><br />
 <input type="password" id="password" />
 </p>
 <input type="submit" id="submitLogin" value="Логин" />
 </div>
 <p>
 <input type="submit" id="getData" value="Получить данные" />
 </p>
 <script>
 var tokenKey = "accessToken";
 // при нажатии на кнопку отправки формы идет запрос к /login для получения токена
 document.getElementById("submitLogin").addEventListener("click", async e => {
 e.preventDefault();
 // отправляет запрос и получаем ответ
 const response = await fetch("/login", {
 method: "POST",
 headers: { "Accept": "application/json", "Content-Type": "application/json" },
 body: JSON.stringify({
 email: document.getElementById("email").value,
 password: document.getElementById("password").value
 })
 });
 // если запрос прошел нормально
 if (response.ok === true) {
 // получаем данные
 const data = await response.json();
 // изменяем содержимое и видимость блоков на странице
 document.getElementById("userName").innerText = data.username;
 document.getElementById("userInfo").style.display = "block";
 document.getElementById("loginForm").style.display = "none";
 // сохраняем в хранилище sessionStorage токен доступа
 sessionStorage.setItem(tokenKey, data.access_token);
 }
 else // если произошла ошибка, получаем код статуса
 console.log("Status: ", response.status);
 });

 // кнопка для обращения по пути "/data" для получения данных
 document.getElementById("getData").addEventListener("click", async e => {
 e.preventDefault();
 // получаем токен из sessionStorage
 const token = sessionStorage.getItem(tokenKey);
 // отправляем запрос к "/data
 const response = await fetch("/data", {
 method: "GET",
 headers: {
 "Accept": "application/json",
 "Authorization": "Bearer " + token // передача токена в заголовке
 }
 });

 if (response.ok === true) {
 const data = await response.json();
 alert(data.message);
 }
 else
 console.log("Status: ", response.status);
 });

 // условный выход - просто удаляем токен и меняем видимость блоков
 document.getElementById("logOut").addEventListener("click", e => {

 e.preventDefault();
 document.getElementById("userName").innerText = "";
 document.getElementById("userInfo").style.display = "none";
 document.getElementById("loginForm").style.display = "block";
 sessionStorage.removeItem(tokenKey);
 });
 </script>
</body>
</html>

```


Первый блок на странице выводит информацию о вошедшем пользователе и ссылку для выхода. Второй блок содержит форму для логина.


После нажатия кнопки на форме логина запрос будет отправляться методом POST на адрес "/login". Конечная точка, которая отвечает
за обработку POST-запросов по этому маршруту, если переданы корректные email и пароль, отправит в ответ токен.


Ответом сервера в случае удачной аутентификации будет примерно следующий объект:

```

{
 access_token : "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93
 cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1lIjoicXdlcnR5IiwiaHR0cDovL3NjaGVtYXMub
 Wljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2NsYWltcy9yb2xlIjoidXNlciIsIm5iZi
 I6MTQ4MTYzOTMxMSwiZXhwIjoxNDgxNjM5MzcxLCJpc3MiOiJNeUF1dGhTZXJ2ZXIiLCJhdWQiOiJ
 odHRwOi8vbG9jYWxob3N0OjUxODg0LyJ9.dQJF6pALUZW3wGBANy_tCwk5_NR0TVBwgnxRbblp5Ho",
 username: "tom@gmail.com"
}

```


Параметр `access_token` как раз и будет представлять токен доступа. Также в объекте передается дополнительная информация о нике
пользователя.


Для того, чтобы в коде js данный токен в дальнейшем был доступен, то он сохраняется в хранилище sessionStorage.


Дополнительная кнопка с id="getData" на странице предназначена для тестирования авторизации с помощью токена.
По ее нажатию будет выполняться запрос по адресу "/data", для доступа к которому необходимо быть аутентифицированным.
Чтобы отправить токен в запросе, нам нужно настроить в запросе заголовок Authorization:

```

headers: {
 "Accept": "application/json",
 "Authorization": "Bearer " + token // передача токена в заголовке
}

```


Запустим проект и введем данные одного из пользователя, который есть в списке people:
![Получение токена JWT в клиенте на javascript в ASP.NET Core и C#](https://metanit.com./pics/13.5.png)


При вводе корректных данных север пришлет клиенту объект с jwt-токеном и логином пользователя. И после этого мы можем нажать на кпопку "Получить данные" и тем
самым обратиться к ресурсу "/data", для доступа к которому требуется токен
![Авторизация с помощью jwt-токена из клиента javascript в ASP.NET Core и C#](https://metanit.com./pics/13.6.png)


В то же время если мы попробуем обратиться к этому же ресурсу без токена или с токеном с истекшим сроком, то получим ошибку 401 (Unauthorized).










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

**Источник:** [https://metanit.com/sharp/aspnet6/13.3.php](https://metanit.com/sharp/aspnet6/13.3.php)
