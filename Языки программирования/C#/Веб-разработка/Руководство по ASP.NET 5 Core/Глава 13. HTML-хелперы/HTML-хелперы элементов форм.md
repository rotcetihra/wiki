# HTML-хелперы элементов форм

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET 5 Core|Руководство по ASP.NET 5 Core]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET 5 Core/Глава 13. HTML-хелперы|Глава 13. HTML-хелперы]] / HTML-хелперы элементов форм

[[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET 5 Core/Глава 13. HTML-хелперы/Создание HTML-хелперов|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET 5 Core/Глава 13. HTML-хелперы|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET 5 Core/Глава 13. HTML-хелперы/Строго типизированные хелперы|Вперёд]]

**Дата написания:** 05.09.2026

## HTML-хелперы элементов форм


Данное руководство устарело. Актуальное руководство: [Руководство по ASP.NET Core 7](https://metanit.com/sharp/aspnet6/)Последнее обновление: 30.11.2019




-

-

-














Хотя мы можем создать любой необходимый хелпер, но в большинстве случаев нам не придется писать свои хелперы,
потому что фреймворк MVC уже предоставляет большой набор встроенных html-хелперов, которые позволяют генерировать ту или иную разметку, например, код элеметов форм.


### Хелпер Html.BeginForm


Пусть в контроллере определены две версии одного метода Create- для методов POST и GET, например:

```

[HttpGet]
public IActionResult Create()
{
 return View();
}
[HttpPost]
public IActionResult Create(string name, int age)
{
 return Content($"{name} - {age}");
}

```


В представлении для метода Create для создания формы ввода данных для последующей их отправки на post-версию метода Create
мы вполне можем использовать стандартные элементы html, например:

```

<form method="post" action="~/Home/Create">
 <p>
 <label>Имя</label><br />
 <input type="text" name="name" />
 </p>
 <p>
 <label>Возраст</label><br />
 <input type="number" name="age" />
 </p>
 <p>
 <input type="submit" value="Отправить" />
 </p>
</form>

```


Это обычная html-форма, которая по нажатию на кнопку отправляет все введенные данные запросом POST на адрес /Home/Create.
Встроенный хелпер BeginForm/EndForm позволяет создать ту же самую форму:

```

@using(Html.BeginForm("Create", "Home", FormMethod.Post))
{
 <p>
 <label>Имя</label><br />
 <input type="text" name="name" />
 </p>
 <p>
 <label>Возраст</label><br />
 <input type="number" name="age" />
 </p>
 <p>
 <input type="submit" value="Отправить" />
 </p>
}

```


Метод BeginForm принимает в качестве параметров имя метода действия и имя контроллера, а также тип запроса.
Данный хелпер создает как открывающий тег `<form>`, так и закрывающий тег `</form>`. Поэтому при рендеринге представления в
выходной поток у нас получится тот же самый html-код, что и с применением тега form. Поэтому оба способа идентичны.


Но вызов страницы с формой и отправка формы осуществляется одним и тем же действием (как в нашем случае действием Create), то в этом случае можно не указывать в
хелпере `Html.BeginForm` параметры:

```

@using(Html.BeginForm())
{
 .............
}

```


### Ввод информации


В предыдущем примере вместе с хелпером Html.BeginForm использовались стандартные элементы html. Однако набор html-хелперов содержит также
хелперы для ввода информации пользователем. В MVC определен широкий набор хелперов ввода практически для каждого html-элемента. Что выбрать -
хелпер или стандартный элементы ввода html, уже решает сам разработчик.


Вне зависимости от типа все базовые html-хелперы используют как минимум два параметра: первый параметр применяется для установки значений
для атрибутов `id` и `name`, а второй параметр - для установки значения атрибута `value`


#### Html.TextBox


Хелпер `Html.TextBox` генерирует тег `input` со значением атрибута `type` равным `text`.
Хелпер `TextBox` используют для получения ввода пользователем информации. Так, перепишем предыдущую форму с заменой полей ввода на хелпер
Html.TextBox:

```

@using (Html.BeginForm("Create", "Home", FormMethod.Post))
{
 <p>
 <label>Имя</label><br />
 @Html.TextBox("Name")
 </p>
 <p>
 <label>Возраст</label><br />
 @Html.TextBox("Age","", new { type="number" })
 </p>
 <p>
 <input type="submit" value="Отправить" />
 </p>
}

```


Хелпер позволяет установить ряд дополнительных параметров с помощью перегружженных версий. Так, вызов хелпера:

```
@Html.TextBox("Price","", new { type="number" })
```


В качестве второго параметра устанавливает значение по умолчанию (здесь пустая строка). Третий параметр в виде анонимного объекта позволяет задать
ряд атрибутов генерируемого html-элемента. Так, в данном случае мы указываем, что поле будет числовое, так как по умолчанию создаваемое поле расценивается как текстовое, то есть
с атрибутом `type="text"`.


В итоге мы получим практически аналогичный результат:
![текстовые поля в asp.net core](https://metanit.com./pics/htmlhelper2.png)


#### Html.Label


Хелпер `Html.Label` создает элемент `<label/>`, а передаваемый в хелпер параметр определяет значение атрибута
`for` и одновременно текст на элементе. Перегруженная версия хелпера позволяет определить значение атрибута `for` и
текст на метке независимо друг от друга. Например, объявление хелпера `Html.Label("Name", "Имя")` создает следующую разметку:

```
<label for="Name">Имя</label>
```


Элемент `label` представляет простую метку, предназначенную для прикрепления информации к элементам ввода, например, к текстовым полям.
Атрибут `for` элемента `label` должен содержать id ассоциированного элемента ввода. Если пользователь нажимает на
метку, то браузер автоматически передает фокус связанному с этой меткой элементу ввода.


#### Html.TextArea


Хелпер `TextArea` используется для создания элемента
`<textarea>`, который представляет многострочное текстовое поле. Результатом выражения `@Html.TextArea("text", "привет мир")`


будет следующая html-разметка:

```

<textarea cols="20" id="text" name="text" rows="2">привет мир
</textarea>

```


Обратите внимание, что хелпер декодирует помещаемое в него значение, в том числе и html-теги, (все хелперы декодируют значения моделей
и значения атрибутов). Другие версии хелпера `TextArea` позволяют указать число строк и столбцов, определяющих размер текстового поля.

```
@Html.TextArea("text", "привет мир", 5, 50, null)
```


Этот хелпер сгенерирует следующую разметку:

```
<textarea cols="50" id="text" name="text" rows="5">привет мир</textarea>
```


#### Html.Hidden


Хелпер Html.Hidden генерирует скрытое поле. Например, следующий вызов хелпера:


`@Html.Hidden("UserId", "2")`


сгенерирует разметку:

```

<input id="UserId" name="UserId" type="hidden" value="2" />

```


#### Html.Password


`Html.Password` создает поле для ввода пароля. Он похож на хелпер `TextBox`, но вместо
введенных символов отображает маску пароля. Следующий код:


`@Html.Password("UserPassword", "val")`


генерирует разметку:

```

<input id="UserPassword" name="UserPassword" type="password" value="val" />

```


#### Html.RadioButton


Для создания переключателей применяется хелпер `Html.RadioButton`. Он генерирует элемент `input` со значением `type="radio"`.
Для создания группы переключателей, надо присвоить всем им одно и то же имя (свойство `name`):

```

@Html.RadioButton("color", "red")
<span>красный</span> <br />
@Html.RadioButton("color", "blue")
<span>синий</span> <br />
@Html.RadioButton("color", "green", true)
<span>зеленый</span>

```


Этот код создает следующую разметку:

```

<input id="color" name="color" type="radio" value="red" />
<span>красный</span> <br />
<input id="color" name="color" type="radio" value="blue" />
<span>синий</span> <br />
<input checked="checked" id="color" name="color" type="radio" value="green" />
<span>зеленый</span>

```

![Html.RadioButton в ASP.NET Core](https://metanit.com./pics/htmlhelper3.png)


#### Html.CheckBox


`Html.CheckBox` применяется для создания элемента флажка или checkbox. Например, следующий код:

```
@Html.CheckBox("Enable", false)
```


будет генерировать следующий HTML:

```

<input id="Enable" name="Enable" type="checkbox" value="true">
<input name="Enable" type="hidden" value="false">

```


Фактически создается два элемента - собственно флажок и скрытое поле, которое обычно помещается в конец формы и используется для отслеживания изменений значения флажка.


#### Html.DropDownList


Хелпер Html.DropDownList создает выпадающий список, то есть элемент `<select />`.
Для генерации такого списка нужна коллекция объектов `SelectListItem`, которые представляют элементы списка.
Можно создать коллекцию объектов `SelectListItem` или использовать хелпер `SelectList`. Этот хелпер просматривает объекты
`IEnumerable` и преобразуют их в последовательность объектов `SelectListItem`.
Так, следующий код:

```

@Html.DropDownList("user", new SelectList(new string[] { "Tom", "Sam", "Bob", "Alice" }), "Выберите пользователя")

```

генерирует следующую разметку:

```

<select id="phone" name="phone"><option value="">Выберите пользователя</option>
<option>Tom</option>
<option>Sam</option>
<option>Bob</option>
<option>Alice</option>
</select>

```


Объект `SelectListItem` имеет свойства `Text` (отображаемый текст), `Value` (само значение, которое может не
совпадать с текстом) и `Selected`. Теперь более сложный пример. Выведем в список коллекцию элементов User:

```

public class User
{
 public int Id { get; set; }
 public string Name { get; set; }
 public int Age { get; set; }
}

```


В контроллере передадим список объектов User через ViewBag:

```

public IActionResult Create()
{
 List<User> users = new List<User>
 {
 new User {Id=1, Name="Tom", Age=35 },
 new User {Id=2, Name="Alice", Age=29 },
 new User {Id=3, Name="Sam", Age=36 },
 new User {Id=4, Name="Bob", Age=31 },
 };
 ViewBag.Users = new SelectList(users, "Id", "Name");
 return View();
}

```


Здесь мы создаем объект SelectList, передавая в его конструктор набор значений (список users), название свойства модели User,
которое будет использоваться в качестве значения (Id), и название свойства модели User, которое будет использоваться для отображения в списке.
В данном случае необязательно устанавливать два разных свойства, можно было и одно установить и для значения и отображения.


Тогда в представлении мы можем так использовать этот SelectList:

```

@Html.DropDownList("userid", ViewBag.Users as SelectList)

```


И при рендеринге представления все элементы SelectList добавятся в выпадающий список


#### Html.ListBox


Хелпер `Html.ListBox`, также как и `DropDownList`, создает элемент `<select />`,
но при этом делает возможным множественное выделение элементов (то есть для атрибута `multiple` устанавливается значение `multiple`).
Для создания списка, поддерживающего множественное выделение, вместо `SelectList` можно использовать класс `MultiSelectList`:

```

@Html.ListBox("users", new MultiSelectList(new string[] { "Tom", "Sam", "Bob", "Alice" }))

```


Этот код генерирует следующую разметку:

```

<select id="users" multiple="multiple" name="users">
<option>Tom</option>
<option>Sam</option>
<option>Bob</option>
<option>Alice</option>
</select>

```


#### Html.GetEnumSelectList


Для создания выпадающего списка по перечислению применяется хелпер Html.GetEnumSelectList. Допустим, у нас есть следующее перечисление:

```

using System.ComponentModel.DataAnnotations;

namespace HtmlHelpersApp.App_Code
{
 public enum TimeOfDay
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
}

```


Тогда в представлении мы сможем вывести выпадающий список значений из этого перечисления:

```

@using HtmlHelpersApp.App_Code

@using (Html.BeginForm("Create", "Home", FormMethod.Post))
{
 @Html.DropDownList("daytime", Html.GetEnumSelectList(typeof(TimeOfDay)))
 <br />
 <p>
 <input type="submit" value="Отправить" />
 </p>
}

```

![Список из enum в ASP.NET Core](https://metanit.com./pics/htmlhelper4.png)










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

**Источник:** [https://metanit.com/sharp/aspnet5/9.2.php](https://metanit.com/sharp/aspnet5/9.2.php)
