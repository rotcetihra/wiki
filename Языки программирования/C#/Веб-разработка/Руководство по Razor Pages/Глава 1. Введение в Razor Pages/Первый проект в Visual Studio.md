# Первый проект в Visual Studio

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по Razor Pages|Руководство по Razor Pages]] / [[Языки программирования/C#/Веб-разработка/Руководство по Razor Pages/Глава 1. Введение в Razor Pages|Глава 1. Введение в Razor Pages]] / Первый проект в Visual Studio

[[Языки программирования/C#/Веб-разработка/Руководство по Razor Pages/Глава 1. Введение в Razor Pages/Введение в Razor Pages. Первый проект с .NET CLI|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по Razor Pages/Глава 1. Введение в Razor Pages|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по Razor Pages/Глава 1. Введение в Razor Pages/Добавление RazorPages в пустой проект|Вперёд]]

**Дата написания:** 05.09.2026

## Первый проект в Visual Studio

Последнее обновление: 26.11.2023




-

-

-














Для создания приложений на основе Razor Pages в Visual Studio имеется готовый шаблон -
ASP.NET Core Web App (Razor Pages). Выберем его в качестве шаблона проекта:
![шаблон проекта Razor Pages в ASP.NET Core и C#](https://metanit.com./pics/1.1.png)


На следующем шаге необходимо будет указать имя проекта и его расположение. Допустим, проект будет называться HelloRazorPagesApp:
![первый проект Razor Pages в ASP.NET Core и C# в Visual Studio](https://metanit.com./pics/1.2.png)


Далее можно будет указать версию .NET и еще ряд настроек. Оставим все настройки по умолчанию и нажмем на кнопку Create для создания проекта:
![настройка проекта Razor Pages на ASP.NET Core и C# в Visual Studio](https://metanit.com./pics/1.3.png)


После создания проект будет иметь следующую структуру:
![Структура проекта Razor Pages в ASP.NET Core и C# в Visual Studio](https://metanit.com./pics/1.4.png)


Эта та же структура, которая создается с помощью .NET CLI:


-

Dependencies: все добавленные в проект пакеты и библиотеки

-

Properties: содержит настройки проекта, в частности, файл launchSettings.json, который определяет настройки запуска проекта

-

wwwroot: эта папка предназначен для хранения статических файлов. По умолчанию здесь уже есть ряд скриптов javascript и файлов css,
в частности, файлы фреймворка bootstrap и библиотек валидации.

-

Pages: содержит все страницы Razor. По умолчанию здесь имеются следующие файлы:


 -

_Layout.cshtml: мастер-страница, в которую вставляются страницы Razor

 -

_ViewStart.cshtml: задает мастер-страницу

 -

_ViewImports.cshtml: определяет директивы Razor, которые добавляются на каждую страницу Razor

 -

_ValidationScriptsPartial.cshtml: частичное представление, которое подключает js-скрипты валидации на стороне клиента

 -

Index.cshtml, Error.cshtml и Privacy.cshtml:
собственно страницы Razor, которые определяют визуальную часть страницы и логику обработки запроса.


-

appsettings.json: хранит конфигурацию приложения

-

Program.cs: файл, который определяет класс Program, с которого начинается работа приложения. То есть это входная точка в приложение.


И если мы запустим проект на выполнение, то сработает запрос к странице Razor по умолчанию - странице Index.cshtml, на основе которой и будет сгенерирована
html-страница, которую мы увидим в своем веб-браузере:
![Первый проект на Razor Pages в ASP.NET Core и C#](https://metanit.com./pics/1.5.png)











- Глава 1. Введение в Razor Pages


 - [Введение в Razor Pages. Первый проект с .NET CLI](//metanit.com/sharp/razorpages/1.3.php)

 - [Первый проект в Visual Studio](//metanit.com/sharp/razorpages/1.1.php)

 - [Добавление RazorPages в пустой проект](//metanit.com/sharp/razorpages/1.2.php)



- Глава 2. Основы Razor Pages


 - [Определение страниц Razor](//metanit.com/sharp/razorpages/2.1.php)

 - [Синтаксис Razor](//metanit.com/sharp/razorpages/2.2.php)

 - [Модель страницы Razor](//metanit.com/sharp/razorpages/2.3.php)

 - [Обработка запросов. Контекст страницы Razor](//metanit.com/sharp/razorpages/2.4.php)

 - [Передача данных на страницу Razor в GET-запросе](//metanit.com/sharp/razorpages/2.5.php)

 - [POST-запросы и отправка форм](//metanit.com/sharp/razorpages/2.6.php)

 - [Привязка свойств страниц и моделей Razor к параметрам запроса](//metanit.com/sharp/razorpages/2.7.php)

 - [Параметры маршрутов](//metanit.com/sharp/razorpages/2.8.php)

 - [Обработчики страницы](//metanit.com/sharp/razorpages/2.9.php)

 - [Возвращение результата](//metanit.com/sharp/razorpages/2.10.php)

 - [Отправка файлов](//metanit.com/sharp/razorpages/2.11.php)

 - [Отправка статусных кодов](//metanit.com/sharp/razorpages/2.12.php)

 - [Переадресация](//metanit.com/sharp/razorpages/2.13.php)

 - [Передача зависимостей на страницу](//metanit.com/sharp/razorpages/2.14.php)

 - [ViewBag и ViewData](//metanit.com/sharp/razorpages/2.15.php)



- Глава 3. Определение пользовательского интерфейса


 - [Мастер-страницы layout](//metanit.com/sharp/razorpages/3.1.php)

 - [Файл _ViewImports.cshtml](//metanit.com/sharp/razorpages/3.2.php)

 - [Введение в tag-хелперы](//metanit.com/sharp/razorpages/3.3.php)

 - [Создание ссылок](//metanit.com/sharp/razorpages/3.4.php)

 - [Работа с формами. Tag-хелперы форм](//metanit.com/sharp/razorpages/3.5.php)



- Глава 4. Работа с базой данных через Entity Framework


 - [Подключение к базе данных](//metanit.com/sharp/razorpages/4.1.php)

 - [Создание и вывод объектов из базы данных](//metanit.com/sharp/razorpages/4.2.php)

 - [Изменение и удаление в базе данных](//metanit.com/sharp/razorpages/4.3.php)










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

**Источник:** [https://metanit.com/sharp/razorpages/1.1.php](https://metanit.com/sharp/razorpages/1.1.php)
