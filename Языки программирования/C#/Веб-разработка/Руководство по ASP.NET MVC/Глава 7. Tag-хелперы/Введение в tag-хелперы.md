# Введение в tag-хелперы

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC|Руководство по ASP.NET MVC]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 7. Tag-хелперы|Глава 7. Tag-хелперы]] / Введение в tag-хелперы

[[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 6. HTML-хелперы/URL-хелперы|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 7. Tag-хелперы|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 7. Tag-хелперы/AnchorTagHelper. Создание ссылок|Вперёд]]

**Дата написания:** 05.09.2026

## Введение в tag-хелперы

Последнее обновление: 03.04.2022




-

-

-














Tag-хелперы представляют собой функциональность, предназначенную для генерации HTML-разметки. Tag-хелперы применяются в представлениях
и выглядят как обычные html-элементы или атрибуты, однако при работе приложения они обрабатываются движком Razor на стороне сервера и в
конечном счете преобразуются в стандартные html-элементы.


Tag-хелперы представляют более удобный способ для генерации html-элементов, нежели обычные html-хелперы, поскольку tag-хелперы во многом выглядят как обычные html-элементы,
Visual Studio имеет встроенную поддержку IntelliSense для tag-хелперов


Использовать tag-хелперы довольно просто. Рассмотрим на примере примитивного проекта. Пусть у нас есть проект по типу ASP.NET Core Empty. Определим в
файле Program.cs подключение необходимых сервисов MVC:

```

var builder = WebApplication.CreateBuilder(args);
builder.Services.AddControllersWithViews();
var app = builder.Build();

app.MapControllerRoute(
 name: "default",
 pattern: "{controller=Home}/{action=Index}/{id?}");

app.Run();

```


Для тестирования в проекте определим папку Controllers, а в нее поместим следующий контроллер HomeController:

```

using Microsoft.AspNetCore.Mvc;

namespace MvcApp.Controllers
{
 public class HomeController : Controller
 {
 public IActionResult Index() => View();
 public string Contacts() => "Contacts page";
 }
}

```


Для представлений этого контроллера создадим в проекте папку Views, а в ней - каталог Home. Затем в папку Views/Home поместим
новое представление Index.cshtml:

```

@addTagHelper *, Microsoft.AspNetCore.Mvc.TagHelpers

<a asp-controller="Home" asp-action="Contacts">Контакты</a>

```


Сначала в представлении идет директива addTagHelper

```
@addTagHelper *, Microsoft.AspNetCore.Mvc.TagHelpers
```


Первый параметр директивы указывает на tag-хелперы, которые будут доступны в представлении, а второй параметр определяет
библиотеку хелперов. В данном случае директива использует синтаксис подстановок - знак звездочки ("*") означает, что подключаются все хелперы из
библиотеки Microsoft.AspNetCore.Mvc.TagHelpers.


Далее идет собственно tag-хелпер:

```
<a asp-controller="Home" asp-action="Contacts">Контакты</a>
```


Внешне данный хелпер напоминает обычную ссылку - стандартный элемент html, однако это не элемент html. И если мы воспользуемся всплывающей подсказкой,
то увидим, что кроме обычных для элемента `<a />` он имеет ряд других:
![Tag хелперы в ASP.NET Core MVC и C#](https://metanit.com./pics/7.1.png)


Данный хелпер создает ссылку, для которой в качестве контроллера используется Home, а в качестве метода Contact. Такой хелпер будет интуитивно более
понятным и привычным, нежели создание ссылки с помощью Html.ActionLink:

```
@Html.ActionLink("Контакты", "Contacts", "Home")
```


В то же время нам необязательно использовать именно tag-хелперы. Мы можем использовать обычные html-хелперы, если они нам более удобны.


В итоге при запуске проекта вместа данного tag-хелпера будет сформирована гиперссылка, по нажатию на которую запрос будет обрабатываться методом Contacts контроллера Home:
![добавление tag-хелперов в представление в ASP.NET Core MVC и C#](https://metanit.com./pics/7.2.png)


### _ViewImports.cshtml и @addTagHelper


Выше в представление были подключены tag-хелперы. Но что, если нам надо подключить tag-хелперы в кучу представлений? Вместо того, чтобы прописывать директиву
@addTagHelper в каждом отдельном представлении, мы можем подключить все хелперы разом.
Для этого применяется файл _ViewImports.cshtml.


Итак, добавим в проект в папку Views новый файл _ViewImports.cshtml:
![_ViewImports.cshtml в ASP.NET Core MVC и C#](https://metanit.com./pics/7.3.png)


В файле _ViewImports.cshtml определим подключение tag-хелперов:

```
@addTagHelper *, Microsoft.AspNetCore.Mvc.TagHelpers
```


После этого из представления Index.cshtml можно удалить подключение tag-хелперов и оставить только создание ссылки:

```
<a asp-controller="Home" asp-action="Contacts">Контакты</a>
```


Также мы можем конкретизировать применение хелперов к определенной группе представлений. Например, если у нас есть каталог Views/Home -
специально для представлений для контроллера HomeController,
и мы хотим применить только к ним определенные хелперы. В этом случае мы можем добавить файл _ViewImports.cshtml непосредственно в этот каталог.
И любой tag-хелпер, добавленный директивой `@addTagHelper` из файла Views/Home/_ViewImports.cshtml, будет применяться только к представлениям
из каталога Views/Home.


### Удаление tag-хелперов


Еще одна директива `removeTagHelper` удаляет ранее добавленные tag-хелперы. Ее применение аналогично:

```
@removeTagHelper "*, Microsoft.AspNetCore.Mvc.TagHelpers"
```


Данная директива может быть полезной, если мы, например, захотим ограничить применение хелперов в каком-то одном представлении или группе представлений.
Эту директиву также можно определять в файле _ViewImports.cshtml.











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

**Источник:** [https://metanit.com/sharp/aspnetmvc/7.1.php](https://metanit.com/sharp/aspnetmvc/7.1.php)
