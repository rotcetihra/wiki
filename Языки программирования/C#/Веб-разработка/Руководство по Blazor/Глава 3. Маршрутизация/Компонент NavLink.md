# Компонент NavLink

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по Blazor|Руководство по Blazor]] / [[Языки программирования/C#/Веб-разработка/Руководство по Blazor/Глава 3. Маршрутизация|Глава 3. Маршрутизация]] / Компонент NavLink

[[Языки программирования/C#/Веб-разработка/Руководство по Blazor/Глава 3. Маршрутизация/Компоновка|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по Blazor/Глава 3. Маршрутизация|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по Blazor/Глава 3. Маршрутизация/Параметры маршрутов|Вперёд]]

**Дата написания:** 05.09.2026

## Компонент NavLink

Последнее обновление: 30.11.2023




-

-

-














Встроенный компонент NavLink применяется для создания ссылок на компоненты. В целом этот компонент ведет себя как стандартный html-элемент `<a>`
за тем исключением, что он также переключает css-класс `active`, который позволяет стилизовать текующю активную ссылку.


Пусть у нас есть в проекте в папке "Components/Pages" три маршоутизируемых компонента: Home, Contacts и About
с каким-нибудь содержимым:
![NavLink и создание ссылок в компонентах Blazor на C#](https://metanit.com./pics/3.19.png)


Например, пусть в компоненте Home будет следующее содержимое:

```

@page "/"

<h2>Home Page</h2>

```



Компонент Contacts:

```

@page "/contacts"

<h2>Contacts Page</h2>

```



Компонент About:

```

@page "/about"

<h2>About Page</h2>

```


В папке Components/Layouts определим компонент компоновки MainLayout со следующим кодом:

```

@inherits LayoutComponentBase
@using Microsoft.AspNetCore.Components.Routing @*для NavLink*@
<style>
 a {
 color: #00897B;
 }
 a.active {
 color: #004D40;
 font-weight: 700;
 }
</style>
<div>
 <div>
 <NavLink href="/">Home</NavLink> |
 <NavLink href="contacts">Contacts</NavLink> |
 <NavLink href="about">About</NavLink>
 </div>
 <div>
 @Body
 </div>
</div>

```


Здесь с помощью компонента `NavLink` определены ссылки на компоненты Home, Contacts и About. Кроме того, определены стили ссылок, в частности, класс `active`
для стилизации активной ссылки.


В компоненте App определим маршрутизацию и применим компонент компоновки:

```

@using Microsoft.AspNetCore.Components.Routing
@** пространство имен компонента MainLayout **@
@using BlazorApp.Components.Layouts

<!DOCTYPE html>
<html>
<head>
 <title>METANIT.COM</title>
 <meta charset="utf-8" />
 <base href="/" />
</head>
<body>
 <Router AppAssembly="@typeof(Program).Assembly">
 <Found Context="routeData">
 <RouteView RouteData="routeData" DefaultLayout="@typeof(MainLayout)" />
 </Found>
 </Router>
 <script src="_framework/blazor.web.js"></script>
</body>
</html>

```


Если мы запустим проект, то по NavLink будут создаваться сслыки, которые будут стилизоваться в соответствии с установленными нами стилями:
![Стилизация NavLink в компонентах Blazor на C#](https://metanit.com./pics/3.20.png)


Однако мы видим, что при переходе к компонентам Contacts и About стилизуются как активная ссылка (с помощью класса `active`) не только ссылки
на эти компоненты, но и ссылка на компонент Home, что, возможно, представляет не самое лучшее и ожидаемое поведение.


С помощью свойства Match класс NavLink позволяет установить, в каком случае к ссылке будет применяться класс `active`. Это свойство
принимает значение типа `NavLinkMatch` и может принимать два значения:


-

`NavLinkMatch.All`: ссылка активна, если ее адрес полностью соответствует адресу текущего компонента.

-

`NavLinkMatch.Prefix`: ссылка активна, если ее адрес соответствует началу адреса текущего компонента (значение по умолчанию).


В примере выше адрес компонента About представляет путь "/about" - он начинается с префикса "/", а это путь к компоненту Home. Поэтому как активные выделяются две ссылки -
на компонент About и на компонент Home. Чтобы выйти из этой ситуации у NavLink свойству `Match` надо передать значение `NavLinkMatch.All`:

```

<div>
 <NavLink Match="NavLinkMatch.All" href="/">Home</NavLink> |
 <NavLink href="contacts">Contacts</NavLink> |
 <NavLink href="about">About</NavLink>
</div>

```

![Настройка NavLink в компонентах Blazor на C#](https://metanit.com./pics/3.21.png)


Стоит отметить, что с помощью свойства ActiveClass компонента `NavLink` можно установить другой класс в качестве класса активной ссылки.

```

@inherits LayoutComponentBase
@using Microsoft.AspNetCore.Components.Routing @*для NavLink*@
<style>
 a {
 color: #F44336;
 }
 .activeNavLink {
 color: #B71C1C;
 font-weight:700;
 }
</style>
<div>
 <div>
 <NavLink ActiveClass="activeNavLink" Match="NavLinkMatch.All" href="/">Home</NavLink> |
 <NavLink ActiveClass="activeNavLink" href="contacts">Contacts</NavLink> |
 <NavLink ActiveClass="activeNavLink" href="about">About</NavLink>
 </div>
 <div>
 @Body
 </div>
</div>

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

**Источник:** [https://metanit.com/sharp/blazor/3.3.php](https://metanit.com/sharp/blazor/3.3.php)
