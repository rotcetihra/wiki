# SignalR Core. Первое приложение

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET 5 Core|Руководство по ASP.NET 5 Core]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET 5 Core/Глава 29. SignalR Core|Глава 29. SignalR Core]] / SignalR Core. Первое приложение

[[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET 5 Core/Глава 28. Глобализация и локализация/Хранение ресурсов в базе данных|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET 5 Core/Глава 29. SignalR Core|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET 5 Core/Глава 29. SignalR Core/Создание и конфигурация хабов|Вперёд]]

**Дата написания:** 05.09.2026

## SignalR Core. Первое приложение


Данное руководство устарело. Актуальное руководство: [Руководство по ASP.NET Core 7](https://metanit.com/sharp/aspnet6/)Последнее обновление: 23.12.2019




-

-

-














### Что такое SignalR


SignalR Core представляет библиотеку от компании Microsoft, которая предназначена для создания приложений, работающих в режиме
реального времени. В частности, ее можно использовать вместе с ASP.NET Core. SignalR использует двунаправленную связь для обмена сообщениями
между клиентом и сервером, благодаря чему сервер может отправлять в режиме реального времени всем клиентам некоторые данные.


Где может использоваться SignalR? Прежде всего это приложения, которые получают данные в реальном режиме времени, например, чаты, социальные сети,
игровые приложения, карты, приложения для аукционов, голосований и карт, панели управления, приложения для мониторинга данных и так далее.


Для обмена сообщениями между клиентом и сервером SignalR использует ряд механизмов:


-

WebSockets

-

Server-Side Events

-

Long Polling


Исходя из возможностей клиента и сервера инфраструктура SignalR выбирает наилучший механизм для взаимодействия. В частности, наиболее оптимальным является
WebSockets, соответственно если и клиент, и сервер позволяют использовать этот механизм, то взаимодействие идет через WebSockets.
Однако если WebSockets не поддерживается, то применяется Server-Side Events. И если SSE не поддерживается, то применяется
Long Polling.


### Поддерживаемые клиенты


SignalR обеспечивает взаимодействие клиента с сервером. Если на стороне сервера ожидаемое это приложение ASP.NET Core, то на стороне клиента
все намного интереснее. В частности, в качестве клиента в SignalR может выступать:


-

Приложение на JavaScript, запущенное на Node.js (поддерживается версия Node.js 8 и выше)

-

Приложение на JavaScript, которое работает в рамках браузеров Google Chrome (в том числе на Android), Microsoft Edge, Mozilla Firefox,
Opera, Safari (в том числе на iOS), Internet Explorer (только 11-я версия)

-

Приложение на .NET. Это может быть десктопное приложение WPF, Windows Forms, мобильное приложение Xamarin.

-

Приложение на языке Java


Также в прекрасном SignalR будущего ожидается поддержка приложений на C++ и Swift.


### Первое приложение


Создадим новый проект ASP.NET Core по типу Empty:
![SignalR в ASP.NET Core](https://metanit.com./pics/signalr1.png)


### Определение серверной части


При работы с SignalR на стороне сервера необходимо создать специальную сущность - хаб (hub). По сути хаб представляет класс, наследующийся от
класса Hub, который может обрабатывать запросы. Создадим новый хаб. Для этого добавим в проект следующий класс ChatHub:

```

using Microsoft.AspNetCore.SignalR;
using System.Threading.Tasks;

namespace SignalRApp
{
 public class ChatHub : Hub
 {
 public async Task Send(string message)
 {
 await this.Clients.All.SendAsync("Send", message);
 }
 }
}

```


Класс хаба наследуется от класса Hub. И здесь определен один метод Send(), который получает некоторое отправленное сообщение в
виде параметра message и затем с помощью вызова `await Clients.All.SendAsync("Send", message)` ретранслирует это сообщение всем подключенным клиентам.


Первый параметр метода `SendAsync()` указывает на метод, который будет получать ответ от сервера, а второй параметр представляет набор значений, которые
посылаются в ответе клиенту. То есть метод Send на клиенте получит значение параметра message. То есть наш хаб будет просто получать сообщение и транслировать его всем подключенным клиентам.


Но чтобы SignalR и хаб ChatHub заработали, надо сконфигурировать класс Startup:

```

using Microsoft.AspNetCore.Builder;
using Microsoft.Extensions.DependencyInjection;

namespace SignalRApp
{
 public class Startup
 {
 public void ConfigureServices(IServiceCollection services)
 {
 services.AddSignalR();
 }

 public void Configure(IApplicationBuilder app)
 {
 app.UseDeveloperExceptionPage();

 app.UseDefaultFiles();
 app.UseStaticFiles();

 app.UseRouting();

 app.UseEndpoints(endpoints =>
 {
 endpoints.MapHub<ChatHub>("/chat");
 });
 }
 }
}

```


Чтобы задействовать сервисы SignalR, в методе ConfigureServices вызывает метод:

```
services.AddSignalR();
```


А следующий вызов в методе Configure:

```

app.UseEndpoints(endpoints =>
{
 endpoints.MapHub<ChatHub>("/chat");
});

```


У объекта IEndpointRouteBuilder вызывается метод MapHub, который позволяет связать запросы и класс хаба.
В данном случае он устанавливает класс ChatHub в качестве обработчика запросов по пути "/chat". То есть, чтобы обратиться к хабу, строка запроса должна иметь вид типа
"http://localhost:5000/chat".


Стоит отметить, что если адрес сервера и адрес клиента не будут совпадать, то, возможно, потребуется настроить поддержку CORS, о которой речь идет в следующей главе.


### Создание клиентской части


Для создания клиентской части можно использовать различные способы. Например, можно использовать javascript, либо же использовать typescript, определить приложение на .NET или Java.
В данном случае мы будем использовать JavaScript, который будет выполняться на обычной странице html.


Для хранения статических файлов добавим в проект папку wwwroot.


Прежде всего на стороне клиента javascript нам потребуется подключить специальный js-скрипт. Для хранения всех необходимых javascript
вначале создадим в папке wwwroot новый подкаталог js.
Далее нажмем на эту папку правой кнопкой мыши и в контекстном меню выберем Add -> Client Side Library
![Install signalr core in ASP.NET Core](https://metanit.com./pics/signalr2.png)


Далее нам откроется окно добавления клиентских библиотек. Укажем в нем следующие опции:
![Установка signalr core в ASP.NET Core](https://metanit.com./pics/signalr3.png)


В поле Provider укажем значение unpkg.


В поле Library в качестве названия пакета введем @microsoft/signalr@latest.


Поскольку пакет содержит много файлов, которые нам могут не понадобиться, то отметим пункт Choose specific files:
и затем из списка файлов отметим только signalr.min.js, то есть минимизированную версию библиотеки. Но при желании и
необходимости можно выбрать и другие файлы.


И в конце в поле Target location укажем расположение, по которому будет сохранена библиотека, то есть путь wwwroot/js/signalr.


В итоге в проекте по пути wwwroot/js/signalr/dist/browser/ мы сможем найти файл signalr.min.js


В качестве альтернативы, особенно, если мы работаем не в Visual Studio, можно было бы загрузить пакет "@microsoft/signalr" через пакетный менеджер NPM,
например, определим следующий файл package.json:

```

{
 "version": "1.0.0",
 "name": "asp.net",
 "private": true,
 "devDependencies": {
 "@microsoft/signalr": "3.1.0"
 }
}

```


Теперь определим клиентскую часть. Добавим в папку wwwroot новый файл index.html. В итоге проект будет выглядеть следующим образом:
![Первый проект signalr в Asp.Net Core](https://metanit.com./pics/signalr4.png)


На странице index.html определим следующий код:

```

<!DOCTYPE html>
<html>
<head>
 <meta charset="utf-8" />
 <title>SignalR Chat - Metanit.com</title>
</head>
<body>
 <div id="inputForm">
 <input type="text" id="message" />
 <input type="button" id="sendBtn" value="Отправить" />
 </div>
 <div id="chatroom"></div>
 <script src="js/signalr/dist/browser/signalr.min.js"></script>
 <script>
 const hubConnection = new signalR.HubConnectionBuilder()
 .withUrl("/chat")
 .build();

 hubConnection.on("Send", function (data) {

 let elem = document.createElement("p");
 elem.appendChild(document.createTextNode(data));
 let firstElem = document.getElementById("chatroom").firstChild;
 document.getElementById("chatroom").insertBefore(elem, firstElem);

 });

 document.getElementById("sendBtn").addEventListener("click", function (e) {
 let message = document.getElementById("message").value;
 hubConnection.invoke("Send", message);
 });

 hubConnection.start();
 </script>
</body>
</html>

```


На странице определено текстовое поле для ввода сообщение и кнопка для его отправки. Под ними расположен блок chatroom, в который будут добавляться
полученные сообщения.


Внизу страницы подключается скрипт "signalr.min.js". Далее в коде javascript определена основная логика взаимодействия клиента с хабом.


Вначале определяется переменная, с помощью которой устанавливается подключение:

```

const hubConnection = new signalR.HubConnectionBuilder()
 .withUrl("/chat")
 .build();

```


Для взаимодействия с хабом ChatHub с помощью метода `build()` объекта HubConnectionBuilder создается объект hubConnection - объект подключения. Метод withUrl
устанавливает адрес, по котору приложение будет обращаться к хабу. Поскольку ChatHub на сервере
сопоставляется с адресом "/chat", то именно этот адрес и передается в withUrl.


Далее метод `hubConnection.on` устанавливает метод на стороне клиента, который будет получать данные от сервера:

```

hubConnection.on("Send", function (data) {

 let elem = document.createElement("p");
 elem.appendChild(document.createTextNode(data));
 let firstElem = document.getElementById("chatroom").firstChild;
 document.getElementById("chatroom").insertBefore(elem, firstElem);

});

```


В данном случае метод называется Send и фактически он представляют функцию, которая передается в качестве второго параметра. Эта функция
принимает один параметр data - те данные, которые в хабе отправляются клиенту. В самой функции с помощью стандартных функций javascript создается
элемент. В этот элемент помещается присланное с сервера сообщение. Затем элемент добавляется в начало элемента chatroom.


Далее устанавливается обработчик для кнопки, который вызывается при ее нажатии:

```

document.getElementById("sendBtn").addEventListener("click", function (e) {
 let message = document.getElementById("message").value;
 hubConnection.invoke("Send", message);
});

```


Для отправки данных хабу на сервер вызывается метод `hubConnection.invoke("Send", message)`, первый параметр которого представляет
метод хаба, обрабатывающий данный запрос, а второй параметр - данные, отправляемые на сервер.


И для начала соединения с сервером вызывается функция `hubConnection.start()`.


После запуска приложения в разных браузерах при отправке сообщения каждый браузер будет получать отправленное сообщение и выводить его на веб-страницу:
![SignalR в ASP.NET Core](https://metanit.com./pics/signalr5.png)


Теперь модифицируем приложение, что кроме сообщения пользователя также передавалось и его имя. Вначале изменим код класса ChatHub:

```

using Microsoft.AspNetCore.SignalR;
using System.Threading.Tasks;

namespace SignalRApp
{
 public class ChatHub : Hub
 {
 public async Task Send(string message, string userName)
 {
 await Clients.All.SendAsync("Send", message, userName);
 }
 }
}

```


Теперь метод Send принимает два параметра и значения обоих параметров ретранслирует всем подключенным клиентам.


И изменим страницу index.html:

```

<!DOCTYPE html>
<html>
<head>
 <meta charset="utf-8" />
 <title>SignalR Chat - Metanit.com</title>
</head>
<body>
 <div id="loginBlock">
 Введите логин:<br />
 <input id="userName" type="text" />
 <input id="loginBtn" type="button" value="Войти" />
 </div><br />

 <div id="header"></div><br />

 <div id="inputForm">
 <input type="text" id="message" />
 <input type="button" id="sendBtn" value="Отправить" />
 </div>
 <div id="chatroom"></div>
 <script src="js/signalr/dist/browser/signalr.min.js"></script>
 <script>
 const hubConnection = new signalR.HubConnectionBuilder()
 .withUrl("/chat")
 .build();

 let userName = '';
 // получение сообщения от сервера
 hubConnection.on('Send', function (message, userName) {

 // создаем элемент <b> для имени пользователя
 let userNameElem = document.createElement("b");
 userNameElem.appendChild(document.createTextNode(userName + ': '));

 // создает элемент <p> для сообщения пользователя
 let elem = document.createElement("p");
 elem.appendChild(userNameElem);
 elem.appendChild(document.createTextNode(message));

 var firstElem = document.getElementById("chatroom").firstChild;
 document.getElementById("chatroom").insertBefore(elem, firstElem);

 });

 // установка имени пользователя
 document.getElementById("loginBtn").addEventListener("click", function (e) {
 userName = document.getElementById("userName").value;
 document.getElementById("header").innerHTML = '<h3>Welcome ' + userName + '</h3>';
 });
 // отправка сообщения на сервер
 document.getElementById("sendBtn").addEventListener("click", function (e) {
 let message = document.getElementById("message").value;
 hubConnection.invoke("Send", message, userName);
 });

 hubConnection.start();
 </script>
</body>
</html>

```


Так как хаб на сервере отправляет клиентам два значения - имя пользователя и его сообщение, то соответственно на стороне клиента в функции,
которая регистрируется в методе hubConnection.on мы можем получить оба этих значения.


И теперь мы условно можем войти под разными пользователями в различных браузерах и отправлять друг другу сообщения:
![Работа с SignalR Core](https://metanit.com./pics/signalr6.png)










- Глава 1. Введение в ASP.NET Core


 - [ASP.NET Core - новая эпоха в развитии ASP.NET](//metanit.com/sharp/aspnet5/1.1.php)

 - [Начало работы с ASP.NET Core](//metanit.com/sharp/aspnet5/1.2.php)

 - [Проект ASP.NET Core в Visual Studio for Mac](//metanit.com/sharp/aspnet5/1.3.php)



- Глава 2. Основы ASP.NET Core


 - [Запуск приложения. Класс Program](//metanit.com/sharp/aspnet5/2.13.php)

 - [Класс Startup](//metanit.com/sharp/aspnet5/2.1.php)

 - [Конвейер обработки запроса и middleware](//metanit.com/sharp/aspnet5/2.2.php)

 - [Методы Use, Run и делегат RequestDelegate](//metanit.com/sharp/aspnet5/2.3.php)

 - [Методы Map и MapWhen](//metanit.com/sharp/aspnet5/2.22.php)

 - [Создание компонентов middleware](//metanit.com/sharp/aspnet5/2.4.php)

 - [Конвейер обработки запроса](//metanit.com/sharp/aspnet5/2.18.php)

 - [IWebHostEnvironment и окружение](//metanit.com/sharp/aspnet5/2.21.php)

 - [Статические файлы](//metanit.com/sharp/aspnet5/2.5.php)

 - [Работа со статическими файлами](//metanit.com/sharp/aspnet5/2.14.php)

 - [Обработка ошибок](//metanit.com/sharp/aspnet5/17.1.php)

 - [Работа с HTTPS](//metanit.com/sharp/aspnet5/18.6.php)



- Глава 3. Сервисы и Dependency Injection


 - [Сервисы и метод ConfigureServices](//metanit.com/sharp/aspnet5/6.1.php)

 - [Создание своих сервисов](//metanit.com/sharp/aspnet5/2.19.php)

 - [Передача зависимостей](//metanit.com/sharp/aspnet5/6.4.php)

 - [Жизненный цикл зависимостей](//metanit.com/sharp/aspnet5/6.2.php)

 - [Применение сервисов в middleware](//metanit.com/sharp/aspnet5/2.20.php)

 - [Singleton-объекты и scoped-сервисы](//metanit.com/sharp/aspnet5/6.5.php)



- Глава 4. Конфигурация


 - [Основы конфигурации](//metanit.com/sharp/aspnet5/2.6.php)

 - [Нефайловые провайдеры конфигурации](//metanit.com/sharp/aspnet5/2.16.php)

 - [Файловые провайдеры конфигурации](//metanit.com/sharp/aspnet5/2.12.php)

 - [Объединение конфигураций и установка сервиса IConfiguration](//metanit.com/sharp/aspnet5/2.23.php)

 - [Работа с конфигурацией](//metanit.com/sharp/aspnet5/2.17.php)

 - [Создание провайдера конфгурации](//metanit.com/sharp/aspnet5/2.15.php)

 - [Проекция конфигурации на классы](//metanit.com/sharp/aspnet5/2.9.php)

 - [Передача конфигурации через IOptions](//metanit.com/sharp/aspnet5/6.3.php)



- Глава 5. Состояние приложения. Куки. Сессии


 - [HttpContext.Items](//metanit.com/sharp/aspnet5/2.11.php)

 - [Куки](//metanit.com/sharp/aspnet5/2.25.php)

 - [Сессии](//metanit.com/sharp/aspnet5/2.26.php)



- Глава 6. Логгирование


 - [Ведение лога и ILogger](//metanit.com/sharp/aspnet5/2.10.php)

 - [Фабрика логгера и провайдеры логгирования](//metanit.com/sharp/aspnet5/2.29.php)

 - [Конфигурация и фильтрация логгирования](//metanit.com/sharp/aspnet5/2.28.php)

 - [Создание провайдера логгирования](//metanit.com/sharp/aspnet5/2.27.php)



- Глава 7. Маршрутизация


 - [Основы маршрутизации в ASP.NET Core](//metanit.com/sharp/aspnet5/11.1.php)

 - [RouterMiddleware](//metanit.com/sharp/aspnet5/11.12.php)

 - [Определение маршрутов](//metanit.com/sharp/aspnet5/11.2.php)

 - [Работа с маршрутами](//metanit.com/sharp/aspnet5/11.4.php)

 - [Ограничения маршрутов](//metanit.com/sharp/aspnet5/11.3.php)

 - [Создание ограничений маршрутов](//metanit.com/sharp/aspnet5/11.7.php)

 - [Создание своего маршрута](//metanit.com/sharp/aspnet5/11.8.php)



- Глава 8. ASP.NET Core MVC


 - [Введение в ASP.NET Core MVC](//metanit.com/sharp/aspnet5/3.1.php)

 - [Добавление MVC в пустой проект](//metanit.com/sharp/aspnet5/3.6.php)

 - [Первое приложение. Добавление моделей и базы данных](//metanit.com/sharp/aspnet5/3.2.php)

 - [Создание контроллера и инициализатора базы данных](//metanit.com/sharp/aspnet5/3.3.php)

 - [Добавление методов контроллера и представлений](//metanit.com/sharp/aspnet5/3.4.php)

 - [Добавление мастер-страницы и стилизации](//metanit.com/sharp/aspnet5/3.5.php)



- Глава 9. Контроллеры


 - [Контроллеры и их действия](//metanit.com/sharp/aspnet5/5.1.php)

 - [Передача данных в контроллер](//metanit.com/sharp/aspnet5/5.2.php)

 - [Результаты действий](//metanit.com/sharp/aspnet5/5.3.php)

 - [ContentResult и JsonResult](//metanit.com/sharp/aspnet5/5.4.php)

 - [Переадресация](//metanit.com/sharp/aspnet5/5.5.php)

 - [Отправка статусных кодов](//metanit.com/sharp/aspnet5/5.6.php)

 - [Отправка файлов](//metanit.com/sharp/aspnet5/5.7.php)

 - [Переопределение контроллеров](//metanit.com/sharp/aspnet5/5.8.php)

 - [Контекст контроллера](//metanit.com/sharp/aspnet5/5.9.php)

 - [Передача зависимостей в контроллер](//metanit.com/sharp/aspnet5/5.10.php)



- Глава 10. Представления


 - [Введение в представления](//metanit.com/sharp/aspnet5/7.1.php)

 - [Движок представлений Razor](//metanit.com/sharp/aspnet5/7.2.php)

 - [Передача данных в представление](//metanit.com/sharp/aspnet5/7.3.php)

 - [Мастер-страницы](//metanit.com/sharp/aspnet5/7.4.php)

 - [Файл _ViewImports.cshtml](//metanit.com/sharp/aspnet5/7.9.php)

 - [Частичные представления](//metanit.com/sharp/aspnet5/7.5.php)

 - [Внедрение зависимостей в представления](//metanit.com/sharp/aspnet5/7.7.php)

 - [Работа с формами](//metanit.com/sharp/aspnet5/7.8.php)

 - [Создание движка представлений](//metanit.com/sharp/aspnet5/7.10.php)



- Глава 11. Маршрутизация в ASP.NET Core MVC


 - [Маршрутизация в MVC с помощью конечных точек](//metanit.com/sharp/aspnet5/11.5.php)

 - [Маршрутизация с помощью RouterMiddleware. Метод UseMvc](//metanit.com/sharp/aspnet5/11.13.php)

 - [Атрибуты маршрутизации](//metanit.com/sharp/aspnet5/11.6.php)

 - [Области](//metanit.com/sharp/aspnet5/11.9.php)



- Глава 12. Модели


 - [Модели в ASP.NET Core MVC](//metanit.com/sharp/aspnet5/8.1.php)

 - [Модели представления View Model](//metanit.com/sharp/aspnet5/8.2.php)

 - [Привязка модели](//metanit.com/sharp/aspnet5/8.3.php)

 - [Передача данных в контроллер](//metanit.com/sharp/aspnet5/8.4.php)

 - [Управление привязкой](//metanit.com/sharp/aspnet5/8.5.php)

 - [Создание привязчика модели](//metanit.com/sharp/aspnet5/8.6.php)



- Глава 13. HTML-хелперы


 - [Создание HTML-хелперов](//metanit.com/sharp/aspnet5/9.1.php)

 - [HTML-хелперы элементов форм](//metanit.com/sharp/aspnet5/9.2.php)

 - [Строго типизированные хелперы](//metanit.com/sharp/aspnet5/9.3.php)

 - [Шаблонные хелперы](//metanit.com/sharp/aspnet5/9.4.php)

 - [Генерация ссылок](//metanit.com/sharp/aspnet5/9.5.php)

 - [URL-хелперы](//metanit.com/sharp/aspnet5/11.11.php)



- Глава 14. Tag-хелперы


 - [Введение в tag-хелперы](//metanit.com/sharp/aspnet5/10.1.php)

 - [AnchorTagHelper](//metanit.com/sharp/aspnet5/10.2.php)

 - [LinkTagHelper и ScriptTagHelper](//metanit.com/sharp/aspnet5/10.3.php)

 - [Tag-хелперы форм](//metanit.com/sharp/aspnet5/10.4.php)

 - [EnvironmentTagHelper](//metanit.com/sharp/aspnet5/10.6.php)

 - [CacheTagHelper](//metanit.com/sharp/aspnet5/10.7.php)

 - [Создание tag-хелперов](//metanit.com/sharp/aspnet5/10.8.php)

 - [Управление выводом tag-хелпера](//metanit.com/sharp/aspnet5/10.10.php)

 - [Контекст хелпера и получение зависимостей](//metanit.com/sharp/aspnet5/10.11.php)

 - [Атрибут HtmlTargetElement](//metanit.com/sharp/aspnet5/10.12.php)

 - [Tag-хелперы и сложные объекты и коллекции](//metanit.com/sharp/aspnet5/10.9.php)



- Глава 15. View Component


 - [Определение компонента представлений](//metanit.com/sharp/aspnet5/7.6.php)

 - [Передача данных в View Component](//metanit.com/sharp/aspnet5/7.11.php)

 - [Генерация контента в View Component](//metanit.com/sharp/aspnet5/7.12.php)

 - [ViewViewComponentResult и представления](//metanit.com/sharp/aspnet5/7.13.php)

 - [Асинхронные операции в View Component](//metanit.com/sharp/aspnet5/7.14.php)

 - [ViewComponentContext](//metanit.com/sharp/aspnet5/7.15.php)



- Глава 16. Метаданные и валидация модели


 - [Основы валидации](//metanit.com/sharp/aspnet5/19.1.php)

 - [Атрибуты валидации](//metanit.com/sharp/aspnet5/19.2.php)

 - [Валидация на стороне сервера](//metanit.com/sharp/aspnet5/19.3.php)

 - [Валидация на стороне клиента](//metanit.com/sharp/aspnet5/19.4.php)

 - [Tag-хелперы валидации](//metanit.com/sharp/aspnet5/10.5.php)

 - [Создание атрибута валидации. Самовалидация модели](//metanit.com/sharp/aspnet5/19.5.php)

 - [Аннотации данных](//metanit.com/sharp/aspnet5/19.6.php)



- Глава 17. Работа с данными в Entity Framework в MVC


 - [Подключение и создание базы данных в Entity Framework Core](//metanit.com/sharp/aspnet5/12.1.php)

 - [Операции с моделями. Создание и вывод](//metanit.com/sharp/aspnet5/12.2.php)

 - [Операции с моделями. Редактирование и удаление](//metanit.com/sharp/aspnet5/12.3.php)

 - [Сортировка](//metanit.com/sharp/aspnet5/12.4.php)

 - [Создание tag-хелпера сортировки](//metanit.com/sharp/aspnet5/12.5.php)

 - [Фильтрация](//metanit.com/sharp/aspnet5/12.6.php)

 - [Постраничная навигация](//metanit.com/sharp/aspnet5/12.7.php)

 - [Tag-хелпер для постраничной навигации](//metanit.com/sharp/aspnet5/12.8.php)

 - [Объединение сортировки, фильтрации и пагинации](//metanit.com/sharp/aspnet5/12.9.php)

 - [Tag-хелпер пагинации с сортировкой и фильтрацией](//metanit.com/sharp/aspnet5/12.10.php)



- Глава 18. Razor Pages


 - [Введение в Razor Pages](//metanit.com/sharp/aspnet5/29.1.php)

 - [Добавление RazorPages в пустой проект](//metanit.com/sharp/aspnet5/29.2.php)

 - [Обработка запросов. Передача форм](//metanit.com/sharp/aspnet5/29.3.php)

 - [Привязка свойств RazorPage к параметрам запроса](//metanit.com/sharp/aspnet5/29.4.php)

 - [Параметры маршрутов в Razor Pages](//metanit.com/sharp/aspnet5/29.5.php)

 - [Обработчики страницы](//metanit.com/sharp/aspnet5/29.6.php)

 - [Возвращение результата](//metanit.com/sharp/aspnet5/29.7.php)

 - [Переадресация и создание ссылок](//metanit.com/sharp/aspnet5/29.8.php)

 - [Подключение к базе данных](//metanit.com/sharp/aspnet5/29.9.php)

 - [Создание и вывод объектов из базы данных](//metanit.com/sharp/aspnet5/29.10.php)

 - [Изменение и удаление в базе данных](//metanit.com/sharp/aspnet5/29.11.php)



- Глава 19. Web API


 - [Введение в Web API](//metanit.com/sharp/aspnet5/23.1.php)

 - [Создание контроллера](//metanit.com/sharp/aspnet5/23.2.php)

 - [Тестирование контроллера](//metanit.com/sharp/aspnet5/23.3.php)

 - [Создание клиента для WEB API](//metanit.com/sharp/aspnet5/23.4.php)

 - [Валидация в Web API](//metanit.com/sharp/aspnet5/23.5.php)

 - [Content negotiation](//metanit.com/sharp/aspnet5/23.6.php)



- Глава 20. Фильтры


 - [Введение в фильтры](//metanit.com/sharp/aspnet5/18.1.php)

 - [Передача параметров в фильтры и установка зависимостей](//metanit.com/sharp/aspnet5/18.5.php)

 - [Фильтры ресурсов](//metanit.com/sharp/aspnet5/18.2.php)

 - [Фильтры действий](//metanit.com/sharp/aspnet5/18.3.php)

 - [Фильтры результатов](//metanit.com/sharp/aspnet5/18.4.php)

 - [Фильтры исключений](//metanit.com/sharp/aspnet5/17.2.php)

 - [Фильтры RazorPages](//metanit.com/sharp/aspnet5/18.7.php)



- Глава 21. Аутентификация и авторизация


 - [Аутентификация на основе куки. Часть 1](//metanit.com/sharp/aspnet5/15.1.php)

 - [Аутентификация на основе куки. Часть 2](//metanit.com/sharp/aspnet5/15.2.php)

 - [Авторизация](//metanit.com/sharp/aspnet5/15.3.php)

 - [ClaimPrincipal и объекты Claim](//metanit.com/sharp/aspnet5/15.4.php)

 - [Авторизация по ролям](//metanit.com/sharp/aspnet5/15.5.php)

 - [Авторизация на основе Claims](//metanit.com/sharp/aspnet5/15.6.php)

 - [Пример авторизации на основе Claims](//metanit.com/sharp/aspnet5/15.7.php)

 - [Создание ограничений для политики авторизации](//metanit.com/sharp/aspnet5/15.8.php)

 - [JWT-токены](//metanit.com/sharp/aspnet5/23.7.php)



- Глава 22. ASP.NET Core Identity


 - [Введение в ASP.NET Core Identity](//metanit.com/sharp/aspnet5/16.1.php)

 - [Основные классы в ASP.NET Core Identity](//metanit.com/sharp/aspnet5/16.11.php)

 - [Добавление Identity в проект с нуля](//metanit.com/sharp/aspnet5/16.2.php)

 - [Регистрация и создание пользователей в Identity](//metanit.com/sharp/aspnet5/16.3.php)

 - [Авторизация пользователей в Identity](//metanit.com/sharp/aspnet5/16.4.php)

 - [Управление пользователями](//metanit.com/sharp/aspnet5/16.7.php)

 - [Изменение пароля](//metanit.com/sharp/aspnet5/16.8.php)

 - [Валидация пароля](//metanit.com/sharp/aspnet5/16.9.php)

 - [Валидация пользователя](//metanit.com/sharp/aspnet5/16.10.php)

 - [Управление ролями](//metanit.com/sharp/aspnet5/16.13.php)

 - [Инициализация БД ролями и пользователями](//metanit.com/sharp/aspnet5/16.12.php)



- Глава 23. Клиентская разработка


 - [Бандлинг и минификация](//metanit.com/sharp/aspnet5/13.6.php)

 - [Менеджер Libman](//metanit.com/sharp/aspnet5/13.7.php)

 - [Пакетный менеджер NPM](//metanit.com/sharp/aspnet5/13.5.php)

 - [Gulp](//metanit.com/sharp/aspnet5/13.1.php)

 - [Grunt](//metanit.com/sharp/aspnet5/13.2.php)

 - [Препроцессоры Less и Sass](//metanit.com/sharp/aspnet5/13.4.php)



- Глава 24. Производительность и кэширование


 - [Кэширование с помощью MemoryCache](//metanit.com/sharp/aspnet5/14.1.php)

 - [Атрибут ResponseCache](//metanit.com/sharp/aspnet5/14.2.php)

 - [Сжатие ответа](//metanit.com/sharp/aspnet5/14.3.php)

 - [Кэширование статических файлов](//metanit.com/sharp/aspnet5/14.4.php)



- Глава 25. Сервер и публикация приложения


 - [Сервер](//metanit.com/sharp/aspnet5/2.7.php)

 - [Публикация на IIS](//metanit.com/sharp/aspnet5/20.1.php)

 - [Установка приложения в виде службы Windows](//metanit.com/sharp/aspnet5/20.2.php)



- Глава 26. Тестирование


 - [Введение в юнит-тесты](//metanit.com/sharp/aspnet5/22.1.php)

 - [Создание проекта юнит-тестов. Добавление xUnit](//metanit.com/sharp/aspnet5/22.2.php)

 - [Создание юнит-тестов](//metanit.com/sharp/aspnet5/22.3.php)

 - [Фреймворк Moq и moq-объекты](//metanit.com/sharp/aspnet5/22.4.php)

 - [Тестирование контроллера](//metanit.com/sharp/aspnet5/22.5.php)



- Глава 27. URL Rewriting


 - [Введение в URL Rewriting](//metanit.com/sharp/aspnet5/24.1.php)

 - [Правила IIS для URL Rewriting](//metanit.com/sharp/aspnet5/24.2.php)

 - [Применение правил для Apache](//metanit.com/sharp/aspnet5/24.3.php)

 - [Создание правил URL Rewriting](//metanit.com/sharp/aspnet5/24.4.php)



- Глава 28. Глобализация и локализация


 - [Определение культуры](//metanit.com/sharp/aspnet5/28.1.php)

 - [RequestLocalizationMiddleware](//metanit.com/sharp/aspnet5/28.2.php)

 - [Локализация строк. IStringLocalizer](//metanit.com/sharp/aspnet5/28.3.php)

 - [Ресурсы и локализация в контроллерах](//metanit.com/sharp/aspnet5/28.4.php)

 - [Локализация представлений](//metanit.com/sharp/aspnet5/28.5.php)

 - [Локализация аннотаций данных](//metanit.com/sharp/aspnet5/28.6.php)

 - [Переключение языка приложения](//metanit.com/sharp/aspnet5/28.7.php)

 - [Общие ресурсы локализации](//metanit.com/sharp/aspnet5/28.8.php)

 - [Хранение ресурсов в базе данных](//metanit.com/sharp/aspnet5/28.9.php)



- Глава 29. SignalR Core


 - [SignalR Core. Первое приложение](//metanit.com/sharp/aspnet5/30.1.php)

 - [Создание и конфигурация хабов](//metanit.com/sharp/aspnet5/30.2.php)

 - [Клиент javascript](//metanit.com/sharp/aspnet5/30.3.php)

 - [Контекст хаба, подключение и отключение клиентов](//metanit.com/sharp/aspnet5/30.4.php)

 - [Взаимодействие с клиентами](//metanit.com/sharp/aspnet5/30.5.php)

 - [IHubContext](//metanit.com/sharp/aspnet5/30.6.php)

 - [Отправка сложных объектов](//metanit.com/sharp/aspnet5/30.7.php)

 - [Аутентификация и авторизация на основе куки](//metanit.com/sharp/aspnet5/30.8.php)

 - [Аутентификация и авторизация с помощью токенов](//metanit.com/sharp/aspnet5/30.9.php)

 - [Пользователи](//metanit.com/sharp/aspnet5/30.10.php)

 - [Группы](//metanit.com/sharp/aspnet5/30.11.php)

 - [Клиент на Xamarin Forms](//metanit.com/sharp/aspnet5/30.12.php)



- Глава 30. CORS и кросс-доменные запросы


 - [Начало работы с CORS](//metanit.com/sharp/aspnet5/31.1.php)

 - [Конфигурация CORS](//metanit.com/sharp/aspnet5/31.2.php)

 - [Политики CORS](//metanit.com/sharp/aspnet5/31.3.php)

 - [Глобальная и локальная настройка CORS](//metanit.com/sharp/aspnet5/31.5.php)

 - [CORS в MVC](//metanit.com/sharp/aspnet5/31.4.php)



- Глава 31. Dapper


 - [Работа с Dapper в ASP.NET Core](//metanit.com/sharp/aspnet5/26.1.php)



- Глава 32. React.JS


 - [Подключение React в ASP.NET Core](//metanit.com/sharp/aspnet5/25.1.php)

 - [Взаимодействие React.JS и ASP.NET Core](//metanit.com/sharp/aspnet5/25.2.php)



- Глава 33. Дополнительные статьи


 - [Отправка email в ASP.NET Core](//metanit.com/sharp/aspnet5/21.1.php)

 - [Загрузка файлов на сервер](//metanit.com/sharp/aspnet5/21.3.php)










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

**Источник:** [https://metanit.com/sharp/aspnet5/30.1.php](https://metanit.com/sharp/aspnet5/30.1.php)
