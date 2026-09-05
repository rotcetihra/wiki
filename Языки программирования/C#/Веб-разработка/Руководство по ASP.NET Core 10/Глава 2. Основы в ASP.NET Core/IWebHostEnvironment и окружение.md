# IWebHostEnvironment и окружение

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10|Руководство по ASP.NET Core 10]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 2. Основы в ASP.NET Core|Глава 2. Основы в ASP.NET Core]] / IWebHostEnvironment и окружение

[[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 2. Основы в ASP.NET Core/Построение конвейера обработки запроса|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 2. Основы в ASP.NET Core|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 3. Dependency Injection/Внедрение зависимостей и IServiceCollection|Вперёд]]

**Дата написания:** 05.09.2026

## IWebHostEnvironment и окружение

Последнее обновление: 20.12.2021




-

-

-














Для взаимодействия с окружением, в котором запущено приложение, фреймфорк ASP.NET Core предоставляет интерфейс IWebHostEnvironment.
Этот интерфейс предлагает ряд свойств, с помощью которых мы можем получить информацию об окружении:


-

ApplicationName: хранит имя приложения

-

EnvironmentName: хранит название среды, в которой хостируется приложение

-

ContentRootPath: хранит путь к корневой папке приложения

-

WebRootPath: хранит путь к папке, в которой хранится статический контент приложения. По умолчанию это папка wwwroot

-

ContentRootFileProvider: возвращает реализацию интерфейса `Microsoft.AspNetCore.FileProviders.IFileProvider`,
которая может использоваться для чтения файлов из папки ContentRootPath

-

WebRootFileProvider: возвращает реализацию интерфейса `Microsoft.AspNetCore.FileProviders.IFileProvider`,
которая может использоваться для чтения файлов из папки WebRootPath


При разработке мы можем использовать эти свойства. Но наиболее часто при разработке придется сталкиваться со свойством EnvironmentName.
По умолчанию имеются три варианта значений для этого свойства: Development, Staging и Production. В проекте это свойство задается через установку
переменной среды `ASPNETCORE_ENVIRONMENT`. Текущее значение данного параметра задается в файле launchSettings.json, который располагается в проекте в папке Properties.
![файл launchSettings.json и переменная ASPNETCORE_ENVIRONMENT в ASP.NET Core и C#](https://metanit.com./pics/2.54.png)


Откроем данный файл:

```

{
 "iisSettings": {
 "windowsAuthentication": false,
 "anonymousAuthentication": true,
 "iisExpress": {
 "applicationUrl": "http://localhost:56234",
 "sslPort": 44384
 }
 },
 "profiles": {
 "HelloApp": {
 "commandName": "Project",
 "dotnetRunMessages": true,
 "launchBrowser": true,
 "applicationUrl": "https://localhost:7256;http://localhost:5256",
 "environmentVariables": {
 "ASPNETCORE_ENVIRONMENT": "Development"
 }
 },
 "IIS Express": {
 "commandName": "IISExpress",
 "launchBrowser": true,
 "environmentVariables": {
 "ASPNETCORE_ENVIRONMENT": "Development"
 }
 }
 }
}

```


Здесь можно увидеть, что переменная "ASPNETCORE_ENVIRONMENT" встречается два раза - для запуска через IISExpress и для запуска через Kestrel.
В обоих случаях она имеет значение Development. Но мы можем поменять значение этой переменной.


Для определения значения этой переменной для интерфейса IWebHostEnvironment определены специальные методы расширения:


-

IsEnvironment(string envName): возвращает `true`, если имя среды равно значению параметра envName

-

IsDevelopment(): возвращает `true`, если имя среды - Development

-

IsStaging(): возвращает `true`, если имя среды - Staging

-

IsProduction(): возвращает `true`, если имя среды - Production


Данная функциональность позволяет нам выполнять определенный код в зависимости от того, на какой стадии находится приложение. Если приложение в процессе
разработки, то мы можем выполнять один код, а при разветывании для полноценного использования другой код:

```

var builder = WebApplication.CreateBuilder();
WebApplication app = builder.Build();

if (app.Environment.IsDevelopment())
{
 app.Run(async (context) => await context.Response.WriteAsync("In Development Stage"));
}
else
{
 app.Run(async (context) => await context.Response.WriteAsync("In Production Stage"));
}
Console.WriteLine($"{app.Environment.EnvironmentName}");

app.Run();

```


Так, если мы посмотрим на код класса [WebApplicationBuilder](https://github.com/dotnet/aspnetcore/blob/main/src/DefaultBuilder/src/WebApplicationBuilder.cs), который применяется для создания приложения,
то мы там можем увидеть там следующие строки:

```

if (context.HostingEnvironment.IsDevelopment())
{
 app.UseDeveloperExceptionPage();
}

```


Здесь если имя среды имеет значение "Development" (то есть приложение находится в состоянии разработки), то при ошибке разработчик увидит
детальное описание ошибки.
Если же приложение развернуто на хостинге и соответственно имеет другое имя хостирующей среды, то простой пользователь при ошибке ничего не увидит.
Таким образом, в зависимости от стадии, на которой находится проект, мы можем скрывать или задействовать часть функционала приложения.


Если мы хотим поменять значение среды, необязательно изменять файл launchSettings.json. Это можно сделать также программно:

```

var builder = WebApplication.CreateBuilder();
WebApplication app = builder.Build();

app.Environment.EnvironmentName = "Production";

```


### Определение своих состояний среды


Хотя по умолчанию среда может принимать три состояния: Development, Staging, Production, но мы можем при желании вводить новые значения. Например, нам надо отслеживать какие-то дополнительные состояния. Это можно сделать через изменение файла
launchSettings.json либо программно.


Например, изменим название среды на "Test" (значение может быть произвольное):

```

var builder = WebApplication.CreateBuilder();
WebApplication app = builder.Build();

app.Environment.EnvironmentName = "Test"; // изменяем название среды на Test

if (app.Environment.IsEnvironment("Test")) // Если проект в состоянии "Test"
{
 app.Run(async (context) => await context.Response.WriteAsync("In Test Stage"));
}
else
{
 app.Run(async (context) => await context.Response.WriteAsync("In Development or Production Stage"));
}

app.Run();

```

![Окружение и переменные среды в ASP.NET Core и C#](https://metanit.com./pics/2.55.png)


Также можно изменить значение "ASPNETCORE_ENVIRONMENT" на "Test" или любое другой в файле launchSettings.json для используемого профиля:

```

{
 "iisSettings": {
 "windowsAuthentication": false,
 "anonymousAuthentication": true,
 "iisExpress": {
 "applicationUrl": "http://localhost:56234",
 "sslPort": 44384
 }
 },
 "profiles": {
 "HelloApp": {
 "commandName": "Project",
 "dotnetRunMessages": true,
 "launchBrowser": true,
 "applicationUrl": "https://localhost:7256;http://localhost:5256",
 "environmentVariables": {
 "ASPNETCORE_ENVIRONMENT": "Test"
 }
 },
 "IIS Express": {
 "commandName": "IISExpress",
 "launchBrowser": true,
 "environmentVariables": {
 "ASPNETCORE_ENVIRONMENT": "Development"
 }
 }
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

**Источник:** [https://metanit.com/sharp/aspnet6/2.17.php](https://metanit.com/sharp/aspnet6/2.17.php)
