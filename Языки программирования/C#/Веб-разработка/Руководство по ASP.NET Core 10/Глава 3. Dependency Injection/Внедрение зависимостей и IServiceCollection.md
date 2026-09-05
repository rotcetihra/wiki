# Внедрение зависимостей и IServiceCollection

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10|Руководство по ASP.NET Core 10]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 3. Dependency Injection|Глава 3. Dependency Injection]] / Внедрение зависимостей и IServiceCollection

[[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 2. Основы в ASP.NET Core/IWebHostEnvironment и окружение|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 3. Dependency Injection|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 3. Dependency Injection/Создание сервисов|Вперёд]]

**Дата написания:** 05.09.2026

## Внедрение зависимостей и IServiceCollection

Последнее обновление: 17.12.2021




-

-

-














Dependency injection (DI) или внедрение зависимостей представляет механизм, который позволяет сделать взаимодействующие в приложении
объекты слабосвязанными. Такие объекты связаны между собой через абстракции, например, через интерфейсы, что делает всю систему более гибкой,
более адаптируемой и расширяемой.


В центре подобного механизма находится понятие зависимость - некоторая сущность, от которой зависит другая сущность. Например:

```

class Logger
{
 public void Log(string message) => Console.WriteLine(message);
}
class Message
{
 Logger logger = new Logger();
 public string Text { get; set; } = "";
 public void Print() => logger.Log(Text);
}

```


Здесь сущность Message, которая представляет некоторое сообщение, зависит от другой сущности - Logger, которая представляет логгер. В методе `Print()`
класса Message имитируется логгирование текста сообщения путем вызова у объекта Logger метода Log, который выводит сообщение на консоль.
Однако здесь класс Message тесно связан с классом Loger. Класс Message
отвечает за создание объекта Logger. Это имеет ряд недостатков. Прежде всего, если мы захотим вместо класса Logger использовать другой тип тип логгера, например, логгировать в файл, а не на консоль,
то нам придется менять класс Message. Один класс не составит труда поменять, но если в проекте таких классов много, то поменять во всех класс Logger на
другой будет труднее. Кроме того, класс Logger может иметь свои зависимости, которые тоже может потребоваться поменять. В итоге такими системами сложнее управлять и сложнее
тестировать.


Чтобы отвязать объект Logger от класса Message, мы можем создать абстракцию, которая будет представлять логгер, и передавать ее извне в объект Message:

```

interface ILogger
{
 void Log(string message);
}
class Logger : ILogger
{
 public void Log(string message) => Console.WriteLine(message);
}
class Message
{
 ILogger logger;
 public string Text { get; set; } = "";
 public Message(ILogger logger)
 {
 this.logger = logger;
 }
 public void Print() => logger.Log(Text);
}

```


Теперь класс Message не зависит от конкретной реализации класса Logger - это может быть любая реализация интерфейса ILogger. Кроме того, создание объекта логгера
выносится во внешний код. Класс Message больше ничего не знает о логгере кроме того, что у него есть метод Log, который позволяет логгировать его текст.


Тем не менее остается проблема управления подобными зависимостями, особенно если это касается больших приложений.
Нередко для установки зависимостей в подобных системах используются специальные контейнеры - IoC-контейнеры (Inversion of Control).
Такие контейнеры служат своего рода фабриками, которые устанавливают зависимости между абстракциями и конкретными объектами и, как правило, управляют
созданием этих объектов.


Преимуществом ASP.NET Core в этом оношении является то, что фреймворк уже по умолчанию имеет встроенный контейнер внедрения зависимостей,
который представлен интерфейсом IServiceProvider. А сами зависимости еще называются сервисами, собственно поэтому контейнер можно назвать
провайдером сервисов. Этот контейнер отвечает за сопоставление зависимостей с конкретными типами и за внедрение зависимостей в
различные объекты.


### Установка встроенных сервисов фреймворка


За управление сервисами в приложении в классе WebApplicationBuilder определено свойство Services,
которое представляет объект IServiceCollection - коллекцию сервисов:

```

WebApplicationBuilder builder = WebApplication.CreateBuilder();
IServiceCollection allServices = builder.Services; // коллекция сервисов

```


И даже если мы не добавляем в эту коллекцию никаких сервисов, IServiceCollection уже содержит ряд сервисов по умолчанию
![Сервисы в IServiceCollection в ASP.NET Core и C#](https://metanit.com./pics/4.1.png)


Как видно на скриншоте, в коллекции IServiceCollection 81 сервис, который мы можем использовать в приложении. Это такие сервисы, как ILogger<T>,
ILoggerFactory, IWebHostEnvironment и ряд других. Они добавляются по умолчанию инфраструктурой ASP.NET Core. И мы их можем использовать
в различных частях приложения.


### Информация о сервисах


Каждый сервис в коллекции IServiceCollection представляет объект ServiceDescriptor, который несет некоторую информацию.
В частности, наиболее важные свойства этого объекта:


-

ServiceType: тип сервиса

-

ImplementationType: тип реализации сервиса

-

Lifetime: жизненный цикл сервиса


Например, получим все сервисы, которые добавлены в приложение:

```

using System.Text;

var builder = WebApplication.CreateBuilder();

var services = builder.Services;

var app = builder.Build();

app.Run(async context =>
{
 var sb = new StringBuilder();
 sb.Append("<h1>Все сервисы</h1>");
 sb.Append("<table>");
 sb.Append("<tr><th>Тип</th><th>Lifetime</th><th>Реализация</th></tr>");
 foreach (var svc in services)
 {
 sb.Append("<tr>");
 sb.Append($"<td>{svc.ServiceType.FullName}</td>");
 sb.Append($"<td>{svc.Lifetime}</td>");
 sb.Append($"<td>{svc.ImplementationType?.FullName}</td>");
 sb.Append("</tr>");
 }
 sb.Append("</table>");
 context.Response.ContentType = "text/html;charset=utf-8";
 await context.Response.WriteAsync(sb.ToString());
});

app.Run();

```

![Получение всех сервисов их IServiceCollection в ASP.NET Core и C#](https://metanit.com./pics/4.2.png)


### Регистрация встроенных сервисов ASP.NET Core


Кроме ряда подключаемых по умолчанию сервисов ASP.NET Core имеет еще ряд встроенных сервисов, которые мы можем подключать в приложение при необходимости.
Все сервисы и компоненты middleware, которые предоставляются ASP.NET по умолчанию, регистрируются в приложение с помощью методов расширений IServiceCollection,
имеющих общую форму `Add[название_сервиса]`.


Например:

```

var builder = WebApplication.CreateBuilder();
builder.Services.AddMvc();

```


Для объекта IServiceCollection определено ряд методов расширений, которые начинаются на Add, как, например, `AddMvc()`. Эти методы добавляют
в объект IServiceCollection соответствующие сервисы. Например, `AddMvc()` добавляет в приложение сервисы MVC, благодаря чему мы сможем их использовать
в приложении.











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

**Источник:** [https://metanit.com/sharp/aspnet6/4.1.php](https://metanit.com/sharp/aspnet6/4.1.php)
