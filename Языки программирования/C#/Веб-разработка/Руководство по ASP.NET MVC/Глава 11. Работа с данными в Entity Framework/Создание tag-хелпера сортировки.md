# Создание tag-хелпера сортировки

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC|Руководство по ASP.NET MVC]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 11. Работа с данными в Entity Framework|Глава 11. Работа с данными в Entity Framework]] / Создание tag-хелпера сортировки

[[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 11. Работа с данными в Entity Framework/Сортировка|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 11. Работа с данными в Entity Framework|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 11. Работа с данными в Entity Framework/Фильтрация|Вперёд]]

**Дата написания:** 05.09.2026

## Создание tag-хелпера сортировки

Последнее обновление: 11.04.2022




-

-

-














Продолжим работу с проектом, который был создан в прошлой теме, где у нас были модели User и Company:

```

public class User
{
 public int Id { get; set; }
 public string? Name { get; set; }
 public int Age { get; set; }
 public int? CompanyId { get; set; }
 public Company? Company { get; set; }
}
public class Company
{
 public int Id { get; set; }
 public string Name { get; set; }

 public List<User> Users { get; set; } = new();
}

```


Также был класс UsersContext для взаимодействия с бд:

```

using Microsoft.EntityFrameworkCore;

namespace MvcApp.Models
{
 public class UsersContext : DbContext
 {
 public DbSet<User> Users { get; set; } = null!;
 public DbSet<Company> Companies { get; set; } = null!;
 public UsersContext(DbContextOptions<UsersContext> options)
 : base(options)
 {
 Database.EnsureCreated();
 }
 }
}

```


И было перечисление, которое описывает все критерии сортировки:

```

public enum SortState
{
 NameAsc,
 NameDesc,
 AgeAsc,
 AgeDesc,
 CompanyAsc,
 CompanyDesc
}

```


Теперь добавим специальный tag-хелпер для создания ссылок, по нажатию на которые будет производиться сортировка. Это позволит управлять созданием заголовков,
настраивать их. Для этого добавим в проект новую папку TagHelpers. А в эту папку поместим новый класс SortHeaderTagHelper:

```

using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.Rendering;
using Microsoft.AspNetCore.Mvc.Routing;
using Microsoft.AspNetCore.Mvc.ViewFeatures;
using Microsoft.AspNetCore.Razor.TagHelpers;
using MvcApp.Models;

namespace MvcApp.TagHelpers
{
 public class SortHeaderTagHelper : TagHelper
 {
 public SortState Property { get; set; } // значение текущего свойства, для которого создается тег
 public SortState Current { get; set; } // значение активного свойства, выбранного для сортировки
 public string? Action { get; set; } // действие контроллера, на которое создается ссылка
 public bool Up { get; set; } // сортировка по возрастанию или убыванию

 [ViewContext]
 [HtmlAttributeNotBound]
 public ViewContext ViewContext { get; set; } = null!;

 IUrlHelperFactory urlHelperFactory;
 public SortHeaderTagHelper(IUrlHelperFactory helperFactory)
 {
 urlHelperFactory = helperFactory;
 }

 public override void Process(TagHelperContext context, TagHelperOutput output)
 {
 IUrlHelper urlHelper = urlHelperFactory.GetUrlHelper(ViewContext);
 output.TagName = "a";
 string? url = urlHelper.Action(Action, new { sortOrder = Property });
 output.Attributes.SetAttribute("href", url);
 // если текущее свойство имеет значение CurrentSort
 if (Current == Property)
 {
 TagBuilder tag = new TagBuilder("i");
 tag.AddCssClass("glyphicon");

 if (Up == true) // если сортировка по возрастанию
 tag.AddCssClass("glyphicon-chevron-up");
 else // если сортировка по убыванию
 tag.AddCssClass("glyphicon-chevron-down");

 output.PreContent.AppendHtml(tag);
 }
 }
 }
}

```


Данные в tag-хелпер будут передаваться извне через набор свойств:

```

public SortState Property { get; set; } // значение текущего свойства, для которого создается тег
public SortState Current { get; set; } // значение активного свойства, выбранного для сортировки
public string? Action { get; set; } // действие контроллера, на которое создается ссылка
public bool Up { get; set; } // сортировка по возрастанию или убыванию

```


В идеале все эти свойства можно выделить в отдельную модель, но я не буду этого делать, чтобы не множить чрезмерно классы.


Для создания адреса ссылки по методу контроллера потребуется объект IUrlHelperFactory. И мы можем получить его в конструкторе,
так как он встраивается по умолчанию через встроенный в ASP.NET Core механизм dependency injection.


Через тот же механизм внедрения зависимостей мы можем через атрибут получить контекст представления ViewContext, в котором будет вызываться хелпер:

```

[ViewContext]
[HtmlAttributeNotBound]
public ViewContext ViewContext { get; set; } = null!;

```


С помощью этого объекта мы сможем получить объект IUrlHelper, который необходим для создания ссылки.


Далее в методе Process идет создание ссылки. Для ее стилизации используются классы, которые будут определены далее в представлении и которые
для визуализации будут использовать шрифты библиотеки font-awesome.


Теперь нам надо передать данные для этого хелпера. Для этого определим в папке Models новый класс SortViewModel:

```

namespace MvcApp.Models
{
 public class SortViewModel
 {
 public SortState NameSort { get; set; } // значение для сортировки по имени
 public SortState AgeSort { get; set; } // значение для сортировки по возрасту
 public SortState CompanySort { get; set; } // значение для сортировки по компании
 public SortState Current { get; set; } // значение свойства, выбранного для сортировки
 public bool Up { get; set; } // Сортировка по возрастанию или убыванию

 public SortViewModel(SortState sortOrder)
 {
 // значения по умолчанию
 NameSort = SortState.NameAsc;
 AgeSort = SortState.AgeAsc;
 CompanySort = SortState.CompanyAsc;
 Up = true;

 if (sortOrder == SortState.AgeDesc || sortOrder == SortState.NameDesc
 || sortOrder == SortState.CompanyDesc)
 {
 Up = false;
 }

 switch (sortOrder)
 {
 case SortState.NameDesc:
 Current = NameSort = SortState.NameAsc;
 break;
 case SortState.AgeAsc:
 Current = AgeSort = SortState.AgeDesc;
 break;
 case SortState.AgeDesc:
 Current = AgeSort = SortState.AgeAsc;
 break;
 case SortState.CompanyAsc:
 Current = CompanySort = SortState.CompanyDesc;
 break;
 case SortState.CompanyDesc:
 Current = CompanySort = SortState.CompanyAsc;
 break;
 default:
 Current = NameSort = SortState.NameDesc;
 break;
 }
 }
 }
}

```


Здесь важно понимать смысл свойства `Current`. Оно нам нужно лишь для того, чтобы в выше определенном tag-хелпере определить, что данное свойство,
для которого применяется хелпер, используется в текущий момент для сортировки. Поэтому свойство Current указывает на значение текущего выбраного свойства, по которому проводится сортировка. То есть свойство Current будет равно одну из свойств NameSort, AgeSort или CompanySort


И далее добавим в папку Models новый класс IndexViewModel, который будет представлять модель для представления Index.cshtml:

```

namespace MvcApp.Models
{
 public class IndexViewModel
 {
 public IEnumerable<User> Users { get; set; } = new List<User>();
 public SortViewModel SortViewModel { get; set; } = new SortViewModel(SortState.NameAsc);
 }
}

```


Теперь изменим код контроллера HomeController:

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
 // добавим начальные данные для тестирования
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
 public async Task<IActionResult> Index(SortState sortOrder = SortState.NameAsc)
 {
 IQueryable<User> users = db.Users.Include(x => x.Company);

 users = sortOrder switch
 {
 SortState.NameDesc => users.OrderByDescending(s => s.Name),
 SortState.AgeAsc => users.OrderBy(s => s.Age),
 SortState.AgeDesc => users.OrderByDescending(s => s.Age),
 SortState.CompanyAsc => users.OrderBy(s => s.Company!.Name),
 SortState.CompanyDesc => users.OrderByDescending(s => s.Company!.Name),
 _ => users.OrderBy(s => s.Name),
 };
 IndexViewModel viewModel = new IndexViewModel
 {
 Users = await users.AsNoTracking().ToListAsync(),
 SortViewModel = new SortViewModel(sortOrder)
 };
 return View(viewModel);
 }
 }
}

```


И в конце изменим код представления Index.cshtml:

```

@addTagHelper *, Microsoft.AspNetCore.Mvc.TagHelpers
@using MvcApp.Models
@model IndexViewModel
<!--импортируем tag-хелперы проекта-->
@addTagHelper *, MvcApp

<style>
td, th {padding: 0 13px 0 0;}

.glyphicon{
 border: solid black;
 border-width: 0 3px 3px 0;
 display: inline-block;
 padding: 3px;
 margin: 0 5px;
}
.glyphicon-chevron-down {
 transform: rotate(45deg);
 -webkit-transform: rotate(45deg);
}

.glyphicon-chevron-up {
 transform: rotate(-135deg);
 -webkit-transform: rotate(-135deg);
}
</style>
<h1>Список пользователей</h1>
<table class="table">
 <tr>
 <th>
 <sort-header action="Index" up="@Model.SortViewModel.Up"
 current="@Model.SortViewModel.Current" property="@Model.SortViewModel.NameSort">
 Имя
 </sort-header>
 </th>
 <th>
 <sort-header action="Index" up="@Model.SortViewModel.Up"
 current="@Model.SortViewModel.Current" property="@Model.SortViewModel.AgeSort">
 Возраст
 </sort-header>
 </th>
 <th>
 <sort-header action="Index" up="@Model.SortViewModel.Up"
 current="@Model.SortViewModel.Current" property="@Model.SortViewModel.CompanySort">
 Компания
 </sort-header>
 </th>
 </tr>
 @foreach (User u in Model.Users)
 {
 <tr><td>@u.Name</td><td>@u.Age</td><td>@u.Company?.Name</td></tr>
 }
</table>

```


Создаваемый тег-хелпер использует классы glyphicon, glyphicon-chevron-down и glyphicon-chevron-up, и для их отрисовки в представлении определены некоторые стили css, которые должны выводить на веб-страницу стрелочки.


Поскольку класс tag-хелпера в своем названии имеет несколько слов, которые начинаются с большой буквы - SortHeaderTagHelper,
то в имени соотвествующего тега все части названия будут разделяться дефисом: `<sort-header>` (суффикс TagHelper при этом отбрасывается).


Через атрибуты тега `sort-header` мы можем передать значения для соотвествующих одноименных свойств класса SortHeaderTagHelper.


В итоге получился следующий проект:
![TagHelper и сортировка в ASP.NET Core MVC и C#](https://metanit.com./pics/11.9.png)


Запустим проект и отсортируем по разным критериям:
![TagHelper и сортировка данных в Entity Framework в ASP.NET Core MVC и C#](https://metanit.com./pics/11.10.png)











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

**Источник:** [https://metanit.com/sharp/aspnetmvc/11.5.php](https://metanit.com/sharp/aspnetmvc/11.5.php)
