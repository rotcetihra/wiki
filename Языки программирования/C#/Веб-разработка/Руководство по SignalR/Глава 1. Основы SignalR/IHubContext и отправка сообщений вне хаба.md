# IHubContext и отправка сообщений вне хаба

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по SignalR|Руководство по SignalR]] / [[Языки программирования/C#/Веб-разработка/Руководство по SignalR/Глава 1. Основы SignalR|Глава 1. Основы SignalR]] / IHubContext и отправка сообщений вне хаба

[[Языки программирования/C#/Веб-разработка/Руководство по SignalR/Глава 1. Основы SignalR/Отправка сложных объектов|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по SignalR/Глава 1. Основы SignalR|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по SignalR/Глава 1. Основы SignalR/Аутентификация и авторизация на основе куки|Вперёд]]

**Дата написания:** 05.09.2026

## IHubContext и отправка сообщений вне хаба

Последнее обновление: 04.08.2022




-

-

-














Класс хаба - не единственное место, где мы можем отправлять сообщения клиентам. SignalR позволяет это делать также
в контроллерах, страницах Razor Pages, компонентах middleware, сервисах благодаря внедрению зависимости IHubContext. Объект IHubContext реализует часть функциональности стандартного класса хаба, в частности, в нем определены такие же свойства
Groups и Clients, которые позволяют манипулировать группами и отправлять сообщения всем подключенным клиентам.


Например, определим хаб ChatHub:

```

using Microsoft.AspNetCore.SignalR;

namespace SignalRApp
{
 public class ChatHub : Hub
 {
 }
}

```


Несмотря на то, что класс хаба пустой, он нам понадобится для типизиации объекта IHubContext, кроме того, взаимодействие с клиентами будет идти через данный хаб.


Далее в файле Program.cs определим конечную точку, которая будет принимать данные и, используя функционал хаба SignalR, регтранслировать эти данные
всем подключенным клиентам:

```

using Microsoft.AspNetCore.SignalR; // для IHubContext
using SignalRApp; // пространство имен класса ChatHub

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddSignalR();

var app = builder.Build();

app.UseDefaultFiles();
app.UseStaticFiles();

app.MapPost("create", async (Message message, IHubContext<ChatHub> hubContext) =>
{
 await hubContext.Clients.All.SendAsync("Receive", $"{message.Text} - {DateTime.Now.ToLongTimeString()}");
});

app.MapHub<ChatHub>("/chat");
app.Run();

record class Message(string Text);

```


Итак, здесь по прежнему клиенты подключаются к хабу ChatHub по пути "/chat". Но теперь данные получает конечная точка, которая определена с помощью метода MapPost и которая соответственно обрабатывает
POST-запросы.


В качестве первого параметра обработчик конечной точки принимает собственно отправленные пользователем данные в виде объекта Message, который имеет строковое свойство Text.


В качестве второго параметра в обработчик конечной точки передается объект IHubContext, который мы можем получить благодаря встроенному механизму внедрения зависимостей.
Основное ограничение в данном случае - этот объект должен быть типизирован классом хаба.


Затем мы можем использовать данный IHubContext, например, отправив сообщение подключенным клиентам. К примеру, в данном случае конечная точка получает отправленные данные в post-запросе
по адресу "/create", добавляет к ним текущее время и отправляет их всем подключенным клиентам.


Для тестирования определим в папке wwwroot следующую веб-страницу index.html:

```

<!DOCTYPE html>
<html>
<head>
 <meta charset="utf-8" />
 <title>Metanit.com</title>
</head>
<body>
 <div id="inputForm">
 <input type="text" id="message" />
 <input type="button" id="sendBtn" value="Отправить" disabled="disabled" />
 </div>
 <div id="chatroom"></div>
 <script src="https://cdnjs.cloudflare.com/ajax/libs/microsoft-signalr/6.0.1/signalr.js"></script>
 <script>
 const hubConnection = new signalR.HubConnectionBuilder()
 .withUrl("/chat")
 .build();

 document.getElementById("sendBtn").addEventListener("click",()=> {
 const message = document.getElementById("message").value;

 fetch("create", {
 method: "POST",
 headers: { "Content-Type": "application/json" },
 body: JSON.stringify({
 "text": message
 })
 })
 .catch(error => console.error(error));
 });

 hubConnection.on("Receive", message =>{

 const messageElement = document.createElement("p");
 messageElement.textContent = message;

 // добавляем новый элемент в самое начало
 // для этого сначала получаем первый элемент
 const firstElem = document.getElementById("chatroom").firstChild;
 document.getElementById("chatroom").insertBefore(messageElement, firstElem);
 });

 hubConnection.start()
 .then(() => document.getElementById("sendBtn").disabled = false)
 .catch((err) =>console.error(err) );
 </script>
</body>
</html>

```


На данной веб-странице определено поле для ввода некоторого сообщения, и после нажатия на кнопку это сообщение с помощью функции fetch отправляется на сервер по адресу "/create".
Причем стоит отметить, что также идет подключение идет по адресу "/chat" - то есть фактически к хабу ChatHub. При получении уведомлений от хаба будет вызываться функция receive.


И после отправки формы все остальные подключенные клиенты увидят информацию об отправленных данных.
![HubContext в SignalR в ASP.NET Core и C#](https://metanit.com./pics/1.16.png)


Подобным образом можно получать сервис IHubContext также как и любyю другую зависимость в других сервисах, компонентах middleware, контроллерах MVC и страницах Razor Pages.


Однако стоит отметить, что данный способ отправки сообщений клиентам имее некоторые недостатки. Например, у свойства Clients доступно только свойство All -
то есть мы можем отправить сообщение только всем клиентам и нету таких свойств как Other или Caller, которые доступны при использовании в
классе хаба. Также мы не можем получить из IHubContext id подключения. Поэтому если нам потребуется в контроллерах или других классах получить id подключения, то его можно получить при подключении на клиенте и затем
пересылать тем или иным образом, например, через куки или через параметры запроса.


К примеру, определим следующий код в файле Program.cs:

```

using Microsoft.AspNetCore.SignalR; // для IHubContext
using SignalRApp; // пространство имен класса ChatHub

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddSignalR();

var app = builder.Build();

app.UseDefaultFiles();
app.UseStaticFiles();

app.MapPost("create", async (Message message, IHubContext<ChatHub> hubContext) =>
{
 await hubContext.Clients.AllExcept(message.ConnectionId).SendAsync("Receive", $"{message.ConnectionId}: {message.Text}");
 await hubContext.Clients.Client(message.ConnectionId).SendAsync("Receive", "Ваше сообщение добавлено!");
});

app.MapHub<ChatHub>("/chat");
app.Run();

record class Message(string Text, string ConnectionId);

```


Теперь конечная точка также получает объект Message, но который теперь содержит свойство ConnectionId для хранения id подключение отправителя. И в зависимости от того, кто отправитель,
отправляет то или иное сообщение.


Также изменим веб-страницу index.html:

```

<!DOCTYPE html>
<html>
<head>
 <meta charset="utf-8" />
 <title>Metanit.com</title>
</head>
<body>
 <div id="inputForm">
 <input type="text" id="message" />
 <input type="button" id="sendBtn" value="Отправить" disabled="disabled" />
 </div>
 <div id="chatroom"></div>
 <script src="https://cdnjs.cloudflare.com/ajax/libs/microsoft-signalr/6.0.1/signalr.js"></script>
 <script>
 let connectionId = ""; // id подключения
 const hubConnection = new signalR.HubConnectionBuilder()
 .withUrl("/chat")
 .build();

 document.getElementById("sendBtn").addEventListener("click",()=> {
 const message = document.getElementById("message").value;

 fetch("create", {
 method: "POST",
 headers: { "Content-Type": "application/json" },
 body: JSON.stringify({
 "text": message,
 "connectionid": connectionId
 })
 })
 .catch(error => console.error(error));
 });

 hubConnection.on("Receive", message =>{

 const messageElement = document.createElement("p");
 messageElement.textContent = message;

 const firstElem = document.getElementById("chatroom").firstChild;
 document.getElementById("chatroom").insertBefore(messageElement, firstElem);
 });

 hubConnection.start()
 .then(() => {
 document.getElementById("sendBtn").disabled = false;
 // после соединения получаем id подключения
 console.log(hubConnection.connectionId);
 connectionId = hubConnection.connectionId;
 })
 .catch((err) =>console.error(err) );
 </script>
</body>
</html>

```


Теперь страница отправляет ajax-запросы к методу Create контроллера Home. После подключения к хабу через функцию
`hubConnection.start()` получаем id подключения. И затем при отправке включаем его в тело запроса.
![SignalR и HubContext в приложении на ASP.NET Core и C#](https://metanit.com./pics/1.17.png)










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

**Источник:** [https://metanit.com/sharp/signalr/1.7.php](https://metanit.com/sharp/signalr/1.7.php)
