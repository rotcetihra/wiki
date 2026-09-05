# Tag-хелпер пагинации с сортировкой и фильтрацией

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC|Руководство по ASP.NET MVC]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 11. Работа с данными в Entity Framework|Глава 11. Работа с данными в Entity Framework]] / Tag-хелпер пагинации с сортировкой и фильтрацией

[[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 11. Работа с данными в Entity Framework/Объединение сортировки, фильтрации и пагинации|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 11. Работа с данными в Entity Framework|Содержание]]

**Дата написания:** 05.09.2026

## Tag-хелпер пагинации с сортировкой и фильтрацией

Последнее обновление: 12.04.2022




-

-

-














В прошлой теме было рассмотрено создание ссылок для постраничного перехода. Теперь посмотрим, как мы можем заменить эти ссылки на специальный tag-хелпер для постраничной навигации.


Добавим в проект новый класс PageLinkTagHelper:

```

using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.Rendering;
using Microsoft.AspNetCore.Mvc.Routing;
using Microsoft.AspNetCore.Mvc.ViewFeatures;
using Microsoft.AspNetCore.Razor.TagHelpers;
using MvcApp.Models;

namespace MvcApp.TagHelpers
{
 public class PageLinkTagHelper : TagHelper
 {
 private IUrlHelperFactory urlHelperFactory;
 public PageLinkTagHelper(IUrlHelperFactory helperFactory)
 {
 urlHelperFactory = helperFactory;
 }
 [ViewContext]
 [HtmlAttributeNotBound]
 public ViewContext ViewContext { get; set; } = null!;
 public PageViewModel? PageModel { get; set; }
 public string PageAction { get; set; } = "";

 [HtmlAttributeName(DictionaryAttributePrefix = "page-url-")]
 public Dictionary<string, object> PageUrlValues { get; set; } = new();

 public override void Process(TagHelperContext context, TagHelperOutput output)
 {
 if(PageModel == null) throw new Exception("PageModel is not set");
 IUrlHelper urlHelper = urlHelperFactory.GetUrlHelper(ViewContext);
 output.TagName = "div";

 // набор ссылок будет представлять список ul
 TagBuilder tag = new TagBuilder("ul");
 tag.AddCssClass("pagination");

 // формируем три ссылки - на текущую, предыдущую и следующую
 TagBuilder currentItem = CreateTag(PageModel.PageNumber, urlHelper);

 // создаем ссылку на предыдущую страницу, если она есть
 if (PageModel.HasPreviousPage)
 {
 TagBuilder prevItem = CreateTag(PageModel.PageNumber - 1, urlHelper);
 tag.InnerHtml.AppendHtml(prevItem);
 }

 tag.InnerHtml.AppendHtml(currentItem);
 // создаем ссылку на следующую страницу, если она есть
 if (PageModel.HasNextPage)
 {
 TagBuilder nextItem = CreateTag(PageModel.PageNumber + 1, urlHelper);
 tag.InnerHtml.AppendHtml(nextItem);
 }
 output.Content.AppendHtml(tag);
 }

 TagBuilder CreateTag(int pageNumber, IUrlHelper urlHelper)
 {
 TagBuilder item = new TagBuilder("li");
 TagBuilder link = new TagBuilder("a");
 if (pageNumber == PageModel?.PageNumber)
 {
 item.AddCssClass("active");
 }
 else
 {
 PageUrlValues["page"] = pageNumber;
 link.Attributes["href"] = urlHelper.Action(PageAction, PageUrlValues);
 }
 item.AddCssClass("page-item");
 link.AddCssClass("page-link");
 link.InnerHtml.Append(pageNumber.ToString());
 item.InnerHtml.AppendHtml(link);
 return item;
 }
 }
}

```


Ранее уже было рассмотрено создание tag-хелпера для постраничной навигации, и в данном случае основная часть повторяется. Единственным исключением является свойство
PageUrlValues:

```

[HtmlAttributeName(DictionaryAttributePrefix = "page-url-")]
public Dictionary<string, object> PageUrlValues { get; set; } = new();

```


Это свойство представляет словарь `Dictionary<string, object>`, в котором каждой строке будет сопоставлен некоторый объект.


Его отличительной чертой является атрибут `[HtmlAttributeName(DictionaryAttributePrefix = "page-url-")]`. Он указывает, что при применении
хелпера в представлении мы сможем передать ему некоторые значения через атрибуты с префиксом "page-url-". Например:

```

<page-link page-url-action="Index" page-url-number="2"></page-link>

```


В этом случае в словаре PageUrlValues окажутся две пары значений: {"action" : "Index"} и {"number" : 2}. То есть ключи в словаре будут представлять названия атрибутов
без префикса `page-url-`, а их значения - значения в этих атрибутах. Таким образом, мы можем передать в словарь PageUrlValues произвольное количество значений.


Далее все эти значения мы можем использовать, к примеру, для создания навигационных ссылок:

```

PageUrlValues["page"] = pageNumber;
link.Attributes["href"] = urlHelper.Action(PageAction, PageUrlValues);

```


Применим этот хелпер в представлении:

```

@addTagHelper *, Microsoft.AspNetCore.Mvc.TagHelpers
@addTagHelper *, MvcApp

@using MvcApp.Models
@model IndexViewModel

<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" />

<h1>Список пользователей</h1>
<form method="get">
 <label>Имя: </label>
 <input name="name" value="@Model.FilterViewModel.SelectedName" />

 <label>Компания: </label>
 <select name="company" asp-items="Model.FilterViewModel.Companies"></select>

 <input type="submit" value="Фильтр" />
</form>

<table class="table">
 <tr>
 <th>
 <a asp-action="Index"
 asp-route-sortOrder="@(Model.SortViewModel.NameSort)"
 asp-route-name="@(Model.FilterViewModel.SelectedName)"
 asp-route-company="@(Model.FilterViewModel.SelectedCompany)">Имя</a>
 </th>
 <th>
 <a asp-action="Index" asp-route-sortOrder="@(Model.SortViewModel.AgeSort)"
 asp-route-name="@(Model.FilterViewModel.SelectedName)"
 asp-route-company="@(Model.FilterViewModel.SelectedCompany)">Возраст</a>
 </th>
 <th>
 <a asp-action="Index" asp-route-sortOrder="@(Model.SortViewModel.CompanySort)"
 asp-route-name="@(Model.FilterViewModel.SelectedName)"
 asp-route-company="@(Model.FilterViewModel.SelectedCompany)">Компания</a>
 </th>
 </tr>
 @foreach (User u in Model.Users)
 {
 <tr><td>@u.Name</td><td>@u.Age</td><td>@u.Company?.Name</td></tr>
 }
</table>

<page-link page-model="Model.PageViewModel" page-action="Index"
 page-url-name="@(Model.FilterViewModel.SelectedName)"
 page-url-company="@(Model.FilterViewModel.SelectedCompany)"
 page-url-sortorder="@(Model.SortViewModel.Current)"></page-link>

```

![Tag-хелпер для постраничной навигации с сортировкой и фильтрацией в ASP.NET Core MVC и C#](https://metanit.com./pics/11.18.png)











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

**Источник:** [https://metanit.com/sharp/aspnetmvc/11.10.php](https://metanit.com/sharp/aspnetmvc/11.10.php)
