# Статические файлы и MapStaticAssets

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10|Руководство по ASP.NET Core 10]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 5. Статические файлы|Глава 5. Статические файлы]] / Статические файлы и MapStaticAssets

[[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 5. Статические файлы/Работа со статическими файлами|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 5. Статические файлы|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 6. Конфигурация/Основы конфигурации|Вперёд]]

**Дата написания:** 05.09.2026

Последнее обновление: 22.05.2025




-

-

-














В ASP.NET Core 9.0 был добавлен новый компонент middleware - MapStaticAssets. Посмотрим, чем он отличается от стандартного компонента UseStaticFiles,
который применялся в ранних версиях ASP.NET Core.


Прежде всего `UseStaticFiles` обслуживает статические файлы, но не обеспечивает тот же уровень оптимизации, что и `MapStaticAssets`. `MapStaticAssets` оптимизирован для обслуживания ресурсов, о которых приложение знает во время выполнения.
Если приложение обслуживает ресурсы из других мест, таких как диск или встроенные ресурсы, следует использовать `UseStaticFiles`.


`MapStaticAssets` предоставляет следующие преимущества, которые недоступны при вызове `UseStaticFiles`:


-

Сжатие во время сборки для всех ресурсов в приложении, включая JavaScript и CSS, но исключая ресурсы изображений и шрифтов, которые уже сжаты. Во время разработки применяется сжатие Gzip (Content-Encoding: gz),
а во время публикации - сжатие Brotli (Content-Encoding: br).

-

Для всех ресурсов во время сборки применяется отпечаток Fingerprinting с помощью строки хэша SHA-256 для содержимого каждого файла в кодировке Base64.
Это предотвращает повторное использование старой версии файла, даже если старый файл кэширован. Статические ресурсы с отпечатком кэшируются с помощью директивы immutable (указывает, что ответ не будет обновляться, пока он актуален), что приводит к тому,
что браузер никогда не запрашивает ресурс снова, пока он не изменится. Для браузеров, которые не поддерживают директиву immutable, добавляется директива max-age.


Даже если ресурс не применяет отпечаток fingerprinting, для каждого статического ресурса генерируется тег ETag на основе контента с использованием хэша fingerprint файла в качестве значения ETag. Это гарантирует, что браузер загружает файл только в том случае, если его содержимое изменяется (или файл загружается впервые).


Внутренне фреймворк сопоставляет физические ресурсы с их отпечатками fingerprint, что позволяет приложению находить автоматически сгенерированные ресурсы, такие как CSS для определенных частей приложения.
Кроме того, фреймворк может генерировать теги ссылок в элементе `<head>` страницы для предварительной загрузки ресурсов.

-

Во время тестирования разработки Visual Studio и использования Hot Reload информация о целостности удаляется из ресурсов, чтобы избежать проблем при изменении файла во время работы приложения, и статические ресурсы не кэшируются, чтобы браузер всегда получал текущий контент.


При этом следует отметить, что `MapStaticAssets` не поддерживает ряд функций, которые поддерживаются `UseStaticFiles`, в частности:


-

Обслуживание файлов с диска или встроенных ресурсов или других расположений

-

Обслуживание файлов за пределами корневого каталога wwwroot

-

Установка заголовков ответа HTTP

-

Просмотр каталогов

-

Обслуживание документов по умолчанию

-

FileExtensionContentTypeProvider

-

Обслуживание файлов из нескольких расположений


Таким образом, у разработчика начиная с ASP.NET Core 9 есть выбор, что использовать - MapStaticAssets или UseStaticFiles.


Возможные оптимизации с `MapStaticAssets` включают:


-

Обслуживание определенного ресурса один раз, пока файл не изменится или браузер не очистит свой кэш. Установка заголовков ETag и Last-Modified.

-

Предотвращение использования браузером старых или устаревших ресуров после обновления приложения. Установка заголовка Last-Modified.

-

Настройка правильных заголовков кэширования.

-

Использование кэширования.

-

Обслуживание сжатых версий ресуров, когда это возможно. Эта оптимизация не включает минимизацию.

-

Использование CDN для обслуживания ресуров ближе к пользователю.

-

Снятие отпечатков ресуров для предотвращения повторного использования старых версий файлов.


### Применение MapStaticAssets


Обслуживаемые компонентом `MapStaticAssets` статические файлы хранятся в корневом веб-каталоге проекта, который по умолчанию представляет папку **wwwroot**,
но его можно изменить с помощью метода **UseWebRoot**.


Добпустим, у нас в проекте есть папка **wwwroot** со следующей структурой:


-

Файл index.html

-

Папка js


 -

Файл app.js


Пусть в файле index.html будет какой-нибудь простенький контент с подключением файла js/app.js

```

<!DOCTYPE html>
<html>
<head>
 <meta charset="utf-8" />
 <title>METANIT.COM</title>
</head>
<body>
 <h1>Index Page</h1>
 <script src="js/app.js"></script>
</body>
</html>

```


А в файле js/app.js определим для теста какой-нибудь простенький скрипт:

```

console.log("Hello METANIT.COM");

```


В главный файл программы Program.cs добавим вызов `MapStaticAssets`

```

var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.MapStaticAssets(); // обработка статических файлов

app.MapGet("/", () => "Hello World!");

app.Run();

```


ПРи запуске приложения и обращения по пути "index.html" мы увидим содержимое файла index.html с выполнением скрипта из js/app.js
![MapStaticAssets в ASP.NET Core](https://metanit.com./pics/2.56.png)


ОБратите внимание, что файлы по умолчанию здесь не работают, и при обращении по корневому пути "/" будет срабатывать вызов `app.MapGet("/", () => "Hello World!");`










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

**Источник:** [https://metanit.com/sharp/aspnet6/5.3.php](https://metanit.com/sharp/aspnet6/5.3.php)
