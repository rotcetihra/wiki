# Добавление RazorPages в пустой проект

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по Razor Pages|Руководство по Razor Pages]] / [[Языки программирования/C#/Веб-разработка/Руководство по Razor Pages/Глава 1. Введение в Razor Pages|Глава 1. Введение в Razor Pages]] / Добавление RazorPages в пустой проект

[[Языки программирования/C#/Веб-разработка/Руководство по Razor Pages/Глава 1. Введение в Razor Pages/Первый проект в Visual Studio|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по Razor Pages/Глава 1. Введение в Razor Pages|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по Razor Pages/Глава 2. Основы Razor Pages/Определение страниц Razor|Вперёд]]

**Дата написания:** 05.09.2026

## Добавление RazorPages в пустой проект

Последнее обновление: 26.11.2023




-

-

-














Visual Studio предоставляет готовый шаблон для создания проекта Razor Pages. Однако иногда может возникнуть необходимость добавить функциональность Razor Pages в другие
типы проектов или вообще создать проект с нуля. Поэтому рассмотрим, как добавлять функциональность и страницы RazorPages в пустой проект ASP NET Core.
Если мы работаем в Visual Studio, то создадим по типу ASP NET Core Empty
![Добавление Razor Page в пустой проект ASP.NET Core и C#](https://metanit.com./pics/1.6.png)


Если мы работаем через .NET CLI, то создадим проект по типу webapp, выполнив в терминале команду

```
dotnet new webapp
```


После создания проекта первым делом подключим в него функциональность Razor Pages. Для этого откроем файл Program.cs. По умолчанию он имеет примерно
следующее содержимое:

```

var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.MapGet("/", () => "Hello World!");

app.Run();

```


Изменим его следующим образом:

```

var builder = WebApplication.CreateBuilder(args);

// добавляем в приложение сервисы Razor Pages
builder.Services.AddRazorPages();

var app = builder.Build();

// добавляем поддержку маршрутизации для Razor Pages
app.MapRazorPages();

app.Run();

```


### Добавление страницы Razor Page


Теперь добавим страницу Razor. И в начале определим в проекте папку Pages для хранения Razor Pages. Далее в эту папку добавим новую страницу Razor.


Если мы работаем в Visual Studio, то для добавления нажмем на данную папку правой кнопкой мыши и выберем в контекстном меню пункт Add -> New Item.
Далее среди шаблонов выберем шаблон Razor Page - Empty и назовем новый файл Index.cshtml:
![Создание Razor Page в ASP.NET Core и C#](https://metanit.com./pics/1.9.png)


После создания этой страницы в проект в папку Pages будут добавлены два файла - сама страница Index.cshtml и
связаный с ней файл кода Index.cshtml.cs.
![Страница Razor Page и файл связанного кода в ASP.NET Core и C#](https://metanit.com./pics/1.10.png)


Если мы НЕ работаем в Visual Studio, то надо в папке Pages создать текстовый файл `Index.cshtml`.


При добавлении в Visual Studio файл Index.cshtml по умолчанию выглядит следующим образом:

```

@page
@model RazorPagesApp.Pages.IndexModel
@{
}

```


Фактически это пустая страница. Директива @page указывает, что это страница Razor. А директива @model - в данном случае
это класс привязанного к странице кода IndexModel. Согласно условностям класс модели называется по имени страницы плюс суффикс "Model".


А файл Index.cshtml.cs при добавлении в Visual Studio содержит простейшее определение модели IndexModel:

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


В классе модели определен метод OnGet(). Этот метод обрабатывает GET-запросы. В данном случае он пуст. В реальности в данном случае он нам не понадобится.


В дальнейшем мы подробно разберем обработку запросов в Razor Pages. А пока определим на странице какое-нибудь простейшее содержимое. Для этого изменим файл
Index.cshtml следующим образом:

```

@page

<h2>Hello METANIT.COM!</h2>

```


Запустим проект. И нам отобразится определенный на странице заголовок:
![Первая программа на Razor Page в ASP.NET Core и C#](https://metanit.com./pics/1.11.png)











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

**Источник:** [https://metanit.com/sharp/razorpages/1.2.php](https://metanit.com/sharp/razorpages/1.2.php)
