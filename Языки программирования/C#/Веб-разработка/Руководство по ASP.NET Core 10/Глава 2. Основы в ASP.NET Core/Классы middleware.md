# Классы middleware

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10|Руководство по ASP.NET Core 10]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 2. Основы в ASP.NET Core|Глава 2. Основы в ASP.NET Core]] / Классы middleware

[[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 2. Основы в ASP.NET Core/Метод Map|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 2. Основы в ASP.NET Core|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 2. Основы в ASP.NET Core/Построение конвейера обработки запроса|Вперёд]]

**Дата написания:** 05.09.2026

## Классы middleware

Последнее обновление: 15.12.2021




-

-

-














В прошлых темах используемые компоненты middleware фактически представляли методы, то есть так называемые inline middleware.
Однако также ASP.NET Core позволяет определять middleware в виде отдельных классов.


Итак, добавим в проект новый класс, который назовем TokenMiddleware и который будет иметь следующий код:

```

public class TokenMiddleware
{
 private readonly RequestDelegate next;

 public TokenMiddleware(RequestDelegate next)
 {
 this.next = next;
 }

 public async Task InvokeAsync(HttpContext context)
 {
 var token = context.Request.Query["token"];
 if (token!="12345678")
 {
 context.Response.StatusCode = 403;
 await context.Response.WriteAsync("Token is invalid");
 }
 else
 {
 await next.Invoke(context);
 }
 }
}

```


Класс middleware должен иметь конструктор, который принимает параметр типа RequestDelegate. Через этот параметр можно получить ссылку на тот делегат запроса, который стоит следующим в конвейере
обработки запроса.


Также в классе должен быть определен метод, который должен называться либо Invoke, либо InvokeAsync.
Причем этот метод должен возвращать объект Task и принимать в качестве параметра контекст запроса - объект HttpContext.
Данный метод собственно и будет обрабатывать запрос.


Суть действия класса заключается в том, что мы получаем из запроса параметр "token". Если полученный токен равен строке "12345678", то передаем запрос
дальше следующему компоненту, вызвав метод `_next.Invoke()`. Иначе возвращаем пользователю сообщение об ошибке.


Для добавления компонента middleware, который представляет класс, в конвейер обработки запроса применяется метод UseMiddleware().
Так, изменим файл Program.cs следующим образом:

```

var builder = WebApplication.CreateBuilder();
var app = builder.Build();

app.UseMiddleware<TokenMiddleware>();

app.Run(async(context) => await context.Response.WriteAsync("Hello METANIT.COM"));

app.Run();

```


С помощью метода UseMiddleware<T> в конструктор объекта TokenMiddleware будет внедряться объект
для параметра `RequestDelegate next`. Поэтому явным образом передавать значение для этого параметра нам не нужно.


Запустим проект. И если мы не передадим через строку запроса параметр token или передадим для него значение, отличное от
"12345678", то браузер отобразит ошибку:
![Классы middleware в ASP.NET Core и C#](https://metanit.com./pics/2.46.png)


Если же будет передан корректный токен, то вызов `app.UseMiddleware<TokenMiddleware>()` передаст обработку запроса
в компонент middleware из `app.Run()`:
![Классы middleware и UseMiddleware в ASP.NET Core и C#](https://metanit.com./pics/2.47.png)


### Метод расширения для встраивания middleware


Также нередко для встраивания подобных компонентов middleware определяются специальные методы расширения.
Так, добавим в проект новый класс, который назовем TokenExtensions:

```

public static class TokenExtensions
{
 public static IApplicationBuilder UseToken(this IApplicationBuilder builder)
 {
 return builder.UseMiddleware<TokenMiddleware>();
 }
}

```


Здесь создается метод расширения для типа IApplicationBuilder. И этот метод встраивает компонент TokenMiddleware в конвейер
обработки запроса. Как правило, подобные методы возвращают объект IApplicationBuilder.


Теперь применим этот метод в коде программы в Program.cs:

```

var builder = WebApplication.CreateBuilder();
var app = builder.Build();

app.UseToken();

app.Run(async(context) => await context.Response.WriteAsync("Hello METANIT.COM"));

app.Run();

```


### Передача параметров


Изменим класс TokenMiddleware, чтобы он извне получал образец токена для сравнения:

```

public class TokenMiddleware
{
 private readonly RequestDelegate next;
 string pattern;
 public TokenMiddleware(RequestDelegate next, string pattern)
 {
 this.next = next;
 this.pattern = pattern;
 }

 public async Task InvokeAsync(HttpContext context)
 {
 var token = context.Request.Query["token"];
 if (token != pattern)
 {
 context.Response.StatusCode = 403;
 await context.Response.WriteAsync("Token is invalid");
 }
 else
 {
 await next.Invoke(context);
 }
 }
}

```


Образец токена, с которым идет сравнения, устанавливается через конструктор. Чтобы передать его в конструктор, изменим класс TokenExtensions:

```

public static class TokenExtensions
{
 public static IApplicationBuilder UseToken(this IApplicationBuilder builder, string pattern)
 {
 return builder.UseMiddleware<TokenMiddleware>(pattern);
 }
}

```


В метод `builder.UseMiddleware` можно передать набор значений, которые передаются в конструктор компонента middleware.


И при вызове метода расширения UseToken в него можно передать конкретное значение:

```

var builder = WebApplication.CreateBuilder();
var app = builder.Build();

app.UseToken("555555");

app.Run(async(context) => await context.Response.WriteAsync("Hello METANIT.COM"));

app.Run();

```

![Передача параметров в классы middleware в ASP.NET Core и C#](https://metanit.com./pics/2.48.png)










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

**Источник:** [https://metanit.com/sharp/aspnet6/2.15.php](https://metanit.com/sharp/aspnet6/2.15.php)
