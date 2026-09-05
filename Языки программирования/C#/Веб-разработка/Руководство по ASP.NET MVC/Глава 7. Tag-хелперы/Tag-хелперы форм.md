# Tag-хелперы форм

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC|Руководство по ASP.NET MVC]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 7. Tag-хелперы|Глава 7. Tag-хелперы]] / Tag-хелперы форм

[[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 7. Tag-хелперы/LinkTagHelper и ScriptTagHelper|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 7. Tag-хелперы|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 7. Tag-хелперы/EnvironmentTagHelper|Вперёд]]

**Дата написания:** 05.09.2026

## Tag-хелперы форм

Последнее обновление: 03.04.2022




-

-

-














Отдельная группа tag-хелперов позволяет создавать формы html и их элементы.


Рассмотрим применение хелперов на примере следующих моделей:

```

public record class Product(string Name, int Price, int CompanyId);

public record class Company(int Id, string Name);

```


И допустим в контроллере определено действие Create для создания нового объекта Product:

```

using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.Rendering;
using MvcApp.Models; // пространство имен Product и Company

namespace MvcApp.Controllers
{
 public class HomeController : Controller
 {
 IEnumerable<Company> companies = new List<Company>
 {
 new Company( 1, "Apple"),
 new Company(2, "Samsung"),
 new Company(3, "Google")
 };
 public IActionResult Create()
 {
 ViewBag.Companies = new SelectList(companies, "Id", "Name");
 return View();
 }

 [HttpPost]
 public string Create(Product product)
 {
 Company company = companies.FirstOrDefault(c => c.Id == product.CompanyId);
 return $"Добавлен новый элемент: {product.Name} ({company?.Name})";
 }
 }
}

```


Ранее для создания форм мы могли бы использовать html-хелперы:

```

@using MvcApp.Models
@model Product

@using (Html.BeginForm())
{
 <p>
 @Html.LabelFor(m => m.Name)
 @Html.EditorFor(m => m.Name)
 </p>
 <p>
 @Html.LabelFor(m => m.Price)
 @Html.EditorFor(m => m.Price)
 </p>
 <p>
 @Html.LabelFor(m => m.CompanyId, "Company")
 @Html.DropDownListFor(m => m.CompanyId, ViewBag.Companies as IEnumerable<SelectListItem>)
 </p>
 <p>
 <input type="submit" value="Save" />
 </p>
}

```


С помощью tag-хелперов мы можем определить следующую аналогичную форму:

```

@model MvcApp.Models.Product

<h2>Добавление телефона</h2>

<form asp-action="Create" asp-controller="Home" asp-antiforgery="true">
 <div>
 <p>
 <label asp-for="Name"></label>
 <input type="text" asp-for="Name" />
 </p>
 <p>
 <label asp-for="Price"></label>
 <input asp-for="Price" />
 </p>
 <p>
 <label asp-for="CompanyId">Company</label>
 <select asp-for="CompanyId" asp-items="ViewBag.Companies"></select>
 </p>
 <p>
 <input type="submit" value="Save" />
 </p>
 </div>
</form>

```

![Form tag-helpers in ASP.NET Core MVC и C#](https://metanit.com./pics/7.6.png)


Тег-хелперы, используемые для создания форм, аналогичны соответствующим элементам html за тем исключением, что они добавляют дополнительную функциональность.
Так, для создания формы используется класс FormTagHelper, представленный тегом form. Этот тег может принимать следующие атрибуты:


-

asp-controller: указывает на контроллер, которому предназначен запрос

-

asp-action: указывает на действие контроллера

-

asp-area: указывает на название области, в которой будет вызываться контроллер для обработки формы

-

asp-antiforgery: если имеет значение true, то для этой формы будет генерироваться antiforgery token

-

asp-route: указывает на название маршрута

-

asp-all-route-data: устанавливает набор значений для параметров

-

asp-route-[название параметра]: определяет значение для определенного параметра

-

asp-page: указывает на страницу RazorPage, которая будет обрабатывать запрос

-

asp-page-handler: указывает на обработчик страницы RazorPage, который применяется для обработки запроса

-

asp-fragment: указывает фрагмент, который добавляется к запрашиваемому адресу после символа #.


Например, форма:

```

<form asp-antiforgery="true" asp-action="Create" asp-controller="Home">

```


В данном случае форма будет отправлять данные методу Create котроллера Home и для формы будет генерироваться antiforgery token.


Все остальные теги, которые используются на формах, имеют один общий атрибут asp-for,
который указывает, для какого свойства модели создается элемент.


### LabelTagHelper


LabelTagHelper использует тег `label` для создания метки:

```

<label asp-for="Name"></label>

```


### InputTagHelper


InputTagHelper создает поле ввода:

```

<input asp-for="Name" />

```


### TextAreaTagHelper


TextAreaTagHelper используется для создания многострочного текстового поля textarea. Данный хелпер применяет только атрибут
`asp-for`:

```

<textarea asp-for="Name"></textarea>

```


### SelectTagHelper


SelectTagHelper создает элемент списка:

```

<select asp-for="CompanyId" asp-items="ViewBag.Companies"></select>

```


Атрибут asp-items указывает на объект `IEnumerable<SelectListItem>`,
который будет использоваться для наполнения списка.


При необходимости мы можем указать элемент, который будет отображаться по умолчанию:

```

<select asp-for="CompanyId" asp-items="ViewBag.Companies">
 <option selected="selected" disabled="disabled">Выберите компанию</option>
</select>

```


### Работа с enum


Теперь рассмотрим, как привязать объект select к перечислению. Допустим, у нас есть следующий тип enum:

```

using System.ComponentModel.DataAnnotations;

public enum DayTime
{
 [Display(Name ="Утро")]
 Morning,
 [Display(Name = "День")]
 Afternoon,
 [Display(Name = "Вечер")]
 Evening,
 [Display(Name = "Ночь")]
 Night
}
public class DayTimeViewModel
{
 public DayTime Period { get; set; }
}

```


Для работы в представлении определена модель `DayTimeViewModel`, которая будет хранить выбранное значение DayTime.


В контроллере определим пару методов, для отправки представления и получения выбранного значения:

```

public IActionResult Index() => View();

[HttpPost]
public string Index(DayTimeViewModel model) => model.Period.ToString();

```


И определим представление Index.cshtml:

```

@using MvcApp.Models
@model DayTimeViewModel

<form method="post">
 <div>
 <div>
 <label asp-for="Period">Время суток</label>
 <select asp-for="Period" asp-items="Html.GetEnumSelectList<DayTime>()"></select>
 </div>
 <div>
 <input type="submit" value="Save" />
 </div>
 </div>
</form>

```


Для наполнения списка мы можем применить статический метод GetEnumSelectList<TEnum>() класса HtmlHelper.


В итоге получится выпадающий список со значениями из перечисления:
![список enum в представлении ASP.NET Core MVC и C#](https://metanit.com./pics/7.7.png)


В качестве альтернативы можно создавать список с помощью конструктора SelectList:

```

<div>
 <label asp-for="Period">Время суток</label>
 <select asp-for="Period" asp-items="@new SelectList(Enum.GetNames(typeof(DayTime)))"></select>
</div>

```












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

**Источник:** [https://metanit.com/sharp/aspnetmvc/7.4.php](https://metanit.com/sharp/aspnetmvc/7.4.php)
