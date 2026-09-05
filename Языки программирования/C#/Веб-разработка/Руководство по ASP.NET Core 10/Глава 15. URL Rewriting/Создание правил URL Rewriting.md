# Создание правил URL Rewriting

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10|Руководство по ASP.NET Core 10]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 15. URL Rewriting|Глава 15. URL Rewriting]] / Создание правил URL Rewriting

[[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 15. URL Rewriting/Применение правил Apache для URL Rewriting|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 15. URL Rewriting|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 16. Клиентская разработка/Бандлинг и минификация|Вперёд]]

**Дата написания:** 05.09.2026

## Создание правил URL Rewriting

Последнее обновление: 09.05.2022




-

-

-














Если необходимо использовать какую-то более сложную логику по переопределению строки запроса, то в этом случае мы можем
определить свои правила с помощью методов или целых классов.


Например, пусть ранее сайт использовал технологию php, но затем мигрировал на asp.net, а все документы php были сконвертированы
в документы html. То есть ранее сайт, к примеру, использовал адрес http://localhost:1234/some.php,
то теперь документ перемещен по адресу http://localhost:1234/html/some.html. Расмотрим на примере создания своих правил,
как мы можем решить проблему адресов.


Пусть нужные документы находятся в проекте в папке wwwroot/html:
![Миграция с PHP на ASP.NET Core и C# и создание своих правил URL Rewriting](https://metanit.com./pics/15.5.png)


Допустим, там находится следующая страница some.html:

```

<!DOCTYPE html>
<html>
<head>
 <meta charset="utf-8" />
 <title></title>
</head>
<body>
 <h2>Hello World!</h2>
</body>
</html>

```


Вначале рассмотрим простой рерайт без переадресации и определим правило в виде отдельного метода. Для этого изменим код в файле Program.cs следующим образом:

```

using Microsoft.AspNetCore.Rewrite; // Пакет с middleware URL Rewriting

var builder = WebApplication.CreateBuilder();

var app = builder.Build();

var options = new RewriteOptions().Add(RewritePHPRequests);

app.UseRewriter(options);
app.UseStaticFiles();

app.MapGet("/", async context => await context.Response.WriteAsync("Hello World!"));

app.Run();

static void RewritePHPRequests(RewriteContext context)
{
 var path = context.HttpContext.Request.Path;
 var pathValue = path.Value; // запрошенный путь
 // если запрос к папке html, возвращаем ошибку 404
 if (path.StartsWithSegments(new PathString("/html")))
 {
 context.HttpContext.Response.StatusCode = StatusCodes.Status404NotFound;
 context.Result = RuleResult.EndResponse;
 return;
 }
 // если запрос к файлам с расширением php, переопределяем запрос на папку html
 if (pathValue!=null && pathValue.EndsWith(".php", StringComparison.OrdinalIgnoreCase))
 {
 // отрезаем расширение "php" в запрошенном пути и добавляем "html"
 string proccedPath = "/html" + pathValue.Substring(0, pathValue.Length - 3) + "html";
 context.HttpContext.Request.Path = new PathString(proccedPath);
 }
}

```


Для применения правила у объекта RewriteOptions вызывается метод Add, в который передается делегат Action<RewriteContext>. В данном случае передаем ссылку на метод
RewritePHPRequests.


В методе RewritePHPRequests вначале получаем объекты запроса, ответа и запрошенный путь. Если запрошенный путь уже содержит gпуть к каталогу html, то отклоняем его, устанавливая в качестве кода
ответа статусный код 404. Для завершения выполнения задается значение `context.Result = RuleResult.EndResponse`.
Тем самым мы предотвращаем прямой доступ к папке html (допустим, необходимо скрыть путь к документам html).


Если запрошенный адрес заканчивается на ".php", то выпоняем ряд преобразований, получая путь к html-документу в папке webroot/html. И затем
устанавливаем новое значение у свойства request.Path. Из него последующие компоненты middleware будут брать информацию о запрошенном пути и обработать его соответствующим образом.


Запустим приложение на выполнение и обратимся по адресу http://localhost:xxxx/some.php:
![Изменение php на asp.net core](https://metanit.com./pics/15.6.png)


В этом случае произойдет обращение к документу webroot/html/some.html.


Рассмотрим другой способ. Допустим, нам надо не просто переопределить адрес внутри приложения, а выполнить постоянную переадресацию, уведомляя браузеры пользователей и
поисковики, что адрес документа окончательно изменился. Для этого определим новый класс RedirectPHPRequests (хотя можно было бы и в виде метода определить):

```

using System.Text.RegularExpressions;
using Microsoft.AspNetCore.Rewrite;
using Microsoft.Net.Http.Headers;

namespace UrlRewritingApp
{
 public class RedirectPHPRequests : IRule
 {
 private readonly string _extension;
 private readonly PathString _newPath;

 public RedirectPHPRequests(string extension, string newPath)
 {
 if (string.IsNullOrEmpty(extension))
 {
 throw new ArgumentException(nameof(extension));
 }
 if (!Regex.IsMatch(newPath, @"(/[A-Za-z0-9]+)+?"))
 {
 throw new ArgumentException("Запрошенный путь недействителен", nameof(newPath));
 }

 _extension = extension;
 _newPath = new PathString(newPath);
 }

 public void ApplyRule(RewriteContext context)
 {
 var request = context.HttpContext.Request;
 var pathValue = request.Path.Value; // запрошенный путь

 if (request.Path.StartsWithSegments(new PathString(_newPath))) return;

 if (pathValue != null && pathValue.EndsWith(".php", StringComparison.OrdinalIgnoreCase))
 {
 var response = context.HttpContext.Response;

 response.StatusCode = StatusCodes.Status301MovedPermanently;
 context.Result = RuleResult.EndResponse;
 response.Headers[HeaderNames.Location] = _newPath + pathValue.Substring(0, pathValue.Length - 3) + _extension;
 }
 }
 }
}

```


Класс правила должен реализовать интерфейс IRule, который определяет метод ApplyRule.


В конструкторе получаем расширение, которое стоит использовать вместо php, а также путь к документам в рамках проекта.


В методе ApplyRule если вдруг запрошенный адрес начинается с названия каталог, где лежать файлы html, то завершаем выполнение. Так как нет смысла выполнять переадресацию, ведь запрос уже идет к файлам в нужном каталоге.
Иначе, если запрошен документ php, извлекаем имя документа и формируем новый путь. Этот путь передается через заголовок "Location". И кроме того,
устанавливается статусный код постоянной переадресации 301.


Применим этот класс в файле Program.cs:

```

using UrlRewritingApp; // пространство имен класса RedirectPHPRequests
using Microsoft.AspNetCore.Rewrite; // Пакет с middleware URL Rewriting

var builder = WebApplication.CreateBuilder();

var app = builder.Build();

var options = new RewriteOptions()
 .Add(new RedirectPHPRequests(extension: "html", newPath: "/html"));

app.UseRewriter(options);
app.UseStaticFiles();

app.MapGet("/", async context => await context.Response.WriteAsync("Hello World!"));

app.Run();

```


Перегруженная версия метода Add класса RewriteOptions принимает объект IRule, в качестве которого в данном случае передается объект RedirectPHPRequests,










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

**Источник:** [https://metanit.com/sharp/aspnet6/15.4.php](https://metanit.com/sharp/aspnet6/15.4.php)
