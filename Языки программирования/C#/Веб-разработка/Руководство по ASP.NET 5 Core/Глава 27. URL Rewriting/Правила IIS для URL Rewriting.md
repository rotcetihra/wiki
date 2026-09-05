# Правила IIS для URL Rewriting

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET 5 Core|Руководство по ASP.NET 5 Core]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET 5 Core/Глава 27. URL Rewriting|Глава 27. URL Rewriting]] / Правила IIS для URL Rewriting

[[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET 5 Core/Глава 27. URL Rewriting/Введение в URL Rewriting|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET 5 Core/Глава 27. URL Rewriting|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET 5 Core/Глава 27. URL Rewriting/Применение правил для Apache|Вперёд]]

**Дата написания:** 05.09.2026

## Правила IIS для URL Rewriting


Данное руководство устарело. Актуальное руководство: [Руководство по ASP.NET Core 7](https://metanit.com/sharp/aspnet6/)Последнее обновление: 22.12.2019




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

using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Rewrite;
using Microsoft.Extensions.Hosting;

namespace UrlRewritingApp
{
 public class Startup
 {
 public void Configure(IApplicationBuilder app, IHostEnvironment env)
 {
 app.UseDeveloperExceptionPage();

 var options = new RewriteOptions()
 .AddIISUrlRewrite(env.ContentRootFileProvider, "urlrewrite.xml");
 app.UseRewriter(options);

 app.UseRouting();

 app.UseEndpoints(endpoints =>
 {
 endpoints.MapGet("/", async context =>
 {
 await context.Response.WriteAsync("Hello World!");
 });
 endpoints.MapGet("/home", async context =>
 {
 await context.Response.WriteAsync("Home Page!");
 });
 endpoints.MapGet("/home/index", async context =>
 {
 await context.Response.WriteAsync("Home Index Page!");
 });
 });
 }
 }
}

```


Начиная с версии ASP.NET Core 2.0, можно также загружать файл конфигурации следующим образом:

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


Для тестирования мы можем определить следующий метод Configure в классе Startup:

```

public void Configure(IApplicationBuilder app, IHostEnvironment env)
{
 app.UseDeveloperExceptionPage();

 var options = new RewriteOptions()
 .AddIISUrlRewrite(env.ContentRootFileProvider, "urlrewrite.xml");
 app.UseRewriter(options);

 app.UseRouting();

 app.UseEndpoints(endpoints =>
 {
 endpoints.MapGet("/", async context =>
 {
 await context.Response.WriteAsync("Hello World!");
 });
 endpoints.MapGet("/home/products", async context =>
 {
 await context.Response.WriteAsync($"Values: id = {context.Request.Query["id"]} " +
 $"name = {context.Request.Query["name"]}");
 });
 });
}

```

![IIS URL Rewriting в ASP.NET Core MVC](https://metanit.com./pics/urlrewriting2.png)


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


 - [ASP.NET Core - новая эпоха в развитии ASP.NET](//metanit.com/sharp/aspnet5/1.1.php)

 - [Начало работы с ASP.NET Core](//metanit.com/sharp/aspnet5/1.2.php)

 - [Проект ASP.NET Core в Visual Studio for Mac](//metanit.com/sharp/aspnet5/1.3.php)



- Глава 2. Основы ASP.NET Core


 - [Запуск приложения. Класс Program](//metanit.com/sharp/aspnet5/2.13.php)

 - [Класс Startup](//metanit.com/sharp/aspnet5/2.1.php)

 - [Конвейер обработки запроса и middleware](//metanit.com/sharp/aspnet5/2.2.php)

 - [Методы Use, Run и делегат RequestDelegate](//metanit.com/sharp/aspnet5/2.3.php)

 - [Методы Map и MapWhen](//metanit.com/sharp/aspnet5/2.22.php)

 - [Создание компонентов middleware](//metanit.com/sharp/aspnet5/2.4.php)

 - [Конвейер обработки запроса](//metanit.com/sharp/aspnet5/2.18.php)

 - [IWebHostEnvironment и окружение](//metanit.com/sharp/aspnet5/2.21.php)

 - [Статические файлы](//metanit.com/sharp/aspnet5/2.5.php)

 - [Работа со статическими файлами](//metanit.com/sharp/aspnet5/2.14.php)

 - [Обработка ошибок](//metanit.com/sharp/aspnet5/17.1.php)

 - [Работа с HTTPS](//metanit.com/sharp/aspnet5/18.6.php)



- Глава 3. Сервисы и Dependency Injection


 - [Сервисы и метод ConfigureServices](//metanit.com/sharp/aspnet5/6.1.php)

 - [Создание своих сервисов](//metanit.com/sharp/aspnet5/2.19.php)

 - [Передача зависимостей](//metanit.com/sharp/aspnet5/6.4.php)

 - [Жизненный цикл зависимостей](//metanit.com/sharp/aspnet5/6.2.php)

 - [Применение сервисов в middleware](//metanit.com/sharp/aspnet5/2.20.php)

 - [Singleton-объекты и scoped-сервисы](//metanit.com/sharp/aspnet5/6.5.php)



- Глава 4. Конфигурация


 - [Основы конфигурации](//metanit.com/sharp/aspnet5/2.6.php)

 - [Нефайловые провайдеры конфигурации](//metanit.com/sharp/aspnet5/2.16.php)

 - [Файловые провайдеры конфигурации](//metanit.com/sharp/aspnet5/2.12.php)

 - [Объединение конфигураций и установка сервиса IConfiguration](//metanit.com/sharp/aspnet5/2.23.php)

 - [Работа с конфигурацией](//metanit.com/sharp/aspnet5/2.17.php)

 - [Создание провайдера конфгурации](//metanit.com/sharp/aspnet5/2.15.php)

 - [Проекция конфигурации на классы](//metanit.com/sharp/aspnet5/2.9.php)

 - [Передача конфигурации через IOptions](//metanit.com/sharp/aspnet5/6.3.php)



- Глава 5. Состояние приложения. Куки. Сессии


 - [HttpContext.Items](//metanit.com/sharp/aspnet5/2.11.php)

 - [Куки](//metanit.com/sharp/aspnet5/2.25.php)

 - [Сессии](//metanit.com/sharp/aspnet5/2.26.php)



- Глава 6. Логгирование


 - [Ведение лога и ILogger](//metanit.com/sharp/aspnet5/2.10.php)

 - [Фабрика логгера и провайдеры логгирования](//metanit.com/sharp/aspnet5/2.29.php)

 - [Конфигурация и фильтрация логгирования](//metanit.com/sharp/aspnet5/2.28.php)

 - [Создание провайдера логгирования](//metanit.com/sharp/aspnet5/2.27.php)



- Глава 7. Маршрутизация


 - [Основы маршрутизации в ASP.NET Core](//metanit.com/sharp/aspnet5/11.1.php)

 - [RouterMiddleware](//metanit.com/sharp/aspnet5/11.12.php)

 - [Определение маршрутов](//metanit.com/sharp/aspnet5/11.2.php)

 - [Работа с маршрутами](//metanit.com/sharp/aspnet5/11.4.php)

 - [Ограничения маршрутов](//metanit.com/sharp/aspnet5/11.3.php)

 - [Создание ограничений маршрутов](//metanit.com/sharp/aspnet5/11.7.php)

 - [Создание своего маршрута](//metanit.com/sharp/aspnet5/11.8.php)



- Глава 8. ASP.NET Core MVC


 - [Введение в ASP.NET Core MVC](//metanit.com/sharp/aspnet5/3.1.php)

 - [Добавление MVC в пустой проект](//metanit.com/sharp/aspnet5/3.6.php)

 - [Первое приложение. Добавление моделей и базы данных](//metanit.com/sharp/aspnet5/3.2.php)

 - [Создание контроллера и инициализатора базы данных](//metanit.com/sharp/aspnet5/3.3.php)

 - [Добавление методов контроллера и представлений](//metanit.com/sharp/aspnet5/3.4.php)

 - [Добавление мастер-страницы и стилизации](//metanit.com/sharp/aspnet5/3.5.php)



- Глава 9. Контроллеры


 - [Контроллеры и их действия](//metanit.com/sharp/aspnet5/5.1.php)

 - [Передача данных в контроллер](//metanit.com/sharp/aspnet5/5.2.php)

 - [Результаты действий](//metanit.com/sharp/aspnet5/5.3.php)

 - [ContentResult и JsonResult](//metanit.com/sharp/aspnet5/5.4.php)

 - [Переадресация](//metanit.com/sharp/aspnet5/5.5.php)

 - [Отправка статусных кодов](//metanit.com/sharp/aspnet5/5.6.php)

 - [Отправка файлов](//metanit.com/sharp/aspnet5/5.7.php)

 - [Переопределение контроллеров](//metanit.com/sharp/aspnet5/5.8.php)

 - [Контекст контроллера](//metanit.com/sharp/aspnet5/5.9.php)

 - [Передача зависимостей в контроллер](//metanit.com/sharp/aspnet5/5.10.php)



- Глава 10. Представления


 - [Введение в представления](//metanit.com/sharp/aspnet5/7.1.php)

 - [Движок представлений Razor](//metanit.com/sharp/aspnet5/7.2.php)

 - [Передача данных в представление](//metanit.com/sharp/aspnet5/7.3.php)

 - [Мастер-страницы](//metanit.com/sharp/aspnet5/7.4.php)

 - [Файл _ViewImports.cshtml](//metanit.com/sharp/aspnet5/7.9.php)

 - [Частичные представления](//metanit.com/sharp/aspnet5/7.5.php)

 - [Внедрение зависимостей в представления](//metanit.com/sharp/aspnet5/7.7.php)

 - [Работа с формами](//metanit.com/sharp/aspnet5/7.8.php)

 - [Создание движка представлений](//metanit.com/sharp/aspnet5/7.10.php)



- Глава 11. Маршрутизация в ASP.NET Core MVC


 - [Маршрутизация в MVC с помощью конечных точек](//metanit.com/sharp/aspnet5/11.5.php)

 - [Маршрутизация с помощью RouterMiddleware. Метод UseMvc](//metanit.com/sharp/aspnet5/11.13.php)

 - [Атрибуты маршрутизации](//metanit.com/sharp/aspnet5/11.6.php)

 - [Области](//metanit.com/sharp/aspnet5/11.9.php)



- Глава 12. Модели


 - [Модели в ASP.NET Core MVC](//metanit.com/sharp/aspnet5/8.1.php)

 - [Модели представления View Model](//metanit.com/sharp/aspnet5/8.2.php)

 - [Привязка модели](//metanit.com/sharp/aspnet5/8.3.php)

 - [Передача данных в контроллер](//metanit.com/sharp/aspnet5/8.4.php)

 - [Управление привязкой](//metanit.com/sharp/aspnet5/8.5.php)

 - [Создание привязчика модели](//metanit.com/sharp/aspnet5/8.6.php)



- Глава 13. HTML-хелперы


 - [Создание HTML-хелперов](//metanit.com/sharp/aspnet5/9.1.php)

 - [HTML-хелперы элементов форм](//metanit.com/sharp/aspnet5/9.2.php)

 - [Строго типизированные хелперы](//metanit.com/sharp/aspnet5/9.3.php)

 - [Шаблонные хелперы](//metanit.com/sharp/aspnet5/9.4.php)

 - [Генерация ссылок](//metanit.com/sharp/aspnet5/9.5.php)

 - [URL-хелперы](//metanit.com/sharp/aspnet5/11.11.php)



- Глава 14. Tag-хелперы


 - [Введение в tag-хелперы](//metanit.com/sharp/aspnet5/10.1.php)

 - [AnchorTagHelper](//metanit.com/sharp/aspnet5/10.2.php)

 - [LinkTagHelper и ScriptTagHelper](//metanit.com/sharp/aspnet5/10.3.php)

 - [Tag-хелперы форм](//metanit.com/sharp/aspnet5/10.4.php)

 - [EnvironmentTagHelper](//metanit.com/sharp/aspnet5/10.6.php)

 - [CacheTagHelper](//metanit.com/sharp/aspnet5/10.7.php)

 - [Создание tag-хелперов](//metanit.com/sharp/aspnet5/10.8.php)

 - [Управление выводом tag-хелпера](//metanit.com/sharp/aspnet5/10.10.php)

 - [Контекст хелпера и получение зависимостей](//metanit.com/sharp/aspnet5/10.11.php)

 - [Атрибут HtmlTargetElement](//metanit.com/sharp/aspnet5/10.12.php)

 - [Tag-хелперы и сложные объекты и коллекции](//metanit.com/sharp/aspnet5/10.9.php)



- Глава 15. View Component


 - [Определение компонента представлений](//metanit.com/sharp/aspnet5/7.6.php)

 - [Передача данных в View Component](//metanit.com/sharp/aspnet5/7.11.php)

 - [Генерация контента в View Component](//metanit.com/sharp/aspnet5/7.12.php)

 - [ViewViewComponentResult и представления](//metanit.com/sharp/aspnet5/7.13.php)

 - [Асинхронные операции в View Component](//metanit.com/sharp/aspnet5/7.14.php)

 - [ViewComponentContext](//metanit.com/sharp/aspnet5/7.15.php)



- Глава 16. Метаданные и валидация модели


 - [Основы валидации](//metanit.com/sharp/aspnet5/19.1.php)

 - [Атрибуты валидации](//metanit.com/sharp/aspnet5/19.2.php)

 - [Валидация на стороне сервера](//metanit.com/sharp/aspnet5/19.3.php)

 - [Валидация на стороне клиента](//metanit.com/sharp/aspnet5/19.4.php)

 - [Tag-хелперы валидации](//metanit.com/sharp/aspnet5/10.5.php)

 - [Создание атрибута валидации. Самовалидация модели](//metanit.com/sharp/aspnet5/19.5.php)

 - [Аннотации данных](//metanit.com/sharp/aspnet5/19.6.php)



- Глава 17. Работа с данными в Entity Framework в MVC


 - [Подключение и создание базы данных в Entity Framework Core](//metanit.com/sharp/aspnet5/12.1.php)

 - [Операции с моделями. Создание и вывод](//metanit.com/sharp/aspnet5/12.2.php)

 - [Операции с моделями. Редактирование и удаление](//metanit.com/sharp/aspnet5/12.3.php)

 - [Сортировка](//metanit.com/sharp/aspnet5/12.4.php)

 - [Создание tag-хелпера сортировки](//metanit.com/sharp/aspnet5/12.5.php)

 - [Фильтрация](//metanit.com/sharp/aspnet5/12.6.php)

 - [Постраничная навигация](//metanit.com/sharp/aspnet5/12.7.php)

 - [Tag-хелпер для постраничной навигации](//metanit.com/sharp/aspnet5/12.8.php)

 - [Объединение сортировки, фильтрации и пагинации](//metanit.com/sharp/aspnet5/12.9.php)

 - [Tag-хелпер пагинации с сортировкой и фильтрацией](//metanit.com/sharp/aspnet5/12.10.php)



- Глава 18. Razor Pages


 - [Введение в Razor Pages](//metanit.com/sharp/aspnet5/29.1.php)

 - [Добавление RazorPages в пустой проект](//metanit.com/sharp/aspnet5/29.2.php)

 - [Обработка запросов. Передача форм](//metanit.com/sharp/aspnet5/29.3.php)

 - [Привязка свойств RazorPage к параметрам запроса](//metanit.com/sharp/aspnet5/29.4.php)

 - [Параметры маршрутов в Razor Pages](//metanit.com/sharp/aspnet5/29.5.php)

 - [Обработчики страницы](//metanit.com/sharp/aspnet5/29.6.php)

 - [Возвращение результата](//metanit.com/sharp/aspnet5/29.7.php)

 - [Переадресация и создание ссылок](//metanit.com/sharp/aspnet5/29.8.php)

 - [Подключение к базе данных](//metanit.com/sharp/aspnet5/29.9.php)

 - [Создание и вывод объектов из базы данных](//metanit.com/sharp/aspnet5/29.10.php)

 - [Изменение и удаление в базе данных](//metanit.com/sharp/aspnet5/29.11.php)



- Глава 19. Web API


 - [Введение в Web API](//metanit.com/sharp/aspnet5/23.1.php)

 - [Создание контроллера](//metanit.com/sharp/aspnet5/23.2.php)

 - [Тестирование контроллера](//metanit.com/sharp/aspnet5/23.3.php)

 - [Создание клиента для WEB API](//metanit.com/sharp/aspnet5/23.4.php)

 - [Валидация в Web API](//metanit.com/sharp/aspnet5/23.5.php)

 - [Content negotiation](//metanit.com/sharp/aspnet5/23.6.php)



- Глава 20. Фильтры


 - [Введение в фильтры](//metanit.com/sharp/aspnet5/18.1.php)

 - [Передача параметров в фильтры и установка зависимостей](//metanit.com/sharp/aspnet5/18.5.php)

 - [Фильтры ресурсов](//metanit.com/sharp/aspnet5/18.2.php)

 - [Фильтры действий](//metanit.com/sharp/aspnet5/18.3.php)

 - [Фильтры результатов](//metanit.com/sharp/aspnet5/18.4.php)

 - [Фильтры исключений](//metanit.com/sharp/aspnet5/17.2.php)

 - [Фильтры RazorPages](//metanit.com/sharp/aspnet5/18.7.php)



- Глава 21. Аутентификация и авторизация


 - [Аутентификация на основе куки. Часть 1](//metanit.com/sharp/aspnet5/15.1.php)

 - [Аутентификация на основе куки. Часть 2](//metanit.com/sharp/aspnet5/15.2.php)

 - [Авторизация](//metanit.com/sharp/aspnet5/15.3.php)

 - [ClaimPrincipal и объекты Claim](//metanit.com/sharp/aspnet5/15.4.php)

 - [Авторизация по ролям](//metanit.com/sharp/aspnet5/15.5.php)

 - [Авторизация на основе Claims](//metanit.com/sharp/aspnet5/15.6.php)

 - [Пример авторизации на основе Claims](//metanit.com/sharp/aspnet5/15.7.php)

 - [Создание ограничений для политики авторизации](//metanit.com/sharp/aspnet5/15.8.php)

 - [JWT-токены](//metanit.com/sharp/aspnet5/23.7.php)



- Глава 22. ASP.NET Core Identity


 - [Введение в ASP.NET Core Identity](//metanit.com/sharp/aspnet5/16.1.php)

 - [Основные классы в ASP.NET Core Identity](//metanit.com/sharp/aspnet5/16.11.php)

 - [Добавление Identity в проект с нуля](//metanit.com/sharp/aspnet5/16.2.php)

 - [Регистрация и создание пользователей в Identity](//metanit.com/sharp/aspnet5/16.3.php)

 - [Авторизация пользователей в Identity](//metanit.com/sharp/aspnet5/16.4.php)

 - [Управление пользователями](//metanit.com/sharp/aspnet5/16.7.php)

 - [Изменение пароля](//metanit.com/sharp/aspnet5/16.8.php)

 - [Валидация пароля](//metanit.com/sharp/aspnet5/16.9.php)

 - [Валидация пользователя](//metanit.com/sharp/aspnet5/16.10.php)

 - [Управление ролями](//metanit.com/sharp/aspnet5/16.13.php)

 - [Инициализация БД ролями и пользователями](//metanit.com/sharp/aspnet5/16.12.php)



- Глава 23. Клиентская разработка


 - [Бандлинг и минификация](//metanit.com/sharp/aspnet5/13.6.php)

 - [Менеджер Libman](//metanit.com/sharp/aspnet5/13.7.php)

 - [Пакетный менеджер NPM](//metanit.com/sharp/aspnet5/13.5.php)

 - [Gulp](//metanit.com/sharp/aspnet5/13.1.php)

 - [Grunt](//metanit.com/sharp/aspnet5/13.2.php)

 - [Препроцессоры Less и Sass](//metanit.com/sharp/aspnet5/13.4.php)



- Глава 24. Производительность и кэширование


 - [Кэширование с помощью MemoryCache](//metanit.com/sharp/aspnet5/14.1.php)

 - [Атрибут ResponseCache](//metanit.com/sharp/aspnet5/14.2.php)

 - [Сжатие ответа](//metanit.com/sharp/aspnet5/14.3.php)

 - [Кэширование статических файлов](//metanit.com/sharp/aspnet5/14.4.php)



- Глава 25. Сервер и публикация приложения


 - [Сервер](//metanit.com/sharp/aspnet5/2.7.php)

 - [Публикация на IIS](//metanit.com/sharp/aspnet5/20.1.php)

 - [Установка приложения в виде службы Windows](//metanit.com/sharp/aspnet5/20.2.php)



- Глава 26. Тестирование


 - [Введение в юнит-тесты](//metanit.com/sharp/aspnet5/22.1.php)

 - [Создание проекта юнит-тестов. Добавление xUnit](//metanit.com/sharp/aspnet5/22.2.php)

 - [Создание юнит-тестов](//metanit.com/sharp/aspnet5/22.3.php)

 - [Фреймворк Moq и moq-объекты](//metanit.com/sharp/aspnet5/22.4.php)

 - [Тестирование контроллера](//metanit.com/sharp/aspnet5/22.5.php)



- Глава 27. URL Rewriting


 - [Введение в URL Rewriting](//metanit.com/sharp/aspnet5/24.1.php)

 - [Правила IIS для URL Rewriting](//metanit.com/sharp/aspnet5/24.2.php)

 - [Применение правил для Apache](//metanit.com/sharp/aspnet5/24.3.php)

 - [Создание правил URL Rewriting](//metanit.com/sharp/aspnet5/24.4.php)



- Глава 28. Глобализация и локализация


 - [Определение культуры](//metanit.com/sharp/aspnet5/28.1.php)

 - [RequestLocalizationMiddleware](//metanit.com/sharp/aspnet5/28.2.php)

 - [Локализация строк. IStringLocalizer](//metanit.com/sharp/aspnet5/28.3.php)

 - [Ресурсы и локализация в контроллерах](//metanit.com/sharp/aspnet5/28.4.php)

 - [Локализация представлений](//metanit.com/sharp/aspnet5/28.5.php)

 - [Локализация аннотаций данных](//metanit.com/sharp/aspnet5/28.6.php)

 - [Переключение языка приложения](//metanit.com/sharp/aspnet5/28.7.php)

 - [Общие ресурсы локализации](//metanit.com/sharp/aspnet5/28.8.php)

 - [Хранение ресурсов в базе данных](//metanit.com/sharp/aspnet5/28.9.php)



- Глава 29. SignalR Core


 - [SignalR Core. Первое приложение](//metanit.com/sharp/aspnet5/30.1.php)

 - [Создание и конфигурация хабов](//metanit.com/sharp/aspnet5/30.2.php)

 - [Клиент javascript](//metanit.com/sharp/aspnet5/30.3.php)

 - [Контекст хаба, подключение и отключение клиентов](//metanit.com/sharp/aspnet5/30.4.php)

 - [Взаимодействие с клиентами](//metanit.com/sharp/aspnet5/30.5.php)

 - [IHubContext](//metanit.com/sharp/aspnet5/30.6.php)

 - [Отправка сложных объектов](//metanit.com/sharp/aspnet5/30.7.php)

 - [Аутентификация и авторизация на основе куки](//metanit.com/sharp/aspnet5/30.8.php)

 - [Аутентификация и авторизация с помощью токенов](//metanit.com/sharp/aspnet5/30.9.php)

 - [Пользователи](//metanit.com/sharp/aspnet5/30.10.php)

 - [Группы](//metanit.com/sharp/aspnet5/30.11.php)

 - [Клиент на Xamarin Forms](//metanit.com/sharp/aspnet5/30.12.php)



- Глава 30. CORS и кросс-доменные запросы


 - [Начало работы с CORS](//metanit.com/sharp/aspnet5/31.1.php)

 - [Конфигурация CORS](//metanit.com/sharp/aspnet5/31.2.php)

 - [Политики CORS](//metanit.com/sharp/aspnet5/31.3.php)

 - [Глобальная и локальная настройка CORS](//metanit.com/sharp/aspnet5/31.5.php)

 - [CORS в MVC](//metanit.com/sharp/aspnet5/31.4.php)



- Глава 31. Dapper


 - [Работа с Dapper в ASP.NET Core](//metanit.com/sharp/aspnet5/26.1.php)



- Глава 32. React.JS


 - [Подключение React в ASP.NET Core](//metanit.com/sharp/aspnet5/25.1.php)

 - [Взаимодействие React.JS и ASP.NET Core](//metanit.com/sharp/aspnet5/25.2.php)



- Глава 33. Дополнительные статьи


 - [Отправка email в ASP.NET Core](//metanit.com/sharp/aspnet5/21.1.php)

 - [Загрузка файлов на сервер](//metanit.com/sharp/aspnet5/21.3.php)










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

**Источник:** [https://metanit.com/sharp/aspnet5/24.2.php](https://metanit.com/sharp/aspnet5/24.2.php)
