# UdpClient

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Руководства|Руководства]] / [[Языки программирования/C#/Руководства/Сетевое программирование|Сетевое программирование]] / [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 4. Протокол UDP|Протокол UDP]] / UdpClient

[[Языки программирования/C#/Руководства/Сетевое программирование/Глава 4. Протокол UDP/Использование сокетов для работы с UDP|Назад]] | [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 4. Протокол UDP|Протокол UDP]] | [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 4. Протокол UDP/Консольный UDP-чат|Вперёд]]

**Дата написания:** 05.09.2026

## UdpClient

Для упрощения работы с протоколом UDP в .NET можно использовать класс  UdpClient , который построен на основе класса Socket. 
(Исходный код класса  [UdpClient](https://github.com/dotnet/runtime/blob/main/src/libraries/System.Net.Sockets/src/System/Net/Sockets/UDPClient.cs) )

Для создания UdpClient применяется ряд конструкторов:

```csharp
public UdpClient ();
public UdpClient (AddressFamily family);
public UdpClient (int port);
public UdpClient (IPEndPoint localEP);
public UdpClient (int port, AddressFamily family);
public UdpClient (string hostname, int port);
```

Первый и второй конструкторы создают UdpClient и вместе с этим создают сокет, который будет использовать для получения/отправки данных по сети. 
Третий, четвертый и пятый конструкторы позволяют также установить порт или конечную точку для прослушивания входящих сообщений.   
Последний конструктор позволяет адрес хоста и его порт, на который будут посылаться данные. Сам используемый сокет можно получить с помощью свойства  `Client` :

#### Получение данных

Для получения данных у UdpClient применяются методы  Receive()/ReceiveAsync() :

```csharp
public byte[] Receive (ref System.Net.IPEndPoint? remoteEP);
public Task>System.Net.Sockets.UdpReceiveResult> ReceiveAsync ();
```

Синхронная версия в качестве ref-параметра принимает объект IPEndPoint, в который помещается адрес клиента, приславшего данные. Результатом метода служит 
массив полученных байтов.

Асинхронная версия возвращает объект  UdpReceiveResult , у которого с помощью свойства  `Buffer`  можно получить тот массив присланных байтов, а 
с помощью свойства  `RemoteEndPoint`  адрес отправителя в виде объекта IPEndPoint.

Например, определим мини UDP-сервер, который получает данные:

```csharp
using System.Net.Sockets;
using System.Text;

using var udpServer = new UdpClient(5555);
Console.WriteLine("UDP-сервер запущен...");

// получаем данные
var result = await udpServer.ReceiveAsync();
// предположим, что отправлена строка, преобразуем байты в строку
var message = Encoding.UTF8.GetString(result.Buffer);

Console.WriteLine($"Получено {result.Buffer.Length} байт");
Console.WriteLine($"Удаленный адрес: {result.RemoteEndPoint}");
Console.WriteLine(message);
```

В данном случае UdpClient будет прослушивать порт 5555.

#### Отправка данных

Для отправки данных у UdpClient применяются методы  Send()/SendAsync() . Эти методы имеет несколько перегрузок, рассмотрим некоторые:

```csharp
public int Send (ReadOnlySpan<byte> datagram, IPEndPoint? endPoint);
public ValueTask<int> SendAsync (ReadOnlyMemory<byte> datagram, System.Net.IPEndPoint? endPoint, CancellationToken cancellationToken = default);
```

В качестве параметра обе версии принимают набор отправляемых байтов в виде объекта  `ReadOnlySpan<byte>`  и адрес отправки в виде объекта 
 `IPEndPoint` . Результатом методов является количество отправленных байтов.

Метод  `Send()`  имеет ряд перегруженных версий, благодаря чему мы можем указать адрес хоста и порт прямо при отправке:

Например, определим для вышеопределенного udp-сервера программу udp-клиента, которая будет отправлять данные:

```csharp
using System.Net;
using System.Net.Sockets;
using System.Text;

using var udpClient = new UdpClient();

// отправляемые данные
string message = "Hello METANIT.COM";
// преобразуем в массив байтов
byte[] data = Encoding.UTF8.GetBytes(message);
// определяем конечную точку для отправки данных
IPEndPoint remotePoint = new IPEndPoint(IPAddress.Parse("127.0.0.1"), 5555);
// отправляем данные
int bytes = await udpClient.SendAsync(data, remotePoint);
Console.WriteLine($"Отправлено {bytes} байт");
```

В данном случае строка "Hello METANIT.COM" конвертируется в массив байтов и отправляется по адресу 127.0.0.1:5555.

Запустим UDP-сервер, а затем udp-клиента. В итоге udp-клиент отправит данные на сервер строку, и консоль udp-сервера отобразит полученные данные:

```csharp
UDP-сервер запущен...
Получено 17 байт
Удаленный адрес: 127.0.0.1:52679
Hello METANIT.COM
```

#### Метод Connect

Для установки адреса для отправки данных у UdpClient можно вызвать метод  `Connect()` . 
При этом если мы указали информацию о подключении (название хоста, номер порта) в конструкторе или в методе Connect, то метод Receive будет 
получать данные только с указанной удаленной точки, остальные подключения будут игнорироваться. Также в этом случае необязательно указывать адрес получателя данных в методе  `Send()/SendAsync()` :

```csharp
using System.Net.Sockets;
using System.Text;

using var udpClient = new UdpClient();
udpClient.Connect("127.0.0.1", 5555); // отправляем данные только на 127.0.0.1:5555
// отправляемые данные
string message = "Hello METANIT.COM";
// преобразуем в массив байтов
byte[] data = Encoding.UTF8.GetBytes(message);

// отправляем данные
int bytes = await udpClient.SendAsync(data);
Console.WriteLine($"Отправлено {bytes} байт");
```

В метод Connect передается адрес и порт для подключения, то есть настройки внешнего адреса, к которому мы хотим подключиться. В случае с локальным адресом можно указывать один порт. 
При этом Connect не устанавливает постоянного соединения с удаленным хостом. Он только устанавливает параметры подключения, которые также можно задать с помощью конструктора:

```csharp
using var udpClient = new UdpClient("127.0.0.1", 5555);
```

**Источник:** [https://metanit.com/sharp/net/5.1.php](https://metanit.com/sharp/net/5.1.php)

[[Языки программирования/C#/Руководства/Сетевое программирование/Глава 4. Протокол UDP/Использование сокетов для работы с UDP|Назад]] | [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 4. Протокол UDP|Протокол UDP]] | [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 4. Протокол UDP/Консольный UDP-чат|Вперёд]]
