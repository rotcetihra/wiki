# Передача данных на страницу Razor в GET-запросе

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по Razor Pages|Руководство по Razor Pages]] / [[Языки программирования/C#/Веб-разработка/Руководство по Razor Pages/Глава 2. Основы Razor Pages|Глава 2. Основы Razor Pages]] / Передача данных на страницу Razor в GET-запросе

[[Языки программирования/C#/Веб-разработка/Руководство по Razor Pages/Глава 2. Основы Razor Pages/Обработка запросов. Контекст страницы Razor|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по Razor Pages/Глава 2. Основы Razor Pages|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по Razor Pages/Глава 2. Основы Razor Pages/POST-запросы и отправка форм|Вперёд]]

**Дата написания:** 05.09.2026

## Передача данных на страницу Razor в GET-запросе

Последнее обновление: 15.04.2022




-

-

-














В get-запросе также можно передать на страницу данные. Распространенным способом передачи данных в GET-запросе представляет строка запроса.
Строка запроса представляет ту часть адреса, которая идет после знака вопроса ? и представляет набор параметров, где каждый параметр отделен от другого с помощью амперсанда:

```
название_ресурса?параметр1=значение1&параметр2=значение2
```


Например, в адресе:

```
https://localhost:7085/Index?name=Tom&age=37
```


часть ?name=Tom&age=37 как раз представляет строку запроса, которая содержит два параметра: name и age. Значение параметра name - "Tom", а значение параметра age - 37.


Например, у нас есть страница Razor Index.cshtml и код связанной модели IndexModel в файле Index.cshtml.cs:
![OnGet и OnPost в Razor Page в ASP.NET Core и C#](https://metanit.com./pics/2.13.png)


Передадим в страницу Index.cshtml через строку запроса данные для параметра name. Для этого определим следующую модель IndexModel:

```

using Microsoft.AspNetCore.Mvc.RazorPages;

namespace RazorPagesApp.Pages
{
 public class IndexModel : PageModel
 {
 public string Message { get; private set; } = "";
 public void OnGet(string name)
 {
 Message = $"Name: {name}";
 }
 }
}

```


А на странице Index.cshtml выведем значение свойства Message модели:

```

@page

@model RazorPagesApp.Pages.IndexModel
<h2>@Model.Message</h2>

```

![Передача значений для параметров метода контроллера через строку запроса в Razor Pages ASP.NET Core и C#](https://metanit.com./pics/2.15.png)


То есть в данном случае при обращении к методу Index с запросом `https://localhost:7085/Index?name=Eugene` параметру name будет передаваться значение "Eugene".


Система привязки по умолчанию сопоставляет параметры запроса и параметры метода по имени. То есть, если в строке запроса
идет параметр `name`, то его значение будет передаваться именно параметру метода, который также называется `name`. При этом должно быть также
соответствие по типу, то есть если параметр метода принимает числовое значение, то и через строку запроса надо передавать для этого параметра число, а не строку.


Подобным образом можно передать значения для нескольких параметров. Например, изменим модель IndexModel следующим образом:

```

using Microsoft.AspNetCore.Mvc.RazorPages;

namespace RazorPagesApp.Pages
{
 public class IndexModel : PageModel
 {
 public string Message { get; private set; } = "";
 public void OnGet(string name, int age)
 {
 Message = $"Name: {name} Age: {age}";
 }
 }
}

```


В этом случае мы можем обратиться к действию, набрав в адресной строке https://localhost:7085?name=Tom&age=37.
![Передача значений в действия контроллера через строку запроса в ASP.NET Core Razor Pages и C#](https://metanit.com./pics/2.16.png)


Если же мы не используем параметры в строке запроса, то мы можем использовать параметры по умолчанию, которые будут работать,
если через строку запроса не передается никаких параметров:

```

using Microsoft.AspNetCore.Mvc.RazorPages;

namespace RazorPagesApp.Pages
{
 public class IndexModel : PageModel
 {
 public string Message { get; private set; } = "";
 public void OnGet(string name = "Bob", int age = 33)
 {
 Message = $"Name: {name} Age: {age}";
 }
 }
}

```


Например, при отправке запроса https://localhost:7085/Index?age=41 параметр name будет иметь значение по умолчанию.
![Значения по умолчанию в методе OnGet в ASP.NET Core Razor Pages и C#](https://metanit.com./pics/2.17.png)


Подобным образом можно получать данные из строки запроса непосредственно на странице Index.cshtml

```

@page

<h2>@Message</h2>

@functions {
 public string Message { get; set; } = "";
 public void OnGet(string name, int age)
 {
 Message = $"Name: {name} Age: {age}";
 }
}

```


### Передача сложных объектов


Хотя строка запроса преимущественно используется для передачи данных примитивных типов, но мы также можем принимать более сложные объекты.
Например, определим рядом с моделью класс Person:

```

using Microsoft.AspNetCore.Mvc.RazorPages;

namespace RazorPagesApp.Pages
{
 public class IndexModel : PageModel
 {
 public string Message { get; private set; } = "";
 public void OnGet(Person person)
 {
 Message = $"Person {person.Name} ({person.Age})";
 }
 }
 public record class Person(string Name, int Age);
}

```


Класс Person определяет два свойства: Name и Age. И в модели IndexModel метод OnGet принимает параметр типа Person. В этом случае значения через строку запроса
передаются как и в предыдущем случае. При этом параметры строки запроса должны соответствовать по имени свойствам объекта. Регистр названий параметров при этом не учитывается:
![Передача сложных объектов в метод OnGet в Razor Pages в ASP.NET Core и C#](https://metanit.com./pics/2.18.png)


### Передача массивов


Допустим, метод OnGet принимает массив строк-имен:

```

using Microsoft.AspNetCore.Mvc.RazorPages;

namespace RazorPagesApp.Pages
{
 public class IndexModel : PageModel
 {
 public string Message { get; private set; } = "";
 public void OnGet(string[] people)
 {
 string result = "";
 foreach (var person in people)
 result = $"{result}{person}; ";
 Message = result;
 }
 }
}

```


Для передачи методу данных через строку запроса применяется название параметра:

```
https://localhost:7085/?people=Tom&people=Bob&people=Sam
```

![Передача массивов на страницу Razor Pages в ASP.NET Core и C#](https://metanit.com./pics/2.19.png)


Можно явным образом указать индексы элементов:

```
https://localhost:7085/?people[0]=Tom&people[2]=Bob&people[1]=Sam
```


Можно просто ограничиться индексами:

```
https://localhost:7085/?[0]=Tom&[2]=Bob&[1]=Sam
```


### Передача массивов сложных объектов


Подобным образом можно принимать массивы сложных объектов. Например, определим следующую модель IndexModel, которая в методе Onget принимает массив объектов некоторого класса Person:

```

using Microsoft.AspNetCore.Mvc.RazorPages;

namespace RazorPagesApp.Pages
{
 public class IndexModel : PageModel
 {
 public string Message { get; private set; } = "";
 public void OnGet(Person[] people)
 {
 string result = "";
 foreach (Person person in people)
 {
 result = $"{result} {person.Name}; ";
 }
 Message = result;
 }
 }
 public record class Person(string Name, int Age);
}

```


И чтобы передать в этот метод данные, нам надо использовать запрос типа

```
https://localhost:7085/?people[0].name=Tom&people[0].age=37&people[1].name=Bob&people[1].age=41
```


В этом случае в массиве people будут два объекта Person.


Также можно опустить название параметра и оставить только индексы:

```
https://localhost:7085/?[0].name=Tom&[0].age=37&[1].name=Bob&[1].age=41
```


### Передача словарей Dictionary


Передача в метод словарей аналогично передаче массивов, только у передаваемых элементов необходимо установить ключ. Например, пусть метод OnGet получает в качестве параметра объект Dictionary:

```

public void OnGet(Dictionary<string,string> items)
{
 string result = "";
 foreach (var item in items)
 {
 result = $"{result} {item.Key} - {item.Value}; ";
 }
 Message = result;
}

```


Для отправки данных мы можем использовать строку запроса:

```
https://localhost:7085/?items[germany]=berlin&items[france]=paris&items[spain]=madrid
```


Каждый отдельный элемент этой строки типа `items[germany]=berlin` будет представлять элемент словаря, где `items` - название
словаря, "germany" - ключ, а "berlin" - значение.


### Объект Request.Query


Параметры представляют самый простой способ получения данных, но в действительности нам необязательно их использовать. На странице и в ее модели доступен объект Request,
у которого можно получить как данные строки запроса через свойство Request.Query. Это свойство представляет объект `IQueryCollection`, где по
ключу - названию параметра можно получить его значение. Например:

```

public void OnGet()
{
 string name = Request.Query["name"];
 string age = Request.Query["age"];
 Message = $"Name: {name} Age: {age}";
}

```


В данном случае мы можем передать странице данные через запрос типа https://localhost:7085/Index?name=Tom&age=37.











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

**Источник:** [https://metanit.com/sharp/razorpages/2.5.php](https://metanit.com/sharp/razorpages/2.5.php)
