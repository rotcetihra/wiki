# Подключение Entity Framework

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10|Руководство по ASP.NET Core 10]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 12. Работа с базой данных и Entity Framework|Глава 12. Работа с базой данных и Entity Framework]] / Подключение Entity Framework

[[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 11. Web API/Пример приложения Web API|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 12. Работа с базой данных и Entity Framework|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 12. Работа с базой данных и Entity Framework/Основные операции с данными в Entity Framework Core|Вперёд]]

**Дата написания:** 05.09.2026

Последнее обновление: 19.11.2025




-

-

-














Entity Framework представляет ORM-решение, которое позволяет автоматически связать классы языка C# с таблицами в базе данных. Entity Framework Core
поддерживает большинство популярных СУБД, таких как MS SQL Server, SQLite, MySQL, Postres. В данном случае мы будем работать через Entity Framework Core с базами данных в
SQLite как наиболее демократичный вариант, который не требует установки сервера и доступен на любой поддерживаемой архитектуре и платформе.


Детально ознакомиться с работой с Entity Framework Core можно в соответствуюшем [руководстве](../efcore), здесь же мы сосредоточимся
прежде всего на тех моментах, которые характерны для веб-приложения ASP.NET Core.


Для работы с базами данных SQLite через Entity Framework Core необходим пакет Microsoft.EntityFrameworkCore.SQLite.
По умолчанию он отсутствует в проекте, поэтому его надо добавить. Если мы работаем через .NET CLI, то для добавления пакета мы можем использовать следующую команду:

```
dotnet add package Microsoft.EntityFrameworkCore.Sqlite
```


При работе в Visual Studio можно использовать встроенный визуальный инструмент пакетного менеджера Nuget:
![Добавление Entity Framework Core в ASP.NET Core и C#](https://metanit.com./pics/12.1.png)


Далее добавим в проект класс, которые будет представлять данные. Пусть он будет называться User и будет иметь следующий код:

```

public class User
{
 public int Id { get; set; }
 public string Name { get; set; } = ""; // имя пользователя
 public int Age { get; set; } // возраст пользователя
}

```


Этот класс представляет те объекты, которые будут храниться в базе данных.


Для взаимодействия с базой данных через Entity Framework Core необходим контекст данных - класс, унаследованный от класса
Microsoft.EntityFrameworkCore.DbContext. Поэтому добавим в проект новый класс, который назовем
ApplicationContext (название класса контекста произвольное):

```

using Microsoft.EntityFrameworkCore;
public class ApplicationContext : DbContext
{
 public DbSet<User> Users { get; set; } = null!;
 public ApplicationContext(DbContextOptions<ApplicationContext> options)
 : base(options)
 {
 Database.EnsureCreated(); // создаем базу данных при первом обращении
 }
 protected override void OnModelCreating(ModelBuilder modelBuilder)
 {
 modelBuilder.Entity<User>().HasData(
 new User { Id = 1, Name = "Tom", Age = 37 },
 new User { Id = 2, Name = "Bob", Age = 41 },
 new User { Id = 3, Name = "Sam", Age = 24 }
 );
 }
}

```


Свойство DbSet представляет собой коллекцию объектов, которая сопоставляется с определенной таблицей в базе данных. То есть свойство Users будет представлять таблицу, в которой будут храниться объекты User.


Класс DbSet, как и другие типы, является ссылочным. А, начиная с C# 10 и .NET 6 автоматически применяется функциональность ссылочных
nullable-типов. И переменные/свойства тех типов, которые не являются nullable, следует инициализировать некотором значением перед
их использованием. Чтобы выйти из этой ситуации мы можем инициализировать свойство с помощью выражения null!, которое говорит, что данное свойство в принципе не будет иметь значение null.
Потому что в реальности конструктор базового класса DbContext гарантирует, что все свойства типа DbSet будут инициализированы и соответственно в принципе не будут иметь значение null.


В конструкторе класса ApplicationContext через параметр `options` будут передаваться настройки контекста данных.
А в самом конструкторе с помощью вызова `Database.EnsureCreated()` по определению модели будет создаваться база данных (если она отсутствует).


Кроме того, в методе OnModelCreating() настраивается некоторая начальная конфигурация модели. В частности, с помощью метода
`modelBuilder.Entity<User>().HasData()` в базу данных добавляются три начальных объекта


### Конфигурация и строка подключения


Чтобы подключаться к базе данных, нам надо задать параметры подключения. Это можно сделать либо в коде C#, либо в файле конфигурации.
Выберем второй способ. Для этого изменим файл appsettings.json. По умолчанию он содержит только настройки логгирования:

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


Теперь изменим его, добавив определение строки подключения:

```

{
 "ConnectionStrings": {
 "DefaultConnection": "Data Source=app.db"
 },
 "Logging": {
 "LogLevel": {
 "Default": "Information",
 "Microsoft.AspNetCore": "Warning"
 }
 },
 "AllowedHosts": "*"
}

```


В данном случае мы добавили параметр `ConnectionStrings` для хранения строк подключения. Этот параметр содержит одну строку подключения - с ключом `DefaultConnection` и значением
`Data Source=app.db`. Это значение собственно и представляет строку подключения.


Строка подключения также представляет собой набор параметров в виде "ключ=значения". В нашем случае для работы с базой данных SQLite достаточно одного параметра - "Data Source", который представляет адрес файла база данных.
В нашем случае база данных называется "app.db" (название файла произвольное).


### Добавление контекста данных EF Core в качестве сервиса


Контекст данных, через который идет взаимодействие с базой данных, передается в приложение в качестве сервиса через механизм внедрения зависимостей.
Поэтому для работы с Entity Framework Core необходимо добавить класс контекста данных в коллекцию сервисов приложения:

```

using Microsoft.EntityFrameworkCore;

var builder = WebApplication.CreateBuilder();

// получаем строку подключения из файла конфигурации
var connection = builder.Configuration.GetConnectionString("DefaultConnection");

// добавляем контекст ApplicationContext в качестве сервиса в приложение
builder.Services.AddDbContext<ApplicationContext>(options => options.UseSqlite(connection));

var app = builder.Build();

app.Run();

```


Для использования контекста данных ему надо передать строку подключения, которая выше была определена в файл конфигурации appsettings.json. Поэтому сначала считываем
строку подключения под названием "DefaultConnection":

```
string connection = builder.Configuration.GetConnectionString("DefaultConnection");
```


Для получения строки конфигурации для объекта IConfiguration, который представляет конфигурацию, определен метод расширения GetConnectionString(),
в который передается название строки подключения.


Для добавления контекста данных в качестве сервиса у объекта коллекции сервисов IServiceCollection определен метод AddDbContext(), который типизируется
классом контекста данных:

```

builder.Services.AddDbContext<ApplicationContext>(options => options.UseSqlite(connection));

```


Этот метод в качестве параметра принимает делегат, который настраивает подключение. В частности, с помощью вызова `options.UseSqlite()`
настраивается подключение к базе данных SQLite, а в качестве параметра в этот вызов передается строка подключения.


### Обращение к базе данных


Подключив контекст данных мы можем с его помощью обращаеться к базе данных. Например, в качестве теста получим добавляемые по умолчанию данные:

```

using Microsoft.EntityFrameworkCore;

var builder = WebApplication.CreateBuilder();
var connection = builder.Configuration.GetConnectionString("DefaultConnection");
builder.Services.AddDbContext<ApplicationContext>(options => options.UseSqlite(connection));

var app = builder.Build();

// получение данных
app.MapGet("/", (ApplicationContext db) => db.Users.ToList());

app.Run();

```


Поскольку контекст данных добавлен в сервисы, то мы можем его получить в обработчике конечной точки:

```
app.MapGet("/", (ApplicationContext db) => db.Users.ToList());
```


В данном случае клиенту отправляется список добавленных в БД по умолчанию объектов User в формате JSON:
![Взаимодействие с базой данных через Entity Framework Core в ASP.NET Core и C#](https://metanit.com./pics/12.2.png)











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

**Источник:** [https://metanit.com/sharp/aspnet6/12.1.php](https://metanit.com/sharp/aspnet6/12.1.php)
