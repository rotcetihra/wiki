# Введение в tag-хелперы

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по Razor Pages|Руководство по Razor Pages]] / [[Языки программирования/C#/Веб-разработка/Руководство по Razor Pages/Глава 3. Определение пользовательского интерфейса|Глава 3. Определение пользовательского интерфейса]] / Введение в tag-хелперы

[[Языки программирования/C#/Веб-разработка/Руководство по Razor Pages/Глава 3. Определение пользовательского интерфейса/Файл _ViewImports.cshtml|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по Razor Pages/Глава 3. Определение пользовательского интерфейса|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по Razor Pages/Глава 3. Определение пользовательского интерфейса/Создание ссылок|Вперёд]]

**Дата написания:** 05.09.2026

## Введение в tag-хелперы

Последнее обновление: 18.04.2022




-

-

-














Для определения пользовательского интерфейса можно применять стандартные элементы html, а также конструкции Razor. Но кроме того для упрощения создания интерфейса
ASP.NET Core предоставляет специальный инструмент, который называется tag-хелперы. Tag-хелперы представляют функциональность, предназначенную для генерации
HTML-разметки. Tag-хелперы выглядят как обычные html-элементы или атрибуты, однако при работе приложения они обрабатываются движком Razor на стороне сервера и в
конечном счете преобразуются в стандартные html-элементы.


Использовать tag-хелперы довольно просто. Допустим, у нас в проекте в папке Pages есть две страницы: Index.cshtml
и About
![Подключение tag-хелперов в Razor Pages в ASP.NET Core и C#](https://metanit.com./pics/3.10.png)


На странице Index.cshtml определим следующий код:

```

@page

@addTagHelper *, Microsoft.AspNetCore.Mvc.TagHelpers

<a asp-page="About">About</a>

```


Сначала на странице идет директива addTagHelper

```
@addTagHelper *, Microsoft.AspNetCore.Mvc.TagHelpers
```


Первый параметр директивы указывает на tag-хелперы, которые будут доступны на странице Razor, а второй параметр определяет
библиотеку хелперов. В данном случае директива использует синтаксис подстановок - знак звездочки ("*") означает, что подключаются все хелперы из
библиотеки Microsoft.AspNetCore.Mvc.TagHelpers.


Далее идет собственно tag-хелпер:

```
<a asp-page="About">О приложении</a>
```


Внешне данный хелпер напоминает обычную ссылку - стандартный элемент html, однако это не элемент html. И если мы воспользуемся всплывающей подсказкой,
то увидим, что кроме обычных для элемента `<a />` он имеет ряд других:
![Tag хелперы в Razor Pages ASP.NET Core и C#](https://metanit.com./pics/3.11.png)


Данный хелпер создает ссылку, которая указывает на страницу About.cshtml. В итоге при запуске проекта вместа данного tag-хелпера будет
сформирована гиперссылка, по нажатию на которую уйдет запрос на страницу About.cshtml:
![добавление tag-хелперов на страницу Razor Pages в ASP.NET Core и C#](https://metanit.com./pics/3.12.png)


### _ViewImports.cshtml и @addTagHelper


Выше на странице Index.cshtml были подключены tag-хелперы. Но что, если нам надо подключить tag-хелперы на множество страниц Razor? Вместо того, чтобы прописывать директиву
@addTagHelper на каждой отдельной странице, мы можем подключить все хелперы разом.
Для этого, как и для подключения различных пространств имен, применяется файл _ViewImports.cshtml.


Итак, добавим в проект в папку Pages новый файл _ViewImports.cshtml:
![_ViewImports.cshtml в ASP.NET Core MVC и C#](https://metanit.com./pics/3.13.png)


В файле _ViewImports.cshtml определим подключение tag-хелперов:

```
@addTagHelper *, Microsoft.AspNetCore.Mvc.TagHelpers
```


После этого из кода страницы Index.cshtml можно удалить подключение tag-хелперов и оставить только создание ссылки:

```

@page

<a asp-page="Contacts">О приложении</a>

```


### Удаление tag-хелперов


Еще одна директива `removeTagHelper` удаляет ранее добавленные tag-хелперы. Ее применение аналогично:

```
@removeTagHelper "*, Microsoft.AspNetCore.Mvc.TagHelpers"
```


Данная директива может быть полезной, если мы, например, захотим ограничить применение хелперов в какой-то одной странице или группе страниц Razor.
Эту директиву также можно определять в файле _ViewImports.cshtml.











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

**Источник:** [https://metanit.com/sharp/razorpages/3.3.php](https://metanit.com/sharp/razorpages/3.3.php)
