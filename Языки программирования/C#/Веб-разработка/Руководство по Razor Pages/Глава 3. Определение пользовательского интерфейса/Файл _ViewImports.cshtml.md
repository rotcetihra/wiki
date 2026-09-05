# Файл _ViewImports.cshtml

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по Razor Pages|Руководство по Razor Pages]] / [[Языки программирования/C#/Веб-разработка/Руководство по Razor Pages/Глава 3. Определение пользовательского интерфейса|Глава 3. Определение пользовательского интерфейса]] / Файл _ViewImports.cshtml

[[Языки программирования/C#/Веб-разработка/Руководство по Razor Pages/Глава 3. Определение пользовательского интерфейса/Мастер-страницы layout|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по Razor Pages/Глава 3. Определение пользовательского интерфейса|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по Razor Pages/Глава 3. Определение пользовательского интерфейса/Введение в tag-хелперы|Вперёд]]

**Дата написания:** 05.09.2026

## Файл _ViewImports.cshtml

Последнее обновление: 18.04.2022




-

-

-














Файл _ViewImports.cshtml позволяет по умолчанию подключить на страницы Razor некоторый функционал. Сначала рассмотрим ситуацию, с которой мы
можем столкнуться. Пусть у нас в проекте есть некоторый класс Person:

```

namespace RazorPagesApp
{
 public record class Person(string Name, int Age);
}

```


Допустим, мы хотим использовать тип Person на странице Index.cshtml:

```

@page

@* Подключаем пространство имен класса Person *@
@using RazorPagesApp
@{
 Person tom = new Person("Tom", 37);
}
<h2>Person Data</h2>
<p>Name: <b>@tom.Name</b></p>
<p>Age: <b>@tom.Age</b></p>

```


Чтобы использовать тип Person на странице Razor, мы вынуждены импортировать с помощью директивы using пространство имен, где этот тип определен.
В данном случае ничего сложного нет, однако если у нас куча страниц, где мы хотим использовать этот же тип Person, то мы будем вынуждены определить
то же самое выражение импорта на всех страницах. Это может создавать некоторые неудобства. Во-первых, мы повторяем один и тот же код. Во-вторых,
если пространство имен изменится, то мы вынуждены будем менять все страницы. В-третьих, возможно, мы захотим подключить еще какие-то пространства имен, что
увеличит работу, если будут какие-то изменения. Файл _ViewImports.cshtml решает эту проблему


Итак, добавим в проект в папку Pages файл _ViewImports.cshtml. Для его добавления в Visual Studio можно применять шаблон
Razor View Imports:
![_ViewImports.cshtml в Razor Pages ASP.NET Core и C#](https://metanit.com./pics/3.7.png)


Далее добавим в этот файл подключение пространства имен класса Person:

```

@* Подключаем пространство имен класса Person *@
@using RazorPagesApp

```

![файл _ViewImports.cshtml в ASP.NET Core Razor Pages и C#](https://metanit.com./pics/3.8.png)


В этом случае функциональность пространства имен `RazorPagesApps` будет автоматически подключаться на все страницы Razor.


И тогда мы можем убрать из страницы Index.cshtml подключение пространства имен:

```

@page

@{
 Person tom = new Person("Tom", 37);
}
<h2>Person Data</h2>
<p>Name: <b>@tom.Name</b></p>
<p>Age: <b>@tom.Age</b></p>

```

![файл _ViewImports.cshtml и подключение на страницу Razor Pages в ASP.NET Core и C#](https://metanit.com./pics/3.9.png)











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

**Источник:** [https://metanit.com/sharp/razorpages/3.2.php](https://metanit.com/sharp/razorpages/3.2.php)
