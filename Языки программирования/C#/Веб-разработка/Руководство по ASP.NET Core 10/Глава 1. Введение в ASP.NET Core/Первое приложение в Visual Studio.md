# Первое приложение в Visual Studio

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10|Руководство по ASP.NET Core 10]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 1. Введение в ASP.NET Core|Глава 1. Введение в ASP.NET Core]] / Первое приложение в Visual Studio

[[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 1. Введение в ASP.NET Core/Первое приложение на ASP.NET Core с .NET CLI|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 1. Введение в ASP.NET Core|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 2. Основы в ASP.NET Core/Создание и запуск приложения. WebApplication и WebApplicationBuilder|Вперёд]]

**Дата написания:** 05.09.2026

## Первое приложение в Visual Studio

Последнее обновление: 25.11.2023




-

-

-














В прошлой теме было рассмотрено создание первого проекта ASP.NET Core с помощью .NET CLI с компиляцией и запуском проекта в терминале. Это самый простой способ для создания
приложений ASP.NET. Однако также мы можем использовать среду разработки Visual Studio, которая упрощает многие аспекты по работе с проектом ASP.NET. Рассмотрим, как создавать проект в
Visual Studio.


Итак, в начале загрузим бесплатный выпуск среды - Visual Studio Community 2022 по следующему адресу:
[Microsoft Visual Studio 2022](https://visualstudio.microsoft.com/ru/downloads/)
![Установка Visual Studio 2022](https://metanit.com./pics/1.7.png)


После загрузки запустим программу установщика. В открывшемся окне нам будет предложено выбрать те компоненты, которые мы хотим установить вместе Visual Studio.
Стоит отметить, что Visual Studio - очень функциональная среда разработки и позволяет разрабатывать приложения с помощью множества языков и платформ.
В нашем случае нам будет интересовать прежде всего C# и .NET.


Чтобы добавить в Visual Studio поддержку проектов для ASP.NET Core, в программе установки среди рабочих нагрузок можно выбрать только пункт
ASP.NET и разработка веб-приложений. Можно выбрать и больше опций или вообще
все опции, однако стоит учитывать свободный размер на жестком диске - чем больше опций будет выбрано, соответственно тем больше места на диске будет занято.
![Установка Visual Studio 2022](https://metanit.com./pics/1.8.png)


И при инсталляции Visual Studio на ваш компьютер будут установлены все необходимые инструменты для разработки программ, в том
числе фреймворк .NET.


После завершения установки создадим первый проект на ASP.NET Core. Вначале откроем Visual Studio. На стартовом экране выберем
Create a new project (Создать новый проект)
![Создание первого проекта в Visual Studio 2022](https://metanit.com./pics/1.9.png)


На следующем окне в качестве типа проекта выберем ASP.NET Core Empty
![Проект консольного приложения на C# и .NET в Visual Studio 2022](https://metanit.com./pics/1.10.png)


Далее на следующем этапе нам будет предложено указать имя проекта и каталог, где будет располагаться проект.
![Создание первого приложения на C#](https://metanit.com./pics/1.1.png)


В поле Project Name дадим проекту какое-либо название. В моем случае это HelloApp.


На следующем окне Visual Studio предложит нам выбрать версию .NET, которая будет использоваться для проекта. Выбрем здесь последнюю доступную версию.
![Установка C# и .NET в Visual Studio](https://metanit.com./pics/1.13.png)


Кроме того, здесь с помощью флажка Configure for HTTPS можно установить использование протокола https. По умолчанию этот флажок отмечен,
это значит, что проект по умолчанию будет использовать протокол https.


Другой флажок - Enable Docker позволяет задействовать Docker. Если этот флажок установлен, то в поле ниже можно будет выбрать ОС, которая будет
использоваться под Docker. Но в данном случае оставим этот флажок неотмеченным.


Третий флажок - Do not use level statements позволяет, как и в консольных проектах, отключить поддержку выражений верхнего уровня.
Этот флажок также оставим неотмеченным.


Оставим все остальные настройки по умолчанию и нажмем на кнопку Create (Создать) для создания проекта. После этого Visual Studio создаст и откроет нам проект:
![Первый проект ASP.NET Core на C#](https://metanit.com./pics/1.2.png)


### Структура проекта ASP.NET Core


Рассмотрим базовую структуру стандартного проекта ASP.NET Core в Visual Studio. Проект ASP.NET Core Empty содержит очень простую структуру - необходимый минимум для запуска приложения:


-

Connected Services: подключенные сервисы из Azure

-

Dependencies: все добавленные в проект пакеты и библиотеки, иначе говоря зависимости

-

Properties: узел, который содержит некоторые настройки проекта. В частности, в файле launchSettings.json описаны
настройки запуска проекта, например, адреса, по которым будет запускаться приложение.

-

appsettings.json: файл конфигурации проекта в формате json

-

appsettings.Development.json: версия файла конфигурации приложения, которая используется в процессе разработки

-

Program.cs: главный файл приложения, с которого и начинается его выполнение. Код этого файла настраивает и запускает веб-приложение


### Запуск проекта


Проект по умолчанию не представляет какой-то грандиозной функциональности, тем не менее этот проект мы уже можем запустить. Итак, запустим проект.
При запуске нам может отобразиться окно, где надо подтвердить доверие для серфиката SSL, а также его установку
![Потверждение сертификата SSL при запуске приложения ASP.NET Core](https://metanit.com./pics/1.3.png)
![Установка сертификата SSL при запуске приложения ASP.NET Core](https://metanit.com./pics/1.5.png)


И после подтверждения и установки сертификата отобразиться консоль, где выводися некоторая базовая информация о приложении:


И, кроме того, будет запущен браузер, где мы сможем лицезреть строку "Hello World!" - результат работы кода по умолчанию из файла Program.cs:
![Первое приложение на ASP.NET Core](https://metanit.com./pics/1.4.png)











- Глава 1. Введение в ASP.NET Core


 - [Что такое ASP.NET Core](//metanit.com/sharp/aspnet6/1.1.php)

 - [Первое приложение на ASP.NET Core с .NET CLI](//metanit.com/sharp/aspnet6/1.3.php)

 - [Первое приложение в Visual Studio](//metanit.com/sharp/aspnet6/1.2.php)



- Глава 2. Основы в ASP.NET Core


 - [Создание и запуск приложения. WebApplication и WebApplicationBuilder](//metanit.com/sharp/aspnet6/2.1.php)

 - [Конвейер обработки запроса и middleware](//metanit.com/sharp/aspnet6/2.2.php)

 - [Метод Run и определение терминального middleware](//metanit.com/sharp/aspnet6/2.3.php)

 - [HttpResponse. Отправка ответа](//metanit.com/sharp/aspnet6/2.4.php)

 - [HttpRequest. Получение данных запроса](//metanit.com/sharp/aspnet6/2.5.php)

 - [Отправка файлов](//metanit.com/sharp/aspnet6/2.6.php)

 - [Отправка форм](//metanit.com/sharp/aspnet6/2.8.php)

 - [Переадресация](//metanit.com/sharp/aspnet6/2.9.php)

 - [Отправка и получение json](//metanit.com/sharp/aspnet6/2.10.php)

 - [Создание простейшего API](//metanit.com/sharp/aspnet6/2.11.php)

 - [Загрузка файлов на сервер](//metanit.com/sharp/aspnet6/2.12.php)

 - [Метод Use](//metanit.com/sharp/aspnet6/2.7.php)

 - [Создание ветки конвейера. UseWhen и MapWhen](//metanit.com/sharp/aspnet6/2.13.php)

 - [Метод Map](//metanit.com/sharp/aspnet6/2.14.php)

 - [Классы middleware](//metanit.com/sharp/aspnet6/2.15.php)

 - [Построение конвейера обработки запроса](//metanit.com/sharp/aspnet6/2.16.php)

 - [IWebHostEnvironment и окружение](//metanit.com/sharp/aspnet6/2.17.php)



- Глава 3. Dependency Injection


 - [Внедрение зависимостей и IServiceCollection](//metanit.com/sharp/aspnet6/4.1.php)

 - [Создание сервисов](//metanit.com/sharp/aspnet6/4.2.php)

 - [Получение зависимостей](//metanit.com/sharp/aspnet6/4.3.php)

 - [Жизненный цикл зависимостей](//metanit.com/sharp/aspnet6/4.4.php)

 - [Применение сервисов в классах middleware](//metanit.com/sharp/aspnet6/4.5.php)

 - [Scoped-сервисы в singleton-объектах](//metanit.com/sharp/aspnet6/4.6.php)

 - [Множественная регистрация сервисов](//metanit.com/sharp/aspnet6/4.7.php)



- Глава 4. Маршрутизация


 - [Конечные точки. Метод Map](//metanit.com/sharp/aspnet6/3.1.php)

 - [Параметры маршрута](//metanit.com/sharp/aspnet6/3.2.php)

 - [Ограничения маршрутов](//metanit.com/sharp/aspnet6/3.3.php)

 - [Создание ограничений маршрутов](//metanit.com/sharp/aspnet6/3.4.php)

 - [Передача зависимостей в конечные точки](//metanit.com/sharp/aspnet6/3.5.php)

 - [Сопоставление запроса с конечной точкой](//metanit.com/sharp/aspnet6/3.6.php)

 - [Сочетание конечных точек с другими middleware](//metanit.com/sharp/aspnet6/3.7.php)

 - [Получение параметров строки запроса](//metanit.com/sharp/aspnet6/3.8.php)



- Глава 5. Статические файлы


 - [Установка каталога статических файлов. UseStaticFiles](//metanit.com/sharp/aspnet6/5.1.php)

 - [Работа со статическими файлами](//metanit.com/sharp/aspnet6/5.2.php)

 - [Статические файлы и MapStaticAssets](//metanit.com/sharp/aspnet6/5.3.php)



- Глава 6. Конфигурация


 - [Основы конфигурации](//metanit.com/sharp/aspnet6/6.1.php)

 - [Нефайловые провайдеры конфигурации](//metanit.com/sharp/aspnet6/6.2.php)

 - [Конфигурация в файлах JSON, XML и Ini](//metanit.com/sharp/aspnet6/6.3.php)

 - [Конфигурация по умолчанию и объединение конфигураций](//metanit.com/sharp/aspnet6/6.4.php)

 - [Анализ конфигурации](//metanit.com/sharp/aspnet6/6.5.php)

 - [Создание провайдера конфгурации](//metanit.com/sharp/aspnet6/6.6.php)

 - [Проекция конфигурации на классы](//metanit.com/sharp/aspnet6/6.7.php)

 - [Передача конфигурации через IOptions](//metanit.com/sharp/aspnet6/6.8.php)



- Глава 7. Логгирование


 - [Ведение лога и ILogger](//metanit.com/sharp/aspnet6/7.1.php)

 - [Фабрика логгера и провайдеры логгирования](//metanit.com/sharp/aspnet6/7.2.php)

 - [Конфигурация и фильтрация логгирования](//metanit.com/sharp/aspnet6/7.3.php)

 - [Создание провайдера логгирования](//metanit.com/sharp/aspnet6/7.4.php)



- Глава 8. Состояние приложения. Куки. Сессии


 - [HttpContext.Items](//metanit.com/sharp/aspnet6/8.1.php)

 - [Куки](//metanit.com/sharp/aspnet6/8.2.php)

 - [Сессии](//metanit.com/sharp/aspnet6/8.3.php)



- Глава 9. Обработка ошибок


 - [Обработка исключений](//metanit.com/sharp/aspnet6/9.1.php)

 - [Обработка ошибок HTTP](//metanit.com/sharp/aspnet6/9.2.php)



- Глава 10. Results API


 - [Введение в Results API](//metanit.com/sharp/aspnet6/10.1.php)

 - [Отправка текста и json в Results API](//metanit.com/sharp/aspnet6/10.2.php)

 - [Переадресация в Results API](//metanit.com/sharp/aspnet6/10.3.php)

 - [Отправка статусных кодов в Results API](//metanit.com/sharp/aspnet6/10.4.php)

 - [Отправка файлов в Results API](//metanit.com/sharp/aspnet6/10.5.php)

 - [Определение своего типа IResult](//metanit.com/sharp/aspnet6/10.6.php)



- Глава 11. Web API


 - [Пример приложения Web API](//metanit.com/sharp/aspnet6/11.1.php)



- Глава 12. Работа с базой данных и Entity Framework


 - [Подключение Entity Framework](//metanit.com/sharp/aspnet6/12.1.php)

 - [Основные операции с данными в Entity Framework Core](//metanit.com/sharp/aspnet6/12.2.php)



- Глава 13. Аутентификация и авторизация


 - [Введение в аутентификацию и авторизацию](//metanit.com/sharp/aspnet6/13.1.php)

 - [Аутентификация с помощью JWT-токенов](//metanit.com/sharp/aspnet6/13.2.php)

 - [Авторизация с помощью JWT-токенов в клиенте JavaScript](//metanit.com/sharp/aspnet6/13.3.php)

 - [Аутентификация с помощью куки](//metanit.com/sharp/aspnet6/13.4.php)

 - [HttpContext.User, ClaimPrincipal и ClaimsIdentity](//metanit.com/sharp/aspnet6/13.5.php)

 - [ClaimPrincipal и объекты Claim](//metanit.com/sharp/aspnet6/13.6.php)

 - [Авторизация по ролям](//metanit.com/sharp/aspnet6/13.7.php)

 - [Авторизация на основе Claims](//metanit.com/sharp/aspnet6/13.8.php)

 - [Создание ограничений для авторизации](//metanit.com/sharp/aspnet6/13.9.php)



- Глава 14. CORS и кросс-доменные запросы


 - [Подключение CORS в приложении](//metanit.com/sharp/aspnet6/14.1.php)

 - [Конфигурация CORS](//metanit.com/sharp/aspnet6/14.2.php)

 - [Политики CORS](//metanit.com/sharp/aspnet6/14.3.php)

 - [Глобальная и локальная настройка CORS](//metanit.com/sharp/aspnet6/14.4.php)



- Глава 15. URL Rewriting


 - [Введение в URL Rewriting](//metanit.com/sharp/aspnet6/15.1.php)

 - [Правила IIS для URL Rewriting](//metanit.com/sharp/aspnet6/15.2.php)

 - [Применение правил Apache для URL Rewriting](//metanit.com/sharp/aspnet6/15.3.php)

 - [Создание правил URL Rewriting](//metanit.com/sharp/aspnet6/15.4.php)



- Глава 16. Клиентская разработка


 - [Бандлинг и минификация](//metanit.com/sharp/aspnet6/16.1.php)

 - [Пакетный менеджер Libman](//metanit.com/sharp/aspnet6/16.2.php)

 - [Пакетный менеджер NPM](//metanit.com/sharp/aspnet6/16.3.php)



- Глава 17. Кэширование


 - [Кэширование с помощью MemoryCache](//metanit.com/sharp/aspnet6/17.1.php)

 - [Распределенное кэширование. Redis](//metanit.com/sharp/aspnet6/17.2.php)

 - [Сжатие ответа](//metanit.com/sharp/aspnet6/17.3.php)

 - [Кэширование статических файлов](//metanit.com/sharp/aspnet6/17.4.php)

 - [Кэширование ответа и OutputCache](//metanit.com/sharp/aspnet6/17.5.php)



- Глава 18. Мониторинг работоспособности приложения


 - [Health Check Middleware](//metanit.com/sharp/aspnet6/18.1.php)










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

**Источник:** [https://metanit.com/sharp/aspnet6/1.2.php](https://metanit.com/sharp/aspnet6/1.2.php)
