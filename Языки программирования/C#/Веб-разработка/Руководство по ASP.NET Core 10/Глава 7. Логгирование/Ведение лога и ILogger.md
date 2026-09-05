# Ведение лога и ILogger

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10|Руководство по ASP.NET Core 10]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 7. Логгирование|Глава 7. Логгирование]] / Ведение лога и ILogger

[[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 6. Конфигурация/Передача конфигурации через IOptions|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 7. Логгирование|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 7. Логгирование/Фабрика логгера и провайдеры логгирования|Вперёд]]

**Дата написания:** 05.09.2026

## Ведение лога и ILogger

Последнее обновление: 22.12.2021




-

-

-














ASP.NET Core имеет встроенную поддержку логгирования, что позволяет применять логгирование с минимальными вкраплениями кода в функционал приложения.


Для логгирования данных нам необходим объект ILogger<T>. По умолчанию среда ASP NET Core через механизм внедрения зависимостей
уже предоставляет нам такой объект. Его можно получить как и любую другую зависимость в приложении. Также этот объект можно получить через свойство Logger
объекта WebApplication.


Например, используем встроенный логгер для логгирования на консоль приложения:

```

var builder = WebApplication.CreateBuilder();
var app = builder.Build();

app.Run(async (context) =>
{
 // пишем на консоль информацию
 app.Logger.LogInformation($"Processing request {context.Request.Path}");

 await context.Response.WriteAsync("Hello World!");
});

app.Run();

```


В данном случае через свойство app.Logger получаем встроенный логгер и с помощью его метода
`logger.LogInformation` передаем на консоль некоторую информацию.


При обращении к приложению с помощью следующего запроса http://localhost:xxxxx/hello на консоль будет выведена информация, переданная логгером:
![Тестирование логгера в ASP.NET Core и C#](https://metanit.com./pics/7.1.png)


### Категория логгера


При создании логгера для него указывается категория. Обычно в качестве категории логгера выступает класс, в котором используется логгер.
В этом случае логгер типизируется классом-категории. Например, логгер, для которого в качестве категории выступает класс Program:

```
ILogger<Program>
```


В чем смысл категории? Категория задает
текстовую метку, с которой ассоциируется сообщение логгера, и в выводе лога мы ее можем увидеть.
![Категория логгирования в ASP.NET Core и C#](https://metanit.com./pics/7.2.png)


Где это может быть полезно? Например, у нас есть несколько
классов middleware, где ведется логгирование. Указывая в качестве категории текущий класс, в последствии в логе мы
можем увидеть, в каком классе именно было создано данное сообщение лога. Поэтому, как правило, в качестве категории указывается текущий класс, но в принципе это необязательно.


### Получение логгера через внедрение зависимостей


Поскольку логгер добавляется в сервисы приложения, то мы можем получить его как и любой другой сервис через систему внедрения зависимостей. Например:

```

var builder = WebApplication.CreateBuilder();
var app = builder.Build();

app.Map("/hello", (ILogger<Program> logger) =>
{
 logger.LogInformation($"Path: /hello Time: {DateTime.Now.ToLongTimeString()}");
 return "Hello World";
});

app.Run();

```


В данном случае при обращении по адресу "/hello" сработает конечная точка, в обработчике которой через механизм внедрения зависимостей можно получить объект логгера.
Стоит учитывать, что в этом случае для логгера надо определить категорию. Здесь в качестве категории применяется класс Program (неявный класс, в котором и запускается приложение).


В самом обработчике логгер выводит на консоль путь запроса и время запроса:
![Категория логгера и ILogger в ASP.NET Core и C#](https://metanit.com./pics/7.3.png)


### Уровни и методы логгирования


При настройке логгирования мы можем установить уровень детализации информации с помощью одного из значений перечисления LogLevel.
Всего мы можем использовать следующие значения:


-

`Trace`: используется для вывода наиболее детализированных сообщений. Подобные сообщения могут нести важную информацию о
приложении и его строении, поэтому данный уровень лучше использовать при разработке, но никак не при публикации

-

`Debug`: для вывода информации, которая может быть полезной в процессе разработки и отладки приложения

-

`Information`: уровень сообщений, позволяющий просто отследить поток выполнения приложения

-

`Warning`: используется для вывода сообщений о неожиданных событиях, например, ошибках, которые не останавливают выполнение приложения,
но в то же время должны быть иследованы

-

`Error`: для вывода информации об ошибках и исключениях, которые возникли при текущей операции и которые не могут быть обработаны

-

`Critical`: уровень критических ошибок, которые требуют немедленной реакции - ошибками операционной системы, потерей данных в бд,
переполнение памяти диска и т.д.

-

`None`: вывод информации в лог не применяется


Для вывода соответствующего уровня информации у объекта `ILogger` определены соответствующие методы расширения:


-

`LogDebug()`

-

`LogTrace()`

-

`LogInformation()`

-

`LogWarning()`

-

`LogError()`

-

`LogCritical()`


Так, в примере выше для вывода информации на консоль использовался метод `LogInformation()`.


Вывод сообщений уровня Trace по умолчанию отключен.


Каждый такой метод имеет несколько перегрузок, которые могут принимать ряд различных параметров:


-

`string data`: строковое сообщение для лога

-

`int eventId`: числовой идентификатор, который связан с логом. Идентификатор должен быть статическим и специфическим для
определенной части логгируемых событий.

-

`string format`: строковое сообщения для лога, которое может содержать параметры

-

`object[] args`: набор параметров для строкового сообщения

-

`Exception error`: логгируемый объект исключения


Также для логгирования определен общий метод Log(), который позволяет определить уровень логгера через один из параметров:

```
logger.Log(LogLevel.Information, $"Requested Path: {context.Request.Path}");
```


При стандартном логгировании на консоль для каждого уровня/метода определен своя метка и цветовой маркер, которые позволяют сразу выделить сообщение
соответствующего уровня. Например, при запуске следующего кода:

```

var builder = WebApplication.CreateBuilder();
var app = builder.Build();

app.Run(async (context) =>
{
 var path = context.Request.Path;
 app.Logger.LogCritical($"LogCritical {path}");
 app.Logger.LogError($"LogError {path}");
 app.Logger.LogInformation($"LogInformation {path}");
 app.Logger.LogWarning($"LogWarning {path}");

 await context.Response.WriteAsync("Hello World!");
});

app.Run();

```


мы получим следующий лог на консоль:
![Уровни логгирования в ASP.NET Core и C#](https://metanit.com./pics/7.4.png)










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

**Источник:** [https://metanit.com/sharp/aspnet6/7.1.php](https://metanit.com/sharp/aspnet6/7.1.php)
