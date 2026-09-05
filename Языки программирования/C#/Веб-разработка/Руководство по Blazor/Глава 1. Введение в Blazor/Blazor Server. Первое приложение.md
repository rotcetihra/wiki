# Blazor Server. Первое приложение

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по Blazor|Руководство по Blazor]] / [[Языки программирования/C#/Веб-разработка/Руководство по Blazor/Глава 1. Введение в Blazor|Глава 1. Введение в Blazor]] / Blazor Server. Первое приложение

[[Языки программирования/C#/Веб-разработка/Руководство по Blazor/Глава 1. Введение в Blazor/Первое приложение на Blazor|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по Blazor/Глава 1. Введение в Blazor|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по Blazor/Глава 1. Введение в Blazor/Рендеринг WebAssembly и авторендеринг|Вперёд]]

**Дата написания:** 05.09.2026

## Рендеринг на сервере

Последнее обновление: 29.11.2023




-

-

-














### Статический рендеринг


Самая простая модель рендеринга в приложении Blazor представляет статический рендеринг на сервере. Так, создадим новый проект Blazor по типу Blazor Web App.


При создании проекта для опции Interactive render mode укажем значение None (интерактивность по умолчанию отсутствует).
И также снимем отметку с поля Include sample pages, чтобы проект был предельно простым:
![Статический рендеринг в приложении Blazor](https://metanit.com./pics/1.34.png)


Для создания аналогичного проекта с помощью .NET CLI применяется команда

```
dotnet new blazor -o ServerBlazorApp -e --interactivity None
```


В итоге у нас получится следующий проект:
![Статический рендеринг в приложении Blazor на ASP.NET Core](https://metanit.com./pics/1.35.png)


В чем отличительные особенности проекта со статическим рендерингом? Посмотрим на файл Program.cs:

```

using StaticBlazorApp.Components;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddRazorComponents();

var app = builder.Build();

if (!app.Environment.IsDevelopment())
{
 app.UseExceptionHandler("/Error", createScopeForErrors: true);
 app.UseHsts();
}

app.UseHttpsRedirection();

app.UseStaticFiles();
app.UseAntiforgery();

app.MapRazorComponents<App>();

app.Run();


```


Для приложения Blazor здесь важны два момента. Прежде всего добавляем сервисы для работы с компонентами Razor:

```
builder.Services.AddRazorComponents();
```


Затем устанавливаем корневой компонент приложения - App:

```
app.MapRazorComponents<App>();
```


Благодаря этому компоненты Blazor внутри компонента App смогут сопоставляться с запросами.


Эти два метода позволяют определить базовое приложение Blazor. Однако оно не применяет никакой интерактивности, только статический рендеринг.


В папке "Components/Pages" есть один базовый компонент, которые сопоставляется с запросами - Home.razor


Мы можем запустить проект и попереходить по ссылкам, обращаясь к компонентам:
![Статический рендеринг Blazor](https://metanit.com./pics/1.36.png)


Тем не менее поддержка интерактивности в проекте отсутствует. Для теста изменим данный компонент следующим образом:

```

@page "/"

<PageTitle>Home</PageTitle>

<h1>Hello, world!</h1>

<button @onclick="IncrementCount">Click</button>
<p>Count: @count</p>
@code {
 int count = 0;
 void IncrementCount() => count++;
}

```


Теперь компонент определяет кнопку, по нажатию на которую срабатывает метод IncrementCount, увеличивая значение переменной count.
То есть мы предполагаем некоторую интерактивность - нажимаем на кнопку, счетчик увеличивается и изменяется содержимое страницы. Тем не менее поскольку интерактивность не подключена,
нажатия на кнопку не будут иметь никакого смысла, а счетчик count все время будет равен 0:
![Статический рендеринг Blazor ASP.NET Core](https://metanit.com./pics/1.37.png)


Соответственно такой тип рендеринга подходит для статических сайтов, где не нужна интерактивность, и в тоже время можно сочетать различные преимущества Blazor, типа организации веб-приложения, установку общего макета веб-страниц.


### Интерактивный рендеринг на сервере


Для поддержки на сервере интерактивного рендеринга изменим файл Program.cs следующим образом:

```

using ServerBlazorApp.Components;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddRazorComponents()
 .AddInteractiveServerComponents(); // добавляем сервисы интерактивного рендеринга

var app = builder.Build();

if (!app.Environment.IsDevelopment())
{
 app.UseExceptionHandler("/Error", createScopeForErrors: true);
 app.UseHsts();
}

app.UseHttpsRedirection();

app.UseStaticFiles();
app.UseAntiforgery();

app.MapRazorComponents<App>()
 .AddInteractiveServerRenderMode(); // устанавливаем поддержку рендеринга на сервере

app.Run();

```


Здесь опять же важны два момента. Прежде всего нам надо добавить необходимые сервисы для поддержки интерактивного рендеринга на сервере:

```
AddInteractiveServerComponents()
```


Далее непосредственно устанавливаем режим интерактивного рендеринга:

```
AddInteractiveServerRenderMode()
```


После этого надо настроить режим рендеринга для компонентов. Это можно сделать как для всех компонентов приложения глобально, так и для отдельных компонентов. Для применения режима рендеринга для компонентов
применяется директива @rendermode, которая получает одно из значений перечисления `Microsoft.AspNetCore.Components.Web.RenderMode`:


-

`InteractiveServer`

-

`InteractiveWebAssembly`

-

`InteractiveAuto`


Соответственно, чтобы применить рендеринг на сервере, надо использовать значение `InteractiveServer`. Так, изменим компонент
Home.razor следующим образом:

```

@page "/"
@using static Microsoft.AspNetCore.Components.Web.RenderMode
@rendermode InteractiveServer

<PageTitle>Home</PageTitle>

<h1>Hello, world!</h1>

<button @onclick="IncrementCount">Click</button>
<p>Count: @count</p>
@code {
 int count = 0;
 void IncrementCount()
 {
 count++;
 Console.WriteLine($"count: {count}");
 }
}

```


Здесь сначала импортируем перечисление `RenderMode`

```
@using static Microsoft.AspNetCore.Components.Web.RenderMode
```


В реальности его не надо импортировать для каждого компонента, и обычно оно импортируется в файле _Imports.razor сразу для всех компонентов.


Затем собственно применяем режим рендеринга:

```
@rendermode InteractiveServer
```


Запустим сервер, и благодаря соединению SignalR между сервером и клиентом будет происходить взаимодействие. При нажати на кнопку на сервере выполнится метод IncrementCount, который увеличивает переменную count,
клиент получить результат работы сервера и обновит код страницы.
![Интерактивный рендеринг на сервере в Blazor ASP.NET Core](https://metanit.com./pics/1.38.png)












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

**Источник:** [https://metanit.com/sharp/blazor/1.7.php](https://metanit.com/sharp/blazor/1.7.php)
