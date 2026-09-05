# TCP-клиент на сокетах

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Руководства|Руководства]] / [[Языки программирования/C#/Руководства/Сетевое программирование|Сетевое программирование]] / [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 3. Протокол TCP|Протокол TCP]] / TCP-клиент на сокетах

[[Языки программирования/C#/Руководства/Сетевое программирование/Глава 2. Протокол HTTP/HttpListener. HTTP-сервер|Назад]] | [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 3. Протокол TCP|Протокол TCP]] | [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 3. Протокол TCP/TCP-сервер на сокетах|Вперёд]]

**Дата написания:** 05.09.2026

Одним из наиболее распространенных протоколов взаимодействия в сети является протокол TCP (Transmission Control Protocol). Этот протокол гарантирует 
доставку сообщений и широко используется в различных существующих на сегодняшний день программах. Для работы с протоколом TCP в .NET предназначены классы  TcpClient  и  TcpListener . 
Эти классы строятся поверх класса  System.Net.Sockets.Socket . TcpClient и TcpListener упрощают создание клиента и сервера, которые 
реализуют протокол TCP. Если же функциональности этих классов недостаточно, то для более продвинутных и изощренных сценариев можно 
использовать тот же класс Socket. В данной главе мы рассмотрим различные подходы к построению tcp-клиента и tcp-сервера, как с помощью TcpClient и TcpListener, 
так и с помощью чистых сокетов.

## TCP-клиент на сокетах

Рассмотрим определение простейшего клиента, который использует TCP-сокеты для подключения к хосту, отправки и получения данных. Прежде всего для определения 
сокета, который использует протокол TCP, необходимо для сокета указать в качестве типа протокола Tcp, а в качестве типа сокета -  `Stream` :

```csharp
Socket tcpSocket = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
```

### Подключение к хосту

Для подключения к удаленному хосту применяется метод  Connect() / ConnectAsync() . Оба этих метода имеют множество версий, но в общем случае для 
подключения к удаленному хосту нам необходим адрес хоста в виде ip-адреса или домена и порт. Отмечу пару перегрузок:

```csharp
public Task ConnectAsync (string host, int port);
public Task ConnectAsync (IPAddress address, int port);
```

Например, подключемся к хосту "google.com":

```csharp
using System.Net.Sockets;

var port = 80;
var url = "www.google.com";

using var socket = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
try
{
    // пытаемся подключиться используя URL-адрес и порт
    await socket.ConnectAsync(url, port);
    Console.WriteLine($"Подключение к {url} установлено");
}
catch (SocketException)
{
    Console.WriteLine($"Не удалось установить подключение к {url}");
}
```

В данном случае после успешного подключения выводим на консоль соответствующее сообщение.

При неудаче подключения будет сгенерировано исключение  SocketException

### Информация о подключении

После подключения к удаленному хосту мы можем получить его адрес (то есть ip-адрес+порт) с помощью свойства  RemoteEndPoint . Кроме того, мы можем получить адрес 
самого сокета с помощью свойства  LocalEndPoint :

```csharp
using System.Net.Sockets;

var port = 80;
var url = "www.google.com";

using var socket = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
try
{
    // пытаемся подключиться используя URL-адрес и порт
    await socket.ConnectAsync(url, port);
    Console.WriteLine($"Подключение к {url} установлено");
    Console.WriteLine($"Адрес подключения {socket.RemoteEndPoint}");
    Console.WriteLine($"Адрес приложения {socket.LocalEndPoint}");
}
catch (SocketException)
{
    Console.WriteLine($"Не удалось установить подключение к {url}");
}
```

Например, консольный вывод с моем случае:

```csharp
Подключение к www.google.com установлено
Адрес подключения 216.58.210.164:80
Адрес приложения 192.168.0.112:65103
```

### Отключение от хоста

Если мы завершили взаимодействие с хостом, но планируем продолжать использовать сокет, чтобы соединение с удаленным хостом не висело, мы можем отключиться с помощью 
метода  Disconnect() / DisconnectAsync() . Данный метод в качестве параметра принимает значение  `bool`  - если оно равно  `true` , то 
после отключения можно заново использовать сокет для новых подключений:

```csharp
using System.Net.Sockets;

var port = 80;
var url = "www.google.com";

using var socket = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
try
{
    await socket.ConnectAsync(url, port);
    await socket.DisconnectAsync(true); // отключаемся
}
catch (SocketException ex)
{
    Console.WriteLine(ex.Message);
}
```

Чтобы гарантировать, что все данные отправлены и получены перед закрытием подключения, перед вызовом метода Disconnect/DisconnectAsync Microsoft рекомендует вызывать метод Shutdown.

### Отправка данных

Для отправки данных применяется метод  Send()/SendAsync() . Оба этих метода имеют различные версии. Рассмотрим самые простые версии:

```csharp
public Task<int> SendAsync (ArraySegment<byte> buffer);
public Task<int> SendAsync (ArraySegment<byte> buffer, SocketFlags socketFlags);
```

В качестве параметра он получает отправляемые данные в виде структуры  `ArraySegment<byte>`  - грубо говоря часть массива байтов. 
Дополнительно с помощью значений перечисления SocketFlags можно установить параметры отправки.

В качестве результата метод  `SendAsync()`  возвращает количество отправленных данных.

Например, отправим на google.com запрос с некоторыми данными:

```csharp
using System.Net.Sockets;
using System.Text;

var port = 80;
var url = "www.google.com";

using var socket = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
try
{
    await socket.ConnectAsync(url, port);
    // определяем отправляемые данные
    var message = $"GET / HTTP/1.1\r\nHost: {url}\r\nConnection: close\r\n\r\n";
    // конвертируем данные в массив байтов
    var messageBytes = Encoding.UTF8.GetBytes(message);
    int bytesSent = await socket.SendAsync(messageBytes);
    Console.WriteLine($"на адрес {url} отправлено {bytesSent} байт(а)");
}
catch (SocketException ex)
{
    Console.WriteLine(ex.Message);
}
```

При взаимодействии с сервером надо понимать, какой протокол реализует данный сервер, то есть правила, по которым этим сервер получает запросы. 
Так, google.com, как любой стандартный сайт, принимает сообщения, которые соответствуют протоколу 
HTTP. Грубо говоря, чтобы удаленный хост нас понял, нам надо говорить на его языке. И в данном случае мы посылаем сообщение, которое соответствует протоколу HTTP:

```csharp
var message = $"GET / HTTP/1.1\r\nHost: {url}\r\nConnection: close\r\n\r\n";
```

Формат запроса HTTP включает прежде всего линию запроса, которая состоит из типа запроса, пути к запрошенному ресурсу и специфической версии 
протокола. То есть здесь в сообщении мы указываем, что отправляется запрос типа GET по пути "/" (то есть к корню сайта google.com"). При этом применяется протокол HTTP/1.1. 
Линия запроса должна завершаться двойным набором символов каретки и перевода строки  `\r\n` .

Кроме того, запрос HTTP может содержать заголовки. Так, в данном случае отправляем заголовок "Host", который указывает на ажрес хоста. В данном случае это "www.gooogle.com:80". И также 
в данном случае отправляем заголовок "Connection", который имеет значение "close" - это значение предписывает серверу закрыть подключение.

Поскольку мы можем послать только байты, а не строки, то переводим строку в массив байтов:

```csharp
var messageBytes = Encoding.UTF8.GetBytes(message);
```

И отправляем данные:

```csharp
int bytesSent = await socket.SendAsync(messageBytes);
```

Стоит обратить внимание, что хотя метод SendAsync принимает объект ArraySegment, здесь мы передаем непосредственно массив с данными, который автоматически будет 
конвертироваться в структуру  `ArraySegment<byte>` .

В итоге при выполнении запроса получим следющий консольный вывод:

```csharp
на адрес www.google.com отправлено 62 байт(а)
```

### Получение данных от хоста

Для получения данных класс Socket применяет методы  Receive() / ReceiveAsync() . Оба метода имеют много перегруженных версий с разным набором параметров, но 
ключевой параметр - буфер, в который загружаются полученные данные. Для синхронного метода Receive в качестве буфера обычно выступает массив байт, а для асинхронного ReceiveAsync - 
структура  `ArraySegment<byte>` :

```csharp
Task<int> ReceiveAsync (ArraySegment<byte> buffer);
int Receive (byte[] buffer);
```

Результатом обоих методов является количество считанных байтов.

Например, получим от google.com ответ:

```csharp
using System.Net.Sockets;
using System.Text;

var port = 80;
var url = "www.google.com";

using var socket = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
try
{
    await socket.ConnectAsync(url, port);
    // определяем отправляемые данные
    var message = $"GET / HTTP/1.1\r\nHost: {url}\r\nConnection: close\r\n\r\n";
    // конвертируем данные в массив байтов
    var messageBytes = Encoding.UTF8.GetBytes(message);
    // отправляем данные
    await socket.SendAsync(messageBytes);

    // буфер для получения данных
    var responseBytes = new byte[512];
    // получаем данные
    var bytes = await socket.ReceiveAsync(responseBytes);
    // преобразуем полученные данные в строку
    string response = Encoding.UTF8.GetString(responseBytes, 0, bytes);
    // выводим данные на консоль
    Console.WriteLine(response);
}
catch (SocketException ex)
{
    Console.WriteLine(ex.Message);
}
```

В качестве буфера отправляемых байтов определена переменная  `responseBytes` , которая представляет массив в 512 байт. В размер буфера в данном случае 
не принципиально. Главное представлять, насколько большие могут быть полученные данные и в соответствии с этим определять размер для буфера. А чтобы отслеживать 
реальное количество считанных байт (которое может быть меньше размера буфера), определена переменная bytes.

Причем как и в случае с методом SendAsync в метод ReceiveAsync передается массив байт, который автоматически преобразуется в ArraySegment<byte>.

```csharp
var bytes = await socket.ReceiveAsync(responseBytes);
```

Поскольку в данном случае ответ от google.com по сути представляет строку, то конвертируем преобразованные данные в строку и выводим ее на консоль.

```csharp
string response = Encoding.UTF8.GetString(responseBytes, 0, bytes);
Console.WriteLine(response);
```

Как мы видим, это обычный ответ HTTP, где вначале идут статус ответа, заголовки. Однако по ответу видно, что он не полный. Идеальна была бы ситуация, когда мы точно знаем, сколько байт пришлет удаленный хост. И соответственно могли бы определить соответствующий буфер. Но в данном случае мы этого 
точно не знаем - они могут быть больше размера буфера, а могут быть меньше. Очевидно, нам надо считывать данные в цикле, пока мы не получим последний байт ответа:using System.Net.Sockets;
using System.Text;

var port = 80;
var url = "www.google.com";

using var socket = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
try
{
    await socket.ConnectAsync(url, port);
    // определяем отправляемые данные
    var message = $"GET / HTTP/1.1\r\nHost: {url}\r\nConnection: close\r\n\r\n";
    // конвертируем данные в массив байтов
    var messageBytes = Encoding.UTF8.GetBytes(message);
    // отправляем данные
    await socket.SendAsync(messageBytes);

    // буфер для получения данных
    var responseBytes = new byte[512];
    // объект StringBuilder для склеивания ответа в строку
    var builder = new StringBuilder();
    int bytes;
    // в цикле получаем данные
    do
    {
        bytes = await socket.ReceiveAsync(responseBytes);
        // преобразуем полученный набор байтов в строку
        string responsePart = Encoding.UTF8.GetString(responseBytes, 0, bytes);
        // добавляем в StringBuilder
        builder.Append(responsePart);
    }
    while (bytes > 0);  // повторяем цикл, пока сервер отправляет более 0 байтов
    // выводим ответ на консоль
    Console.WriteLine(builder);
}
catch (SocketException ex)
{
    Console.WriteLine(ex.Message);
}теперь для считывания используем цикл do..while. Смотрим, сколько байтов возвращает ReceiveAsync. И пока он вернет 0 байтов, повторяем цикл. 
Полученные байты конвертируем в строку и добавляем в StringBuilder. В конце выводим полученное содержимое из StringBuilder на консоль:Теперь мы получили весь ответ от google.com. Но следует учитывать, что при отсутствии данных ReceiveAsync для tcp-сокетов завершает выполнение и возвращает количество байт только в том случае, когда буфер заполнен или когда одна из сторон завершает соединение. 
Поскольку TCP предполагает установление соединения, при котором хосты могут продолжительное время отправлять и получать данные. В примере выше сделано просто: 
на сервер google.com отправляется следующее сообщение:var message = $"GET / HTTP/1.1\r\nHost: {url}\r\nConnection: close\r\n\r\n";Кроме метода HTTP, пути и протокола здесь также отправляется заголовок "Connection: Close", который предписывает закрыть подключение после завершения текущей транзакции. Благодаря этому мы выполнение 
не зависает на строкеbytes = await socket.ReceiveAsync(responseBytes);Уберем этот заголовокvar message = $"GET / HTTP/1.1\r\nHost: {url}\r\n\r\n";И сокет бы продолжал ждать от google.com новых данных. Поскольку в данном случае мы имеем дело с потоковой передачей, и сокет может бесконечно ждать новую порцию данных. 
Но данный пример довольно ситуативен, поскольку google.com принимает запросы HTTP, и здесь идет манипуляция с заголовками HTTP. Но широта использования tcp-сокетов протоколом HTTP не ограничивается, и 
в других ситуациях могут потребоваться другие возможности (не говоря о том, что даже в новых версиях протокола HTTP отказались от заголовка Connection). И здесь же опять все зависит от удаленного хоста. Когда мы 
сами делаем клиент и сервер, мы сами можем определить любую логику взаимодействия. Когда мы никак не можем повлиять на работу удаленного хоста, то приходится сообразовать работу сокета с работой удаленного хоста. 
Тем не менее тут также есть варианты. Так, мы можем отключить получение и/или отправку данных на сокете с помощью методаShutdown()using System.Net.Sockets;
using System.Text;

var port = 80;
var url = "www.google.com";

using var socket = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
try
{
    await socket.ConnectAsync(url, port);

    var message = $"GET / HTTP/1.1\r\nHost: {url}\r\n\r\n";
    var messageBytes = Encoding.UTF8.GetBytes(message);
    await socket.SendAsync(messageBytes);

    // явным образом отключаем отправку данных на сокете
    socket.Shutdown(SocketShutdown.Send);

    var responseBytes = new byte[512];
    var builder = new StringBuilder();
    int bytes;
    do
    {
        bytes = await socket.ReceiveAsync(responseBytes);
        string responsePart = Encoding.UTF8.GetString(responseBytes, 0, bytes);
        builder.Append(responsePart);
    }
    while (bytes > 0);
    Console.WriteLine(builder);
}
catch (SocketException ex)
{
    Console.WriteLine(ex.Message);
}В данном случае после отправки данных сокет будет отключен от дальнейшей отправки данных с помощью вызоваsocket.Shutdown(SocketShutdown.Send), и после получения данных в методе ReceiveAsync google.com также завершит отправку.Свойство AvailableСвойствоAvailableхранит количество доступных для чтения байтов. Соответственно возникает вопрос, почему бы не использовать эти 
свойство для отслеживания наличия данных, например:do
{
    bytes = await socket.ReceiveAsync(responseBytes);
    string responsePart = Encoding.UTF8.GetString(responseBytes, 0, bytes);
    builder.Append(responsePart);
}
while (socket.Available > 0);Но свойство Available будет иметь ненулевое значение, если втекущий моментв потоке есть доступные для чтения данные. 
Но природа протокола TCP такова, что крупные наборы данных отправляются отдельными пакетами. Какой-то пакет 
может прийти быстрее, какой-то задержится, какой-то будет потерян, и потребуется переотправка. Поэтому может возникнуть ситуация, что сервер отправил данные, часть данных пришла. В какой-то момент 
свойство Available у сокета возратило 0, соответственно произошел выход из цикла. И в итоге мы получим неполные данные. Поэтому использование свойства Available 
в данном случае не лучший вариант.Обычно при получении данных используют одну из следующих стратегий, которые позволяют определить завершение получения данных:Использование буфера фиксированной длины, когда мы точно знаем, какой именно объем данных будет посланОтправка в ответе информации о размере ответа, получив которую, нам будет проще считать нужное количество байтовИспользование маркера окончания ответа, получив который, мы завершим считывание данныхВыбор и реализация конкретной стратегии всецело зависит от сервера, который получает запрос и отправляет ответ.Рефакторинг подключенияДля упрощения работы с сокетом мы можем вынести код подключения и код отправки-получения данных в отдельные методы:using System.Net.Sockets;
using System.Text;

var port = 80;
var url = "www.google.coms";
var response = await SocketSendReceiveAsync(url, port);
Console.WriteLine(response);

async Task<Socket?> ConnectSocketAsync(string url, int port)
{
    Socket tempSocket = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
    try
    {
        await tempSocket.ConnectAsync(url, port);
        return tempSocket;
    }
    catch(SocketException ex)
    {
        Console.WriteLine(ex.Message);
        tempSocket.Close();
    }
    return null;
}

async Task<string> SocketSendReceiveAsync(string url, int port)
{
    using Socket? socket = await ConnectSocketAsync(url, port);
    if (socket is null)
        return $"Не удалось установить соединение с {url}";

    // отправляем данные
    var message = $"GET / HTTP/1.1\r\nHost: {url}\r\nConnection: Close\r\n\r\n";
    var messageBytes = Encoding.UTF8.GetBytes(message);
    await socket.SendAsync(messageBytes);

    // получаем данные
    int bytes;
    // буфер для получения данных
    var responseBytes = new byte[512];
    var builder = new StringBuilder();
    do
    {
        bytes = await socket.ReceiveAsync(responseBytes);
        string responsePart = Encoding.UTF8.GetString(responseBytes, 0, bytes);
        builder.Append(responsePart);
    }
    while (bytes > 0);

    return builder.ToString();
}

**Источник:** [https://metanit.com/sharp/net/3.4.php](https://metanit.com/sharp/net/3.4.php)

[[Языки программирования/C#/Руководства/Сетевое программирование/Глава 2. Протокол HTTP/HttpListener. HTTP-сервер|Назад]] | [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 3. Протокол TCP|Протокол TCP]] | [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 3. Протокол TCP/TCP-сервер на сокетах|Вперёд]]
