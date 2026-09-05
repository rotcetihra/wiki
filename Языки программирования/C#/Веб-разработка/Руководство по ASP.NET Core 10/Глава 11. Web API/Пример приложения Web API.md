# Пример приложения Web API

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10|Руководство по ASP.NET Core 10]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 11. Web API|Глава 11. Web API]] / Пример приложения Web API

[[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 10. Results API/Определение своего типа IResult|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 11. Web API|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 12. Работа с базой данных и Entity Framework/Подключение Entity Framework|Вперёд]]

**Дата написания:** 05.09.2026

## Пример приложения Web API

Последнее обновление: 25.12.2021




-

-

-














Web API представляет способ построения приложения в стиле REST
(Representation State Transfer или "передача состояния представления").
REST-архитектура предполагает применение следующих методов или типов запросов HTTP для взаимодействия с сервером:


-

GET (получение данных)

-

POST (добавление данных)

-

PUT (изменение данных)

-

DELETE (удаление данных)


Для реализации подобной архитектуру фреймворк ASP.NET Core предоставляет ряд встроенных методов, которые как и метод Map() реализованы
как методы расширения для типа Microsoft.AspNetCore.Routing.IEndpointRouteBuilder (а соответственно и для типа WebApplication).
Эти методы также встраивают в конвейер обработки запроса конечные точки, которые обрабатывают определенные типы запросов:


-

MapGet (запрос GET)

-

MapPost (запрос POST)

-

MapPut (запрос PUT)

-

MapDelete (запрос DELETE)


Рассмотрим, как мы можем реализовать с помощью этих методов простейший API.


### Создание сервера


Вначале определим веб-приложение на ASP.NET Core, которое и будет собственно представлять Web API:

```

// начальные данные
List<Person> users = new List<Person>
{
 new() { Id = Guid.NewGuid().ToString(), Name = "Tom", Age = 37 },
 new() { Id = Guid.NewGuid().ToString(), Name = "Bob", Age = 41 },
 new() { Id = Guid.NewGuid().ToString(), Name = "Sam", Age = 24 }
};

var builder = WebApplication.CreateBuilder();
var app = builder.Build();

app.UseDefaultFiles();
app.UseStaticFiles();

app.MapGet("/api/users", ()=> users);

app.MapGet("/api/users/{id}", (string id) =>
{
 // получаем пользователя по id
 Person? user = users.FirstOrDefault(u => u.Id == id);
 // если не найден, отправляем статусный код и сообщение об ошибке
 if (user == null) return Results.NotFound(new { message = "Пользователь не найден" });

 // если пользователь найден, отправляем его
 return Results.Json(user);
});

app.MapDelete("/api/users/{id}", (string id) =>
{
 // получаем пользователя по id
 Person? user = users.FirstOrDefault(u => u.Id == id);

 // если не найден, отправляем статусный код и сообщение об ошибке
 if (user == null) return Results.NotFound(new { message = "Пользователь не найден" });

 // если пользователь найден, удаляем его
 users.Remove(user);
 return Results.Json(user);
});

app.MapPost("/api/users", (Person user)=>{

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
 if (user == null) return Results.NotFound(new { message = "Пользователь не найден" });
 // если пользователь найден, изменяем его данные и отправляем обратно клиенту

 user.Age = userData.Age;
 user.Name = userData.Name;
 return Results.Json(user);
});

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


Далее после создания объекта WebApplication подключаем функциональность статических файлов:

```

app.UseDefaultFiles();
app.UseStaticFiles();

```


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
 if (user == null) return Results.NotFound(new { message = "Пользователь не найден" });

 // если пользователь найден, отправляем его
 return Results.Json(user);
});

```


Здесь через параметр id получаем из пути запроса идентификатор объекта Person и по этому идентификатору ищем нужный объект в списке users.
Если объект по Id не был найден, то возвращаем с помощью метода `Results.NotFound()` статусный код 404 с некоторым сообщением в формате JSON.
Если объект найден, то с помощью метода `Results.Json()` отправляет найденный объект клиенту.


При получении запроса типа DELETE по маршруту "/api/users/{id}" срабатывает другая конечная точка:

```

app.MapDelete("/api/users/{id}", (string id) =>
{
 // получаем пользователя по id
 Person? user = users.FirstOrDefault(u => u.Id == id);

 // если не найден, отправляем статусный код и сообщение об ошибке
 if (user == null) return Results.NotFound(new { message = "Пользователь не найден" });

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
 if (user == null) return Results.NotFound(new { message = "Пользователь не найден" });
 // если пользователь найден, изменяем его данные и отправляем обратно клиенту
 user.Age = userData.Age;
 user.Name = userData.Name;
 return Results.Json(user);
});

```


Таким образом, мы определили простейший API. Теперь добавим код клиента.


### Определение клиента


Теперь создадим в проекте новую папку wwwroot, в которую добавим новый файл index.html
![Создание клиента javascript для Web API в ASP.NET Core и C#](https://metanit.com./pics/11.3.png)


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
![взаимодействие javascript с Web API и MapGet, MapPost, MapPut, MapDelete в ASP.NET Core и C#](https://metanit.com./pics/1.21.png)


После этого мы сможем выполнять все базовые операции с пользователями - получение, добавление, изменение, удаление. Например, добавим нового пользователя:
![REST и Web API с помощью MapGet, MapPost, MapPut, MapDelete в ASP.NET Core и C#](https://metanit.com./pics/1.22.png)











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

**Источник:** [https://metanit.com/sharp/aspnet6/11.1.php](https://metanit.com/sharp/aspnet6/11.1.php)
