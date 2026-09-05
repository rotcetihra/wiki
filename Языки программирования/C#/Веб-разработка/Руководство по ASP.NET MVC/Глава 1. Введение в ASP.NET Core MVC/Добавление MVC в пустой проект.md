# Добавление MVC в пустой проект

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC|Руководство по ASP.NET MVC]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 1. Введение в ASP.NET Core MVC|Глава 1. Введение в ASP.NET Core MVC]] / Добавление MVC в пустой проект

[[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 1. Введение в ASP.NET Core MVC/Первый проект на ASP.NET Core MVC в Visual Studio|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 1. Введение в ASP.NET Core MVC|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 2. Контроллеры/Контроллеры и их действия|Вперёд]]

**Дата написания:** 05.09.2026

## Добавление MVC в пустой проект

Последнее обновление: 13.11.2022




-

-

-














В прошлой теме был создан первый проект ASP.NET Core, который по умолчанию применяет паттерн MVC, но осталось за кадром, что именно заставляет паттерн MVC работать в проекте на ASP.NET Core.
Рассмотрим этот момент и чтобы лучше это понять, возьмем стандартный пустой проект ASP.NET, который по умолчанию никакой функциональности MVC в проект не подключает.
(Для этого можно либо в .NET CLI создадить проект с помощью команды `dotnet new web`, либо в Visual Studio создадать новый проект по типу ASP.NET Core Empty)
![Подключение MVC в пустой проект ASP.NET Core](https://metanit.com./pics/1.6.png)


Допустим, в моем случае проект называется MvcApp. По умолчанию создается примитивный проект ASP.NET Core, в котором файл Program.cs стандартный код:

```

var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.MapGet("/", () => "Hello World!");

app.Run();

```


Теперь задействуем функциональность фреймворка MVC в нашем приложении и изменим файл Program.cs следующим образом:

```

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddControllersWithViews(); // добавляем сервисы MVC

var app = builder.Build();

// устанавливаем сопоставление маршрутов с контроллерами
app.MapControllerRoute(
 name: "default",
 pattern: "{controller=Home}/{action=Index}/{id?}");

app.Run();

```


Прежде всего надо отметить, что функциональность MVC, в частности, поддержка контроллеров и представлений, подключается в приложение в виде сервиса - в данном случае
с помощью вызова `services.AddControllersWithViews()`. После этого мы можем использовать функциональность фреймворка MVC.


Кроме того, чтобы связать приходящие от пользователей запросы с контроллерами применяется метод `MapControllerRoute()`.
Через перевый параметр - name в метод передается название маршрута - в данном случае "default". Через второй параметр - параметр pattern передается шаблон маршрута,
которому должен соответствовать запрос. В качестве шаблона маршрута применяется шаблон "{controller=Home}/{action=Index}/{id?}",
который представляет трехсегментный запрос. В нем первый сегмент представляет контроллер, второй сегмент - метод контроллера, а третий - необязательный параметр.
При этом если в запросе не указаны сегменты (например, обращение идет к корню веб-приложения), то в качестве контроллера по умолчанию применяется HomeController, а в качестве
его метода - метод Index.


### Добавление контроллера


Теперь добавим в проект для хранения контроллеров папку Controllers. И затем в нее добавим новый класс, который назовем HomeController и который
будет иметь следующий код:

```

using Microsoft.AspNetCore.Mvc;

namespace MvcApp.Controllers
{
 public class HomeController : Controller
 {
 public IActionResult Index()
 {
 return View();
 }
 }
}

```


Контроллер наследуется от класса Controller и в данном случае он имеет один метод Index, который с помощью метода
View обращается к представлению.


### Добавление представления


Теперь добавим в проект папку Views, которая будет хранить представления. В эту папку вначале добавим каталог Home - каталог, предназначенный непосредственно для представлений
контроллера Home. И в конце добавим в каталог Views/Home новый элемент по типу Razor View (Empty), который назовем Index.cshtml.
![Добавление представление в проект Mvc в ASP NET Core](https://metanit.com./pics/1.7.png)


Определим в этом файле следующий код:

```

@{
 Layout = null;
}
<!doctype html>
<html>
<head>
 <title>METANIT.COM</title>
 <meta charset="utf-8" />
</head>
<body>
 <h2>Hello METANIT.COM!</h2>
</body>
</html>

```


Это простейшее представление, которое будет использоваться методом Index контроллера HomeController. То есть в итоге у нас получится следующая структра проекта:
![Первый проект c ASP.NET Core MVC в C#](https://metanit.com./pics/1.8.png)


Теперь запустим приложение на выполнение, и браузер выведет сообщение, определенное в представлении Index.cshtml:
![запуск проекта на ASP.NET Core MVC и C#](https://metanit.com./pics/1.9.png)


Таким образом мы можем добавлять функциональность MVC в свой проект. Однако, как правило, для работы с MVC используется шаблон ASP.NET Core Web App (Model-View-Controller), который по умолчанию содержит некоторую
базовую функциональность.


### Сервисы MVC


Функциональность MVC и ее работа в приложении зависит от добавляемых сервисов. В примере выше мы использовали метод `AddControllersWithViews()` для добавления сервисов MVC,
благодаря чему система маршрутизации смогла связать запрос с контроллером. Однако в данном случае у нас есть ряд опций по встраиванию сервисов,
которые мы можем при необходимости использовать:


-

AddMvc(): добавляет все сервисы фреймворка MVC (в том числе сервисы для работы с аутентификацией и авторизацией, валидацией и т.д.)

-

AddMvcCore(): добавляет только основные сервисы фреймворка MVC, а всю дополнительную функциональность, типа
аутентификацией и авторизацией, валидацией и т.д., необходимо добавлять самостоятельно

-

AddControllersWithViews(): добавляет только те сервисы фреймворка MVC, которые позволяют использовать контроллеры и представления и связанную функциональность.
При создании проекта по типу ASP.NET Core Web App (Model-View-Controller) используется именно этот метод

-

AddControllers(): позволяет использовать контроллеры, но без представлений.


И в зависимости от того, насколько широко нам надо использовать возможности фреймворка MVC, выбирается соответствующий метод. Например, в примере выше мы могли бы использовать
вместо вызова `AddControllersWithViews()` метод `AddMvc()`.










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

**Источник:** [https://metanit.com/sharp/aspnetmvc/1.3.php](https://metanit.com/sharp/aspnetmvc/1.3.php)
