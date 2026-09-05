# Отправка и получение куки с HttpClient

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Руководства|Руководства]] / [[Языки программирования/C#/Руководства/Сетевое программирование|Сетевое программирование]] / [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 2. Протокол HTTP|Протокол HTTP]] / Отправка и получение куки с HttpClient

[[Языки программирования/C#/Руководства/Сетевое программирование/Глава 2. Протокол HTTP/Отправка файлов и класс MultipartFormDataContent|Назад]] | [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 2. Протокол HTTP|Протокол HTTP]] | [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 2. Протокол HTTP/HttpListener. HTTP-сервер|Вперёд]]

**Дата написания:** 05.09.2026

## Отправка и получение куки с HttpClient

Вне зависимости от того, собираемся мы получить или отправить куки, нам придется иметь дело с двумя классами: Cookie и CookieContainer. Поэтому сначала вкратце рассмотрим эти типы.

### Cookie

Класс  Cookie  собственно представляет куки в .NET. Данный тип имеет четыре конструктора:

```csharp
public Cookie ();
public Cookie (string name, string? value);
public Cookie (string name, string? value, string? path);
public Cookie (string name, string? value, string? path, string? domain);
```

Параметры конструкторов:

- name : название куки
- value : значение куки
- path : путь (по умолчанию "/", то есть корень веб-приложения)
- domain : домен, для которого созданы данные куки

Для установки или получения значенний кук можно использовать ряд свойств данного класса:

- Comment : возвращает или задает комментарий, который сервер может добавлять в Cookie
- CommentUri : возвращает или задает комментарий для URI, который сервер может предоставлять с Cookie
- Discard : возвращает или задает флаг сброса, задаваемый сервером
- Domain : возвращает или задает URI, для которого Cookie является допустимым
- Expired : возвращает или задает текущее состояние Cookie
- Expires : возвращает или задает для Cookie дату и время окончания действия в виде DateTime
- HttpOnly : определяет, может ли получить доступ к файлу cookie скрипт страницы или другое активное содержимое
- Name : возвращает или задает имя Cookie
- Path : возвращает или задает идентификаторы URI, к которым применяется Cookie
- Port : возвращает или задает список TCP-портов, к которым применяется Cookie
- Secure : возвращает или задает уровень безопасности Cookie
- TimeStamp : возвращает время выпуска файла cookie в виде DateTime
- Value : возвращает или задает Value для объекта Cookie
- Version : возвращает или задает версию поддержки запоминания состояния HTTP, которой соответствует файл cookie

Например, создание куки и получение их свойств:

```csharp
Cookie nameCookie = new Cookie("name", "Tom");
Console.WriteLine(nameCookie.Name);    // name
Console.WriteLine(nameCookie.Value);    // Tom
```

### CookieContainer

Класс  CookieContainer  представляет контейнер куки, то есть по сути некоторую надстройку над набором объектов Cookie. Для конфигурации контейнера класс 
определяет несколько свойств:

- Capacity : получает или задает количество экземпляров Cookie, которое может храниться в CookieContainer. Значение по умолчанию - 300
- Count : возвращает количество экземпляров Cookie, которые имеются в текущий момент в CookieContainer.
- MaxCookieSize : представляет максимально допустимую длину Cookie в байтах. Значение по умолчанию - 4096 байт
- PerDomainCapacity : получает или задает количество экземпляров Cookie, которое может храниться в CookieContainer для каждого домена. 
Значение по умолчанию - 20

Для создания объекта CookieContainer применяются три конструктора:

```csharp
public CookieContainer (int capacity, int perDomainCapacity, int maxCookieSize);
public CookieContainer (int capacity);
public CookieContainer ();
```

Параметры конструкторов применяются для установки соответствующих свойств CookieContainer.

Для управления куками CookieContainer предоставляет ряд методов. Основные из них:

- Add(Cookie) : добавляет объект Cookie в CookieContainer. Метод использует свойство Domen из объекта Cookie для определения Uri, для которого добавляется Cookie.
- Add(Uri, Cookie) : добавляет экземпляр Cookie в CookieContainer для определенного URI.
- GetAllCookies() : возвращает объект CookieCollection , который содержит все объекты Cookie контейнера.
- GetCookieHeader(Uri) : возвращает заголовок HTTP-cookie, который включает данные всех объектов Cookie, связанных с определенным URI.
- GetCookies(Uri) : возвращает коллекцию CookieCollection с объектами Cookie, которые связанны с указанным URI.
- SetCookies(Uri, String) : добавляет объекты Cookie для определенного URI.

Например, добавление кук:

```csharp
Uri uri = new Uri("http://metanit.com");
Cookie nameCookie = new Cookie("name", "Tom");
Cookie emailCookie = new Cookie("email", "tom@localhost.com");
CookieContainer cookieContainer = new CookieContainer();
cookieContainer.Add(uri, nameCookie); // добавляем куки nameCookie для uri http://metanit.com
cookieContainer.Add(uri, emailCookie); // добавляем куки emailCookie для uri http://metanit.com
```

в качестве альтернативы можно установки куки в помощью SetCookies, передав заголовок куки(то есть строку в формате "имя_куки:значение_куки"):

```csharp
Uri uri = new Uri("http://metanit.com");
CookieContainer cookieContainer = new CookieContainer();

// установка кук
cookieContainer.SetCookies(uri, "name=Bob");
cookieContainer.SetCookies(uri, "email=bob@localhost.com");
```

Получение кук из контейнера:

```csharp
// получаем все куки
var allCookies = cookieContainer.GetAllCookies();
foreach (Cookie cookie in allCookies)
{
    Console.WriteLine($"{cookie.Name} : {cookie.Value}");
}

// получаем куки только для uri http://metanit.com
var uriCookies = cookieContainer.GetCookies(uri);
foreach (Cookie cookie in uriCookies)
{
    Console.WriteLine($"{cookie.Name} : {cookie.Value}");
}
```

Получение заголовка кук:

```csharp
var cookieHeader = cookieContainer.GetCookieHeader(uri);
Console.WriteLine(cookieHeader);    // name=Tom; email=tom@localhost.com
```

Общий заголовок кук по сути представляет строку, в которой все куки отделены друг от друга точкой с запятой.

Теперь рассмотрим, как все это использовать и отправке и получении кук в http-запросе с помощью HttpClient.

### Получение куки

Для тестирования получения куки с помощью HttpClient определим следующее веб-приложение ASP.NET Core:

```csharp
var builder = WebApplication.CreateBuilder();
var app = builder.Build();

app.MapGet("/", (HttpContext context) =>
{
    // устанавливаем куки
    context.Response.Cookies.Append("name", "Tom");
    context.Response.Cookies.Append("email", "tom@localhost.com");
});

app.Run();
```

В данном случае с помощью метода  `context.Response.Cookies.Append()`  в ответ клиенту добавляются две куки: name и email.

Теперь рассмотрим, как получить эти данные на клиенте.

#### Получение кук из запроса через заголовок Set-Cookie

Второй способ состоит в извлечении куки из запроса по заголовку "Set-Cookie":

```csharp
using System.Net;

class Program
{
    static HttpClient httpClient = new HttpClient();
    static async Task Main()
    {
        // адрес сервера
        Uri uri = new Uri("https://localhost:7094/");

        using var response = await httpClient.GetAsync(uri);
        CookieContainer cookies = new CookieContainer();
        // получаем из запроса все элементы с заголовком Set-Cookie
        foreach (var cookieHeader in response.Headers.GetValues("Set-Cookie"))
            // добавляем заголовки кук в CookieContainer
            cookies.SetCookies(uri, cookieHeader);

        // получение всех куки
        foreach (Cookie cookie in cookies.GetCookies(uri))
            Console.WriteLine($"{cookie.Name}: {cookie.Value}");

        // получение отдельных куки
        // получаем куку "email"
        Cookie? email = cookies.GetCookies(uri).FirstOrDefault(c => c.Name == "email");
        Console.WriteLine($"Электронный адрес: {email?.Value}");
    }
}
```

В данном случае после выполнения запроса получаем по ключу "Set-Cookie" все заголовки и добавляем их в CookieContainer с помощью  `SetCookies()` :

```csharp
CookieContainer cookies = new CookieContainer();
foreach (var cookieHeader in response.Headers.GetValues("Set-Cookie"))
    cookies.SetCookies(uri, cookieHeader);
```

Затем с помощью вызова  `cookies.GetCookies(uri)`  получаем куки. Консольный вывод программы:

```csharp
name: Tom
email: tom%40localhost.com
Электронный адрес: tom%40localhost.com
```

#### Применение HttpClientHandler

Объект HttpClient инициализируется определенным обработчиком. По умолчанию это объект типа  HttpClientHandler . Этот тип имеет свойство  CookieContainer , 
которое принимает объект типа  CookieContainer  и представляет контейнер куки для данного HttpClientHandler.

Если у объекта HttpClientHandler свойство  UseCookies  равно  `true`  (а это значение по умолчанию), 
то свойство  `CookieContainer`  будет использоваться для сохранения куки с сервера или их отправки на сервер.

Например, получим от веб-приложения куки "name" и "email":

```csharp
using System.Net;

class Program
{
    static HttpClient? httpClient;
    static async Task Main()
    {
        // адрес сервера
        Uri uri = new Uri("https://localhost:7094/");
        var cookies = new CookieContainer();
        using var handler = new HttpClientHandler();
        handler.CookieContainer = cookies;

        httpClient = new HttpClient(handler);

        using var response = await httpClient.GetAsync(uri);
        // получение всех куки
        foreach (Cookie cookie in cookies.GetCookies(uri))
            Console.WriteLine($"{cookie.Name}: {cookie.Value}");
        // получение отдельных куки
        // получаем куку "email"
        Cookie? email = cookies.GetCookies(uri).FirstOrDefault(c=>c.Name== "email");
        Console.WriteLine($"Электронный адрес: {email?.Value}");
    }
}
```

Вначале создается контейнер куки - CookieContainer и объект HttpClientHandler. Затем устанавливаем для HttpClientHandler контейнер куки и создаем HttpClient, который использует данный объект HttpClientHandler.

После выполнения запроса CookieContainer будет содержать куки с сервера. Остальной процесс получения тот же, что и в предыдущем примере.

### Отправка кук

Для текста отправки кук с клиента на сервер определим следующее веб-приложение ASP.NET Core:

```csharp
var builder = WebApplication.CreateBuilder();
var app = builder.Build();

app.MapGet("/", (HttpContext context) =>
{
    // получаем куки
    context.Request.Cookies.TryGetValue("name", out string? name);
    context.Request.Cookies.TryGetValue("email", out string? email);

    return $"Name: {name}   Email:{email}";
});

app.Run();
```

Здесь с помощью метода  `context.Request.Cookies.TryGetValue()`  получаем значения двух кук - name и email и из значения в виде одной строки отправляем обратно клиенту.

Самый простой способ представляет установка заголовка "cookie" при отправке запроса. Например:

```csharp
using System.Net;

class Program
{
    static HttpClient httpClient = new HttpClient();
    static async Task Main()
    {
        // адрес сервера
        Uri uri = new Uri("https://localhost:7094/");

        CookieContainer cookies = new CookieContainer();
        // устанавливаем куки name и email
        cookies.Add(uri, new Cookie("name", "Bob"));
        cookies.Add(uri, new Cookie("email", "bob@localhost.com"));
        // устанавливаем заголовок cookie
        httpClient.DefaultRequestHeaders.Add("cookie", cookies.GetCookieHeader(uri));

        using var response = await httpClient.GetAsync(uri);
        string responseText = await response.Content.ReadAsStringAsync();
        Console.WriteLine(responseText);
    }
}
```

Здесь добавляем в контейнер CookieContainer две куки: name и email. А с помощью метода  `cookies.GetCookieHeader(uri)`  получаем строковое представление заголовка, который включает все данные кук и 
передаем его заголовку "cookie".

Консольный вывод программы:

```csharp
Name: Bob   Email:bob@localhost.com
```

**Источник:** [https://metanit.com/sharp/net/2.12.php](https://metanit.com/sharp/net/2.12.php)

[[Языки программирования/C#/Руководства/Сетевое программирование/Глава 2. Протокол HTTP/Отправка файлов и класс MultipartFormDataContent|Назад]] | [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 2. Протокол HTTP|Протокол HTTP]] | [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 2. Протокол HTTP/HttpListener. HTTP-сервер|Вперёд]]
