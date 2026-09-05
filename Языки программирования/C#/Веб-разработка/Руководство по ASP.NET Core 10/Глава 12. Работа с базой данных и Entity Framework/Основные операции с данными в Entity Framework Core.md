# Основные операции с данными в Entity Framework Core

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10|Руководство по ASP.NET Core 10]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 12. Работа с базой данных и Entity Framework|Глава 12. Работа с базой данных и Entity Framework]] / Основные операции с данными в Entity Framework Core

[[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 12. Работа с базой данных и Entity Framework/Подключение Entity Framework|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 12. Работа с базой данных и Entity Framework|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 13. Аутентификация и авторизация/Введение в аутентификацию и авторизацию|Вперёд]]

**Дата написания:** 05.09.2026

Последнее обновление: 19.11.2025




-

-

-














Рассмотрим, как мы можем выполнять основные операции с данными в приложении ASP.NET Core. За основу возьмем проект Web API, описанный в статье
[Пример приложения Web API](11.1), но теперь добавим в него взаимодействие с базой данных.


Пусть у нас проекте определен класс User, который будет представлять данные:

```

public class User
{
 public int Id { get; set; }
 public string Name { get; set; } = ""; // имя пользователя
 public int Age { get; set; } // возраст пользователя
}

```


Для взаимодействия с базой данных MS SQL Server в качестве контекста данных определим следующий класс ApplicationContext:

```

using Microsoft.EntityFrameworkCore;
public class ApplicationContext : DbContext
{
 public DbSet<User> Users { get; set; } = null!;
 public ApplicationContext(DbContextOptions<ApplicationContext> options)
 : base(options)
 {
 Database.EnsureCreated(); // создаем базу данных при первом обращении
 }
 protected override void OnModelCreating(ModelBuilder modelBuilder)
 {
 modelBuilder.Entity<User>().HasData(
 new User { Id = 1, Name = "Tom", Age = 37 },
 new User { Id = 2, Name = "Bob", Age = 41 },
 new User { Id = 3, Name = "Sam", Age = 24 }
 );
 }
}

```


Далее в файле Program.cs определим основной код приложения, который будет обрабатывать запросы и подключаться к базе данных:

```

using Microsoft.EntityFrameworkCore;

var builder = WebApplication.CreateBuilder();
var connection = "Data Source=app.db";
builder.Services.AddDbContext<ApplicationContext>(options => options.UseSqlite(connection));

var app = builder.Build();

app.UseDefaultFiles();
app.UseStaticFiles();

app.MapGet("/api/users", async (ApplicationContext db) => await db.Users.ToListAsync());

app.MapGet("/api/users/{id:int}", async (int id, ApplicationContext db) =>
{
 // получаем пользователя по id
 User? user = await db.Users.FirstOrDefaultAsync(u => u.Id == id);

 // если не найден, отправляем статусный код и сообщение об ошибке
 if (user == null) return Results.NotFound(new { message = "Пользователь не найден" });

 // если пользователь найден, отправляем его
 return Results.Json(user);
});

app.MapDelete("/api/users/{id:int}", async (int id, ApplicationContext db) =>
{
 // получаем пользователя по id
 User? user = await db.Users.FirstOrDefaultAsync(u => u.Id == id);

 // если не найден, отправляем статусный код и сообщение об ошибке
 if (user == null) return Results.NotFound(new { message = "Пользователь не найден" });

 // если пользователь найден, удаляем его
 db.Users.Remove(user);
 await db.SaveChangesAsync();
 return Results.Json(user);
});

app.MapPost("/api/users", async (User user, ApplicationContext db) =>
{
 // добавляем пользователя в массив
 await db.Users.AddAsync(user);
 await db.SaveChangesAsync();
 return user;
});

app.MapPut("/api/users", async (User userData, ApplicationContext db) =>
{
 // получаем пользователя по id
 var user = await db.Users.FirstOrDefaultAsync(u => u.Id == userData.Id);

 // если не найден, отправляем статусный код и сообщение об ошибке
 if (user == null) return Results.NotFound(new { message = "Пользователь не найден" });

 // если пользователь найден, изменяем его данные и отправляем обратно клиенту
 user.Age = userData.Age;
 user.Name = userData.Name;
 await db.SaveChangesAsync();
 return Results.Json(user);
});

app.Run();

```


Вначале добавляем класс ApplicationContext в сервисы приложения:

```

var builder = WebApplication.CreateBuilder();
var connection = "Data Source=app.db";
builder.Services.AddDbContext<ApplicationContext>(options => options.UseSqlite(connection));

```


Далее после создания объекта WebApplication подключаем функциональность статических файлов:

```

app.UseDefaultFiles();
app.UseStaticFiles();

```


Затем с помощью методов MapGet/MapPost/MapPut/MapDelete определяется набор конечных точек, которые будут обрабатывать разные типы запросов.


Первая конечная точка обрабатывает запрос типа GET по маршруту "api/users":

```

app.MapGet("/api/users", async (ApplicationContext db) => await db.Users.ToListAsync());

```


Поскольку выше в коде контекст данных ApplicationContext был добавлен в качестве сервиса, то мы можем его получить через параметр обработчика
конечной точки и через полученный контекст данных получить из БД список объектов User и отправить их клиенту.


Когда клиент обращается к приложению для получения одного объекта по id в запрос типа GET по адресу "api/users/{id}", то срабатывает другая конечная точка:

```

app.MapGet("/api/users/{id:int}", async (int id, ApplicationContext db) =>
{
 // получаем пользователя по id
 User? user = await db.Users.FirstOrDefaultAsync(u => u.Id == id);

 // если не найден, отправляем статусный код и сообщение об ошибке
 if (user == null) return Results.NotFound(new { message = "Пользователь не найден" });

 // если пользователь найден, отправляем его
 return Results.Json(user);
});

```


Здесь через параметр id получаем из пути запроса идентификатор объекта User и по этому идентификатору ищем нужный объект в базе данных,
используя контекст данных ApplicationContext. Если объект по Id не был найден, то возвращаем с помощью метода `Results.NotFound()` статусный код 404 с некоторым сообщением в формате JSON.
Если объект найден, то с помощью метода `Results.Json()` отправляет найденный объект клиенту.


При получении запроса типа DELETE по маршруту "/api/users/{id}" срабатывает другая конечная точка:

```

app.MapDelete("/api/users/{id:int}", async (int id, ApplicationContext db) =>
{
 // получаем пользователя по id
 User? user = await db.Users.FirstOrDefaultAsync(u => u.Id == id);

 // если не найден, отправляем статусный код и сообщение об ошибке
 if (user == null) return Results.NotFound(new { message = "Пользователь не найден" });

 // если пользователь найден, удаляем его
 db.Users.Remove(user);
 await db.SaveChangesAsync();
 return Results.Json(user);
});

```


Здесь если объект по Id не найден в базе данных, то отправляем статусный код 404. Если же объект найден, то с помощью вызова `db.Users.Remove(user)` указываем, что данный объект надо
удалить из БД. А с помощью последующего вызова `db.SaveChangesAsync()` сохраняем изменения в базу данных (то есть удаляем объект). И в конце посылаем удаленный объект клиенту.


При получении запроса с методом POST по адресу "/api/users" срабатывает следующая конечная точка:

```

app.MapPost("/api/users", async (User user, ApplicationContext db) =>
{
 // добавляем пользователя в массив
 await db.Users.AddAsync(user);
 await db.SaveChangesAsync();
 return user;
});

```


Здесь мы ожидаем, что в запросе типа POST клиент будет передавать на сервер данные, которые соответствуют определению типа User. И поэтому
инфраструктура ASP.NET Core сможет автоматически создать из них объект User. И этот объект мы сможем получить в качестве параметра в обработчике
конечной точки вместе с сервисом ApplicationContext.


После получения объекта User с помощью метода `db.Users.AddAsync(user)` указываем, что данный объект надо добавить в БД. А с помощью последующего
вызова `db.SaveChangesAsync()` сохраняем изменения в базу данных (то есть добавляем объект).
После добавления отправляем объект User обратно клиенту.


Если приложению приходит PUT-запрос по адресу "/api/users", то запрос обрабатывает последняя конечная точка:

```

app.MapPut("/api/users", async (User userData, ApplicationContext db) =>
{
 // получаем пользователя по id
 var user = await db.Users.FirstOrDefaultAsync(u => u.Id == userData.Id);

 // если не найден, отправляем статусный код и сообщение об ошибке
 if (user == null) return Results.NotFound(new { message = "Пользователь не найден" });

 // если пользователь найден, изменяем его данные и отправляем обратно клиенту
 user.Age = userData.Age;
 user.Name = userData.Name;
 await db.SaveChangesAsync();
 return Results.Json(user);
});

```


Здесь аналогичным образом получаем отправленные клиентом данные в виде объекта User и сервис ApplicationContext.
Затем пытаемся найти подобный объект в базе данных. Если объект не найден, отправляем статусный код 404.
Если объект найден, то изменяем его данные, с помощью вызова `db.SaveChangesAsync()` сохраняем изменения в базу данных и отправляем измененный объект обратно клиенту


Теперь добавим код клиента. Для этого создадим в проекте новую папку wwwroot, в которую добавим новый файл index.html
![Клиент javascript для Web API и Entity Framework в ASP.NET Core и C#](https://metanit.com./pics/12.3.png)


Определим в файле index.html следующим код для взаимодействия с веб-приложением ASP.NET Core:

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


И функция `deleteUser()` посылает приложению ASP.NET Core запрос типа DELETE на удаление пользователя, и при успешном удалении на сервере
удаляет пользователя по id из таблицы пользователей.


Теперь запустим проект, и по умолчанию приложение отправит браузеру веб-страницу index.html, которая загрузит список объектов:
![взаимодействие клиента javascript с базой данных MS SQL Server через Entity Framework в ASP.NET Core и C#](https://metanit.com./pics/1.21.png)


После этого мы сможем выполнять все базовые операции с пользователями - получение, добавление, изменение, удаление. Например, добавим нового пользователя:
![REST, Web API, работа с базой данных MS SQL Server и Entity Framework в ASP.NET Core и C#](https://metanit.com./pics/1.22.png)











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

**Источник:** [https://metanit.com/sharp/aspnet6/12.2.php](https://metanit.com/sharp/aspnet6/12.2.php)
