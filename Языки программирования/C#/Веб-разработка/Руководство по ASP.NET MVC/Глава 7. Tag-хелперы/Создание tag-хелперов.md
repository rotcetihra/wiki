# Создание tag-хелперов

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC|Руководство по ASP.NET MVC]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 7. Tag-хелперы|Глава 7. Tag-хелперы]] / Создание tag-хелперов

[[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 7. Tag-хелперы/CacheTagHelper|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 7. Tag-хелперы|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 7. Tag-хелперы/Управление выводом tag-хелпера|Вперёд]]

**Дата написания:** 05.09.2026

## Создание tag-хелперов

Последнее обновление: 04.04.2022




-

-

-














Чтобы создать свой tag-хелпер, нам надо унаследовать класс от класса TagHelper, переопределив его метод Process
или ProcessAsync().


### Определение tag-хелпера


Для примера создадим какой-нибудь простейший тег-хелпер. Допустим, пусть он будет выводить текущее время. Для создания хелпера вначале добавим в проект новую папку, которую
назовем TagHelpers. Далее в эту папку добавим новый класс TimerTagHelper:

```

using Microsoft.AspNetCore.Razor.TagHelpers;

namespace MvcApp.TagHelpers
{
 public class TimerTagHelper : TagHelper
 {
 public override void Process(TagHelperContext context, TagHelperOutput output)
 {
 }
 }
}

```

![Создание tag-хелперов в ASP.NET Core MVC и C#](https://metanit.com./pics/7.12.png)


По умолчанию tag-хелперы применяют соглашения об наименовании, согласно которым класс должен оканчиваться на суффикс TagHelper.
Хотя это не является обязательной практикой, мы могли бы определить и просто класс Timer:

```

public class Timer : TagHelper
{
}

```


А вся остальная часть названия, которая идет до TagHelper, будет использоваться в качестве названия тега, то есть `<timer>`.


Для генерации элемента html на основе тега используется метод Process. Он принимает два параметра: объект TagHelperContext,
представляющий контекст тега (его содержимое, атрибуты), и объект TagHelperOutput, отвечающий за генерацию выходного элемента html на основе тега.


Теперь изменим определение класса следующим образом:

```

using Microsoft.AspNetCore.Razor.TagHelpers;
namespace MvcApp.TagHelpers
{
 public class TimerTagHelper : TagHelper
 {
 public override void Process(TagHelperContext context, TagHelperOutput output)
 {
 output.TagName = "div"; // заменяет тег <timer> тегом <div>
 // устанавливаем содержимое элемента
 output.Content.SetContent($"Текущее время: {DateTime.Now.ToString("HH:mm:ss")}");
 }
 }
}

```


### Подключение tag-хелпера


Чтобы задействовать класс хелпера в представлении, нам надо подключить его функциональность в представление следующим образом:

```

@addTagHelper *, MvcApp

```


В данном случае предполагается, что проект приложения называется MvcApp. Для добавления хелпера используется директива addTagHelper. Директива использует синтаксис подстановочных знаков,
определяя, какие tag-хелперы будут загружаться в представление. И также указывается сборка, которая содержит классы хелперы. То в директиве

```
@addTagHelper *, MvcApp
```


первая часть до запятой (в данном случае символ звездочка) указывает, какие tag-хелперы будут загружаться в представление (символ
звездочки * используется для загрузки всех хелперов). А вторая часть после запятой указывает на сборку, в которой хранятся хелперы - в данном случае
сборка MvcApp (так как хелперы определены в текущем проекте).


Если представления использует файл _ViewImports.cshtml, то данную директиву можно определить в _ViewImports.cshtml,
чтобы подключить хелпер сразу во все представления.


### Использование tag-хелпера


Теперь используем выше определенный tag-хелпер TimerTagHelper в каком-нибудь представлении:

```

@addTagHelper *, MvcApp

<timer></timer>

```


При этом не важно, что элемент `<timer>` пустой. Можно добавить в него какой-нибудь текст, но он не имеет значение. Главное, что этот тег называется по имени класса без суффикса TagHelper. И в итоге вместо этого тега будет сгенерирован
элемент `<div>`, в котором будет выводиться время:
![Создание и подключение tag helper в ASP.NET Core MVC и C#](https://metanit.com./pics/7.13.png)


### Асинхронные операции в тег-хелпере


Если в tag-хелпер должен выполнять какие-то асинхронные операции, например, обращаться к базе данных или к файлу в асинхронном режиме, то вместо метода
`Process()` мы можем переопределить другой метод класса TagHelper - метод `ProcessAsync()`. Например:

```

using Microsoft.AspNetCore.Razor.TagHelpers;

namespace MvcApp.TagHelpers
{
 public class TimerTagHelper : TagHelper
 {
 public override void Process(TagHelperContext context, TagHelperOutput output)
 {
 output.TagName = "div";
 output.Content.SetContent($"Текущее время: {DateTime.Now.ToString("HH:mm:ss")}");
 }
 }
 public class DateTagHelper : TagHelper
 {
 public override void Process(TagHelperContext context, TagHelperOutput output)
 {
 output.TagName = "div";
 output.Content.SetContent($"Текущая дата: {DateTime.Now.ToString("dd/mm/yyyy")}");
 }
 }
 public class SummaryTagHelper : TagHelper
 {
 public override async Task ProcessAsync(TagHelperContext context, TagHelperOutput output)
 {
 output.TagName = "div";
 // получаем вложенный контекст из дочерних tag-хелперов
 var target = await output.GetChildContentAsync();
 var content = "<h3>Общая информация</h3>" + target.GetContent();
 output.Content.SetHtmlContent(content);
 }
 }
}

```


Здесь определены три tag-хелпера. TimerTagHelper и DateTagHelper однотипны, выводят время и дату соответственно.
SummaryTagHelper служит как-бы оберткой для обоих хелперов. Предполагается, что TimerTagHelper и DateTagHelper будут вложены в
SummaryTagHelper. Например, следующим образом:

```

@addTagHelper *, MvcApp

<summary>
 <timer></timer>
 <date></date>
</summary>

```

![Асинхронный tag-хелпер в ASP.NET Core MVC и C#](https://metanit.com./pics/7.14.png)


В SummaryTagHelper вызывает асинхронный метод `output.GetChildContentAsync()`, который возвращает сгенерированную разметку html для вложенных
tag-хелперов. Затем мы можем дополнительно каким-либо образом изменить эту разметку и установить ее в качестве содержимого.


И этот как раз тот случай, когда можно использовать асинхронный метод ProcessAsync.


Если tag-хелпер содержит оба метода: и `Process()`, и `ProcessAsync()`, то вызываться будет именно метод `ProcessAsync()`.










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

**Источник:** [https://metanit.com/sharp/aspnetmvc/7.7.php](https://metanit.com/sharp/aspnetmvc/7.7.php)
