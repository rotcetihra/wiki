# Tag-хелперы валидации и стилизация ошибок

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC|Руководство по ASP.NET MVC]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 9. Метаданные и валидация модели|Глава 9. Метаданные и валидация модели]] / Tag-хелперы валидации и стилизация ошибок

[[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 9. Метаданные и валидация модели/Атрибуты валидации|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 9. Метаданные и валидация модели|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 9. Метаданные и валидация модели/Создание атрибута валидации. Самовалидация модели|Вперёд]]

**Дата написания:** 05.09.2026

## Tag-хелперы валидации и стилизация ошибок

Последнее обновление: 08.04.2022




-

-

-














Для определения полей для вывода ошибок валидации применяются специальные хелперы. Рассмотрим их применение на примере следующей модели Person:

```

using System.ComponentModel.DataAnnotations;

namespace MvcApp.Models
{
 public class Person
 {
 [Required(ErrorMessage = "Не указано имя")]
 public string? Name { get; set; }


 [Required(ErrorMessage = "Не указан электронный адрес")]
 public string? Email { get; set; }

 [Required(ErrorMessage = "Не указан возраст")]
 [Range(1, 100)]
 public int Age { get; set; }
 }
}

```


### ValidationMessageTagHelper


Для валидации на стороне клиента применяется класс ValidationMessageTagHelper. Данный tag-хелпер определяется с помощью применения
к элементу `<span >` атрибута asp-validation-for:

```

<span asp-validation-for="имя_свойства_модели"></span>

```


Атрибут `asp-validation-for` в качестве значения принимает название свойства модели, для которого будет выводиться сообщение об ошибке валидации.
Соответственно для каждого поля ввода мы можем предусмотреть подобный хелпер для вывода ошибок валидации. Например, форма для ввода значений для выше определенной модели Person:

```

@model MvcApp.Models.Person
@addTagHelper *, Microsoft.AspNetCore.Mvc.TagHelpers

<form method="post">
 <div>
 <p>
 <label asp-for="Name">Name</label><br />
 <input type="text" asp-for="Name" />
 <span asp-validation-for="Name" />
 </p>
 <p>
 <label asp-for="Email">Email</label><br />
 <input type="text" asp-for="Email" />
 <span asp-validation-for="Email" />
 </p>
 <p>
 <label asp-for="Age">Age</label><br />
 <input asp-for="Age" />
 <span asp-validation-for="Age" />
 </p>
 <p>
 <input type="submit" value="Send" />
 </p>
 </div>
</form>

<script src="https://ajax.aspnetcdn.com/ajax/jQuery/jquery-3.5.1.min.js"></script>
<script src="https://ajax.aspnetcdn.com/ajax/jquery.validate/1.17.0/jquery.validate.min.js"></script>
<script src="https://ajax.aspnetcdn.com/ajax/jquery.validation.unobtrusive/3.2.10/jquery.validate.unobtrusive.min.js"></script>

```


Например, возьмем tag-хелпер, который применяется для вывода ошибок для свойства Name:

```
<span asp-validation-for="Name" />
```


Данный элемент span будет генерировать следующую разметку:

```

<span class="field-validation-valid" data-valmsg-for="Name" data-valmsg-replace="true"></span>

```


### ValidationSummaryTagHelper


Другой tag-хелпера - ValidationSummaryTagHelper применяется для отображения сводки ошибок валидации. Он применяется к элементу `<div>`
в виде атрибута asp-validation-summary:

```
<div asp-validation-summary="ModelOnly"/>
```


В качестве значения атрибут `asp-validation-summary` принимает одно из значений перечисления ValidationSummary:


-

None: ошибки валидации не отображаются

-

ModelOnly: отображаются только ошибка валидации уровня модели, ошибки валидации для отдельных свойств не отображаются

-

All: отображаются все ошибки валидации


На выходе тег-хелпер будет генерировать следующий код:

```

<div class="validation-summary-valid" data-valmsg-summary="true">
 <ul>
 <li style="display:none"></li>
 </ul>
</div>

```


При возникновении ошибок в список `<ul>` добавляются все сообщения об ошибках.


Теперь применим ValidationSummaryTagHelper и для этого для модели Person определим следующее представление:

```

@model MvcApp.Models.Person
@addTagHelper *, Microsoft.AspNetCore.Mvc.TagHelpers

<form method="post">
 <div asp-validation-summary="All"></div>
 <p>
 <label asp-for="Name">Name</label><br />
 <input type="text" asp-for="Name" />
 <span asp-validation-for="Name" />
 </p>
 <p>
 <label asp-for="Email">Email</label><br />
 <input type="text" asp-for="Email" />
 <span asp-validation-for="Email" />
 </p>
 <p>
 <label asp-for="Age">Age</label><br />
 <input asp-for="Age" />
 <span asp-validation-for="Age" />
 </p>
 <p>
 <input type="submit" value="Send" />
 </p>
</form>

<script src="https://ajax.aspnetcdn.com/ajax/jQuery/jquery-3.5.1.min.js"></script>
<script src="https://ajax.aspnetcdn.com/ajax/jquery.validate/1.17.0/jquery.validate.min.js"></script>
<script src="https://ajax.aspnetcdn.com/ajax/jquery.validation.unobtrusive/3.2.10/jquery.validate.unobtrusive.min.js"></script>

```


И в случае некорректного ввода в верху формы отобразятся ошибки валидации:
![хелперы валидации ValidationMessageTagHelper и ValidationSummaryTagHelper в ASP.NET Core MVC и C#](https://metanit.com./pics/9.12.png)


При подобном определении формы сообщения об ошибках отображаются как поверх формы ввода, так и ряд с соответствующими полями ввода. Может показаться, что в таком дополнительном
выводе ошибок свойств нет смысла - для этого ведь уже есть вывод ошибок возле каждого поля ввода. Тем не менее это может быть полезным, когда какая-то часть валидации производится на сервере.


Например, в контроллере в методе, который получает данную форму, добавим дополнительную проверку данных:

```

using Microsoft.AspNetCore.Mvc;
using MvcApp.Models; // пространство имен класса Person

namespace MvcApp.Controllers
{
 public class HomeController : Controller
 {
 public IActionResult Create() => View();

 [HttpPost]
 public IActionResult Create(Person person)
 {
 if (person.Name == "admin")
 ModelState.AddModelError("Name", "admin - запрещенное имя.");
 if (ModelState.IsValid)
 return Content($"{person.Name} - {person.Age}");
 return View(person);
 }
 }
}

```


Здесь в post-методе Create, если свойству Name передана строка "admin", то для этого свойства добавляется дополнительная ошибка валидации. То есть с точки зрения атрибутов валидации
для свойства Name строка "admin" - корректное значение, а форма благополучно отправится методу контроллера. Но благодаря проверке на сервере подобное значение все равно не пройдет валидацию, :
![валидация свойств модели и вывод ошибок с помощью ValidationSummaryTagHelper в ASP.NET Core MVC и C#](https://metanit.com./pics/9.14.png)


### Ошибки уровня модели


Теперь изменим определение хелпера, чтобы он отображал только ошибки уровня модели:

```

@model MvcApp.Models.Person
@addTagHelper *, Microsoft.AspNetCore.Mvc.TagHelpers

<form method="post">
 <div asp-validation-summary="ModelOnly"></div>
 <p>
 <label asp-for="Name">Name</label><br />
 <input type="text" asp-for="Name" />
 <span asp-validation-for="Name" />
 </p>
 <p>
 <label asp-for="Email">Email</label><br />
 <input type="text" asp-for="Email" />
 <span asp-validation-for="Email" />
 </p>
 <p>
 <label asp-for="Age">Age</label><br />
 <input asp-for="Age" />
 <span asp-validation-for="Age" />
 </p>
 <p>
 <input type="submit" value="Send" />
 </p>
</form>

<script src="https://ajax.aspnetcdn.com/ajax/jQuery/jquery-3.5.1.min.js"></script>
<script src="https://ajax.aspnetcdn.com/ajax/jquery.validate/1.17.0/jquery.validate.min.js"></script>
<script src="https://ajax.aspnetcdn.com/ajax/jquery.validation.unobtrusive/3.2.10/jquery.validate.unobtrusive.min.js"></script>

```


А в контроллере в методе, который получает данную форму, добавим дополнительную проверку данных:

```

using Microsoft.AspNetCore.Mvc;
using MvcApp.Models; // пространство имен класса Person

namespace MvcApp.Controllers
{
 public class HomeController : Controller
 {
 public IActionResult Create() => View();

 [HttpPost]
 public IActionResult Create(Person person)
 {
 if (person.Name == person.Email)
 ModelState.AddModelError("", "Имя и электронный адрес не должны совпадать.");
 if (ModelState.IsValid)
 return Content($"{person.Name} - {person.Age}");
 return View(person);
 }
 }
}

```


Здесь в post-методе Create, если свойства Name и Email модели Person имеют одинаковые значение, то добавляется ошибка валидации:

```
ModelState.AddModelError("", "Имя и электронный адрес не должны совпадать.");
```


Пустая строка, передаваемая первому параметру метода, указывает, что данная ошибка относится ко всей модели в целом, а не к отдельному свойству. То есть даже
если пользователь ввел в форму корректные значения для отдельных свойств и форма была успешна отправлена, но при этом значения свойств Name и Email совпадают, то модель в итоге
не пройдет проверку и возвратиться пользователю.
![валидация модели и вывод ошибок с помощью ValidationSummaryTagHelper в ASP.NET Core MVC и C#](https://metanit.com./pics/9.13.png)


### Стилизация сообщений об ошибках


Когда происходит валидация, то при отображении ошибок соответствующим полям присваиваются определенные классы css:


-

для блока ошибок, который генерируется хелпером ValidationSummaryTagHelper, при наличии ошибок устанавливается класс validation-summary-errors. Если
ошибок нет, то данный блок не отображается

-

для элемента `<span>`, который отображает ошибку для каждого отдельного поля и который генерируется хелпером ValidationTagHelper,
при наличии ошибок устанавливается класс field-validation-error. Если
ошибок нет, то данный элемент имеет класс field-validation-valid

-

для поля ввода при наличии ошибок устанавливается класс input-validation-error. Если
ошибок нет, то устанавливается класс valid


Используя эти классы, мы можем настроить отображение сообщений. Например, изменим представление следующим образом:

```

@model MvcApp.Models.Person
@addTagHelper *, Microsoft.AspNetCore.Mvc.TagHelpers

<style>
.field-validation-error {
 color: #b94a48;
}

input.input-validation-error {
 border: 1px solid #b94a48;
}
input.valid {
 border: 1px solid #16a085;
}

.validation-summary-errors {
 color: #b94a48;
}
</style>
<form method="post">
 <div asp-validation-summary="ModelOnly"></div>
 <p>
 <label asp-for="Name">Name</label><br />
 <input type="text" asp-for="Name" />
 <span asp-validation-for="Name" />
 </p>
 <p>
 <label asp-for="Email">Email</label><br />
 <input type="text" asp-for="Email" />
 <span asp-validation-for="Email" />
 </p>
 <p>
 <label asp-for="Age">Age</label><br />
 <input asp-for="Age" />
 <span asp-validation-for="Age" />
 </p>
 <p>
 <input type="submit" value="Send" />
 </p>
</form>

<script src="https://ajax.aspnetcdn.com/ajax/jQuery/jquery-3.5.1.min.js"></script>
<script src="https://ajax.aspnetcdn.com/ajax/jquery.validate/1.17.0/jquery.validate.min.js"></script>
<script src="https://ajax.aspnetcdn.com/ajax/jquery.validation.unobtrusive/3.2.10/jquery.validate.unobtrusive.min.js"></script>

```

![Стилизация ошибок валидации в ASP.NET Core MVC и C#](https://metanit.com./pics/9.15.png)











- Глава 1. Введение в ASP.NET Core MVC


 - [Фреймворк ASP.NET Core MVC](//metanit.com/sharp/aspnetmvc/1.1.php)

 - [Первый проект на ASP.NET Core MVC с .NET CLI](//metanit.com/sharp/aspnetmvc/1.4.php)

 - [Первый проект на ASP.NET Core MVC в Visual Studio](//metanit.com/sharp/aspnetmvc/1.2.php)

 - [Добавление MVC в пустой проект](//metanit.com/sharp/aspnetmvc/1.3.php)



- Глава 2. Контроллеры


 - [Контроллеры и их действия](//metanit.com/sharp/aspnetmvc/2.1.php)

 - [Контекст контроллера](//metanit.com/sharp/aspnetmvc/2.2.php)

 - [Передача данных в контроллер через строку запроса](//metanit.com/sharp/aspnetmvc/2.3.php)

 - [Передача данных в контроллер через формы](//metanit.com/sharp/aspnetmvc/2.4.php)

 - [Результаты действий](//metanit.com/sharp/aspnetmvc/2.5.php)

 - [ContentResult и JsonResult](//metanit.com/sharp/aspnetmvc/2.6.php)

 - [Переадресация](//metanit.com/sharp/aspnetmvc/2.7.php)

 - [Отправка статусных кодов](//metanit.com/sharp/aspnetmvc/2.8.php)

 - [Отправка файлов](//metanit.com/sharp/aspnetmvc/2.9.php)

 - [Передача зависимостей в контроллер](//metanit.com/sharp/aspnetmvc/2.10.php)

 - [Переопределение контроллеров](//metanit.com/sharp/aspnetmvc/2.11.php)



- Глава 3. Представления


 - [Введение в представления](//metanit.com/sharp/aspnetmvc/3.1.php)

 - [Движок представлений Razor](//metanit.com/sharp/aspnetmvc/3.2.php)

 - [Передача данных в представление](//metanit.com/sharp/aspnetmvc/3.3.php)

 - [Мастер-страницы](//metanit.com/sharp/aspnetmvc/3.4.php)

 - [Файл _ViewImports.cshtml](//metanit.com/sharp/aspnetmvc/3.5.php)

 - [Частичные представления](//metanit.com/sharp/aspnetmvc/3.6.php)

 - [Внедрение зависимостей в представления](//metanit.com/sharp/aspnetmvc/3.7.php)

 - [Работа с формами](//metanit.com/sharp/aspnetmvc/3.8.php)

 - [Создание движка представлений](//metanit.com/sharp/aspnetmvc/3.9.php)



- Глава 4. Маршрутизация


 - [Добавление маршрутизации](//metanit.com/sharp/aspnetmvc/4.1.php)

 - [Определение маршрутов](//metanit.com/sharp/aspnetmvc/4.2.php)

 - [Атрибуты маршрутизации](//metanit.com/sharp/aspnetmvc/4.3.php)

 - [Области](//metanit.com/sharp/aspnetmvc/4.4.php)



- Глава 5. Модели


 - [Модели в ASP.NET Core MVC](//metanit.com/sharp/aspnetmvc/5.1.php)

 - [Введение в определение и применение моделей](//metanit.com/sharp/aspnetmvc/5.2.php)

 - [Привязка модели](//metanit.com/sharp/aspnetmvc/5.3.php)

 - [Управление привязкой](//metanit.com/sharp/aspnetmvc/5.4.php)

 - [Создание привязчика модели](//metanit.com/sharp/aspnetmvc/5.5.php)



- Глава 6. HTML-хелперы


 - [Создание HTML-хелперов](//metanit.com/sharp/aspnetmvc/6.1.php)

 - [HTML-хелперы элементов форм](//metanit.com/sharp/aspnetmvc/6.2.php)

 - [Строго типизированные хелперы](//metanit.com/sharp/aspnetmvc/6.3.php)

 - [Шаблонные хелперы](//metanit.com/sharp/aspnetmvc/6.4.php)

 - [Генерация ссылок](//metanit.com/sharp/aspnetmvc/6.5.php)

 - [URL-хелперы](//metanit.com/sharp/aspnetmvc/6.6.php)



- Глава 7. Tag-хелперы


 - [Введение в tag-хелперы](//metanit.com/sharp/aspnetmvc/7.1.php)

 - [AnchorTagHelper. Создание ссылок](//metanit.com/sharp/aspnetmvc/7.2.php)

 - [LinkTagHelper и ScriptTagHelper](//metanit.com/sharp/aspnetmvc/7.3.php)

 - [Tag-хелперы форм](//metanit.com/sharp/aspnetmvc/7.4.php)

 - [EnvironmentTagHelper](//metanit.com/sharp/aspnetmvc/7.5.php)

 - [CacheTagHelper](//metanit.com/sharp/aspnetmvc/7.6.php)

 - [Создание tag-хелперов](//metanit.com/sharp/aspnetmvc/7.7.php)

 - [Управление выводом tag-хелпера](//metanit.com/sharp/aspnetmvc/7.8.php)

 - [Контекст хелпера и получение зависимостей](//metanit.com/sharp/aspnetmvc/7.9.php)

 - [Атрибут HtmlTargetElement](//metanit.com/sharp/aspnetmvc/7.10.php)

 - [Tag-хелперы и сложные объекты и коллекции](//metanit.com/sharp/aspnetmvc/7.11.php)



- Глава 8. View Component


 - [Определение компонента представлений](//metanit.com/sharp/aspnetmvc/8.1.php)

 - [Передача данных в View Component](//metanit.com/sharp/aspnetmvc/8.2.php)

 - [Генерация контента в View Component](//metanit.com/sharp/aspnetmvc/8.3.php)

 - [ViewComponentResult и представления](//metanit.com/sharp/aspnetmvc/8.4.php)

 - [ViewComponentContext](//metanit.com/sharp/aspnetmvc/8.5.php)



- Глава 9. Метаданные и валидация модели


 - [Валидация модели на стороне сервера](//metanit.com/sharp/aspnetmvc/9.1.php)

 - [Валидация на стороне клиента](//metanit.com/sharp/aspnetmvc/9.2.php)

 - [Атрибуты валидации](//metanit.com/sharp/aspnetmvc/9.3.php)

 - [Tag-хелперы валидации и стилизация ошибок](//metanit.com/sharp/aspnetmvc/9.4.php)

 - [Создание атрибута валидации. Самовалидация модели](//metanit.com/sharp/aspnetmvc/9.5.php)

 - [Аннотации данных](//metanit.com/sharp/aspnetmvc/9.6.php)



- Глава 10. Фильтры


 - [Введение в фильтры](//metanit.com/sharp/aspnetmvc/10.1.php)

 - [Область действия фильтров](//metanit.com/sharp/aspnetmvc/10.2.php)

 - [Передача параметров в фильтры и установка зависимостей](//metanit.com/sharp/aspnetmvc/10.3.php)

 - [Фильтры ресурсов](//metanit.com/sharp/aspnetmvc/10.4.php)

 - [Фильтры действий](//metanit.com/sharp/aspnetmvc/10.5.php)

 - [Фильтры результатов](//metanit.com/sharp/aspnetmvc/10.6.php)

 - [Фильтры исключений](//metanit.com/sharp/aspnetmvc/10.7.php)



- Глава 11. Работа с данными в Entity Framework


 - [Подключение Entity Framework Core](//metanit.com/sharp/aspnetmvc/11.1.php)

 - [Добавление и вывод данных](//metanit.com/sharp/aspnetmvc/11.2.php)

 - [Редактирование и удаление данных](//metanit.com/sharp/aspnetmvc/11.3.php)

 - [Сортировка](//metanit.com/sharp/aspnetmvc/11.4.php)

 - [Создание tag-хелпера сортировки](//metanit.com/sharp/aspnetmvc/11.5.php)

 - [Фильтрация](//metanit.com/sharp/aspnetmvc/11.6.php)

 - [Постраничная навигация](//metanit.com/sharp/aspnetmvc/11.7.php)

 - [Tag-хелпер для постраничной навигации](//metanit.com/sharp/aspnetmvc/11.8.php)

 - [Объединение сортировки, фильтрации и пагинации](//metanit.com/sharp/aspnetmvc/11.9.php)

 - [Tag-хелпер пагинации с сортировкой и фильтрацией](//metanit.com/sharp/aspnetmvc/11.10.php)










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

**Источник:** [https://metanit.com/sharp/aspnetmvc/9.4.php](https://metanit.com/sharp/aspnetmvc/9.4.php)
