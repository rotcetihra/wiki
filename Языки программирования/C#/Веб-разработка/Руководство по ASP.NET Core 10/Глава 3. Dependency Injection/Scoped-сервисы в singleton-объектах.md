# Scoped-сервисы в singleton-объектах

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10|Руководство по ASP.NET Core 10]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 3. Dependency Injection|Глава 3. Dependency Injection]] / Scoped-сервисы в singleton-объектах

[[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 3. Dependency Injection/Применение сервисов в классах middleware|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 3. Dependency Injection|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 3. Dependency Injection/Множественная регистрация сервисов|Вперёд]]

**Дата написания:** 05.09.2026

## Scoped-сервисы в singleton-объектах

Последнее обновление: 18.12.2021




-

-

-














Все объекты, которые используются в ASP.NET Core, имеет три варианта жизненного цикла. Singleton-объекты создаются один раз при первом к ним обращении,
а при всех последующих запросах к приложению используется ранее созданный singleton-объект. К подобным singleton-объектам относятся, к примеру, компоненты
middleware или сервисы, которые регистрируются с помощью метода `AddSingleton()`.


Transient-объекты создаются каждый раз, когда нам требуется экземпляр определенного класса. А scoped-объекты создаются по одному на каждый запрос.


Одни объекты или сервисы с помощью встроенного механизма dependency injection можно передать в другие объекты.
Наиболее распространенный способ внедрения объектов предсталяет инъекция через конструктор. Однако начиная с версии ASP.NET Core 2.0
мы не можем передавать scoped-сервисы в конструктор singleton-объектов.


Например, пусть будут опеделены следующие классы:

```

public interface ITimer
{
 string Time { get; }
}
public class Timer : ITimer
{
 public Timer()
 {
 Time = DateTime.Now.ToLongTimeString();
 }
 public string Time { get; }
}
public class TimeService
{
 private ITimer timer;
 public TimeService(ITimer timer)
 {
 this.timer = timer;
 }
 public string GetTime() => timer.Time;
}

```


TimeService получает через конструктор сервис ITimer и использует его для получения текущего времени.


Также пусть будет определен компонент middleware TimerMiddleware:

```

public class TimerMiddleware
{
 TimeService timeService;
 public TimerMiddleware(RequestDelegate next, TimeService timeService)
 {
 this.timeService = timeService;
 }

 public async Task Invoke(HttpContext context)
 {
 await context.Response.WriteAsync($"Time: {timeService?.GetTime()}");
 }
}

```


Компонент TimerMiddleware получает сервис TimeService и отправляет в ответ клиенту информацию о текущем времени.


TimerMiddleware является singleton-объектом. И теперь зарегистрируем сервис TimeService как scoped-объект:

```

var builder = WebApplication.CreateBuilder();

builder.Services.AddTransient<ITimer, Timer>();
builder.Services.AddScoped<TimeService>();

var app = builder.Build();

app.UseMiddleware<TimerMiddleware>();

app.Run();

```


Если мы запустим приложение, то консоль приложения нам отобразит ошибку типа "InvalidOperationException: Cannot resolve scoped service 'TimeService' from root provider.":
![Cannot resolve scoped service from root provider в ASP.NET Core и C#](https://metanit.com./pics/4.12.png)


То есть на момент создания объекта TimerMiddleware scoped-сервис TimeService еще не установлен, соответственно он использоваться не может. А без создания объекта TimeService
нельзя создать объект TimerMiddleware.


Аналогичная ситуация может возникнуть, если TimeService добавляется как Transient, а сервис ITimer определен как Scoped:

```

var builder = WebApplication.CreateBuilder();

builder.Services.AddScoped<ITimer, Timer>();
builder.Services.AddTransient<TimeService>();

var app = builder.Build();

app.UseMiddleware<TimerMiddleware>();

app.Run();

```


В этом случае для создания объекта TimeService надо получить сервис ITimer, но на момент вызова конструктора TimerMiddleware сервис ITimer еще неопределен:
![Cannot resolve from root provider because it requires scoped service в ASP.NET Core и C#](https://metanit.com./pics/4.13.png)


Для выхода из этой ситуации ни TimeService, ни ITimer не должны иметь жизненный цикл Scoped. То есть это может быть Transient или Singleton.


Рассмотрим еще одну ситуацию, с которой можно столкнуться в любой части приложения, а не только в конструкторе middleware, когда
сервис TimeService представляет singleton, а ITimer - scoped-объект:

```

var builder = WebApplication.CreateBuilder();

builder.Services.AddScoped<ITimer, Timer>();
builder.Services.AddSingleton<TimeService>();

var app = builder.Build();

app.UseMiddleware<TimerMiddleware>();

app.Run();

```


И, допустим, эти сервисы используются в TimerMiddleware непосредственно при обработке запроса в методе Invoke/InvokeAsync:

```

public class TimerMiddleware
{
 public TimerMiddleware(RequestDelegate next) { }

 public async Task Invoke(HttpContext context, TimeService timeService)
 {
 await context.Response.WriteAsync($"Time: {timeService?.GetTime()}");
 }
}

```


При запуске приложения мы опять же столкнемся с ошибкой, только немного другой "Cannot consume scoped service 'DIApp.ITimer' from singleton 'DIApp.TimeService'"
![Cannot consume scoped service from singleton in ASP.NET Core и C#](https://metanit.com./pics/4.14.png)


Но суть будет та же самая - мы не можем по умолчанию передавать в конструктор singleton-объекта scoped-сервис.










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

**Источник:** [https://metanit.com/sharp/aspnet6/4.6.php](https://metanit.com/sharp/aspnet6/4.6.php)
