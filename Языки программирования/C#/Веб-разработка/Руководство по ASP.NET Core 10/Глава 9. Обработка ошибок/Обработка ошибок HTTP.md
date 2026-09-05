# Обработка ошибок HTTP

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10|Руководство по ASP.NET Core 10]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 9. Обработка ошибок|Глава 9. Обработка ошибок]] / Обработка ошибок HTTP

[[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 9. Обработка ошибок/Обработка исключений|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 9. Обработка ошибок|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 10. Results API/Введение в Results API|Вперёд]]

**Дата написания:** 05.09.2026

## Обработка ошибок HTTP

Последнее обновление: 23.12.2021




-

-

-














В отличие от исключений стандартный функционал проекта ASP.NET Core почти никак не обрабатывает ошибки HTTP, например, в случае если ресурс не найден.
При обращении к несуществующему ресурсу мы увидим в браузере пустую страницу, и только через консоль веб-браузера мы сможем увидеть статусный код. Либо браузер может отобразить какую-то
стандартную страницу.


Но с помощью компонента StatusCodePagesMiddleware можно добавить в проект отправку информации о статусном коде.
Для этого применяется метод app.UseStatusCodePages():

```

var builder = WebApplication.CreateBuilder();
var app = builder.Build();

// обработка ошибок HTTP
app.UseStatusCodePages();

app.Map("/hello", () => "Hello ASP.NET Core");

app.Run();

```


Здесь мы можем обращаться только по адресу "/hello". При обращении ко всем остальным адресам браузер отобразит базовую информацию об ошибке:
![метод UseStatusCodePages и отправка информации об ошибке в ASP.NET Core и C#](https://metanit.com./pics/9.4.png)


Метод UseStatusCodePages() следует вызывать ближе к началу конвейера обработки запроса, в частности, до
добавления middleware для работы со статическими файлами и до добавления конечных точек.


### Настройка сообщения


Сообщение, отправляемое методом `UseStatusCodePages()` по умолчанию, не очень информативное. Однако одна из версий метода позволяет настроить отправляемое
пользователю сообщение. В частности, мы можем изменить вызов метода так:

```

var builder = WebApplication.CreateBuilder();
var app = builder.Build();

// обработка ошибок HTTP
app.UseStatusCodePages("text/plain", "Error: Resource Not Found. Status code: {0}");

app.Map("/hello", () => "Hello ASP.NET Core");

app.Run();

```


В качестве первого параметра указывается MIME-тип ответа - в данном случае простой текст (""text/plain""). В качестве второго параметра
передается собственно то сообщение, которое увидит пользователь. В сообщение мы можем передать код ошибки через плейсхолдер "{0}".
![метод UseStatusCodePages и настройка сообщения об ошибке в ASP.NET Core и C#](https://metanit.com./pics/9.5.png)


### Установка обработчика ошибок


Еще одна версия метода UseStatusCodePages() позволяет более детально задать обаботчик ошибок. В частности, она принимает делегат, параметр которого - объект StatusCodeContext.
В свою очередь, объект StatusCodeContext имеет свойство HttpContext, из которого мы можем получить всю информацию о запросе и настроить отправку ответа. Например:

```

var builder = WebApplication.CreateBuilder();
var app = builder.Build();

// обработка ошибок HTTP
app.UseStatusCodePages(async statusCodeContext =>
{
 var response = statusCodeContext.HttpContext.Response;
 var path = statusCodeContext.HttpContext.Request.Path;

 response.ContentType = "text/plain; charset=UTF-8";
 if (response.StatusCode == 403)
 {
 await response.WriteAsync($"Path: {path}. Access Denied ");
 }
 else if (response.StatusCode == 404)
 {
 await response.WriteAsync($"Resource {path} Not Found");
 }
});

app.Map("/hello", () => "Hello ASP.NET Core");

app.Run();

```

![метод UseStatusCodePages и настройка обработки ошибки HTTP в ASP.NET Core и C#](https://metanit.com./pics/9.6.png)


### Методы UseStatusCodePagesWithRedirects и UseStatusCodePagesWithReExecute


Вместо метода `UseStatusCodePages()` мы также можем использовать еще пару других, которые также обрабатывают ошибки HTTP.


С помощью метода `app.UseStatusCodePagesWithRedirects()` можно выполнить переадресацию на определенный метод, который непосредственно обработает статусный код:

```

var builder = WebApplication.CreateBuilder();
var app = builder.Build();

app.UseStatusCodePagesWithRedirects("/error/{0}");

app.Map("/hello", () => "Hello ASP.NET Core");
app.Map("/error/{statusCode}", (int statusCode) => $"Error. Status Code: {statusCode}");

app.Run();

```


Здесь будет идти перенаправление по адресу "/error/{0}". В качестве параметра через плейсхолдер "{0}" будет передаваться статусный код
ошибки.


Но теперь при обращении к несуществующему ресурсу клиент получит статусный код 302 / Found. То есть формально несуществующий ресурс будет существовать, просто статусный код 302
будет указывать, что ресурс перемещен на другое место - по пути "/error/404".


Подобное поведение может быть неудобно, особенно с точки зрения поисковой индексации, и в этом случае мы можем применить другой метод
app.UseStatusCodePagesWithReExecute():

```

var builder = WebApplication.CreateBuilder();
var app = builder.Build();

app.UseStatusCodePagesWithReExecute("/error/{0}");

app.Map("/hello", () => "Hello ASP.NET Core");
app.Map("/error/{statusCode}", (int statusCode) => $"Error. Status Code: {statusCode}");

app.Run();

```


В качестве параметра метод `UseStatusCodePagesWithReExecute()` приминает путь к ресурсу, который будет обрабатывать ошибку. И также с помощью
плейсхолдера `{0}` можно передать статусный код ошибки. То есть в данном случае при возникновении ошибки будет вызываться конечная точка

```
app.Map("/error/{statusCode}", (int statusCode) => $"Error. Status Code: {statusCode}");
```


Формально мы получим тот же ответ, так как так же будет идти перенаправление на путь "/error/404". Но теперь браузер получит оригинальный статусный код 404.
![метод UseStatusCodePagesWithReExecute и обработки ошибок HTTP в ASP.NET Core и C#](https://metanit.com./pics/9.7.png)


Также можно задействовать другую версию метода, которая в качестве второго параметра принимает параметры строки запроса

```
app.UseStatusCodePagesWithReExecute("/error", "?code={0}");
```


Первый параметр метода указывает на путь перенаправления, а второй задает параметры строки запроса, которые будут передаваться при перенаправлении.
Вместо плейсхолдера {0} опять же будет передаваться статусный код ошибки. Пример использования:

```

var builder = WebApplication.CreateBuilder();
var app = builder.Build();

app.UseStatusCodePagesWithReExecute("/error", "?code={0}");

app.Map("/hello", () => "Hello ASP.NET Core");
app.Map("/error", (string code) => $"Error Code: {code}");


app.Run();

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

**Источник:** [https://metanit.com/sharp/aspnet6/9.2.php](https://metanit.com/sharp/aspnet6/9.2.php)
