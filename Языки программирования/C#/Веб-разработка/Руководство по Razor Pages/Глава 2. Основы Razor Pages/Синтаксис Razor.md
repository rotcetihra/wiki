# Синтаксис Razor

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по Razor Pages|Руководство по Razor Pages]] / [[Языки программирования/C#/Веб-разработка/Руководство по Razor Pages/Глава 2. Основы Razor Pages|Глава 2. Основы Razor Pages]] / Синтаксис Razor

[[Языки программирования/C#/Веб-разработка/Руководство по Razor Pages/Глава 2. Основы Razor Pages/Определение страниц Razor|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по Razor Pages/Глава 2. Основы Razor Pages|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по Razor Pages/Глава 2. Основы Razor Pages/Модель страницы Razor|Вперёд]]

**Дата написания:** 05.09.2026

## Синтаксис Razor

Последнее обновление: 14.04.2022




-

-

-














Ключевым моментом в определении интерфейса на страницах Razor Page является использование конструкций движка Razor. Благодаря Razor мы можем применять
на странице выражения языка C#. Синтаксис Razor довольно прост - все его конструкции предваряются символом @, после которого происходит переход от кода HTML к коду C#. При генерации ответа клиенту Razor обрабатывает выражения языка C# и на их основе генерирует код HTML.
Например, определим следующее
представление:

```

@page

<!DOCTYPE html>
<html>
<head>
 <title>METANIT.COM</title>
 <meta charset="utf-8" />
</head>
<body>
 <h2>Time: @DateTime.Now.ToShortTimeString()</h2>
</body>
</html>

```


Здесь вместо выражения `@DateTime.Now.ToShortTimeString()` при рендеринге представления будет вставляться текущее время:
![движок представлений razor в Razor Pages в ASP.NET Core и C#](https://metanit.com./pics/2.2.png)


Стоит отметить, что по умолчанию Razor подключает на страницы следующие пространства имен

```

using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.Rendering;
using Microsoft.AspNetCore.Mvc.ViewFeatures;

```


Соответственно мы можем использовать функционал этих пространств имен на страницах Razor, как в примере выше структуру DateTime из пространства System.


### Типы конструкций Razor


Все конструкции Razor можно условно разделить на два вида: однострочные выражения и блоки кода.


Пример применения однострочных выражений:

```
<p>Date: @DateTime.Now.ToLongDateString()</p>
```


В данном случае используется объект DateTime и его метод `ToLongDateString()`


Или еще один пример:

```
<p>@(20 + 30)</p>
```


Так как перед скобками стоит знак @, то выражение в скобках будет интерпретироваться как выражение на языке C#. Поэтому браузер выведет число 50, а не "20 + 30".


Но если вдруг мы создаем код html, в котором присутствует символ @ не как часть синтаксиса Razor, а сам по себе, то, чтобы его отобразить, нам надо его дублировать:

```
<p>@@DateTime.Now =@DateTime.Now.ToLongDateString()</p>
```


Блоки кода могут иметь несколько выражений. Блок кода заключается в фигурные скобки, а каждое выражение завершается точкой с запятой аналогично
блокам кода и выражениям на C#:

```

@page

@{
 string head = "Hello METANIT.COM!"; // определяем переменную head
 string text = "ASP.NET Core Application"; // определяем переменную text
}

<h2>@head</h2> <!-- используем переменную head -->
<div>@text</div> <!-- используем переменную text -->

```


В блоках кода мы можем определить обычные переменные и потом их использовать в представлении.
![определение переменных на странице Razor Pages в ASP.NET Core и C#](https://metanit.com./pics/2.3.png)


Если необходимо вывести значение переменной без каких-либо html-элементов, то мы можем использовать специальный снипет `<text>`:

```

@page

@{
 int i = 8;
 <text>@i</text>
}
<text>@(i+1)</text>

```


В Razor могут использоваться комментарии. Они располагаются между символами `@**@`:

```
@* текст комментария *@
```


### Условные конструкции


Также мы можем использовать условные конструкции:

```

@page

@{
 string morning = "Good Morning";
 string evening = "Good Evening";
 string hello = "Hello";
 int hour = DateTime.Now.Hour;
}
@if (hour < 12)
{
 <h2>@morning</h2>
}
else if (hour > 17)
{
 <h2>@evening</h2>
}
else
{
 <h2>@hello</h2>
}

```


Конструкция `switch`:

```

@page

@{
 string language = "german";
}
@switch(language)
{
 case "russian":
 <h3>Привет мир!</h3>
 break;
 case "german":
 <h3>Hallo Welt!</h3>
 break;
 default:
 <h3>Hello World!</h3>
 break;
}

```


### Циклы


Кроме того, мы можем использовать все возможные циклы. Цикл for:

```

@page

@{
 string[] people = { "Tom", "Sam", "Bob" };
}
<ul>
 @for (var i = 0; i < people.Length; i++)
 {
 <li>@people[i]</li>
 }
</ul>

```

![Циклы на C# в Razor Pages в представлениях в ASP.NET Core](https://metanit.com./pics/2.4.png)


Цикл foreach:

```

@page

@{
 string[] people = { "Tom", "Sam", "Bob" };
}
<ul>
 @foreach (var person in people)
 {
 <li>@person</li>
 }
</ul>

```


Цикл while:

```

@page

@{
 string[] people = { "Tom", "Sam", "Bob" };
 var i = 0;
}
<ul>
 @while ( i < people.Length)
 {
 <li>@people[i++]</li>
 }
</ul>

```


Цикл do..while:

```

@page

@{
 var i = 1;
}
<ul>
 @do
 {
 <li>@(i * i)</li>
 }
 while ( i++ < 5);
</ul>

```


### try...catch


Конструкция `try...catch...finally`, как и в C#, позволяет обработать исключение, которое может возникнуть при выполнение кода:

```

@page

@try
{
 throw new InvalidOperationException("Something wrong");
}
catch (Exception ex)
{
 <p>Exception: @ex.Message</p>
}
finally
{
 <p>finally</p>
}

```


Если в блоке try выбрасывается исключение, то выполняется блок catch. И в любом случае в конце блока try и catch выполняется блок finaly.


### Вывод текста в блоке кода


Обычный текст в блоке кода мы не сможем вывести:

```

@page

@{
 bool isEnabled = true;
}
@if (isEnabled)
{
 Hello World
}

```


В этом случае Razor будет рассматривать строку "Hello" как набор операторов языка C#, которых, естественно в C# нет, поэтому мы получим ошибку.
И чтобы вывести текст как есть в блоке кода, нам надо использовать выражение `@:`:

```

@page

@{
 bool isEnabled = true;
}
@if (isEnabled)
{
 @: Hello
}

```


### Функции


Директива @functions позволяет определить функции, которые могут применяться в представлении. Например:

```

@page

@functions
{
 public int Sum(int a, int b)
 {
 return a + b;
 }
 public int Square(int n) => n * n;
}
<p>Sum of 5 and 4: <b> @Sum(5, 4)</b></p>
<p>Square of 4: <b>@Square(4)</b></p>

```

![функции в коде razor pages в ASP.NET Core на C#](https://metanit.com./pics/2.5.png)


### Локальные функции


В блоках кода также можно определять локальные функции:

```

@page

@{
 void RenderName(string name)
 {


Name: **@name**
 }

 RenderName("Tom");
 RenderName("Bob");
}

@{RenderName("Sam");}

```


В данном случае функция RenderName выводит некоторую разметку html, в которую передается значение параметра name:
![локальные функции в razor pages на C# в ASP.NET Core](https://metanit.com./pics/2.6.png)


### Инструкция using


С помощью директивы using можно подключать на страницу Razor различные пространства. Например, определим в проекте новый класс Person:

```

namespace RazorPagesApp
{
 public class Person
 {
 public string Name { get; }
 public int Age { get; }
 public Person(string name, int age)
 {
 Name = name;
 Age = age;
 }
 public override string ToString() => $"Person {Name} ({Age} лет)";
 }
}

```


В данном случае класс Person расположен в пространстве имен RazorPagesApp:
![определение классов для razor pages на C# в ASP.NET Core](https://metanit.com./pics/2.7.png)


Чтобы использовать данный класс на странице Razor, его пространство имен необходимо подключить с помощью директивы @using:

```

@page

@using RazorPagesApp @* подключение пространства имен RazorPagesApp *@

@{
 Person tom = new Person("Tom", 37);
}

<h2>@tom</h2>

```

![подключение пространств имен и директива using в razor pages на C# в ASP.NET Core](https://metanit.com./pics/2.8.png)


В качестве альтрнативы, как и в общем в C#, можно было бы указать полное имя класса с учетом пространства имен:

```
RazorPagesApp.Person tom = new RazorPagesApp.Person("Tom", 37);
```


Но директива using позволяет сократить код.











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

**Источник:** [https://metanit.com/sharp/razorpages/2.2.php](https://metanit.com/sharp/razorpages/2.2.php)
