# Отправка json с помощью HttpClient

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Руководства|Руководства]] / [[Языки программирования/C#/Руководства/Сетевое программирование|Сетевое программирование]] / [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 2. Протокол HTTP|Протокол HTTP]] / Отправка json с помощью HttpClient

[[Языки программирования/C#/Руководства/Сетевое программирование/Глава 2. Протокол HTTP/Отправка данных в запросе|Назад]] | [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 2. Протокол HTTP|Протокол HTTP]] | [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 2. Протокол HTTP/Взаимодействие HttpClient с Web API|Вперёд]]

**Дата написания:** 05.09.2026

## Отправка json с помощью HttpClient

Для отправки данных в формате JSON с помощью HttpClient проще всего использовать класс  JsonContent , унаследованный от HttpContent.

Тип JsonContent не имеет публичного конструктора, а для создания его объекта применяется статический метод  Create() , который типизируется типом отправляемых данных и 
который в качестве обязательного параметра получает отправляемый объект:

```csharp
JsonContent content = JsonContent.Create(отправляемый_объект);
```

При этом мы можем передать в метод  `JsonContent.Create()`  обычный объект C#, который будет автоматически сериализоваться в JSON.

Для тестирования определим следующее веб-приложение ASP.NET Core:

```csharp
var builder = WebApplication.CreateBuilder();
var app = builder.Build();

app.MapPost("/create", (Person person) =>
{
    // устанавливает id у объекта Person
    person.Id = Guid.NewGuid().ToString();
    // отправляем обратно объект Person
    return person;
});

app.Run();
class Person
{
    public string Id { get; set; } = "";
    public string Name { get; set; } = "";
    public int Age { get; set; }
}
```

Здесь метод  `app.MapPost()`  обрабатывает запросы по пути "/create. В частности, в обработчик конечной точки из запроса получает объект Person, устанавливает у него свойство Id  и отправляет назад клиенту.

Используем тип  JsonContent  для отправки данных:

```csharp
using System.Net.Http.Json;

class Program
{
    static HttpClient httpClient = new HttpClient();
    static async Task Main()
    {
        // отправляемый объект 
        Person tom = new Person { Name = "Tom", Age = 38 };
        // создаем JsonContent
        JsonContent content = JsonContent.Create(tom);
        // отправляем запрос
        using var response = await httpClient.PostAsync("https://localhost:7094/create", content);
        Person? person = await response.Content.ReadFromJsonAsync<Person>();
        Console.WriteLine($"{person?.Id} - {person?.Name}");
    }
}
class Person
{
    public string Id { get; set; } = "";
    public string Name { get; set; } = "";
    public int Age { get; set; }
}
```

В данном случае отправляется объект Person, а метод Create неявно типизируется типом Person.

Ответ от сервера считываем с помощью метода  `response.Content.ReadFromJsonAsync()` , который возвратит нам тот объект Person, только с установленным на сервере свойством Id.

#### PostAsJsonAsync

Для упрощения отправки JSON для типа HttpClient в пространстве имен  `System.Net.Http.Json`  определены специальные методы расщирения:

- PostAsJsonAsync()
- PutAsJsonAsync()
- PatchAsJsonAsync()

Все эти методы автоматически сериализуют отправляемые данные в JSON. Они типизируются типом, данные которого надо отправить и принимают как минимум два параметра: адрес ресурса и 
отправляемый объект:

```csharp
Task<HttpResponseMessage> PostAsync<T> (string? requestUri, T content);
Task<HttpResponseMessage> PutAsync<T> (string? requestUri, T content);
Task<HttpResponseMessage> PatchAsync<T> (string? requestUri, T content);
```

Так, мы можем переписать программу по отправке данных на сервер следующим образом:

```csharp
using System.Net.Http.Json;

class Program
{
    static HttpClient httpClient = new HttpClient();
    static async Task Main()
    {
        // отправляемый объект 
        Person tom = new Person { Name = "Tom", Age = 38 };
        // отправляем запрос
        using var response = await httpClient.PostAsJsonAsync("https://localhost:7094/create", tom);
        Person? person = await response.Content.ReadFromJsonAsync<Person>();
        Console.WriteLine($"{person?.Id} - {person?.Name}");
    }
}
class Person
{
    public string Id { get; set; } = "";
    public string Name { get; set; } = "";
    public int Age { get; set; }
}
```

**Источник:** [https://metanit.com/sharp/net/2.6.php](https://metanit.com/sharp/net/2.6.php)

[[Языки программирования/C#/Руководства/Сетевое программирование/Глава 2. Протокол HTTP/Отправка данных в запросе|Назад]] | [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 2. Протокол HTTP|Протокол HTTP]] | [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 2. Протокол HTTP/Взаимодействие HttpClient с Web API|Вперёд]]
