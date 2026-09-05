# Модель страницы Razor

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по Razor Pages|Руководство по Razor Pages]] / [[Языки программирования/C#/Веб-разработка/Руководство по Razor Pages/Глава 2. Основы Razor Pages|Глава 2. Основы Razor Pages]] / Модель страницы Razor

[[Языки программирования/C#/Веб-разработка/Руководство по Razor Pages/Глава 2. Основы Razor Pages/Синтаксис Razor|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по Razor Pages/Глава 2. Основы Razor Pages|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по Razor Pages/Глава 2. Основы Razor Pages/Обработка запросов. Контекст страницы Razor|Вперёд]]

**Дата написания:** 05.09.2026

## Модель страницы Razor

Последнее обновление: 14.04.2022




-

-

-














Вместе со страницей Razor в проект добавляется файл связанного кода на языке C#. Этот код определяется в виде класса, который по умолчанию называется по имени
страницы плюс суффикс "Model" (например, для страницы Index - класс IndexModel) и который помещается в файл с именем
[файл_страницы_razor].cs.
![Model in Razor Page в ASP.NET Core и C#](https://metanit.com./pics/2.11.png)


Например, при добавлении страницы Index.cshtml вместе с ней будет добавляться файл Index.cshtml.cs,
который будет содержать определение класса IndexModel

```

using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;

namespace RazorPagesApp.Pages
{
 public class IndexModel : PageModel
 {
 public void OnGet()
 {
 }
 }
}

```


Класс модели страницы Razor должен обязательно наследоваться от абстрактного класса PageModel.
По умолчанию данный класс содержит пустой метод OnGet(), который призван обрабатывать get-запросы. Здесь мы можем определить какие-то данные, какую-то логику, которая будет применяться на
странице razor.


К пример, изменим этот класс следующим образом:

```

using Microsoft.AspNetCore.Mvc.RazorPages;

namespace RazorPagesApp.Pages
{
 public class IndexModel : PageModel
 {
 public string Message { get; }
 public IndexModel()
 {
 Message = "Hello METANIT.COM";
 }
 public string PrintTime() => DateTime.Now.ToShortTimeString();
 }
}

```


В данном случае класс IndexModel определяет свойство Message и метод PrintTime, который возвращает текущее время.


Для подключения класса-модели на страницу Razor применяется директива @model, после которой идет имя класса. Например, изменим определение страницы
Index.cshtml следующим образом:

```

@page

@model RazorPagesApp.Pages.IndexModel
<h2>@Model.Message</h2>

<h3>Time: @Model.PrintTime()</h3>

```


Обратите внимание, что после директивы `@model` указывается полное имя класса с учетом пространства имен.


После подключения модели мы можем обращаться к ее функционалу через свойство Model. Например, с помощью выражения `@Model.Message` мы
можем обратиться к свойству Message в модели.


В итоге при обращении к странице Index и генерации ответа будет использоваться функционал модели IndexModel:
![Подключение модели на странице Razor Page в ASP.NET Core и C#](https://metanit.com./pics/2.12.png)











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

**Источник:** [https://metanit.com/sharp/razorpages/2.3.php](https://metanit.com/sharp/razorpages/2.3.php)
