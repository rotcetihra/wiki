# HTML-хелперы элементов форм

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC|Руководство по ASP.NET MVC]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 6. HTML-хелперы|Глава 6. HTML-хелперы]] / HTML-хелперы элементов форм

[[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 6. HTML-хелперы/Создание HTML-хелперов|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 6. HTML-хелперы|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 6. HTML-хелперы/Строго типизированные хелперы|Вперёд]]

**Дата написания:** 05.09.2026

## HTML-хелперы элементов форм

Последнее обновление: 29.03.2022




-

-

-














Хотя мы можем создать любой необходимый хелпер, но в большинстве случаев нам не придется писать свои хелперы,
потому что фреймворк MVC уже предоставляет большой набор встроенных html-хелперов, которые позволяют генерировать ту или иную разметку, например, код элеметов форм.


### Хелпер Html.BeginForm


Пусть в контроллере определены две версии одного метода Create- для методов POST и GET, например:

```

[HttpGet]
public IActionResult Create() => View();

[HttpPost]
public string Create(string name, int age) => $"{name} - {age}";

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
@Html.TextBox("Age","", new { type="number" })
```


В качестве второго параметра устанавливает значение по умолчанию (здесь пустая строка). Третий параметр в виде анонимного объекта позволяет задать
ряд атрибутов генерируемого html-элемента. Так, в данном случае мы указываем, что поле будет числовое, так как по умолчанию создаваемое поле расценивается как текстовое, то есть
с атрибутом `type="text"`.


В итоге мы получим практически аналогичный результат:
![текстовые поля в asp.net core mvc и c#](https://metanit.com./pics/6.2.png)


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

```
@Html.Password("UserPassword", "val")
```


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

![Html.RadioButton в ASP.NET Core MVC и C#](https://metanit.com./pics/6.3.png)


#### Html.CheckBox


`Html.CheckBox` применяется для создания элемента флажка или checkbox. Например, следующий код:

```
@Html.CheckBox("Enable", false)
```


будет генерировать следующий HTML:

```

<input id="Enable" name="Enable" type="checkbox" value="true">

```


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

<select id="user" name="user"><option value="">Выберите пользователя</option>
<option>Tom</option>
<option>Sam</option>
<option>Bob</option>
<option>Alice</option>
</select>

```


Объект `SelectListItem` имеет свойства `Text` (отображаемый текст), `Value` (само значение, которое может не
совпадать с текстом) и `Selected`. Теперь более сложный пример. Выведем в список коллекцию элементов User:

```

public record class User(int Id, string Name, int Age);

```


В контроллере передадим список объектов User через ViewBag:

```

public IActionResult Create()
{
 var users = new List<User>
 {
 new User(1, "Tom", 37),
 new User(2, "Alice", 33),
 new User(3, "Sam", 28),
 new User(4, "Bob", 41),
 };
 ViewBag.Users = new Microsoft.AspNetCore.Mvc.Rendering.SelectList(users, "Id", "Name");
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

using System.ComponentModel.DataAnnotations; // для атрибута Display

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

```


Тогда в представлении мы сможем вывести выпадающий список значений из этого перечисления:

```

@using MvcApp

@using (Html.BeginForm("Create", "Home", FormMethod.Post))
{
 @Html.DropDownList("daytime", Html.GetEnumSelectList(typeof(TimeOfDay)))
 <br />
 <p>
 <input type="submit" value="Отправить" />
 </p>
}

```

![Список из enum в ASP.NET Core MVC и C#](https://metanit.com./pics/6.4.png)











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

**Источник:** [https://metanit.com/sharp/aspnetmvc/6.2.php](https://metanit.com/sharp/aspnetmvc/6.2.php)
