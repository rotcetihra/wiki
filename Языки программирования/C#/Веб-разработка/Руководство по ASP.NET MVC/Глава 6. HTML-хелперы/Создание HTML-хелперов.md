# Создание HTML-хелперов

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC|Руководство по ASP.NET MVC]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 6. HTML-хелперы|Глава 6. HTML-хелперы]] / Создание HTML-хелперов

[[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 5. Модели/Создание привязчика модели|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 6. HTML-хелперы|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 6. HTML-хелперы/HTML-хелперы элементов форм|Вперёд]]

**Дата написания:** 05.09.2026

## Создание HTML-хелперов

Последнее обновление: 29.03.2022




-

-

-














Для вывода содержимого в представлении можно применять стандартные html-элементы, которые позволяют создавать блоки, списки, таблицы и т.д. Но кроме
собственно html-элементов в ASP.NET Core MVC для создания разметки можно использовать специальные методы - html-хелперы. Вообще helper можно перевести с
английского как "вспомогательный метод". И фактически html-хелперы представляют собой вспомогательные методы, цель которых - генерация html-разметки.


Для создания простейшего html-хелпера в проект ASP.NET Core добавим новый класс ListHelper:

```

using Microsoft.AspNetCore.Html; // для HtmlString
using Microsoft.AspNetCore.Mvc.Rendering; // для IHtmlHelper

namespace MvcApp
{
 public static class ListHelper
 {
 public static HtmlString CreateList(this IHtmlHelper html, string[] items)
 {
 string result = "<ul>";
 foreach (string item in items)
 {
 result = $"{result}<li>{item}</li>";
 }
 result = $"{result}</ul>";
 return new HtmlString(result);
 }
 }
}

```


В новом классе хелпера определен один статический метод `CreateList`, принимающий в качестве первого параметра объект, для которого
создается метод. Так как данный метод расширяет функциональность html-хелперов, которые представляет интерфейс
Microsoft.AspNetCore.Mvc.Rendering.IHtmlHelper, то именно объект этого типа и передается в данном случае в качестве первого
параметра. Второй параметр метода CreateList - массив строк-значений, которые потом будут выводиться в списке.


В самом методе просто пробегаемся по массиву строк и формируем из них разметку html в виде строки. Результатом метода является объект HtmlString,
который в конструкторе получает разметку html в виде строки.


Этот очень простой метод уже может упростить работу с разметкой. Рассмотрим его использование. Допустим, нам надо в представлении вывести массив строк в списке:

```

@{
 string[] cities = new string[] { "Лондон", "Париж", "Берлин" };
 string[] countries = new string[] { "Великобритания", "Франция", "Германия" };
}
@using MvcApp

<h3>Города</h3>
@Html.CreateList(cities)
<br />
<h3>Страны</h3>
<!-- или можно вызвать так -->
@ListHelper.CreateList(Html, countries)

```


Поскольку html-хелпер представляет метод расширения для объекта IHtmlHelper, то для его применения нам достаточно написать `Html.CreateList`
и передать в метод необходимые параметры. Либо мы можем вызвать его как метод класса, в котором он определен: `ListHelper.CreateList`


И теперь, если мы захотим создать список `<ul>`, нам достаточно будет написать одну строку с вызовом хелпера, передав ему массив:
![Html Helper in ASP.NET Core MVC и C#](https://metanit.com./pics/6.1.png)


При отсутствии подобного хелпера, то нам бы пришлось по сути дублировать один и тот же html-код для создания списка. Однако этот хелпер еще довольно простой, а если нам приходится создавать по сто раз более сложную, но однотипную разметку html, тогда хелперы окажутся еще более полезными.


### TagBuilder


Для создания html-тегов в хелпере мы можем использовать класс Microsoft.AspNetCore.Mvc.Rendering.TagBuilder. Так, перепишем код хелпера
следующим образом:

```

using Microsoft.AspNetCore.Html; // для HtmlString
using Microsoft.AspNetCore.Mvc.Rendering; // для IHtmlHelper
using System.Text.Encodings.Web; // для HtmlEncoder

namespace MvcApp
{
 public static class ListHelper
 {
 public static HtmlString CreateList(this IHtmlHelper html, string[] items)
 {
 TagBuilder ul = new TagBuilder("ul");
 foreach (string item in items)
 {
 TagBuilder li = new TagBuilder("li");
 // добавляем текст в li
 li.InnerHtml.Append(item);
 // добавляем li в ul
 ul.InnerHtml.AppendHtml(li);
 }
 ul.Attributes.Add("class", "itemsList");
 using var writer = new StringWriter();
 ul.WriteTo(writer, HtmlEncoder.Default);
 return new HtmlString(writer.ToString());
 }
 }
}

```


В конструктор TagBuilder передается элемент, для которого создается тег. TagBuilder имеет ряд свойств и методов, которые можно использовать:


-

Свойство InnerHtml позволяет установить или получить содержимое тега в виде строки. Чтобы манипулировать этим свойством,
можно вызвать один из методов:


 -

`Append(string text)`: добавление строки текста внутрь элемента

 -

`AppendHtml(IHtmlContent html)`: добавление в элемент кода html в виде объекта IHtmlContent - это может быть другой объект TagBuilder

 -

`Clear()`: очистка элемента

 -

`SetContent(string text)`: установка текста элемента

 -

`SetHtmlContent(IHtmlContent html)`: установка внутреннего кода html в виде объекта IHtmlContent


-

Свойство Attributes позволяет управлять атрибутами элемента

-

Метод MergeAttribute() позволяет добавить к элементу один атрибут

-

Метод AddCssClass() позволяет добавить к элементу класс css

-

Метод WriteTo() позволяет создать из элемента и его внутреннего содержимого строку при помощью объектов TextWriter и HtmlEncoder.


В итоге мы получим тот же самый список, что и ранее.











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

**Источник:** [https://metanit.com/sharp/aspnetmvc/6.1.php](https://metanit.com/sharp/aspnetmvc/6.1.php)
