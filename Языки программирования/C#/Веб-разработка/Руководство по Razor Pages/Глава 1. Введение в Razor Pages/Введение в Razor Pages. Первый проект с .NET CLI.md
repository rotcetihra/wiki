# Введение в Razor Pages. Первый проект с .NET CLI

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по Razor Pages|Руководство по Razor Pages]] / [[Языки программирования/C#/Веб-разработка/Руководство по Razor Pages/Глава 1. Введение в Razor Pages|Глава 1. Введение в Razor Pages]] / Введение в Razor Pages. Первый проект с .NET CLI

[[Языки программирования/C#/Веб-разработка/Руководство по Razor Pages/Глава 1. Введение в Razor Pages|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по Razor Pages/Глава 1. Введение в Razor Pages/Первый проект в Visual Studio|Вперёд]]

**Дата написания:** 05.09.2026

## Что такое Razor Pages. Первый проект с .NET CLI

Последнее обновление: 26.11.2023




-

-

-














Начиная с версии 2.0 в ASP.NET Core была добавлена такая платформа, как Razor Pages.
Razor Pages предоставляют технологию, альтернативную фреймворку MVC(Model-View-Controller). В тоже время Razor Pages в плане организации считается проще чем MVC.


Приложение в Razor Pages организовано в виде страниц Razor. Каждая страница представляет пользовательский интерфейс и связанную с ним логику, причем
определение пользовательского интерфейса от связанной с ним логики, что облегчает разработку приложения и его тестирование. Для определения пользовательского интерфейса применяется
движок Razor, а для описания связанной со страницей логики - C#.


Для начала работы с Razor Pages создадим новый проект ASP.NET Core с .NET CLI. Для создания приложений на основе Razor Pages в .NET CLI имеется готовый шаблон -
webapp, razor.


Итак, определим каталог для проекта Razor Pages. Например, в моем случае это будет каталог C:\dotnet\razorpages\helloapp. Перейдем к этому каталогу в терминале
с помощью команды cd:

```
cd C:\dotnet\razorpages\helloapp
```


Затем для создания проекта в этой папке выполним команду dotnet new webapp:

```

C:\dotnet\razorpages\helloapp>dotnet new webapp
Шаблон "Веб-приложение ASP.NET Core" успешно создан.
Этот шаблон содержит технологии сторонних производителей, кроме Майкрософт. Дополнительные сведения см. в разделе https://aka.ms/aspnetcore/8.0-third-party-notices.

Идет обработка действий после создания...
Восстановление C:\dotnet\razorpages\helloapp\helloapp.csproj:
 Определение проектов для восстановления...
 Восстановлен C:\dotnet\razorpages\helloapp\helloapp.csproj (за 431 ms).
Восстановление выполнено.


C:\dotnet\razorpages\helloapp>

```


После выполнения команды будет создан следующий проект:
![Структура проекта Razor Pages в ASP.NET Core и C# с помощью .NET CLI](https://metanit.com./pics/1.13.png)


Частично, этот тип проекта будет повторять общую структуру проектов ASP.NET Core. Главным же отличием данного проекта от других типов проектов ASP.NET Core будет наличие папки Pages. Эта папка содержит все страницы Razor,
которые есть в проекте по умолчанию. Вкратце организация проекта:


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

appsettings.Development.json: хранит конфигурацию приложения для стадии разработки

-

appsettings.json: хранит конфигурацию приложения

-

helloapp.csproj: главный файл проекта, который определяет его конфигурацию

-

Program.cs: файл, который определяет класс Program, с которого начинается работа приложения. То есть это входная точка в приложение.


Каждая страница Razor представляет файл с расширением .cshtml и содержит смесь кода html и конструкций C#. С каждой страницей Razor связан файл
отделенного кода логики на C#. Например,
с файлом Index.cshtml, который определяет визуальную часть с помощью синтаксиса Razor (HTML + C#), связан файл Index.cshtml.cs,
который определяет логику страницы или ее поведение с помощью кода C#.


Аналогично обстоит дело с другими страницами - Error.cshtml и Privacy.cshtml, с которыми связаны соответственно файлы кода
Error.cshtml.cs и Privacy.cshtml.cs


### Подключение Razor Pages


Как работают Razor Pages? Чтобы разобраться в этом, откроем файл Program.cs:

```

var builder = WebApplication.CreateBuilder(args);

// подключение сервисов razor pages
builder.Services.AddRazorPages();

var app = builder.Build();

if (!app.Environment.IsDevelopment())
{
 app.UseExceptionHandler("/Error");
 app.UseHsts();
}

app.UseHttpsRedirection();
app.UseStaticFiles();

app.UseRouting();

app.UseAuthorization();

app.MapRazorPages();

app.Run();

```


Здесь надо отметить два момента. Во-первых, для использования Razor Pages необходимо подключить соответствующие сервисы:

```
builder.Services.AddRazorPages();
```


Для подключения сервисов Razor Pages применяется метод AddRazorPages.


Другим важным моментом является маршрутизация или как Razor Pages сопоставляются с запросами. В частности, в файле Program.cs также можно найти следующий вызов:

```

app.MapRazorPages();

```


Данный вызов добавляет поддержку системы маршрутизации, которая позволяет сопоставить строку запроса URL с определенной страницей Razor на основании ее расположения в
проекте в папке Pages. Например, запросу /Index будет соответствовать страница /Pages/Index.cshtml.
Затем на основе страницы Razor будет генерироваться html-страница, отправляемая в ответ клиенту.


Запустим проект с помощью команды

```
dotnet run
```

![Запуск проекта Razor Pages ASP.NET Core на C# с помощью .NET CLI](https://metanit.com./pics/1.14.png)


Консоль отобразит адрес зарущенного приложения (в моем случае это http://localhost:5183). Обратимся по этому адресу, и сработает запрос к странице Razor по умолчанию - странице Index.cshtml, на основе которой и будет сгенерирована
html-страница, которую мы увидим в своем веб-браузере:
![Первое приложение на Razor Pages в ASP.NET Core и C# с .NET CLI](https://metanit.com./pics/1.15.png)











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

**Источник:** [https://metanit.com/sharp/razorpages/1.3.php](https://metanit.com/sharp/razorpages/1.3.php)
