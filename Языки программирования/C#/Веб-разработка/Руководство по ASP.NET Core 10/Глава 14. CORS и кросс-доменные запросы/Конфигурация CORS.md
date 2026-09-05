# Конфигурация CORS

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10|Руководство по ASP.NET Core 10]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 14. CORS и кросс-доменные запросы|Глава 14. CORS и кросс-доменные запросы]] / Конфигурация CORS

[[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 14. CORS и кросс-доменные запросы/Подключение CORS в приложении|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 14. CORS и кросс-доменные запросы|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 14. CORS и кросс-доменные запросы/Политики CORS|Вперёд]]

**Дата написания:** 05.09.2026

## Конфигурация CORS

Последнее обновление: 08.05.2022




-

-

-














Для обработки кроссдоменных запросов и работы CORS в прошлой теме код приложения выглядел следующим образом:

```

var builder = WebApplication.CreateBuilder();

builder.Services.AddCors(); // добавляем сервисы CORS

var app = builder.Build();

// настраиваем CORS
app.UseCors(builder => builder.AllowAnyOrigin());

app.Map("/", async context => await context.Response.WriteAsync("Hello METANIT.COM!"));

app.Run();

```


В вызове app.UseCors() с помощью методов объекта CorsPolicyBuilder можно настроить конфигурацию CORS:


-

AllowAnyOrigin(): принимаются запросы с любого адреса

-

AllowAnyHeader(): принимаются запросы с любыми заголовками

-

AllowAnyMethod(): принимаются запросы любого типа (GET/POST)

-

AllowCredentials(): разрешается принимать идентификационные данные от клиента (например, куки)

-

WithHeaders(): принимаются только те запросы, которые используют содержат определенные заголовки

-

WithMethods(): принимаются запросы только определенного типа

-

WithOrigins(): принимаются запросы только с определенных адресов

-

WithExposedHeaders(): позволяет серверу отправлять на сторону клиента свои заголовки


### Определение адреса


Метод AllowAnyOrigin() позволяет установить взаимодействие с любым приложением по любому адресу. Однако подобное поведение может
быть нежелательным. В этом случае мы можем ограничить круг адресов с помощью метода WithOrigins():

```

app.UseCors(builder => builder.WithOrigins("http://example.com", "http://google.com"));

```


При чем, что важно, в конце названия домена не должно быть конечного слеша.


### Определение метода запроса


Метод AllowAnyMethod() позволяет принимать запросы любого типа (GET/POST). Также можно настроить принятие только определенного типа запросов:

```

app.UseCors(builder => builder.WithOrigins("https://localhost:7027").WithMethods("GET"));

```


### Определение заголовков


Для разрешения запросов с любыми заголовками применяется метод AllowAnyHeader(). Следует отметить, что вместе с этим методом лучше также указывать и
метод AllowAnyMethod() или WithMethods() для указания типа запроса:

```

app.UseCors(builder => builder.WithOrigins("https://localhost:7027")
 .AllowAnyHeader()
 .AllowAnyMethod());

```


Если необходимо принимать запросы только с определенными
заголовоками, то все требуемые заголовки надо передать в метод WithHeaders():

```

app.UseCors(builder => builder.WithOrigins("https://localhost:7027")
 .AllowAnyMethod()
 .WithHeaders("custom-header"));

```


В данном случае необходимо, чтобы клиент отправлял в запросе заголовок "custom-header". Например, отправка данного заголовка в коде javascript
с помощью функции fetch:

```

<h2 id="result"></h2>
<button id="btn" value="Запрос">Запрос</button>

<script>
 const btn = document.getElementById("btn");
 const result = document.getElementById("result");
 btn.addEventListener("click", async () => {
 try {
 const response = await fetch("https://localhost:7199/", { headers: { "custom-header": "test" } });
 if (response.ok) result.innerText = await response.text();
 }
 catch (e) {
 result.innerText = e.message;
 }
 });
</script>

```


### Получение заголовков на клиенте


Если сервер отправляет какие-то свои заголовки, то по умолчанию клиент их не получает. Чтобы на стороне сервера указать, какие заголовки может получать клиент,
следует использовать метод WithExposedHeaders():

```

var builder = WebApplication.CreateBuilder();

builder.Services.AddCors(); // добавляем сервисы CORS

var app = builder.Build();

// настраиваем CORS
app.UseCors(builder => builder.WithOrigins("https://localhost:7027")
 .AllowAnyMethod()
 .AllowAnyHeader()
 .WithExposedHeaders("custom-header"));

app.Run(async (context) =>
{
 context.Response.Headers.Add("custom-header", "5678");
 await context.Response.WriteAsync("Hello World!");
});

app.Run();

```


Сервер устанавливает заголовок custom-header и отправляет его клиенту. Чтобы клиент получил этот заголовок, он передается в метод WithExposedHeaders.


Затем на стороне клиента можно получить значение этого заголовка. Например, получение в коде JavaScript с помощью функции fetch:

```

<!DOCTYPE html>
<html>
<head>
 <meta charset="utf-8" />
 <title>Test CORS</title>
</head>
<body>
 <h2 id="result"></h2>
 <button id="btn" value="Запрос">Запрос</button>

 <script>
 const btn = document.getElementById("btn");
 const result = document.getElementById("result");
 btn.addEventListener("click", async () => {
 try {
 const response = await fetch("https://localhost:7199/");
 if (response.ok) {
 const headerTitle = "custom-header"; // название заголовка
 result.innerText = await response.text();
 if (response.headers.has(headerTitle)) { // если заголовок есть
 console.log(response.headers.get(headerTitle)); // получаем его значение
 }
 }
 }
 catch (e) {
 result.innerText = e.message;
 }
 });
 </script>
</body>
</html>

```


Альтернативное получение через XMLHttpRequest:

```

const btn = document.getElementById("btn");
const result = document.getElementById("result");
const headers = document.getElementById("headers");
const request = new XMLHttpRequest();

btn.addEventListener("click", function (e) {
 request.open("GET", "https://localhost:44313/");
 request.onreadystatechange = reqReadyStateChange;
 request.send();
});

function reqReadyStateChange() {
 if (request.readyState == 4) {
 if (request.status == 200){
 result.innerText = request.responseText;
 // получаем заголовок
 headers.innerText = request.getResponseHeader("custom-header");
 }
 }
}

```


### Передача идентификационных данных


По умолчанию браузер не посылает никаких идентификационных данных. Подобные данные включают куки, а также данные HTTP-аутентификации.
Для отправки идентификационных данных в кроссдоменном запросе на стороне клиента у объекта XMLHttpRequest необходимо установить свойство
withCredentials равным true.

```

const request = new XMLHttpRequest();
request.open("GET", "https://localhost:44313/");
request.withCredentials = true;

```


Для получения данных на стороне сервера применяется метод AllowCredentials(). Этот метод устанавливает заголовок `Access-Control-Allow-Credentials`,
который говорит браузеру, что сервер разрешает отправку идентификационных данных. При этом данный метод не может использоваться с методом AllowAllOrigin, то
есть обязательно нужно указать набор адресов, с которыми будет взаимодействовать сервер. Например:

```

var builder = WebApplication.CreateBuilder();

builder.Services.AddCors(); // добавляем сервисы CORS

var app = builder.Build();

// настраиваем CORS
app.UseCors(builder => builder.WithOrigins("https://localhost:7027")
 .AllowCredentials());

app.Run(async (context) =>
{
 var login = context.Request.Cookies["login"]; // получаем отправленные куки
 await context.Response.WriteAsync($"Hello {login}!");
});

app.Run();

```


При отправке запроса с помощью функции fetch ей необходимо передать опцию credentials со значением include

```

<!DOCTYPE html>
<html>
<head>
 <meta charset="utf-8" />
 <title>Test CORS</title>
</head>
<body>
 <h2 id="result"></h2>
 <button id="btn" value="Запрос">Запрос</button>

 <script>
 const btn = document.getElementById("btn");
 const result = document.getElementById("result");
 document.cookie = "login=tom32"; // куки, которые будут отправляться
 btn.addEventListener("click", async () => {
 try {
 const response = await fetch("https://localhost:7199/", { credentials: "include"});
 if (response.ok) result.innerText = await response.text();

 }
 catch (e) {
 result.innerText = e.message;
 }
 });
 </script>
</body>
</html>

```


Альтернативный вариант с помощью XMLHttpRequest:

```

const btn = document.getElementById("btn");

const request = new XMLHttpRequest();
document.cookie = "login=tom32;"; // куки, которые будут отправляться

btn.addEventListener("click", function () {
 request.open("GET", "https://localhost:44313/");
 request.onreadystatechange = reqReadyStateChange;
 request.withCredentials = true; // устанавливаем отправку
 request.send();
});
function reqReadyStateChange() {
 if (request.readyState == 4) {
 if (request.status == 200)
 console.log(request.responseText);
 }
}

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

**Источник:** [https://metanit.com/sharp/aspnet6/14.2.php](https://metanit.com/sharp/aspnet6/14.2.php)
