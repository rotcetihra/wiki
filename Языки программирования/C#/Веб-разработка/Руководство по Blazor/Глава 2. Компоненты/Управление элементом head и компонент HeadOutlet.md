# Управление элементом head и компонент HeadOutlet

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по Blazor|Руководство по Blazor]] / [[Языки программирования/C#/Веб-разработка/Руководство по Blazor/Глава 2. Компоненты|Глава 2. Компоненты]] / Управление элементом head и компонент HeadOutlet

[[Языки программирования/C#/Веб-разработка/Руководство по Blazor/Глава 2. Компоненты/Привязка моделей|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по Blazor/Глава 2. Компоненты|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по Blazor/Глава 2. Компоненты/Файл _Imports.razor и общие директивы компонентов|Вперёд]]

**Дата написания:** 05.09.2026

## Управление элементом head и компонент HeadOutlet

Последнее обновление: 30.11.2023




-

-

-














Компоненты Blazor могут изменить содержимое элемента `<head>` html-страницы, в частности, заголовок и метаданные. Для этого применяется встроенный компонент
HeadOutlet. HeadOutlet, в свою очередь, вставляет на страницу содержимое, предоставляемое другими компонентами -
PageTitle и HeadContent.


Встроенный компонент <PageTitle> устанавливает заголовок страницы (то, что помещается в элемент `<title>` на html-странице):

```
<PageTitle>Текст заголовка</PageTitle>
```


Компонент
<HeadContent> устанавливает метаданные и прочие элементы, которые надо поместить в элемент `<head>`,:

```

<HeadContent>
 элементы, добавляемые в <head>
</HeadContent>

```


Для работы с компонентом HeadOutlet прежде всего необходимо добавить этот компонент. Например, определим следующий корневой комонент
App.razor

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


В секции `<head>` определен компонент HeadOutlet:

```

<head>
 <HeadOutlet />
 <meta charset="utf-8" />
</head>

```


Через HeadOutlet будет устанавливаться сождержимое, которое зависит от компонента. Также можно установить теги, которые не зависят от конкретного компонента. Например, в данном случае это метатег кодировки
страницы.


Поскольку компонент HeadOutlet располагается в пространстве имен `Microsoft.AspNetCore.Components.Web`, то в начале компонента импортируем данное пространство имен.В коде компонента App происходит обращение к другому компоненту - Home. Теперь определим следующий компонент Home:

```

@using Microsoft.AspNetCore.Components.Web

<PageTitle>METANIT.COM</PageTitle>
<HeadContent>
 <meta name="description" content="Как устанавливать заголовок страницы в Blazor" />
 <meta name="updated_at" content="@DateTime.Now" />
</HeadContent>

<h2>Hello METANIT.COM</h2>

```


Здесь в качестве заголовка страницы здесь будет применяться текст "METANIT.COM". Кроме того, в `<head>` будут помещаться два элемента

```

<meta name="description" content="Как устанавливать заголовок страницы в Blazor" />
<meta name="updated_at" content="@DateTime.Now" />

```


И при рендеринге компонента мы увидим эти элементы в коде страницы:
![Установка заголовка страницы с помощью HeadOutlet в компонентах Blazor в C#](https://metanit.com./pics/2.33.png)










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

**Источник:** [https://metanit.com/sharp/blazor/2.13.php](https://metanit.com/sharp/blazor/2.13.php)
