# Передача конфигурации через IOptions

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10|Руководство по ASP.NET Core 10]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 6. Конфигурация|Глава 6. Конфигурация]] / Передача конфигурации через IOptions

[[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 6. Конфигурация/Проекция конфигурации на классы|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 6. Конфигурация|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 7. Логгирование/Ведение лога и ILogger|Вперёд]]

**Дата написания:** 05.09.2026

## Передача конфигурации через IOptions

Последнее обновление: 22.12.2021




-

-

-














Фреймворк ASP.NET Core реализует паттерн Options, который позволяет передавать конфигурацию не просто
как набор настроек в виде пар ключ-значение, а как объекты определенных классов.


Для применения этого паттерна в приложении у объекта IServiceCollection, который представляет коллекцию сервисов приложения, определен метод
Configure():

```

public static IServiceCollection Configure<TOptions>(this IServiceCollection services, IConfiguration config) where TOptions : class
public static IServiceCollection Configure<TOptions>(this IServiceCollection services, IConfiguration config, Action<BinderOptions> configureBinder) where TOptions : class
public static IServiceCollection Configure<TOptions>(this IServiceCollection services, string name, IConfiguration config) where TOptions : class
public static IServiceCollection Configure<TOptions>(this IServiceCollection services, string name, IConfiguration config, Action<BinderOptions> configureBinder)

```


Этот метод реализован как метод расширения для типа IServiceCollection. И все версии метода типизируются типом, объект которого надо передавать через
механизм внедрения зависимостей. И также все версии метода принимают в качестве одного из параметров объект конфигурации, на основе которой будет создаваться объект TOptions.


Допустим, у нас в проекте определен файл конфигурации person.json со следующим содержимым:

```

{
 "age": "37",
 "name": "Tom",
 "languages": [
 "English",
 "German",
 "Spanish"
 ],
 "company": {
 "title": "Microsoft",
 "country": "USA"
 }
}

```


Данный файл по сути описывает одного пользователя. Элемент name сопоставляется с именем пользвателя, age - с возрастом, languages представляет языки, которыми владеет
пользователь, а элемент company - компания, в которой пользователь работает. И мы хотим использовать эти данные в приложении как целостный объект.
Для этого добавим вначале в проект класс Person:

```

public class Person
{
 public string Name { get; set; } = "";
 public int Age { get; set; }
 public List<string> Languages { get; set; } = new();
 public Company? Company { get; set; }
}
public class Company
{
 public string Title { get; set; } = "";
 public string Country { get; set; } = "";
}

```


Для представления компании пользователя определен дополнительный класс Company. Но, как можно заметить, определение класса Person совпадает со структурой json-файла.


И чтобы передать конфигурационные настройки через объект Person, мы можем использовать сервис IOptions<TOptions>:

```

using Microsoft.Extensions.Options;

var builder = WebApplication.CreateBuilder();
builder.Configuration.AddJsonFile("person.json");
// устанавливаем объект Person по настройкам из конфигурации
builder.Services.Configure<Person>(builder.Configuration);

var app = builder.Build();

app.Map("/", (IOptions<Person> options) =>
{
 Person person = options.Value; // получаем переданные через Options объект Person
 return person;
});
app.Run();

```


Прежде всего необходимо связать объект Person, который будет передаваться через механизм внедреия зависимостей, с конфигурацией файла json.
Для этого метод `builder.Services.Configure()` типизирует типом Person и в качестве параметра получает конфигурацию приложения
(свойство builder.Configuration реализует интерфейс IConfiguration и поэтому может передаваться в качестве параметра):

```
builder.Services.Configure<Person>(builder.Configuration);
```


Далее через механиз внедрения зависимостей мы можем получить созданный объект через сервис `IOptions<Person>`:

```

app.Map("/", (IOptions<Person> options) =>
{
 Person person = options.Value; // получаем переданные через Options объект Person
 return person;
});

```


Причем через механизм DI передается не просто объект Person, а объект IOptions<Person>, из которого мы можем получим непосредственно
сам объект Person с помощью свойства Value.
![Паттерн Options и проекция конфигурации на классы в ASP.NET Core и C#](https://metanit.com./pics/6.20.png)


Другой пример: определим в проекте новый класс middleware - PersonMiddleware, который фактически будет выводить информацию о пользователе на веб-станицу:

```

using Microsoft.Extensions.Options;

var builder = WebApplication.CreateBuilder();
builder.Configuration.AddJsonFile("person.json");
builder.Services.Configure<Person>(builder.Configuration);

var app = builder.Build();

app.UseMiddleware<PersonMiddleware>();
app.Run();
public class PersonMiddleware
{
 private readonly RequestDelegate _next;
 public Person Person { get; }
 public PersonMiddleware(RequestDelegate next, IOptions<Person> options)
 {
 _next = next;
 Person = options.Value;
 }
 public async Task InvokeAsync(HttpContext context)
 {
 System.Text.StringBuilder stringBuilder = new();
 stringBuilder.Append($"<p>Name: {Person.Name}</p>");
 stringBuilder.Append($"<p>Age: {Person.Age}</p>");
 stringBuilder.Append($"<p>Company: {Person.Company?.Title}</p>");
 stringBuilder.Append("<h3>Languages</h3><ul>");
 foreach (string lang in Person.Languages)
 stringBuilder.Append($"<li>{lang}</li>");
 stringBuilder.Append("</ul>");

 await context.Response.WriteAsync(stringBuilder.ToString());
 }
}

```

![IOptions и передача конфигурации в класс middleware в ASP.NET Core и C#](https://metanit.com./pics/6.21.png)


### Настройка привязки конфгурации


При необходимости мы можем переопределить настройки с помощью перегрузки метода `services.Configure()`:

```

using Microsoft.Extensions.Options;

var builder = WebApplication.CreateBuilder();
builder.Configuration.AddJsonFile("person.json");
builder.Services.Configure<Person>(builder.Configuration);
builder.Services.Configure<Person>(opt =>
{
 opt.Age = 22;
});

var app = builder.Build();

app.Map("/", (IOptions<Person> options) =>
{
 Person person = options.Value; // получаем переданные через Options объект Person
 return person;
});
app.Run();

```


Также можно передавать отдельные секции конфигурации. Например, передадим секцию Company:

```

using Microsoft.Extensions.Options;

var builder = WebApplication.CreateBuilder();
builder.Configuration.AddJsonFile("person.json");
builder.Services.Configure<Person>(builder.Configuration);
builder.Services.Configure<Company>(builder.Configuration.GetSection("company"));

var app = builder.Build();

app.Map("/", (IOptions<Company> options) => options.Value);

app.Run();

```

![IOptions и привязка объекта к секции конфигурации в ASP.NET Core и C#](https://metanit.com./pics/6.22.png)










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

**Источник:** [https://metanit.com/sharp/aspnet6/6.8.php](https://metanit.com/sharp/aspnet6/6.8.php)
