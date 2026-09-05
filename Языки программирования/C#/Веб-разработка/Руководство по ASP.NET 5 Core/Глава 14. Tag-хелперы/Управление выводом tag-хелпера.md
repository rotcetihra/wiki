# Управление выводом tag-хелпера

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET 5 Core|Руководство по ASP.NET 5 Core]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET 5 Core/Глава 14. Tag-хелперы|Глава 14. Tag-хелперы]] / Управление выводом tag-хелпера

[[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET 5 Core/Глава 14. Tag-хелперы/Создание tag-хелперов|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET 5 Core/Глава 14. Tag-хелперы|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET 5 Core/Глава 14. Tag-хелперы/Контекст хелпера и получение зависимостей|Вперёд]]

**Дата написания:** 05.09.2026

## Управление выводом хелпера


Данное руководство устарело. Актуальное руководство: [Руководство по ASP.NET Core 7](https://metanit.com/sharp/aspnet6/)Последнее обновление: 07.12.2019




-

-

-














Для управления выводом хелпера используется объект TagHelperOutput, который передается в качестве параметра в метод Process tag-хелпера.
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
`TagMode` мы можем регулировать закрытие элемента. Оно принимает одно из значений перечисления `TagMode`:


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


Для управления контентом применяется свойство `Content`, представляющее объект TagHelperContent, у которого можно
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


В итоге будет сгенерирована следующая разметка:

```

<div style="color:red;" class="timer">20:57:26</div>

```


### Атрибуты тега


Мы можем не только управлять атрибутами создаваемых html-элементов, но и определять для тег-хелперов свои атрибуты. Через атрибуты мы можем передать из вне
в класс хелпера некоорые значения. В самом классе можно получить переданные значения с помощью публичных свойств. Например, добавим
возможность установки цвета элемента и возможность выбора, надо ли выводить секунды:

```

public class TimerTagHelper : TagHelper
{
 public bool SecondsIncluded { get; set; }
 public string Color { get; set; }
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
 // устанавливаем цвет
 output.Attributes.SetAttribute("style", $"color:{Color};");

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

![Атрибуты в TagHelpers в ASP.NET Core MVC](https://metanit.com./pics/customtaghelper3.png)


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

using System;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Razor.TagHelpers;
namespace TagHelpersApp.TagHelpers
{
 public class TimerTagHelper : TagHelper
 {
 public StyleInfo Style { get; set; }
 public override void Process(TagHelperContext context, TagHelperOutput output)
 {
 output.TagName = "div";
 output.TagMode = TagMode.StartTagAndEndTag;
 // формируем стиль
 string style = $"color:{Style.Color};font-size:{Style.FontSize}px;font-family:{Style.FontFamily};";
 output.Attributes.SetAttribute("style", style);
 output.Content.SetContent($"{DateTime.Now.ToString("HH:mm:ss")}");
 }
 }
 public class StyleInfo
 {
 public string Color { get; set; }
 public int FontSize { get; set; }
 public string FontFamily { get; set; }
 }
}

```


Здесь хелпер хранит ссылку на объект StyleInfo, которые инкапсулирует стилевые свойства создаваемого элемента. Далее в представлении мы можем передать
значения для этого свойства:

```

@using TagHelpersApp.TagHelpers <!-- пространство имен класса StyleInfo-->
<timer style='new StyleInfo{Color="#74b9ff", FontFamily="Verdana", FontSize=18}' />
<timer style='new StyleInfo{Color="#ff7675", FontFamily="Arial", FontSize=18}' />

```

![Атрибуты и свойства в Tag Helper в ASP.NET Core MVC](https://metanit.com./pics/customtaghelper4.png)










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

**Источник:** [https://metanit.com/sharp/aspnet5/10.10.php](https://metanit.com/sharp/aspnet5/10.10.php)
