# NetworkStream

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Руководства|Руководства]] / [[Языки программирования/C#/Руководства/Сетевое программирование|Сетевое программирование]] / [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 3. Протокол TCP|Протокол TCP]] / NetworkStream

[[Языки программирования/C#/Руководства/Сетевое программирование/Глава 3. Протокол TCP/TCP-сервер на сокетах|Назад]] | [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 3. Протокол TCP|Протокол TCP]] | [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 3. Протокол TCP/TCP-клиент. Класс TcpClient|Вперёд]]

**Дата написания:** 05.09.2026

## NetworkStream

Для получения и отправки данных в .NET может использоваться и по умолчанию в ряде классов используется класс потоков  NetworkStream  
из пространства имен  `System.Net.Sockets` . Он наследуется от базового класса Stream. В то же время он отличается от других классов потоков тем, что он не является буферизованным и не поддерживает 
перемещение в произвольную позицию с помощью метода Seek. Также при записи в поток не надо использовать метод Flush для сброса в поток всех данных. (Исходный код класса 
 [NetworkStream](https://github.com/dotnet/runtime/blob/main/src/libraries/System.Net.Sockets/src/System/Net/Sockets/NetworkStream.cs) )

Для создания объекта NetworkStream необходимо в его конструктор передать как минимум один параметр - используемый сокет - объект Socket:

```csharp
public NetworkStream (System.Net.Sockets.Socket socket);
```

При этом сокет должен быть потоковым то есть иметь тип  `SocketType.Stream` . А поскольку такие сокеты на данный момент применяются только 
для протокола TCP, то класс NetworkStream применяется только при получении/отправке данных по протоколу TCP, соответственно мы будем говорить о примении NetworkStream 
только в контексте протокола TCP.

Стоит отметить, что мы можем создать поток NetworkStream лишь после подключения сокета к серверу:

```csharp
using System.Net.Sockets;

using var mySocket = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
var server = "www.google.com";
mySocket.Connect(server, 80);       // подключемся к удаленному серверу

using var stream = new NetworkStream(mySocket); // создаем сетевой поток
// получаем локальный адрес
Console.WriteLine($"Локальный адрес: {stream.Socket.LocalEndPoint}");
// получаем адрес сервера
Console.WriteLine($"Адрес сервера: {stream.Socket.RemoteEndPoint}");
```

Через свойство  Socket  далее можно обращаться к используемому сокету. Так, в примере выше подключаемся к адресу "google.com", создаем NetworkStream и, 
обращаясь к сокету, получаем локальный адрес клиента и адрес сервера.

После завершения работы с NetworkStream его как и любой поток необходимо закрыть. Для этого можно применть метод  Close() :

```csharp
var stream = new NetworkStream(mySocket);
//..........
stream.Close();
```

Также можно использовать конструкцию  using , как в предыдущем примере.

### Методы NetworkStream

С помощью методов NetworkStream можно получить или отправить данные:

- Read()/ReadAsync() : считывает данные из потока в массив байтов и возвращает количество считанных байтов
- ReadByte() : считывает один байт из потока и возвращает его
- ReadAtLeast()/ReadAtLeastAsync() : считывает из потока как минимум определенное количество байтов (или больше) и возвращает количество считанных байтов
- ReadExactly()/ReadExactlyAsync() : считывает из потока точное количество байтов
- Write()/WriteAsync() : отправляет в поток данные в виде массива байтов
- WriteByte() : отправляет в поток один байт

Рассмотрим применение некоторых методов.

### Отправка данных

Для отправки данных у NetworkStream используется метод  `Write()/WriteAsync()` :

```csharp
public ValueTask WriteAsync (ReadOnlyMemory<byte> buffer, CancellationToken cancellationToken = default);
public Task WriteAsync (byte[] buffer, int offset, int count);
```

Отправляемые данные передаются в виде массива байтов, либо в виде объекта ReadOnlyMemory<byte>, который опять же инкапсулирует массив байтов.

```csharp
using System.Net.Sockets;
using System.Text;

using var mySocket = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
var server = "www.google.com";
mySocket.Connect(server, 80);

using var stream = new NetworkStream(mySocket);
// отправляем сообщение для отправки
var message = $"GET / HTTP/1.1\r\nHost: {server}\r\nConnection: Close\r\n\r\n";
// кодируем его в массив байт
var data = Encoding.UTF8.GetBytes(message);
// отправляем массив байт на сервер 
await stream.WriteAsync(data);
Console.WriteLine($"Данные отправлены на сервер {server}");
```

Как правило, взаимодействие клиента и сервера происходит по некоторому протоколу, которому следуют и клиент, и сервер. Сервер, который обрабатывает 
запросы к "www.google.com" представляет собой http-сервер и обрабатывает запросы по протоколу http. Поэтому наш клиент посылает сообщение, которое соответствует 
протоколу http. В данном случае серверу отправляется сообщение

```csharp
var message = $"GET / HTTP/1.1\r\nHost: {server}\r\nConnection: Close\r\n\r\n";
```

Поскольку в реальности мы можем отправить только байты, а не строки, то преобразуем сообщение в массив байт и передаем его в метод WriteAsync:

```csharp
var data = Encoding.UTF8.GetBytes(message);
await stream.WriteAsync(data);
```

Хотя здесь мы используем перегрузку, которая принимает объект ReadOnlyMemory<byte>. Но .NET может автоматически преобразовать массив байт в подобный объект.

### Получение данных

Для получения данных к NetworkStream в общем случае применяются методы  Read()/ReadAsync() , которые имеют ряд перегрузок. Например, перегрузки метода  `ReadAsync` :

```csharp
public ValueTask<int> ReadAsync (Memory<byte> buffer, CancellationToken cancellationToken = default);
public Task<int> ReadAsync (byte[] buffer, int offset, int count);
public Task<int> ReadAsync (byte[] buffer, int offset, int count, CancellationToken cancellationToken);
```

В качестве первого параметра метод получает буфер чтения в виде массива байт или объекта  `Memory<byte>` , в которые считываются данные из потока. 
Дополнительно можно установить смещение в массиве и количество считываемых байтов.

В качестве результата метод неявно возвращает количество реально считанных байтов, которое может быть меньше длины буфера чтения.

Так, в примере выше мы посылали http-запрос к серверу "www.google.com". Теперь получим от него ответ:

```csharp
using System.Net.Sockets;
using System.Text;

using var mySocket = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
var server = "www.google.com";
mySocket.Connect(server, 80);

using var stream = new NetworkStream(mySocket);
// отправляем сообщение для отправки
var message = $"GET / HTTP/1.1\r\nHost: {server}\r\nConnection: Close\r\n\r\n";
// кодируем его в массив байт
var data = Encoding.UTF8.GetBytes(message);
// отправляем массив байт на сервер 
await stream.WriteAsync(data);

// буфер для получения данных
var responseData = new byte[512];
// получаем данные
var bytes = await stream.ReadAsync(responseData);
// преобразуем полученные данные в строку
string response = Encoding.UTF8.GetString(responseData, 0, bytes);
// выводим данные на консоль
Console.WriteLine(response);
```

В качестве буфера отправляемых байтов определена переменная  `responseData` , которая представляет массив байт. По умолчанию буфер имеет 
размер в 512 байт. Но это не принципиально. Главное представлять, насколько большие могут быть полученные данные и в соответствии с этим определять размер для буфера. А чтобы отслеживать 
реальное количество считанных байт (которое может быть меньше размера буфера), определена переменная bytes. Поскольку в данном случае ответ от google.com по сути представляет строку, то 
конвертируем преобразованные данные в строку. В конце выводим строку ответа на консоль.

Как мы видим, это обычный ответ HTTP, где в начале идут статус ответа, заголовки. По сути это те данные, которые получает браузер при обращении по адресу "www.google.com". 
Однако по ответу видно, что он не полный. Идеальна была бы ситуация, когда мы точно знаем, сколько байт пришлет удаленный хост. И соответственно могли бы определить соответствующий буфер. Но в данном случае мы этого 
точно не знаем - они могут быть больше размера буфера, а могут быть меньше. Очевидно, нам надо считывать данные в цикле, пока мы не получим последний байт:using System.Net.Sockets;
using System.Text;

using var mySocket = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
var server = "www.google.com";
mySocket.Connect(server, 80);

using var stream = new NetworkStream(mySocket);
// отправляем сообщение для отправки
var message = $"GET / HTTP/1.1\r\nHost: {server}\r\nConnection: Close\r\n\r\n";
// кодируем его в массив байт
var data = Encoding.UTF8.GetBytes(message);
// отправляем массив байт на сервер 
await stream.WriteAsync(data);

// буфер ддя получения данных
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
while (bytes > 0); // пока данные есть в потоке 

// выводим данные на консоль
Console.WriteLine(response);теперь для считывания используем цикл do..while. Смотрим, сколько байтов возвращает ReadAsync. И пока он вернет 0 байтов, повторяем цикл. 
Полученные байты конвертируем в строку и добавляем в StringBuilder. В конце выводим полученное содержимое из StringBuilder на консоль:ReadAtLeastAsyncМетодыReadAtLeast()/ReadAtLeastAsync()позволяют установить минимальное количество считываемых байтов:public ValueTask<int> ReadAtLeastAsync (Memory<byte> buffer, int minimumBytes, bool throwOnEndOfStream = true, CancellationToken cancellationToken = default);Через первый параметр типаMemory<byte>передается буфер для считывания данных, а второй параметр - minimumBytes указывает на минимальное количество байтов, 
которые надо считать с потока.Например, получим как минимум 16 байтов:// буфер ддя получения данных
var responseData = new byte[512];
// получаем данные
int bytes = await stream.ReadAtLeastAsync(responseData, 16);
// преобразуем в строку
var response = Encoding.UTF8.GetString(responseData, 0, bytes);
// выводим данные на консоль
Console.WriteLine(response);ReadExactlyМетодыReadExactly()/ReadExactlyAsync()позволяют установить точное количество байтов, которые надо получить из потока:public ValueTask ReadExactlyAsync (Memory<byte> buffer, CancellationToken cancellationToken = default);
public ValueTask ReadExactlyAsync (byte[] buffer, int offset, int count, CancellationToken cancellationToken = default);Через первый параметр передается буфер для считывания данных. В первой версии количество байтов, которые надо считать, устанавливается исходя из 
размера буфера. Во второй версии для этого служит параметр count.Например, получим 16 байтов:int bytes = 16; // сколько надо получить данных
// буфер ддя получения данных
var responseData = new byte[bytes];
// получаем данные
await stream.ReadExactlyAsync(responseData);
// преобразуем в строку 
var response = Encoding.UTF8.GetString(responseData);
// выводим данные на консоль
Console.WriteLine(response);

**Источник:** [https://metanit.com/sharp/net/3.6.php](https://metanit.com/sharp/net/3.6.php)

[[Языки программирования/C#/Руководства/Сетевое программирование/Глава 3. Протокол TCP/TCP-сервер на сокетах|Назад]] | [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 3. Протокол TCP|Протокол TCP]] | [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 3. Протокол TCP/TCP-клиент. Класс TcpClient|Вперёд]]
