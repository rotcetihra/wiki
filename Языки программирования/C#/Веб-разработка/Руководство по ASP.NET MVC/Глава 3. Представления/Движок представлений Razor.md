# Движок представлений Razor

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC|Руководство по ASP.NET MVC]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 3. Представления|Глава 3. Представления]] / Движок представлений Razor

[[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 3. Представления/Введение в представления|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 3. Представления|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 3. Представления/Передача данных в представление|Вперёд]]

**Дата написания:** 05.09.2026

## Движок представлений Razor

Последнее обновление: 22.03.2022




-

-

-














Представления в ASP.NET Core MVC может содержать не только стандартный код html, но и также вставки кода на языке C#. Для обработки кода, который
содержит как элементы html, так и конструкции языка C#, применяется движок представлений.


В действительности при вызове метода View контроллер не производит рендеринг представления и не генерирует разметку html. Контроллер только
готовит данные и выбирает, какое представление надо возвратить в качестве объекта ViewResult. Затем уже объект ViewResult обращается к движку
представления для рендеринга представления в выходной ответ.


По умолчанию в ASP.NET Core MVC применяется один движок представлений - Razor. Хотя при желании мы можем также использовать какие-то другие сторонние движки или создать
свой движок представлений самостоятельно. Цель движка представлений Razor - определить переход от разметки html к коду C#.


Синтаксис Razor довольно прост - все его конструкции предваряются символом @, после которого происходит переход к коду C#. Например, определим следующее
представление:

```

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
![движок представлений razor в представлении ASP.NET Core MVC на C#](https://metanit.com./pics/3.5.png)


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

@{
 string head = "Hello METANIT.COM!"; // определяем переменную head
 string text = "ASP.NET Core Application"; // определяем переменную text
}
<!DOCTYPE html>
<html>
<head>
 <title>METANIT.COM</title>
 <meta charset="utf-8" />
</head>
<body>
 <h2>@head</h2> <!-- используем переменную head -->
 <div>@text</div> <!-- используем переменную text -->
</body>
</html>

```


В блоках кода мы можем определить обычные переменные и потом их использовать в представлении.
![определение переменных в коде razor в представлении ASP.NET Core MVC на C#](https://metanit.com./pics/3.6.png)


Если необходимо вывести значение переменной без каких-либо html-элементов, то мы можем использовать специальный снипет `<text>`:

```

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


Кроме того, мы можем использовать все возможные циклы. Цикл `for`:

```

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

![Циклы в Razor в представлениях в ASP.NET Core MVC на C#](https://metanit.com./pics/3.8.png)


Цикл `foreach`:

```

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


Цикл `while`:

```

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


Цикл `do..while`:

```

@{
 var i = 0;
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

![функции в коде razor в представлении ASP.NET Core MVC на C#](https://metanit.com./pics/3.7.png)










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

**Источник:** [https://metanit.com/sharp/aspnetmvc/3.2.php](https://metanit.com/sharp/aspnetmvc/3.2.php)
