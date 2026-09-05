# Аутентификация с помощью JWT-токенов

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10|Руководство по ASP.NET Core 10]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 13. Аутентификация и авторизация|Глава 13. Аутентификация и авторизация]] / Аутентификация с помощью JWT-токенов

[[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 13. Аутентификация и авторизация/Введение в аутентификацию и авторизацию|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 13. Аутентификация и авторизация|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 13. Аутентификация и авторизация/Авторизация с помощью JWT-токенов в клиенте JavaScript|Вперёд]]

**Дата написания:** 05.09.2026

## Аутентификация с помощью JWT-токенов

Последнее обновление: 22.05.2025




-

-

-














Одним из подходов к авторизации и аутентификации в ASP.NET Core представляет механизм аутентификации и авторизации с помощью
JWT-токенов. Что такое JWT-токен? JWT (или JSON Web Token) представляет собой веб-стандарт, который определяет способ передачи данных о
пользователе в формате JSON в зашифрованном виде.


JWT-токен состоит из трех частей:


-

Header - объект JSON, который содержит информацию о типе токена и алгоритме его шифрования

-

Payload - объект JSON, который содержит данные, нужные для авторизации пользователя

-

Signature - строка, которая создается с помощью секретного кода, Headera и Payload. Эта строка служит для верификации токена


Для использования JWT-токенов в проект ASP.NET Core необходимо добавить Nuget-пакет Microsoft.AspNetCore.Authentication.JwtBearer. Это можно сделать с помощью .NET CLI с помощью команды

```
dotnet add package Microsoft.AspNetCore.Authentication.JwtBearer
```


Либо, если работа идет в Visual Studio, графически:
![JWT Token in ASP.NET Core Minimal API и C#](https://metanit.com./pics/13.1.png)


Сначала рассмотрим принцип генерации и отправки jwt-токена. Для этого в файле Program.cs определим следующий код приложения:

```

using Microsoft.AspNetCore.Authentication.JwtBearer;
using Microsoft.AspNetCore.Authorization;
using Microsoft.IdentityModel.Tokens;
using System.IdentityModel.Tokens.Jwt;
using System.Security.Claims;
using System.Text;

var builder = WebApplication.CreateBuilder();

builder.Services.AddAuthorization();
builder.Services.AddAuthentication(JwtBearerDefaults.AuthenticationScheme)
 .AddJwtBearer(options =>
 {
 options.TokenValidationParameters = new TokenValidationParameters
 {
 // указывает, будет ли валидироваться издатель при валидации токена
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
var app = builder.Build();

app.UseAuthentication();
app.UseAuthorization();

app.Map("/login/{username}", (string username) =>
{
 var claims = new List<Claim> {new Claim(ClaimTypes.Name, username) };
 // создаем JWT-токен
 var jwt = new JwtSecurityToken(
 issuer: AuthOptions.ISSUER,
 audience: AuthOptions.AUDIENCE,
 claims: claims,
 expires: DateTime.UtcNow.Add(TimeSpan.FromMinutes(2)),
 signingCredentials: new SigningCredentials(AuthOptions.GetSymmetricSecurityKey(), SecurityAlgorithms.HmacSha256));

 return new JwtSecurityTokenHandler().WriteToken(jwt);
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

```


Для описания некоторых настроек генерации токена в конце кода определен специальный класс AuthOptions:

```

public class AuthOptions
{
 public const string ISSUER = "MyAuthServer"; // издатель токена
 public const string AUDIENCE = "MyAuthClient"; // потребитель токена
 const string KEY = "mysupersecret_secretsecretsecretkey!123"; // ключ для шифрации
 public static SymmetricSecurityKey GetSymmetricSecurityKey() =>
 new SymmetricSecurityKey(Encoding.UTF8.GetBytes(KEY));
}

```


Константа `ISSUER` представляет издателя токена. Здесь можно определить любое название.


Константа `AUDIENCE` представляет потребителя токена - опять же может быть любая строка, обычно это сайт, на котором применяется токен.


Константа `KEY` хранит ключ, который будет применяться для создания токена. Стоит отметить, что для разных алгоритмов шифрования могут применяться ограничения на размер ключа.
Так, в данном примере применяется алгоритм `SecurityAlgorithms.HmacSha256`, для которого необходим ключ длиной не менее 256 бит или 32 байта


И метод `GetSymmetricSecurityKey()` возвращает ключ безопасности, который применяется для генерации токена. Для генерации токена
нам необходим объект класса SecurityKey. В качестве такого здесь выступает объект производного класса SymmetricSecurityKey,
в конструктор которого передается массив байт, созданный по секретному ключу.


Чтобы указать, что приложение для аутентификации будет использовать токена, в метод AddAuthentication() передается значение константы
JwtBearerDefaults.AuthenticationScheme.

```
builder.Services.AddAuthentication(JwtBearerDefaults.AuthenticationScheme)
```


#### Конфигурация и валидация токена


С помощью метода AddJwtBearer() в приложение добавляется конфигурация токена. Для конфигурации токена применяется
объект JwtBearerOptions, который позволяет с помощью свойств настроить работу с токеном. Данный объект имеет множество свойств.
Здесь же использовано только свойство TokenValidationParameters, которое задает параметры валидации токена.

```

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
 ValidateIssuerSigningKey = true,
 };
});

```


Объект TokenValidationParameters обладает множеством свойств, которые позволяют настроить различные аспекты валидации токена. В данном случае применяются следующие свойства:


-

ValidateIssuer: указывает, будет ли валидироваться издатель при валидации токена

-

ValidIssuer: строка, которая представляет издателя токена

-

ValidateAudience: указывает, будет ли валидироваться потребитель токена

-

ValidAudience: строка, которая представляет потребителя токена

-

ValidateLifetime: указывает, будет ли валидироваться время существования

-

IssuerSigningKey: представляет ключ безопасности - объект SecurityKey, который будет применяться при генерации токена

-

ValidateIssuerSigningKey: указывает, будет ли валидироваться ключ безопасности


Здесь устанавливаются наиболее основные свойства. А вообще можно установить кучу других параметров, например, названия claims для ролей и логинов пользователя и т.д.


### Генерация токена


Чтобы пользователь мог использовать токен, приложение должно отправить ему этот токен, а перед этим соответственно сгенерировать токен.
И для генерации токена здесь предусмотрена типовая конечная точка "/login":

```

app.Map("/login/{username}", (string username) =>
{
 var claims = new List<Claim> {new Claim(ClaimTypes.Name, username) };
 var jwt = new JwtSecurityToken(
 issuer: AuthOptions.ISSUER,
 audience: AuthOptions.AUDIENCE,
 claims: claims,
 expires: DateTime.UtcNow.Add(TimeSpan.FromMinutes(2)), // время действия 2 минуты
 signingCredentials: new SigningCredentials(AuthOptions.GetSymmetricSecurityKey(), SecurityAlgorithms.HmacSha256));

 return new JwtSecurityTokenHandler().WriteToken(jwt);
});

```


Для простоты конечная точка через параметр маршрута "username" получает некоторый логин пользователя и применяет его для генерации токена. На данном этапе для простоты
мы пока ничего не проверяем, валидный ли это логин, что это за логин, пока просто смотрим, как генерировать токен.


Для создания токена применяется конструктор JwtSecurityToken. Одним из параметров служит список объектов Claim. Объекты Claim служат для хранения некоторых
данных о пользователе, описывают пользователя. Затем эти данные можно применять для аутентификации. В данном случае добавляем в список один Claim, который хранит логин пользователя.


Затем собственно создаем JWT-токен, передавая в конструктор JwtSecurityToken соответствующие параметры. Обратите внимание, что для инициализации токена применяются
все те же константы и ключ безопасности, которые определены в классе AuthOptions и которые использовались для конфигурации настроек
в методе AddJwtBearer().


В конце посредством метода `JwtSecurityTokenHandler().WriteToken(jwt)` создается сам токен , который отправляется клиенту.


Для тестирования генерации токена обратимся к этой конечной точке:
![Генерация токена JWT в ASP.NET Core и C#](https://metanit.com./pics/13.2.png)


При обращении к конечной точке "/login" (например, по пути "/login/tom", где "tom" предствляет параметр "username") приложение сгенерирует нам jwt-токен, который нам необходимо отправлять
для доступа к ресурсам приложения с защищенным доступом. Например, в коде также определена еще одна конечная точка "/data":

```
app.Map("/data", [Authorize] (HttpContext context) => $"Hello World!");
```


Она применяет атрибут Authorize, соответственно доступ к ней ограничен только для аутентифицированных пользователей, которые имеют токен.
Например, если мы попытаемся обратиться по пути "/data", мы столкнемся с ошибкой 401 (Unauthorized) - доступ не авторизован:
![Ограничение доступа с помощью токена JWT в ASP.NET Core и C#](https://metanit.com./pics/13.3.png)


Поэтому для обращения к этому ресурсу (и ко всем другим ресурсам, к которым имеют доступ только аутентифицированные пользователи)
необходимо посылать полученный токен в запросе в заголовое Authorization:

```

"Authorization": "Bearer " + token // token - полученный ранее jwt-токен

```


В следующей статье рассмотрим, как применять токен для доступа к ресурсам.










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

**Источник:** [https://metanit.com/sharp/aspnet6/13.2.php](https://metanit.com/sharp/aspnet6/13.2.php)
