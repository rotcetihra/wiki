# Создание tag-хелпера сортировки

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET 5 Core|Руководство по ASP.NET 5 Core]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET 5 Core/Глава 17. Работа с данными в Entity Framework в MVC|Глава 17. Работа с данными в Entity Framework в MVC]] / Создание tag-хелпера сортировки

[[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET 5 Core/Глава 17. Работа с данными в Entity Framework в MVC/Сортировка|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET 5 Core/Глава 17. Работа с данными в Entity Framework в MVC|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET 5 Core/Глава 17. Работа с данными в Entity Framework в MVC/Фильтрация|Вперёд]]

**Дата написания:** 05.09.2026

## Создание tag-хелпера сортировки


Данное руководство устарело. Актуальное руководство: [Руководство по ASP.NET Core 7](https://metanit.com/sharp/aspnet6/)Последнее обновление: 09.12.2019




-

-

-














Продолжим работу с проектом, который был создан в прошлой теме, где у нас были модели User и Company:

```

public class User
{
 public int Id { get; set; }
 public string Name { get; set; }
 public int Age { get; set; }
 public string Company { get; set; }
 public int CompanyId { get; set; }
 public Company Company { get; set; }
}
public class Company
{
 public int Id { get; set; }
 public string Name { get; set; }

 public List<User> Users { get; set; }
 public Company()
 {
 Users = new List<User>();
 }
}

```


Также был класс UsersContext для взаимодействия с бд:

```

using Microsoft.EntityFrameworkCore;

namespace SortApp.Models
{
 public class UsersContext : DbContext
 {
 public DbSet<User> Users { get; set; }
 public DbSet<Company> Companies { get; set; }
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
using SortApp.Models;

namespace SortApp.TagHelpers
{
 public class SortHeaderTagHelper : TagHelper
 {
 public SortState Property { get; set; } // значение текущего свойства, для которого создается тег
 public SortState Current { get; set; } // значение активного свойства, выбранного для сортировки
 public string Action { get; set; } // действие контроллера, на которое создается ссылка
 public bool Up { get; set; } // сортировка по возрастанию или убыванию

 private IUrlHelperFactory urlHelperFactory;
 public SortHeaderTagHelper(IUrlHelperFactory helperFactory)
 {
 urlHelperFactory = helperFactory;
 }
 [ViewContext]
 [HtmlAttributeNotBound]
 public ViewContext ViewContext { get; set; }

 public override void Process(TagHelperContext context, TagHelperOutput output)
 {
 IUrlHelper urlHelper = urlHelperFactory.GetUrlHelper(ViewContext);
 output.TagName = "a";
 string url = urlHelper.Action(Action, new { sortOrder = Property });
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
public string Action { get; set; } // действие контроллера, на которое создается ссылка
public bool Up { get; set; } // сортировка по возрастанию или убыванию

```


В идеале все эти свойства можно выделить в отдельную модель, но я не буду этого делать, чтобы не множить чрезмерно классы.


Для создания адреса ссылки по методу контроллера потребуется объект IUrlHelperFactory. И мы можем получить его в конструкторе,
так как он встраивается по умолчанию через встроенный в ASP.NET Core механизм dependency injection.


Через тот же механизм внедрения зависимостей мы можем через атрибут получить контекст представления ViewContext, в котором будет вызываться хелпер:

```

[ViewContext]
[HtmlAttributeNotBound]
public ViewContext ViewContext { get; set; }

```


С помощью этого объекта мы сможем получить объект IUrlHelper, который необходим для создания ссылки.


Далее в методе Process идет создание ссылки. Для ее стилизации используются классы, которые будут определены далее в представлении и которые
для визуализации будут использовать шрифты библиотеки font-awesome.


Теперь нам надо передать данные для этого хелпера. Для этого определим в папке Models новый класс SortViewModel:

```

namespace SortApp.Models
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

using System.Collections.Generic;

namespace SortApp.Models
{
 public class IndexViewModel
 {
 public IEnumerable<User> Users { get; set; }
 public SortViewModel SortViewModel { get; set; }
 }
}

```


Теперь изменим код контроллера HomeController:

```

using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using SortApp.Models;
using System.Linq;

namespace SortApp.Controllers
{
 public class HomeController : Controller
 {
 UsersContext db;
 public HomeController(UsersContext context)
 {
 this.db = context;
 // добавим начальные данные для тестирования
 if(db.Companies.Count() == 0)
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
 IQueryable<User> users = db.Users.Include(x=>x.Company);

 users = sortOrder switch
 {
 SortState.NameDesc => users.OrderByDescending(s => s.Name),
 SortState.AgeAsc => users.OrderBy(s => s.Age),
 SortState.AgeDesc => users.OrderByDescending(s => s.Age),
 SortState.CompanyAsc => users.OrderBy(s => s.Company.Name),
 SortState.CompanyDesc => users.OrderByDescending(s => s.Company.Name),
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

@using SortApp.Models

@model IndexViewModel
<!--импортируем tag-хелперы проекта-->
@addTagHelper *, SortApp

@{
 ViewData["Title"] = "Список пользователей";
}
<style>
@@font-face{font-family:'FontAwesome';src:url('https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/fonts/fontawesome-webfont.woff2') format('woff2'),
url('https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/fonts/fontawesome-webfont.woff') format('woff'),
url('https://maxcdn.bootstrapcdn.com/font-awesome/4.4.0/fonts/fontawesome-webfont.ttf') format('truetype');font-weight:normal;font-style:normal}
.glyphicon {
 display: inline-block;
 font: normal normal normal 14px/1 FontAwesome;
 font-size: inherit;
 text-rendering: auto;
 -webkit-font-smoothing: antialiased;
 -moz-osx-font-smoothing: grayscale
}
.glyphicon-chevron-down:before {
content: "\f078";
}

.glyphicon-chevron-up:before {
content: "\f077";
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
 <tr><td>@u.Name</td><td>@u.Age</td><td>@u.Company.Name</td></tr>
 }
</table>

```


Поскольку создаваемый тег-хелпер использует классы glyphicon, glyphicon-chevron-down и glyphicon-chevron-up, которые визуализируются с помощью библиотеки font-awesome.
В данном случае подключение необходимых шрифтов font-awesome и определение используемых их классов для краткости производися в представлении, но в реальном приложении, конечно,
все это можно вынести в отдельный css-файл.


Поскольку класс tag-хелпера в своем названии имеет несколько слов, которые начинаются с большой буквы - SortHeaderTagHelper,
то в имени соотвествующего тега все части названия будут разделяться дефисом: `<sort-header>` (суффикс TagHelper при этом отбрасывается).


Через атрибуты тега `sort-header` мы можем передать значения для соотвествующих одноименных свойств класса SortHeaderTagHelper.


В итоге получился следующий проект:
![TagHelper и сортировка в ASP.NET Core](https://metanit.com./pics/sort4.png)


Запустим проект и отсортируем по разным критериям:
![TagHelper и сортировка в ASP.NET Core MVC](https://metanit.com./pics/sort5.png)










- Глава 1. Введение в ASP.NET Core


 - [ASP.NET Core - новая эпоха в развитии ASP.NET](//metanit.com/sharp/aspnet5/1.1.php)

 - [Начало работы с ASP.NET Core](//metanit.com/sharp/aspnet5/1.2.php)

 - [Проект ASP.NET Core в Visual Studio for Mac](//metanit.com/sharp/aspnet5/1.3.php)



- Глава 2. Основы ASP.NET Core


 - [Запуск приложения. Класс Program](//metanit.com/sharp/aspnet5/2.13.php)

 - [Класс Startup](//metanit.com/sharp/aspnet5/2.1.php)

 - [Конвейер обработки запроса и middleware](//metanit.com/sharp/aspnet5/2.2.php)

 - [Методы Use, Run и делегат RequestDelegate](//metanit.com/sharp/aspnet5/2.3.php)

 - [Методы Map и MapWhen](//metanit.com/sharp/aspnet5/2.22.php)

 - [Создание компонентов middleware](//metanit.com/sharp/aspnet5/2.4.php)

 - [Конвейер обработки запроса](//metanit.com/sharp/aspnet5/2.18.php)

 - [IWebHostEnvironment и окружение](//metanit.com/sharp/aspnet5/2.21.php)

 - [Статические файлы](//metanit.com/sharp/aspnet5/2.5.php)

 - [Работа со статическими файлами](//metanit.com/sharp/aspnet5/2.14.php)

 - [Обработка ошибок](//metanit.com/sharp/aspnet5/17.1.php)

 - [Работа с HTTPS](//metanit.com/sharp/aspnet5/18.6.php)



- Глава 3. Сервисы и Dependency Injection


 - [Сервисы и метод ConfigureServices](//metanit.com/sharp/aspnet5/6.1.php)

 - [Создание своих сервисов](//metanit.com/sharp/aspnet5/2.19.php)

 - [Передача зависимостей](//metanit.com/sharp/aspnet5/6.4.php)

 - [Жизненный цикл зависимостей](//metanit.com/sharp/aspnet5/6.2.php)

 - [Применение сервисов в middleware](//metanit.com/sharp/aspnet5/2.20.php)

 - [Singleton-объекты и scoped-сервисы](//metanit.com/sharp/aspnet5/6.5.php)



- Глава 4. Конфигурация


 - [Основы конфигурации](//metanit.com/sharp/aspnet5/2.6.php)

 - [Нефайловые провайдеры конфигурации](//metanit.com/sharp/aspnet5/2.16.php)

 - [Файловые провайдеры конфигурации](//metanit.com/sharp/aspnet5/2.12.php)

 - [Объединение конфигураций и установка сервиса IConfiguration](//metanit.com/sharp/aspnet5/2.23.php)

 - [Работа с конфигурацией](//metanit.com/sharp/aspnet5/2.17.php)

 - [Создание провайдера конфгурации](//metanit.com/sharp/aspnet5/2.15.php)

 - [Проекция конфигурации на классы](//metanit.com/sharp/aspnet5/2.9.php)

 - [Передача конфигурации через IOptions](//metanit.com/sharp/aspnet5/6.3.php)



- Глава 5. Состояние приложения. Куки. Сессии


 - [HttpContext.Items](//metanit.com/sharp/aspnet5/2.11.php)

 - [Куки](//metanit.com/sharp/aspnet5/2.25.php)

 - [Сессии](//metanit.com/sharp/aspnet5/2.26.php)



- Глава 6. Логгирование


 - [Ведение лога и ILogger](//metanit.com/sharp/aspnet5/2.10.php)

 - [Фабрика логгера и провайдеры логгирования](//metanit.com/sharp/aspnet5/2.29.php)

 - [Конфигурация и фильтрация логгирования](//metanit.com/sharp/aspnet5/2.28.php)

 - [Создание провайдера логгирования](//metanit.com/sharp/aspnet5/2.27.php)



- Глава 7. Маршрутизация


 - [Основы маршрутизации в ASP.NET Core](//metanit.com/sharp/aspnet5/11.1.php)

 - [RouterMiddleware](//metanit.com/sharp/aspnet5/11.12.php)

 - [Определение маршрутов](//metanit.com/sharp/aspnet5/11.2.php)

 - [Работа с маршрутами](//metanit.com/sharp/aspnet5/11.4.php)

 - [Ограничения маршрутов](//metanit.com/sharp/aspnet5/11.3.php)

 - [Создание ограничений маршрутов](//metanit.com/sharp/aspnet5/11.7.php)

 - [Создание своего маршрута](//metanit.com/sharp/aspnet5/11.8.php)



- Глава 8. ASP.NET Core MVC


 - [Введение в ASP.NET Core MVC](//metanit.com/sharp/aspnet5/3.1.php)

 - [Добавление MVC в пустой проект](//metanit.com/sharp/aspnet5/3.6.php)

 - [Первое приложение. Добавление моделей и базы данных](//metanit.com/sharp/aspnet5/3.2.php)

 - [Создание контроллера и инициализатора базы данных](//metanit.com/sharp/aspnet5/3.3.php)

 - [Добавление методов контроллера и представлений](//metanit.com/sharp/aspnet5/3.4.php)

 - [Добавление мастер-страницы и стилизации](//metanit.com/sharp/aspnet5/3.5.php)



- Глава 9. Контроллеры


 - [Контроллеры и их действия](//metanit.com/sharp/aspnet5/5.1.php)

 - [Передача данных в контроллер](//metanit.com/sharp/aspnet5/5.2.php)

 - [Результаты действий](//metanit.com/sharp/aspnet5/5.3.php)

 - [ContentResult и JsonResult](//metanit.com/sharp/aspnet5/5.4.php)

 - [Переадресация](//metanit.com/sharp/aspnet5/5.5.php)

 - [Отправка статусных кодов](//metanit.com/sharp/aspnet5/5.6.php)

 - [Отправка файлов](//metanit.com/sharp/aspnet5/5.7.php)

 - [Переопределение контроллеров](//metanit.com/sharp/aspnet5/5.8.php)

 - [Контекст контроллера](//metanit.com/sharp/aspnet5/5.9.php)

 - [Передача зависимостей в контроллер](//metanit.com/sharp/aspnet5/5.10.php)



- Глава 10. Представления


 - [Введение в представления](//metanit.com/sharp/aspnet5/7.1.php)

 - [Движок представлений Razor](//metanit.com/sharp/aspnet5/7.2.php)

 - [Передача данных в представление](//metanit.com/sharp/aspnet5/7.3.php)

 - [Мастер-страницы](//metanit.com/sharp/aspnet5/7.4.php)

 - [Файл _ViewImports.cshtml](//metanit.com/sharp/aspnet5/7.9.php)

 - [Частичные представления](//metanit.com/sharp/aspnet5/7.5.php)

 - [Внедрение зависимостей в представления](//metanit.com/sharp/aspnet5/7.7.php)

 - [Работа с формами](//metanit.com/sharp/aspnet5/7.8.php)

 - [Создание движка представлений](//metanit.com/sharp/aspnet5/7.10.php)



- Глава 11. Маршрутизация в ASP.NET Core MVC


 - [Маршрутизация в MVC с помощью конечных точек](//metanit.com/sharp/aspnet5/11.5.php)

 - [Маршрутизация с помощью RouterMiddleware. Метод UseMvc](//metanit.com/sharp/aspnet5/11.13.php)

 - [Атрибуты маршрутизации](//metanit.com/sharp/aspnet5/11.6.php)

 - [Области](//metanit.com/sharp/aspnet5/11.9.php)



- Глава 12. Модели


 - [Модели в ASP.NET Core MVC](//metanit.com/sharp/aspnet5/8.1.php)

 - [Модели представления View Model](//metanit.com/sharp/aspnet5/8.2.php)

 - [Привязка модели](//metanit.com/sharp/aspnet5/8.3.php)

 - [Передача данных в контроллер](//metanit.com/sharp/aspnet5/8.4.php)

 - [Управление привязкой](//metanit.com/sharp/aspnet5/8.5.php)

 - [Создание привязчика модели](//metanit.com/sharp/aspnet5/8.6.php)



- Глава 13. HTML-хелперы


 - [Создание HTML-хелперов](//metanit.com/sharp/aspnet5/9.1.php)

 - [HTML-хелперы элементов форм](//metanit.com/sharp/aspnet5/9.2.php)

 - [Строго типизированные хелперы](//metanit.com/sharp/aspnet5/9.3.php)

 - [Шаблонные хелперы](//metanit.com/sharp/aspnet5/9.4.php)

 - [Генерация ссылок](//metanit.com/sharp/aspnet5/9.5.php)

 - [URL-хелперы](//metanit.com/sharp/aspnet5/11.11.php)



- Глава 14. Tag-хелперы


 - [Введение в tag-хелперы](//metanit.com/sharp/aspnet5/10.1.php)

 - [AnchorTagHelper](//metanit.com/sharp/aspnet5/10.2.php)

 - [LinkTagHelper и ScriptTagHelper](//metanit.com/sharp/aspnet5/10.3.php)

 - [Tag-хелперы форм](//metanit.com/sharp/aspnet5/10.4.php)

 - [EnvironmentTagHelper](//metanit.com/sharp/aspnet5/10.6.php)

 - [CacheTagHelper](//metanit.com/sharp/aspnet5/10.7.php)

 - [Создание tag-хелперов](//metanit.com/sharp/aspnet5/10.8.php)

 - [Управление выводом tag-хелпера](//metanit.com/sharp/aspnet5/10.10.php)

 - [Контекст хелпера и получение зависимостей](//metanit.com/sharp/aspnet5/10.11.php)

 - [Атрибут HtmlTargetElement](//metanit.com/sharp/aspnet5/10.12.php)

 - [Tag-хелперы и сложные объекты и коллекции](//metanit.com/sharp/aspnet5/10.9.php)



- Глава 15. View Component


 - [Определение компонента представлений](//metanit.com/sharp/aspnet5/7.6.php)

 - [Передача данных в View Component](//metanit.com/sharp/aspnet5/7.11.php)

 - [Генерация контента в View Component](//metanit.com/sharp/aspnet5/7.12.php)

 - [ViewViewComponentResult и представления](//metanit.com/sharp/aspnet5/7.13.php)

 - [Асинхронные операции в View Component](//metanit.com/sharp/aspnet5/7.14.php)

 - [ViewComponentContext](//metanit.com/sharp/aspnet5/7.15.php)



- Глава 16. Метаданные и валидация модели


 - [Основы валидации](//metanit.com/sharp/aspnet5/19.1.php)

 - [Атрибуты валидации](//metanit.com/sharp/aspnet5/19.2.php)

 - [Валидация на стороне сервера](//metanit.com/sharp/aspnet5/19.3.php)

 - [Валидация на стороне клиента](//metanit.com/sharp/aspnet5/19.4.php)

 - [Tag-хелперы валидации](//metanit.com/sharp/aspnet5/10.5.php)

 - [Создание атрибута валидации. Самовалидация модели](//metanit.com/sharp/aspnet5/19.5.php)

 - [Аннотации данных](//metanit.com/sharp/aspnet5/19.6.php)



- Глава 17. Работа с данными в Entity Framework в MVC


 - [Подключение и создание базы данных в Entity Framework Core](//metanit.com/sharp/aspnet5/12.1.php)

 - [Операции с моделями. Создание и вывод](//metanit.com/sharp/aspnet5/12.2.php)

 - [Операции с моделями. Редактирование и удаление](//metanit.com/sharp/aspnet5/12.3.php)

 - [Сортировка](//metanit.com/sharp/aspnet5/12.4.php)

 - [Создание tag-хелпера сортировки](//metanit.com/sharp/aspnet5/12.5.php)

 - [Фильтрация](//metanit.com/sharp/aspnet5/12.6.php)

 - [Постраничная навигация](//metanit.com/sharp/aspnet5/12.7.php)

 - [Tag-хелпер для постраничной навигации](//metanit.com/sharp/aspnet5/12.8.php)

 - [Объединение сортировки, фильтрации и пагинации](//metanit.com/sharp/aspnet5/12.9.php)

 - [Tag-хелпер пагинации с сортировкой и фильтрацией](//metanit.com/sharp/aspnet5/12.10.php)



- Глава 18. Razor Pages


 - [Введение в Razor Pages](//metanit.com/sharp/aspnet5/29.1.php)

 - [Добавление RazorPages в пустой проект](//metanit.com/sharp/aspnet5/29.2.php)

 - [Обработка запросов. Передача форм](//metanit.com/sharp/aspnet5/29.3.php)

 - [Привязка свойств RazorPage к параметрам запроса](//metanit.com/sharp/aspnet5/29.4.php)

 - [Параметры маршрутов в Razor Pages](//metanit.com/sharp/aspnet5/29.5.php)

 - [Обработчики страницы](//metanit.com/sharp/aspnet5/29.6.php)

 - [Возвращение результата](//metanit.com/sharp/aspnet5/29.7.php)

 - [Переадресация и создание ссылок](//metanit.com/sharp/aspnet5/29.8.php)

 - [Подключение к базе данных](//metanit.com/sharp/aspnet5/29.9.php)

 - [Создание и вывод объектов из базы данных](//metanit.com/sharp/aspnet5/29.10.php)

 - [Изменение и удаление в базе данных](//metanit.com/sharp/aspnet5/29.11.php)



- Глава 19. Web API


 - [Введение в Web API](//metanit.com/sharp/aspnet5/23.1.php)

 - [Создание контроллера](//metanit.com/sharp/aspnet5/23.2.php)

 - [Тестирование контроллера](//metanit.com/sharp/aspnet5/23.3.php)

 - [Создание клиента для WEB API](//metanit.com/sharp/aspnet5/23.4.php)

 - [Валидация в Web API](//metanit.com/sharp/aspnet5/23.5.php)

 - [Content negotiation](//metanit.com/sharp/aspnet5/23.6.php)



- Глава 20. Фильтры


 - [Введение в фильтры](//metanit.com/sharp/aspnet5/18.1.php)

 - [Передача параметров в фильтры и установка зависимостей](//metanit.com/sharp/aspnet5/18.5.php)

 - [Фильтры ресурсов](//metanit.com/sharp/aspnet5/18.2.php)

 - [Фильтры действий](//metanit.com/sharp/aspnet5/18.3.php)

 - [Фильтры результатов](//metanit.com/sharp/aspnet5/18.4.php)

 - [Фильтры исключений](//metanit.com/sharp/aspnet5/17.2.php)

 - [Фильтры RazorPages](//metanit.com/sharp/aspnet5/18.7.php)



- Глава 21. Аутентификация и авторизация


 - [Аутентификация на основе куки. Часть 1](//metanit.com/sharp/aspnet5/15.1.php)

 - [Аутентификация на основе куки. Часть 2](//metanit.com/sharp/aspnet5/15.2.php)

 - [Авторизация](//metanit.com/sharp/aspnet5/15.3.php)

 - [ClaimPrincipal и объекты Claim](//metanit.com/sharp/aspnet5/15.4.php)

 - [Авторизация по ролям](//metanit.com/sharp/aspnet5/15.5.php)

 - [Авторизация на основе Claims](//metanit.com/sharp/aspnet5/15.6.php)

 - [Пример авторизации на основе Claims](//metanit.com/sharp/aspnet5/15.7.php)

 - [Создание ограничений для политики авторизации](//metanit.com/sharp/aspnet5/15.8.php)

 - [JWT-токены](//metanit.com/sharp/aspnet5/23.7.php)



- Глава 22. ASP.NET Core Identity


 - [Введение в ASP.NET Core Identity](//metanit.com/sharp/aspnet5/16.1.php)

 - [Основные классы в ASP.NET Core Identity](//metanit.com/sharp/aspnet5/16.11.php)

 - [Добавление Identity в проект с нуля](//metanit.com/sharp/aspnet5/16.2.php)

 - [Регистрация и создание пользователей в Identity](//metanit.com/sharp/aspnet5/16.3.php)

 - [Авторизация пользователей в Identity](//metanit.com/sharp/aspnet5/16.4.php)

 - [Управление пользователями](//metanit.com/sharp/aspnet5/16.7.php)

 - [Изменение пароля](//metanit.com/sharp/aspnet5/16.8.php)

 - [Валидация пароля](//metanit.com/sharp/aspnet5/16.9.php)

 - [Валидация пользователя](//metanit.com/sharp/aspnet5/16.10.php)

 - [Управление ролями](//metanit.com/sharp/aspnet5/16.13.php)

 - [Инициализация БД ролями и пользователями](//metanit.com/sharp/aspnet5/16.12.php)



- Глава 23. Клиентская разработка


 - [Бандлинг и минификация](//metanit.com/sharp/aspnet5/13.6.php)

 - [Менеджер Libman](//metanit.com/sharp/aspnet5/13.7.php)

 - [Пакетный менеджер NPM](//metanit.com/sharp/aspnet5/13.5.php)

 - [Gulp](//metanit.com/sharp/aspnet5/13.1.php)

 - [Grunt](//metanit.com/sharp/aspnet5/13.2.php)

 - [Препроцессоры Less и Sass](//metanit.com/sharp/aspnet5/13.4.php)



- Глава 24. Производительность и кэширование


 - [Кэширование с помощью MemoryCache](//metanit.com/sharp/aspnet5/14.1.php)

 - [Атрибут ResponseCache](//metanit.com/sharp/aspnet5/14.2.php)

 - [Сжатие ответа](//metanit.com/sharp/aspnet5/14.3.php)

 - [Кэширование статических файлов](//metanit.com/sharp/aspnet5/14.4.php)



- Глава 25. Сервер и публикация приложения


 - [Сервер](//metanit.com/sharp/aspnet5/2.7.php)

 - [Публикация на IIS](//metanit.com/sharp/aspnet5/20.1.php)

 - [Установка приложения в виде службы Windows](//metanit.com/sharp/aspnet5/20.2.php)



- Глава 26. Тестирование


 - [Введение в юнит-тесты](//metanit.com/sharp/aspnet5/22.1.php)

 - [Создание проекта юнит-тестов. Добавление xUnit](//metanit.com/sharp/aspnet5/22.2.php)

 - [Создание юнит-тестов](//metanit.com/sharp/aspnet5/22.3.php)

 - [Фреймворк Moq и moq-объекты](//metanit.com/sharp/aspnet5/22.4.php)

 - [Тестирование контроллера](//metanit.com/sharp/aspnet5/22.5.php)



- Глава 27. URL Rewriting


 - [Введение в URL Rewriting](//metanit.com/sharp/aspnet5/24.1.php)

 - [Правила IIS для URL Rewriting](//metanit.com/sharp/aspnet5/24.2.php)

 - [Применение правил для Apache](//metanit.com/sharp/aspnet5/24.3.php)

 - [Создание правил URL Rewriting](//metanit.com/sharp/aspnet5/24.4.php)



- Глава 28. Глобализация и локализация


 - [Определение культуры](//metanit.com/sharp/aspnet5/28.1.php)

 - [RequestLocalizationMiddleware](//metanit.com/sharp/aspnet5/28.2.php)

 - [Локализация строк. IStringLocalizer](//metanit.com/sharp/aspnet5/28.3.php)

 - [Ресурсы и локализация в контроллерах](//metanit.com/sharp/aspnet5/28.4.php)

 - [Локализация представлений](//metanit.com/sharp/aspnet5/28.5.php)

 - [Локализация аннотаций данных](//metanit.com/sharp/aspnet5/28.6.php)

 - [Переключение языка приложения](//metanit.com/sharp/aspnet5/28.7.php)

 - [Общие ресурсы локализации](//metanit.com/sharp/aspnet5/28.8.php)

 - [Хранение ресурсов в базе данных](//metanit.com/sharp/aspnet5/28.9.php)



- Глава 29. SignalR Core


 - [SignalR Core. Первое приложение](//metanit.com/sharp/aspnet5/30.1.php)

 - [Создание и конфигурация хабов](//metanit.com/sharp/aspnet5/30.2.php)

 - [Клиент javascript](//metanit.com/sharp/aspnet5/30.3.php)

 - [Контекст хаба, подключение и отключение клиентов](//metanit.com/sharp/aspnet5/30.4.php)

 - [Взаимодействие с клиентами](//metanit.com/sharp/aspnet5/30.5.php)

 - [IHubContext](//metanit.com/sharp/aspnet5/30.6.php)

 - [Отправка сложных объектов](//metanit.com/sharp/aspnet5/30.7.php)

 - [Аутентификация и авторизация на основе куки](//metanit.com/sharp/aspnet5/30.8.php)

 - [Аутентификация и авторизация с помощью токенов](//metanit.com/sharp/aspnet5/30.9.php)

 - [Пользователи](//metanit.com/sharp/aspnet5/30.10.php)

 - [Группы](//metanit.com/sharp/aspnet5/30.11.php)

 - [Клиент на Xamarin Forms](//metanit.com/sharp/aspnet5/30.12.php)



- Глава 30. CORS и кросс-доменные запросы


 - [Начало работы с CORS](//metanit.com/sharp/aspnet5/31.1.php)

 - [Конфигурация CORS](//metanit.com/sharp/aspnet5/31.2.php)

 - [Политики CORS](//metanit.com/sharp/aspnet5/31.3.php)

 - [Глобальная и локальная настройка CORS](//metanit.com/sharp/aspnet5/31.5.php)

 - [CORS в MVC](//metanit.com/sharp/aspnet5/31.4.php)



- Глава 31. Dapper


 - [Работа с Dapper в ASP.NET Core](//metanit.com/sharp/aspnet5/26.1.php)



- Глава 32. React.JS


 - [Подключение React в ASP.NET Core](//metanit.com/sharp/aspnet5/25.1.php)

 - [Взаимодействие React.JS и ASP.NET Core](//metanit.com/sharp/aspnet5/25.2.php)



- Глава 33. Дополнительные статьи


 - [Отправка email в ASP.NET Core](//metanit.com/sharp/aspnet5/21.1.php)

 - [Загрузка файлов на сервер](//metanit.com/sharp/aspnet5/21.3.php)










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

**Источник:** [https://metanit.com/sharp/aspnet5/12.5.php](https://metanit.com/sharp/aspnet5/12.5.php)
