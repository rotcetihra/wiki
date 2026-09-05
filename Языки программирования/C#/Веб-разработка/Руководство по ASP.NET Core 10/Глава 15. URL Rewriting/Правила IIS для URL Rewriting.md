# Правила IIS для URL Rewriting

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10|Руководство по ASP.NET Core 10]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 15. URL Rewriting|Глава 15. URL Rewriting]] / Правила IIS для URL Rewriting

[[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 15. URL Rewriting/Введение в URL Rewriting|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 15. URL Rewriting|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 15. URL Rewriting/Применение правил Apache для URL Rewriting|Вперёд]]

**Дата написания:** 05.09.2026

## Правила IIS для URL Rewriting

Последнее обновление: 09.05.2022




-

-

-














В более ранних технологиях на платформе ASP.NET (например, в ASP.NET MVC 5) правила для URL Rewriting задавались в основном для IIS с помощью файла конфигурации web.config. И в ASP.NET Core мы также можем
использовать все эти правила с помощью специального метода AddIISUrlRewrite().


Итак, добавим в корень проекта новый xml-файл urlrewrite.xml:

```

<rewrite>
 <rules>
 <rule name="Redirect from home to home/index">
 <match url = "^home$"/>
 <conditions>
 <add input="{REQUEST_URI}" pattern="home" />
 </conditions>
 <action type="Redirect" url ="home/index" />
 </rule>
 </rules>
</rewrite>

```


Здесь определено одно правило, которое выполняет переадресацию с адреса "/home" на адрес "/home/index". Теперь применим это правило в классе Startup:

```

using Microsoft.AspNetCore.Rewrite; // Пакет с middleware URL Rewriting

var builder = WebApplication.CreateBuilder();

var app = builder.Build();

IHostEnvironment? env = app.Services.GetService<IHostEnvironment>();
if(env is not null)
{
 var options = new RewriteOptions()
 .AddIISUrlRewrite(env.ContentRootFileProvider, "urlrewrite.xml");
 app.UseRewriter(options);
}

app.MapGet("/", async context => await context.Response.WriteAsync("Hello World!"));
app.MapGet("/home", async context =>
 await context.Response.WriteAsync("Home Page!"));
app.MapGet("/home/index", async context =>
 await context.Response.WriteAsync("Home Index Page!"));

app.Run();

```


В качестве первого параметра в `AddIISUrlRewrite` передается провайдер файлов. В данном случае используем встроенный провайдер из добавлемого по умолчанию сервиса IHostEnvironment.


Второй параметр представляет путь к файлу.


Также загружать файл конфигурации следующим образом:

```

using System.IO;

using (StreamReader iisReader = File.OpenText("urlrewrite.xml"))
{
 var options = new RewriteOptions().AddIISUrlRewrite(iisReader);
 app.UseRewriter(options);
}

```


Все правила определяются в элементе <rules>. Каждое правило, представленное элементом `<rule>`, состоит из трех частей:


-

Pattern – выражение, которому должна соответствовать строка запроса и которое задается в элементе `<match>`

-

Conditions – различные дополнительные условия, которым должен соответствовать URL-адрес.
Например, значения HTTP-заголовков, пути к файлам и т.д.

-

Action – действие, которое должно выполняться, если строка URL соответствует регулярному выражению в Pattern и
условиям Conditions


Мы можем использовать несколько правил одновременно, но их выполнение не всегда обязательно. Поэтому у каждого элемента `rule`
определен атрибут `StopProcessing`. Если имеет значение `true`, то после выполнения действия в элементе `<action>` адрес URL,
создаваемый данным правилом, передается в конвейер обработки запроса, а другие правила не будут обрабатываться.


Переопределение URL имеет следующий порядок действий:


1.

Строка запроса сравнивается с выражением в элементе match. Если обнаружится, что запрошенный адрес не соответствует выражению, то
модуль URL Rewrite Module прекращает обрабатывать текущее правило и переходит к следующему (если задано несколько правил)

2.

Если строка запроса соответствует выражению в элементе match и при этом не задано никаких дополнительных условий с помощью элемента
`<conditions>`, то URL Rewrite Module выполняет действие, которое определено в правиле с помощью элемента `<action>`.

3.

Если строка запроса соответствует выражению в элементе match и также определены дополнительные условия, то URL Rewrite Module проверяет эти условия. И если URL соответствует этим условиям,
то выполняется действие action


### Определение условий


Условия, задаваемые элементом `<conditions>`, определяют дополнительную логику оценки URL на соответствие правилу.
Каждое отдельное условие задается с помощью элемента `<add >` и настраивается с помощью следующих атрибутов:


-

`input`: определяет объект, который будет использоваться условием для оценки. В частности, в примере выше используется
`input="{REQUEST_URI}"`, где "REQUEST_URI" представляет переменную сервера, хранящую запрошенный адрес url. Тут также могут использоваться и другие переменные сервера.

-

`pattern`: определяет регулярное выражение, которому должен соответствовать объект

-

`matchType`: принимает следующие значения:


 -

`Pattern`: в этом случае объект (в данном случае адрес URL) сопоставляется с выражением в атрибуте pattern. При других значениях
атрибут pattern не учитывается

 -

`IsFile`: определяет, является ли объект (адрес URL) файлом в файловой системе

 -

`IsDirectory`: определяет, является ли объект (адрес URL) каталогом в файловой системе


-

`ignoreCase`: указывает, надо ли игнорировать регистр адреса URL. По умолчанию равно true, поэтому регистр не учитывается

-

`negate`: если равно true, то правило применяется, если условие НЕ учитывается. По умолчанию равно false


### Определение действий


Если выражение и условия, определяемые правилом, соответствуют объекту (например, адресу URL), то выполняется определенное действие, заданное элементом
`<action>`. Действия могут быть нескольких типов. Тип задается с помощью атрибута `type`, который принимает следующие значения:


-

Rewrite: заменяет текущую строку запроса URL другой строкой

-

Redirect: выполняет редирект, посылая клиенту статусный код 3хх.

-

CustomResponse: отправляет клиенту определенный статусный код, а также может отправлять специфическое сообщение

-

AbortRequest: сбрасывает подключение для текущего клиента


Другие атрибуты элемента action:


-

`url`: строка, которая будет заменять текущую строку запроса URL

-

`appendQueryString`: определяет, должна ли сохраняться та часть строки запроса, которая идет после названия домена и порта. По умолчанию
имеет значение true, что значит, что строка запроса со всеми параметрами за исключением названия домена будет сохраняться.

-

`redirectType`: статусный код переадресации при использовании типа Redirect (301 – Permanent, 302 – Found,
303 – See other, 307 – Temporary)

-

`statusCode`: определяет статусный код в качестве ответа клиенту при использовании типа CustomResponse

-

`subStatusCode`: определяет вспомогательный статусный код при использовании типа CustomResponse

-

`statusReason`: определяет сообщение, отправляемое клиенту вместе со статусным кодом при использовании типа CustomResponse

-

`statusDescription`: определяет сообщение, отправляемое клиенту в теле ответа при использовании типа CustomResponse


### Использование переменных сервера


При изменении URL мы можем использовать следующие переменные сервера:


-

`QUERY_STRING`: параметры запроса

-

`HTTP_HOST`: домен

-

`SERVER_PORT`: номер порта

-

`SERVER_PORT_SECURE` и `HTTPS`: указывают, использует ли клиент защищенное подключение

-

`REQUEST_URI`: полная строка запроса


URL представляется в следующем виде: `http(s)://<host>:<port>/<path>?<querystring>`.
Допустим, пользователь обращается к URL _http://www.somesite.com/home/index?id=2&name=3_. Тогда IIS сегментирует ее следующим образом:


-

`path`: представляет сегмент `home/index`. Эта часть затем сравнивается правилом с выражением, определенным в элементе `<match>`

-

`QUERY_STRING`: в данном случае сегмент параметров `id=2&name=3`

-

`HTTP_HOST`: сегмент `www.somesite.com`

-

`SERVER_PORT`: если номер порта не указан, то по умолчанию равен 80.

-

`SERVER_PORT_SECURE` равен 0, а `HTTPS` содержит `OFF`

-

`REQUEST_URI`: сегмент `home/index?id=2&name=3`


При создании условий для правил мы можем ссылаться на эти переменные через выражение вида "{НАЗВАНИЕ_ПЕРЕМЕННОЙ}". Например, нам нужно условие,
согласно которому в строке параметров должен быть числовой параметр id:

```
<add input="{QUERY_STRING}" pattern="id=([0-9]+)" />
```


Кроме того, нам доступны заголовки HTTP-запроса, например, строку юзер-агента мы можем получить с помощью выражения "{HTTP_USER_AGENT}".


При использовании заголовков запроса надо учитывать, что все дефисы в названии заголовков (например, User-Agent) заменяются символами подчеркивания.
Все строчные буквы заменяются заглавными, а к названию переменных добавляется префикс "HTTP_". Как например, из заголовка User-Agent создается переменная
HTTP_USER_AGENT.


### Обратные ссылки


Обратные ссылки представляют отдельные сегменты выражений, которые используются в условиях. Например:

```

<rewrite>
 <rules>
 <rule name="Redirect">
 <match url = "(.*)"/>
 <conditions>
 <add input="{REQUEST_URI}" pattern="([a-z]+)/([a-z]+)/([0-9]+)" matchType="Pattern" />
 </conditions>
 <action type="Redirect" url ="{C:1}/{C:3}" />
 </rule>
 </rules>
</rewrite>

```


Все обратные ссылки представляют выражения типа {C:N}, где N - число от 0 до 9. При этом значение `{C:0}`
представляет всю попадающую под условие строку.


То есть из строки запроса "home/index/2" генерировались бы три обратных ссылки `C:1 = "home"`, `C:2 = "index"` и `C:3 = "2"`.
И в соответствии с элементом `action` шла бы переадресация на адрес "home/2" (то есть "{C:1}/{C:3}").


Кроме условий для создания обратных ссылок могут применяться выражения в элементе `match`. Все обратные ссылки из выражения match
доступны через выражения типа {R:N}, где N - число от 0 до 9. При этом значение `{R:0}`
представляет всю попадающую под условие строку.


Так, рассмотрим другой пример. Допустим, у нас есть правило:

```

<rule name="Rewrite query" stopProcessing="true">
 <match url="^home/products/([0-9]+)/([_0-9a-z-]+)" />
 <action type="Rewrite" url="home/products?id={R:1}&amp;name={R:2}" />
</rule>

```


Например, при запросе _http://localhost:50645/Home/Products/2/phones_ мы получим следующие сегменты:


{R:0} = "Home/Products/2/phones"


{R:1} = "2"


{R:2} = "phones"


В итоге будет формироваться следующая строка URL: http://localhost:50645/Home/Products?id=2&name=phones


Для тестирования определим следующее приложение:

```

using Microsoft.AspNetCore.Rewrite; // Пакет с middleware URL Rewriting

var builder = WebApplication.CreateBuilder();

var app = builder.Build();

IHostEnvironment? env = app.Services.GetService<IHostEnvironment>();
if(env is not null)
{
 var options = new RewriteOptions()
 .AddIISUrlRewrite(env.ContentRootFileProvider, "urlrewrite.xml");
 app.UseRewriter(options);
}

app.MapGet("/", async context => await context.Response.WriteAsync("Hello World!"));
app.MapGet("/home/products", async context =>
 await context.Response.WriteAsync($"Values: id = {context.Request.Query["id"]} name = {context.Request.Query["name"]}"));

app.Run();

```

![IIS URL Rewriting в ASP.NET Core и C#](https://metanit.com./pics/15.4.png)


Еще один пример - переадресация с домена без www на субдомен www:

```

<rule name="Redirect to WWW" enabled="true" stopProcessing="true">
 <match url=".*" />
 <conditions logicalGrouping="MatchAll">
 <add input="{HTTP_HOST}" pattern=".*" />
 </conditions>
 <action type="Redirect" url="http://www.localhost:50645/{R:0}" />
</rule>

```


Или обратное действие - перенаправление с www на домен без www (для домена localhost):

```

<rule name="Redirect to NonWWW" stopProcessing="true">
 <match url=".*" />
 <conditions logicalGrouping="MatchAll">
 <add input="{HTTP_HOST}" pattern="^localhost" negate="true" />
 </conditions>
 <action type="Redirect" url="http://localhost:50645/{R:0}" />
</rule>

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

**Источник:** [https://metanit.com/sharp/aspnet6/15.2.php](https://metanit.com/sharp/aspnet6/15.2.php)
