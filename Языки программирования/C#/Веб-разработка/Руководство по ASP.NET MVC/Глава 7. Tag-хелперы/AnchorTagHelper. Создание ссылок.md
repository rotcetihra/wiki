# AnchorTagHelper. Создание ссылок

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC|Руководство по ASP.NET MVC]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 7. Tag-хелперы|Глава 7. Tag-хелперы]] / AnchorTagHelper. Создание ссылок

[[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 7. Tag-хелперы/Введение в tag-хелперы|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 7. Tag-хелперы|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 7. Tag-хелперы/LinkTagHelper и ScriptTagHelper|Вперёд]]

**Дата написания:** 05.09.2026

## AnchorTagHelper

Последнее обновление: 03.04.2022




-

-

-














AnchorTagHelper представляет тег-хелпер, который позволяет создавать ссылки. Он может принимать ряд специальных атрибутов:


-

asp-controller: указывает на контроллер, которому предназначен запрос

-

asp-action: указывает на действие контроллера

-

asp-area: указывает на действие область, в которой расположен контроллер или страница RazorPage (если они находятся в отдельной области)

-

asp-page: указывает на RazorPage, которая будет обрабатывать запрос

-

asp-page-handler: указывает на обработчик страницы RazorPage, которая будет применяться для обработки запроса

-

asp-host: указывает на домен сайта

-

asp-protocol: определяет протокол (http или https)

-

asp-route: указывает на название маршрута

-

asp-all-route-data: устанавливает набор значений для параметров

-

asp-route-[название параметра]: определяет значение для определенного параметра

-

asp-fragment: определяет ту часть хэш-ссылки, которая идет после символа решетки #. Например, "paragraph2" в ссылке
"http://mysite.com/#paragraph2"


### asp-action и asp-controller


Мы можем создавать ссылки в ASP.NET Core различными способами. Например:

```

@Html.ActionLink("О сайте","About","Home")
<a href='@Url.Action("About", "Home")'>О сайте</a>

```


В первом случае используется html-хелпер, во втором - стандартный элемент ссылки с хелпером Url.Content. Еще один способ предоставляют
tag-хелпер AnchorTagHelper:

```

<a asp-controller="Home" asp-action="About">О сайте</a>

```


В данном случае используется не элемент html `<a />`, а именно хелпер AnchorTagHelper. Его атрибут
asp-controller указывает на название контроллера, а asp-action
определяет действие, которому будет идти запрос. Если указан атрибут `asp-action`, но не указан `asp-controller`, то в качестве
контроллера используется тот контроллер, который связан с текущим представлением.


Если необходимо установить ссылку на действие контроллера, который находится в другой области, то применяется атрибут asp-area:

```
<a asp-controller="Home" asp-action="About" asp-area="Service">О сайте</a>
```


В данном случае предполагается, что контроллер Home находится в области Service.


Если, наоборот, в представлении, которое находится в какой-нибудь области, надо создать ссылку на действие контроллера, который не находится ни в какой области, то указывается пустой атрибут:

```
<a asp-controller="Home" asp-action="About" asp-area="">О сайте</a>
```


### asp-host и asp-protocol


AnchorTagHelper по умолчанию создает локальную ссылку, если же нам надо создать ссылку на другой домен, то мы можем применить атрибут asp-host:

```

<a asp-controller="Home" asp-action="About" asp-host="localhost.com" asp-protocol="https">О сайте</a>

```


Кроме того, мы можем изменить стандартный протокол на https, использовав атрибут asp-protocol.
Данный элемент в итоге создает следующую ссылку: https://localhost.com/Home/About


### asp-route- и asp-all-route-data


А что если у нас метод принимает какие-нибудь параметры, которые надо указать в ссылке:

```

public string GetPerson(int id) => $"Id: {id}";

```


В этом случае мы можем использовать атрибут asp-route-:

```

<a asp-controller="Home" asp-action="GetPerson" asp-route-id="5" >Person 5</a>

```


Если метод принимает несколько параметров, например:

```

public string GetPerson(int id, string name, int age) => $"id={id} name={name} age={age}";

```


то мы можем указать несколько атрибутов `asp-route-`:

```

<a asp-controller="Home" asp-action="GetPerson" asp-route-id="5" asp-route-age="18" asp-route-name="tom" >Person 5</a>

```


Чтобы не устанавливать все параметры по отдельности, можно применить атрибут asp-all-route-data:

```

<a asp-controller="Home" asp-action="GetPerson" asp-all-route-data='new Dictionary<string,string> { { "id", "5" }, {"name", "tom" }, { "age", "18" } }' >Person 5</a>

```


`asp-all-route-data` в качестве значения принимает словарь с параметрами и их значениями. В результате будет генерироваться
ссылка, аналогичная предыдущей.


### Влияние системы маршрутизации


При использовавании данного тег-хелпера может возникнуть вопрос, а какая именно ссылка будет сгенерирована? В реальности ответ на этот вопрос зависиот системы маршрутизации.
Например, по умолчанию в проекте определен один маршрут (в файле Program.cs):

```

app.MapControllerRoute(
 name: "default",
 pattern: "{controller=Home}/{action=Index}/{id?}");

```


Возьмем предпоследний пример:

```

<a asp-controller="Home" asp-action="GetPerson" asp-route-id="5" asp-route-age="18" asp-route-name="tom" >Person 5</a>

```


В итоге будет создаваться следующая ссылка: http://localhost:1234/Home/GetPerson/5?name=tom&age=18. Обратите внимание,
что параметр id является частью шаблона маршрута, поэтому в сгенерированной ссылке он не входит строку запроса.


Если мы немного изменим определение маршрута, убрав сегмент параметра id:

```

app.MapControllerRoute(
 name: "default",
 pattern: "{controller=Home}/{action=Index}");

```


То параметр id будет трактоваться как часть строки запроса: http://localhost:60141/Home/GetPerson?id=5&name=tom&age=18


Но это только одна из частностей. Возьмем другой пример. Допустим, в файле Program.cs определено несколько маршрутов:

```

app.MapControllerRoute(
 name: "products",
 pattern: "Products/{action}/{id?}",
 defaults: new { controller = "Home" });

app.MapControllerRoute(
 name: "default",
 pattern: "{controller=Home}/{action=Index}/{id?}");

```


Первым здесь установлен маршрут "products", который будет сопоставлять запросы к контроллеру Home с маршрутом "Products/{action}/{id?}". В частности,
запрос http://localhost:xxxxx/Products/Index будет обрабатываться методом Index контроллера Home.


И теперь следующий тег

```

<a asp-controller="Home" asp-action="Index">Жми здесь</a>

```


сгенерирует следующую ссылку

```
<a href="/Products/Index">Жми здесь</a>
```


И не смотря на то, что у нас также определен стандартный маршрут, который позволяет генерировать стандартные ссылки, включающие имя контроллера и имя его метода,
но в данном случае для генерации ссылок будет применяться первый маршрут, который совпадает с определением ссылки.


Но возьмем чуть более сложную систему маршрутов:

```

app.MapControllerRoute(
 name: "default",
 pattern: "BookStore",
 defaults: new { controller = "Book", action = "Index" });
app.MapControllerRoute(
 name: "default1",
 pattern: "Store/Sub{action}/{id?}",
 defaults: new { controller = "Home" });

app.MapControllerRoute(
 name: "default2",
 pattern: "{controller=Home}/{action=Index}/{id?}");

```


Из определения маршрутов ясно, то запрос http://localhost:xxxxx/BookStore будет обрабатываться методом Index контроллера Book.
А запрос http://localhost:xxxxx/Store/SubIndex/ будет обрабатываться контроллером Home и его методом Index.


Теперь пусть у нас в представлении создаются две ссылки:

```

<p>
 <a asp-controller="Home" asp-action="Index">Home</a>
</p>
<p>
 <a asp-controller="Book" asp-action="Index">Book</a>
</p>

```


Первая ссылка соответствует второму маршруту, так как для определения ссылки используется контроллер Home. Поэтому в соответствии со вторым маршрутом будет сгенерирована
следующая ссылка:

```
http://localhost:xxxxx/Store/SubIndex
```


Вторая же ссылка соответствует первому маршруту, который для обработки запроса применяет контроллер BookController. Поэтому второе выражение сгенерирует следующую ссылку:

```
http://localhost:xxxxx/BookStore
```


Поэтому если в приложении определено несколько маршрутов, то следует учитывать систему маршрутизации и проверять сгенерированные ссылки, иначе в результате можно получить совсем не то, что ожидалось.


### asp-route


С помощью параметра `asp-route` можно сгенерировать ссылку на основании маршрута. Например, пусть у нас есть такой маршрут:

```

app.MapControllerRoute(
 name: "book",
 pattern: "BookStore",
 defaults: new { controller = "Book", action = "Index" });

app.MapControllerRoute(
 name: "default",
 pattern: "{controller=Home}/{action=Index}/{id?}");

```


Возьмем первый маршрут по имени "book":

```
<a asp-route="book">Книги</a>
```


Такой тег создаст следующую ссылку:

```
<a href="/BookStore">Книги</a>
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

**Источник:** [https://metanit.com/sharp/aspnetmvc/7.2.php](https://metanit.com/sharp/aspnetmvc/7.2.php)
