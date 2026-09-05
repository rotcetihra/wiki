# Взаимодействие приложения Blazor с Web API

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по Blazor|Руководство по Blazor]] / [[Языки программирования/C#/Веб-разработка/Руководство по Blazor/Глава 5. Отправка http-запросов|Глава 5. Отправка http-запросов]] / Взаимодействие приложения Blazor с Web API

[[Языки программирования/C#/Веб-разработка/Руководство по Blazor/Глава 5. Отправка http-запросов/HttpClient в проекте Blazor WebAssembly|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по Blazor/Глава 5. Отправка http-запросов|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по Blazor/Глава 6. Дополнительные статьи/Конфигурация|Вперёд]]

**Дата написания:** 05.09.2026

## Взаимодействие приложения Blazor с Web API

Последнее обновление: 01.12.2023




-

-

-














Рассмотрим взаимодействие проекта Blazor с простейшим сервисом Web API, при котором приложение на Blazor реализует простейший CRUD.
Для этого определим следующий проект:
![Создание проекта ASP.NET Web API для тестирования приложения Blazor на C#](https://metanit.com./pics/5.8.png)


В файле Program.cs определим следующий код программы:

```

using BlazorApp.Components;

// начальные данные
List<Person> users = [
 new() { Id = Guid.NewGuid().ToString(), Name = "Tom", Age = 37 },
 new() { Id = Guid.NewGuid().ToString(), Name = "Bob", Age = 41 },
 new() { Id = Guid.NewGuid().ToString(), Name = "Sam", Age = 24 }
];

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddRazorComponents()
 .AddInteractiveServerComponents();

builder.Services.AddHttpClient();

var app = builder.Build();

app.UseAntiforgery();

app.MapGet("/api/users", () => users);

app.MapGet("/api/users/{id}", (string id) =>
{
 // получаем пользователя по id
 Person? user = users.FirstOrDefault(u => u.Id == id);
 // если не найден, отправляем статусный код и сообщение об ошибке
 if (user == null) return Results.NotFound("Пользователь не найден");

 // если пользователь найден, отправляем его
 return Results.Json(user);
});

app.MapDelete("/api/users/{id}", (string id) =>
{
 // получаем пользователя по id
 Person? user = users.FirstOrDefault(u => u.Id == id);

 // если не найден, отправляем статусный код и сообщение об ошибке
 if (user == null) return Results.NotFound("Пользователь не найден");

 // если пользователь найден, удаляем его
 users.Remove(user);
 return Results.Json(user);
});

app.MapPost("/api/users", (Person user) => {

 // устанавливаем id для нового пользователя
 user.Id = Guid.NewGuid().ToString();
 // добавляем пользователя в список
 users.Add(user);
 return user;
});

app.MapPut("/api/users", (Person userData) => {

 // получаем пользователя по id
 var user = users.FirstOrDefault(u => u.Id == userData.Id);
 // если не найден, отправляем статусный код и сообщение об ошибке
 if (user == null) return Results.NotFound("Пользователь не найден");
 // если пользователь найден, изменяем его данные и отправляем обратно клиенту

 user.Age = userData.Age;
 user.Name = userData.Name;
 return Results.Json(user);
});

app.MapRazorComponents<App>()
 .AddInteractiveServerRenderMode();

app.Run();


public class Person
{
 public string Id { get; set; } = "";
 public string Name { get; set; } = "";
 public int Age { get; set; }
}

```


Разберем в общих чертах этот код. Вначале создается список объектов Person - те данные, с которыми будет работать пользователь:

```

var users = new List<Person>
{
 new() { Id = Guid.NewGuid().ToString(), Name = "Tom", Age = 37 },
 new() { Id = Guid.NewGuid().ToString(), Name = "Bob", Age = 41 },
 new() { Id = Guid.NewGuid().ToString(), Name = "Sam", Age = 24 }
};

```


Стоит обратить внимание, что каждый объект Person имеет свойство Id, которое в качестве значения получает Guid - уникальный идентификатор, например "2e752824-1657-4c7f-844b-6ec2e168e99c".


Для упрошения данные определены в виде обычного списка объектов, но в реальной ситуации обычно подобные данные извлекаются из какой-нибудь базы данных.


Затем с помощью методов MapGet/MapPost/MapPut/MapDelete определяется набор конечных точек, которые будут обрабатывать разные типы запросов.


Вначале добавляется конечная точка, которая обрабатывает запрос типа GET по маршруту "api/users":

```

app.MapGet("/api/users", () => users);

```


Запрос GET предполагает получение объектов, и в данном случае отправляем выше определенный список объектов Person.


Когда клиент обращается к приложению для получения одного объекта по id в запрос типа GET по адресу "api/users/{id}", то срабатывает другая конечная точка:

```

app.MapGet("/api/users/{id}", (string id) =>
{
 // получаем пользователя по id
 Person? user = users.FirstOrDefault(u => u.Id == id);
 // если не найден, отправляем статусный код и сообщение об ошибке
 if (user == null) return Results.NotFound("Пользователь не найден");

 // если пользователь найден, отправляем его
 return Results.Json(user);
});

```


Здесь через параметр id получаем из пути запроса идентификатор объекта Person и по этому идентификатору ищем нужный объект в списке users.
Если объект по Id не был найден, то возвращаем с помощью метода `Results.NotFound()` статусный код 404 с некоторым сообщением.
Если объект найден, то с помощью метода `Results.Json()` отправляет найденный объект клиенту.


При получении запроса типа DELETE по маршруту "/api/users/{id}" срабатывает другая конечная точка:

```

app.MapDelete("/api/users/{id}", (string id) =>
{
 // получаем пользователя по id
 Person? user = users.FirstOrDefault(u => u.Id == id);

 // если не найден, отправляем статусный код и сообщение об ошибке
 if (user == null) return Results.NotFound("Пользователь не найден");

 // если пользователь найден, удаляем его
 users.Remove(user);
 return Results.Json(user);
});

```


Здесь действует аналогичная логика - если объект по Id не найден, отправляет статусный код 404. Если же объект найден, то удаляем его из списка
и посылаем клиенту.


При получении запроса с методом POST по адресу "/api/users" срабатывает следующая конечная точка:

```

app.MapPost("/api/users", (Person user)=>{

 // устанавливаем id для нового пользователя
 user.Id = Guid.NewGuid().ToString();
 // добавляем пользователя в список
 users.Add(user);
 return user;
});

```


Запрос типа POST предполагает передачу приложению отправляемых данных. Причем мы ожидаем, что клиент отправит данные, которые соответствуют определению типа Person. И поэтому
инфраструктура ASP.NET Core сможет автоматически собрать из них объект Person. И этот объект мы сможем получить в качестве параметра в обработчике
конечной точки.


После получения данных устанавливаем у нового объекта свойство Id, добавляем его в список users и отправляем обратно клиенту.


Если приложению приходит PUT-запрос по адресу "/api/users", то аналогичным образом получаем отправленные клиентом данные в виде объекта Person
и пытаемся найти подобный объект в списке users. Если объект не найден, отправляем статусный код 404.
Если объект найден, то изменяем его данные и отправляем обратно клиенту:

```

app.MapPut("/api/users", (Person userData) => {

 // получаем пользователя по id
 var user = users.FirstOrDefault(u => u.Id == userData.Id);
 // если не найден, отправляем статусный код и сообщение об ошибке
 if (user == null) return Results.NotFound("Пользователь не найден");
 // если пользователь найден, изменяем его данные и отправляем обратно клиенту
 user.Age = userData.Age;
 user.Name = userData.Name;
 return Results.Json(user);
});

```


Таким образом, мы определили простейший API. В качестве клиента в проекте в папке Components определен компонент App:

```

@page "/"

<!DOCTYPE html>
<html>
<head>
 <title>METANIT.COM</title>
 <meta charset="utf-8" />
</head>
<body>
 <Home />
 <script src="_framework/blazor.web.js"></script>
</body>
</html>

```


Здесь просто загружается компонент Home, где и определена основная логика взаимодействия с веб-сервисом:

```

@using Microsoft.AspNetCore.Components.Forms
@using Microsoft.AspNetCore.Components.Web
@using System.Net.Http.Json

@rendermode RenderMode.InteractiveServer
@inject IHttpClientFactory ClientFactory


<h2>Список пользователей</h2>
<div>
 <p>
 Имя:<br />
 <input @bind-value="person.Name" />
 </p>
 <p>
 Возраст:<br />
 <input type="number" @bind-value="person.Age" />
 </p>
 <p>
 <button @onclick="Submit">Сохранить</button>
 </p>
</div>
<table>
 <thead><tr><th>Имя</th><th>Возраст</th><th></th></tr></thead>
 <tbody>
 @foreach (var person in people)
 {
 <tr>
 <td>@person.Name</td>
 <td>@person.Age</td>
 <td>
 <button @onclick="()=>Edit(person)">Изменить</button>
 <button @onclick="@(async ()=> await Delete(person.Id))">Удалить</button>
 </td>
 </tr>
 }
 </tbody>
</table>

@code {

 List<Person> people = [];
 Person person = new();
 HttpClient httpClient = null!;

 protected override async Task OnInitializedAsync()
 {
 httpClient = ClientFactory.CreateClient();
 httpClient.BaseAddress = new Uri("https://localhost:7134/api/users");
 await LoadData();
 }

 async Task LoadData()
 {
 people = await httpClient.GetFromJsonAsync<List<Person>>(httpClient.BaseAddress) ?? people;
 }
 // устанавливаем редактируемый объект
 void Edit(Person p)
 {
 person.Id = p.Id;
 person.Name = p.Name;
 person.Age = p.Age;
 }
 async Task Submit()
 {
 // если id не установлен, то метод добавляем объект
 if (string.IsNullOrWhiteSpace(person.Id))
 await httpClient.PostAsJsonAsync(httpClient.BaseAddress, person);
 else // иначе обновляем объект
 await httpClient.PutAsJsonAsync(httpClient.BaseAddress, person);
 // сбрасываем значения
 person.Id = "";
 person.Name = "";
 person.Age = 0;
 await LoadData();
 }
 // удаление объекта
 async Task Delete(string id)
 {
 await httpClient.DeleteAsync($"{httpClient.BaseAddress}/{id}");
 await LoadData();
 }
 class Person
 {
 public string Id { get; set; } = "";
 public string Name { get; set; } = "";
 public int Age { get; set; }
 }
}

```


В коде компонента определяем три переменных:

```

List<Person> people = [];
Person person = new();
HttpClient httpClient = null!;

```


Список people представляет список загруженных с сервера данные, а переменная person представляет добавляемый или обновляемый объект.


В методе `OnInitializedAsync()` при инициализации компонента создаем объект HttpClient, устанавливаем базовый адрес и с помощью метода LoadData загружаем данные с сервера:

```

protected override async Task OnInitializedAsync()
{
 httpClient = ClientFactory.CreateClient();
 httpClient.BaseAddress = new Uri("https://localhost:7134/api/users");
 await LoadData();
}

async Task LoadData()
{
 people = await httpClient.GetFromJsonAsync<List<Person>>(httpClient.BaseAddress) ?? people;
}

```


Чтобы после запуска приложения данные уже были загружены, переопределяем метод `OnInitializedAsync()` и в нем вызываем метод LoadData.


Загруженный список выводится в компоненте в таблицу:

```

@foreach (var person in people)
{
 <tr>
 <td>@person.Name</td>
 <td>@person.Age</td>
 <td>
 <button @onclick="()=>Edit(person)">Изменить</button>
 <button @onclick="@(async ()=> await Delete(person.Id))">Удалить</button>
 </td>
 </tr>
}

```


В таблице для каждого объекта определяются две кнопки. При нажатии на первую кнопку - кнопку изменения срабатывает метод `Edit`, который просто изменяет
значения свойств объекта person:

```

void Edit(Person p)
{
 person.Id = p.Id;
 person.Name = p.Name;
 person.Age = p.Age;
}

```


При нажатии на вторую кнопку - кнопку удаления срабатывает метод Delete, который отправляет запрос DELETE на сервер, а потом перезагружает данные:

```

async Task Delete(string id)
{
 await httpClient.DeleteAsync($"api/users/{id}");
 await LoadData();
}

```


Компонент определяет форму, на которой элементы ввода привязаны к переменной person - это будет либо добавляемые, либо обновляемые данные.

```

<div>
 <p>
 Имя:<br />
 <input @bind-value="person.Name" />
 </p>
 <p>
 Возраст:<br />
 <input type="number" @bind-value="person.Age" />
 </p>
 <p>
 <button @onclick="Submit">Сохранить</button>
 </p>
</div>

```


По нажатию на кнопку срабатывает метод Submit:

```

async Task Submit()
{
 if (string.IsNullOrWhiteSpace(person.Id))
 await httpClient.PostAsJsonAsync("api/users", person);
 else
 await httpClient.PutAsJsonAsync($"api/users", person);
 person.Id = "";
 person.Name = "";
 person.Age = 0;
 await LoadData();
}

```


Если ранее была нажата кнопка изменения объекта, и сработал метод Edit, то у объекта person свойство Id будет представлять непустую строку. При добавлении это свойство равнои пустой строки.
Соответственно по свойству Id мы можем узнать, идет речь об измении или добавлении объекта, и в зависимости от этого выполнить определенный запрос на сервер. После
выполнения запроса сбрасываем значения объекта person и перезагружаем данные.
![HttpClient в Blazor в C#](https://metanit.com./pics/5.2.png)











- Глава 1. Введение в Blazor


 - [Что такое Blazor](//metanit.com/sharp/blazor/1.1.php)

 - [Первое приложение на Blazor](//metanit.com/sharp/blazor/1.2.php)

 - [Рендеринг на сервере](//metanit.com/sharp/blazor/1.7.php)

 - [Рендеринг WebAssembly и авторендеринг](//metanit.com/sharp/blazor/1.8.php)

 - [Добавление Blazor в пустой проект ASP.NET Core](//metanit.com/sharp/blazor/1.4.php)

 - [Blazor WebAssembly. Первое приложение](//metanit.com/sharp/blazor/1.3.php)



- Глава 2. Компоненты


 - [Установка главного компонента](//metanit.com/sharp/blazor/2.2.php)

 - [Определение компонентов](//metanit.com/sharp/blazor/2.1.php)

 - [Вложенные компоненты. Параметры компонентов](//metanit.com/sharp/blazor/2.3.php)

 - [Передача произвольного набора атрибутов](//metanit.com/sharp/blazor/2.4.php)

 - [Обработка событий](//metanit.com/sharp/blazor/2.5.php)

 - [Обработка событий дочернего компонента в родительском](//metanit.com/sharp/blazor/2.6.php)

 - [Привязка данных](//metanit.com/sharp/blazor/2.7.php)

 - [Двусторонняя привязка и привязка параметров компонентов](//metanit.com/sharp/blazor/2.8.php)

 - [Каскадная передача значений](//metanit.com/sharp/blazor/2.9.php)

 - [Жизненный цикл компонентов](//metanit.com/sharp/blazor/2.10.php)

 - [Внедрение зависимостей в компоненты Blazor](//metanit.com/sharp/blazor/2.11.php)

 - [Привязка моделей](//metanit.com/sharp/blazor/2.12.php)

 - [Управление элементом head и компонент HeadOutlet](//metanit.com/sharp/blazor/2.13.php)

 - [Файл _Imports.razor и общие директивы компонентов](//metanit.com/sharp/blazor/2.14.php)



- Глава 3. Маршрутизация


 - [Маршрутизация между компонентами](//metanit.com/sharp/blazor/3.1.php)

 - [Компоновка](//metanit.com/sharp/blazor/3.2.php)

 - [Компонент NavLink](//metanit.com/sharp/blazor/3.3.php)

 - [Параметры маршрутов](//metanit.com/sharp/blazor/3.4.php)

 - [Параметры строки запроса](//metanit.com/sharp/blazor/3.5.php)

 - [Управление навигацией и NavigationManager](//metanit.com/sharp/blazor/3.6.php)



- Глава 4. Работа с формами и валидация


 - [Встроенные компоненты ввода](//metanit.com/sharp/blazor/4.1.php)

 - [Компонент EditForm](//metanit.com/sharp/blazor/4.2.php)

 - [Валидация на основе аннотаций данных](//metanit.com/sharp/blazor/4.3.php)

 - [Валидация и вывод сообщений об ошибках](//metanit.com/sharp/blazor/4.4.php)

 - [Программная валидация](//metanit.com/sharp/blazor/4.5.php)

 - [Кастомная валидации](//metanit.com/sharp/blazor/4.6.php)



- Глава 5. Отправка http-запросов


 - [HttpClient в проекте Blazor Server](//metanit.com/sharp/blazor/6.3.php)

 - [HttpClient в проекте Blazor WebAssembly](//metanit.com/sharp/blazor/6.1.php)

 - [Взаимодействие приложения Blazor с Web API](//metanit.com/sharp/blazor/6.2.php)



- Глава 6. Дополнительные статьи


 - [Конфигурация](//metanit.com/sharp/blazor/5.1.php)










 [Настройки](//metanit.com/settings.php)




 Помощь сайту


 [Помощь сайту](https://yoomoney.ru/to/410011174743222)



 Юмани:
 410011174743222



 Номер карты:
 4048415020898850











[Вконтакте](https://vk.com/metanit)|
[МАКС](https://max.ru/metanit)|
[Донаты/Помощь сайту](https://metanit.com/donations.php)


Contacts: metanit22@mail.ru


Copyright © Евгений Попов, metanit.com, 2026. Все права защищены.

---

**Источник:** [https://metanit.com/sharp/blazor/6.2.php](https://metanit.com/sharp/blazor/6.2.php)
