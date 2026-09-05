# Отправка форм и класс FormUrlEncodedContent

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Руководства|Руководства]] / [[Языки программирования/C#/Руководства/Сетевое программирование|Сетевое программирование]] / [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 2. Протокол HTTP|Протокол HTTP]] / Отправка форм и класс FormUrlEncodedContent

[[Языки программирования/C#/Руководства/Сетевое программирование/Глава 2. Протокол HTTP/Взаимодействие HttpClient с Web API|Назад]] | [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 2. Протокол HTTP|Протокол HTTP]] | [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 2. Протокол HTTP/Отправка потоков и массива байтов|Вперёд]]

**Дата написания:** 05.09.2026

## Отправка форм и класс FormUrlEncodedContent

Для отправки данных формы с помощью HttpClient применяется класс  FormUrlEncodedContent . Он имеет один конструктор, который 
в качестве параметра принимает объект  `IEnumerable<KeyValuePair<string, string>>` , то есть некоторый набор пар ключ-значение.

Для тестирования определим следующее веб-приложение ASP.NET Core:

```csharp
var builder = WebApplication.CreateBuilder();
var app = builder.Build();

app.MapPost("/data", async(HttpContext httpContext) =>
{
    // получаем данные формы
    var form = httpContext.Request.Form; 
    string? name = form["name"];
    string? email = form["email"];
    string? age = form["age"];
    await httpContext.Response.WriteAsync($"Name: {name}   Email:{email}    Age: {age}");
});

app.Run();
```

Здесь с помощью метода  `app.MapPost()`  определена одна конечная точка, которая обрабатывает POST-запросы по адресу "/data"/. В обработчике конечной точки 
с помощью контекста запроса HttpContext через свойство  `httpContext.Request.Form`  получаем отправленную форму и затем по определенным ключам извлекаем 
отправленные значения. В данном случае мы предполагаем, что клиент отправляет три значения с ключами "name", "email" и "age". И в конце отправляем эти данные одной строкой обратно клиенту.

В качестве клиента будет выступать следующее консольное приложение:

```csharp
class Program
{
    static HttpClient httpClient = new HttpClient();
    static async Task Main()
    {
        // данные для отправки в виде объекта IEnumerable<KeyValuePair<string, string>>
        Dictionary<string, string> data = new Dictionary<string, string>
        {
            ["name"]= "Tom",
            ["email"]= "tom@localhost.com",
            ["age"] = "38"
        };
        // создаем объект HttpContent
        HttpContent contentForm = new FormUrlEncodedContent(data);
        // отправляем запрос
        using var response = await httpClient.PostAsync("https://localhost:7094/data", contentForm);
        // получаем ответ
        string responseText = await response.Content.ReadAsStringAsync();
        Console.WriteLine(responseText);
    }
}
```

Отправляемые данные должны представлять тип  `IEnumerable<KeyValuePair<string, string>>` , и в качестве такового мы можем использовать стандартный словарь, 
где ключи и значения представляют строки. И в данном случае определяется подобный словарь, в который добавляются три элемента с ключами "name", "email" и "age", 
которые будут использоваться на сервере для извлечения данных.

В результате выполнения программы на консоли мы лицезреем ответ сервера, который содержит отправленные данные:

```csharp
Name: Tom   Email:tom@localhost.com    Age: 38
```

**Источник:** [https://metanit.com/sharp/net/2.8.php](https://metanit.com/sharp/net/2.8.php)

[[Языки программирования/C#/Руководства/Сетевое программирование/Глава 2. Протокол HTTP/Взаимодействие HttpClient с Web API|Назад]] | [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 2. Протокол HTTP|Протокол HTTP]] | [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 2. Протокол HTTP/Отправка потоков и массива байтов|Вперёд]]
