# Консольный UDP-чат

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Руководства|Руководства]] / [[Языки программирования/C#/Руководства/Сетевое программирование|Сетевое программирование]] / [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 4. Протокол UDP|Протокол UDP]] / Консольный UDP-чат

[[Языки программирования/C#/Руководства/Сетевое программирование/Глава 4. Протокол UDP/UdpClient|Назад]] | [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 4. Протокол UDP|Протокол UDP]] | [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 4. Протокол UDP/Широковещательная рассылка|Вперёд]]

**Дата написания:** 05.09.2026

## Консольный UDP-чат

В прошлых темах рассматривалось взаимодействие по сети с помощью протокола UDP. Теперь рассмотрим чуть более сложный пример, когда udp-клиент 
одновременно посылает и отправляет данные. Для этого определим простейший udp-чат. Хотя создание консольных чатов - не самое удобное дело, учитывая, что поле для ввода сообщений 
совмещено с полем вывода сообщений. Но в данном случае мы абстрагируемся от конкретной технологии графических приложений и просто акцентируем внимание на взаимодейтсвии с помощью 
протокола UDP.

### Консольный чат на UDP-сокетах

Сначала используем чистые udp-сокеты и для этого определим следующий код программы:

```csharp
using System.Net;
using System.Net.Sockets;
using System.Text;

IPAddress localAddress = IPAddress.Parse("127.0.0.1");
Console.Write("Введите свое имя: ");
string? username = Console.ReadLine();
Console.Write("Введите порт для приема сообщений: ");
if (!int.TryParse(Console.ReadLine(), out var localPort)) return;
Console.Write("Введите порт для отправки сообщений: ");
if (!int.TryParse(Console.ReadLine(), out var remotePort)) return;
Console.WriteLine();

// запускаем получение сообщений
Task.Run(ReceiveMessageAsync);
// запускаем ввод и отправку сообщений
await SendMessageAsync();

// отправка сообщений в группу
async Task SendMessageAsync()
{
    using Socket sender = new Socket(AddressFamily.InterNetwork, SocketType.Dgram, ProtocolType.Udp);
    Console.WriteLine("Для отправки сообщений введите сообщение и нажмите Enter");
    // отправляем сообщения
    while (true)
    {
        var message = Console.ReadLine(); // сообщение для отправки
        // если введена пустая строка, выходим из цикла и завершаем ввод сообщений
        if (string.IsNullOrWhiteSpace(message)) break;
        // иначе добавляем к сообщению имя пользователя
        message = $"{username}: {message}";
        byte[] data = Encoding.UTF8.GetBytes(message);
        // и отправляем на 127.0.0.1:remotePort
        await sender.SendToAsync(data, new IPEndPoint(localAddress, remotePort));
    }
}
// отправка сообщений
async Task ReceiveMessageAsync()
{
    byte[] data = new byte[65535]; // буфер для получаемых данных
    // сокет для прослушки сообщений
    using Socket receiver = new Socket(AddressFamily.InterNetwork, SocketType.Dgram, ProtocolType.Udp);
    // запускаем получение сообщений по адресу 127.0.0.1:localPort
    receiver.Bind(new IPEndPoint(localAddress, localPort));
    while (true)
    {
        // получаем данные в массив data
        var result = await receiver.ReceiveFromAsync(data, new IPEndPoint(IPAddress.Any, 0));
        var message = Encoding.UTF8.GetString(data, 0, result.ReceivedBytes);
        // выводим сообщение
        Console.WriteLine(message);
    }
}
```

Вначале определяем адрес, по которому будет запущена программа

```csharp
IPAddress localAddress = IPAddress.Parse("127.0.0.1");
```

Вначале пользователь вводит свое имя, а также порты для приема данных и для отправки. Предполагается, что два приложения клиента, 
которые будут между собой взаимодействовать, запущены на одной локальной машине по адресу "127.0.0.1". Если адреса клиентов различаются, то можно предусмотреть и 
ввода адреса для отправки данных.

После ввода портов запускается задача на прослушивание входящих сообщений и метод для отправки данных:

```csharp
// запускаем получение сообщений
Task.Run(ReceiveMessageAsync);
// запускаем ввод и отправку сообщений
await SendMessageAsync();
```

В методе ReceiveMessageAsync создаем сокет для получения данных и запускаем прослушивание с помощью метода Bind:

```csharp
using Socket receiver = new Socket(AddressFamily.InterNetwork, SocketType.Dgram, ProtocolType.Udp);
receiver.Bind(new IPEndPoint(localAddress, localPort));
```

Далее в бесконечном цикле получаем данные в массив data, преобразуем их в строку и выводим на консоль:

```csharp
var result = await receiver.ReceiveFromAsync(data, new IPEndPoint(IPAddress.Any, 0));
var message = Encoding.UTF8.GetString(data, 0, result.ReceivedBytes);
Print(message);
```

В методе  `SendMessageAsync()`  для отправки сообщений создается отдельный сокет:

```csharp
using Socket sender = new Socket(AddressFamily.InterNetwork, SocketType.Dgram, ProtocolType.Udp);
```

Затем считываем введенное сообщение, добавляем к нему имя пользователя, преобразуем сообщение в массив байт и отправляем на порт remotePort:

```csharp
var message = Console.ReadLine();
if (string.IsNullOrWhiteSpace(message)) break;
message = $"{username}: {message}";
byte[] data = Encoding.UTF8.GetBytes(message);
await sender.SendToAsync(data, new IPEndPoint(localAddress, remotePort));
```

Если введена пустая строка, то выходим из цикла и соответственно из метода и завершаем приложение.

Теперь запустим две копии приложения и введем разные данные для портов. Первый клиент:

```csharp
Введите свое имя: Евгений
Введите порт для приема сообщений: 4004
Введите порт для отправки сообщений: 4005

Для отправки сообщений введите сообщение и нажмите Enter
Том: Привет чат!
Привет Том!
Том: Как дела, Евгений
```

Второй клиент:

```csharp
Введите свое имя: Том
Введите порт для приема сообщений: 4005
Введите порт для отправки сообщений: 4004

Для отправки сообщений введите сообщение и нажмите Enter
Привет чат!
Евгений: Привет Том!
Как дела, Евгений
```

Здесь первый клиент получает сообщения на порт 4004 и отправляет на порт 4005, а второй клиент, наоборот, получает сообщения на порт 4005, а отправляет на порт 4004. Таким образом, 
оба запущенных на одной машине клиента будут взаимодействовать друг с другом.

Стоит отметить, что хотя здесь для отправки и получения сообщений создавались разные сокеты, но это необязательно. В принципе мы можем использовать один и тот же сокет.

### Консольный чат с помощью UdpClient

Применение UdpClient позволяет немного упростить программу. Тот же чат, только с UdpClient:

```csharp
using System.Net;
using System.Net.Sockets;
using System.Text;

IPAddress localAddress = IPAddress.Parse("127.0.0.1");
Console.Write("Введите свое имя: ");
string? username = Console.ReadLine();
Console.Write("Введите порт для приема сообщений: ");
if (!int.TryParse(Console.ReadLine(), out var localPort)) return;
Console.Write("Введите порт для отправки сообщений: ");
if (!int.TryParse(Console.ReadLine(), out var remotePort)) return;
Console.WriteLine();

// запускаем получение сообщений
Task.Run(ReceiveMessageAsync);
// запускаем ввод и отправку сообщений
await SendMessageAsync();

// отправка сообщений в группу
async Task SendMessageAsync()
{
    using UdpClient sender = new UdpClient();
    Console.WriteLine("Для отправки сообщений введите сообщение и нажмите Enter");
    // отправляем сообщения
    while (true)
    {
        var message = Console.ReadLine(); // сообщение для отправки
        // если введена пустая строка, выходим из цикла и завершаем ввод сообщений
        if (string.IsNullOrWhiteSpace(message)) break;
        // иначе добавляем к сообщению имя пользователя
        message = $"{username}: {message}";
        byte[] data = Encoding.UTF8.GetBytes(message);
        // и отправляем на 127.0.0.1:remotePort
        await sender.SendAsync(data, new IPEndPoint(localAddress, remotePort));
    }
}
// отправка сообщений
async Task ReceiveMessageAsync()
{
    using UdpClient receiver = new UdpClient(localPort);
    while (true)
    {
        // получаем данные
        var result = await receiver.ReceiveAsync();
        var message = Encoding.UTF8.GetString(result.Buffer);
        // выводим сообщение
        Console.WriteLine(message);
    }
}
```

### Наложение полученного сообщения на ввод сообщения

Примеры консольного чата выше довольно просты, запускаются на том же компьютере. И мы последовательно отправляем сообщение сначала в одном приложении, а потом в другом. 
Но что, если клиенты на разных машинах, и один клиент присылает сообщение непосредственно в то время, когда 
другой клиент вводит свое сообщение? Тогда очевидно полченное сообщение выводится в той же строке консоли, где клиент вводит свое сообщение. Если ОС windows, 
то мы можем добавить в программу небольшой хак, чтобы этого избежать - копировать уже введенные символы еще не отправленного сообщения на следующую строку, 
а на текущей выводит полученное сообщение. Для этого изменим метод ReceiveMessageAsync следующим образом:

```csharp
async Task ReceiveMessageAsync()
{
    // сокет для прослушки сообщений
    using UdpClient receiver = new UdpClient(localPort);
    while (true)
    {
        // получаем данные в массив data
        var result = await receiver.ReceiveAsync();
        var message = Encoding.UTF8.GetString(result.Buffer);
        // выводим сообщение
        Print(message);
    }
}

void Print(string message)
{
    if (OperatingSystem.IsWindows())    // если ОС Windows
    {
        var position = Console.GetCursorPosition(); // получаем текущую позицию курсора
        int left = position.Left;   // смещение в символах относительно левого края
        int top = position.Top;     // смещение в строках относительно верха
        // копируем ранее введенные символы в строке на следующую строку
        Console.MoveBufferArea(0, top, left, 1, 0, top + 1);
        // устанавливаем курсор в начало текущей строки
        Console.SetCursorPosition(0, top);
        // в текущей строке выводит полученное сообщение
        Console.WriteLine(message);
        // переносим курсор на следующую строку
        // и пользователь продолжает ввод уже на следующей строке
        Console.SetCursorPosition(left, top + 1);
    }
    else Console.WriteLine(message);
}
```

**Источник:** [https://metanit.com/sharp/net/5.3.php](https://metanit.com/sharp/net/5.3.php)

[[Языки программирования/C#/Руководства/Сетевое программирование/Глава 4. Протокол UDP/UdpClient|Назад]] | [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 4. Протокол UDP|Протокол UDP]] | [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 4. Протокол UDP/Широковещательная рассылка|Вперёд]]
