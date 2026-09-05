# Управление выводом tag-хелпера

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC|Руководство по ASP.NET MVC]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 7. Tag-хелперы|Глава 7. Tag-хелперы]] / Управление выводом tag-хелпера

[[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 7. Tag-хелперы/Создание tag-хелперов|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 7. Tag-хелперы|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 7. Tag-хелперы/Контекст хелпера и получение зависимостей|Вперёд]]

**Дата написания:** 05.09.2026

## Управление выводом хелпера

Последнее обновление: 04.04.2022




-

-

-














Для управления выводом tag-хелпера применяется объект TagHelperOutput, который передается в качестве параметра в метод Process/ProcessAsync tag-хелпера.
Его свойства позволяют управлять генерацией элемента html:


-

TagName: указывает, какой элемент html будет создаваться вместо тега хелпера

-

TagMode: устанавливает формат создаваемого элемента (с одним или с двумя тегами)

-

Attributes: представляет коллекцию атрибутов, устанавливаемых у создаваемого элемента html

-

Content: представляет содержимое генерируемого элемента html в виде объекта TagHelperContent

-

PreContent: представляет содержимое, которое устанавливается перед создаваемым элементом html

-

PostContent: представляет содержимое, которое устанавливается после создаваемого элемента html

-

PreElement: представляет html-элемент, который добавляется перед создаваемым элементом html

-

PostElement: представляет html-элемент, который добавляется после создаваемого элемента html


### Закрытие элемента


Элементы html могут состоять из двух тегов (открывающего и закрывающего), либо из одного тега (открывающегося или самозакрывающегося). С помощью свойства
TagMode мы можем регулировать закрытие элемента. Оно принимает одно из значений перечисления TagMode:


-

`StartTagAndEndTag`: элемент имеет оба тега

-

`SelfClosing`: элемент содержит самозакрывающийся тег

-

`StartTagOnly`: элемент имеет только открывающий тег


По умолчанию при создании элемента применяется тот же режим закрытия тега, который использовался при его использовании. Например, если мы не устанавливаем
содержимое внутри tag-хелпера, то нет смысла определять для него оба тега. Например, определим следующий tag-хелпер:

```

public class TimerTagHelper : TagHelper
{
 public override void Process(TagHelperContext context, TagHelperOutput output)
 {
 output.TagName = "div";
 output.TagMode = TagMode.StartTagAndEndTag;
 output.Content.SetContent($"Текущее время: {DateTime.Now.ToString("HH:mm:ss")}");
 }
}

```


И теперь мы сможем использовать только один тег:

```
<timer />
```


### Управление контентом


Для управления контентом применяется свойство Content, представляющее объект TagHelperContent, у которого можно
выделить следующие методы:


-

SetContent(text): устанавливает текстовое содержимое элемента

-

SetHtmlContent(html): устанавливает вложенный html-код элемента

-

Append(text): добавляет к текстовому содержимому элемента некоторый текст

-

AppendHtml(html): добавляет к внутреннему коду элемента некоторый код html

-

Clear(): очищает элемент


Так, выше уже использовался метод `output.Content.SetContent()`.


С помощью дополнительных свойств PreElement/PostElement/PreContent/PostContent, который также представляют объект TagHelperContent,
можно управлять контентом вокруг элемента. Например, изменим класс хелпера:

```

public class TimerTagHelper : TagHelper
{
 public override void Process(TagHelperContext context, TagHelperOutput output)
 {
 output.TagName = "div";
 output.TagMode = TagMode.StartTagAndEndTag;
 // элемент перед тегом
 output.PreElement.SetHtmlContent("<h4>Дата и время</h4>");
 // элемент после тега
 output.PostElement.SetHtmlContent($"<div>Дата: {DateTime.Now.ToString("dd/MM/yyyy")}</div>");

 output.Content.SetContent($"Время: {DateTime.Now.ToString("HH:mm:ss")}");
 }
}

```


В итоге в данном случае тег `<timer />` будет преобразован в следующий набор элементов:

```

<h4>Дата и время</h4>
<div>Время: 20:34:42</div>
<div>Дата: 07.12.2019</div>

```


### Установка атрибутов


Свойство Attributes позволяет устанавливать атрибуты генерируемого элемента. Оно представляет объект
TagHelperAttributeList, который управляет атрибутами с помощью ряда методов. Некоторые из них:


-

Add(string name, object value): добавляет атрибут с именем name и значением value

-

RemoveAll(string name): удаляет все атрибуты с именем name

-

SetAttribute(string name, object value): устанавливает для атрибута с именем name значение value

-

Clear(): удаляет все атрибуты


Для примера установим стиль и класс элемента:

```

public class TimerTagHelper : TagHelper
{
 public override void Process(TagHelperContext context, TagHelperOutput output)
 {
 output.TagName = "div";
 output.TagMode = TagMode.StartTagAndEndTag;
 output.Attributes.SetAttribute("style", "color:red;");
 output.Attributes.SetAttribute("class", "timer");
 output.Content.SetContent($"{DateTime.Now.ToString("HH:mm:ss")}");
 }
}

```


В итоге из тега:

```
<timer />
```


сгенерирована следующая разметка:

```

<div style="color:red;" class="timer">20:57:26</div>

```


### Атрибуты тега


Мы можем не только управлять атрибутами создаваемых html-элементов, но и определять для тег-хелперов свои атрибуты. Через атрибуты мы можем передать из вне
в класс хелпера некоторые значения. В самом классе можно получить переданные значения с помощью публичных свойств. Например, добавим
возможность установки цвета элемента и возможность выбора, надо ли выводить секунды:

```

public class TimerTagHelper : TagHelper
{
 public bool SecondsIncluded { get; set; }
 public string? Color { get; set; }
 public override void Process(TagHelperContext context, TagHelperOutput output)
 {
 var now = DateTime.Now;
 var time = String.Empty;
 if (SecondsIncluded) // если true добавляем секунды
 time = now.ToString("HH:mm:ss");
 else
 time = now.ToString("HH:mm");

 output.TagName = "div";
 output.TagMode = TagMode.StartTagAndEndTag;
 // устанавливаем цвет, если свойство Color не равно null
 if(Color != null) output.Attributes.SetAttribute("style", $"color:{Color};");

 output.Content.SetContent(time);
 }
}

```


Используем этот хелпер в представлении:

```

<timer color="navy" seconds-included="true" />
<timer color="#0984e3" seconds-included="true" />
<timer color="#ff7675" />
<timer />

```

![Атрибуты в TagHelpers в ASP.NET Core MVC и C#](https://metanit.com./pics/7.15.png)


Во время выполнения приложения из атрибутов будут передаваться значения соответствующим свойствам. Соответствие идет по имени.
Но надо отметить, что если атрибут тега или сам тег в названии содержит дефисы в качестве разделителей, то название соответствующего тегу
свойства состоит из нескольких частей и каждая из этих частей начинается с заглавной буквы. Например, атрибуту `seconds-included`
будет соответствовать свойство `SecondsIncluded`.


Кроме того, мы можем не указывать атрибуты в теге, тогда свойства хелпера получат значения по умолчанию, как в случае выше. Но если в случае
выше это не критично, то в других конкретных случаях это может сыграть важную роль, и на этот случае можно проверять значения свойств перед использованием.


### Метод SuppressOutput


Кроме свойств TagHelperOutput имеет еще ряд методов, которые позволяют управлять выводом. Среди них надо отметить метод
SuppressOutput(), который позволяет не обрабатывать тег. То есть при применении этого метода тег не будет обрабатываться, и для него не будет создаваться никакой
html-разметки на веб-странице. Так, изменим класс хелпера следующим образом:

```

public class TimerTagHelper : TagHelper
{
 public bool Condition { get; set; }
 public override void Process(TagHelperContext context, TagHelperOutput output)
 {
 if (!Condition)
 {
 output.SuppressOutput();
 }
 else
 {
 output.TagName = "div";
 output.TagMode = TagMode.StartTagAndEndTag;
 output.Content.SetContent($"{DateTime.Now.ToString("HH:mm:ss")}");
 }
 }
}

```


Здесь добавляется свойство Condition, которое хранит логическое значение true или false. А в методе Process в зависимости от его значения
применяется метод `output.SuppressOutput()`, который прекращает обработку тега.


В этом случае в представлении мы можем определить следующий код:

```

<timer condition="false" />
<timer condition="true" />

```


Здесь свойству Condition соответствует атрибут condition, который принимает значение true или false. И поскольку в первом случае в
атрибут condition передано значение false, для этого тега в классе будет применяться метод `output.SuppressOutput()`,
поэтому вместо этого тега на веб-странице мы ничего не увидим.


### Передача сложных объектов


Кроме простых свойств типа int или string в хелпер можно передавать сложные объекты. Например:

```

using Microsoft.AspNetCore.Razor.TagHelpers;

namespace MvcApp.TagHelpers
{
 public class TimerTagHelper : TagHelper
 {
 public StyleInfo? Style { get; set; }
 public override void Process(TagHelperContext context, TagHelperOutput output)
 {
 output.TagName = "div";
 output.TagMode = TagMode.StartTagAndEndTag;
 // формируем стиль
 string style = "";
 if (Style?.Color != null) style = $"color:{Style.Color};";
 if (Style?.FontSize != null) style = $"{style}font-size:{Style.FontSize}px;";
 if (Style?.FontFamily != null) style = $"{style}font-family:{Style.FontFamily};";

 output.Attributes.SetAttribute("style", style);
 output.Content.SetContent($"{DateTime.Now.ToString("HH:mm:ss")}");
 }
 }
 public class StyleInfo
 {
 public string? Color { get; set; }
 public int? FontSize { get; set; }
 public string? FontFamily { get; set; }
 }
}

```


Здесь хелпер хранит ссылку на объект StyleInfo, которые инкапсулирует стилевые свойства создаваемого элемента. Далее в представлении мы можем передать
значения для этого свойства:

```

@using MvcApp.TagHelpers @*пространство имен класса StyleInfo*@
@addTagHelper *, MvcApp

<timer style='new StyleInfo{Color="#c0392b", FontFamily="Verdana", FontSize=18}' />
<timer style='new StyleInfo{Color="#2980b9", FontFamily="Arial", FontSize=18}' />

```

![Атрибуты и свойства в Tag Helper в ASP.NET Core MVC и C#](https://metanit.com./pics/7.16.png)










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

**Источник:** [https://metanit.com/sharp/aspnetmvc/7.8.php](https://metanit.com/sharp/aspnetmvc/7.8.php)
