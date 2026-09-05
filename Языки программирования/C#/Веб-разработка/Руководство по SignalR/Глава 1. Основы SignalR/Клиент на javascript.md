# Клиент на javascript

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по SignalR|Руководство по SignalR]] / [[Языки программирования/C#/Веб-разработка/Руководство по SignalR/Глава 1. Основы SignalR|Глава 1. Основы SignalR]] / Клиент на javascript

[[Языки программирования/C#/Веб-разработка/Руководство по SignalR/Глава 1. Основы SignalR/Создание и конфигурация хабов|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по SignalR/Глава 1. Основы SignalR|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по SignalR/Глава 1. Основы SignalR/Клиент на .NET|Вперёд]]

**Дата написания:** 05.09.2026

## Клиент javascript

Последнее обновление: 02.08.2022




-

-

-














### Установка


Клиент javascript является одним из распространенных типов клиентов в SignalR, который может взаимодействовать
с хабом на сервере. Для создания клиента js на веб-страницу необходимо подключить специальную библиотеку.


#### Получение из CDN


Для подключения SignalR можно использовать сети CDN, которые содержат данную библиотеку. В частности, подключить SignalR на страницу
можно по одному из следующих адресов:

```

https://cdnjs.cloudflare.com/ajax/libs/microsoft-signalr/6.0.1/signalr.js
https://unpkg.com/@microsoft/signalr@6.0.1/dist/browser/signalr.min.js
https://cdn.jsdelivr.net/npm/@microsoft/signalr/dist/browser/signalr.min.js

```


### Варианты добавления библиотеки в проект


Выше рассматривалась работа с библиотекой SignalR, когда она подключается через CDN:

```
<script src="https://cdnjs.cloudflare.com/ajax/libs/microsoft-signalr/6.0.1/signalr.js"></script>
```


Либо при необходимости мы можем сохранить данный файл локально в проект и подключать уже из проекта. Это самый простой вариант, однако есть также и другие способы добавления SignalR
в проект.


#### Добавление через NPM


В качестве альтернативы, особенно, если мы работаем не в Visual Studio, можно было бы загрузить пакет "@microsoft/signalr" через пакетный менеджер NPM с помощью команды:

```
npm install @microsoft/signalr
```



либо добавить библиотеку через файл package.json:

```

{
 "version": "1.0.0",
 "name": "asp.net",
 "private": true,
 "devDependencies": {
 "@microsoft/signalr": "6.0.0"
 }
}

```


#### Добавление через менеджер libman


Другая альтернатива состоит в добавлении библиотеки SignalR в проект через пакетный менеджер libman. Для хранения всех необходимых javascript
вначале создадим в папке wwwroot новый подкаталог js.
Далее нажмем на эту папку правой кнопкой мыши и в контекстном меню выберем Add -> Client Side Library
![Установка signalr в проект на ASP.NET Core и C#](https://metanit.com./pics/1.3.png)


Далее нам откроется окно добавления клиентских библиотек. Укажем в нем следующие опции:
![Установка и настройка signalr core в проекте на ASP.NET Core и C#](https://metanit.com./pics/1.4.png)


В поле Provider укажем значение unpkg.


В поле Library в качестве названия пакета введем @microsoft/signalr@latest.


Поскольку пакет содержит много файлов, которые нам могут не понадобиться, то отметим пункт Choose specific files:
и затем из списка файлов отметим только signalr.min.js, то есть минимизированную версию библиотеки. Но при желании и
необходимости можно выбрать и другие файлы.


И в конце в поле Target location укажем расположение, по которому будет сохранена библиотека, то есть путь wwwroot/js/signalr.


В итоге в проекте по пути wwwroot/js/signalr/dist/browser/ мы сможем найти файл signalr.min.js
![Первый проект signalr в Asp.Net Core и C#](https://metanit.com./pics/1.5.png)


И затем мы сможем подключить библиотеку на веб-страницу:

```
<script src="js/signalr/dist/browser/signalr.min.js"></script>
```


### Определение клиента на javascript


Допустим, на стороне сервера определен следующий хаб ChatHub:

```

using Microsoft.AspNetCore.SignalR;

namespace SignalRApp
{
 public class ChatHub : Hub
 {
 public async Task Send(string message, string userName)
 {
 await Clients.All.SendAsync("Receive", message, userName);
 }
 }
}

```


В файле Program.cs для хаба определена следующая конфигурация:

```

using SignalRApp; // пространство имен класса ChatHub

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddSignalR(); // подключаем сервисы SignalR

var app = builder.Build();

app.UseDefaultFiles();
app.UseStaticFiles();

app.MapHub<ChatHub>("/chat"); // ChatHub будет обрабатывать запросы по пути /chat

app.Run();

```


И определим в проекте в папке wwwroot страницу index.html:
![Клиентское приложение SignalR на JavaScript в ASP.NET Core и C#](https://metanit.com./pics/1.10.png)


И определим в ней следующий код

```

<!DOCTYPE html>
<html>
<head>
 <meta charset="utf-8" />
 <title>Metanit.com</title>
</head>
<body>
 <div>
 Введите логин:<br />
 <input id="userName" type="text" /><br/><br/>
 Введите сообщение:<br />
 <input type="text" id="message" /><br/><br/>
 <input type="button" id="sendBtn" value="Отправить" disabled="disabled" />
 </div>
 <div id="chatroom"></div>
 <script src="https://cdnjs.cloudflare.com/ajax/libs/microsoft-signalr/6.0.1/signalr.js"></script>
 <script>
 const hubConnection = new signalR.HubConnectionBuilder()
 .withUrl("/chat")
 .build();

 document.getElementById("sendBtn").addEventListener("click", function () {
 const userName = document.getElementById("userName").value; // получаем введенное имя
 const message = document.getElementById("message").value;

 hubConnection.invoke("Send", message, userName) // отправка данных серверу
 .catch(function (err) {
 return console.error(err.toString());
 });
 });
 // получение данных с сервера
 hubConnection.on("Receive", function (message, userName) {

 // создаем элемент <b> для имени пользователя
 const userNameElem = document.createElement("b");
 userNameElem.textContent = `${userName}: `;

 // создает элемент <p> для сообщения пользователя
 const elem = document.createElement("p");
 elem.appendChild(userNameElem);
 elem.appendChild(document.createTextNode(message));

 // добавляем новый элемент в самое начало
 // для этого сначала получаем первый элемент
 const firstElem = document.getElementById("chatroom").firstChild;
 document.getElementById("chatroom").insertBefore(elem, firstElem);
 });

 hubConnection.start()
 .then(function () {
 document.getElementById("sendBtn").disabled = false;
 })
 .catch(function (err) {
 return console.error(err.toString());
 });
 </script>
</body>
</html>

```

![Клиентское приложение на JavaScript для приложения SignalR на ASP.NET Core и C#](https://metanit.com./pics/1.9.png)


Теперь рассмотрим подробнее основные моменты работы клиента javascript.


### Подключение к хабу


Чтобы подключиться к хабу, применяется объект signalR.HubConnectionBuilder:

```

const hubConnection = new signalR.HubConnectionBuilder()
 .withUrl("/chat")
 .build();

```


Через его метод withUrl передается адрес, по которому доступен хаб. А метод build()
собственно создает объек подключения - объект HubConnection, через который мы можем взаимодействовать с хабом.


После получения объекта HubConnection для подключения к хабу надо вызвать метод start():

```

 hubConnection.start()
 .then(function () {
 document.getElementById("sendBtn").disabled = false;
 })
 .catch(function (err) {
 return console.error(err.toString());
 });

```


Для обработки подключения или ошибки мы можем в методу start добавить вызовы методов then и catch. В метод then передается функция, которая вызывается при успешном подключении.
А в метод catch передается функция, вызываемая при возникновении ошибки. Параметр этой функции как раз содержит информацию об оишбке.


### Отправка данных хабу


Для отправки данных хабу у объекта HubConnection применяется метод invoke(). Например, выше в классе хаба ChatHub
был определен метод Send, который принимает два параметра. Обратимся к этому методу из кода javascript:

```

hubConnection.invoke("Send", "Hello SignalR", "Tom")
 .catch(function (err) {
 return console.error(err.toString());
 });

```


Первый параметр метода представляет имя метода хаба, к которому идет обращения. Например, в данном случае это
метод Send. Все последующие параметры передают данные для параметров метода хаба. Так, метод Send в хабе ChatHub принимает два строковых параметра.
Соответственно в методе invoke мы можем передать для них данные.


Параметры передаются по позиции: второй аргумент метода invoke передает значение для первого параметра метода Send, третий аргумент в invoke - для второго параметра в Send и так далее.


Сам метод invoke представляет объект Promise языка javascript. Соответственно для обработки ошибок, которые могут произойти в процессе отправки, к методу invoke мы можем добавить вызов метода catch. В метод catch в нее передается функция, которая вызывается при возникновении
ошибки. Параметр этой функции (в примере выше параметр err) содержит информацию об ошибке.


### Вызов метода клиента из хаба


Клиент может обращаться к методу хаба, но и хаб может вызывать метод на клиенте. Для этого объект HubConnection с помощью метода
on должен зарегистрировать функцию, которую сможет вызывать хаб. Например, выше в методе Send в хабе
полученные данные транслировались на функцию Receive всем подключенным клиентам:

```
await Clients.All.SendAsync("Receive", message, userName);
```


Первый аргумент функции SendAsync как раз представляет название функции в коде клиента, которая будет вызываться. Последующие
аргументы передают данные, которые получит функция на клиенте.


В этом случае на клиенте мы могли бы определить функцию Receive и получить данные от хаба:

```

hubConnection.on("Receive", function (message, userName) {

 // обработка данных
});

```


Первый параметр функции on - это название вызываемой хабом функции - в данном случае Receive. Второй параметр - функция,
которая получает переданные хабом данные.


### Логгирование


У объекта `signalR.HubConnectionBuilder` есть метод configureLogging(), в который передается
уровень логгирования:

```

const connection = new signalR.HubConnectionBuilder()
 .withUrl("/chat")
 .configureLogging(signalR.LogLevel.Information)
 .build();

```


Все возможные уровни логгирования:


-

`signalR.LogLevel.None`: логгирование отключено

-

`signalR.LogLevel.Critical`: логгирование сообщений об ошибках, которые относятся ко всему приложению в целом

-

`signalR.LogLevel.Error`: логгирование сообшений об ошибках, которые относятся к текущей операции

-

`signalR.LogLevel.Warning`: логгирование сообщений, которые не представляют ошибки

-

`signalR.LogLevel.Information`: логгирование информационных сообщений

-

`signalR.LogLevel.Debug`: логгирование диагностических сообщений, используемых при отладке

-

`signalR.LogLevel.Trace`: логгирование диагностических сообщений с детальной информацией


### Конфигурация клиента


#### Настройка типа транспорта


Для настройки транспорта в методе withUrl() у дополнительного параметра устанавливается свойство
`transport`, которому передаются значения объекта HttpTransportType: WebSockets, LongPolling или ServerSentEvents.
По умолчанию используются все эти виды транспорта, но можно указать только один из них:

```

const hubConnection = new signalR.HubConnectionBuilder()
 .withUrl("/chat", { transport: signalR.HttpTransportType.WebSockets })
 .configureLogging(signalR.LogLevel.Information)
 .build();

```


Установка нескольких типов транспорта:

```

const hubConnection = new signalR.HubConnectionBuilder()
 .withUrl("/chat", { transport: signalR.HttpTransportType.WebSockets | signalR.HttpTransportType.LongPolling })
 .configureLogging(signalR.LogLevel.Information)
 .build();

```


Единственное, что надо учитывать, что сервер тоже должен поддерживать устанавливаемые виды транспорта.


#### Установка времени таймаута


Для установки таймаута для объекта HubConnection определено два свойства:


-

serverTimeoutInMilliseconds представляет таймаут, в течение которого подключение считается активным.
Если в течение этого периода сервер не присылает никакого сообщения, то клиент считает, что подключение к серверу разорвано. И в этом случае вызывается
метод onclose(). Рекомендуется устанавливать это значение в два раза большим, чем параметр KeepAliveInterval на стороне сервера.
По умолчанию равно 30 секунд (30000 миллисекунд).

-

keepAliveIntervalInMilliseconds определяет интервал, в течение которого клиент посылает пинг-сообщения серверу.
Отправка любого сообщения от клиента сбрасывает таймер для отслеживания этого интервала до нуля. Если клиент не отправит никакого сообщения в
течении интервала, который устанавливается свойством ClientTimeoutInterval класса хаба на сервере, то сервер считает, что клиент отключился. Значение по умолчанию - 15 секунд


Например, установим таймаут в виде 10 минут:

```

var connection = new signalR.HubConnectionBuilder()
 .withUrl("/chat")
 .configureLogging(signalR.LogLevel.Trace)
 .build();

connection.serverTimeoutInMilliseconds = 1000 * 60 * 10;

```












- Глава 1. Основы SignalR


 - [Первое приложение](//metanit.com/sharp/signalr/1.1.php)

 - [Создание и конфигурация хабов](//metanit.com/sharp/signalr/1.2.php)

 - [Клиент на javascript](//metanit.com/sharp/signalr/1.3.php)

 - [Клиент на .NET](//metanit.com/sharp/signalr/1.12.php)

 - [Контекст хаба, подключение и отключение клиентов](//metanit.com/sharp/signalr/1.4.php)

 - [Взаимодействие с клиентами](//metanit.com/sharp/signalr/1.5.php)

 - [Отправка сложных объектов](//metanit.com/sharp/signalr/1.6.php)

 - [IHubContext и отправка сообщений вне хаба](//metanit.com/sharp/signalr/1.7.php)

 - [Аутентификация и авторизация на основе куки](//metanit.com/sharp/signalr/1.8.php)

 - [Аутентификация и авторизация с помощью токенов](//metanit.com/sharp/signalr/1.9.php)

 - [Пользователи](//metanit.com/sharp/signalr/1.10.php)

 - [Группы](//metanit.com/sharp/signalr/1.11.php)

 - [Фильтры хабов](//metanit.com/sharp/signalr/1.14.php)

 - [Клиент на .NET MAUI](//metanit.com/sharp/signalr/1.13.php)











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

**Источник:** [https://metanit.com/sharp/signalr/1.3.php](https://metanit.com/sharp/signalr/1.3.php)
