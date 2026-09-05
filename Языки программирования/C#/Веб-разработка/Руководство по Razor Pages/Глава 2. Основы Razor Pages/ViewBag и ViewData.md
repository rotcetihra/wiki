# ViewBag и ViewData

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по Razor Pages|Руководство по Razor Pages]] / [[Языки программирования/C#/Веб-разработка/Руководство по Razor Pages/Глава 2. Основы Razor Pages|Глава 2. Основы Razor Pages]] / ViewBag и ViewData

[[Языки программирования/C#/Веб-разработка/Руководство по Razor Pages/Глава 2. Основы Razor Pages/Передача зависимостей на страницу|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по Razor Pages/Глава 2. Основы Razor Pages|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по Razor Pages/Глава 3. Определение пользовательского интерфейса/Мастер-страницы layout|Вперёд]]

**Дата написания:** 05.09.2026

## ViewBag и ViewData

Последнее обновление: 18.04.2022




-

-

-














Для передачи данных из кода c# на страницу Razor можно использовать ряд способов. Самый распространенный и предпочтительный - использование свойств модели страницы.
Тем не менее есть и другие способы, в частности, примение объектов ViewBag и ViewData.


### ViewData


ViewData представляет словарь из пар ключ-значение.


Например, у нас есть страница Razor Index.cshtml и код связанной модели IndexModel в файле Index.cshtml.cs:
![OnGet и OnPost в Razor Page в ASP.NET Core и C#](https://metanit.com./pics/2.13.png)


В коде модели IndexModel в файле Index.cshtml.cs определим следующий код:

```

using Microsoft.AspNetCore.Mvc.RazorPages;

namespace RazorPagesApp.Pages
{
 public class IndexModel : PageModel
 {
 public void OnGet()
 {
 ViewData["Message"] = "Razor Pages on METANIT.COM";
 }
 }
}

```


В данном случае в словаре ViewData определяется элемент с ключом "Message", значением которого является строка "Razor Pages on METANIT.COM".
На странице Index.cshtml получим это значение:

```

@page

@model RazorPagesApp.Pages.IndexModel

<h2>@ViewData["Message"]</h2>

```


Здесь получаем из словаря ViewData элемент с ключом "Message" и выводим его в заголовке.
![Передача данных через ViewData на страницу Razor Pages в ASP.NET Core и C#](https://metanit.com./pics/2.46.png)


Подобным образом через ViewData можно передавать и более комплексные данные, только стоит учитывать, что в этом случае может потрбеоваться приведение типов.
Например, определим в коде модели передачу списка строк:

```

using Microsoft.AspNetCore.Mvc.RazorPages;

namespace RazorPagesApp.Pages
{
 public class IndexModel : PageModel
 {
 public void OnGet()
 {
 ViewData["Message"] = "Список пользователей";
 ViewData["People"] = new List<string> { "Tom", "Sam", "Bob" };
 }
 }
}

```


На странице Index.cshtml выведем данные из списка:

```

@page

@model RazorPagesApp.Pages.IndexModel

<h2>@ViewData["Message"]</h2>
<ul>
 @if(ViewData["People"] is List<string> people)
 {
 foreach(var person in people)
 {
 <li>@person</li>
 }
 }
</ul>

```

![ ViewData в Razor Pages в ASP.NET Core и C#](https://metanit.com./pics/2.47.png)


Как видно, здесь потребовалось преобразование данных. С этой точки зрения использование свойств модели вместо ViewData было бы более предпочтительным.


При этом данные ViewData можно определять непосредственно на самой странице Razor:

```

@page

@{
 ViewData["Message"] = "Razor Pages on METANIT.COM";
}

<h2>@ViewData["Message"]</h2>

```


В конкретно данном случае применение ViewData не имеет большого смысла, посколько можно было бы просто определить переменную, тем не менее в ряде сценариев может потребоваться передать данные
из страницы Razor в другие представления или страницы.


### ViewBag


ViewBag во многом подобен ViewData. Он позволяет динамически определить различные свойства и присвоить им любое значение. Так, мы могли бы переписать предыдущий пример следующим образом::

```

@page

@{
 ViewBag.Message = "Razor Pages on METANIT.COM";
}

<h2>@ViewBag.Message</h2>

```


Стоит отметить, что свойство ViewBag можно использовать только на странице Razor, а в классе модели оно не доступно.


На странице Razor также можно получать все данные, переданные через ViewData, через ViewBag:

```

@page

@{
 ViewData["Message"] = "Razor Pages on METANIT.COM";
}

<h2>@ViewBag.Message</h2>

```












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

**Источник:** [https://metanit.com/sharp/razorpages/2.15.php](https://metanit.com/sharp/razorpages/2.15.php)
