# EnvironmentTagHelper

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC|Руководство по ASP.NET MVC]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 7. Tag-хелперы|Глава 7. Tag-хелперы]] / EnvironmentTagHelper

[[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 7. Tag-хелперы/Tag-хелперы форм|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 7. Tag-хелперы|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 7. Tag-хелперы/CacheTagHelper|Вперёд]]

**Дата написания:** 05.09.2026

## EnvironmentTagHelper

Последнее обновление: 04.04.2022




-

-

-














Тег EnvironmentTagHelper используется для генерации определенной разметки html в зависимости от состояния приложения: находится ли приложение в процессе разработки, тестирования или уже опубликовано на сервере.
Состояние проекта задается с помощью среды окружения ASPNETCORE_ENVIRONMENT. Нередко данный тег-хелпер используется совместно с LinkTagHelper и ScriptTagHelper. Его ключевой атрибут names
позволяет установить названия состояний среды, при которых применяется данный тег.


Например, мы могли бы подключать css-стили bootstrap с использованием данного тег-хелпера следующим образом:

```

<environment names="Development">
 <link rel="stylesheet" href="~/css/bootstrap.min.css" />
</environment>
<environment names="Staging,Production">
 <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" />
</environment>

```


Атрибут names позволяет через запятую перечислить, к каким состояниям среды приложения применяется этот тег.
В данном случае, если проект на стадии Development (то есть в разработке), то подключается локальный файл bootstrap.min.css, который расположен в проекте
в папке wwwroot/css.


Если же проект находится в процессе тестирования (Staging) или уже опубликован (Production), то подключается файл bootstrap.min.css из CDN.


При обработке данного тега фреймворк использует значение переменной окружения ASPNETCORE_ENVIRONMENT. При разработке по умолчанию эта переменная имеет
значение "Development". Для управления этой переменной можно использовать файл launchSettings.json,
который расположен в проекте в папке Properties:
![environmenttaghelper и настройка окружения ASP.NET Core MVC и C#](https://metanit.com./pics/7.8.png)


Значение переменной ASPNETCORE_ENVIRONMENT привязано к определенному профилю. По умолчанию проект ASP.NET Core предлагает два профиля. Один называется
IISExpress, а другой по имени проекта.


Например, в данном случае проект находится в состоянии Development, поэтому выше определенный тег environment будет генерировать следующую разметку:

```
<link rel="stylesheet" href="/css/bootstrap.css" />
```


Если же мы изменим значение ASPNETCORE_ENVIRONMENT на Production:
![Переменная ASPNETCORE_ENVIRONMENT в ASP.NET Core MVC и C#](https://metanit.com./pics/7.9.png)


В этом случае тег environment сгенерирует следующую разметку:

```
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" />
```


Также обращаю внимание, что тег environment касается не только подключения стилей или скриптов, но и добавление любой разметки html. Например, определим в представлении
следующий код:

```

<environment names="Production">
 <p>Проект развернут на сервере</p>
</environment>

<environment names="Development">
 <p>Проект в состоянии разработки</p>
</environment>

```


Например, если приложение находится в состоянии "Development":
![Profile ASPNETCORE_ENVIRONMENT в ASP.NET Core MVC и C#](https://metanit.com./pics/7.10.png)











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

**Источник:** [https://metanit.com/sharp/aspnetmvc/7.5.php](https://metanit.com/sharp/aspnetmvc/7.5.php)
