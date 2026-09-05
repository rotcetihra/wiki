# Отправка файлов и класс MultipartFormDataContent

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Руководства|Руководства]] / [[Языки программирования/C#/Руководства/Сетевое программирование|Сетевое программирование]] / [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 2. Протокол HTTP|Протокол HTTP]] / Отправка файлов и класс MultipartFormDataContent

[[Языки программирования/C#/Руководства/Сетевое программирование/Глава 2. Протокол HTTP/Отправка потоков и массива байтов|Назад]] | [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 2. Протокол HTTP|Протокол HTTP]] | [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 2. Протокол HTTP/Отправка и получение куки с HttpClient|Вперёд]]

**Дата написания:** 05.09.2026

## Отправка файлов и класс MultipartFormDataContent

Для отправки файлов на сервер HttpClient использует класс  System.Net.Http.MultipartFormDataContent . 
Фактически этот класс выступает в качестве контейнера объектов HttpContent. А для добавления элементов в MultipartFormDataContent применяется метод  Add()

```csharp
public void Add(HttpContent content, string name, string fileName);
```

Первый параметр - отправляемое содержимое (это может быть как файлы, так и любые другие данные). Второй параметр -  `name`  определяет название данных в запросе, по которому мы можем 
получить файл на сервере. Третий параметр -  `fileName`  устанавливает имя файла.

### Загрузка одного файла

Для тестирования загрузки файла определим приложение ASP.NET Core со следующим кодом:

```csharp
var builder = WebApplication.CreateBuilder();
var app = builder.Build();

app.MapPost("/upload", async (HttpContext context) =>
{
    // получем коллецию загруженных файлов
    IFormFileCollection files = context.Request.Form.Files;
    // путь к папке, где будут храниться файлы
    var uploadPath = $"{Directory.GetCurrentDirectory()}/uploads";
    // создаем папку для хранения файлов
    Directory.CreateDirectory(uploadPath);

    // пробегаемся по всем файлам
    foreach (var file in files)
    {
        // формируем путь к файлу в папке uploads
        string fullPath = $"{uploadPath}/{file.FileName}";

        // сохраняем файл в папку uploads
        using (var fileStream = new FileStream(fullPath, FileMode.Create))
        {
            await file.CopyToAsync(fileStream);
        }
    }
    await context.Response.WriteAsync("Файлы успешно загружены");
});

app.Run();
```

Здесь метод  `app.MapPost()`  определяет конечную точку, которая обрабатывает запросы по пути "\upload". В обработчике конечной точки в качестве параметра получаем 
контекст запроса HttpContext и через него с помощью свойства  `context.Request.Form.Files`  получаем коллекцию загруженных файлов. Далее пробегаемся по этой коллекции и сохраняем все данные 
в проекте в папке "upoload" (если ее нет, она создается).

Теперь определим клиент:

```csharp
using System.Net.Http.Headers;
class Program
{
    static HttpClient httpClient = new HttpClient();
    static async Task Main()
    {
        // адрес сервера
        var serverAddress = "https://localhost:7094/upload";
        // пусть к файлу
        var filePath = @"D:\forest.jpg";

        // создаем MultipartFormDataContent
        using var multipartFormContent = new MultipartFormDataContent();
        // Загружаем отправляемый файл
        var fileStreamContent = new StreamContent(File.OpenRead(filePath));
        // Устанавливаем заголовок Content-Type
        fileStreamContent.Headers.ContentType = new MediaTypeHeaderValue("image/jpeg");
        // Добавляем загруженный файл в MultipartFormDataContent
        multipartFormContent.Add(fileStreamContent, name: "file", fileName: "forest.jpg");

        // Отправляем файл
        using var response = await httpClient.PostAsync(serverAddress, multipartFormContent);
        // считываем ответ
        var responseText = await response.Content.ReadAsStringAsync();
        Console.WriteLine(responseText);
    }
}
```

Итак, в моем случае веб-приложение запущено по адресу ""https://localhost:7094/", поэтому для обращения к конечной точке, которая получает файлы, я использую адрес ""https://localhost:7094/upload". 
Также в моем случае загружается файл "D:\forest.jpg".

Для отправки создаем MultipartFormDataContent

```csharp
using var multipartFormContent = new MultipartFormDataContent();
```

Обратите внимание на конструкцию using, которая позволит закрыть все связанные с объектом потоки, использованные при отправке файла.

Затем создаем объект  StreamContent , который получает содержимое файла в виде файлового потока:

```csharp
var fileStreamContent = new StreamContent(File.OpenRead(filePath));
```

Устанавливаем mime-тип, который соответствует загружаемому файлу:

```csharp
fileStreamContent.Headers.ContentType = new MediaTypeHeaderValue("image/jpeg");
```

Далее добавляем этот объект в MultipartFormDataContent:

```csharp
multipartFormContent.Add(fileStreamContent, name: "file", fileName: "forest.jpg");
```

В конце отправляем файл и получаем ответ:

```csharp
using var response = await httpClient.PostAsync(serverAddress, multipartFormContent);
var responseText = await response.Content.ReadAsStringAsync();
```

Стоит отметить, что нам необязательно применять для отправки файла именно StreamContent. Например, можно считать данные файла в массив байтов и отправить его, 
используя класс  ByteArrayContent :

```csharp
using System.Net.Http.Headers;
class Program
{
    static HttpClient httpClient = new HttpClient();
    static async Task Main()
    {
        // адрес сервера
        var serverAddress = "https://localhost:7094/upload";
        // пусть к файлу
        var filePath = @"D:\forest.jpg";

        // создаем MultipartFormDataContent
        using var multipartFormContent = new MultipartFormDataContent();
        // считываем данные файла в массив байтов
        byte[] fileToBytes = await File.ReadAllBytesAsync(filePath);
        // формируем отправляемое содержимое
        var content = new ByteArrayContent(fileToBytes);
        // Устанавливаем заголовок Content-Type
        content.Headers.ContentType = new MediaTypeHeaderValue("image/jpeg");
        // Добавляем загруженный файл в MultipartFormDataContent
        multipartFormContent.Add(content, name: "file", fileName: "forest5.jpg");

        // Отправляем файл
        using var response = await httpClient.PostAsync(serverAddress, multipartFormContent);
        // считываем ответ
        var responseText = await response.Content.ReadAsStringAsync();
        Console.WriteLine(responseText);
    }
}
```

Код сервера при этом остается тем же.

### Множественная отправка файлов

Подобным образом можно отправлять и большее количество файлов. Например:

```csharp
using System.Net.Http.Headers;
class Program
{
    static HttpClient httpClient = new HttpClient();
    static async Task Main()
    {
        // адрес для отправки 
        var serverAddress = "https://localhost:7094/upload";
        // пути к файлам
        var files = new string[] { "D:\forest.jpg", "D:\cats.jpg" };

        using var multipartFormContent = new MultipartFormDataContent();
        // в цикле добавляем все файлы в MultipartFormDataContent
        foreach (var file in files)
        {
            // получаем краткое имя файла
            var fileName = Path.GetFileName(file);
            var fileStreamContent = new StreamContent(File.OpenRead(file));
            fileStreamContent.Headers.ContentType = new MediaTypeHeaderValue("image/jpeg");
            multipartFormContent.Add(fileStreamContent, name: "files", fileName: fileName);
        }
        // Отправляем файлы
        using var response = await httpClient.PostAsync(serverAddress, multipartFormContent);
        // считываем ответ
        var responseText = await response.Content.ReadAsStringAsync();
        Console.WriteLine(responseText);
    }
}
```

### Отправка смешанного содержимого

Плюсом MultipartFormDataContent состоит в том, что он позволяет отправить смешенного содержимое, не только файлы. Например, пусть у нас веб-приложение ASP.NET получает некоторые данные:

```csharp
using Microsoft.AspNetCore.Mvc;

var builder = WebApplication.CreateBuilder();
var app = builder.Build();

app.MapPost("/upload", async (HttpContext context) =>
{
    var form = context.Request.Form;
    // получаем отдельные данные
    string? username = form["username"];
    string? email = form["email"];

    // получаем коллецию загруженных файлов
    IFormFileCollection files = form.Files;
    // путь к папке, где будут храниться файлы
    var uploadPath = $"{Directory.GetCurrentDirectory()}/uploads";
    // создаем папку для хранения файлов
    Directory.CreateDirectory(uploadPath);

    foreach (var file in files)
    {
        // путь к папке uploads
        string fullPath = $"{uploadPath}/{file.FileName}";

        // сохраняем файл в папку uploads
        using (var fileStream = new FileStream(fullPath, FileMode.Create))
        {
            await file.CopyToAsync(fileStream);
        }
    }
    return $"Данные пользователя {username} ({email}) успешно загружены";
});

app.Run();
```

На сервере теперь из коллекции  `context.Request.Form`  получаем данные с ключом "username" и "email" (условные имя и электронный адрес пользователя).

На клиенте определим следующий код:

```csharp
using System.Net.Http.Headers;
class Program
{
    static HttpClient httpClient = new HttpClient();
    static async Task Main()
    {
        using var multipartFormContent = new MultipartFormDataContent();

        // добавляем обычные данные
        multipartFormContent.Add(new StringContent("Tom"), name: "username");
        multipartFormContent.Add(new StringContent("tom@localhost.com"), name: "email");

        // добавляем файл
        var fileStreamContent = new StreamContent(File.OpenRead("D:\logo.jpg"));
        fileStreamContent.Headers.ContentType = new MediaTypeHeaderValue("image/jpeg");
        multipartFormContent.Add(fileStreamContent, name: "files", fileName: "logo.jpg");
         
        // Отправляем данные
        using var response = await httpClient.PostAsync("https://localhost:7094/upload", multipartFormContent);
        // считываем ответ
        var responseText = await response.Content.ReadAsStringAsync();
        Console.WriteLine(responseText);
    }
}
```

В данном случае кроме файла в MultipartFormDataContent добавляется два объекта StringContent, который представляет обычную строку. Ключи обоих объектов соответствуют тем, которые используются 
для получения данных на сервере - "username" и "email".

В результате выполнения консоль нам выведет:

```csharp
Данные пользователя Tom (tom@localhost.com) успешно загружены
```

А на сервере в папке uploads появится еще один файл - logo.jpg.

**Источник:** [https://metanit.com/sharp/net/2.10.php](https://metanit.com/sharp/net/2.10.php)

[[Языки программирования/C#/Руководства/Сетевое программирование/Глава 2. Протокол HTTP/Отправка потоков и массива байтов|Назад]] | [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 2. Протокол HTTP|Протокол HTTP]] | [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 2. Протокол HTTP/Отправка и получение куки с HttpClient|Вперёд]]
