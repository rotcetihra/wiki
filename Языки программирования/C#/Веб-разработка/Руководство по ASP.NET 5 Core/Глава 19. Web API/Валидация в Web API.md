# Валидация в Web API

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET 5 Core|Руководство по ASP.NET 5 Core]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET 5 Core/Глава 19. Web API|Глава 19. Web API]] / Валидация в Web API

[[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET 5 Core/Глава 19. Web API/Создание клиента для WEB API|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET 5 Core/Глава 19. Web API|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET 5 Core/Глава 19. Web API/Content negotiation|Вперёд]]

**Дата написания:** 05.09.2026

## Валидация в Web API


Данное руководство устарело. Актуальное руководство: [Руководство по ASP.NET Core 7](https://metanit.com/sharp/aspnet6/)Последнее обновление: 30.12.2019




-

-

-














В прошлой теме было рассмотрено создание представления - визуальной части для работы с Web API. В частности, мы могли создать или отредактировать модель и отправить ее на сервер.
Но при этом не учитывалась валидация данных. Более того не учитывался вывод ошибок валидации, чтобы пользователь смог увидеть, что не так, изменить данные и повторить отправку.


Если бы мы работали в ASP.NET Core MVC, то там с валидацией все проще - с помощью значения ModelState.IsValid проверяем корректность модели.
Если модель проходит валидацию, то перенаправляем на определенное действие, если не проходит валидацию, то возвращаем представление с ошибками. Однако
Web API использует в целом иную модель обработки запросов, а взаимодействие между сервером и клиентом происходит главным образом через Ajax, что накладывает свои ограничения
на валидацию данных.


При использовании Web API состояние обработки запроса на сервере мы можем контролировать с помощью статусных кодов:


-

`200`: статус Ok. Указывает на удачное выполнение запроса

-

`201`: статус Created. Указывает на успешное создание объекта, как правило, используется в запросах POST

-

`204`: статус NoContent - запрос прошел успешно, например, после удаления

-

`400`: статус BadRequest - ошибка при выполнении запроса

-

`401`: статус Unathorized - пользователь не авторизован

-

`403`: статус Forbidden - доступ запрещен

-

`404`: статус NotFound - ресурс не найден


Отправляя определенный статусный код, мы уже даем клиенту знать о характере возникшей ошибки или статусе запросе.


Но мы не ограничены статусными кодами и, как и в MVC, можем использовать для валидации объект ModelState.


В прошлых темах мы работали с моделью User. Теперь добавим в нее атрибуты валидации:

```

using System;
using System.ComponentModel.DataAnnotations;

namespace WebAPIApp.Models
{
 public class User
 {
 public int Id { get; set; }
 [Required(ErrorMessage = "Укажите имя пользователя")]
 public string Name { get; set; }
 [Range(1, 100, ErrorMessage = "Возраст должен быть в промежутке от 1 до 100")]
 [Required(ErrorMessage = "Укажите возраст пользователя")]
 public int Age { get; set; }
 }
}

```


Поскольку изменилось определение модели, выполним миграцию базы данных.


Далее добавим в код контроллера валидацию. Для этого изменим метод, обрабатывающий запросы POST:

```

using System.Collections.Generic;
using System.Linq;
using Microsoft.EntityFrameworkCore;
using Microsoft.AspNetCore.Mvc;
using WebAPIApp.Models;
using System.Threading.Tasks;

namespace WebAPIApp.Controllers
{
 [ApiController]
 [Route("api/[controller]")]
 public class UsersController : ControllerBase
 {
 UsersContext db;
 public UsersController(UsersContext context)
 {
 db = context;
 if (!db.Users.Any())
 {
 db.Users.Add(new User { Name = "Tom", Age = 26 });
 db.Users.Add(new User { Name = "Alice", Age = 31 });
 db.SaveChanges();
 }
 }

 [HttpGet]
 public async Task<ActionResult<IEnumerable<User>>> Get()
 {
 return await db.Users.ToListAsync();
 }

 // GET api/users/5
 [HttpGet("{id}")]
 public async Task<ActionResult<User>> Get(int id)
 {
 User user = await db.Users.FirstOrDefaultAsync(x => x.Id == id);
 if (user == null)
 return NotFound();
 return new ObjectResult(user);
 }

 // POST api/users
 [HttpPost]
 public async Task<ActionResult<User>> Post(User user)
 {
 // обработка частных случаев валидации
 if (user.Age == 99)
 ModelState.AddModelError("Age", "Возраст не должен быть равен 99");

 if (user.Name == "admin")
 {
 ModelState.AddModelError("Name", "Недопустимое имя пользователя - admin");
 }
 // если есть лшибки - возвращаем ошибку 400
 if (!ModelState.IsValid)
 return BadRequest(ModelState);

 // если ошибок нет, сохраняем в базу данных
 db.Users.Add(user);
 await db.SaveChangesAsync();
 return Ok(user);
 }
 // остальные методы
 }
}

```


С помощью объекта ModelState здесь валидируется полученная модель User. Но кроме проверки свойства ModelState.IsValid мы также можем добавить и еще дополнительные проверки. Например:

```

if (user.Name == "admin")
{
 ModelState.AddModelError("Name", "Недопустимое имя пользователя - admin");
}

```


Для добавления дополнительной ошибки используется метод `ModelState.AddModelError`, первый параметр которого - ключ ошибки, а второй -
сообщение об ошибке. В качестве ключа мы можем использовать любое значение, но по умолчанию система сохраняет все ошибки свойств модели по ключу
"Название_свойства". Поэтому все ошибки, связанные со свойством Name, сохраняются по ключу "Name". Причем по одному ключу мы можем указать множество ошибок.


Все ошибки валидаци сохраняются в объекте ModelState, который передается в метод `BadRequest` и, таким образом, отправляется клиенту вместе с ошибкой 400.


Теперь рассмотрим, как мы можем получить эти ошибки на стороне клиента. Изменим код веб-страницы index.html следующим образом:

```

<!DOCTYPE html>
<html>
<head>
 <meta charset="utf-8" />
 <meta name="viewport" content="width=device-width" />
 <title>Список пользователей</title>
 <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.0/css/bootstrap.min.css" rel="stylesheet" />
</head>
<body>
 <h2>Список пользователей</h2>
 <div id="errors" class="alert alert-danger" style="display:none;"></div>
 <form name="userForm">
 <input type="hidden" name="id" value="0" />
 <div class="form-group col-md-5">
 <label for="name">Имя:</label>
 <input class="form-control" name="name" />
 </div>
 <div class="form-group col-md-5">
 <label for="age">Возраст:</label>
 <input class="form-control" name="age" type="number" />
 </div>
 <div class="panel-body">
 <button type="submit" id="submit" class="btn btn-primary">Сохранить</button>
 <a id="reset" class="btn btn-primary">Сбросить</a>
 </div>
 </form>
 <table class="table table-condensed table-striped col-md-6">
 <thead><tr><th>Id</th><th>Имя</th><th>возраст</th><th></th></tr></thead>
 <tbody>
 </tbody>
 </table>
 <div>2019 © Metanit.com</div>
 <script>
 // Получение всех пользователей
 async function GetUsers() {
 // отправляет запрос и получаем ответ
 const response = await fetch("/api/users", {
 method: "GET",
 headers: { "Accept": "application/json" }
 });
 // если запрос прошел нормально
 if (response.ok === true) {
 // получаем данные
 const users = await response.json();
 let rows = document.querySelector("tbody");
 users.forEach(user => {
 // добавляем полученные элементы в таблицу
 rows.append(row(user));
 });
 }
 }
 // Получение одного пользователя
 async function GetUser(id) {
 const response = await fetch("/api/users/" + id, {
 method: "GET",
 headers: { "Accept": "application/json" }
 });
 if (response.ok === true) {
 const user = await response.json();
 const form = document.forms["userForm"];
 form.elements["id"].value = user.id;
 form.elements["name"].value = user.name;
 form.elements["age"].value = user.age;
 }
 }
 // Добавление пользователя
 async function CreateUser(userName, userAge) {

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
 reset();
 document.querySelector("tbody").append(row(user));
 }
 else {
 const errorData = await response.json();
 console.log("errors", errorData);
 if (errorData) {
 // ошибки вследствие валидации по атрибутам
 if (errorData.errors) {
 if (errorData.errors["Name"]) {
 addError(errorData.errors["Name"]);
 }
 if (errorData.errors["Age"]) {
 addError(errorData.errors["Age"]);
 }
 }
 // кастомные ошибки, определенные в контроллере
 // добавляем ошибки свойства Name
 if (errorData["Name"]) {
 addError(errorData["Name"]);
 }

 // добавляем ошибки свойства Age
 if (errorData["Age"]) {
 addError(errorData["Age"]);
 }
 }

 document.getElementById("errors").style.display = "block";
 }
 }
 // Изменение пользователя
 async function EditUser(userId, userName, userAge) {
 const response = await fetch("api/users", {
 method: "PUT",
 headers: { "Accept": "application/json", "Content-Type": "application/json" },
 body: JSON.stringify({
 id: parseInt(userId, 10),
 name: userName,
 age: parseInt(userAge, 10)
 })
 });
 if (response.ok === true) {
 const user = await response.json();
 reset();
 document.querySelector("tr[data-rowid='" + user.id + "']").replaceWith(row(user));
 }
 }
 // Удаление пользователя
 async function DeleteUser(id) {
 const response = await fetch("/api/users/" + id, {
 method: "DELETE",
 headers: { "Accept": "application/json" }
 });
 if (response.ok === true) {
 const user = await response.json();
 document.querySelector("tr[data-rowid='" + user.id + "']").remove();
 }
 }

 // сброс формы
 function reset() {
 const form = document.forms["userForm"];
 form.reset();
 form.elements["id"].value = 0;
 }
 function addError(errors) {
 errors.forEach(error => {
 const p = document.createElement("p");
 p.append(error);
 document.getElementById("errors").append(p);
 });
 }
 // создание строки для таблицы
 function row(user) {

 const tr = document.createElement("tr");
 tr.setAttribute("data-rowid", user.id);

 const idTd = document.createElement("td");
 idTd.append(user.id);
 tr.append(idTd);

 const nameTd = document.createElement("td");
 nameTd.append(user.name);
 tr.append(nameTd);

 const ageTd = document.createElement("td");
 ageTd.append(user.age);
 tr.append(ageTd);

 const linksTd = document.createElement("td");

 const editLink = document.createElement("a");
 editLink.setAttribute("data-id", user.id);
 editLink.setAttribute("style", "cursor:pointer;padding:15px;");
 editLink.append("Изменить");
 editLink.addEventListener("click", e => {

 e.preventDefault();
 GetUser(user.id);
 });
 linksTd.append(editLink);

 const removeLink = document.createElement("a");
 removeLink.setAttribute("data-id", user.id);
 removeLink.setAttribute("style", "cursor:pointer;padding:15px;");
 removeLink.append("Удалить");
 removeLink.addEventListener("click", e => {

 e.preventDefault();
 DeleteUser(user.id);
 });

 linksTd.append(removeLink);
 tr.appendChild(linksTd);

 return tr;
 }
 // сброс значений формы
 document.getElementById("reset").addEventListener("click", function (e) {

 e.preventDefault();
 reset();
 })

 // отправка формы
 document.forms["userForm"].addEventListener("submit", e => {
 e.preventDefault();
 document.getElementById("errors").innerHTML="";
 document.getElementById("errors").style.display = "none";

 const form = document.forms["userForm"];
 const id = form.elements["id"].value;
 const name = form.elements["name"].value;
 const age = form.elements["age"].value;
 if (id == 0)
 CreateUser(name, age);
 else
 EditUser(id, name, age);
 });

 // загрузка пользователей
 GetUsers();

 </script>
</body>
</html>

```


Для вывода ошибок здесь определен специальный блок с `id="errors"`. При получении ошибки в функции `CreateUser()`
мы получаем данные, посланные через объект ModelState.

```

if (errorData) {
 const errorData = await response.json();
 console.log("errors", errorData);
 (errorData) {
 // ошибки вследствие валидации по атрибутам
 if (errorData.errors) {
 if (errorData.errors["Name"]) {
 addError(errorData.errors["Name"]);
 }
 if (errorData.errors["Age"]) {
 addError(errorData.errors["Age"]);
 }
 }
 // кастомные ошибки, определенные в контроллере
 // добавляем ошибки свойства Name
 if (errorData["Name"]) {
 addError(errorData["Name"]);
 }
 // добавляем ошибки свойства Age
 if (errorData["Age"]) {
 addError(errorData["Age"]);
 }
 }
 document.getElementById("errors").style.display = "block";
}

```


Но чтобы обратиться к ошибкам, надо пройти несколько уровней вложенности. Ошибки, которые добавляются в результате применения правил атрибутов валидации,
можно получить из объекта `errorData.errors`. Например, чтобы получить ошибки свойства Age, придется использовать вызов
`errorData.errors["Age"]`. Получение сообщения об ошибках, которые были определены в контроллере, производится непосредственно из
посланного объекта `errorData.["Age"]`. Причем каждый из таких вызовов представляет собой массив.


И теперь если мы введем некорретные данные, мы получим сообщения об ошибках.
![Валидация в ASP.NET Core Web API](https://metanit.com./pics/webapi17.png)










- Глава 1. Введение в ASP.NET Core


 - [ASP.NET Core - новая эпоха в развитии ASP.NET](//metanit.com/sharp/aspnet5/1.1.php)

 - [Начало работы с ASP.NET Core](//metanit.com/sharp/aspnet5/1.2.php)

 - [Проект ASP.NET Core в Visual Studio for Mac](//metanit.com/sharp/aspnet5/1.3.php)



- Глава 2. Основы ASP.NET Core


 - [Запуск приложения. Класс Program](//metanit.com/sharp/aspnet5/2.13.php)

 - [Класс Startup](//metanit.com/sharp/aspnet5/2.1.php)

 - [Конвейер обработки запроса и middleware](//metanit.com/sharp/aspnet5/2.2.php)

 - [Методы Use, Run и делегат RequestDelegate](//metanit.com/sharp/aspnet5/2.3.php)

 - [Методы Map и MapWhen](//metanit.com/sharp/aspnet5/2.22.php)

 - [Создание компонентов middleware](//metanit.com/sharp/aspnet5/2.4.php)

 - [Конвейер обработки запроса](//metanit.com/sharp/aspnet5/2.18.php)

 - [IWebHostEnvironment и окружение](//metanit.com/sharp/aspnet5/2.21.php)

 - [Статические файлы](//metanit.com/sharp/aspnet5/2.5.php)

 - [Работа со статическими файлами](//metanit.com/sharp/aspnet5/2.14.php)

 - [Обработка ошибок](//metanit.com/sharp/aspnet5/17.1.php)

 - [Работа с HTTPS](//metanit.com/sharp/aspnet5/18.6.php)



- Глава 3. Сервисы и Dependency Injection


 - [Сервисы и метод ConfigureServices](//metanit.com/sharp/aspnet5/6.1.php)

 - [Создание своих сервисов](//metanit.com/sharp/aspnet5/2.19.php)

 - [Передача зависимостей](//metanit.com/sharp/aspnet5/6.4.php)

 - [Жизненный цикл зависимостей](//metanit.com/sharp/aspnet5/6.2.php)

 - [Применение сервисов в middleware](//metanit.com/sharp/aspnet5/2.20.php)

 - [Singleton-объекты и scoped-сервисы](//metanit.com/sharp/aspnet5/6.5.php)



- Глава 4. Конфигурация


 - [Основы конфигурации](//metanit.com/sharp/aspnet5/2.6.php)

 - [Нефайловые провайдеры конфигурации](//metanit.com/sharp/aspnet5/2.16.php)

 - [Файловые провайдеры конфигурации](//metanit.com/sharp/aspnet5/2.12.php)

 - [Объединение конфигураций и установка сервиса IConfiguration](//metanit.com/sharp/aspnet5/2.23.php)

 - [Работа с конфигурацией](//metanit.com/sharp/aspnet5/2.17.php)

 - [Создание провайдера конфгурации](//metanit.com/sharp/aspnet5/2.15.php)

 - [Проекция конфигурации на классы](//metanit.com/sharp/aspnet5/2.9.php)

 - [Передача конфигурации через IOptions](//metanit.com/sharp/aspnet5/6.3.php)



- Глава 5. Состояние приложения. Куки. Сессии


 - [HttpContext.Items](//metanit.com/sharp/aspnet5/2.11.php)

 - [Куки](//metanit.com/sharp/aspnet5/2.25.php)

 - [Сессии](//metanit.com/sharp/aspnet5/2.26.php)



- Глава 6. Логгирование


 - [Ведение лога и ILogger](//metanit.com/sharp/aspnet5/2.10.php)

 - [Фабрика логгера и провайдеры логгирования](//metanit.com/sharp/aspnet5/2.29.php)

 - [Конфигурация и фильтрация логгирования](//metanit.com/sharp/aspnet5/2.28.php)

 - [Создание провайдера логгирования](//metanit.com/sharp/aspnet5/2.27.php)



- Глава 7. Маршрутизация


 - [Основы маршрутизации в ASP.NET Core](//metanit.com/sharp/aspnet5/11.1.php)

 - [RouterMiddleware](//metanit.com/sharp/aspnet5/11.12.php)

 - [Определение маршрутов](//metanit.com/sharp/aspnet5/11.2.php)

 - [Работа с маршрутами](//metanit.com/sharp/aspnet5/11.4.php)

 - [Ограничения маршрутов](//metanit.com/sharp/aspnet5/11.3.php)

 - [Создание ограничений маршрутов](//metanit.com/sharp/aspnet5/11.7.php)

 - [Создание своего маршрута](//metanit.com/sharp/aspnet5/11.8.php)



- Глава 8. ASP.NET Core MVC


 - [Введение в ASP.NET Core MVC](//metanit.com/sharp/aspnet5/3.1.php)

 - [Добавление MVC в пустой проект](//metanit.com/sharp/aspnet5/3.6.php)

 - [Первое приложение. Добавление моделей и базы данных](//metanit.com/sharp/aspnet5/3.2.php)

 - [Создание контроллера и инициализатора базы данных](//metanit.com/sharp/aspnet5/3.3.php)

 - [Добавление методов контроллера и представлений](//metanit.com/sharp/aspnet5/3.4.php)

 - [Добавление мастер-страницы и стилизации](//metanit.com/sharp/aspnet5/3.5.php)



- Глава 9. Контроллеры


 - [Контроллеры и их действия](//metanit.com/sharp/aspnet5/5.1.php)

 - [Передача данных в контроллер](//metanit.com/sharp/aspnet5/5.2.php)

 - [Результаты действий](//metanit.com/sharp/aspnet5/5.3.php)

 - [ContentResult и JsonResult](//metanit.com/sharp/aspnet5/5.4.php)

 - [Переадресация](//metanit.com/sharp/aspnet5/5.5.php)

 - [Отправка статусных кодов](//metanit.com/sharp/aspnet5/5.6.php)

 - [Отправка файлов](//metanit.com/sharp/aspnet5/5.7.php)

 - [Переопределение контроллеров](//metanit.com/sharp/aspnet5/5.8.php)

 - [Контекст контроллера](//metanit.com/sharp/aspnet5/5.9.php)

 - [Передача зависимостей в контроллер](//metanit.com/sharp/aspnet5/5.10.php)



- Глава 10. Представления


 - [Введение в представления](//metanit.com/sharp/aspnet5/7.1.php)

 - [Движок представлений Razor](//metanit.com/sharp/aspnet5/7.2.php)

 - [Передача данных в представление](//metanit.com/sharp/aspnet5/7.3.php)

 - [Мастер-страницы](//metanit.com/sharp/aspnet5/7.4.php)

 - [Файл _ViewImports.cshtml](//metanit.com/sharp/aspnet5/7.9.php)

 - [Частичные представления](//metanit.com/sharp/aspnet5/7.5.php)

 - [Внедрение зависимостей в представления](//metanit.com/sharp/aspnet5/7.7.php)

 - [Работа с формами](//metanit.com/sharp/aspnet5/7.8.php)

 - [Создание движка представлений](//metanit.com/sharp/aspnet5/7.10.php)



- Глава 11. Маршрутизация в ASP.NET Core MVC


 - [Маршрутизация в MVC с помощью конечных точек](//metanit.com/sharp/aspnet5/11.5.php)

 - [Маршрутизация с помощью RouterMiddleware. Метод UseMvc](//metanit.com/sharp/aspnet5/11.13.php)

 - [Атрибуты маршрутизации](//metanit.com/sharp/aspnet5/11.6.php)

 - [Области](//metanit.com/sharp/aspnet5/11.9.php)



- Глава 12. Модели


 - [Модели в ASP.NET Core MVC](//metanit.com/sharp/aspnet5/8.1.php)

 - [Модели представления View Model](//metanit.com/sharp/aspnet5/8.2.php)

 - [Привязка модели](//metanit.com/sharp/aspnet5/8.3.php)

 - [Передача данных в контроллер](//metanit.com/sharp/aspnet5/8.4.php)

 - [Управление привязкой](//metanit.com/sharp/aspnet5/8.5.php)

 - [Создание привязчика модели](//metanit.com/sharp/aspnet5/8.6.php)



- Глава 13. HTML-хелперы


 - [Создание HTML-хелперов](//metanit.com/sharp/aspnet5/9.1.php)

 - [HTML-хелперы элементов форм](//metanit.com/sharp/aspnet5/9.2.php)

 - [Строго типизированные хелперы](//metanit.com/sharp/aspnet5/9.3.php)

 - [Шаблонные хелперы](//metanit.com/sharp/aspnet5/9.4.php)

 - [Генерация ссылок](//metanit.com/sharp/aspnet5/9.5.php)

 - [URL-хелперы](//metanit.com/sharp/aspnet5/11.11.php)



- Глава 14. Tag-хелперы


 - [Введение в tag-хелперы](//metanit.com/sharp/aspnet5/10.1.php)

 - [AnchorTagHelper](//metanit.com/sharp/aspnet5/10.2.php)

 - [LinkTagHelper и ScriptTagHelper](//metanit.com/sharp/aspnet5/10.3.php)

 - [Tag-хелперы форм](//metanit.com/sharp/aspnet5/10.4.php)

 - [EnvironmentTagHelper](//metanit.com/sharp/aspnet5/10.6.php)

 - [CacheTagHelper](//metanit.com/sharp/aspnet5/10.7.php)

 - [Создание tag-хелперов](//metanit.com/sharp/aspnet5/10.8.php)

 - [Управление выводом tag-хелпера](//metanit.com/sharp/aspnet5/10.10.php)

 - [Контекст хелпера и получение зависимостей](//metanit.com/sharp/aspnet5/10.11.php)

 - [Атрибут HtmlTargetElement](//metanit.com/sharp/aspnet5/10.12.php)

 - [Tag-хелперы и сложные объекты и коллекции](//metanit.com/sharp/aspnet5/10.9.php)



- Глава 15. View Component


 - [Определение компонента представлений](//metanit.com/sharp/aspnet5/7.6.php)

 - [Передача данных в View Component](//metanit.com/sharp/aspnet5/7.11.php)

 - [Генерация контента в View Component](//metanit.com/sharp/aspnet5/7.12.php)

 - [ViewViewComponentResult и представления](//metanit.com/sharp/aspnet5/7.13.php)

 - [Асинхронные операции в View Component](//metanit.com/sharp/aspnet5/7.14.php)

 - [ViewComponentContext](//metanit.com/sharp/aspnet5/7.15.php)



- Глава 16. Метаданные и валидация модели


 - [Основы валидации](//metanit.com/sharp/aspnet5/19.1.php)

 - [Атрибуты валидации](//metanit.com/sharp/aspnet5/19.2.php)

 - [Валидация на стороне сервера](//metanit.com/sharp/aspnet5/19.3.php)

 - [Валидация на стороне клиента](//metanit.com/sharp/aspnet5/19.4.php)

 - [Tag-хелперы валидации](//metanit.com/sharp/aspnet5/10.5.php)

 - [Создание атрибута валидации. Самовалидация модели](//metanit.com/sharp/aspnet5/19.5.php)

 - [Аннотации данных](//metanit.com/sharp/aspnet5/19.6.php)



- Глава 17. Работа с данными в Entity Framework в MVC


 - [Подключение и создание базы данных в Entity Framework Core](//metanit.com/sharp/aspnet5/12.1.php)

 - [Операции с моделями. Создание и вывод](//metanit.com/sharp/aspnet5/12.2.php)

 - [Операции с моделями. Редактирование и удаление](//metanit.com/sharp/aspnet5/12.3.php)

 - [Сортировка](//metanit.com/sharp/aspnet5/12.4.php)

 - [Создание tag-хелпера сортировки](//metanit.com/sharp/aspnet5/12.5.php)

 - [Фильтрация](//metanit.com/sharp/aspnet5/12.6.php)

 - [Постраничная навигация](//metanit.com/sharp/aspnet5/12.7.php)

 - [Tag-хелпер для постраничной навигации](//metanit.com/sharp/aspnet5/12.8.php)

 - [Объединение сортировки, фильтрации и пагинации](//metanit.com/sharp/aspnet5/12.9.php)

 - [Tag-хелпер пагинации с сортировкой и фильтрацией](//metanit.com/sharp/aspnet5/12.10.php)



- Глава 18. Razor Pages


 - [Введение в Razor Pages](//metanit.com/sharp/aspnet5/29.1.php)

 - [Добавление RazorPages в пустой проект](//metanit.com/sharp/aspnet5/29.2.php)

 - [Обработка запросов. Передача форм](//metanit.com/sharp/aspnet5/29.3.php)

 - [Привязка свойств RazorPage к параметрам запроса](//metanit.com/sharp/aspnet5/29.4.php)

 - [Параметры маршрутов в Razor Pages](//metanit.com/sharp/aspnet5/29.5.php)

 - [Обработчики страницы](//metanit.com/sharp/aspnet5/29.6.php)

 - [Возвращение результата](//metanit.com/sharp/aspnet5/29.7.php)

 - [Переадресация и создание ссылок](//metanit.com/sharp/aspnet5/29.8.php)

 - [Подключение к базе данных](//metanit.com/sharp/aspnet5/29.9.php)

 - [Создание и вывод объектов из базы данных](//metanit.com/sharp/aspnet5/29.10.php)

 - [Изменение и удаление в базе данных](//metanit.com/sharp/aspnet5/29.11.php)



- Глава 19. Web API


 - [Введение в Web API](//metanit.com/sharp/aspnet5/23.1.php)

 - [Создание контроллера](//metanit.com/sharp/aspnet5/23.2.php)

 - [Тестирование контроллера](//metanit.com/sharp/aspnet5/23.3.php)

 - [Создание клиента для WEB API](//metanit.com/sharp/aspnet5/23.4.php)

 - [Валидация в Web API](//metanit.com/sharp/aspnet5/23.5.php)

 - [Content negotiation](//metanit.com/sharp/aspnet5/23.6.php)



- Глава 20. Фильтры


 - [Введение в фильтры](//metanit.com/sharp/aspnet5/18.1.php)

 - [Передача параметров в фильтры и установка зависимостей](//metanit.com/sharp/aspnet5/18.5.php)

 - [Фильтры ресурсов](//metanit.com/sharp/aspnet5/18.2.php)

 - [Фильтры действий](//metanit.com/sharp/aspnet5/18.3.php)

 - [Фильтры результатов](//metanit.com/sharp/aspnet5/18.4.php)

 - [Фильтры исключений](//metanit.com/sharp/aspnet5/17.2.php)

 - [Фильтры RazorPages](//metanit.com/sharp/aspnet5/18.7.php)



- Глава 21. Аутентификация и авторизация


 - [Аутентификация на основе куки. Часть 1](//metanit.com/sharp/aspnet5/15.1.php)

 - [Аутентификация на основе куки. Часть 2](//metanit.com/sharp/aspnet5/15.2.php)

 - [Авторизация](//metanit.com/sharp/aspnet5/15.3.php)

 - [ClaimPrincipal и объекты Claim](//metanit.com/sharp/aspnet5/15.4.php)

 - [Авторизация по ролям](//metanit.com/sharp/aspnet5/15.5.php)

 - [Авторизация на основе Claims](//metanit.com/sharp/aspnet5/15.6.php)

 - [Пример авторизации на основе Claims](//metanit.com/sharp/aspnet5/15.7.php)

 - [Создание ограничений для политики авторизации](//metanit.com/sharp/aspnet5/15.8.php)

 - [JWT-токены](//metanit.com/sharp/aspnet5/23.7.php)



- Глава 22. ASP.NET Core Identity


 - [Введение в ASP.NET Core Identity](//metanit.com/sharp/aspnet5/16.1.php)

 - [Основные классы в ASP.NET Core Identity](//metanit.com/sharp/aspnet5/16.11.php)

 - [Добавление Identity в проект с нуля](//metanit.com/sharp/aspnet5/16.2.php)

 - [Регистрация и создание пользователей в Identity](//metanit.com/sharp/aspnet5/16.3.php)

 - [Авторизация пользователей в Identity](//metanit.com/sharp/aspnet5/16.4.php)

 - [Управление пользователями](//metanit.com/sharp/aspnet5/16.7.php)

 - [Изменение пароля](//metanit.com/sharp/aspnet5/16.8.php)

 - [Валидация пароля](//metanit.com/sharp/aspnet5/16.9.php)

 - [Валидация пользователя](//metanit.com/sharp/aspnet5/16.10.php)

 - [Управление ролями](//metanit.com/sharp/aspnet5/16.13.php)

 - [Инициализация БД ролями и пользователями](//metanit.com/sharp/aspnet5/16.12.php)



- Глава 23. Клиентская разработка


 - [Бандлинг и минификация](//metanit.com/sharp/aspnet5/13.6.php)

 - [Менеджер Libman](//metanit.com/sharp/aspnet5/13.7.php)

 - [Пакетный менеджер NPM](//metanit.com/sharp/aspnet5/13.5.php)

 - [Gulp](//metanit.com/sharp/aspnet5/13.1.php)

 - [Grunt](//metanit.com/sharp/aspnet5/13.2.php)

 - [Препроцессоры Less и Sass](//metanit.com/sharp/aspnet5/13.4.php)



- Глава 24. Производительность и кэширование


 - [Кэширование с помощью MemoryCache](//metanit.com/sharp/aspnet5/14.1.php)

 - [Атрибут ResponseCache](//metanit.com/sharp/aspnet5/14.2.php)

 - [Сжатие ответа](//metanit.com/sharp/aspnet5/14.3.php)

 - [Кэширование статических файлов](//metanit.com/sharp/aspnet5/14.4.php)



- Глава 25. Сервер и публикация приложения


 - [Сервер](//metanit.com/sharp/aspnet5/2.7.php)

 - [Публикация на IIS](//metanit.com/sharp/aspnet5/20.1.php)

 - [Установка приложения в виде службы Windows](//metanit.com/sharp/aspnet5/20.2.php)



- Глава 26. Тестирование


 - [Введение в юнит-тесты](//metanit.com/sharp/aspnet5/22.1.php)

 - [Создание проекта юнит-тестов. Добавление xUnit](//metanit.com/sharp/aspnet5/22.2.php)

 - [Создание юнит-тестов](//metanit.com/sharp/aspnet5/22.3.php)

 - [Фреймворк Moq и moq-объекты](//metanit.com/sharp/aspnet5/22.4.php)

 - [Тестирование контроллера](//metanit.com/sharp/aspnet5/22.5.php)



- Глава 27. URL Rewriting


 - [Введение в URL Rewriting](//metanit.com/sharp/aspnet5/24.1.php)

 - [Правила IIS для URL Rewriting](//metanit.com/sharp/aspnet5/24.2.php)

 - [Применение правил для Apache](//metanit.com/sharp/aspnet5/24.3.php)

 - [Создание правил URL Rewriting](//metanit.com/sharp/aspnet5/24.4.php)



- Глава 28. Глобализация и локализация


 - [Определение культуры](//metanit.com/sharp/aspnet5/28.1.php)

 - [RequestLocalizationMiddleware](//metanit.com/sharp/aspnet5/28.2.php)

 - [Локализация строк. IStringLocalizer](//metanit.com/sharp/aspnet5/28.3.php)

 - [Ресурсы и локализация в контроллерах](//metanit.com/sharp/aspnet5/28.4.php)

 - [Локализация представлений](//metanit.com/sharp/aspnet5/28.5.php)

 - [Локализация аннотаций данных](//metanit.com/sharp/aspnet5/28.6.php)

 - [Переключение языка приложения](//metanit.com/sharp/aspnet5/28.7.php)

 - [Общие ресурсы локализации](//metanit.com/sharp/aspnet5/28.8.php)

 - [Хранение ресурсов в базе данных](//metanit.com/sharp/aspnet5/28.9.php)



- Глава 29. SignalR Core


 - [SignalR Core. Первое приложение](//metanit.com/sharp/aspnet5/30.1.php)

 - [Создание и конфигурация хабов](//metanit.com/sharp/aspnet5/30.2.php)

 - [Клиент javascript](//metanit.com/sharp/aspnet5/30.3.php)

 - [Контекст хаба, подключение и отключение клиентов](//metanit.com/sharp/aspnet5/30.4.php)

 - [Взаимодействие с клиентами](//metanit.com/sharp/aspnet5/30.5.php)

 - [IHubContext](//metanit.com/sharp/aspnet5/30.6.php)

 - [Отправка сложных объектов](//metanit.com/sharp/aspnet5/30.7.php)

 - [Аутентификация и авторизация на основе куки](//metanit.com/sharp/aspnet5/30.8.php)

 - [Аутентификация и авторизация с помощью токенов](//metanit.com/sharp/aspnet5/30.9.php)

 - [Пользователи](//metanit.com/sharp/aspnet5/30.10.php)

 - [Группы](//metanit.com/sharp/aspnet5/30.11.php)

 - [Клиент на Xamarin Forms](//metanit.com/sharp/aspnet5/30.12.php)



- Глава 30. CORS и кросс-доменные запросы


 - [Начало работы с CORS](//metanit.com/sharp/aspnet5/31.1.php)

 - [Конфигурация CORS](//metanit.com/sharp/aspnet5/31.2.php)

 - [Политики CORS](//metanit.com/sharp/aspnet5/31.3.php)

 - [Глобальная и локальная настройка CORS](//metanit.com/sharp/aspnet5/31.5.php)

 - [CORS в MVC](//metanit.com/sharp/aspnet5/31.4.php)



- Глава 31. Dapper


 - [Работа с Dapper в ASP.NET Core](//metanit.com/sharp/aspnet5/26.1.php)



- Глава 32. React.JS


 - [Подключение React в ASP.NET Core](//metanit.com/sharp/aspnet5/25.1.php)

 - [Взаимодействие React.JS и ASP.NET Core](//metanit.com/sharp/aspnet5/25.2.php)



- Глава 33. Дополнительные статьи


 - [Отправка email в ASP.NET Core](//metanit.com/sharp/aspnet5/21.1.php)

 - [Загрузка файлов на сервер](//metanit.com/sharp/aspnet5/21.3.php)










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

**Источник:** [https://metanit.com/sharp/aspnet5/23.5.php](https://metanit.com/sharp/aspnet5/23.5.php)
