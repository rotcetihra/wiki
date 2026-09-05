# Первый проект на ASP.NET Core MVC с .NET CLI

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC|Руководство по ASP.NET MVC]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 1. Введение в ASP.NET Core MVC|Глава 1. Введение в ASP.NET Core MVC]] / Первый проект на ASP.NET Core MVC с .NET CLI

[[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 1. Введение в ASP.NET Core MVC/Фреймворк ASP.NET Core MVC|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 1. Введение в ASP.NET Core MVC|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 1. Введение в ASP.NET Core MVC/Первый проект на ASP.NET Core MVC в Visual Studio|Вперёд]]

**Дата написания:** 05.09.2026

## Первый проект на ASP.NET Core MVC с .NET CLI

Последнее обновление: 25.11.2023




-

-

-














Создадим первое приложение на ASP.NET Core MVC. Для написания кода программы нам потребуется текстовый редактор для написания кода программы, а
для компиляции и запуска программы потребуется .NET SDK. Для его установки перейдем на официальный сайт по ссылке
[.NET SDK](https://dotnet.microsoft.com/en-us/download)
![Загрузка .NET SDK для ASP.NET Core](https://metanit.com./pics/1.17.png)


Выберем последнюю на данный момент версию - .NET SDK 7.


После установки .NET SDK для первого проекта определим какую-нибудь папку. Например, в моем случае это будет папка C:\dotnet\aspnetmvc\helloapp.
Откроем терминал/командную строку и перейдем к созданной папке проекта с помощью команды cd

```
cd C:\dotnet\aspnetmvc\helloapp
```


В данном случае мы для создания и запуска проекта мы будем использовать встроенную инфраструктуру .NET CLI, которая устанавливается вместе с .NET SDK.


Для создания проекта в .NET CLI применяется команда dotnet new, после которой указывается тип проекта. Для создания проекта ASP.NET Core MVC
предназначен шаблон mvc. Поэтому введем в терминале команду dotnet new mvc:

```

C:\dotnet\aspnetmvc\helloapp>dotnet new mvc
Шаблон "Веб-приложение ASP.NET Core (модель-представление-контроллер)" успешно создан.
Этот шаблон содержит технологии сторонних производителей, кроме Майкрософт. Дополнительные сведения см. в разделе https://aka.ms/aspnetcore/8.0-third-party-notices.

Идет обработка действий после создания...
Восстановление C:\dotnet\aspnetmvc\helloapp\helloapp.csproj:
 Определение проектов для восстановления...
 Восстановлен C:\dotnet\aspnetmvc\helloapp\helloapp.csproj (за 349 ms).
Восстановление выполнено.


C:\dotnet\aspnetmvc\helloapp>

```


После выполнения этой команды у нас будет создан следующий проект:
![Первый проект ASP.NET Core MVC на C# в Visual Studio Code](https://metanit.com./pics/1.28.png)


Структура создаваемого проекта будет отличаться от структуры простейшего проекта для ASP.NET Core. В частности, мы увидим ряд новых папок и файлов:


-

Dependencies: все добавленные в проект пакеты и библиотеки

-

wwwroot: этот узел (на жестком диске ему соответствует одноименная папка) предназначен для хранения статических файлов -
изображений, скриптов javascript, файлов css и т.д., которые используются приложением.

-

Controllers: папка для хранения контроллеров, используемых приложением. По умолчанию здесь уже есть один контроллер - Homecontroller

-

Models: каталог для хранения моделей. По умолчанию здесь создается модель ErrorviewModel

-

Views: каталог для хранения представлений. Здесь также по умолчанию добавляются ряд файлов - представлений

-

appsettings.json: хранит конфигурацию приложения

-

Program.cs: файл, который определяет входную точку в приложение ASP.NET Core


Фактически эта та же структура, что и у проекта по шаблону "web" за тем исключением, что здесь также добавлены по умолчанию папки для ключевых компонентов фреймворка MVC: контроллеров
и представлений. А также есть дополнительные узлы и файлы для управления зависимостями клиентской части приложения.


Запустим проект на выполение с помощью команды dotnet run:
![Запуск приложения ASP.NET Core MVC на C# в консоли](https://metanit.com./pics/1.29.png)


При запуске консоль отобразит адрес, по которому доступен проект. В моем случае это "http://localhost:5132". И если мы обратимся по адресу запущенного приложения, то сработает запрос к контроллеру по умолчанию - классу HomeController, который выберет для генерации ответа
нужное представление. И в итоге из представления будет создана html-страница, которую мы увидим в своем веб-браузере:
![Первый проект на ASP.NET MVC Core и C# в .NET CLI](https://metanit.com./pics/1.30.png)










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

**Источник:** [https://metanit.com/sharp/aspnetmvc/1.4.php](https://metanit.com/sharp/aspnetmvc/1.4.php)
