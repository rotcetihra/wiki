# Клиент на Xamarin Forms

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET 5 Core|Руководство по ASP.NET 5 Core]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET 5 Core/Глава 29. SignalR Core|Глава 29. SignalR Core]] / Клиент на Xamarin Forms

[[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET 5 Core/Глава 29. SignalR Core/Группы|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET 5 Core/Глава 29. SignalR Core|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET 5 Core/Глава 30. CORS и кросс-доменные запросы/Начало работы с CORS|Вперёд]]

**Дата написания:** 05.09.2026

## Клиент на Xamarin Forms


Данное руководство устарело. Актуальное руководство: [Руководство по ASP.NET Core 7](https://metanit.com/sharp/aspnet6/)Последнее обновление: 08.12.2018




-

-

-














Xamarin Forms позволяет создавать клиентские приложения, которые могут взаимодействовать с хабом SignalR на стороне сервера.
Рассмотрим, как это сделать.


### Создание сервера


Сначала определим код сервера, с которым будет взаимодействовать клиент на Xamarin. Для этого создадим проект ASP.NET Core по типу
Empty.


Определим в проекте следующий простейший класс хаба:

```

using Microsoft.AspNetCore.SignalR;
using System.Threading.Tasks;

namespace SignalRService
{
 public class ChatHub : Hub
 {
 public async Task Send(string username, string message)
 {
 await this.Clients.All.SendAsync("Receive", username, message);
 }
 }
}

```


В методе Send хаб будет принимать имя пользователя и его сообщение и транслировать его на функцию Receive всех подключенных клиентов.


В классе Startup определим следующий код:

```

using Microsoft.AspNetCore.Builder;
using Microsoft.Extensions.DependencyInjection;

namespace SignalRService
{
 public class Startup
 {
 public void ConfigureServices(IServiceCollection services)
 {
 services.AddSignalR();
 }

 public void Configure(IApplicationBuilder app)
 {
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


И также для теста определим в папке wwwroot простейшую веб-страницу index.html:

```

<!DOCTYPE html>
<html>
<head>
 <meta charset="utf-8" />
 <title>SignalR Chat</title>
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

 <script src="js/signalr.min.js"></script>
 <script>
 let hubUrl = "http://localhost:62432/chat";
 const hubConnection = new signalR.HubConnectionBuilder()
 .withUrl(hubUrl)
 .configureLogging(signalR.LogLevel.Information)
 .build();
 let userName = "";
 // получение сообщения от сервера
 hubConnection.on("Receive", function (userName, message) {

 // создаем элемент <b> для имени пользователя
 let userNameElem = document.createElement("b");
 userNameElem.appendChild(document.createTextNode(userName + ": "));

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
 document.getElementById("header").innerHTML = "<h3>Welcome " + userName + "</h3>";
 });
 // отправка сообщения на сервер
 document.getElementById("sendBtn").addEventListener("click", function (e) {
 let message = document.getElementById("message").value;
 hubConnection.invoke("Send", userName, message);
 });

 hubConnection.start();
 </script>
</body>
</html>

```


Общий проект сервера:
![SignalR Hub для работы с Xamarin Forms](https://metanit.com./pics/signalr19.png)


### Создание клиента Xamarin Forms


Теперь создадим клиентское приложение на Xamarin. Для этого опеделим новый проект Xamarin Forms. И прежде всего добавим
во все проекты решения через пакетный менеджер Nuget пакет Microsoft.AspNetCore.SignalR.Client.
![Microsoft.AspNetCore.SignalR.Client в Xamarin Forms](https://metanit.com./pics/signalr20.png)


В главном проекте определим класс MessageData, который будет представляет полученные с сервера данные:

```

public class MessageData
{
 public string Message { get; set; }
 public string User { get; set; }
}

```


То есть объект MessageData будет содержать данные о сообщении и отправившем его пользователе.


Также добавим в главный проект класс ChatViewModel, который будет выполнять роль модели представления и
через который будет идти взаимодействие с сервером:

```

using Microsoft.AspNetCore.SignalR.Client;
using System;
using System.Collections.ObjectModel;
using System.ComponentModel;
using System.Threading.Tasks;
using Xamarin.Forms;

namespace XamSignalRClient
{
 public class ChatViewModel : INotifyPropertyChanged
 {
 HubConnection hubConnection;

 public string UserName { get; set; }
 public string Message { get; set; }
 // список всех полученных сообщений
 public ObservableCollection<MessageData> Messages { get; }

 // идет ли отправка сообщений
 bool isBusy;
 public bool IsBusy
 {
 get => isBusy;
 set
 {
 if (isBusy != value)
 {
 isBusy = value;
 OnPropertyChanged("IsBusy");
 }
 }
 }
 // осуществлено ли подключение
 bool isConnected;
 public bool IsConnected
 {
 get => isConnected;
 set
 {
 if (isConnected != value)
 {
 isConnected = value;
 OnPropertyChanged("IsConnected");
 }
 }
 }
 // команда отправки сообщений
 public Command SendMessageCommand { get; }

 public ChatViewModel()
 {
 // создание подключения
 hubConnection = new HubConnectionBuilder()
 .WithUrl("http://192.168.0.103:3000/chat")
 .Build();

 Messages = new ObservableCollection<MessageData>();

 IsConnected = false; // по умолчанию не подключены
 IsBusy = false; // отправка сообщения не идет

 SendMessageCommand = new Command(async () => await SendMessage(), () => IsConnected);

 hubConnection.Closed += async (error) =>
 {
 SendLocalMessage(String.Empty, "Подключение закрыто...");
 IsConnected = false;
 await Task.Delay(5000);
 await Connect();
 };

 hubConnection.On<string, string>("Receive", (user, message) =>
 {
 SendLocalMessage(user, message);
 });
 }
 // подключение к чату
 public async Task Connect()
 {
 if (IsConnected)
 return;
 try
 {
 await hubConnection.StartAsync();
 SendLocalMessage(String.Empty, "Вы вошли в чат...");

 IsConnected = true;
 }
 catch (Exception ex)
 {
 SendLocalMessage(String.Empty, $"Ошибка подключения: {ex.Message}");
 }
 }

 // Отключение от чата
 public async Task Disconnect()
 {
 if (!IsConnected)
 return;

 await hubConnection.StopAsync();
 IsConnected = false;
 SendLocalMessage(String.Empty, "Вы покинули чат...");
 }

 // Отправка сообщения
 async Task SendMessage()
 {
 try
 {
 IsBusy = true;
 await hubConnection.InvokeAsync("Send", UserName, Message);
 }
 catch (Exception ex)
 {
 SendLocalMessage(String.Empty, $"Ошибка отправки: {ex.Message}");
 }
 finally
 {
 IsBusy = false;
 }
 }
 // Добавление сообщения
 private void SendLocalMessage(string user, string message)
 {
 Messages.Insert(0, new MessageData
 {
 Message = message,
 User = user
 });
 }
 public event PropertyChangedEventHandler PropertyChanged;
 public void OnPropertyChanged(string prop = "")
 {
 if (PropertyChanged != null)
 PropertyChanged(this, new PropertyChangedEventArgs(prop));
 }
 }
}

```


Раберем код этого класса. Для взаимодействия с хабом нам потребует класс HubConnection, который предоставляет нам функционал для
подключения к хабу и отправки сообщений.


Свойства UserName и Message представляют соответственно имя пользователя и текст сообщения, которые будут отправляться на сервер.
Свойство Messages представляет объект ObservableCollection<MessageData> - полученные с сервера сообщения.


Чтобы извещать пользователя о процессе отправки, определено свойство IsBusy - если оно равно `true`, то приложение находится в процессе оправки сообщения.


Свойство `IsConnected` указывает, подключено ли приложение к хабу.


Непосредственно для отправки сообщений определена команда `SendMessageCommand`.


В конструкторе ChatViewModel с помощью класса `HubConnectionBuilder` создается объект HubConnection. Для его инициализации
через метод `WithUrl()` передается адрес хаба:

```

hubConnection = new HubConnectionBuilder()
 .WithUrl("http://192.168.0.103:3000/chat")
 .Build();

```


В каждом конктретном случае адрес будет отличаться.


Затем определяется команда отправки сообщений:

```

SendMessageCommand = new Command(async () => await SendMessage(), () => IsConnected);

```


При выполнении команды будет вызываться метод SendMessage. Кроме того, команда будет доступна, если свойство IsConnected равно true, то есть
если мы подключены к хабу.


Получив объект HubConnection, мы можем выполнить его настройку. Так, далее устанавливается обрабатчик события завершения подключения:

```

hubConnection.Closed += async (error) =>
{
 SendLocalMessage(String.Empty, "Подключение закрыто...");
 IsConnected = false;
 await Task.Delay(5000);
 await Connect();
};

```


При закрытии подключения, которое может происходить по самым разным причинам, коллекцию Messages добавляется диагностическое сообщение
для пользователя (поэтому вместо имени пользователя используется пустая строка String.Empty) и затем через 5 секунд мы повторно пытаемся подключиться к хабу.


Кроме того, нам надо настроить прием сообщений. Для этого применяется метод `On`:

```

hubConnection.On<string, string>("Receive", (user, message) =>
{
 SendLocalMessage(user, message);
});

```


В классе хаба мы транслируем всем подключенным клиентам на функцию Receive две строки: `this.Clients.All.SendAsync("Receive", username, message);`.
Поэтому в данном случае метод `On()` типизирован двумя объектами string - для получения имени пользователя и его сообщения.
Первый парамет метода указавает название функции - Receive, а второй параметр представляет лямбда-выражение, в котором мы получаем от сервера данные.


В методе `Connect()` осуществляется подключение к хабу. Для этого применяется вызов `hubConnection.StartAsync()`.
После его успешного выполнения мы можем взаимодействовать с сервером.


В методе `Disconnect()` происходит отключение от сервера. Для этого применяется вызов `hubConnection.StopAsync()`


Метод `SendMessage()` предназначен для отправки сообщений хабу. Это осуществляется посредством вызова
`hubConnection.InvokeAsync("Send", UserName, Message);` - на хабе вызывается метод Send, которому передаются значения UserName и Message.


Теперь используем этот класс. Для этого определим к следующий интерфейс на странице MainPage.xaml:

```

<?xml version="1.0" encoding="utf-8" ?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
 xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
 xmlns:local="clr-namespace:XamSignalRClient"
 x:Class="XamSignalRClient.MainPage">
 <StackLayout>
 <ActivityIndicator IsRunning="{Binding IsBusy}" IsVisible="{Binding IsBusy}"
 HorizontalOptions="CenterAndExpand" VerticalOptions="CenterAndExpand"/>
 <StackLayout Padding="10">
 <Label FontSize="Small" Text="Логин" VerticalOptions="Center"/>
 <Entry x:Name="userNameBox" Text="{Binding UserName}" HorizontalOptions="FillAndExpand"/>
 <Label FontSize="Small" Text="Сообщение" VerticalOptions="Center"/>
 <Entry HorizontalOptions="FillAndExpand" Text="{Binding Message}"/>
 <Button Text="Отправить" IsEnabled="{Binding IsConnected}" Command="{Binding SendMessageCommand}"/>
 </StackLayout>
 <ListView ItemsSource="{Binding Messages}">
 <ListView.ItemTemplate>
 <DataTemplate>
 <ViewCell>
 <ViewCell.View>
 <StackLayout Orientation="Horizontal">
 <Label Text="{Binding User}" FontAttributes="Bold" />
 <Label Text="{Binding Message}" />
 </StackLayout>
 </ViewCell.View>
 </ViewCell>
 </DataTemplate>
 </ListView.ItemTemplate>
 </ListView>
 </StackLayout>
</ContentPage>

```


Элемент ActivityIndicator извещает пользователя об процессе отправки сообщений. Для ввода данных определены два текстовых поля.
И по нажатию на кнопку вызывается команда SendMessageCommand, которая оправляет введенные данные.


Для отображения сообщений определен элемент ListView.


В файле MainPage.xaml.cs определим привязку ChatViewModel к странице:

```

using Xamarin.Forms;

namespace XamSignalRClient
{
 public partial class MainPage : ContentPage
 {
 ChatViewModel viewModel;
 public MainPage()
 {
 InitializeComponent();
 viewModel = new ChatViewModel();
 this.BindingContext = viewModel;
 }

 protected override async void OnAppearing()
 {
 base.OnAppearing();
 await viewModel.Connect();
 }

 protected override async void OnDisappearing()
 {
 base.OnDisappearing();
 await viewModel.Disconnect();
 }
 }
}

```


В методе OnAppearing, то есть когда начинается отображение страницы, осуществляется подключение к хабу. В методе OnDisappearing, когда
пользователь покидает страницу или приложение переходит в фоновый режим, то выполняется отключение от хаба.


Итоговый проект для Xamarin:
![Проект Xamarin для работы с SignalR](https://metanit.com./pics/signalr21.png)


Запустим сначала приложение ASP.NET Core, а затем приложение на Xamarin. Чтобы сделать приложение ASP.NET Core доступным для всех устройств,
подключенных к одной и той же локальной сети, можно использовать описанный [здесь](https://metanit.com/sharp/mvc5/24.3.php) второй способ.
![Xamarin Forms и ASP.NET Core SignalR](https://metanit.com./pics/signalr22.png)










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

**Источник:** [https://metanit.com/sharp/aspnet5/30.12.php](https://metanit.com/sharp/aspnet5/30.12.php)
