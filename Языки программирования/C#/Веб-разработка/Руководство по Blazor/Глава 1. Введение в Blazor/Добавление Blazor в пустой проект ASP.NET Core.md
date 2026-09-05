# Добавление Blazor в пустой проект ASP.NET Core

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по Blazor|Руководство по Blazor]] / [[Языки программирования/C#/Веб-разработка/Руководство по Blazor/Глава 1. Введение в Blazor|Глава 1. Введение в Blazor]] / Добавление Blazor в пустой проект ASP.NET Core

[[Языки программирования/C#/Веб-разработка/Руководство по Blazor/Глава 1. Введение в Blazor/Рендеринг WebAssembly и авторендеринг|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по Blazor/Глава 1. Введение в Blazor|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по Blazor/Глава 1. Введение в Blazor/Blazor WebAssembly. Первое приложение|Вперёд]]

**Дата написания:** 05.09.2026

## Добавление Blazor в проект ASP.NET Core

Последнее обновление: 27.11.2023




-

-

-














.NET CLI и Visual Studo уже по умолчанию предоставляет шаблоны проектов для использования Blazor. Подобные шаблоны проектов имеют некоторое типовое содержимое,
что позволяет нам тут же запустить и протестировать проект. Тем не менее мы можем взять и обычный
проект ASP.NET Core и с нуля добавить в него все необходимые файлы. Потому что
и стандартный проект ASP.NET Core, и проект Blazor используют один и тот же SDK - `Microsoft.NET.Sdk.Web`. Рассмотрим, как добавить функциональность Blazor в проект
ASP.NET Core и вообще как можно сочетать стандартную функциональность ASP.NET Core и компоненты Blazor.


Для этого в качестве типа проекта выберем ASP.NET Core Empty:
![Добавление Blazor Server в пустой проект ASP.NET Core](https://metanit.com./pics/1.12.png)


Основным стоительным блоком приложения Razor являются компоненты. Определим один компонент. Для этого в корень проекта добавим новый
элемент Razor Component, который назовем App.razor:
![Добавление компонента Razor Component в проект Blazor Server](https://metanit.com./pics/1.13.png)


То есть в итоге проект будет выглядеть следующим образом:
![Сочетание Minimal API ASP.NET Core и Blazor в одном проекте](https://metanit.com./pics/1.32.png)


Определим в файле App.razor самый простейший код:

```

@page "/app"

<h1>Hello METANIT.COM</h1>
<h2>Первое приложение на Blazor</h2>

```


Первая строка - директива `@page` указывает, что данный компонент будет обрабатывать запросы по пути "/app". И далее идут заголовки, которые собственно составляют содержимое компонента.


В идеале мы могли бы определить здесь полноценную веб-страницу с более сложной структурой, добавить более сложную логику, маршрутизацию и кучу компонентов,
но пока остановимся на этом и будем идти от простого.


Но пока по умолчанию данный компонент никак не участвует в обработке запроса. Нам надо его встроить в конвейер обработки запроса. И для этого изменим файл Program.cs
следующим образом:

```

using SimpleBlazorApp;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddRazorComponents(); // добавляем сервисы компонентов Razor

var app = builder.Build();

app.UseAntiforgery();

// устанавливает корневой компонент и встраиваем его в конвейер обработки запроса
app.MapRazorComponents<App>();

app.MapGet("/", () => "Hello World!");

app.Run();

```


Прежде всего нам надо добавить необходимые сервисы для работы с компонентами Razor:

```
builder.Services.AddRazorComponents();
```


После создания объекта приложения app у него вызывается метод MapRazorComponents().

```
app.MapRazorComponents<App>();
```


Данный метод устанавливает корневой компонент - в данном случае компонент App и встраивает его (все его вложенные компоненты) в конвейер обработки запроса. Таким образом, компонент
App сможет сопоставляться с запросами.


Для работы компонентов Blazor также необходимо установить middleware для защиты от поддельных ресурсов:

```
app.UseAntiforgery();
```


При этом в проекте могут быть и стандартные middleware ASP.NET Core, обработчки других запросов.


Запустим приложение, обратимся в браузере по пути "/app" и увидим код нашего компонента:
![Приложение Blazor Server с нуля в проекте на ASP.NET Core и C#](https://metanit.com./pics/1.16.2.png)


### Добавление интерактивности


В примере выше был продемонстрирован статический рендеринг компонента. Но простой компонент, который выводит статический текст, не очень интересен. Добавим интерактивность.
Однако ограничение Blazor таково, что корневой компонент не может быть интерактивным. Поэтому добавим в проект еще один компонент, который назовем Counter,
а также добавим дополнительный файл _Imports.razor:
![Интерактивность в приложении Blazor в проекте на ASP.NET Core и C#](https://metanit.com./pics/1.33.png)


В файле _Imports.razor подключим ряд пространст имен, которые будут использоваться в обоих компонентах:

```

@using Microsoft.AspNetCore.Components.Routing
@using Microsoft.AspNetCore.Components.Web
@using static Microsoft.AspNetCore.Components.Web.RenderMode

```


Далее изменим компонент App следующий код:

```

<!DOCTYPE html>
<html>
 <head>
 <title>METANIT.COM</title>
 </head>
 <body>

 <h1>Hello METANIT.COM</h1>
 <Router AppAssembly="@typeof(Program).Assembly">
 <Found Context="routeData">
 <RouteView RouteData="@routeData" />
 </Found>
 </Router>

 <script src="_framework/blazor.web.js"></script>
 </body>
</html>

```


Теперь компонент App представляет полноценную веб-страницу, в которую встроен компонент Router. Его атрибут AppAssembly указывает на сборку, в которой следует искать
запрошенные вложенные компоненты (в нашем случае компонент Counter). Если c запрошенным путем сопоставлен определенный компонент,
то он рендерится вложенный компонент Found. Компонент Found содержит другой компонент - RouteView. Через атрибут RouteData он получает контекст маршрутизации,
который будут использоваться при обработке запроса.


В файле Counter.razor определим следующий код:

```

@page "/app"
@rendermode InteractiveServer


<p>Count: @currentCount</p>
<button @onclick="IncrementCount">+</button>
<button @onclick="DecrementCount">-</button>

@code {
 private int currentCount = 0;

 private void IncrementCount()
 {
 currentCount++;
 }

 private void DecrementCount()
 {
 if(currentCount > 0) currentCount--;
 }
}

```


Первая строка - директива `@page "/app"` позволяет настроить данный компонент на обоработку запросов по пути "/app". Вторая строка:

```
@rendermode InteractiveServer
```


устанавливает для компонента режим рендеринга на стороне сервера.


Суть компонента - по нажатию на одну из кнопок происходит увеличение или уменьшение счетчика currentCount, который выводится на страницу. И поскольку для компонента установлен рендеринг
на стороне сервера, то эти действия будут выполняться на сервере.


И внизу компонента подключается скрипт _framework/blazor.web.js. Это автогенерируемый скрипт, нам не надо его специально подключать. Его роль
заключается в установке подключения SignalR с сервером, что и обеспечивает интерактивность.


Последний шаг в установке интерактивности состоит в изменении файла Program.cs:

```

using SimpleBlazorApp;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddRazorComponents()
 .AddInteractiveServerComponents(); // добавляем сервисы для серверного рендеринга

var app = builder.Build();

app.UseAntiforgery();

app.MapRazorComponents<App>()
 .AddInteractiveServerRenderMode(); // добавляем интерактивный рендеринг сервера

app.MapGet("/", () => "Hello World!");

app.Run();

```


Здесь вначале добавляем сервисы для обеспечения интерактивного рендеринга на стороне сервера:

```
AddInteractiveServerComponents()
```


Далее с помощью метода

```
AddInteractiveServerRenderMode()
```


устанавливаем собственно режим интерактивного рендеринга уровня сервера.


Запустим проект и снова обратимся по пути "/app":
![Проект веб-приложения Blazor Server на C# с нуля](https://metanit.com./pics/1.16.3.png)










- Глава 1. Введение в Blazor


 - [Что такое Blazor](//metanit.com/sharp/blazor/1.1.php)

 - [Первое приложение на Blazor](//metanit.com/sharp/blazor/1.2.php)

 - [Рендеринг на сервере](//metanit.com/sharp/blazor/1.7.php)

 - [Рендеринг WebAssembly и авторендеринг](//metanit.com/sharp/blazor/1.8.php)

 - [Добавление Blazor в пустой проект ASP.NET Core](//metanit.com/sharp/blazor/1.4.php)

 - [Blazor WebAssembly. Первое приложение](//metanit.com/sharp/blazor/1.3.php)



- Глава 2. Компоненты


 - [Установка главного компонента](//metanit.com/sharp/blazor/2.2.php)

 - [Определение компонентов](//metanit.com/sharp/blazor/2.1.php)

 - [Вложенные компоненты. Параметры компонентов](//metanit.com/sharp/blazor/2.3.php)

 - [Передача произвольного набора атрибутов](//metanit.com/sharp/blazor/2.4.php)

 - [Обработка событий](//metanit.com/sharp/blazor/2.5.php)

 - [Обработка событий дочернего компонента в родительском](//metanit.com/sharp/blazor/2.6.php)

 - [Привязка данных](//metanit.com/sharp/blazor/2.7.php)

 - [Двусторонняя привязка и привязка параметров компонентов](//metanit.com/sharp/blazor/2.8.php)

 - [Каскадная передача значений](//metanit.com/sharp/blazor/2.9.php)

 - [Жизненный цикл компонентов](//metanit.com/sharp/blazor/2.10.php)

 - [Внедрение зависимостей в компоненты Blazor](//metanit.com/sharp/blazor/2.11.php)

 - [Привязка моделей](//metanit.com/sharp/blazor/2.12.php)

 - [Управление элементом head и компонент HeadOutlet](//metanit.com/sharp/blazor/2.13.php)

 - [Файл _Imports.razor и общие директивы компонентов](//metanit.com/sharp/blazor/2.14.php)



- Глава 3. Маршрутизация


 - [Маршрутизация между компонентами](//metanit.com/sharp/blazor/3.1.php)

 - [Компоновка](//metanit.com/sharp/blazor/3.2.php)

 - [Компонент NavLink](//metanit.com/sharp/blazor/3.3.php)

 - [Параметры маршрутов](//metanit.com/sharp/blazor/3.4.php)

 - [Параметры строки запроса](//metanit.com/sharp/blazor/3.5.php)

 - [Управление навигацией и NavigationManager](//metanit.com/sharp/blazor/3.6.php)



- Глава 4. Работа с формами и валидация


 - [Встроенные компоненты ввода](//metanit.com/sharp/blazor/4.1.php)

 - [Компонент EditForm](//metanit.com/sharp/blazor/4.2.php)

 - [Валидация на основе аннотаций данных](//metanit.com/sharp/blazor/4.3.php)

 - [Валидация и вывод сообщений об ошибках](//metanit.com/sharp/blazor/4.4.php)

 - [Программная валидация](//metanit.com/sharp/blazor/4.5.php)

 - [Кастомная валидации](//metanit.com/sharp/blazor/4.6.php)



- Глава 5. Отправка http-запросов


 - [HttpClient в проекте Blazor Server](//metanit.com/sharp/blazor/6.3.php)

 - [HttpClient в проекте Blazor WebAssembly](//metanit.com/sharp/blazor/6.1.php)

 - [Взаимодействие приложения Blazor с Web API](//metanit.com/sharp/blazor/6.2.php)



- Глава 6. Дополнительные статьи


 - [Конфигурация](//metanit.com/sharp/blazor/5.1.php)










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

**Источник:** [https://metanit.com/sharp/blazor/1.4.php](https://metanit.com/sharp/blazor/1.4.php)
