# Tag-хелпер для постраничной навигации

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC|Руководство по ASP.NET MVC]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 11. Работа с данными в Entity Framework|Глава 11. Работа с данными в Entity Framework]] / Tag-хелпер для постраничной навигации

[[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 11. Работа с данными в Entity Framework/Постраничная навигация|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 11. Работа с данными в Entity Framework|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 11. Работа с данными в Entity Framework/Объединение сортировки, фильтрации и пагинации|Вперёд]]

**Дата написания:** 05.09.2026

## Tag-хелпер для постраничной навигации

Последнее обновление: 12.04.2022




-

-

-














В прошлой теме был рассмотрен постраничный вывод. Для создания ссылок применялись встроенные хелперы:

```

@if (Model.PageViewModel.HasPreviousPage)
{
 <a asp-action="Index"
 asp-route-page="@(Model.PageViewModel.PageNumber - 1)" class="glyphicon glyphicon-chevron-left">
 Назад
 </a>
}
@if (Model.PageViewModel.HasNextPage)
{
 <a asp-action="Index"
 asp-route-page="@(Model.PageViewModel.PageNumber + 1)" class="glyphicon glyphicon-chevron-right">
 Вперед
 </a>
}

```


Но нередко для создания постраничной навигации создаются какие-то специальные панельки, где можно увидеть ссылки с номерами страниц, по которым
можно перейти к нужным страницы, еще какие-то элементы. Все эти элементы нередко должным образом стилизованы.


Нередко элементы навигации - ссылки размещаются в виде ненумерованного списка. В данном случае наша задача - создать компонент навигации наподобие следующего:

```

<ul class="pagination">
 <li><a href="/?page=1">1</a></li>
 <li class="active"><a>2</a></li>
 <li><a href="/?page=3">3</a></li>
</ul>

```


Для стилизации применяется класс bootstrap - pagination. Перед активной ссылкой располагаются ссылки на предыдущую и следующую страницу.


Вместо того, чтобы определять все необходимые ссылки и элементы напрямую в представлении, удобнее создать специальный tag-хелпер.
Поэтому возьмем проект из прошлой темы и добавим в него новую папку TagHelpers, а в эту папку добавим новый класс PageLinkTagHelper:

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
 IUrlHelperFactory urlHelperFactory;
 public PageLinkTagHelper(IUrlHelperFactory helperFactory)
 {
 urlHelperFactory = helperFactory;
 }
 [ViewContext]
 [HtmlAttributeNotBound]
 public ViewContext ViewContext { get; set; } = null!;
 public PageViewModel? PageModel { get; set; }
 public string PageAction { get; set; } = "";

 public override void Process(TagHelperContext context, TagHelperOutput output)
 {
 if (PageModel == null) throw new Exception("PageModel is not set");
 IUrlHelper urlHelper = urlHelperFactory.GetUrlHelper(ViewContext);
 output.TagName = "div";

 // набор ссылок будет представлять список ul
 TagBuilder tag = new TagBuilder("ul");
 tag.AddCssClass("pagination");

 // формируем три ссылки - на текущую, предыдущую и следующую
 TagBuilder currentItem = CreateTag(urlHelper, PageModel.PageNumber);

 // создаем ссылку на предыдущую страницу, если она есть
 if (PageModel.HasPreviousPage)
 {
 TagBuilder prevItem = CreateTag(urlHelper, PageModel.PageNumber - 1);
 tag.InnerHtml.AppendHtml(prevItem);
 }

 tag.InnerHtml.AppendHtml(currentItem);
 // создаем ссылку на следующую страницу, если она есть
 if (PageModel.HasNextPage)
 {
 TagBuilder nextItem = CreateTag(urlHelper, PageModel.PageNumber + 1);
 tag.InnerHtml.AppendHtml(nextItem);
 }
 output.Content.AppendHtml(tag);
 }

 TagBuilder CreateTag(IUrlHelper urlHelper, int pageNumber = 1)
 {
 TagBuilder item = new TagBuilder("li");
 TagBuilder link = new TagBuilder("a");
 if (pageNumber == PageModel?.PageNumber)
 {
 item.AddCssClass("active");
 }
 else
 {
 link.Attributes["href"] = urlHelper.Action(PageAction, new { page = pageNumber });
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


Фреймворк MVC предоставляет ряд сервисов, и один из них - IUrlHelperFactory, который используется для создания ссылки и который мы можем получить в конструкторе.


Всю информацию о пагинации мы получаем через свойство `PageModel`. Свойство `PageAction` указывает на метод контроллера, на который будет создаваться
ссылка.


Для создания ссылки используется объект IUrlHelper, а для его получения нам нужен контекст представления, в котором вызывается tag-хелпер. Получить контекст представления
мы можем через внедрение зависимости через атрибуты. В частности, чтобы получить контекст представления над свойством ставится атрибут ViewContext:

```

[ViewContext]
[HtmlAttributeNotBound]
public ViewContext ViewContext { get; set; } = null!;

```


Чтобы избежать привязки к атрибутам тега, к свойству также применяется атрибут `HtmlAttributeNotBound`.


В методе Process вначале получаем объект IUrlHelper для создания ссылки:

```

IUrlHelper urlHelper = urlHelperFactory.GetUrlHelper(ViewContext);

```


Далее создаем html-элемент ul. Затем нам надо создать максимум три ссылки, если позволяет количество страниц. Так как каждый элемент
списка ul создается одним и тем же способом, то весь механизм создания элемента списка с ссылкой вынесен в отдельный метод `CreateTag()`.


Для стилизации ссылок применяются классы pagination, page-item и page-link фреймворка bootstrap, который далее подключим в представлении.


Применим этот хелпер в представлении:

```

@using MvcApp.Models
@model IndexViewModel

@*подключаем все tag-хелперы*@
@addTagHelper *, MvcApp

<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" />

<h1>Список пользователей</h1>
<table class="table">
 <tr><th>Имя</th><th>Возраст</th><th>Компания</th></tr>
 @foreach (User u in Model.Users)
 {
 <tr><td>@u.Name</td><td>@u.Age</td><td>@u.Company.Name</td></tr>
 }
</table>
<page-link page-model="Model.PageViewModel" page-action="Index"></page-link>

```


Так как название хелпера состоит из нескольких частей: PageLinkTagHelper, то при использовании все эти части разделяются дефисом
(суффикс TagHelper отбрасывается): `page-link`. То же самое касается и свойств хелпера. Так, чтобы передать значение для свойства PageModel,
нам надо использовать атрибут `page-model`.


Код контроллера остается тем же, что и в прошлой теме:

```

using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using MvcApp.Models;

namespace MvcApp.Controllers
{
 public class HomeController : Controller
 {
 UsersContext db;
 public HomeController(UsersContext context)
 {
 db = context;
 // добавляем начальные данные
 if (!db.Companies.Any())
 {
 Company oracle = new Company { Name = "Oracle" };
 Company google = new Company { Name = "Google" };
 Company microsoft = new Company { Name = "Microsoft" };
 Company apple = new Company { Name = "Apple" };

 User user1 = new User { Name = "Олег Васильев", Company = oracle, Age = 26 };
 User user2 = new User { Name = "Александр Овсов", Company = oracle, Age = 24 };
 User user3 = new User { Name = "Алексей Петров", Company = microsoft, Age = 25 };
 User user4 = new User { Name = "Иван Иванов", Company = microsoft, Age = 26 };
 User user5 = new User { Name = "Петр Андреев", Company = microsoft, Age = 23 };
 User user6 = new User { Name = "Василий Иванов", Company = google, Age = 23 };
 User user7 = new User { Name = "Олег Кузнецов", Company = google, Age = 25 };
 User user8 = new User { Name = "Андрей Петров", Company = apple, Age = 24 };

 db.Companies.AddRange(oracle, microsoft, google, apple);
 db.Users.AddRange(user1, user2, user3, user4, user5, user6, user7, user8);
 db.SaveChanges();
 }
 }
 public async Task<IActionResult> Index(int page = 1)
 {
 int pageSize = 3;
 IQueryable<User> source = db.Users.Include(x => x.Company);
 var count = await source.CountAsync();
 var items = await source.Skip((page - 1) * pageSize).Take(pageSize).ToListAsync();

 PageViewModel pageViewModel = new PageViewModel(count, page, pageSize);
 IndexViewModel viewModel = new IndexViewModel(items, pageViewModel);
 return View(viewModel);
 }
 }
}

```


Итоговый проект будет выглядеть следующим образом:
![Pagination in ASP.NET Core MVC and C#](https://metanit.com./pics/11.14.png)


И при запуске проекта мы увидим набор стилизованных ссылок, по котором сможем перемещаться по страницам:
![Постраничная навигация в ASP.NET Core MVC и C#](https://metanit.com./pics/11.15.png)











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

**Источник:** [https://metanit.com/sharp/aspnetmvc/11.8.php](https://metanit.com/sharp/aspnetmvc/11.8.php)
