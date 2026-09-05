# Привязка свойств страниц и моделей Razor к параметрам запроса

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по Razor Pages|Руководство по Razor Pages]] / [[Языки программирования/C#/Веб-разработка/Руководство по Razor Pages/Глава 2. Основы Razor Pages|Глава 2. Основы Razor Pages]] / Привязка свойств страниц и моделей Razor к параметрам запроса

[[Языки программирования/C#/Веб-разработка/Руководство по Razor Pages/Глава 2. Основы Razor Pages/POST-запросы и отправка форм|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по Razor Pages/Глава 2. Основы Razor Pages|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по Razor Pages/Глава 2. Основы Razor Pages/Параметры маршрутов|Вперёд]]

**Дата написания:** 05.09.2026

## Привязка свойств страниц и моделей Razor к параметрам запроса

Последнее обновление: 16.04.2022




-

-

-














Для получения отправленных данных мы можем использовать параметры в методах OnGet/OnPost/OnPut/OnDelete и затем передавать их значения свойствам или как-то иначе обрабатывать.
Однако Razor Pages позволяет напрямую установить привязку свойств страницы Razor Pages и ее модели и параметров запроса с помощью атрибута BindProperty, что в ряде случаев может упростить обработку.


Например, у нас есть страница Razor Index.cshtml и код связанной модели IndexModel в файле Index.cshtml.cs:
![OnGet и OnPost в Razor Page в ASP.NET Core и C#](https://metanit.com./pics/2.13.png)


Определим в файле Index.cshtml.cs следующий код:

```

using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;

namespace RazorPagesApp.Pages
{

 [IgnoreAntiforgeryToken]
 public class IndexModel : PageModel
 {
 [BindProperty]
 public string Name { get; set; } = "";

 [BindProperty]
 public int Age { get; set; }

 }
}

```


В модели IndexModel определены два свойства, к которым применяется атрибут BindProperty. Причем в модели нет никаких методов OnGet или OnPost. Тем не менее если
в запросе будут данные с ключами name и age (регистр названий ключей не имеет значения), то эти данные будут автоматически передаваться одноименным свойствам.


Далее на странице Index.cshtml определим форму для ввода данных и элементы для их вывода:

```

@page

@model RazorPagesApp.Pages.IndexModel

<h2>Введите данные</h2>
<form method="post" >
 <p>
 <label>Имя:</label><br />
 <input type="text" name="name" />
 </p>
 <p>
 <label>Возраст:</label><br />
 <input type="number" name="age" />
 </p>
 <input type="submit" value="Отправить" />
</form>
@if(Request.Method == "POST")
{
 <h3>Полученные данные</h3>
 <p>Name: @Model.Name</p>
 <p>Age: @Model.Age</p>
}

```


В данном случае названия полей формы соответствуют именам свойств модели IndexModel, за счет чего с помощью атрибута BindProperty будет происходить автоматическая привязка
![Атрибут BindProperty и привязка свойств к параметрам запроса в Razor Pages ASP.NET Core в C#](https://metanit.com./pics/2.27.png)


При этом можно также обрабатываться запросы в методах OnGet/OnPost, например:

```

using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;

namespace RazorPagesApp.Pages
{

 [IgnoreAntiforgeryToken]
 public class IndexModel : PageModel
 {
 [BindProperty]
 public string Name { get; set; } = "";

 [BindProperty]
 public int Age { get; set; }

 public string Message { get; private set; } = "";
 public void OnGet()
 {
 Message = "Введите данные";
 }
 public void OnPost()
 {
 Message = $"Имя: {Name} Возраст: {Age}";
 }

 }
}

```


### Привязка к сложным объектам


Выше каждое из отправляемых из формы значений связывалось с определенным свойством. Однако можно также определить общую модель, которая будет объединять все
эти значения. Например, изменим модель IndexModel следующим образом:

```

using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;

namespace RazorPagesApp.Pages
{

 [IgnoreAntiforgeryToken]
 public class IndexModel : PageModel
 {
 [BindProperty]
 public Person? Person { get; set; }
 }
 public record class Person (string Name, int Age);
}

```


Теперь данные будут связываться с объектом класса Person.


На странице Index.cshtml изменим код вывода полученных значений:

```

@page

@model RazorPagesApp.Pages.IndexModel

<h2>Введите данные</h2>
<form method="post" >
 <p>
 <label>Имя:</label><br />
 <input type="text" name="name" />
 </p>
 <p>
 <label>Возраст:</label><br />
 <input type="number" name="age" />
 </p>
 <input type="submit" value="Отправить" />
</form>
@if(Request.Method == "POST")
{
 <h3>Полученные данные</h3>
 <p>Name: @Model.Person?.Name</p>
 <p>Age: @Model.Person?.Age</p>
}

```


### Получение данных из GET-запросов


По умолчанию атрибут BindProperty не поддерживает привязку свойств к значениям из GET-запрос. Для добавления этого типа запросов у атрибута
для свойства SupportGet необходимо установить значение true:

```

using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;

namespace RazorPagesApp.Pages
{

 [IgnoreAntiforgeryToken]
 public class IndexModel : PageModel
 {
 [BindProperty(SupportsGet = true)]
 public string? Name { get; set; }
 }
}

```


На странице Index.cshtml выведем полученное значение:

```

@page

@model RazorPagesApp.Pages.IndexModel

<h2>Name: @Model.Name</h2>

```

![Атрибут BindProperty и get-запросы в Razor Pages ASP.NET Core в C#](https://metanit.com./pics/2.28.png)


### Переопределение названий параметров


Выше свойства модели и параметры запросы связывались по имени. Однако мы можем переопределить имя параметра запроса с помощью свойства Name
атрибута BindProperty:

```

using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;

namespace RazorPagesApp.Pages
{
 public class IndexModel : PageModel
 {
 [BindProperty(SupportsGet = true, Name = "id")]
 public string? Name { get; set; }
 }
}

```


В данном случае свойству Name будет передаваться значение параметра "id":
![Переопределение атрибута BindProperty и привязка свойств и параметров запроса в Razor Pages ASP.NET Core в C#](https://metanit.com./pics/2.29.png)











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

**Источник:** [https://metanit.com/sharp/razorpages/2.7.php](https://metanit.com/sharp/razorpages/2.7.php)
