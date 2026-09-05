# Атрибут HtmlTargetElement

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC|Руководство по ASP.NET MVC]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 7. Tag-хелперы|Глава 7. Tag-хелперы]] / Атрибут HtmlTargetElement

[[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 7. Tag-хелперы/Контекст хелпера и получение зависимостей|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 7. Tag-хелперы|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 7. Tag-хелперы/Tag-хелперы и сложные объекты и коллекции|Вперёд]]

**Дата написания:** 05.09.2026

## Атрибут HtmlTargetElement

Последнее обновление: 05.04.2022




-

-

-














Применение атрибута HtmlTargetElement позволяет переопределить поведение tag-хелпера. Для этого класс HtmlTargetElementAttribute определяет следующие свойства:


-

Attributes: указывает, что tag-хелпер применяется только к тем элементам, которые имеют определенные атрибуты.

-

ParentTag: указывает, что tag-хелпер применяется только к тем элементам, которые определены внутри определенного элемента

-

TagStructure: указывает, что tag-хелпер применяется только к тем элементам, которые соответствуют определенному значению из перечисления
`TagStructure`: Unspecified, NormalOrSelfClosing (стандартный или самозакрывающийся элемент) и WithoutEndTag (элемент без закрывающего тега)


### Применение tag-хелпера к атрибутам


Определим следующий класс tag-хелпера:

```

using Microsoft.AspNetCore.Razor.TagHelpers;

namespace MvcApp.TagHelpers
{
 [HtmlTargetElement(Attributes = "header")]
 public class HeaderTagHelper : TagHelper
 {
 public override void Process(TagHelperContext context, TagHelperOutput output)
 {
 output.TagName = "h2";
 output.Attributes.RemoveAll("header");
 }
 }
}

```


Атрибут HtmlTargetElement указывает, что класс будет применяться к элементам, у которых установлен атрибут header. Важно, что название хелпера опять
же соответствует целевому объекту - атрибуту header.


В самом классе происходит замена существующего элемента на элемент `<h2>` и удаление атрибута header. Все внутреннее содержание, текст, который определен
в блоках div, при этом сохраняется.


Используем данный tag-хелпер в представлении и для этого определим следующие элементы:

```

@addTagHelper *, MvcApp

<div header>Hello World</div>
<div header>Hello METANIT.COM</div>

```


Здесь к блокам div применяется атрибут header, который как бы помечает эти блоки как заголовочные элементы.


 В итоге вместо двух блоков div будут созданы следующие заголовки:

```

<h2>Hello World</h2>
<h2>Hello METANIT.COM</h2>

```

![атрибут HtmlTargetElement в tag-хелперах в представлениях ASP.NET Core MVC и C#](https://metanit.com./pics/7.18.png)


Мы также можем определить набор атрибутов, которым должен соответствовать tag-хелпер:

```

[HtmlTargetElement(Attributes = "header, divtitle")]
public class HeaderTagHelper : TagHelper
{
 //.......................
}

```


В этом случае элемент должен иметь сразу два атрибута: header и divtitle.

```

<div header divtitle>Hello World</div>
<div header divtitle>Hello METANIT.COM</div>

```


### Переопределение имени элемента


Мы можем переопределить имя элемента, передав в атрибут HtmlTargetElement другое название элемента, которое отличается от имени tag-хелпера. Например:

```

[HtmlTargetElement("article-header")]
public class HeaderTagHelper : TagHelper
{
 public override void Process(TagHelperContext context, TagHelperOutput output)
 {
 output.TagName = "h2";
 output.Attributes.RemoveAll("article-header");
 }
}

```


Данный tag-хелпер будет применяться к элементу "article-header":

```
<article-header>Hello METANIT.COM</article-header>
```


### Установка родительского тега


Через свойство `ParentTag` можно установить элемент, в котором должен использоваться наш tag-хелпер:

```

[HtmlTargetElement(ParentTag ="div")]
public class HeaderTagHelper : TagHelper
{
 public override void Process(TagHelperContext context, TagHelperOutput output)
 {
 output.TagName = "h2";
 }
}

```


В этом случае tag-хелпер будет применяться только к тем элементам header, который расположены внутри элемента `<div>`:

```

<header>Заголовок 1</header>

<div>
 <header>Заголовок 2</header>
</div>

```


В этом примере только второй элемент header будет обрабатываться tag-хелпером.


### Сочетание нескольких условий


Мы можем определить сразу несколько параметров, чтобы конкретизировать диапазон действия tag-хелпера:

```

using Microsoft.AspNetCore.Razor.TagHelpers;

namespace MvcApp.TagHelpers
{
 [HtmlTargetElement("form-header", ParentTag ="form", Attributes ="form-title")]
 public class HeaderTagHelper : TagHelper
 {
 public override void Process(TagHelperContext context, TagHelperOutput output)
 {
 output.TagName = "h2";
 output.Attributes.RemoveAll("form-title");
 }
 }
}

```


В данном случае класс HeaderTagHelper будет применяться к элементу "form-header", который обязательно должен иметь атрибут "form-title" и который
обязательно должен находиться внутри элемента "form". То есть в следующем случае будет обработан только третий элемент "form-header":

```

<form-header>Заголовок1</form-header>
<form-header form-title>Заголовок2</form-header>

<form>
 <form-header form-title>Заголовок3</form-header>
</form>

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

**Источник:** [https://metanit.com/sharp/aspnetmvc/7.10.php](https://metanit.com/sharp/aspnetmvc/7.10.php)
