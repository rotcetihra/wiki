# Определение страниц Razor

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по Razor Pages|Руководство по Razor Pages]] / [[Языки программирования/C#/Веб-разработка/Руководство по Razor Pages/Глава 2. Основы Razor Pages|Глава 2. Основы Razor Pages]] / Определение страниц Razor

[[Языки программирования/C#/Веб-разработка/Руководство по Razor Pages/Глава 1. Введение в Razor Pages/Добавление RazorPages в пустой проект|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по Razor Pages/Глава 2. Основы Razor Pages|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по Razor Pages/Глава 2. Основы Razor Pages/Синтаксис Razor|Вперёд]]

**Дата написания:** 05.09.2026

## Определение страниц Razor

Последнее обновление: 15.04.2022




-

-

-














Основой функциональности платформы Razor Pages являются страницы Razor, которые обрабатывают приходящие к приложению запросы. Рассмотрим, как определять страницы Razor.
Для этого создадим новый проект по типу ASP NET Core Empty. По умолчанию проект этого типа не подключает функциональность Razor Pages, поэтому
после создания проекта первым делом подключим в него функциональность Razor Pages. Для этого откроем файл Program.cs и изменим его следующим образом:

```

var builder = WebApplication.CreateBuilder(args);

// добавляем в приложение сервисы Razor Pages
builder.Services.AddRazorPages();

var app = builder.Build();

// добавляем поддержку маршрутизации для Razor Pages
app.MapRazorPages();

app.Run();

```


### Добавление страницы Razor Page


По умолчанию согласно условностям страницы Razor размещаются в проекте в папке Pages. А строка запроса URL будет сопоставляться с определенной страницей
Razor на основании ее расположения в проекте в папке Pages. Примеры строк URL и сопоставленных с ними страниц:


| Путь к странице | URL |
| --- | --- |
| /Pages/Index.cshtml | / или /Index |
| /Pages/Contact.cshtml | /Contact |
| /Pages/Store/Contact.cshtml | /Store/Contact |
| /Pages/Store/Index.cshtml | /Store или /Store/Index |


Поэтому добавим в проект папку Pages. Затем в папку Pages добавим новую страницу Razor.
Для этого нажмем на данную папку правой кнопкой мыши и выберем в контекстном меню пункт Add -> New Item.
Далее среди шаблонов выберем шаблон Razor Page - Empty и назовем новый файл Index.cshtml:
![Создание Razor Page в ASP.NET Core и C#](https://metanit.com./pics/1.9.png)


После создания этой страницы в проект в папку Pages будут добавлены два файла - сама страница Index.cshtml и
связаный с ней файл кода Index.cshtml.cs.
![Страница Razor Page и файл связанного кода в ASP.NET Core и C#](https://metanit.com./pics/1.10.png)


По умолчанию файл Index.cshtml выглядит следующим образом:

```

@page
@model RazorPagesApp.Pages.IndexModel
@{
}

```


Любая страница Razor должна начинаться с директивы @page - именно эта директива указывает,
что данный файл представляет страницу Razor. После этой директивы может помещаться код html, какие-то выражения синтаксиса Razor. Так, в данном случае с
помощью директивы @model определяет модель представления - в данном случае класс IndexModel - класс, который определен в файле Index.cshtml.cs.
Но в принципе опреление модели необязательно. Например, изменим код страницы следующим образом:

```

@page

<h2>Hello METANIT.COM</h2>

```


Это простейшая страница Razor, которая определяет заголовок
![Определение страницы Razor Page в ASP.NET Core и C#](https://metanit.com./pics/2.1.png)


При этом использование модели на странице в принципе необязательно, как видно из примера выше.


Подобным образом мы можем использовать и другие страницы. Например, добавим в папку Pages новую страницу Razor, которую назовем
About.cshtml
![страницы Razor Pages на C#](https://metanit.com./pics/2.48.png)


Определим на ней какое-нибудь простейшее содержимое:

```

@page

<h2>О сайте</h2>

```


После этого мы можем обратиться к этой странице по адресу "/About":
![обращение к странице Razor Pages в ASP.NET Core и C#](https://metanit.com./pics/2.49.png)


### Переопределение каталога страниц


Хотя обычно страницы Razor помещаются в проекте в каталог Pages, но это необязательно. Например, определим в проекте новую папку MyPages. И далее
в эту папку добавим новую страницу Razor Index.cshtml:
![Установка каталога для страниц Razor в ASP.NET Core и C#](https://metanit.com./pics/2.9.png)


Определим на этой странице какой-нибудь простейший контент, например:

```

@page

<h2>Index Page from MyPages folder</h2>

```


Для изменения каталога для Razor Pages необходимо настроить соответствующие сервисы. Для этого перейдем к файлу Program.cs и изменим его следующим образом:

```

var builder = WebApplication.CreateBuilder(args);

// добавляем в приложение сервисы Razor Pages
builder.Services.AddRazorPages(options => options.RootDirectory = "/MyPages");

var app = builder.Build();

// добавляем поддержку маршрутизации для Razor Pages
app.MapRazorPages();

app.Run();

```


Метод `AddRazorPages()` в качестве параметра принимает делегат Action, который, в свою очередь, имеет параметр RazorPagesOptions.
Через этот параметр можно задать некоторые базовые настройки для Razor Pages. В частности, свойство options.RootDirectory позволяет установить корневой каталог
для страниц Razor.


Соответственно теперь запросы к приложению будут обрабатываться страницами из папки "MyPages":
![Настройка страниц Razor Pages и AddRazorPages в ASP.NET Core и C#](https://metanit.com./pics/2.10.png)











- Глава 1. Введение в Razor Pages


 - [Введение в Razor Pages. Первый проект с .NET CLI](//metanit.com/sharp/razorpages/1.3.php)

 - [Первый проект в Visual Studio](//metanit.com/sharp/razorpages/1.1.php)

 - [Добавление RazorPages в пустой проект](//metanit.com/sharp/razorpages/1.2.php)



- Глава 2. Основы Razor Pages


 - [Определение страниц Razor](//metanit.com/sharp/razorpages/2.1.php)

 - [Синтаксис Razor](//metanit.com/sharp/razorpages/2.2.php)

 - [Модель страницы Razor](//metanit.com/sharp/razorpages/2.3.php)

 - [Обработка запросов. Контекст страницы Razor](//metanit.com/sharp/razorpages/2.4.php)

 - [Передача данных на страницу Razor в GET-запросе](//metanit.com/sharp/razorpages/2.5.php)

 - [POST-запросы и отправка форм](//metanit.com/sharp/razorpages/2.6.php)

 - [Привязка свойств страниц и моделей Razor к параметрам запроса](//metanit.com/sharp/razorpages/2.7.php)

 - [Параметры маршрутов](//metanit.com/sharp/razorpages/2.8.php)

 - [Обработчики страницы](//metanit.com/sharp/razorpages/2.9.php)

 - [Возвращение результата](//metanit.com/sharp/razorpages/2.10.php)

 - [Отправка файлов](//metanit.com/sharp/razorpages/2.11.php)

 - [Отправка статусных кодов](//metanit.com/sharp/razorpages/2.12.php)

 - [Переадресация](//metanit.com/sharp/razorpages/2.13.php)

 - [Передача зависимостей на страницу](//metanit.com/sharp/razorpages/2.14.php)

 - [ViewBag и ViewData](//metanit.com/sharp/razorpages/2.15.php)



- Глава 3. Определение пользовательского интерфейса


 - [Мастер-страницы layout](//metanit.com/sharp/razorpages/3.1.php)

 - [Файл _ViewImports.cshtml](//metanit.com/sharp/razorpages/3.2.php)

 - [Введение в tag-хелперы](//metanit.com/sharp/razorpages/3.3.php)

 - [Создание ссылок](//metanit.com/sharp/razorpages/3.4.php)

 - [Работа с формами. Tag-хелперы форм](//metanit.com/sharp/razorpages/3.5.php)



- Глава 4. Работа с базой данных через Entity Framework


 - [Подключение к базе данных](//metanit.com/sharp/razorpages/4.1.php)

 - [Создание и вывод объектов из базы данных](//metanit.com/sharp/razorpages/4.2.php)

 - [Изменение и удаление в базе данных](//metanit.com/sharp/razorpages/4.3.php)










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

**Источник:** [https://metanit.com/sharp/razorpages/2.1.php](https://metanit.com/sharp/razorpages/2.1.php)
