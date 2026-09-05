# Взаимодействие HttpClient с Web API

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Руководства|Руководства]] / [[Языки программирования/C#/Руководства/Сетевое программирование|Сетевое программирование]] / [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 2. Протокол HTTP|Протокол HTTP]] / Взаимодействие HttpClient с Web API

[[Языки программирования/C#/Руководства/Сетевое программирование/Глава 2. Протокол HTTP/Отправка json с помощью HttpClient|Назад]] | [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 2. Протокол HTTP|Протокол HTTP]] | [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 2. Протокол HTTP/Отправка форм и класс FormUrlEncodedContent|Вперёд]]

**Дата написания:** 05.09.2026

## Взаимодействие HttpClient с Web API

Рассмотрим взаимодействие HttpClient с веб-приложением, которое реализует Web API на примере простейшего веб-приложения ASP.NET Core

### Создание сервера

Сначала определим проект веб-приложения. Для этого создадим проект по типу  ASP.NET Core Empty :

К примеру, в моем случае проект называетсяHttpClientTestApp. Откроем в этом проекте в файлProgram.csи определим в нем следующий код:int id = 1; // для генерации id объектов
// начальные данные
List<Person> users = new List<Person>
{
    new() { Id = id++, Name = "Tom", Age = 37 },
    new() { Id = id++, Name = "Bob", Age = 41 },
    new() { Id = id++, Name = "Sam", Age = 24 }
};

var builder = WebApplication.CreateBuilder();
var app = builder.Build();

app.MapGet("/api/users", () => users);

app.MapGet("/api/users/{id}", (int id) =>
{
    // получаем пользователя по id
    Person? user = users.FirstOrDefault(u => u.Id == id);
    // если не найден, отправляем статусный код и сообщение об ошибке
    if (user == null) return Results.NotFound(new { message = "Пользователь не найден" });

    // если пользователь найден, отправляем его
    return Results.Json(user);
});

app.MapDelete("/api/users/{id}", (int id) =>
{
    // получаем пользователя по id
    Person? user = users.FirstOrDefault(u => u.Id == id);

    // если не найден, отправляем статусный код и сообщение об ошибке
    if (user == null) return Results.NotFound(new { message = "Пользователь не найден" });

    // если пользователь найден, удаляем его
    users.Remove(user);
    return Results.Json(user);
});

app.MapPost("/api/users", (Person user) =>
{

    // устанавливаем id для нового пользователя
    user.Id = id++;
    // добавляем пользователя в список
    users.Add(user);
    return user;
});

app.MapPut("/api/users", (Person userData) =>
{

    // получаем пользователя по id
    var user = users.FirstOrDefault(u => u.Id == userData.Id);
    // если не найден, отправляем статусный код и сообщение об ошибке
    if (user == null) return Results.NotFound(new { message = "Пользователь не найден" });
    // если пользователь найден, изменяем его данные и отправляем обратно клиенту

    user.Age = userData.Age;
    user.Name = userData.Name;
    return Results.Json(user);
});

app.Run();

public class Person
{
    public int Id { get; set; }
    public string Name { get; set; } = "";
    public int Age { get; set; }
}Более подробно создание приложения Web API на ASP.NET рассмотрено в статьеПример приложения Web API на ASP.NET. Сейчас лишь вкратце пройдемся 
по основным момента данного кода. Вначале определяется переменная для генерации id объектов и создается список объектов Person - те данные, с которыми будет работать пользователь::int id = 1;
var users = new List<Person> 
{ 
    new() { Id = id++, Name = "Tom", Age = 37 },
    new() { Id = id++, Name = "Bob", Age = 41 },
    new() { Id = id++, Name = "Sam", Age = 24 }
};При создании нового объекта значение переменной id увеличивается на единицу, поэтому каждый новый объект получает id на единицу больше, чем предыдущий. Для упрошения данные определены в виде обычного списка объектов, но в реальной ситуации обычно подобные данные извлекаются из какой-нибудь базы данных.Затем с помощью методовMapGet/MapPost/MapPut/MapDeleteопределяется набор конечных точек, которые будут обрабатывать разные типы запросов.Вначале добавляется конечная точка, которая обрабатывает запрос типа GET по маршруту "api/users":app.MapGet("/api/users", () => users);Запрос GET предполагает получение объектов, и в данном случае отправляем выше определенный список объектов Person.Когда клиент обращается к приложению для получения одного объекта по id в запрос типа GET по адресу "api/users/{id}", то срабатывает другая конечная точка:app.MapGet("/api/users/{id}", (int id) =>
{
    // получаем пользователя по id
    Person? user = users.FirstOrDefault(u => u.Id == id);
    // если не найден, отправляем статусный код и сообщение об ошибке
    if (user == null)  return Results.NotFound(new { message = "Пользователь не найден" });

    // если пользователь найден, отправляем его
    return Results.Json(user);
});Здесь через параметр id получаем из пути запроса идентификатор объекта Person и по этому идентификатору ищем нужный объект в списке users. 
Если объект по Id не был найден, то возвращаем с помощью методаResults.NotFound()статусный код 404 с некоторым сообщением в формате JSON. 
Если объект найден, то с помощью методаResults.Json()отправляет найденный объект клиенту.При получении запроса типа DELETE по маршруту "/api/users/{id}" срабатывает другая конечная точка:app.MapDelete("/api/users/{id}", (int id) =>
{
    // получаем пользователя по id
    Person? user = users.FirstOrDefault(u => u.Id == id);

    // если не найден, отправляем статусный код и сообщение об ошибке
    if (user == null) return Results.NotFound(new { message = "Пользователь не найден" });

    // если пользователь найден, удаляем его
    users.Remove(user);
    return Results.Json(user);
});Здесь действует аналогичная логика - если объект по Id не найден, отправляет статусный код 404. Если же объект найден, то удаляем его из списка 
и посылаем клиенту.При получении запроса с методом POST по адресу "/api/users" срабатывает следующая конечная точка:app.MapPost("/api/users", (Person user)=>{

    // устанавливаем id для нового пользователя
    user.Id = id++;
    // добавляем пользователя в список
    users.Add(user);
    return user;
});Запрос типа POST предполагает передачу приложению отправляемых данных. Причем мы ожидаем, что клиент отправит данные, которые соответствуют определению типа Person. И поэтому 
инфраструктура ASP.NET Core сможет автоматически собрать из них объект Person. И этот объект мы сможем получить в качестве параметра в обработчике 
конечной точки.После получения данных устанавливаем у нового объекта свойство Id, добавляем его в список users и отправляем обратно клиенту.Если приложению приходит PUT-запрос по адресу "/api/users", то аналогичным образом получаем отправленные клиентом данные в виде объекта Person 
и пытаемся найти подобный объект в списке users. Если объект не найден, отправляем статусный код 404.
Если объект найден, то изменяем его данные и отправляем обратно клиенту:app.MapPut("/api/users", (Person userData) => {

    // получаем пользователя по id
    var user = users.FirstOrDefault(u => u.Id == userData.Id);
    // если не найден, отправляем статусный код и сообщение об ошибке
    if (user == null) return Results.NotFound(new { message = "Пользователь не найден" });
    // если пользователь найден, изменяем его данные и отправляем обратно клиенту
    user.Age = userData.Age;
    user.Name = userData.Name;
    return Results.Json(user);
});Для теста запустим этот проект и обратимся в браузере по адресу "/api/users" для получения списка данных:Таким образом, мы определили простейший API. Теперь посмотрим, как мы можем взаимодействовать с этим кодом с помощью классаHttpClient.Определение клиентаGET-запросПоскольку конечная точка, которая обрабатывает GET-запрос, возвращает список данных в формате JSON, то для его получения у HttpClient удобнее использовать методGetFromJsonAsync():using System.Net.Http.Json;

class Program
{
    static HttpClient httpClient = new HttpClient();
    static async Task Main()
    {
        List<Person>? people = await httpClient.GetFromJsonAsync<List<Person>> ("https://localhost:7094/api/users");
        if (people != null)
        {
            foreach (var person in people)
            {
                Console.WriteLine(person.Name);
            }
        }
    }
}
public class Person
{
    public int Id { get; set; }
    public string Name { get; set; } = "";
    public int Age { get; set; }
}Как видно из предыдущего скриншота, у меня приложение ASP.NET запущено по адресу "https://localhost:7094/", а адресом ресурса является "api/users", соответственно в моем случае для получения 
данных я обращаюсь по адресу "https://localhost:7094/api/users". Полученные данные автоматически десериализуются из JSON в список объектов Person, свойство Name которых затем выводится на консоль:Tom
Bob
SamПолучение одного объектаВ ранее определенном сервере для отправки одного объекта применяется конечная точкаapp.MapGet("/api/users/{id}", (int id) => { ....То есть также надо выполнить get-запрос, только в адресную строку нам надо передать id объекта. И в данном случае мы могли бы использовать тот же методGetFromJsonAsync()int id = 1; // получаем объект с id=1
Person? person = await httpClient.GetFromJsonAsync<Person>($"https://localhost:7094/api/users/{id}");Однако, что если мы отправим id несуществующего объекта. В этом случае объект person будет равен null. Однако сервер в этом случае посылает нам соответствующий статусный код и 
сообщение об ошибке. И было бы неплохо иметь возможность в случае проблемы также использовать эти данные. В этом случае мы можем отправить запрос с помощью методаGetAsync()и 
получить ответ в виде HttpResponseMessage. И в зависимости от статусного кода десериализовать ответ в один из типов данных:using System.Net;
using System.Net.Http.Json;
class Program
{
    static HttpClient httpClient = new HttpClient();
    static async Task Main()
    {
        // id первого объекта 
        int id = 1;
        using var response = await httpClient.GetAsync($"https://localhost:7094/api/users/{id}");
        // если объект на сервере найден, то есть статусный код равен 404
        if (response.StatusCode == HttpStatusCode.NotFound)
        {
            Error? error = await response.Content.ReadFromJsonAsync<Error>();
            Console.WriteLine(error?.Message);
        }
        else if (response.StatusCode == HttpStatusCode.OK)
        {
            // считываем ответ
            Person? person = await response.Content.ReadFromJsonAsync<Person>();
            Console.WriteLine($"{person?.Id} - {person?.Name}");
        }
    }
}
record Error(string Message);
class Person
{
    public int Id { get; set;}
    public string Name { get; set; } = "";
    public int Age { get; set; }
}Добавление данныхДобавление данных на сервере обрабатывается конечной точкойapp.MapPost("/api/users", (Person user) =>То есть нам надо в запросе POST послать данные, которые соответствуют объекту Person. Для отправки данных на HttpClient можно использовать методPostAsync(), либоPostAsJsonAsync(), в который передается адрес ресурса и сами добавляемые данные. Поскольку в данном случае веб-приложение 
ожидает данные в формате JSON, то проще воспользоваться методомPostAsJsonAsync():using System.Net.Http.Json;

class Program
{
    static HttpClient httpClient = new HttpClient();
    static async Task Main()
    {
        // отправляемый объект
        var mike = new Person { Name = "Mike", Age = 31 };
        using var response = await httpClient.PostAsJsonAsync("https://localhost:7094/api/users/", mike);
        // считываем ответ и десериализуем данные в объект Person
        Person? person = await response.Content.ReadFromJsonAsync<Person>();
        Console.WriteLine($"{person?.Id} - {person?.Name}");
    }
}
class Person
{
    public int Id { get; set;}
    public string Name { get; set; } = "";
    public int Age { get; set; }
}Изменение данныхДля изменения данных мы должны отправить данные следующей конечной точке:app.MapPut("/api/users", (Person userData) => { ...Для отправки измененных данных в запросе типа PUT можно использовать методPutAsync(), либоPutAsJsonAsync(), в которые передаются адрес ресурса и сами добавляемые данные. Поскольку в данном случае веб-приложение 
ожидает данные в формате JSON, то проще воспользоваться методомPutAsJsonAsync():using System.Net.Http.Json;

class Program
{
    static HttpClient httpClient = new HttpClient();
    static async Task Main()
    {
        // id изменяемого объекта
        int id = 1;
        // отправляемый объект
        var tom = new Person { Id = id, Name = "Tomas", Age = 38 };
        using var response = await httpClient.PutAsJsonAsync("https://localhost:7094/api/users/", tom);
        if (response.StatusCode == System.Net.HttpStatusCode.NotFound)
        {
            // если возникла ошибка, считываем сообщение об ошибке
            Error? error = await response.Content.ReadFromJsonAsync<Error>();
            Console.WriteLine(error?.Message);
        }
        else if (response.StatusCode == System.Net.HttpStatusCode.OK)
        {
            // десериализуем ответ в объект Person
            Person? person = await response.Content.ReadFromJsonAsync<Person>();
            Console.WriteLine($"{person?.Id} - {person?.Name} ({person?.Age})");
        }
    }
}
record Error(string Message);
class Person
{
    public int Id { get; set;}
    public string Name { get; set; } = "";
    public int Age { get; set; }
}Удаление данныхЗа удаление данных на сервере отвечает конечная точкаapp.MapDelete("/api/users/{id}", (string id) => ..То есть в Delete-запросе нам надо передать id удаляемого объекта. Для этого у HttpClient можно использовать методDeleteFromJsonAsync(), который тиизируется типом удаляемого объекта, 
получает адрес удаляемого ресурса и возвращает удаленный объект:using System.Net.Http.Json;

class Program
{
    static HttpClient httpClient = new HttpClient();
    static async Task Main()
    {
        // id удаляемого объекта
        int id = 1;
        Person? person = await httpClient.DeleteFromJsonAsync<Person>($"https://localhost:7094/api/users/{id}");
        Console.WriteLine($"{person?.Id} - {person?.Name} ({person?.Age})");
    }
}
class Person
{
    public int Id { get; set;}
    public string Name { get; set; } = "";
    public int Age { get; set; }
}Однако если объекта с переданным id не окажется на сервере, веб-приложение возвратит статусный код 404 и сообщение об ошибке. Чтобы отловить эту ситуацию, можно использовать 
методDeleteAsync(), который возвращает объект HttpResponseMessage:using System.Net.Http.Json;

class Program
{
    static HttpClient httpClient = new HttpClient();
    static async Task Main()
    {
        // id удаляемого объекта
        int id = 1;

        using var response = await httpClient.DeleteAsync($"https://localhost:7094/api/users/{id}");
        if (response.StatusCode == System.Net.HttpStatusCode.NotFound)
        {
            // если возникла ошибка, считываем сообщение об ошибке
            Error? error = await response.Content.ReadFromJsonAsync<Error>();
            Console.WriteLine(error?.Message);
        }
        else if (response.StatusCode == System.Net.HttpStatusCode.OK)
        {
            // десериализуем ответ в объект Person
            Person? person = await response.Content.ReadFromJsonAsync<Person>();
            Console.WriteLine($"{person?.Id} - {person?.Name} ({person?.Age})");
        }
    }
}
record Error(string Message);
class Person
{
    public int Id { get; set;}
    public string Name { get; set; } = "";
    public int Age { get; set; }
}

**Источник:** [https://metanit.com/sharp/net/2.7.php](https://metanit.com/sharp/net/2.7.php)

[[Языки программирования/C#/Руководства/Сетевое программирование/Глава 2. Протокол HTTP/Отправка json с помощью HttpClient|Назад]] | [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 2. Протокол HTTP|Протокол HTTP]] | [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 2. Протокол HTTP/Отправка форм и класс FormUrlEncodedContent|Вперёд]]
