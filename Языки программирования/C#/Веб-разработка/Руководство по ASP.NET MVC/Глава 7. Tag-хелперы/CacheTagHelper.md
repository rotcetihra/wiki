# CacheTagHelper

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC|Руководство по ASP.NET MVC]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 7. Tag-хелперы|Глава 7. Tag-хелперы]] / CacheTagHelper

[[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 7. Tag-хелперы/EnvironmentTagHelper|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 7. Tag-хелперы|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 7. Tag-хелперы/Создание tag-хелперов|Вперёд]]

**Дата написания:** 05.09.2026

## CacheTagHelper

Последнее обновление: 04.04.2022




-

-

-














Класс CacheTagHelper позволяет кэшировать в памяти сервера некоторую часть контента представления.
Он использует тег `<cache>`, и весь контент внутри этого тега кэшируется в памяти.
Перед кэшированием тег-хелпер проверяет, сохранен ли уже данный контент в MemoryCache. Если контент имеется в кэше,
тогда движку Razor посылается контент из кэша. Если же данного контента не оказывается в кэше,
тогда Razor обрабатывает контент, а тег-хелпер сохраняет контент в memory cache для последующего использования.


Например, пусть у нас в представлении например, в Index.cshtml, применяется следующий код:

```

<p>Некэшируемое время: <b>@DateTime.Now.ToString("HH:mm:ss")</b></p>
<cache>
<p>Кэшируемое время: <b>@DateTime.Now.ToString("HH:mm:ss")</b></p>
</cache>

```


Здесь два раза выводится текущее время. Но второй вызов метода `DateTime.Now.ToString` помещен в элемент cache, что позволяет кэшировать результат метода.
И если в течение короткого времени мы несколько раз обратимся к приложению, то увидим, что время из второго вызова `DateTime.Now.ToString` застыло и не
изменяется:
![CacheTagHelper и кэширование контента в представлениях ASP.NET Core MVC в C#](https://metanit.com./pics/7.11.png)


Рассмотрим атрибуты, которые использует данный тег.


### expires-after


`expires-after` указывает, на какое время контент будет кэшироваться. В качестве значения атрибут принимает объект
TimeSpan:

```

<cache expires-after="@TimeSpan.FromMinutes(10)">
 @await Html.PartialAsync("TimeView")
</cache>

```


В данном случае контент кэшируется на 10 минут.


### expires-on


`expires-on` указывает, когда именно истечет срок хранения контента в кэше. В качестве значения атрибут принимает объект
DateTime:

```

<cache expires-on="@DateTime.Now.AddDays(1)">
 @await Html.PartialAsync("TimeView")
</cache>

```


Здесь срок кэширования истекает через день.


### expires-sliding


`expires-sliding` определяет, через какое время с момента последнего посещения контент будет удаляться из кэша.
В качестве значения атрибут принимает объект TimeSpan:

```

<cache expires-sliding="@TimeSpan.FromMinutes(10)">
 @await Html.PartialAsync("TimeView")
</cache>

```


### vary-by-user


`vary-by-user` позволяет кэшировать контент отдельно для каждого залогиненного пользователя (для которого установлено значение `User.Identity.Name`). При кэшировании к ключу контента в кэше
добавляется логин пользователя. В качестве значения атрибут принимает логическое значение true (надо кэшировать по пользователю) или false:

```

<cache expires-after="@TimeSpan.FromMinutes(15)" vary-by-user="true">

</cache>

```


### vary-by-route


Данный атрибут позволяет кэшировать различные версии одного и того же контента в зависимости от параметров маршрута.
В качестве значения атрибут принимает названия параметров через запятую, которые будут учитываться при кэшировании.
И затем в кэше для контента к ключу будет добавляться значение параметров:

```

<cache expires-after="@TimeSpan.FromMinutes(15)" vary-by-route="id">

</cache>

```


В данном случае будут создаваться разные версии одного и того же контента для разных значений параметра id.


### vary-by-query


`vary-by-query` позволяет кэшировать различные версии контента в зависимости от значений параметров, переданных в запросе.
В качестве значения атрибуту передается список параметров через запятую. При кэшировании к ключу контента в кэше
добавляется значение этих параметров.

```

<cache vary-by-query="name">

</cache>

```


Здесь для каждого значения параметра name будут кэшироваться свои копии контента.


### vary-by-cookie


Данный атрибут позволяет кэшировать различные версии одного и того же контент в зависимости от значений, которые хранятся в куках.
В качестве значения атрибут принимает названия куков через запятую, которые будут учитываться при кэшировании.
В ходе кэширования значения этих кук будут добавляться к ключам контента в кэше.

```

<cache vary-by-cookie="pubid">

</cache>

```


Здесь предполагается, что наше приложение использует куку "pubid". И для каждого ее значения будут кэшироваться свои копии контента.


### vary-by-header


`vary-by-header` позволяет кэшировать различные версии контента в зависимости от значений заголовков запроса.
В качестве значения атрибуту передается название заголовка запроса. Например, для кэширования разных версий контента для разных браузеров
может использоваться заголовок User-Agent:

```

<cache vary-by-header="User-Agent">

</cache>

```


### vary-by


`vary-by` позволяет кэшировать различные версии контента в зависимости от произвольного строкового значения.
Например, кэшируем в зависимости от значения `ViewBag.Id`:

```

<cache vary-by="@ViewBag.Id">

</cache>

```


### priority


Определяет приоритет кэшируемого контента. Приоритет может иметь значение, если для размещения кэша не хватает памяти.
В этом случае из кэша могут удаляться некоторые объекты. И чем ниже приоритет, тем больше вероятность что данные объекты будут удалены при нехватке памяти.


Атрибут `priority` принимает одно из значений перечисления Microsoft.Extensions.Caching.Memory.CacheItemPriority:


-

Low: низкий приоритет

-

High: высокий приоритет

-

NeverRemove: контент никогда не удаляется из кэша

-

Normal: средний приоритет


Например:

```

<cache vary-by-user="true"
 priority="@Microsoft.Extensions.Caching.Memory.CacheItemPriority.Normal">
</cache>

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

**Источник:** [https://metanit.com/sharp/aspnetmvc/7.6.php](https://metanit.com/sharp/aspnetmvc/7.6.php)
