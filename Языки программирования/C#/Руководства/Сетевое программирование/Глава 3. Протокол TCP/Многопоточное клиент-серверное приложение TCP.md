# Многопоточное клиент-серверное приложение TCP

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Руководства|Руководства]] / [[Языки программирования/C#/Руководства/Сетевое программирование|Сетевое программирование]] / [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 3. Протокол TCP|Протокол TCP]] / Многопоточное клиент-серверное приложение TCP

[[Языки программирования/C#/Руководства/Сетевое программирование/Глава 3. Протокол TCP/Отправка и получение данных. Двунаправленная связь|Назад]] | [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 3. Протокол TCP|Протокол TCP]] | [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 3. Протокол TCP/NetworkStream и текстовые потоки|Вперёд]]

**Дата написания:** 05.09.2026

## Многопоточное клиент-серверное приложение TCP

Рассмотрим, как создать многопоточное клиент-серверное приложение. Фактически оно будет отличаться от однопоточного только тем, что обработка 
запроса клиента будет вынесена в отдельный поток. За основу возьмем проект из прошлой статьи.

### Пример с TcpListener и TcpClient

#### Определение сервера

На стороне сервера определим следующий код:

```csharp
using System.Net;
using System.Net.Sockets;
using System.Text;

var tcpListener = new TcpListener(IPAddress.Any, 8888);

try
{
    tcpListener.Start();    // запускаем сервер
    Console.WriteLine("Сервер запущен. Ожидание подключений... ");

    while (true)
    {
        // получаем подключение в виде TcpClient
        var tcpClient = await tcpListener.AcceptTcpClientAsync();

        // создаем новую задачу для обслуживания нового клиента
        Task.Run(async ()=>await ProcessClientAsync(tcpClient));

        // вместо задач можно использовать стандартный Thread
        // new Thread(async ()=>await ProcessClientAsync(tcpClient)).Start();
    }
}
finally
{
    tcpListener.Stop();
}
// обрабатываем клиент
async Task ProcessClientAsync(TcpClient tcpClient)
{
    // условный словарь
    var words = new Dictionary<string, string>()
    {
        {"red", "красный" },
        {"blue", "синий" },
        {"green", "зеленый" },
    };
    var stream = tcpClient.GetStream();
    // буфер для входящих данных
    var response = new List<byte>();
    int bytesRead = 10;
    while (true)
    {
        // считываем данные до конечного символа
        while ((bytesRead = stream.ReadByte()) != '\n')
        {
            // добавляем в буфер
            response.Add((byte)bytesRead);
        }
        var word = Encoding.UTF8.GetString(response.ToArray());

        // если прислан маркер окончания взаимодействия,
        // выходим из цикла и завершаем взаимодействие с клиентом
        if (word == "END") break;

        Console.WriteLine($"Клиент {tcpClient.Client.RemoteEndPoint} запросил перевод слова {word}");
        // находим слово в словаре и отправляем обратно клиенту
        if (!words.TryGetValue(word, out var translation)) translation = "не найдено в словаре";
        // добавляем символ окончания сообщения 
        translation += '\n';
        // отправляем перевод слова из словаря
        await stream.WriteAsync(Encoding.UTF8.GetBytes(translation));
        response.Clear();
    }
    tcpClient.Close();
}
```

Здесь обработка клиента вынесена в отдельный метод ProcessClientAsync. Для обработки запускаем новую задачу, где вызываем данный метод и передаем ему полученный объект TcpClient:

```csharp
Task.Run(async ()=>await ProcessClientAsync(tcpClient));
```

В качестве альтернативы можно запускать новый поток Thread:

```csharp
new Thread(async ()=>await ProcessClientAsync(tcpClient)).Start();
```

В данном случае мы предполагаем, что сервер будет выполнять роль своего рода словаря - получать от клиента слово и отправлять обратно его перевод. Для 
хранения данных в методе ProcessClientAsync определен тестовый словарь words:

```csharp
var words = new Dictionary<string, string>()
{
    {"red", "красный" },
    {"blue", "синий" },
    {"green", "зеленый" },
};
```

При получении и обработке запросов сервер применяет простой прокотол из двух правил: каждое отдельное сообщение клиенту и серверу должно оканчиваться символом \n, а маркер окончания 
подключения должен представлять строку "END". В соответствии с этими правилами сервер сначала считывает запрос сервера и получаем слово, для которого надо выполнить перевод:

```csharp
while ((bytesRead = stream.ReadByte()) != '\n')
{
    response.Add((byte)bytesRead);
}
var word = Encoding.UTF8.GetString(response.ToArray());
```

Если отправлена строка "END", выходим из цикла и тем самым прекращаем работу с текущим клиентом:

```csharp
if (word == "END") break;
```

Иначе находим в словаре перевод слова (при его наличии) и отправляем клиенту:

```csharp
if (!words.TryGetValue(word, out var translation)) translation = "не найдено в словаре";
translation += '\n';
await stream.WriteAsync(Encoding.UTF8.GetBytes(translation));
```

При этом опять же в соответствии с условным протоколом при отправке добавляем к сообщению символ \n, благодаря чему клиент будет знать, что это окончание слова.

В конце закрываем подключение:

```csharp
tcpClient.Close();
```

#### Создание клиента

Для вышеопределенного сервера создадим следующий тестовый tcp-клиент:

```csharp
using System.Net.Sockets;
using System.Text;

// слова для отправки для получения перевода
var words = new string[] { "red", "yellow", "blue", "green" };

using TcpClient tcpClient = new TcpClient();
await tcpClient.ConnectAsync("127.0.0.1", 8888);
var stream = tcpClient.GetStream();

// буфер для входящих данных
var response = new List<byte>();
int bytesRead = 10; // для считывания байтов из потока
foreach (var word in words)
{
    // считываем строку в массив байтов
    // при отправке добавляем маркер завершения сообщения - \n
    byte[] data = Encoding.UTF8.GetBytes(word + '\n');
    // отправляем данные
    await stream.WriteAsync(data);

    // считываем данные до конечного символа
    while ((bytesRead = stream.ReadByte()) != '\n')
    {
        // добавляем в буфер
        response.Add((byte)bytesRead);
    }
    var translation = Encoding.UTF8.GetString(response.ToArray());
    Console.WriteLine($"Слово {word}: {translation}");
    response.Clear();
    // имитируем долговременную работу, чтобы одновременно несколько клиентов обрабатывались
    await Task.Delay(2000);
}

// отправляем маркер завершения подключения - END
await stream.WriteAsync(Encoding.UTF8.GetBytes("END\n"));
```

Здесь для теста определяем массив из четырех слов, перевод которых мы собираемся получить:

```csharp
var words = new string[] { "red", "yellow", "blue", "green" };
```

Пробегаемся по этому массиву и отправляем каждое слово серверу:

```csharp
foreach (var word in words)
{
    // при отправке добавляем маркер завершения сообщения - \n
    byte[] data = Encoding.UTF8.GetBytes(word + '\n');
    await stream.WriteAsync(data);
```

Опять же в соответствии с принятым нами протоколом каждое слово завершается символом \n.

Затем считываем ответ сервера и получаем перевод слова:

```csharp
while ((bytesRead = stream.ReadByte()) != '\n')
{   
    response.Add((byte)bytesRead);
}
var translation = Encoding.UTF8.GetString(response.ToArray());
```

Для завершения посылаем сервер маркер окончания подключения:

```csharp
await stream.WriteAsync(Encoding.UTF8.GetBytes("END\n"));
```

Запустим сервер и пару клиентов, чтобы они одновременно обращались к серверу. Консоль сервера выведет нам адреса клиентов и запрошенные ими слова:

```csharp
Сервер запущен. Ожидание подключений...
Клиент 127.0.0.1:51449 запросил перевод слова red
Клиент 127.0.0.1:51450 запросил перевод слова red
Клиент 127.0.0.1:51449 запросил перевод слова yellow
Клиент 127.0.0.1:51450 запросил перевод слова yellow
Клиент 127.0.0.1:51449 запросил перевод слова blue
Клиент 127.0.0.1:51450 запросил перевод слова blue
Клиент 127.0.0.1:51449 запросил перевод слова green
Клиент 127.0.0.1:51450 запросил перевод слова green
```

А каждый из клиентов отобразит запрошенные слова и их перевод:

```csharp
Слово red: красный
Слово yellow: не найдено в словаре
Слово blue: синий
Слово green: зеленый
```

### Многопоточое клиент-серверное приложение на сокетах

Создадим аналогичный пример на чистых сокетах. Определим следующий код сервера:

```csharp
using System.Net;
using System.Net.Sockets;
using System.Text;

using Socket tcpListener = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);

try
{
    tcpListener.Bind(new IPEndPoint(IPAddress.Any, 8888));
    tcpListener.Listen();    // запускаем сервер
    Console.WriteLine("Сервер запущен. Ожидание подключений... ");

    while (true)
    {
        // получаем подключение в виде TcpClient
        var tcpClient = await tcpListener.AcceptAsync();

        // создаем новую задачу для обслуживания нового клиента
        Task.Run(async() => await ProcessClientAsync(tcpClient));

        // вместо задач можно использовать стандартный Thread
        // new Thread(async ()=> await ProcessClientAsync(tcpClient)).Start();
    }
}
catch(Exception ex)
{
    Console.WriteLine(ex.Message);
}

// обрабатываем клиент
async Task ProcessClientAsync(Socket tcpClient)
{
    // условный словарь
    var words = new Dictionary<string, string>()
    {
        { "red", "красный" },
        { "blue", "синий" },
        { "green", "зеленый" },
    };
    // буфер для накопления входящих данных
    var response = new List<byte>();
    // буфер для считывания одного байта
    var bytesRead = new byte[1];
    while (true)
    {
        // считываем данные до конечного символа
        while (true)
        {
            var count = await tcpClient.ReceiveAsync(bytesRead);
            // смотрим, если считанный байт представляет конечный символ, выходим
            if (count == 0 || bytesRead[0] == '\n') break;
            // иначе добавляем в буфер
            response.Add(bytesRead[0]);
        }
        var word = Encoding.UTF8.GetString(response.ToArray());
        // если прислан маркер окончания взаимодействия,
        // выходим из цикла и завершаем взаимодействие с клиентом
        if (word == "END") break;

        Console.WriteLine($"Запрошен перевод слова {word}");
        // находим слово в словаре и отправляем обратно клиенту
        if (!words.TryGetValue(word, out var translation)) translation = "не найдено в словаре";
        // добавляем символ окончания сообщения 
        translation += '\n';
        // отправляем перевод слова из словаря
        await tcpClient.SendAsync(Encoding.UTF8.GetBytes(translation));
        response.Clear();
    }
    tcpClient.Shutdown(SocketShutdown.Both);
    tcpClient.Close();
}
```

И определим следующий код клиента:

```csharp
using System.Net.Sockets;
using System.Text;

// слова для отправки для получения перевода
var words = new string[] { "red", "yellow", "blue" };

using var tcpClient = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
try
{
    await tcpClient.ConnectAsync("127.0.0.1", 8888);
    // буфер для входящих данных
    var response = new List<byte>();
    foreach (var word in words)
    {
        // считыванием строку в массив байт
        // при отправке добавляем маркер завершения сообщения - \n
        byte[] data = Encoding.UTF8.GetBytes(word + '\n');
        // отправляем данные
        await tcpClient.SendAsync(data);

        // буфер для считывания одного байта
        var bytesRead = new byte[1];
        // считываем данные до конечного символа
        while (true)
        {
            var count = tcpClient.Receive(bytesRead);
            // смотрим, если считанный байт представляет конечный символ, выходим
            if (count == 0 || bytesRead[0] == '\n') break;
            // иначе добавляем в буфер
            response.Add(bytesRead[0]);
        }
        var translation = Encoding.UTF8.GetString(response.ToArray());
        Console.WriteLine($"Слово {word}: {translation}");
        response.Clear();
        // имитируем долговременную работу, чтобы одновременно несколько клиентов обрабатывались
        await Task.Delay(2000);
    }
    // отправляем маркер завершения подключения - END
    await tcpClient.SendAsync(Encoding.UTF8.GetBytes("END\n"));
}
catch (Exception ex)
{
    Console.WriteLine(ex.Message);
}
```

**Источник:** [https://metanit.com/sharp/net/4.3.php](https://metanit.com/sharp/net/4.3.php)

[[Языки программирования/C#/Руководства/Сетевое программирование/Глава 3. Протокол TCP/Отправка и получение данных. Двунаправленная связь|Назад]] | [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 3. Протокол TCP|Протокол TCP]] | [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 3. Протокол TCP/NetworkStream и текстовые потоки|Вперёд]]
