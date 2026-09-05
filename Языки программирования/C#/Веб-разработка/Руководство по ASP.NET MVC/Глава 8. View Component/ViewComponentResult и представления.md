# ViewComponentResult и представления

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC|Руководство по ASP.NET MVC]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 8. View Component|Глава 8. View Component]] / ViewComponentResult и представления

[[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 8. View Component/Генерация контента в View Component|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 8. View Component|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 8. View Component/ViewComponentContext|Вперёд]]

**Дата написания:** 05.09.2026

## ViewComponentResult и генерация представления

Последнее обновление: 05.04.2022




-

-

-














ViewComponentResult позволяет использовать для рендеринга контента частичное представление. Если мы наследуем класс компонента от базового класса
ViewComponent, то для генерации объекта ViewComponentResult мы можем вызвать унаследованный метод View.


Этот метод имеет четыре перегруженных версии:


-

`View()`: для рендеринга контента выбирает представление по умолчанию

-

`View(model)`: для рендеринга контента выбирает представление по умолчанию, в которое передает некоторую модель

-

`View(viewName)`: для рендеринга контента выбирает представление с именем viewName

-

`View(viewName, model)`: для рендеринга контента выбирает представление с именем viewName, в которое передает некоторую модель


Так, определим следующий класс компонента UsersListViewComponent:

```

using Microsoft.AspNetCore.Mvc;

namespace MvcApp.Components
{
 public class UsersListViewComponent : ViewComponent
 {
 List<string> users = new List<string>
 {
 "Tom", "Tim", "Bob", "Sam"
 }
 public IViewComponentResult Invoke()
 {
 return View(users);
 }
 }
}

```


В этом классе определяется условный список пользователей - коллекция строк.


Метод `Invoke()` возвращает объект `IViewComponentResult` или фактически представление, которое мы далее создадим. Причем в это предствление передается
созданный в конструкторе список.


Теперь создадим представление, которое будет выводить переданные из компонента данные.
Если при вызове метода View в компоненте имя представления явным образом не указано, то в качестве представления по умолчанию используется файл
Default.cshtml. Для поиска файла представления Razor будет просматривать следующие пути в порядке приоритета:


-

`Views/Название_Контроллера/Components/Название_Компонента/Название_Представления.cshtml`

-

`Views/Shared/Components/Название_Компонента/Название_Представления.cshtml`


Допустим, в проекте у нас есть папка Controllers, в которой помещен контроллер HomeController. А в папке Views/Home
расположено представление Index.cshtml для этого контроллера
![View Component и представления в ASP.NET Core MVC и C#](https://metanit.com./pics/8.9.png)


И, допустим, наш UsersListViewComponent будет использоваться только в представлениях
этого контроллера HomeController. В этом случае добавим в папку Views/Home новый каталог, который назовем Components.
А в этот каталог добавим папку, которая называется по имени нашего компонента - UsersList, и определим в ней новое
представление Default.cshtml со следующим кодом:

```

@model IEnumerable<string>
<h2>Список пользователей</h2>
<ul>
 @foreach (var user in Model)
 {
 <li>@user</li>
 }
</ul>

```


Поскольку в представление передается объект List<string>, то оно типизировано типом IEnumerable<string>. В самом представлении
просто выводим переданный список. По сути представление для View Component - это обычнное представление, которое может использовать все те же инсрукции
Razor, конструкции и директивы, что и обычное представление.


То есть в итоге представление, которое используется компонентом, должно лежать по адресу Views/Название_Контроллера/Components/Название_Компонента/Default.cshtml:
![View Component и генерация представлений в ASP.NET Core MVC и C#](https://metanit.com./pics/8.10.png)


Теперь мы можем использовать компонент. Для этого определим в представлении Index.cshtml следующие строки:

```

@addTagHelper *, MvcApp

<div>
 @await Component.InvokeAsync("UsersList")
</div>
<div>
 <vc:users-list />
</div>

```


Результат работы View Component:
![Возвращение представления из View Component в ASP.NET Core MVC и C#](https://metanit.com./pics/8.11.png)


Выше использовалось имя представления по умолчанию: Default.cshtml. Однако нам необязательно применять именно это имя.
Если у нас есть другое представление, например, Users.cshtml, то мы можем его использовать следующим образом:

```

public IViewComponentResult Invoke()
{
 return View("Users", users);
}

```


Имя представления без расширения cshtml передается в метод View в качестве первого параметра. Само представление также должно находиться
по адресу Views/Название_Контроллера/Components/Название_Компонента/










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

**Источник:** [https://metanit.com/sharp/aspnetmvc/8.4.php](https://metanit.com/sharp/aspnetmvc/8.4.php)
