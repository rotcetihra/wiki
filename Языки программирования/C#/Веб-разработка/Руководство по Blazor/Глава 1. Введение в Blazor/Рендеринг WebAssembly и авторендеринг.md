# Рендеринг WebAssembly и авторендеринг

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по Blazor|Руководство по Blazor]] / [[Языки программирования/C#/Веб-разработка/Руководство по Blazor/Глава 1. Введение в Blazor|Глава 1. Введение в Blazor]] / Рендеринг WebAssembly и авторендеринг

[[Языки программирования/C#/Веб-разработка/Руководство по Blazor/Глава 1. Введение в Blazor/Blazor Server. Первое приложение|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по Blazor/Глава 1. Введение в Blazor|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по Blazor/Глава 1. Введение в Blazor/Добавление Blazor в пустой проект ASP.NET Core|Вперёд]]

**Дата написания:** 05.09.2026

## Рендеринг WebAssembly и авторендеринг

Последнее обновление: 29.11.2023




-

-

-














При рендеринге на стороне клиента Blazor применяет WebAssembly. В этом случае код целиком выполняется на стороне клиента, а приложение имеет доступ только к ресурсам в браузере.
Так, создадим новый проект Blazor по типу Blazor Web App.


При создании проекта для опции Interactive render mode укажем значение WebAssembly.
И также уберем отметку с поля Include sample pages, чтобы нам был создан минимальный проект:
![Клиентский рендеринг в приложении Blazor](https://metanit.com./pics/1.39.png)


Для создания аналогичного проекта с помощью .NET CLI применяется команда

```
dotnet new blazor -o ClientBlazorApp -e --interactivity WebAssembly
```


В итоге будут созданы следующие проекты:
![Статический рендеринг в приложении Blazor на ASP.NET Core](https://metanit.com./pics/1.40.png)


Стоит отметить, что в .NET 8 создаются два проекта. Непосредственно для компонентов WebAssembly определен проект с суффиксом "Client". По умолчанию он имеет файл
Program.cs, который настраивает хост WebAssembly, и файл _Imports.razor, который определяет для компонентов проекта
общие директивы Razor.


Если мы откроем файл Program.cs, то увидим, что он довольно простой:

```

using Microsoft.AspNetCore.Components.WebAssembly.Hosting;

var builder = WebAssemblyHostBuilder.CreateDefault(args);

await builder.Build().RunAsync();

```


Основная задача класса Program - настроить и запустить хост, который представлен классом WebAssemblyHost. Для этого у класса билдера хоста -
`WebAssemblyHostBuilder` вызывается метод Build(). А для запуска хоста вызывается метод RunAsync().


Добавим в этот проект новый компонент, который назовем Counter.razor и в котором определим следующий код:

```

@page "/counter"
@rendermode InteractiveWebAssembly

<h1>Counter</h1>

<button @onclick="IncrementCount">Click</button>
<p>Count: @count</p>

@code {
 int count = 0;

 void IncrementCount()
 {
 count++;
 }
}

```


Здесь стандартный компонент, который по нажатию на кнопку увеличивает значение переменной count в методе IncrementCount.
![WebAssembly и Blazor](https://metanit.com./pics/1.41.png)


Благодаря директиве `@page "/counter"` данный компонент применяется для обработки запросов по пути "/counter".


И чтобы применить к компоненту режим рендеринга на стороне клиента, в коде компонента прописана директива

```
@rendermode InteractiveWebAssembly
```


Хотя компононенты WebAssembly расположены в отдельном проекте, по умолчанию запускается другой - главный проект, который подтягивает эти компоненты. Обратися к его файлу
Program.cs:

```

using ClientBlazorApp.Components;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddRazorComponents()
 .AddInteractiveWebAssemblyComponents();

var app = builder.Build();

if (app.Environment.IsDevelopment())
{
 app.UseWebAssemblyDebugging();
}
else
{
 app.UseExceptionHandler("/Error", createScopeForErrors: true);
 app.UseHsts();
}

app.UseHttpsRedirection();

app.UseStaticFiles();
app.UseAntiforgery();

app.MapRazorComponents<App>()
 .AddInteractiveWebAssemblyRenderMode()
 .AddAdditionalAssemblies(typeof(ClientBlazorApp.Client._Imports).Assembly);

app.Run();

```


Здесь надо отметить несколько моментов. Прежде всего, необходимо добавить сервисы для поддержки интерактивного рендеринга на стороне WebAssembly с помощью метода AddInteractiveWebAssemblyComponents()

```

builder.Services.AddRazorComponents()
 .AddInteractiveWebAssemblyComponents();

```


Второй момент - надо установить режим интерактивного рендеринга на стороне WebAssembly с помощью метода AddInteractiveWebAssemblyRenderMode()

```

app.MapRazorComponents<App>()
 .AddInteractiveWebAssemblyRenderMode()
 .AddAdditionalAssemblies(typeof(ClientBlazorApp.Client._Imports).Assembly);

```


Но поскольку наш компонент Counter (как и предположительно другие возможные компоненты WebAssembly) располагаются в другой сборке, то эту сборку также надо добавить
для поиска компонентов. Для этого применяется метод `AddAdditionalAssemblies()`, в который передается объект `System.Reflection.Assembly`. А выражение

```
typeof(ClientBlazorApp.Client._Imports).Assembly
```


Получает сборку, где находится компонент _Imports (файл _Imports.razor)


Кроме того, как и в при серверном рендеринге, для WebAssembly необходим файл "_framework/blazor.web.js", который по умолчанию подключается в главном компоненте App:

```

<!DOCTYPE html>
<html lang="en">

<head>
 <meta charset="utf-8" />
 <meta name="viewport" content="width=device-width, initial-scale=1.0" />
 <base href="/" />
 <link rel="stylesheet" href="app.css" />
 <link rel="stylesheet" href="ClientBlazorApp.styles.css" />
 <HeadOutlet />
</head>

<body>
 <Routes />
 <script src="_framework/blazor.web.js"></script>
</body>

</html>

```


Когда браузер загрузил эту страницу, начинает выполняться подключаемый внизу страницы скрипт blazor.web.js. Он
загружает файл с именем blazor.boot.json, который содержит список всех файлов фреймворка и приложения, необходимых для запуска приложения.
В основном это сборки .NET. И все эти файлы, указанные в `blazor.boot.json`, также загружаются в коде javascript.


Также blazor.web.js загружает еще один специальный файл - dotnet.native.wasm. Этот файл представляет собой среду
выполнения .NET, скомпилированную в WebAssembly.


После загрузки всех файлов из blazor.boot.json код из файла
blazor.web.js инициализирует среду выполнения WebAssembly .NET, которая загружает инфраструктуру Blazor и само приложение.


Таким образом, в приложении основного проекта мы можем использовать компоненты из проекта WebAssembly. И мы сможем по пути "/counter" обращаться к компоненту Counter.
![Рендеринг компонентов Blazor в WebAssembly](https://metanit.com./pics/1.42.png)


Мы можем взаимодействовать с компонентом Counter, и все действия будут выполняться и обрабатываться в браузере без участия сервера.


Через инструменты разработчика мы можем увидеть, что среди прочих файлов загружается файл blazor.boot.json, о котором выше шла речь и который будет иметь содержание типа следующего:

```

{
 "mainAssemblyName": "ClientBlazorApp.Client",
 "resources": {
 "hash": "sha256-j5vxQrBsIrEdtEky1DjTuGD2aaDvm206c6CUosP5Rg4=",
 "jsModuleNative": {
 "dotnet.native.8.0.0.6861x3atex.js": "sha256-LjLDIz9+J7uuiwMlQ4HbNx2BnSpphOtO2MwkoI28vdI="
 },
 "jsModuleRuntime": {
 "dotnet.runtime.8.0.0.nv2fjwutuz.js": "sha256-WdSX3HQvnBYF0KJLZoOyHvTzMHetaob6PV0Kn2K+QXw="
 },
 "wasmNative": {
 "dotnet.native.wasm": "sha256-Vr6ZXKoP77zgabrMIxQ1GbOkrxfx5XGqHO0odLhUIMY="
 },
 "icu": {
 "icudt_CJK.dat": "sha256-SZLtQnRc0JkwqHab0VUVP7T3uBPSeYzxzDnpxPpUnHk=",
 "icudt_EFIGS.dat": "sha256-8fItetYY8kQ0ww6oxwTLiT3oXlBwHKumbeP2pRF4yTc=",
 "icudt_no_CJK.dat": "sha256-L7sV7NEYP37/Qr2FPCePo5cJqRgTXRwGHuwF5Q+0Nfs="
 },
 "assembly": {
 "Microsoft.AspNetCore.Authorization.wasm": "sha256-j29bzsbGr0GXbz3saSOBqDtWxNOK08Or3b1HgnZ+pvA=",
 "Microsoft.AspNetCore.Components.wasm": "sha256-0SRqG4hZOVUUFxERmD93PJWBJR6d4gCf5UB9vF6jB9A=",
 "Microsoft.AspNetCore.Components.Forms.wasm": "sha256-v5x7jiwdpMdHj54wA/JoDsrCrnr89XklOokSoWNJzF0=",
 "Microsoft.AspNetCore.Components.Web.wasm": "sha256-H1qHk5Kqn+R+8t/eTsZzQ5/5ZvgjmC8+ZPyuEp5nals=",
 "Microsoft.AspNetCore.Components.WebAssembly.wasm": "sha256-GDJfIU7XS7MlmrwWZh/CD4wNkm+PPO7FFLZ4Qo0jCPU=",
 .........................................................................................
 "System.wasm": "sha256-cMSi3CkR4f0ANPSwi7X/T6NvBS6QMlbFtcvKQrCeG6I=",
 "WindowsBase.wasm": "sha256-ydADyJcM/JrxGU0lPCIn9utGtPieXB+ubXRN7TJls5Y=",
 "mscorlib.wasm": "sha256-cDuLeL3OCtVtiid/dyex1MVgbuzDSRwZxKzuP2Dp4mg=",
 "netstandard.wasm": "sha256-A0h86SDieTMoU/wU2JTszWCsUmMuguDcbap0b0BzsmI=",
 "System.Private.CoreLib.wasm": "sha256-/0DNIm/T0C07X7Tuz5uR8JvVCoAfEE2MnfPUSjyS9xc=",
 "ClientBlazorApp.Client.wasm": "sha256-pD1UY5WEd3vKDcFPYb4O3gjvtFv8GGYiTGVxAHo7VTk="
 },
 "pdb": {
 "ClientBlazorApp.Client.pdb": "sha256-xSxxOpBIlM0rbF52lVJgayihQWhbyPNixI7VTgOG2ms="
 }
 },
 "cacheBootResources": true,
 "debugLevel": -1,
 "globalizationMode": "sharded",
 "extensions": {
 "blazor": {}
 }
}

```


Здесь мы можем увидеть список всех библиотек dll, которые будут загружаться для работы приложения


Кроме того, в инструментах браузера мы можем увидеть, что также загружается еще ряд файлов. В частности,


-

dotnet.js: это точка входа ("загрузчик"), который содержит общедоступный API для взаимодействия со средой выполнения .NET.

-

dotnet.native.js: содержит Emscripten API и загружается загрузчиком.

-

dotnet.runtime.js: содержит остальную часть среды выполнения .NET.


## Автоматический рендеринг


При автоматическом рендеринге конкретная модель рендеринга компонента определяется во время выполнения. Сначала применяется рендеринг на стороне сервера, а затем при последующих посещениях после загрузки пакета Blazor применяется рендеринг в WebAssembly.


Так, возьмем выше созданный проект и применим в автоматический рендеринг. Прежде всего изменим файл Program.cs в главном проекте:

```

using ClientBlazorApp.Components;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddRazorComponents()
 .AddInteractiveWebAssemblyComponents()
 .AddInteractiveServerComponents();

var app = builder.Build();

if (app.Environment.IsDevelopment())
{
 app.UseWebAssemblyDebugging();
}
else
{
 app.UseExceptionHandler("/Error", createScopeForErrors: true);
 app.UseHsts();
}

app.UseHttpsRedirection();

app.UseStaticFiles();
app.UseAntiforgery();

app.MapRazorComponents<App>()
 .AddInteractiveWebAssemblyRenderMode()
 .AddInteractiveServerRenderMode()
 .AddAdditionalAssemblies(typeof(ClientBlazorApp.Client._Imports).Assembly);

app.Run();

```


Прежде всего подключаем сервисы для интерактивного рендеринга как стороны клиента, так и стороны сервера

```

builder.Services.AddRazorComponents()
 .AddInteractiveWebAssemblyComponents()
 .AddInteractiveServerComponents();

```


Кроме того, применяем оба типа рендеринга:

```

app.MapRazorComponents<App>()
 .AddInteractiveWebAssemblyRenderMode()
 .AddInteractiveServerRenderMode()
 .AddAdditionalAssemblies(typeof(ClientBlazorApp.Client._Imports).Assembly);


```


Стоит отметить, что компоненты, которые применяют автоматический рендеринг, должны располагаться в отдельном проекте WebAssembly. В нашем случае уже ранее был определен компонент Counter. Применим к
нему автоматический рендеринг:

```

@page "/counter"
@rendermode InteractiveAuto

<h1>Counter</h1>

<button @onclick="IncrementCount">Click</button>
<p>Count: @count</p>

@code {
 int count = 0;

 void IncrementCount()
 {
 count++;
 }
}

```


Применение автоматического рендеринга на уровне компонента заключается в использовании директивы:

```
@rendermode InteractiveAuto
```












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

**Источник:** [https://metanit.com/sharp/blazor/1.8.php](https://metanit.com/sharp/blazor/1.8.php)
