# NetworkStream и бинарные потоки

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Руководства|Руководства]] / [[Языки программирования/C#/Руководства/Сетевое программирование|Сетевое программирование]] / [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 3. Протокол TCP|Протокол TCP]] / NetworkStream и бинарные потоки

[[Языки программирования/C#/Руководства/Сетевое программирование/Глава 3. Протокол TCP/NetworkStream и текстовые потоки|Назад]] | [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 3. Протокол TCP|Протокол TCP]] | [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 3. Протокол TCP/Консольный TCP-чат|Вперёд]]

**Дата написания:** 05.09.2026

## NetworkStream и бинарные потоки

Для чтения и записи бинарных данных, которые представляют примитивные типы, в .NET используются классы BinaryReader и BinaryWriter. 
Подобно тому, как с их помощью можно писать данные в файл или читать из файла, также можно читать и писать бинарные данные в сетевой поток NetworkStream.

Для отправки бинарных данных в поток объект NetworkStream обертывается в объект класса  BinaryWriter , 
который для отправки данных предоставляет метод  Write() .

Для чтения бинарных данных из потока объект NetworkStream обертывается в объект класса  BinaryReader , 
который для чтения данных предоставляет ряд методов:

- `ReadBoolean()`
- `ReadByte()`
- `ReadBytes()`
- `ReadChar()`
- `ReadChars()`
- `ReadDecimal()`
- `ReadDouble()`
- `ReadHalf()`
- `ReadInt16()`
- `ReadInt32()`
- `ReadInt64()`
- `ReadSByte()`
- `ReadSingle()`
- `ReadString()`
- `ReadUInt16()`
- `ReadUInt32()`
- `ReadUInt64()`

Допустим, клиент будет отправлять данные товара, как название товара, производитель, количество и цена. А сервер получит эти данные создаст из них 
товар и отправит в ответ клиенту сгенерированный идентификатор товара.

Вначале определим код сервера:

```csharp
using System.Net;
using System.Net.Sockets;

var tcpListener = new TcpListener(IPAddress.Any, 8888);
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

        // создаем BinaryReader для чтения данных
        using var binaryReader = new BinaryReader(stream);
        // создаем BinaryWriter для отправки данных
        using var binaryWriter = new BinaryWriter(stream);

        var name = binaryReader.ReadString();
        var company = binaryReader.ReadString();
        var count = binaryReader.ReadInt32();
        var price = binaryReader.ReadDecimal();

        string id = Guid.NewGuid().ToString();
        var newProduct = new Product(id, name, company, count, price);
        Console.WriteLine($"Добавлен новый товар: {newProduct}");

        // отправляем клиенту сгенерированный id
        binaryWriter.Write(newProduct.Id);
        binaryWriter.Flush();
    }
}
finally
{
    tcpListener.Stop();
}

record Product(string Id, string Name, string Company, int Count, decimal Price);
```

Для считывания данных обертываем объект NetworkStream в BinaryReader, а для записи данных - в объект BinaryWriter:

```csharp
using var binaryReader = new BinaryReader(stream);
using var binaryWriter = new BinaryWriter(stream);
```

Далее по порядку с помощью методов BinaryWriter считываем присланные данные определенного типа:

```csharp
var name = binaryReader.ReadString();
var company = binaryReader.ReadString();
var count = binaryReader.ReadInt32();
var price = binaryReader.ReadDecimal();
```

Далее генерируем Id с помощью функции  `Guid.NewGuid()` , создаем объект Product, выводим его данные на консоль и отправляем в ответ id товара:

```csharp
string id = Guid.NewGuid().ToString();
var newProduct = new Product(id, name, company, count, price);
Console.WriteLine($"Добавлен новый товар: {newProduct}");

binaryWriter.Write(newProduct.Id);
binaryWriter.Flush();
```

#### Клиент

Теперь для этого сервера определим тестовый клиент:

```csharp
using System.Net.Sockets;

// данные для отправки
string name = "iPhone 14";
string company = "Apple";
int count = 2;
decimal price = 145890.34m;

using TcpClient tcpClient = new TcpClient();
await tcpClient.ConnectAsync("127.0.0.1", 8888);
// получаем NetworkStream для взаимодействия с сервером
var stream = tcpClient.GetStream();
// создаем BinaryReader для чтения данных
using var binaryReader = new BinaryReader(stream);
// создаем BinaryWriter для отправки данных
using var binaryWriter = new BinaryWriter(stream);

// отправляем данные товара
binaryWriter.Write(name);
binaryWriter.Write(company);
binaryWriter.Write(count);
binaryWriter.Write(price);
binaryWriter.Flush();

// считываем сгенерированный на сервере id нового товара
var id = binaryReader.ReadString(); 
Console.WriteLine($"Id нового товара: {id}");
```

Здесь сначала определяем данные товара для отправки:

```csharp
string name = "iPhone 14";
string company = "Apple";
int count = 2;
decimal price = 145890.34m;
```

Как и в коде сервера создаем обертки NetworkStream в виде объектов BinaryReader и BinaryWriter:

```csharp
using var binaryReader = new BinaryReader(stream);
using var binaryWriter = new BinaryWriter(stream);
```

Затем отправляем данные с помощью метода Write объекта BinaryWriter:

```csharp
binaryWriter.Write(name);
binaryWriter.Write(company);
binaryWriter.Write(count);
binaryWriter.Write(price);
binaryWriter.Flush();
```

Обратите внимание на последовательность отправки - она должна соответствовать последовательности приема на сервере. То есть сервер сначала принимает строку, потом строку, потом int, потом decimal. 
Соответственно в клиенте сначала отправляем string, потом string, затем int и в конце decimal.

После отправки данных считываем отправленный сервером id товара:

```csharp
var id = binaryReader.ReadString(); 
Console.WriteLine($"Id нового товара: {id}");
```

Запустим программы сервера и клиента. Консоль сервера отобразит данные созданного товара:

```csharp
Сервер запущен. Ожидание подключений...
Добавлен новый товар: Product { Id = 7c036c0d-2682-4f6d-9b7b-7e4869192e21, Name = iPhone 14, Company = Apple, Count = 2, Price = 145890,34 }
```

а консоль клиента выведет полученный идентификатор товара:

```csharp
Id нового товара: 7c036c0d-2682-4f6d-9b7b-7e4869192e21
```

**Источник:** [https://metanit.com/sharp/net/6.2.php](https://metanit.com/sharp/net/6.2.php)

[[Языки программирования/C#/Руководства/Сетевое программирование/Глава 3. Протокол TCP/NetworkStream и текстовые потоки|Назад]] | [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 3. Протокол TCP|Протокол TCP]] | [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 3. Протокол TCP/Консольный TCP-чат|Вперёд]]
