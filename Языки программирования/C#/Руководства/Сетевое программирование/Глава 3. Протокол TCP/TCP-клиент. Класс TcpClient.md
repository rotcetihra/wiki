# TCP-клиент. Класс TcpClient

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Руководства|Руководства]] / [[Языки программирования/C#/Руководства/Сетевое программирование|Сетевое программирование]] / [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 3. Протокол TCP|Протокол TCP]] / TCP-клиент. Класс TcpClient

[[Языки программирования/C#/Руководства/Сетевое программирование/Глава 3. Протокол TCP/NetworkStream|Назад]] | [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 3. Протокол TCP|Протокол TCP]] | [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 3. Протокол TCP/TCP-сервер. Класс TcpListener|Вперёд]]

**Дата написания:** 05.09.2026

## TCP-клиент. Класс TcpClient

Для создания tcp-клиента платформа .NET предоставляет класс класс  TcpClient , который построен поверх сокетов и опять же использует сокет для 
отправки и получения данных, но при этом упрощает написание некоторых вещей. 
(Исходный код  [TcpClient](https://github.com/dotnet/runtime/blob/main/src/libraries/System.Net.Sockets/src/System/Net/Sockets/TCPClient.cs) )

### Создание TcpClient

Для создания TcpClient применяется один из конструкторов класса:

```csharp
public TcpClient ();
public TcpClient (System.Net.Sockets.AddressFamily family);
public TcpClient (string hostname, int port);
public TcpClient (System.Net.IPEndPoint localEP);
```

При использовании всех конструкторов, кроме последнего объекту TcpClient автоматически присваивается наиболее подходящий локальный IP-адрес и порт. Через последний конструктор можно 
вручную задать локальную конечную точку - объект IPEndPoint, к которой будет привязан TcpClient.

При использовании второго конструктора в него передается либо значение  `AddressFamily.InterNetwork`  (для адресов IPv4), либо 
 `AddressFamily.InterNetworkV6`  (для адресов IPv6).

В третий конструктор передается адрес и порт удаленного узла, к которому клиент собирается подклчаться.

### Свойства TcpClient

Свойства TcpClient позволяют настроить состояние объекта или получить информацию о нем. Отметим среди свойств следующие:

Available: возвращает количество байтов данных, полученных из сети и доступных для чтения.

Client: возвращает или задает объект Socket, который используется объектом TcpClient.

Connected: возвращаетtrue, если TcpClient подключен к удаленному узлу.

>LingerState: возвращает или устанавливает, доступен ли порт только одному клиенту.

NoDelay: указывает, применяется ли задержка, когда буферы отправки и получения не заполнены. 
Если равноfalse, то TcpClient отправляет пакеты по сети только тогда, когда наберется достаточное количество данных. Это сделано, потому что 
отправка небольших кусочков данных может быть неэффективной и может привести к перегрузке. В то же время могут быть ситуации, 
когда необходимо отправлять небольшие объемы данных или когда необходимо побыстрее получить ответ.

ReceiveBufferSize: возвращает или задает размер буфера приема (по умолчанию равно 65536).

ReceiveTimeout: возвращает или задает длительность интервала, в течение которого объект TcpClient будет ожидать получение 
данных после начала операции чтения (по умолчанию равно 0).

SendBufferSize: возвращает или задает размер буфера отправки (по умолчанию равно 65536).

SendTimeout: возвращает или задает длительность интервала, в течение которого объект TcpClient будет ожидать 
успешное завершение отправки данных (по умолчанию равно 0).

### Подключение к серверу

Для подключения к серверу TCP, в этом классе определен метод  `Connect()/ConnectAsync()` , которому передается адрес удаленного хоста. Основные версии:

```csharp
public Task ConnectAsync (System.Net.IPEndPoint remoteEP);
public Task ConnectAsync (string host, int port);
public Task ConnectAsync (System.Net.IPAddress address, int port);
```

Например, покдлючимся к хосту "www.google.com":

```csharp
using System.Net.Sockets;

using TcpClient tcpClient = new TcpClient();
try
{
    // подключение к www.google.com
    await tcpClient.ConnectAsync("www.google.com", 80);
    Console.WriteLine("Подключение установлено");
}
catch(SocketException ex)
{
    Console.WriteLine(ex.Message);
}
```

При неудачной попытке подключения метод Connect/ConnectAsync генерирует исключение типа SocketException.

### Закрытие TcpClient

После окончания работы с TcpClient его надо закрыть методом  Close() :

```csharp
using System.Net.Sockets;

TcpClient tcpClient = new TcpClient();

await tcpClient.ConnectAsync("www.google.com", 80);
Console.WriteLine("Подключение установлено");

tcpClient.Close();      // закрываем подключение
Console.WriteLine(tcpClient.Connected);     // False - подключение закрыто
```

Либо можно использовать конструкцию  using , как в предыдущем примере.

### Отправка и получение данных

Для отправки и получения данных TcpClient в общем случае использует рассмотренный в прошлой теме класс  NetworkStream . 
Для получения объекта NetworkStream  после подключения  к серверу у TcpClient можно вызвать метод  `GetStream()` :

```csharp
using System.Net.Sockets;

using TcpClient tcpClient = new TcpClient();
await tcpClient.ConnectAsync("www.google.com", 80);
// получаем поток для взаимодействия с сервером
NetworkStream stream = tcpClient.GetStream();
```

Соответственно отправка и получение данных для TcpClient будет производиться также, как было рассмотрено в прошлой статье про NetworkStream.

Стоит отметить, что в реальности NetworkStream будет использовать для отправки и получения данных тот же объект Socket, что и TcpClient. 
Кроме того, если закрывается объект TcpClient (в примере выше для этого применяется конструкция using), то вместе с ним автоматически закрывается и связанный с ним объект NetworkStream (а также освобождается связанный с ними сокет).

#### Отправка данных

Для отправки данных у NetworkStream используется метод  `Write()/WriteAsync()` :

```csharp
public ValueTask WriteAsync (ReadOnlyMemory<byte> buffer, CancellationToken cancellationToken = default);
public Task WriteAsync (byte[] buffer, int offset, int count);
```

Отправляемые данные передаются в виде массива байтов, либо в виде объекта ReadOnlyMemory<byte>, который опять же инкапсулирует массив байтов.

```csharp
using System.Net.Sockets;
using System.Text;

using TcpClient tcpClient = new TcpClient();
var server = "www.google.com";
await tcpClient.ConnectAsync(server, 80);
// получаем поток для взаимодействия с сервером
NetworkStream stream = tcpClient.GetStream();

 // определяем отправляемые данные
var requestMessage = $"GET / HTTP/1.1\r\nHost: {server}\r\nConnection: Close\r\n\r\n";
// конвертируем данные в массив байтов
var requestData = Encoding.UTF8.GetBytes(requestMessage);
// отправляем данные серверу
await stream.WriteAsync(requestData);
```

Сервер, который обрабатывает запросы к "www.google.com" представляет собой http-сервер и обрабатывает запросы по протоколу http. Поэтому наш клиент посылает сообщение, которое соответствует 
протоколу http.

### Получение данных

Для получения данных к NetworkStream применяется методы  Read()/ReadAsync() . Так, в примере выше мы посылали http-запрос к серверу "www.google.com". Теперь получим от него ответ:

```csharp
using System.Net.Sockets;
using System.Text;

using TcpClient tcpClient = new TcpClient();
var server = "www.google.com";
await tcpClient.ConnectAsync(server, 80);
var stream = tcpClient.GetStream();

var requestMessage = $"GET / HTTP/1.1\r\nHost: {server}\r\nConnection: Close\r\n\r\n";
var requestData = Encoding.UTF8.GetBytes(requestMessage);
await stream.WriteAsync(requestData);

// буфер для получения данных
var responseData = new byte[512];
// StringBuilder для склеивания полученных данных в одну строку
var response = new StringBuilder();
int bytes;  // количество полученных байтов
do
{
    // получаем данные
    bytes = await stream.ReadAsync(responseData);
    // преобразуем в строку и добавляем ее в StringBuilder
    response.Append(Encoding.UTF8.GetString(responseData, 0, bytes));
}
while (bytes>0); // пока данные есть в потоке 

// выводим данные на консоль
Console.WriteLine(response);
```

теперь для считывания используем цикл do..while. Смотрим, сколько байтов возвращает ReadAsync. И пока он вернет 0 байтов, повторяем цикл. 
Полученные байты конвертируем в строку и добавляем в StringBuilder. В конце выводим полученное содержимое из StringBuilder на консоль:

Считывание данные и свойства TcpClient.Available и NetworkStream.DataAvailableПри чтении данных из потока одна из часто встречающихся задач заключается в определении конца данных, особенно если мы считываем данные в бесконечном цикле. В примере выше 
это делалось просто - считывали, пока количество реально считанных байтов не достигнет нуля, то есть доступных байтов для чтения просто не останется:do
{
    bytes = await stream.ReadAsync(responseData);
    response.Append(Encoding.UTF8.GetString(responseData, 0, bytes));
}
while (bytes>0); // пока данные есть в потокеНо у класса TcpClient есть свойствоAvailable, которое возвращает количество доступных для чтения байтов. Кроме того, у класса 
NetworkStream есть похожее свойство -DataAvailable, которое возвращаетtrue, если в потоке есть доступные для чтения данные. 
Соответственно возникает вопрос, почему бы не использовать эти свойства? Например, свойствоAvailable:do
{
    bytes = await stream.ReadAsync(responseData);
    response.Append(Encoding.UTF8.GetString(responseData, 0, bytes));
}
while (tcpClient.Available > 0); // пока данные есть в потокеИли свойствоDataAvailabledo
{
    bytes = await stream.ReadAsync(responseData);
    response.Append(Encoding.UTF8.GetString(responseData, 0, bytes));
}
while (stream.DataAvailable); // пока данные есть в потокеВ реальности оба этих свойства смотрят на значение свойства Available используемого объекта Socket, которое возвращает количество доступных для чтения байтов. 
И соответственно здесь мы столкнемся с той же проблемой, что и при работе с классом Socket - свойство Available будет иметь ненулевое значение, если втекущий моментесть доступные данные. Но природа протокола TCP такова, что крупные наборы данных отправляются отдельными пакетами. Какой-то пакет 
может прийти быстрее, какой-то задержится, какой-то будет потерян, и потребуется переотправка. Поэтому может возникнуть ситуация, что сервер отправил данные, часть данных пришла. В какой-то момент 
свойство Available у сокета возратило 0, соответственно произошел выход из цикла.

**Источник:** [https://metanit.com/sharp/net/4.1.php](https://metanit.com/sharp/net/4.1.php)

[[Языки программирования/C#/Руководства/Сетевое программирование/Глава 3. Протокол TCP/NetworkStream|Назад]] | [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 3. Протокол TCP|Протокол TCP]] | [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 3. Протокол TCP/TCP-сервер. Класс TcpListener|Вперёд]]
