# Метод Use

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10|Руководство по ASP.NET Core 10]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 2. Основы в ASP.NET Core|Глава 2. Основы в ASP.NET Core]] / Метод Use

[[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 2. Основы в ASP.NET Core/Загрузка файлов на сервер|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 2. Основы в ASP.NET Core|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 2. Основы в ASP.NET Core/Создание ветки конвейера. UseWhen и MapWhen|Вперёд]]

**Дата написания:** 05.09.2026

## Метод Use

Последнее обновление: 10.12.2021




-

-

-














Метод расширения Use() добавляет компонент middleware, который позволяет передать обработку запроса далее следующим в конвейере компонентам.
Он имеет следующие версии

```

public static IApplicationBuilder Use(this IApplicationBuilder app, Func<HttpContext, Func<Task>, Task> middleware);
public static IApplicationBuilder Use(this IApplicationBuilder app, Func<HttpContext, RequestDelegate, Task> middleware)

```


Метод Use() реализован как метод расширения для типа IApplicationBuilder, соответственно мы можем вызвать данный метод
у объекта WebApplication для добавления middleware в приложение. В обоих версиях метод Use принимает некоторое действие, которое имеет два параметра и возвращает объект Task.


Первый параметр делегата Func, который передается в метод Use(), представляет объект HttpContext.
Этот объект позволяет получить данные запроса и управлять ответом клиенту.


Второй параметр делегата представляет другой делегат - Func<Task> или RequestDelegate. Этот
делегат представляет следующий в конвейере компонент middleware, которому будет передаваться обработка запроса.


В общем случае применение метода Use() выглядит следующим образом:

```

app.Use(async (context, next) =>
{
 // действия перед передачи запроса в следующий middleware
 await next.Invoke();
 // действия после обработки запроса следующим middleware
});

```


Работа middleware разбивается на две части:


-

Middleware выполняет некоторую начальную обработку запроса до вызова `await next.Invoke()`

-

Затем вызывается метод `next.Invoke()`, который передает обработку запроса следующему компоненту в конвейере

-

Когда следующий в конвейере компонент закончил обработку запрос возвращается в обратно в текущий компонент,
и выполняются действия, которые идут после вызова `await next.Invoke(`


Таким образом, middleware в методе Use выполняет действия до следующего в конвейере компонента и после него.


Рассмотрим метод Use() на примере:

```

var builder = WebApplication.CreateBuilder();
var app = builder.Build();

string date = "";

app.Use(async(context, next) =>
{
 date = DateTime.Now.ToShortDateString();
 await next.Invoke(); // вызываем middleware из app.Run
 Console.WriteLine($"Current date: {date}"); // Current date: 08.12.2021
});

app.Run(async(context) => await context.Response.WriteAsync($"Date: {date}"));

app.Run();

```


В данном случае мы используем перегрузку метода Use, которая в качестве параметров принимает контекст запроса - объект HttpContext и
делегат `Func<Task>`, который представляет собой ссылку на следующий в конвейере компонент middleware.


Middleware в методе `app.Use()` реализует простейшую задачу - присваивает переменной `date` текущую дату в виде строки и затем передает обработку запроса
следующим компонентам middleware в конвейере. То есть при вызове `await next.Invoke()` обработка запроса перейдет к тому компоненту, который установлен в методе `app.Run()`.
В итоге обработка запроса будет выглядеть следующим образом:


1.

Вызов компонента app.Use

2.

Установка значения переменной date:

```
date = DateTime.Now.ToShortDateString();
```


3.

Вызов `await next.Invoke()`. Управление переходит следующему компоненту в конвейере - к app.Run.

4.

В middleware из `app.Run()` отравляет клиенту текущую дату в качестве ответа с помощью метода `context.Response.WriteAsync()`:

```

await context.Response.WriteAsync($"Date: {date}");

```


5.

Метод app.Run закончил свою работу, и управление обработкой возвращается к middleware в методе app.Use. Начинает выполняться та часть кода, которая
идет после `await next.Invoke()`. В этой части выполняется условное логгирование - на консоль выводится значение переменной date:

```
Console.WriteLine($"Current date: {date}");
```


После этого обработка запроса завершена


В итоге в веб-браузере мы увидим следующее сообщение:
![Обработка запроса методом app.Use в ASP.NET Core и C#](https://metanit.com./pics/2.5.png)


А в консоли запущенного приложения мы увидим значение переменной date, которое выводится в middleware из метода app.Use:
![Создание конвейера middleware с помощью метода app.Use в ASP.NET Core и C#](https://metanit.com./pics/2.6.png)


#### Отправка ответа


При использовании метода Use и передаче выполнения следующему делегату следует учитывать, что не рекомендуется вызывать метод
`next.Invoke` после метода `Response.WriteAsync()`. Компонент middleware должен либо генерировать ответ с помощью Response.WriteAsync,
либо вызывать следующий делегат посредством `next.Invoke`, но не выполнять оба этих действия одновременно. Так как согласно документации
последующие изменения объекта Response могут привести к нарушению протокола, например, будет послано больше байт, чем указано в заголовке Content-Length, либо
могут привести к нарушению тела ответа, например, футер страницы HTML запишется в CSS-файл.


То есть к примеру следующая обработка запроса не рекомендуется:

```

var builder = WebApplication.CreateBuilder();
var app = builder.Build();

app.Use(async (context, next) =>
{
 await context.Response.WriteAsync("<p>Hello world!</p>");
 await next.Invoke();
});

app.Run(async (context) =>
{
 //await Task.Delay(10000); // можно поставить задержку
 await context.Response.WriteAsync("<p>Good bye, World...</p>");
});

app.Run();

```


### Использование делегат RequestDelegate


В примере выше использовалась версия метода Use(), которая использует делегат Func<Task>. Подобным образом можно использовать
и другую версию, где используется делегат RequestDelegate. Единственное - при вызове делегата ( то есть фактически следующего в конвейере компонента)
необходимо передавать делегату объект HttpContext:

```

var builder = WebApplication.CreateBuilder();
var app = builder.Build();

string date = "";

app.Use(async(context, next) =>
{
 date = DateTime.Now.ToShortDateString();
 await next.Invoke(context); // здесь next - RequestDelegate
 Console.WriteLine($"Current date: {date}"); // Current date: 08.12.2021
});

app.Run(async(context) => await context.Response.WriteAsync($"Date: {date}"));

app.Run();

```


### Терминальный компонент middleware


Middleware в методе Use() необязательно должен вызывать к следующему в конвейере компоненту. Вместо этого он может завершить обработку запроса. В этом случае
он может выступать в роли такого же терминального компонента middleware, а и компоненты из метода Run(). Например:

```

var builder = WebApplication.CreateBuilder();
var app = builder.Build();

app.Use(async(context, next) =>
{
 string? path = context.Request.Path.Value?.ToLower();
 if (path == "/date")
 {
 await context.Response.WriteAsync($"Date: {DateTime.Now.ToShortDateString()}");
 }
 else
 {
 await next.Invoke();
 }
});

app.Run(async(context) => await context.Response.WriteAsync($"Hello METANIT.COM"));

app.Run();

```


Здесь middleware в app.Use проверяет запрошенный адрес - если он содержит "/date", то клиенту отправляется текущая дата.
Иначае обработка запроса передается дальше в app.Run.
![Терминальный компонент middleware в app.Use в ASP>NET Core и C#](https://metanit.com./pics/2.7.png)


Причем в принципе мы можем использовать компонент в app.Use как единственный и соответственно терминальный:

```

var builder = WebApplication.CreateBuilder();
var app = builder.Build();
app.Use(async (HttpContext context, Func<Task> next) =>
{
 await context.Response.WriteAsync("Hello Work!");
});

app.Run();

```


Однако в данном случае для большей производительости лучше использовать app.Run(), если нам надо определить лишь один компонент,
который в принципе не передает запрос дальше по конвейеру.


### Вынесение компонентов в методы


Также можно вынести все inline-компоненты в отдельные методы:

```

var builder = WebApplication.CreateBuilder();
var app = builder.Build();

app.Use(GetDate);
app.Run(async (context) => await context.Response.WriteAsync("Hello METANIT.COM"));
app.Run();
async Task GetDate(HttpContext context, Func<Task> next)
{
 string? path = context.Request.Path.Value?.ToLower();
 if (path == "/date")
 {
 await context.Response.WriteAsync($"Date: {DateTime.Now.ToShortDateString()}");
 }
 else
 {
 await next.Invoke();
 }
}

```


Подобным образом можно использовать и другую версию метода Use, в которой используется делегат RequestDelegate:

```

async Task GetDate(HttpContext context, RequestDelegate next)
{
 string? path = context.Request.Path.Value?.ToLower();
 if (path == "/date")
 {
 await context.Response.WriteAsync($"Date: {DateTime.Now.ToShortDateString()}");
 }
 else
 {
 await next.Invoke(context);
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

**Источник:** [https://metanit.com/sharp/aspnet6/2.7.php](https://metanit.com/sharp/aspnet6/2.7.php)
