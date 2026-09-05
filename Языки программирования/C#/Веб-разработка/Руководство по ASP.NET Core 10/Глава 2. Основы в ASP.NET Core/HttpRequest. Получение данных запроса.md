# HttpRequest. Получение данных запроса

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10|Руководство по ASP.NET Core 10]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 2. Основы в ASP.NET Core|Глава 2. Основы в ASP.NET Core]] / HttpRequest. Получение данных запроса

[[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 2. Основы в ASP.NET Core/HttpResponse. Отправка ответа|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 2. Основы в ASP.NET Core|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 2. Основы в ASP.NET Core/Отправка файлов|Вперёд]]

**Дата написания:** 05.09.2026

## HttpRequest. Получение данных запроса

Последнее обновление: 10.12.2021




-

-

-














Свойство Request объекта HttpContext представляет объект HttpRequest и хранит информацию о запросе в виде следующих свойств:


-

Body: предоставляет тело запроса в виде объекта Stream

-

BodyReader: возвращает объект типа PipeReader для чтения тела запроса

-

ContentLength: получает или устанавливает заголовок `Content-Length`

-

ContentType: получает или устанавливает заголовок `Content-Type`

-

Cookies: возвращает коллекцию куки (объект Cookies), ассоциированных с данным запросом

-

Form: получает или устанавливает тело запроса в виде форм

-

HasFormContentType: проверяет наличие заголовка `Content-Type`

-

Headers: возвращает заголовки запроса

-

Host: получает или устанавливает заголовок `Host`

-

HttpContext: возвращает связанный с данным запросом объект HttpContext

-

IsHttps: возвращает `true`, если применяется протокол https

-

Method: получает или устанавливает метод HTTP

-

Path: получает или устанавливает путь запроса в виде объекта RequestPath

-

PathBase: получает или устанавливает базовый путь запроса. Такой путь не должен содержать завершающий слеш

-

Protocol: получает или устанавливает протокол, например, HTTP

-

Query: возвращает коллекцию параметров из строки запроса

-

QueryString: получает или устанавливает строку запроса

-

RouteValues: получает данные маршрута для текущего запроса

-

Scheme: получает или устанавливает схему запроса HTTP


Рассмотрим применение некоторых из этих свойств.


### Получение заголовков запроса


Для получения заголовков применяется свойство Headers, которое представляет тип IHeaderDictionary.
Например, получим все заголовки запроса и выведем их на веб-страницу:

```

var builder = WebApplication.CreateBuilder();
var app = builder.Build();

app.Run(async(context) =>
{
 context.Response.ContentType = "text/html; charset=utf-8";
 var stringBuilder = new System.Text.StringBuilder("<table>");

 foreach(var header in context.Request.Headers)
 {
 stringBuilder.Append($"<tr><td>{header.Key}</td><td>{header.Value}</td></tr>");
 }
 stringBuilder.Append("</table>");
 await context.Response.WriteAsync(stringBuilder.ToString());
});

app.Run();

```

![Получение заголовков запроса в ASP.NET Core и C#](https://metanit.com./pics/2.16.png)


Для большинства стандартных заголовков HTTP в этом интерфейсе определены одноименные свойства, например, для заголовка "content-type" определено свойство `ContentType`,
а для заголовка "accept" - свойство `Accept`:

```

var builder = WebApplication.CreateBuilder();
var app = builder.Build();

app.Run(async(context) =>
{
 var acceptHeaderValue = context.Request.Headers.Accept;
 await context.Response.WriteAsync($"Accept: {acceptHeaderValue}");
});

app.Run();

```


Также подобые заголовки, а также какие-то кастомные заголовки, для которых не определены подобные свойства, можно получить как и любой дугой элемент словаря:

```
var acceptHeaderValue = context.Request.Headers["accept"];
```


Для ряда заголовков в классе HttpRequest определены отдельные свойства: Host, Method, ContentType, ContentLength.


### Получение пути запроса


Свойство path позволяет получить запрошенный путь, то есть адрес, к которому обращается клиент:

```

var builder = WebApplication.CreateBuilder();
var app = builder.Build();

app.Run(async(context) => await context.Response.WriteAsync($"Path: {context.Request.Path}"));

app.Run();

```

![получение пути запроса в ASP.NET Core и C#](https://metanit.com./pics/2.17.png)


Это свойство позволяет нам узнать, по какому адресу обращается пользователю. Например, мы можем определить условную обработку запроса в зависимости от запрошенного адреса:


Свойство path позволяет получить запрошенный путь, то есть адрес, к которому обращается клиент:

```

var builder = WebApplication.CreateBuilder();
var app = builder.Build();

app.Run(async(context) =>
{
 var path = context.Request.Path;
 var now = DateTime.Now;
 var response = context.Response;

 if (path=="/date")
 await response.WriteAsync($"Date: {now.ToShortDateString()}");
 else if (path == "/time")
 await response.WriteAsync($"Time: {now.ToShortTimeString()}");
 else
 await response.WriteAsync("Hello METANIT.COM");
});

app.Run();

```


В данном случае, если пользователь обращается по адресу "/date", то ему отображается текущая дата, а если обращается по адресу "/time" - текущее время.
В остальных случаях отображается некоторое универсальное сообщение:
![получение адреса запроса и маршрутизация в ASP.NET Core и C#](https://metanit.com./pics/2.18.png)


Подобным образом можно определить свою систему маршрутизации, однако в ASP.NET Core по умолчанию есть инструменты, которые проще использовать для создания системы маршрутизации в приложении и которые будут рассмотрены в последующих статьях.


### Строка запроса


Свойство QueryString позволяет получить строку запроса. Строка запроса представляет ту часть запрошенного адреса, которая идет после символа ? и
представляет набор параметров, разделенных символом амперсанда &:

```
?параметр1=значение1&параметр2=значение2&параметр3=значение3
```


Каждому параметру с помощью знака равно передается некоторое значение.


Стоит отметить, что строка запроса (query string) НЕ входит в путь запроса (path):

```

var builder = WebApplication.CreateBuilder();
var app = builder.Build();

app.Run(async(context) =>
{
 context.Response.ContentType = "text/html; charset=utf-8";
 await context.Response.WriteAsync($"<p>Path: {context.Request.Path}</p>" +
 $"<p>QueryString: {context.Request.QueryString}</p>");
});

app.Run();

```

![получение строки запроса в ASP.NET Core и C#](https://metanit.com./pics/2.19.png)


Так, в данном случае идет обращение по адресу

```
https://localhost:7256/users?name=Tom&age=37
```


Путь запроса или path представляет ту часть адреса, которая идет после домена/порта и до символа ?.

```
/users
```


Строка запроса или query string представляет ту часть адреса, которая идет начиная с символа ?.

```
?name=Tom&age=37
```


То есть в данном случае через строку запроса передаются два параметра. Первый параметр - `name` имеет значение "Tom". Bторой параметр - `age` имеет значение 37.


С помощью свойства Query можно получить все параметры строки запроса в виде словаря:

```

var builder = WebApplication.CreateBuilder();
var app = builder.Build();

app.Run(async(context) =>
{
 context.Response.ContentType = "text/html; charset=utf-8";
 var stringBuilder = new System.Text.StringBuilder("<h3>Параметры строки запроса</h3><table>");
 stringBuilder.Append("<tr><td>Параметр</td><td>Значение</td></tr>");
 foreach (var param in context.Request.Query)
 {
 stringBuilder.Append($"<tr><td>{param.Key}</td><td>{param.Value}</td></tr>");
 }
 stringBuilder.Append("</table>");
 await context.Response.WriteAsync(stringBuilder.ToString());
});

app.Run();

```

![парсинг строки запроса в ASP.NET Core и C#](https://metanit.com./pics/2.20.png)


Соответственно можно вытащить из словаря Query значения отдельных параметров:

```

var builder = WebApplication.CreateBuilder();
var app = builder.Build();

app.Run(async(context) =>
{
 string name = context.Request.Query["name"];
 string age = context.Request.Query["age"];
 await context.Response.WriteAsync($"{name} - {age}");
});

app.Run();

```

![параметры строки запроса в ASP.NET Core и C#](https://metanit.com./pics/2.21.png)










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

**Источник:** [https://metanit.com/sharp/aspnet6/2.5.php](https://metanit.com/sharp/aspnet6/2.5.php)
