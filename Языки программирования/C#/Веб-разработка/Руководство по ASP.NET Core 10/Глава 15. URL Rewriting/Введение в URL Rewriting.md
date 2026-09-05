# Введение в URL Rewriting

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10|Руководство по ASP.NET Core 10]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 15. URL Rewriting|Глава 15. URL Rewriting]] / Введение в URL Rewriting

[[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 14. CORS и кросс-доменные запросы/Глобальная и локальная настройка CORS|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 15. URL Rewriting|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 15. URL Rewriting/Правила IIS для URL Rewriting|Вперёд]]

**Дата написания:** 05.09.2026

## Введение в URL Rewriting

Последнее обновление: 03.11.2022




-

-

-














Функциональность URL Rewriting позволяет контролировать доступ к определенным URL-адресам в приложении. В частности, мы можем
выполнить переопределение адресов, которые используются для доступа к ресурсам приложения. Например, URL Rewriting позволяет решить такие стандартные проблемы, как
перенаправление с домена с www на домен без www и наоборот или перенаправление с протокола http на https.


URL Rewriting реализуется до того, как запрос попадет в систему маршрутизации, и начнется его непосредственное выполнение в конвейере MVC. Запрошенный адрес
изначально может отсутствовать в приложении, однако URL Rewriting может изменить этот адрес на любой приемлемый.


Для подключения компонента URL Rewriting используется метод расширения UseRewriter(), который в качестве параметра принимает
объект RewriteOptions, задающий все правила переопределения адресов URL:

```

using Microsoft.AspNetCore.Rewrite; // Пакет с middleware URL Rewriting

var builder = WebApplication.CreateBuilder();

var app = builder.Build();

// подключаем URL Rewriting
var options = new RewriteOptions();
app.UseRewriter(options);

app.MapGet("/home", async context => await context.Response.WriteAsync("Hello World!"));

app.Run();

```


Правда, в данном случае для RouteOptions пока еще не определено никаких правил переопределения URL, которые мы можем задать с помощью специальных методов:


-

AddRedirect(): выполняет переадресацию с отправкой статусного кода HTTP 301

-

AddRewrite(): подменяет один адрес другим

-

AddRedirectToWww(): выполняет переадресацию на поддомен WWW

-

AddRedirectToWwwPermanent(): выполняет переадресацию на поддомен WWW с отправкой статусного кода HTTP 301 (постоянная переадресация)

-

AddRedirectToNonWww(): выполняет переадресацию с поддомена WWW на основной домен

-

AddRedirectToNonWwwPermanent(): выполняет переадресацию с поддомена WWW на основной домен с отправкой статусного кода HTTP 301 (постоянная переадресация)

-

AddRedirectToHttps(): выполняет переадресацию на протокол HTTPS

-

AddRedirectToHttpsPermanent(): выполняет переадресацию на протокол HTTPS с отправкой статусного кода HTTP 301 (постоянная переадресация)

-

AddIISUrlRewrite(): в качестве источника правил для переопределения URL использует правила для IIS

-

AddApacheModRewrite(): в качестве источника правил для переопределения URL использует правила для Apache


### AddRedirect


Метод `AddRedirect()` реализован как метод расширения для типа RewriteOptions и имеет две формы:

```

public static RewriteOptions AddRedirect (this RewriteOptions options, string regex, string replacement);
public static RewriteOptions AddRedirect (this RewriteOptions options, string regex, string replacement, int statusCode);

```


-

В качестве параметра `regex` метод принимает регулярное выражение, которому должен соответствовать входящий адрес URL.
В качестве адреса в метод AddRedirect передается та часть URL, которая образуется с помощью объединения значений `Request.Path` и
`Request.QueryString`. То есть, если полный запрошенный адрес `http://localhost:1234/home/index?id=4`, то в метод AddRedirect передается
`home/index?id=4`

-

Параметр `replacement` представляет выражение, которое указывает, по какому адресу нужно выполнять переадресацию.

-

Параметр `statusCode` устанавливает отправляемый статусный код.


Например, нам надо, чтобы с адресов с конечным слешем (например, `localhost/home/`) шло перенаправление на тот же адрес только без слеша
(например, `localhost/home`):

```

using Microsoft.AspNetCore.Rewrite; // Пакет с middleware URL Rewriting

var builder = WebApplication.CreateBuilder();

var app = builder.Build();

// подключаем URL Rewriting
var options = new RewriteOptions().AddRedirect("(.*)/$", "$1");
app.UseRewriter(options);

app.MapGet("/home", async context => await context.Response.WriteAsync("Hello World!"));

app.Run();

```


Регулярное выражение `"(.*)/$"` указывает на любой адрес, который завершается слешем. Второй параметр указывает, что в качестве адреса
для перенаправления будет использоваться та часть исходного URL, которая идет до слеша: `(.*)`. То есть "$1" указывает на первую группу в регулярном выражении "(.*)/$".


То есть в данном случае удаляется концевой слеш (например, перенаправляется с "localhost:1234/home/" на "localhost:1234/home").


Рассмотрим другую ситуацию. Например, мы хотим перенаправлять с адреса home/ на home/index:

```

using Microsoft.AspNetCore.Rewrite; // Пакет с middleware URL Rewriting

var builder = WebApplication.CreateBuilder();

var app = builder.Build();

// подключаем URL Rewriting
var options = new RewriteOptions()
 .AddRedirect("home[/]?$", "home/index"); // переадресация с home на home/index
app.UseRewriter(options);

app.MapGet("/", async context => await context.Response.WriteAsync("Hello World!"));
app.MapGet("/home", async context => await context.Response.WriteAsync("Home Page!"));
app.MapGet("/home/index", async context => await context.Response.WriteAsync("Home Index Page!"));

app.Run();

```


Для примера с помощью метода `app.MapGet` заданы тестовые маршруты, в итоге при обращении по адресу "home" произойдет переадресация
на адрес "home/index", и мы увидим в браузере строку "Home Index Page!".


При этом можно задать последовательно сразу несколько правил:

```

var options = new RewriteOptions()
 .AddRedirect("home[/]?$", "home/index") // переадресация с home на home/index
 .AddRedirect("(.*)/$", "$1"); // удаление концевого слеша

```


### AddRewrite


Метод `AddRewrite()` подменяет входящий адрес другим. Первый параметр метода указывает на регулярное выражение, которому должен соответствовать
адрес. Второй параметр указывает, на какой адрес надо подменить входящий. Третий параметр - булевое значение устанавливает, надо ли прекратить применение остальных правил,
если адрес соответствует выражению из первого параметра. Например:

```

using Microsoft.AspNetCore.Rewrite; // Пакет с middleware URL Rewriting

var builder = WebApplication.CreateBuilder();

var app = builder.Build();

// подключаем URL Rewriting
var options = new RewriteOptions()
 .AddRedirect("(.*)/$", "$1")
 .AddRewrite("home/index", "home/about", skipRemainingRules: false);
app.UseRewriter(options);

app.MapGet("/", async context => await context.Response.WriteAsync("Hello World!"));
app.MapGet("/home/about", async context =>
 await context.Response.WriteAsync($"About: {context.Request.Path}"));
app.MapGet("/home/index", async context =>
 await context.Response.WriteAsync("Home Index Page!"));

app.Run();

```


Правило

```
AddRewrite("home/index", "home/about", skipRemainingRules: false);
```


указывает, что при запросе "home/index" в реальности запрос будет сопоставляться с маршрутом "home/about"
![URL Rewriting и AddRewrite в ASP.NET Core и C#](https://metanit.com./pics/15.2.png)


При этом переадресации как таковой нет, статусный код 301/302 не отправляется клиенту.


### Регистрозависимость


Стоит отметить, что по умолчанию шаблоны в методах Addredirect/AddRewrite регистрозависимы. Что это значит? Возьмем в предыдущем примере следующее правило:

```

AddRewrite("home/index", "home/about", skipRemainingRules: false);

```


При запросе "home/index" запрос будет сопоставляться с маршрутом "home/about", однако запрос "Home/Index" по прежнему будет сопоставляться с запросом "home/index".
![UrlRewriting и переадресация в ASP.NET Core и C#](https://metanit.com./pics/15.1.png)


Но мы можем выйти из данной ситуации, предваряя шаблон элементом `(?i)`:

```

var options = new RewriteOptions()
 .AddRedirect("(.*)/$", "$1")
 //шаблон регистронезависимый
 .AddRewrite("(?i)home/index", "home/about", skipRemainingRules: false);

```


### Элементы регулярных выражений в URL Rewriting


Ключевым элементом, который используется при определении шаблонов адресов, являются группы - набор выражений, которые заключаются в скобки.


Например, в рассмотренном выше примере с удалением концевого слеша применялась одна группа:

```
"(.*)/$"
```


то есть знак точки "." означает любой символ, знак звездочки "*" означает, что таких символов может быть произвольное количество. И все это объединяется в одну группу -
"(.*)". Таким образом, в данном случае группой будет все символы, которые идут до конечного слеша.


При создании паттерна для редиректа или рерайтинга мы можем ссылать на группу по номеру. В примере с концевым слешем определяется одна группа,
поэтому мы можем к ней обратиться через "$1" - после символа $ идет номер группы.


Для понимания работы групп при рерайтинге/редиректе рассмотрим несколько примеров:

```

var options = new RewriteOptions()
 .AddRedirect("(.*)/$", "$1")
 .AddRewrite(@"home/index/(\d+)", "home/about?id=$1", skipRemainingRules: false);

```


В данном случае если адрес соответствует выражению "home/index/(\d+)" (например, "home/index/3"), то фактически происходит обращение по адресу
"home/about?id=$1" - $1 здесь также указывает на первую группу в регулярном выражении - (\d+).


Другой пример. Определим следующее правило url rewriting:

```

using Microsoft.AspNetCore.Rewrite; // Пакет с middleware URL Rewriting

var builder = WebApplication.CreateBuilder();

var app = builder.Build();

// подключаем URL Rewriting
var options = new RewriteOptions()
 .AddRewrite(@"product/(\w+)/(\d+)",
 "home/products?cat=$1&id=$2",
 skipRemainingRules: false);
app.UseRewriter(options);

app.MapGet("/", async context =>
{
 await context.Response.WriteAsync("Hello World!");
});
app.MapGet("/home/products", async context =>
{
 await context.Response.WriteAsync($"cat: {context.Request.Query["cat"]} id: {context.Request.Query["id"]}");
});
app.Run();

```


В данном случае используется следующее правило:

```

AddRewrite(@"product/(\w+)/(\d+)", "home/products?cat=$1&id=$2",
 skipRemainingRules: false);

```


Это правило будет транслировать любой запрос типа "product/tablet/23" в запрос типа "home/products/cat=tablet?id=23". То есть теперь у нас две группы: (\w+) и (\d+).
Соответственно мы к ним можем обратиться через $1 и $2.
![Переопределение адресов приложения и URL-rewriting в ASP.NET Core и C#](https://metanit.com./pics/15.3.png)


В заключении стоит отметить, что использование url rewriting увеличивает накладные расходы на обработку запроса.
Поэтому стоит по возможности избегать сложных комплексных правил переопределения строки запроса.


Кроме того, Rewriting Middleware не покрывает всех возможностей нативных модулей в IIS, Apache, Nginx, которые обеспечивают URL-rewriting. Также, нативные модули выше упомянутых веб-серверов демонстрируют
большую производительность.










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

**Источник:** [https://metanit.com/sharp/aspnet6/15.1.php](https://metanit.com/sharp/aspnet6/15.1.php)
