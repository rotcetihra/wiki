# Создание простейшего API

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10|Руководство по ASP.NET Core 10]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 2. Основы в ASP.NET Core|Глава 2. Основы в ASP.NET Core]] / Создание простейшего API

[[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 2. Основы в ASP.NET Core/Отправка и получение json|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 2. Основы в ASP.NET Core|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 2. Основы в ASP.NET Core/Загрузка файлов на сервер|Вперёд]]

**Дата написания:** 05.09.2026

## Создание простейшего API

Последнее обновление: 16.12.2021




-

-

-














Рассмотренного в прошлых темах материала достаточно для создания примитивного приложения. В этой теме попробуем реализовать простейшее приложение
Web API в стиле REST. Архитектура REST предполагает применение следующих методов или типов запросов HTTP для взаимодействия с сервером, где каждый тип запроса отвечает за определенное действие:


-

GET (получение данных)

-

POST (добавление данных)

-

PUT (изменение данных)

-

DELETE (удаление данных)


Поскольку в приложении ASP.NET Core мы можем легко получить и адрес запроса и тип запроса, то реализовать подобную архитектуру не составит труда.


### Создание сервера на ASP.NET Core


Вначале определим веб-приложение на ASP.NET Core, которое и будет собственно представлять Web API:

```

using System.Text.RegularExpressions;

// начальные данные
List<Person> users = new List<Person>
{
 new() { Id = Guid.NewGuid().ToString(), Name = "Tom", Age = 37 },
 new() { Id = Guid.NewGuid().ToString(), Name = "Bob", Age = 41 },
 new() { Id = Guid.NewGuid().ToString(), Name = "Sam", Age = 24 }
};

var builder = WebApplication.CreateBuilder();
var app = builder.Build();

app.Run(async (context) =>
{
 var response = context.Response;
 var request = context.Request;
 var path = request.Path;
 //string expressionForNumber = "^/api/users/([0-9]+)$"; // если id представляет число

 // 2e752824-1657-4c7f-844b-6ec2e168e99c
 string expressionForGuid = @"^/api/users/\w{8}-\w{4}-\w{4}-\w{4}-\w{12}$";
 if (path == "/api/users" && request.Method=="GET")
 {
 await GetAllPeople(response);
 }
 else if (Regex.IsMatch(path, expressionForGuid) && request.Method == "GET")
 {
 // получаем id из адреса url
 string? id = path.Value?.Split("/")[3];
 await GetPerson(id, response);
 }
 else if (path == "/api/users" && request.Method == "POST")
 {
 await CreatePerson(response, request);
 }
 else if (path == "/api/users" && request.Method == "PUT")
 {
 await UpdatePerson(response, request);
 }
 else if (Regex.IsMatch(path, expressionForGuid) && request.Method == "DELETE")
 {
 string? id = path.Value?.Split("/")[3];
 await DeletePerson(id, response);
 }
 else
 {
 response.ContentType = "text/html; charset=utf-8";
 await response.SendFileAsync("html/index.html");
 }
});

app.Run();

// получение всех пользователей
async Task GetAllPeople(HttpResponse response)
{
 await response.WriteAsJsonAsync(users);
}
// получение одного пользователя по id
async Task GetPerson(string? id, HttpResponse response)
{
 // получаем пользователя по id
 Person? user = users.FirstOrDefault((u) => u.Id == id);
 // если пользователь найден, отправляем его
 if (user != null)
 await response.WriteAsJsonAsync(user);
 // если не найден, отправляем статусный код и сообщение об ошибке
 else
 {
 response.StatusCode = 404;
 await response.WriteAsJsonAsync(new { message = "Пользователь не найден" });
 }
}

async Task DeletePerson(string? id, HttpResponse response)
{
 // получаем пользователя по id
 Person? user = users.FirstOrDefault((u) => u.Id == id);
 // если пользователь найден, удаляем его
 if (user != null)
 {
 users.Remove(user);
 await response.WriteAsJsonAsync(user);
 }
 // если не найден, отправляем статусный код и сообщение об ошибке
 else
 {
 response.StatusCode = 404;
 await response.WriteAsJsonAsync(new { message = "Пользователь не найден" });
 }
}

async Task CreatePerson(HttpResponse response, HttpRequest request)
{
 try
 {
 // получаем данные пользователя
 var user = await request.ReadFromJsonAsync<Person>();
 if (user != null)
 {
 // устанавливаем id для нового пользователя
 user.Id = Guid.NewGuid().ToString();
 // добавляем пользователя в список
 users.Add(user);
 await response.WriteAsJsonAsync(user);
 }
 else
 {
 throw new Exception("Некорректные данные");
 }
 }
 catch (Exception)
 {
 response.StatusCode = 400;
 await response.WriteAsJsonAsync(new { message = "Некорректные данные" });
 }
}

async Task UpdatePerson(HttpResponse response, HttpRequest request)
{
 try
 {
 // получаем данные пользователя
 Person? userData = await request.ReadFromJsonAsync<Person>();
 if (userData != null)
 {
 // получаем пользователя по id
 var user = users.FirstOrDefault(u => u.Id == userData.Id);
 // если пользователь найден, изменяем его данные и отправляем обратно клиенту
 if (user != null)
 {
 user.Age = userData.Age;
 user.Name = userData.Name;
 await response.WriteAsJsonAsync(user);
 }
 else
 {
 response.StatusCode = 404;
 await response.WriteAsJsonAsync(new { message = "Пользователь не найден" });
 }
 }
 else
 {
 throw new Exception("Некорректные данные");
 }
 }
 catch (Exception)
 {
 response.StatusCode = 400;
 await response.WriteAsJsonAsync(new { message = "Некорректные данные" });
 }
}
public class Person
{
 public string Id { get; set; } = "";
 public string Name { get; set; } = "";
 public int Age { get; set; }
}

```


Разберем в общих чертах этот код. Вначале идет определение данных - список объектов Person, с которыми будут работать клиенты:

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


В методе `app.Run()` определяем компонент middleware, который в зависимости от типа запросов (GET/POST/PUT/DELETE) выполняет те или иные действия.


Так, когда приложение получает запрос типа GET по адресу "api/users", то срабатывает следующий код:

```

if (path == "/api/users" && request.Method=="GET")
{
 await GetAllPeople(response);
}
//.........
// получение всех пользователей
async Task GetAllPeople(HttpResponse response)
{
 await response.WriteAsJsonAsync(users);
}

```


Запрос GET предполагает получение объектов, и в данном случае отправляем выше определенный список объектов Person.


Когда клиент обращается к приложению для получения одного объекта по id в запрос типа GET по адресу "api/users/[id]", то срабатывает следующий код:

```

else if (Regex.IsMatch(path, expressionForGuid) && request.Method == "GET")
{
 // получаем id из адреса url
 string? id = path.Value?.Split("/")[3];
 await GetPerson(id, response);
}
//..............
// получение одного пользователя по id
async Task GetPerson(string? id, HttpResponse response)
{
 // получаем пользователя по id
 Person? user = users.FirstOrDefault((u) => u.Id == id);
 // если пользователь найден, отправляем его
 if (user != null)
 await response.WriteAsJsonAsync(user);
 // если не найден, отправляем статусный код и сообщение об ошибке
 else
 {
 response.StatusCode = 404;
 await response.WriteAsJsonAsync(new { message = "Пользователь не найден" });
 }
}

```


Чтобы убедиться, что в запрошенном адресе после "/api/users/" указан id, проверяем соответствие адреса регулярному выражению: `"^/api/users/\w{8}-\w{4}-\w{4}-\w{4}-\w{12}$"`.
Данное выражение проверяет соответствие последнего сегмента адреса значению Guid, который имеет формат `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`


В этом случае нам надо найти нужного пользователя по Id в списке и отправить клиенту. Если же пользователь по Id не был найден, то возвращаем
статусный код 404 с некоторым сообщением в формате JSON.


При получении запроса DELETE действует аналогичная логика:

```

else if (Regex.IsMatch(path, expressionForGuid) && request.Method == "DELETE")
{
 // получаем id из адреса url
 string? id = path.Value?.Split("/")[3];
 await DeletePerson(id, response);
}
//..............
async Task DeletePerson(string? id, HttpResponse response)
{
 // получаем пользователя по id
 Person? user = users.FirstOrDefault((u) => u.Id == id);
 // если пользователь найден, удаляем его
 if (user != null)
 {
 users.Remove(user);
 await response.WriteAsJsonAsync(user);
 }
 // если не найден, отправляем статусный код и сообщение об ошибке
 else
 {
 response.StatusCode = 404;
 await response.WriteAsJsonAsync(new { message = "Пользователь не найден" });
 }
}

```


Только в данном случае, если пользователь найден в списке, удаляем его из списка и посылаем клиенту.


При получении запроса с методом POST по адресу "/api/users" используем метод `request.ReadFromJsonAsync()` для извлечения данных из запроса:

```

else if (path == "/api/users" && request.Method == "POST")
{
 await CreatePerson(response, request);
}
//..............
async Task CreatePerson(HttpResponse response, HttpRequest request)
{
 try
 {
 // получаем данные пользователя
 var user = await request.ReadFromJsonAsync<Person>();
 if (user != null)
 {
 // устанавливаем id для нового пользователя
 user.Id = Guid.NewGuid().ToString();
 // добавляем пользователя в список
 users.Add(user);
 await response.WriteAsJsonAsync(user);
 }
 else
 {
 throw new Exception("Некорректные данные");
 }
 }
 catch (Exception)
 {
 response.StatusCode = 400;
 await response.WriteAsJsonAsync(new { message = "Некорректные данные" });
 }
}

```


Поскольку при извлечении данных из запроса может произойти исключение (например, в результате парсинга в JSON), оборачиваем весь код в
`try..catch`. И в случае успешного получения данных устанавливаем у нового объекта свойство Id, добавляем его в список users и отправляем обратно клиенту.


Если приложению приходит PUT-запрос, то также с помощью метода `request.ReadFromJsonAsync()` получаем отправленные клиентом данные.
Если объект найден в списке, то изменяем его данные и отправляем обратно клиенту, иначе отправляем статусный код 404:

```

else if (path == "/api/users" && request.Method == "PUT")
{
 await UpdatePerson(response, request);
}
//..............
async Task UpdatePerson(HttpResponse response, HttpRequest request)
{
 try
 {
 // получаем данные пользователя
 Person? userData = await request.ReadFromJsonAsync<Person>();
 if (userData != null)
 {
 // получаем пользователя по id
 var user = users.FirstOrDefault(u => u.Id == userData.Id);
 // если пользователь найден, изменяем его данные и отправляем обратно клиенту
 if (user != null)
 {
 user.Age = userData.Age;
 user.Name = userData.Name;
 await response.WriteAsJsonAsync(user);
 }
 else
 {
 response.StatusCode = 404;
 await response.WriteAsJsonAsync(new { message = "Пользователь не найден" });
 }
 }
 else
 {
 throw new Exception("Некорректные данные");
 }
 }
 catch (Exception)
 {
 response.StatusCode = 400;
 await response.WriteAsJsonAsync(new { message = "Некорректные данные" });
 }
}

```


В случае, если запрос идет по другому адресу, то отправляем клиенту веб-страницу index.html, которую мы далее определим:

```

else
{
 response.ContentType = "text/html; charset=utf-8";
 await response.SendFileAsync("html/index.html");
}

```


Таким образом, мы определили простейший API. Теперь добавим код клиента.


### Определение клиента


Теперь добавим в проект папку html, в которую добавим новый файл index.html
![Создание Web API в ASP.NET Core и C#](https://metanit.com./pics/2.33.png)


Определим в файле index.html следующим код для взаимодействия с сервером ASP.NET Core:

```

<!DOCTYPE html>
<html>
<head>
 <meta charset="utf-8" />
 <title>METANIT.COM</title>
<style>
td {padding:5px;}
button{margin: 5px;}
</style>
</head>
<body>
 <h2>Список пользователей</h2>
 <div>
 <input type="hidden" id="userId" />
 <p>
 Имя:<br/>
 <input id="userName" />
 </p>
 <p>
 Возраст:<br />
 <input id="userAge" type="number" />
 </p>
 <p>
 <button id="saveBtn">Сохранить</button>
 <button id="resetBtn">Сбросить</button>
 </p>
 </div>
 <table>
 <thead><tr><th>Имя</th><th>Возраст</th><th></th></tr></thead>
 <tbody>
 </tbody>
 </table>

 <script>
 // Получение всех пользователей
 async function getUsers() {
 // отправляет запрос и получаем ответ
 const response = await fetch("/api/users", {
 method: "GET",
 headers: { "Accept": "application/json" }
 });
 // если запрос прошел нормально
 if (response.ok === true) {
 // получаем данные
 const users = await response.json();
 const rows = document.querySelector("tbody");
 // добавляем полученные элементы в таблицу
 users.forEach(user => rows.append(row(user)));
 }
 }
 // Получение одного пользователя
 async function getUser(id) {
 const response = await fetch(`/api/users/${id}`, {
 method: "GET",
 headers: { "Accept": "application/json" }
 });
 if (response.ok === true) {
 const user = await response.json();
 document.getElementById("userId").value = user.id;
 document.getElementById("userName").value = user.name;
 document.getElementById("userAge").value = user.age;
 }
 else {
 // если произошла ошибка, получаем сообщение об ошибке
 const error = await response.json();
 console.log(error.message); // и выводим его на консоль
 }
 }
 // Добавление пользователя
 async function createUser(userName, userAge) {

 const response = await fetch("api/users", {
 method: "POST",
 headers: { "Accept": "application/json", "Content-Type": "application/json" },
 body: JSON.stringify({
 name: userName,
 age: parseInt(userAge, 10)
 })
 });
 if (response.ok === true) {
 const user = await response.json();
 document.querySelector("tbody").append(row(user));
 }
 else {
 const error = await response.json();
 console.log(error.message);
 }
 }
 // Изменение пользователя
 async function editUser(userId, userName, userAge) {
 const response = await fetch("api/users", {
 method: "PUT",
 headers: { "Accept": "application/json", "Content-Type": "application/json" },
 body: JSON.stringify({
 id: userId,
 name: userName,
 age: parseInt(userAge, 10)
 })
 });
 if (response.ok === true) {
 const user = await response.json();
 document.querySelector(`tr[data-rowid='${user.id}']`).replaceWith(row(user));
 }
 else {
 const error = await response.json();
 console.log(error.message);
 }
 }
 // Удаление пользователя
 async function deleteUser(id) {
 const response = await fetch(`/api/users/${id}`, {
 method: "DELETE",
 headers: { "Accept": "application/json" }
 });
 if (response.ok === true) {
 const user = await response.json();
 document.querySelector(`tr[data-rowid='${user.id}']`).remove();
 }
 else {
 const error = await response.json();
 console.log(error.message);
 }
 }

 // сброс данных формы после отправки
 function reset() {
 document.getElementById("userId").value =
 document.getElementById("userName").value =
 document.getElementById("userAge").value = "";
 }
 // создание строки для таблицы
 function row(user) {

 const tr = document.createElement("tr");
 tr.setAttribute("data-rowid", user.id);

 const nameTd = document.createElement("td");
 nameTd.append(user.name);
 tr.append(nameTd);

 const ageTd = document.createElement("td");
 ageTd.append(user.age);
 tr.append(ageTd);

 const linksTd = document.createElement("td");

 const editLink = document.createElement("button");
 editLink.append("Изменить");
 editLink.addEventListener("click", async() => await getUser(user.id));
 linksTd.append(editLink);

 const removeLink = document.createElement("button");
 removeLink.append("Удалить");
 removeLink.addEventListener("click", async () => await deleteUser(user.id));

 linksTd.append(removeLink);
 tr.appendChild(linksTd);

 return tr;
 }
 // сброс значений формы
 document.getElementById("resetBtn").addEventListener("click", () => reset());

 // отправка формы
 document.getElementById("saveBtn").addEventListener("click", async () => {

 const id = document.getElementById("userId").value;
 const name = document.getElementById("userName").value;
 const age = document.getElementById("userAge").value;
 if (id === "")
 await createUser(name, age);
 else
 await editUser(id, name, age);
 reset();
 });

 // загрузка пользователей
 getUsers();
 </script>
</body>
</html>

```


Основная логика здесь заключена в коде javascript. При загрузке страницы в браузере получаем все объекты из БД с помощью функции `getUsers()`:

```

async function getUsers() {
 // отправляет запрос и получаем ответ
 const response = await fetch("/api/users", {
 method: "GET",
 headers: { "Accept": "application/json" }
 });
 // если запрос прошел нормально
 if (response.ok === true) {
 // получаем данные
 const users = await response.json();
 const rows = document.querySelector("tbody");
 // добавляем полученные элементы в таблицу
 users.forEach(user => rows.append(row(user)));
 }
}

```


Для добавления строк в таблицу используется функция `row()`, которая возвращает строку. В этой строке будут определены ссылки для изменения и удаления пользователя.


Ссылка для изменения пользователя с помощью функции `getUser()` получает с сервера выделенного пользователя:

```

async function getUser(id) {
 const response = await fetch(`/api/users/${id}`, {
 method: "GET",
 headers: { "Accept": "application/json" }
 });
 if (response.ok === true) {
 const user = await response.json();
 document.getElementById("userId").value = user.id;
 document.getElementById("userName").value = user.name;
 document.getElementById("userAge").value = user.age;
 }
 else {
 // если произошла ошибка, получаем сообщение об ошибке
 const error = await response.json();
 console.log(error.message); // и выводим его на консоль
 }
}

```


И выделенный пользователь добавляется в форму над таблицей. Эта же форма применяется и для добавления объекта. С помощью скрытого поля, которое хранит id пользователя, мы можем узнать, какое действие выполняется - добавление или редактирование. Если id не установлен (равен пустой строке), то выполняется функция createUser, которая отправляет данные в POST-запросе:

```

async function createUser(userName, userAge) {

 const response = await fetch("api/users", {
 method: "POST",
 headers: { "Accept": "application/json", "Content-Type": "application/json" },
 body: JSON.stringify({
 name: userName,
 age: parseInt(userAge, 10)
 })
 });
 if (response.ok === true) {
 const user = await response.json();
 document.querySelector("tbody").append(row(user));
 }
 else {
 const error = await response.json();
 console.log(error.message);
 }
}

```


Если же ранее пользователь был загружен на форму, и в скрытом поле сохранился его id, то выполняется функция editUser, которая отправляет PUT-запрос:

```

async function editUser(userId, userName, userAge) {
 const response = await fetch("api/users", {
 method: "PUT",
 headers: { "Accept": "application/json", "Content-Type": "application/json" },
 body: JSON.stringify({
 id: userId,
 name: userName,
 age: parseInt(userAge, 10)
 })
 });
 if (response.ok === true) {
 const user = await response.json();
 document.querySelector(`tr[data-rowid='${user.id}']`).replaceWith(row(user));
 }
 else {
 const error = await response.json();
 console.log(error.message);
 }
}

```


И функция `deleteUser()` посылает на сервер запрос типа DELETE на удаление пользователя, и при успешном удалении на сервере
удаляет объект по id из списка объектов Person.


Теперь запустим проект, и по умолчанию приложение отправит браузеру веб-страницу index.html, которая загрузит список объектов:
![взаимодействие javascript с Web API в ASP.NET Core и C#](https://metanit.com./pics/1.21.png)


После этого мы сможем выполнять все базовые операции с пользователями - получение, добавление, изменение, удаление. Например, добавим нового пользователя:
![REST и Web API с помощью app.Run в ASP.NET Core и C#](https://metanit.com./pics/1.22.png)










- Глава 1. Введение в ASP.NET Core


 - [Что такое ASP.NET Core](//metanit.com/sharp/aspnet6/1.1.php)

 - [Первое приложение на ASP.NET Core с .NET CLI](//metanit.com/sharp/aspnet6/1.3.php)

 - [Первое приложение в Visual Studio](//metanit.com/sharp/aspnet6/1.2.php)



- Глава 2. Основы в ASP.NET Core


 - [Создание и запуск приложения. WebApplication и WebApplicationBuilder](//metanit.com/sharp/aspnet6/2.1.php)

 - [Конвейер обработки запроса и middleware](//metanit.com/sharp/aspnet6/2.2.php)

 - [Метод Run и определение терминального middleware](//metanit.com/sharp/aspnet6/2.3.php)

 - [HttpResponse. Отправка ответа](//metanit.com/sharp/aspnet6/2.4.php)

 - [HttpRequest. Получение данных запроса](//metanit.com/sharp/aspnet6/2.5.php)

 - [Отправка файлов](//metanit.com/sharp/aspnet6/2.6.php)

 - [Отправка форм](//metanit.com/sharp/aspnet6/2.8.php)

 - [Переадресация](//metanit.com/sharp/aspnet6/2.9.php)

 - [Отправка и получение json](//metanit.com/sharp/aspnet6/2.10.php)

 - [Создание простейшего API](//metanit.com/sharp/aspnet6/2.11.php)

 - [Загрузка файлов на сервер](//metanit.com/sharp/aspnet6/2.12.php)

 - [Метод Use](//metanit.com/sharp/aspnet6/2.7.php)

 - [Создание ветки конвейера. UseWhen и MapWhen](//metanit.com/sharp/aspnet6/2.13.php)

 - [Метод Map](//metanit.com/sharp/aspnet6/2.14.php)

 - [Классы middleware](//metanit.com/sharp/aspnet6/2.15.php)

 - [Построение конвейера обработки запроса](//metanit.com/sharp/aspnet6/2.16.php)

 - [IWebHostEnvironment и окружение](//metanit.com/sharp/aspnet6/2.17.php)



- Глава 3. Dependency Injection


 - [Внедрение зависимостей и IServiceCollection](//metanit.com/sharp/aspnet6/4.1.php)

 - [Создание сервисов](//metanit.com/sharp/aspnet6/4.2.php)

 - [Получение зависимостей](//metanit.com/sharp/aspnet6/4.3.php)

 - [Жизненный цикл зависимостей](//metanit.com/sharp/aspnet6/4.4.php)

 - [Применение сервисов в классах middleware](//metanit.com/sharp/aspnet6/4.5.php)

 - [Scoped-сервисы в singleton-объектах](//metanit.com/sharp/aspnet6/4.6.php)

 - [Множественная регистрация сервисов](//metanit.com/sharp/aspnet6/4.7.php)



- Глава 4. Маршрутизация


 - [Конечные точки. Метод Map](//metanit.com/sharp/aspnet6/3.1.php)

 - [Параметры маршрута](//metanit.com/sharp/aspnet6/3.2.php)

 - [Ограничения маршрутов](//metanit.com/sharp/aspnet6/3.3.php)

 - [Создание ограничений маршрутов](//metanit.com/sharp/aspnet6/3.4.php)

 - [Передача зависимостей в конечные точки](//metanit.com/sharp/aspnet6/3.5.php)

 - [Сопоставление запроса с конечной точкой](//metanit.com/sharp/aspnet6/3.6.php)

 - [Сочетание конечных точек с другими middleware](//metanit.com/sharp/aspnet6/3.7.php)

 - [Получение параметров строки запроса](//metanit.com/sharp/aspnet6/3.8.php)



- Глава 5. Статические файлы


 - [Установка каталога статических файлов. UseStaticFiles](//metanit.com/sharp/aspnet6/5.1.php)

 - [Работа со статическими файлами](//metanit.com/sharp/aspnet6/5.2.php)

 - [Статические файлы и MapStaticAssets](//metanit.com/sharp/aspnet6/5.3.php)



- Глава 6. Конфигурация


 - [Основы конфигурации](//metanit.com/sharp/aspnet6/6.1.php)

 - [Нефайловые провайдеры конфигурации](//metanit.com/sharp/aspnet6/6.2.php)

 - [Конфигурация в файлах JSON, XML и Ini](//metanit.com/sharp/aspnet6/6.3.php)

 - [Конфигурация по умолчанию и объединение конфигураций](//metanit.com/sharp/aspnet6/6.4.php)

 - [Анализ конфигурации](//metanit.com/sharp/aspnet6/6.5.php)

 - [Создание провайдера конфгурации](//metanit.com/sharp/aspnet6/6.6.php)

 - [Проекция конфигурации на классы](//metanit.com/sharp/aspnet6/6.7.php)

 - [Передача конфигурации через IOptions](//metanit.com/sharp/aspnet6/6.8.php)



- Глава 7. Логгирование


 - [Ведение лога и ILogger](//metanit.com/sharp/aspnet6/7.1.php)

 - [Фабрика логгера и провайдеры логгирования](//metanit.com/sharp/aspnet6/7.2.php)

 - [Конфигурация и фильтрация логгирования](//metanit.com/sharp/aspnet6/7.3.php)

 - [Создание провайдера логгирования](//metanit.com/sharp/aspnet6/7.4.php)



- Глава 8. Состояние приложения. Куки. Сессии


 - [HttpContext.Items](//metanit.com/sharp/aspnet6/8.1.php)

 - [Куки](//metanit.com/sharp/aspnet6/8.2.php)

 - [Сессии](//metanit.com/sharp/aspnet6/8.3.php)



- Глава 9. Обработка ошибок


 - [Обработка исключений](//metanit.com/sharp/aspnet6/9.1.php)

 - [Обработка ошибок HTTP](//metanit.com/sharp/aspnet6/9.2.php)



- Глава 10. Results API


 - [Введение в Results API](//metanit.com/sharp/aspnet6/10.1.php)

 - [Отправка текста и json в Results API](//metanit.com/sharp/aspnet6/10.2.php)

 - [Переадресация в Results API](//metanit.com/sharp/aspnet6/10.3.php)

 - [Отправка статусных кодов в Results API](//metanit.com/sharp/aspnet6/10.4.php)

 - [Отправка файлов в Results API](//metanit.com/sharp/aspnet6/10.5.php)

 - [Определение своего типа IResult](//metanit.com/sharp/aspnet6/10.6.php)



- Глава 11. Web API


 - [Пример приложения Web API](//metanit.com/sharp/aspnet6/11.1.php)



- Глава 12. Работа с базой данных и Entity Framework


 - [Подключение Entity Framework](//metanit.com/sharp/aspnet6/12.1.php)

 - [Основные операции с данными в Entity Framework Core](//metanit.com/sharp/aspnet6/12.2.php)



- Глава 13. Аутентификация и авторизация


 - [Введение в аутентификацию и авторизацию](//metanit.com/sharp/aspnet6/13.1.php)

 - [Аутентификация с помощью JWT-токенов](//metanit.com/sharp/aspnet6/13.2.php)

 - [Авторизация с помощью JWT-токенов в клиенте JavaScript](//metanit.com/sharp/aspnet6/13.3.php)

 - [Аутентификация с помощью куки](//metanit.com/sharp/aspnet6/13.4.php)

 - [HttpContext.User, ClaimPrincipal и ClaimsIdentity](//metanit.com/sharp/aspnet6/13.5.php)

 - [ClaimPrincipal и объекты Claim](//metanit.com/sharp/aspnet6/13.6.php)

 - [Авторизация по ролям](//metanit.com/sharp/aspnet6/13.7.php)

 - [Авторизация на основе Claims](//metanit.com/sharp/aspnet6/13.8.php)

 - [Создание ограничений для авторизации](//metanit.com/sharp/aspnet6/13.9.php)



- Глава 14. CORS и кросс-доменные запросы


 - [Подключение CORS в приложении](//metanit.com/sharp/aspnet6/14.1.php)

 - [Конфигурация CORS](//metanit.com/sharp/aspnet6/14.2.php)

 - [Политики CORS](//metanit.com/sharp/aspnet6/14.3.php)

 - [Глобальная и локальная настройка CORS](//metanit.com/sharp/aspnet6/14.4.php)



- Глава 15. URL Rewriting


 - [Введение в URL Rewriting](//metanit.com/sharp/aspnet6/15.1.php)

 - [Правила IIS для URL Rewriting](//metanit.com/sharp/aspnet6/15.2.php)

 - [Применение правил Apache для URL Rewriting](//metanit.com/sharp/aspnet6/15.3.php)

 - [Создание правил URL Rewriting](//metanit.com/sharp/aspnet6/15.4.php)



- Глава 16. Клиентская разработка


 - [Бандлинг и минификация](//metanit.com/sharp/aspnet6/16.1.php)

 - [Пакетный менеджер Libman](//metanit.com/sharp/aspnet6/16.2.php)

 - [Пакетный менеджер NPM](//metanit.com/sharp/aspnet6/16.3.php)



- Глава 17. Кэширование


 - [Кэширование с помощью MemoryCache](//metanit.com/sharp/aspnet6/17.1.php)

 - [Распределенное кэширование. Redis](//metanit.com/sharp/aspnet6/17.2.php)

 - [Сжатие ответа](//metanit.com/sharp/aspnet6/17.3.php)

 - [Кэширование статических файлов](//metanit.com/sharp/aspnet6/17.4.php)

 - [Кэширование ответа и OutputCache](//metanit.com/sharp/aspnet6/17.5.php)



- Глава 18. Мониторинг работоспособности приложения


 - [Health Check Middleware](//metanit.com/sharp/aspnet6/18.1.php)










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

**Источник:** [https://metanit.com/sharp/aspnet6/2.11.php](https://metanit.com/sharp/aspnet6/2.11.php)
