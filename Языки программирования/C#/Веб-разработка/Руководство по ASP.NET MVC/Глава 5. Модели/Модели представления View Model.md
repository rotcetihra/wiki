# Модели представления View Model

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC|Руководство по ASP.NET MVC]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 5. Модели|Глава 5. Модели]] / Модели представления View Model

[[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 5. Модели/Введение в определение и применение моделей|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 5. Модели|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 5. Модели/Привязка модели|Вперёд]]

**Дата написания:** 05.09.2026

## Модели представления View Model

Последнее обновление: 26.03.2022




-

-

-














В зависимости от сложности проекта можно использовать одну и ту же модель для хранения данных в базе данных, для передачи данных в представление и получения данных из представления.
Однако нередко все же модели могут не совпадать. Например, нам не надо передавать в представление все данные определенной модели или надо передать в представление
объекты сразу двух моделей. И в этом случае мы можем воспользоваться моделями представления.


Рассмотрим простейший пример работы с моделями. Допустим, в проекте в папке Model у нас есть следующие модели Person и Company.

```

namespace MvcApp.Models
{
 public record class Person(int Id, string Name, int Age, Company Work);
 public record class Company(int Id, string Name, string Country);
}

```


Модель Person представляет пользователей, а модель Company - компанию, где они работают.


И, допустим, нам надо выводить на страницу список пользователей и фильтровать их по компаниям. Наподобие
следующего:
![Модели представления view models в ASP.NET Core MVC и C#](https://metanit.com./pics/5.3.png)


Очевидно, что этих двух моделей - Person и Company для решения поставленной задачи нам недостаточно. И нам надо создать
специальную модель для передачи данных в представление или модель представления (иными словами View Model). Для этого вначале добавим в
проект новую папку ViewModels. В принципе модели представлений не обязательно определять именно в папке ViewModels,
это может быть любая папка, в том числе и имеющаяся по умолчанию папка Models. Далее в каталог ViewModels поместим модель CompanyModel:

```

namespace MvcApp.ViewModels
{
 public record class CompanyModel(int Id, string Name);
}

```


Эта модель упрощает передачу списка компаний в представление.


И также добавим в папку ViewModels собственно модель представления, которую назовем IndexViewModel:

```

using MvcApp.Models; // пространство имен модели Person

namespace MvcApp.ViewModels
{
 public class IndexViewModel
 {
 public IEnumerable<Person> People { get; set; } = new List<Person>();
 public IEnumerable<CompanyModel> Companies { get; set; } = new List<CompanyModel>();
 }
}

```


С помощью этой модели мы сможем передать в представление сразу и список компаний, и список пользователей.


Далее в проекте в папке Controllers определим следующий контроллер HomeController:

```

using Microsoft.AspNetCore.Mvc;
using MvcApp.Models; // пространство имен модели Person и Company
using MvcApp.ViewModels; // пространство имен модели IndexViewModel и CompanyModel

namespace MvcApp.Controllers
{
 public class HomeController : Controller
 {
 List<Person> people;
 List<Company> companies;
 public HomeController()
 {
 Company microsoft = new Company(1, "Microsoft", "USA");
 Company google = new Company(2, "Google", "USA");
 Company jetbrains = new Company(3, "JetBrains", "Czech Republic");
 companies = new List<Company> { microsoft, google, jetbrains};

 people = new List<Person>
 {
 new Person(1, "Tom", 37, microsoft),
 new Person(2, "Bob", 41, microsoft),
 new Person(3, "Sam", 28, google),
 new Person(4, "Bill", 32, google),
 new Person(5, "Kate", 33, jetbrains),
 new Person(6, "Alex", 25, jetbrains),
 };
 }
 public IActionResult Index(int? companyId)
 {
 // формируем список компаний для передачи в представление
 List<CompanyModel> compModels = companies
 .Select(c => new CompanyModel(c.Id, c.Name)).ToList();
 // добавляем на первое место
 compModels.Insert(0, new CompanyModel(0, "Все"));

 IndexViewModel viewModel = new() { Companies = compModels, People = people };

 // если передан id компании, фильтруем список
 if (companyId != null && companyId > 0)
 viewModel.People = people.Where(p => p.Work.Id == companyId);

 return View(viewModel);
 }
 }
}

```


В метод Index передается опциональный параметр `companyId`, который передает идентификатор выбранной компании. Если он не равен 0 и определен, то производим фильтрацию по компаниям.


И в конце определим в проекте в папке Views/Home представление Index.cshtml, которое будет выводить все объекты:

```

@using MvcApp.ViewModels
@using MvcApp.Models
@model IndexViewModel

<style>
td{padding:5px;}
tr:nth-child(even) {background: #CCC}
tr:nth-child(odd) {background: #FFF}
</style>

<form>
 <label>Выберите компанию:</label>
 <select name="companyId" >
 @foreach(CompanyModel comp in Model.Companies)
 {
 <option value="@comp.Id">@comp.Name</option>
 }
 </select>
 <input type="submit" />
</form>
<br />
<table>
 <tr><td>Name</td><td>Company</td><td>Age</td></tr>
 @foreach (Person p in Model.People)
 {
 <tr><td>@p.Name</td><td>@p.Work.Name</td><td>@p.Age</td></tr>
 }
</table>

```


В итоге проект будет иметь следующую структуру:
![Добавление моделей представлений в ASP.NET Core MVC и C#](https://metanit.com./pics/5.4.png)


И теперь у нас получится веб-страница, как на первом скриншоте, на которой используется фильтрация.


В данном случае продемонстрирован наглядный пример, где с помощью только одной простой моделей типа Person и Company было бы сложно передать данные.
И поэтому было бы более оптимально прибегнуть к комплексной модели представления (IndexViewModel).











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

**Источник:** [https://metanit.com/sharp/aspnetmvc/5.2.php](https://metanit.com/sharp/aspnetmvc/5.2.php)
