# Файл _Imports.razor и общие директивы компонентов

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по Blazor|Руководство по Blazor]] / [[Языки программирования/C#/Веб-разработка/Руководство по Blazor/Глава 2. Компоненты|Глава 2. Компоненты]] / Файл _Imports.razor и общие директивы компонентов

[[Языки программирования/C#/Веб-разработка/Руководство по Blazor/Глава 2. Компоненты/Управление элементом head и компонент HeadOutlet|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по Blazor/Глава 2. Компоненты|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по Blazor/Глава 3. Маршрутизация/Маршрутизация между компонентами|Вперёд]]

**Дата написания:** 05.09.2026

## Файл _Imports.razor и общие директивы компонентов

Последнее обновление: 30.11.2023




-

-

-














Проект может содержать множество компонентов, и различные компоненты могут применять ряд общих директив, например, подключать ряд общих пространств имен.


Например, в прошлой теме было два компонента - App.razor и Home.razor.


Компонент App.razor является корневым и устанавливает общую структуру веб-страницы:

```

@page "/"
@using Microsoft.AspNetCore.Components.Web

<!DOCTYPE html>
<html>
<head>
 <HeadOutlet />
 <meta charset="utf-8" />
</head>
<body>
 <Home />
 <script src="_framework/blazor.web.js"></script>
</body>
</html>

```


В данном случае в секции `<head>` применяется встроенный компонент HeadOutlet, но для его применения надо подключить пространство имен
`Microsoft.AspNetCore.Components.Web`.


Во втором компоненте - Home.razor с помощью встроенных компонентов PageTitle и HeadContent устанавливаем метаданные страницы:

```

@using Microsoft.AspNetCore.Components.Web

<PageTitle>METANIT.COM</PageTitle>
<HeadContent>
 <meta name="description" content="Как устанавливать заголовок страницы в Blazor" />
 <meta name="updated_at" content="@DateTime.Now" />
</HeadContent>

<h2>Hello METANIT.COM</h2>

```


И для применения встроенных компонентов PageTitle и HeadContent опять же надо подключить пространство имен "Microsoft.AspNetCore.Components.Web", где эти компоненты содержатся.


Таким образом, мы дублируем в обоих компонентах поключение одного и того же пространства имен. И таких общих пространств имен может быть много. И компонентов, которые их подключают, тоже может быть много.
Поэтому отдельное подключение пространств имен, да и вообще использование повторяющихся директив для компонентов нецелесообразно.


В этом случае мы можем определить в папке компонентов файл с именем _Imports.razor (который фактически тоже выступает как компонент) и
определить в этом файлы все общие директивы компонентов, например, подключение общих пространств имен. А при создании приложения фреймворк blazor подхватит этот файл и добавит его директивы в другие компоненты.


Так, добавим в папку компонентов новый файл _Imports.razor
![_Imports.razor в Blazor](https://metanit.com./pics/2.62.png)


Определим в этом файле следующий код:

```
@using Microsoft.AspNetCore.Components.Web
```


После этого мы можем убрать подключение данного пространства имен из остальных компонентов - App и Home. Например, код компонента
App.razor после изменения:

```

@page "/"

<!DOCTYPE html>
<html>
<head>
 <HeadOutlet />
 <meta charset="utf-8" />
</head>
<body>
 <Home />
 <script src="_framework/blazor.web.js"></script>
</body>
</html>

```


И код компонента Home.razor:

```

<PageTitle>METANIT.COM</PageTitle>
<HeadContent>
 <meta name="description" content="Как устанавливать заголовок страницы в Blazor" />
 <meta name="updated_at" content="@DateTime.Now" />
</HeadContent>

<h2>Hello METANIT.COM</h2>

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

**Источник:** [https://metanit.com/sharp/blazor/2.14.php](https://metanit.com/sharp/blazor/2.14.php)
