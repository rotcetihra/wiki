# Конфигурация в файлах JSON, XML и Ini

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10|Руководство по ASP.NET Core 10]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 6. Конфигурация|Глава 6. Конфигурация]] / Конфигурация в файлах JSON, XML и Ini

[[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 6. Конфигурация/Нефайловые провайдеры конфигурации|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 6. Конфигурация|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 6. Конфигурация/Конфигурация по умолчанию и объединение конфигураций|Вперёд]]

**Дата написания:** 05.09.2026

## Конфигурация в файлах JSON, XML и Ini

Последнее обновление: 21.12.2021




-

-

-














### Конфигурация в JSON


Как правило, для хранения конфигурации в приложении ASP.NET Core используются файлы json. Для работы с файлами json применяется провайдер
JsonConfigurationProvider, а для загрузки конфигурации из json применяется метод расширения AddJsonFile().


По умолчанию в проекте уже есть файл конфигурации json - appsettings.json, а также appsettings.Development.json, которые загружаются
по умолчанию в приложении и которые мы можем использовать для хранения конфигурационных настроек.
![Файл appsettings.json и appsettings.Development.json в ASP.NET Core и C#](https://metanit.com./pics/6.6.png)


Например, код файла appsettings.json:

```

{
 "Logging": {
 "LogLevel": {
 "Default": "Information",
 "Microsoft.AspNetCore": "Warning"
 }
 },
 "AllowedHosts": "*"
}

```


Здесь определяются настройки логгирования (элемент "Logging") и разрешенные хосты (элемент "AllowedHosts"). Одни элементы могут иметь вложенные элементы.
Аналогичным образом можно задать другие необходимые настройки или удалить ранее определенные.


Однако в данном случае для примера возьмем новый файл json. Итак, добавим в проект новый файл config.json:
![Конфигурация json в ASP.NET Core и C#](https://metanit.com./pics/6.8.png)


И определим в нем следующее содержимое:

```

{
 "person": "Tom",
 "company": "Microsoft"
}

```


Здесь задается два элемента с ключами "person" и "company". Используем эти настройки в приложении:

```

var builder = WebApplication.CreateBuilder();
var app = builder.Build();

builder.Configuration.AddJsonFile("config.json");

app.Map("/", (IConfiguration appConfig) => $"{appConfig["person"]} - {appConfig["company"]}");

app.Run();

```


Для установки конфигурации из json-файла название файла передается в метод `AddJsonFile()`.
![Конфигурация из файла json в ASP.NET Core и C#](https://metanit.com./pics/6.9.png)


При определении настроек в файле json нам надо учитывать, что они должны иметь уникальные ключи. Но при этом мы можем использовать для конфигурации
более чем одного файла:

```

builder.Configuration
 .AddJsonFile("config.json")
 .AddJsonFile("otherconfig.json");

```


И если во втором файле есть настройки, которые имеют тот же ключ, что и настройки первого файла, то происходит переопределение настроек:
настройки из второго файла заменяют настройки первого.


Но json может хранить также более сложные по составу объекты, например:

```

{
 "person": {"profile": {"name": "Tomas", "email": "tom@gmail.com"}},
 "company": { "name": "Microsoft"}
}

```


И чтобы обратиться к этой настройке, нам надо использовать знак двоеточия для обращения к иерархии настроек:

```

var builder = WebApplication.CreateBuilder();
var app = builder.Build();

builder.Configuration.AddJsonFile("config.json");

app.Map("/", (IConfiguration appConfig) =>
{
 var personName = appConfig["person:profile:name"];
 var companyName = appConfig["company:name"];
 return $"{personName} - {companyName}";
});

app.Run();

```


### Конфигурация в XML


За использование конфигурации в XML-файле отвечает провайдер XmlConfigurationProvider. Для загрузки xml-файла
применяется метод расширения AddXmlFile().


Итак, добавим в проект новый xml-файл, который назовем config.xml. Затем изменим его код на следующий:

```

<?xml version="1.0" encoding="utf-8" ?>
<configuration>
 <person>Tom</person>
 <company>Microsoft</company>
</configuration>

```


Здесь определены два элемента person и company, которые представляют конфигурационные настройки.


Обратите внимание, что у файла xml в свойствах должно быть выставлено копирование при компиляции в выходную папку приложения:
![Конфигурация из файла XML в ASP.NET Core и C#](https://metanit.com./pics/6.10.png)


Теперь используем этот файл:

```

var builder = WebApplication.CreateBuilder();
var app = builder.Build();

builder.Configuration.AddXmlFile("config.xml");

app.Map("/", (IConfiguration appConfig) => $"{appConfig["person"]} - {appConfig["company"]}");

app.Run();

```


Если у нас файл конфигурации имеет разные уровни вложенности, например:

```

<?xml version="1.0" encoding="utf-8" ?>
<configuration>
 <person>
 <profile>
 <name>Tomas</name>
 <email>toma@gmail.com</email>
 </profile>
 </person>
 <company>
 <name>Microsoft</name>
 </company>
</configuration>

```


то мы можем обращаться к этим уровням также, как и в файле json:

```

app.Map("/", (IConfiguration appConfig) =>
{
 var personName = appConfig["person:profile:name"];
 var companyName = appConfig["company:name"];
 return $"{personName} - {companyName}";
});

```


### Конфигурация в ini-файлах


Для работы с конфигурацией INI применяется провайдер IniConfigurationProvider. А для загрузки конфигурации из INI-файла нам надо использовать метод расширения AddIniFile().


Например, добавим в проект текстовый файл и переименуем его в config.ini.
![Конфигурация из файла ini в ASP.NET Core и C#](https://metanit.com./pics/6.11.png)


Определим в этом файле следующее содержимое:

```

person="Bob"
company="Microsoft"

```


Подключим конфигурацию из этотого файла в приложении:

```

var builder = WebApplication.CreateBuilder();
var app = builder.Build();

builder.Configuration.AddIniFile("config.ini");

app.Map("/", (IConfiguration appConfig) => $"{appConfig["person"]} - {appConfig["company"]}");

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

**Источник:** [https://metanit.com/sharp/aspnet6/6.3.php](https://metanit.com/sharp/aspnet6/6.3.php)
