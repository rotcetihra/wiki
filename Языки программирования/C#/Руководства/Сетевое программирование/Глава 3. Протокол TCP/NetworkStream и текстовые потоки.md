# NetworkStream и текстовые потоки

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Руководства|Руководства]] / [[Языки программирования/C#/Руководства/Сетевое программирование|Сетевое программирование]] / [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 3. Протокол TCP|Протокол TCP]] / NetworkStream и текстовые потоки

[[Языки программирования/C#/Руководства/Сетевое программирование/Глава 3. Протокол TCP/Многопоточное клиент-серверное приложение TCP|Назад]] | [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 3. Протокол TCP|Протокол TCP]] | [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 3. Протокол TCP/NetworkStream и бинарные потоки|Вперёд]]

**Дата написания:** 05.09.2026

## NetworkStream и текстовые потоки

Для упрощения работы с NetworkStream мы можем обертывать его в другие потоки.

Например, часто NetworkStream отправляет и получает только текстовые данные - обычные строки, и в этом случае вполне логично было бы использовать классы текстовых потоков 
 StreamWriter  и  StreamReader . Рассмотрим на примере отправки запроса к www.google.com и получения от него ответа:

```csharp
using System.Net.Sockets;

using TcpClient tcpClient = new TcpClient();
var server = "www.google.com";
await tcpClient.ConnectAsync(server, 80);

// получаем поток
var stream = tcpClient.GetStream();

var message = $"GET / HTTP/1.1\r\nHost: {server}\r\nConnection: Close\r\n\r\n";

using var writer = new StreamWriter(stream);
// отправляем сообщение
await writer.WriteAsync(message);
await writer.FlushAsync();

using var reader = new StreamReader(stream);
// считываем первую строку
var response = await reader.ReadLineAsync();
Console.WriteLine(response);
```

Для отправки текстовых данных в поток обертываем объект NetworkStream в StreamWriter. У класса StreamWriter есть ряд методов для записи текста в поток, в частности: 
 Write()/WriteAsync()  (для записи произвольного текста) и  WriteLine()/WriteLineAsync()  (для записи одной строки текста). 
здесь пишем в поток весь текст.

```csharp
await writer.WriteAsync(message);
```

Чтобы считать текстовые данные из потока обертываем NetworkStream в объект StreamReader. У него есть ряд методов для чтения данных: 
 ReadLine()/ReadLineAsync()  (для чтения одной строки),  Read()/ReadAsync()  (для данных в символьный буфер), 
 ReadBlock()/ReadBlockAsync()  (для чтения части данных в символьный массив) и 
 ReadToEnd()/ReadToEndAsync()  (для чтения всех данных из потока в строку). В примере выше считываем одну строку 

```csharp
var response = await reader.ReadLineAsync();
```

В итоге когда StreamReader считает из потока все символы до первого перевода строки, и мы получим по сути первую строку http-ответа от www.google.com:

```csharp
HTTP/1.1 200 OK
```

Теортически и практически мы можем конкретно в данном случае считать и весь ответ с помощью метода  `ReadToEnd()/ReadToEndAsync()` :

```csharp
using System.Net.Sockets;

using TcpClient tcpClient = new TcpClient();
var server = "www.google.com";
await tcpClient.ConnectAsync(server, 80);

// получаем поток
var stream = tcpClient.GetStream();

var message = $"GET / HTTP/1.1\r\nHost: {server}\r\nConnection: Close\r\n\r\n";

using var writer = new StreamWriter(stream);
// отправляем сообщение
await writer.WriteAsync(message);
await writer.FlushAsync();

using var reader = new StreamReader(stream);
// считываем весь ответ
var response = await reader.ReadToEndAsync();
Console.WriteLine(response);
```

Однако данные методы стоит использовать с осторожностью. Надо четко понимать протокол, в соответствии с которым мы общаемся с сервером. Например, в примере выше 
методReadToEndAsync()считывает до конца ответ. Благодаря тому, что в запросе посылается заголовокConnection: Close, который, в соответствии со стандартом 
HTTP1.1 предписывает закрыть подключение. Таким образом, сервер отправляет ответ и закрывает подключение, входящий поток имеет конец, и метощд считывает до конца. 
Однако это частная ситуация, посколько в целом TCP - это протокол, который позволяет поддерживать подключение в течение времени и обмениваться по нему сообщениями. 
В связи с этим просто может оказаться, что у потока нет окончания. В этой ситуация применять метод ReadToEndAsync не имеет смысла.Клиент-серверное взаимодействиеРассмотрим небольшой пример, где клиент и сервер используют текстовые потоки. Код сервера:using System.Net;
using System.Net.Sockets;

var tcpListener = new TcpListener(IPAddress.Any, 8888);
var words = new Dictionary()
{
    { "red", "красный" },
    { "blue", "синий" },
    { "green", "зеленый" }
};
try
{
    tcpListener.Start();    // запускаем сервер
    Console.WriteLine("Сервер запущен. Ожидание подключений... ");

    while (true)
    {
        // получаем подключение в виде TcpClient
        using var tcpClient = await tcpListener.AcceptTcpClientAsync();
        // получаем объект NetworkStream для взаимодействия с клиентом
        var stream = tcpClient.GetStream();

        // создаем StreamReader для чтения данных
        using var streamReader = new StreamReader(stream);
        // создаем StreamWriter для отправки данных
        using var streamWriter = new StreamWriter(stream);

        while (true)
        {
            // считываем запрошенное слово
            var word = await streamReader.ReadLineAsync();

            // если получен маркер окончания подключения - END, завершаем соединение с клиентом
            if (word == "END") break;

            Console.WriteLine($"Запрошен перевод слова {word}");
            // находим слово в словаре и отправляем обратно клиенту
            if (word is null || !words.TryGetValue(word, out var translation))
                translation = "не найдено в словаре";
            // отправляем перевод слова из словаря
            await streamWriter.WriteLineAsync(translation);
            await streamWriter.FlushAsync();
        }
    }
}
finally
{
    tcpListener.Stop();
}В данном случае мы предполагаем, что сервер будет выполнять роль своего рода словаря - получать от клиента слово и отправлять обратно его перевод. Для хранения 
данных определен тестовый словарь words:var words = new Dictionary<string, string>()
{
    {"red", "красный" },
    {"blue", "синий" },
    {"green", "зеленый" }
};При получении и обработке запросов сервер применяет простой прокотол из двух правил: каждое отдельное сообщение клиенту и серверу должно представлять строку 
(набор символов, который завершается переводом строки \n), а маркер окончания подключения должен представлять строку "END". 
В соответствии с этими правилами сервер сначала считывает запрос сервера и получаем слово, для которого надо выполнить перевод:var word = await streamReader.ReadLineAsync();Если отправлена строка "END", выходим из цикла и тем самым прекращаем работу с текущим клиентом:if (word == "END") break;Иначе находим в словаре перевод слова (при его наличии) и отправляем клиенту:if (word is null || !words.TryGetValue(word, out var translation))
    translation = "не найдено в словаре";
await streamWriter.WriteLineAsync(translation);
await streamWriter.FlushAsync();При этом опять же в соответствии с условным протоколом отправляем отдельную строку, благодаря чему клиент будет знать, что это окончание слова.Для этого сервера определим следующий тестовый клиент:using System.Net.Sockets;

// слова для отправки для получения перевода
var words = new string[] { "red", "yellow", "blue" };

using TcpClient tcpClient = new TcpClient();
await tcpClient.ConnectAsync("127.0.0.1", 8888);
// получаем NetworkStream для взаимодействия с сервером
var stream = tcpClient.GetStream();
// создаем StreamReader для чтения данных
using var streamReader = new StreamReader(stream);
// создаем StreamWriter для отправки данных
using var streamWriter = new StreamWriter(stream);

foreach(var word in words)
{
    // отправляем слово на сервер для перевода
    await streamWriter.WriteLineAsync(word);
    await streamWriter.FlushAsync();

    // получаем перевод от сервера
    var translation = await streamReader.ReadLineAsync();
    Console.WriteLine($"{word} - {translation}");
}
// посылаем маркер окончания подключения
await streamWriter.WriteLineAsync("END");
await streamWriter.FlushAsync();Здесь для теста определяем массив из трех слов, перевод которых мы собираемся получить:var words = new string[] { "red", "yellow", "blue" };Пробегаемся по этому массиву и отправляем каждое слово серверу:foreach (var word in words)
{
    await streamWriter.WriteLineAsync(word);
    await streamWriter.FlushAsync();Опять же в соответствии с принятым нами протоколом каждое слово отправляется в виде отдельной строки, поэтому применяется методWriteLineAsync. То есть сервер ждет строку, и 
соответственно клиент посылает ему строку..Затем считываем ответ сервера и получаем перевод слова:var translation = await streamReader.ReadLineAsync();
    Console.WriteLine($"{word} - {translation}");
}Для завершения посылаем сервер маркер окончания подключения:await streamWriter.WriteLineAsync("END"));Запустим сервер и клиент. При получении запросов консоль сервера отобразит запрошенные слова на перевод:Сервер запущен. Ожидание подключений...
Запрошен перевод слова red
Запрошен перевод слова yellow
Запрошен перевод слова blueА консоль клиента отобразит полученный от сервера перевод запрошенных слов:Слово red: красный
Слово yellow: не найдено в словаре
Слово blue: синий
Все сообщения отправленыПо сути здесь представлены те же самые сервер и клиент, что и в статьеОтправка и получение данных в TCP. Двунаправленная связь. Вы можете сравнить код, и увидить, насколько применение StreamReader и StreamWriter 
позволяют упростить код.

**Источник:** [https://metanit.com/sharp/net/6.1.php](https://metanit.com/sharp/net/6.1.php)

[[Языки программирования/C#/Руководства/Сетевое программирование/Глава 3. Протокол TCP/Многопоточное клиент-серверное приложение TCP|Назад]] | [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 3. Протокол TCP|Протокол TCP]] | [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 3. Протокол TCP/NetworkStream и бинарные потоки|Вперёд]]
