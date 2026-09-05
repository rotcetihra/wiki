# Первое приложение на ASP.NET Core с .NET CLI

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10|Руководство по ASP.NET Core 10]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 1. Введение в ASP.NET Core|Глава 1. Введение в ASP.NET Core]] / Первое приложение на ASP.NET Core с .NET CLI

[[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 1. Введение в ASP.NET Core/Что такое ASP.NET Core|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 1. Введение в ASP.NET Core|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 1. Введение в ASP.NET Core/Первое приложение в Visual Studio|Вперёд]]

**Дата написания:** 05.09.2026

Последнее обновление: 19.11.2025




-

-

-














Создадим первую программу на ASP.NET Core. Что нам для этого потребуется? Прежде всего необходим текстовый редактор для написания кода программы.
В данном случае я буду использовать в качестве текстового редактора [Visual Studio Code](https://code.visualstudio.com/download)


Также для компиляции и запуска программы нам потребуется .NET SDK. В данном случае мы для создания и запуска проекта мы будем использовать встроенную инфраструктуру .NET CLI, которая устанавливается вместе с .NET SDK. Процесс установки был описан в статье [Первая программа на C# с .NET CLI](https://metanit.com/sharp/tutorial/1.3.php)


После установки .NET SDK определим для проектов какую-нибудь папку. Например, в моем случае это будет папка C:\dotnet\aspnet.
Откроем терминал/командную строку и перейдем к созданной папке проекта с помощью команды cd

```
cd C:\dotnet\aspnet
```


Для создания проекта в .NET CLI применяется команда dotnet new, после которой указывается тип проекта. Для ASP.NET Core есть ряд встроенных типов проектов. В данном случае
мы будем использовать самый простейший тип - web. Кроме того, с помощью опции `-o` мы можем указать имя проекта и одновременно каталога, который создается для этого проекта.
Если мы не используем эту опцию, то каталог создается в текущей папке. Поэтому введем в терминале команду

```
dotnet new web -o helloapp
```


В данном случае проект будет называться "helloapp". После создания проекта перейдем в него с помощью команды cd:

```

c:\Users\eugen> cd c:\dotnet\aspnet
c:\dotnet\aspnet> dotnet new web -o helloapp
The template "ASP.NET Core Empty" was created successfully.

Processing post-creation actions...
Restoring C:\dotnet\aspnet\helloapp\helloapp.csproj:
Restore succeeded.


c:\dotnet\aspnet> cd helloapp
c:\dotnet\aspnet\helloapp>

```


После выполнения этой команды у нас будет создан следующий проект:
![Первый проект ASP.NET Core на C# в Visual Studio Code](https://metanit.com./pics/1.28.png)


### Структура проекта ASP.NET Core


Рассмотрим базовую структуру простейшего стандартного проекта ASP.NET Core:


-

Dependencies: все добавленные в проект пакеты и библиотеки, иначе говоря зависимости

-

Properties: узел, который содержит некоторые настройки проекта. В частности, в файле launchSettings.json описаны
 настройки запуска проекта, например, адреса, по которым будет запускаться приложение.

-

appsettings.json: файл конфигурации приложения в формате json

-

appsettings.Development.json: версия файла конфигурации приложения, которая используется в процессе разработки

-

helloapp.csproj: стандартный файл проекта C#, который соответствует назанию проекта (по умолчанию названию каталога) и описывает все его настройки.

-

Program.cs: главный файл приложения, с которого и начинается его выполнение. Код этого файла настраивает и запускает веб-приложение




Например, посмотрим на содержимое файла helloapp.csproj

```

<Project Sdk="Microsoft.NET.Sdk.Web">

 <PropertyGroup>
 <TargetFramework>net10.0</TargetFramework>
 <Nullable>enable</Nullable>
 <ImplicitUsings>enable</ImplicitUsings>
 </PropertyGroup>

</Project>

```


Ключевой компонент здесь - атрибут `Sdk="Microsoft.NET.Sdk.Web"`, который собственно и определяет, что приложение будет использовать SDK "Microsoft.NET.Sdk.Web", который предназначен
именно для веб-проектов.


### Запуск проекта




Проект по умолчанию не представляет какой-то грандиозной функциональности, тем не менее этот проект мы уже можем запустить. Итак, запустим проект. Для этого выполним команду

```
dotnet run
```


Полный вывод консоли:

```

C:\dotnet\aspnet\helloapp>dotnet run
Using launch settings from C:\dotnet\aspnet\helloapp\Properties\launchSettings.json...
Building...
info: Microsoft.Hosting.Lifetime[14]
 Now listening on: http://localhost:5197
info: Microsoft.Hosting.Lifetime[0]
 Application started. Press Ctrl+C to shut down.
info: Microsoft.Hosting.Lifetime[0]
 Hosting environment: Development
info: Microsoft.Hosting.Lifetime[0]
 Content root path: C:\dotnet\aspnet\helloapp

```

 ![запуск проекта ASP.NET Core и C# с помощью .NET CLI](https://metanit.com./pics/1.29.png)


При запуске в консоли мы можем увидеть адрес, по которому мы можем обращаться к приложению. В моем случае это адрес "http://localhost:5204". И я могу обратиться по этому адресу к приложению
 в браузере и увидеть в нем строку "Hello World!" - результат работы кода по умолчанию из файла Program.cs:
 ![Первое приложение на ASP.NET Core на С# с .NET CLI](https://metanit.com./pics/1.30.png)



### Запуск приложения и файл Program.cs




Рассмотрим код файла Program.cs, который создает подобное приложение:

```

 var builder = WebApplication.CreateBuilder(args);
 var app = builder.Build();

 app.MapGet("/", () => "Hello World!");

 app.Run();


```



Это так называемое Minimal API - упрощенная минизированная модель для запуска веб-приложения в ASP.NET.


Приложение в ASP.NET Core представляет объект Microsoft.AspNetCore.Builder.WebApplication. Этот объект настраивает всю
 конфигурацию приложения, его маршруты, используемые зависимости и т.д. Для создания объекта WebApplication необходим специальный класс-строитель - WebApplicationBuilder. И в файле Program.cs вначале создается данный объект
 с помощью статического метода `WebApplication.CreateBuilder`:

```
var builder = WebApplication.CreateBuilder(args);
```



В качестве параметра в метод передаются аргументы, которые передаются приложению при запуске.


Получив объект WebApplicationBuilder, у него вызывается метод Build(), который собствено и
 создает объект WebApplication:

```
var app = builder.Build();
```



С помощью объекта WebApplication можно настроить всю инфраструктуру приложения - его конфигурацию, маршруты и так далее. В
 файле Program.cs по умолчанию для приложения определяется один маршрут:

```
app.MapGet("/", () => "Hello World!");
```



Метод MapGet() в качестве первого параметра принимает путь, по которому можно обратиться к приложению. В данном случае это путь "/", то есть
 по сути корень веб-приложения - имя домена и порта, после которых может идти слеш, например, `https://localhost:7256/`


В качестве второго параметра в метод MapGet() передаются обработчик запроса по этому маршруту в виде функции. Здесь это лямбда-выражение,
 которое возвращает строку "Hello World!". Именно поэтому при обращении к приложению мы увидим данную строку в браузере.


И в конце необходимо запустить приложение. Для этого у класса WebApplication вызывается метод Run():

```
app.Run();
```



В итоге запустится приложение в виде консоли, и мы сможем обращаться к приложению из различных браузеров.












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

**Источник:** [https://metanit.com/sharp/aspnet6/1.3.php](https://metanit.com/sharp/aspnet6/1.3.php)
