# Управление навигацией и NavigationManager

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по Blazor|Руководство по Blazor]] / [[Языки программирования/C#/Веб-разработка/Руководство по Blazor/Глава 3. Маршрутизация|Глава 3. Маршрутизация]] / Управление навигацией и NavigationManager

[[Языки программирования/C#/Веб-разработка/Руководство по Blazor/Глава 3. Маршрутизация/Параметры строки запроса|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по Blazor/Глава 3. Маршрутизация|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по Blazor/Глава 4. Работа с формами и валидация/Встроенные компоненты ввода|Вперёд]]

**Дата написания:** 05.09.2026

## Управление навигацией и NavigationManager

Последнее обновление: 30.11.2023




-

-

-














С помощью класса NavigationManager в коде C# компонентов Blazor можно управлять навигацией. Это абстрактный класс, и в общем случае фреймворк Blazor сам
создает сервис этого типа, который мы можем получить в копмоненте с помощью встроенного механизма внедрения зависимостей:

```
@inject NavigationManager Navigation
```



Прежде всего NavigationManager предоставляет ряд свойств, которые позволяют получить некоторую информацию о состоянии навигации:


-

Uri: текущий адрес

-

BaseUri: базовый адрес приложения. Обычно устанавливается с помощью элемента `<base>` на html-странице

-

HistoryEntryState: состояние истории навигации


Рассмотрим простейший пример. Пусть у нас есть два компонента - Home и About.
![Навигация компонентов Blazor в приложении на C#](https://metanit.com./pics/3.15.png)


Например, получение текущего адреса в компоненте:

```

@page "/about"

@inject NavigationManager Navigation

<h3>@Navigation.Uri</h3>

```


дополнительно с помощью метода ToBaseRelativePath() можно получить относительный путь, а с помощью метода
ToAbsoluteUri() - абсолютный адрес. Например:

```

@page "/about"
@inject NavigationManager Navigation

<h2>About Page</h2>

<h3>Absolute: @Navigation.Uri</h3>
<h3>Relative: @Navigation.ToBaseRelativePath(Navigation.Uri)</h3>

```

![Получение относительного пути и абсолютного адреса компонента Blazor на C#](https://metanit.com./pics/3.12.png)


### Программная навигация


Для программной навигации у класса NavigationManager применяется метод NavigateTo(). Этот метод имеет три версии

```

public void NavigateTo (string uri, bool forceLoad);
public void NavigateTo (string uri, bool forceLoad = false, bool replace = false);
public void NavigateTo (string uri, Microsoft.AspNetCore.Components.NavigationOptions options);

```


Все три версии в качестве первого параметра принимают адрес перехода. Это может быть как абсолютный адрес, так и относительный путь.


Булевый параметр `forceLoad` при значении `true` указывает, что надо вместо клиентской маршрутизации использовать маршрутизацию сервера. То есть переход
обрабатывается НЕ клиентской системой маршрутизации, а сервером.


Булевый параметр `replace` при значении `true` заменяет текущую запись в истрии браузера. Если же он равен `false` в историю браузера добавляется
новая запись.


Последняя версия метода принимает объект `NavigationOptions`, который позволяет установить те же самые возможности, что и параметры `forceLoad` и `replace`.


Например, выполним программый переъод с одного компонента на другой. В компоненте About определим следующий код:

```

@page "/about"

<h2>About Page</h2>

```


Тут ничего примечательного кроме того, что компонент обрабатывает запросы по пути "/about". И в компоненте Home определим переход к компоненту About:

```

@page "/"
@using Microsoft.AspNetCore.Components.Web
@rendermode RenderMode.InteractiveServer
@inject NavigationManager Navigation

<h2>Home Page</h2>

<button @onclick="GoToAbout">To About Page</button>

@code{
 void GoToAbout()
 {
 Navigation.NavigateTo("about");
 }
}

```


Здесь по нажатию на кнопку вызывается метод `GoToAbout()` выполняется навигация по пути "/about", то есть к компоненту About.
![Программная навигация в компонентах Blazor с помощью NavigationManager в C#](https://metanit.com./pics/3.13.png)


### Отслеживание изменение пути


С помощью события LocationChanged у NavigationManager мы можем отслеживать переходы между компонентами с помощью NavigationManager. В качестве аргумента событие
`LocationChanged` принимает объект LocationChangedEventArgs, через который можно получить информацию о смене расположения. В частности, через
свойство Location можно получить новый адрес, на который выполняется переход.


Рассмотрим на примере. Изменим код компонента Home следующим образом:

```

@page "/"
@using Microsoft.AspNetCore.Components.Routing
@using Microsoft.AspNetCore.Components.Web
@rendermode RenderMode.InteractiveServer
@inject NavigationManager Navigation
@implements IDisposable

<h2>Home Page</h2>
<p><a href="/about">About</a></p>
<button @onclick="GoToAbout">To About Page</button>

@code{
 void GoToAbout()
 {
 Navigation.NavigateTo("/about");
 }

 protected override void OnInitialized()
 {
 Navigation.LocationChanged += HandleLocationChanged;
 }

 private void HandleLocationChanged(object? sender, LocationChangedEventArgs e)
 {
 Console.WriteLine($"URL of new location: {e.Location}");
 }

 public void Dispose()
 {
 Navigation.LocationChanged -= HandleLocationChanged;
 }
}

```


В компоненте Home определена ссылка на компонент About, а также кнопка, по нажатию на которую также происходит переход к компоненту About.
Чтобы подписаться на событие в методе `OnInitialized()`, который срабатывает при инициализации компонента, устанавливаем для события обработчик:

```

protected override void OnInitialized()
{
 Navigation.LocationChanged += HandleLocationChanged;
}

```


В обработчике HandleLocationChanged просто выводим на консоль новый адрес, на который выполняется переход:

```

private void HandleLocationChanged(object? sender, LocationChangedEventArgs e)
{
 Console.WriteLine($"URL of new location: {e.Location}");
}

```


Поскольку мы имеем дело с событиями, то нам надо отписаться от них в методе Dispose

```

@implements IDisposable // реализуем интерфейс IDisposable

//...............

public void Dispose()
{
 Navigation.LocationChanged -= HandleLocationChanged;
}

```


И вне зависимости от того, как мы будем переходить к компоненту About - по нажатию на ссылку или программно по нажатию на кнопку, в обоих случаях сработает обработчик HandleLocationChanged,
и на консоль будет выведена строка с новым адресом










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

**Источник:** [https://metanit.com/sharp/blazor/3.6.php](https://metanit.com/sharp/blazor/3.6.php)
