# Передача данных во View Component

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC|Руководство по ASP.NET MVC]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 8. View Component|Глава 8. View Component]] / Передача данных во View Component

[[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 8. View Component/Определение компонента представлений|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 8. View Component|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 8. View Component/Генерация контента в View Component|Вперёд]]

**Дата написания:** 05.09.2026

## Передача данных во View Component

Последнее обновление: 05.04.2022




-

-

-














View Component может извне получаит различные данные. Во-первых, View Component может принимать некоторые параметры, которые ему передаются при вызове
компонента. Во-вторых, класс View Component, также как и другие классы в ASP.NET Core, может получать зависимости из провайдера сервисов через механизм dependency injection.
Рассмотрим, оба случая передачи данных.


### Передача параметров в View Component


Через параметры метода Invoke/InvokeAsync мы можем получать извне некоторые данные. Например, определим следующий компонент:

```

using Microsoft.AspNetCore.Mvc;

namespace MvcApp.Components
{
 [ViewComponent]
 public class Timer
 {
 public string Invoke(bool includeSeconds)
 {
 if (includeSeconds)
 return $"Текущее время: {DateTime.Now.ToString("hh:mm:ss")}";
 else
 return $"Текущее время: {DateTime.Now.ToString("hh:mm")}";
 }
 }
}

```


В методе Invoke компонент принимает один параметр - includeSeconds, который представляет тип bool. Если этот параметр равен true, то строка со временем также содерджит секунды,
если параметр равен false - секунды опускаются.


Теперь обратимся к этому компоненту в представлении:

```

@addTagHelper *, MvcApp

<p>С секундами: <br />
 @await Component.InvokeAsync("Timer", new { includeSeconds=true})
</p>

<p>Без секунд: <br />
 <vc:timer include-seconds="false"></vc:timer>
</p>

```


Для передачи значений параметрам метода Invoke/InvokeAsync в методе `Component.InvokeAsync()` в качестве второго аргумента указывается
анонимный объект, который устанавливает значения всех параметров.


При использовании тег-хелпера параметры компонента определяются как атрибуты тега, которым присваивается необходимое значение. Причем если у нас исползуется
camelcase, при котором каждое подслово в составе составного слова пишется с большой буквы, например, includeSeconds, то в названии атрибута все подслова разделяются дефисом и начинаются со строчной буквы.


Результат выполнения:
![Параметры в View Component в ASP.NET Core MVC и C#](https://metanit.com./pics/8.3.png)


Подобным образом мы можем использовать и больщее количество параметров. Например, изменим код компонента следующим образом:

```

using Microsoft.AspNetCore.Mvc;

namespace MvcApp.Components
{
 [ViewComponent]
 public class Timer
 {
 public string Invoke(bool includeSeconds, bool format24)
 {
 string time;
 DateTime now = DateTime.Now;

 if (format24) // если 24-часовой формат
 time = now.ToString("HH:mm");
 else // если 12-часовой формат
 time = now.ToString("hh:mm");

 if (includeSeconds) // если надо добавить секунды
 time = $"{time}:{now.Second}";

 return $"Текущее время: {time}";
 }
 }
}

```


Новый параметр `format24` указывает в каком формате будет выводиться время - в 24-часовом или в 12 часовом.


Обратимся к компоненту в представлении:

```

@addTagHelper *, MvcApp

<p>24 часовой формат с секундами: <br />
 @await Component.InvokeAsync("Timer", new { includeSeconds=true, format24=true})
</p>

<p>12 часовой формат без секунд: <br />
 <vc:timer include-seconds="false" format24="false"></vc:timer>
</p>
<p>
 24 часовой формат без секунд: <br />
 <vc:timer include-seconds="false" format24="true"></vc:timer>
</p>

```

![Передача параметров в компонент представления View Component в ASP.NET Core MVC и C#](https://metanit.com./pics/8.4.png)


При необходимости для параметров во View Component можно устанавить значения по умолчанию:

```

using Microsoft.AspNetCore.Mvc;

namespace MvcApp.Components
{
 [ViewComponent]
 public class Timer
 {
 public string Invoke(bool includeSeconds = false, bool format24 = true)
 {
 string time;
 DateTime now = DateTime.Now;

 if (format24) // если 24-часовой формат
 time = now.ToString("HH:mm");
 else // если 12-часовой формат
 time = now.ToString("hh:mm");

 if (includeSeconds) // если надо добавить секунды
 time = $"{time}:{now.Second}";

 return $"Текущее время: {time}";
 }
 }
}

```


То есть по умолчанию применяется 24-часовой формат, а секунды не включаются.


Попробуем при обращении к компоненту опустить некоторые параметры (ведь теперь они имеют значения по умолчанию):

```

<p>
 Все значения по умолчанию: <br />
 @await Component.InvokeAsync("Timer")
</p>
<p>
 12-часовой формат: <br />
 @await Component.InvokeAsync("Timer", new { format24 = false })
</p>
<p>
 С секундами: <br />
 @await Component.InvokeAsync("Timer", new { includeSeconds = true })
</p>

```

![Значения по умолчанию для параметров в View Component в ASP.NET Core](https://metanit.com./pics/8.5.png)


### Передача сложных данных в View Component


При этом View Component может принимать более сложные данные. Например, определим в проекте папку Models следующий класс Person:

```

namespace MvcApp.Models
{
 public record class Person(string Name, int Age);
}

```


В папке Components определим новый View Component - класс PersonInfoViewComponent:

```

using MvcApp.Models; // пространство имен класса Person

namespace MvcApp.Components
{
 public class PersonInfoViewComponent
 {
 public string Invoke(Person Person)
 {
 return $"Name: {Person.Name} Age: {Person.Age}";
 }
 }
}

```


Данный компонент принимает объкт Person и возвращает его данные в виде строки.


Теперь применим данный компонент в представлении:

```

@addTagHelper *, MvcApp

@using MvcApp.Models <!-- пространство имен модели Person-->

@{
 Person tom = new("Tom", 37);
 Person alice = new("Alice", 32);
}
<p>
 @await Component.InvokeAsync("PersonInfo", new { person = tom})
</p>
<p>
 <vc:person-info person="alice"></vc:person-info>
</p>

```


Результат работы приложения:
![Передача сложных данных в View Component в ASP.NET Core MVC и C#](https://metanit.com./pics/8.6.png)


### Внедрение зависимостей


Как и другие классы, View Component может получать внеденные в приложение зависимости.


Например, в файле Program.cs определен следующий код:

```

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddTransient<ITimeService, SimpleTimeService>();

builder.Services.AddControllersWithViews();
var app = builder.Build();
app.MapControllerRoute(
 name: "default",
 pattern: "{controller=Home}/{action=Index}/{id?}");

app.Run();

public interface ITimeService
{
 string GetTime();
}
public class SimpleTimeService : ITimeService
{
 public string GetTime() => DateTime.Now.ToString("HH:mm:ss");
}

```


Здесь добавляется сервис ITimeService в виде класса SimpleTimeService.


Используем этот сервис и для этого изменим код компонента Timer:

```

using Microsoft.AspNetCore.Mvc;

namespace MvcApp.Components
{
 [ViewComponent]
 public class Timer
 {
 ITimeService timeService;
 public Timer(ITimeService service)
 {
 timeService = service;
 }
 public string Invoke()
 {
 return $"Текущее время: {timeService.GetTime()}";
 }
 }
}

```


При запуске приложения и вызове компонента ему автоматически будет передаваться нужный объект ITimeService. И также в представлении мы сможем его использовать:

```

@addTagHelper *, MvcApp

<div>
 @await Component.InvokeAsync("Timer")
</div>
<div>
 <vc:timer />
</div>

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

**Источник:** [https://metanit.com/sharp/aspnetmvc/8.2.php](https://metanit.com/sharp/aspnetmvc/8.2.php)
