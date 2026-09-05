# Отправка запросов с помощью HttpClient

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Руководства|Руководства]] / [[Языки программирования/C#/Руководства/Сетевое программирование|Сетевое программирование]] / [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 2. Протокол HTTP|Протокол HTTP]] / Отправка запросов с помощью HttpClient

[[Языки программирования/C#/Руководства/Сетевое программирование/Глава 2. Протокол HTTP/Создание HttpClient|Назад]] | [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 2. Протокол HTTP|Протокол HTTP]] | [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 2. Протокол HTTP/Получение данных в формате JSON|Вперёд]]

**Дата написания:** 05.09.2026

## Отправка запросов с помощью HttpClient

Для выполнения запросов класс  HttpClient  предоставляет ряд методов:

- Send() / SendAsync() : отправляет запрос в виде объекта HttpRequestMessage и получает ответ сервера в виде объекта HttpResponseMessage
- GetAsync() : отправляет GET-запрос на указанный адрес и получает ответ сервера в виде объекта HttpResponseMessage
- GetByteArrayAsync() : отправляет GET-запрос на указанный адрес и возвращает ответ в виде массива байтов ( `byte[]` )
- GetStreamAsync() : отправляет GET-запрос на указанный адрес и возвращает ответ в виде объекта Stream
- GetStringAsync() : отправляет GET-запрос на указанный адрес и возвращает ответ в виде строки
- PostAsync() : отправляет POST-запрос на указанный адрес и получает ответ сервера в виде объекта HttpResponseMessage
- PutAsync() : отправляет PUT-запрос на указанный адрес и получает ответ сервера в виде объекта HttpResponseMessage
- PatchtAsync() : отправляет Patch-запрос на указанный адрес и получает ответ сервера в виде объекта HttpResponseMessage
- DeleteAsync() : отправляет DELETE-запрос на указанный адресми получает ответ сервера в виде объекта HttpResponseMessage

С помощью ряда свойств можно настроить базовые настройки отправки запросов:

- BaseAddress : возвращает или устанавливает базовый адрес в виде объекта URI, который будет использоваться при отправке запросов.
- DefaultProxy : возвращает или устанавливает настройки прокси.
- DefaultRequestHeaders :  возвращает или устанавливает коллекцию заголовков по умолчанию, которые отправляются на сервер при каждом запросе
- DefaultRequestVersion : возвращает или устанавливает версию протокола HTTP по умолчанию, которая применяется при отправке запросов
- DefaultVersionPolicy : возвращает или устанавливает политику версии по умолчанию
- MaxResponseContentBufferSize : возвращает или устанавливает максимальный размер буфера в байтов при считывании 
данных ответа
- Timeout : возвращает или устанавливает тайм-аут перед отправкой запроса.

### Отправка запроса методом SendAsync

Рассмотрим универсальную отправку запроса с помощью метода  SendAsync() . Данный метод имеет ряд версий, но как минимум принимает данные 
запроса (объект  HttpRequestMessage ) и возвращает ответ в виде объекта  HttpResponseMessage :

```csharp
public Task<System.Net.Http.HttpResponseMessage> SendAsync (System.Net.Http.HttpRequestMessage request);
```

#### Установка данных запроса

Класс  HttpRequestMessage  позволяет настроить данные запроса с помощью следующих свойств:

- Content : возвращает или устанавливает содержимое запроса
- Method : возвращает или устанавливает метод запроса.
- RequestUri : возвращает или устанавливает адрес запроса в виде объекта Uri.
- Version : возвращает или устанавливает версию протокола HTTP.

Установить метод и адрес запроса также можно с помощью одного из конструкторов класса:

```csharp
class Program
{
    static HttpClient httpClient = new HttpClient();

    static async Task Main()
    {
        // определяем данные запроса
        using HttpRequestMessage request = new HttpRequestMessage(HttpMethod.Get, "https://www.google.com");
        // выполняем запрос
        await httpClient.SendAsync(request);
    }
}
```

### Получение ответа

После выполнения запроса метод SendAsync возвращает ответ в виде объекта  HttpResponseMessage . Данный объект позволяет получить данные ответа с помощью следующих свойств:

- Content : возвращает или устанавливает содержимое HTTP-ответа. 
Это свойство представляет объект  HttpContent , который позволяет считать данные запроса с помощью одного из методов: `ReadAsStringAsync()` : возвращает ответ в виде строки `ReadAsByteArrayAsync()` : возвращает ответ в виде массива байт `ReadAsStreemAsync()` : возвращает ответ в виде потока - объекта Stream
- Headers : возвращает коллекцию заголовков HTTP-ответа (объект  `HttpResponseHeaders` ). Каждый заголовок в этой коллекции представлен парой ключ-значения. 
Для получения конкретного заголовка можно использовать метод  `GetValues()` , в который передается название заголовка: response.Headers.GetValues("Accept")
- IsSuccessStatusCode : возвращает  `true` , если запрос HTTP прошел успешно.
- ReasonPhrase : возвращает сообщение статуса.
- RequestMessage : возвращает данные запроса, которые связаны с этим ответом.
- StatusCode : возвращает статусный код ответа.
- TrailingHeaders : возвращает дополнительных заголовков, включенных в запрос HTTP.
- Version : возвращает версию использованного протокола HTTP.

Например, отправим запрос на "www.google.com" и выведем данные ответа на консоль:

```csharp
class Program
{
    static HttpClient httpClient = new HttpClient();

    static async Task Main()
    {
        // определяем данные запроса
        using HttpRequestMessage request = new HttpRequestMessage(HttpMethod.Get, "https://www.google.com");
        
        // получаем ответ
        using HttpResponseMessage response = await httpClient.SendAsync(request);

        // просматриваем данные ответа
        // статус
        Console.WriteLine($"Status: {response.StatusCode}\n");
        //заголовки
        Console.WriteLine("Headers");
        foreach (var header in response.Headers)
        {
            Console.Write($"{header.Key}:");
            foreach(var headerValue in header.Value)
            {
                Console.WriteLine(headerValue);
            }
        }
        // содержимое ответа
        Console.WriteLine("\nContent");
        string content = await response.Content.ReadAsStringAsync();
        Console.WriteLine(content);
    }
}
```

В данном случае содержимым ответа сервера фактически будет html-страница, в результате мы получим консольный вывод типа следующего:

GetAsync()МетодыGetAsync()/PostAsync()/PatchAsync()/DeleteAsync()несколько упрощают отправку запроса, так как они заточены под определенный тип запросов и 
в них не надо передавать HttpRequrestMessage. Например, используем методGetAsync(), который отправляет GET-запрос и в качестве параметра принимает адрес ресурса:class Program
{
    static HttpClient httpClient = new HttpClient();
    static async Task Main()
    {
        // получаем ответ
        using HttpResponseMessage response = await httpClient.GetAsync("https://www.google.com");
        // получаем ответ
        string content = await response.Content.ReadAsStringAsync();
        Console.WriteLine(content);
    }
}GetStringAsync / GetByteArrayAsync / GetStreamAsyncВыше была рассмотрена общая механика выполнения Http-запроса. Однако в рассмотренном примере мы по сути получали от сервера (www.google.com) некоторую строку - html-код веб-страницы. Когда нам надо получить строку, 
то гораздо проще выполнить запрос методомGetStringAsync():class Program
{
    static HttpClient httpClient = new HttpClient();

    static async Task Main()
    {
        string content = await httpClient.GetStringAsync("https://www.google.com");
        Console.WriteLine(content);
    }
}Если сервер отправляет двоичные данные, то их можно получить с помощью методаGetByteArrayAsync()class Program
{
    static HttpClient httpClient = new HttpClient();

    static async Task Main()
    {
        byte[] buffer = await httpClient.GetByteArrayAsync("https://www.google.com");
        Console.WriteLine(System.Text.Encoding.UTF8.GetString(buffer));
    }
}И также можно получить поток методомGetStreamAsync()class Program
{
    static HttpClient httpClient = new HttpClient();

    static async Task Main()
    {
        using Stream stream = await httpClient.GetStreamAsync("https://www.google.com");
        StreamReader reader = new StreamReader(stream); 
        string content = await reader.ReadToEndAsync();     // считываем поток в строку
        Console.WriteLine(content);
    }
}

**Источник:** [https://metanit.com/sharp/net/2.2.php](https://metanit.com/sharp/net/2.2.php)

[[Языки программирования/C#/Руководства/Сетевое программирование/Глава 2. Протокол HTTP/Создание HttpClient|Назад]] | [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 2. Протокол HTTP|Протокол HTTP]] | [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 2. Протокол HTTP/Получение данных в формате JSON|Вперёд]]
