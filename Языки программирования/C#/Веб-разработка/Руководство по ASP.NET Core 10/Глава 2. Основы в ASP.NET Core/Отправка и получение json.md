# Отправка и получение json

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10|Руководство по ASP.NET Core 10]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 2. Основы в ASP.NET Core|Глава 2. Основы в ASP.NET Core]] / Отправка и получение json

[[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 2. Основы в ASP.NET Core/Переадресация|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 2. Основы в ASP.NET Core|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 2. Основы в ASP.NET Core/Создание простейшего API|Вперёд]]

**Дата написания:** 05.09.2026

## Отправка и получение json

Последнее обновление: 15.05.2022




-

-

-














JSON является распространенным форматом для передачи данных. Рассмотрим, как мы можем посылать и получить данные json.


### Отправка JSON. Метод WriteAsJsonAsync


Для отправки json можно воспользоваться методом WriteAsJson()/WriteAsJsonAsync() объекта HttpResponse.
Этот метод позволяет сериализовать переданные в него объекты в формат JSON и автоматически для заголовка "content-type" устанавливает значение "application/json; charset=utf-8":

```

var builder = WebApplication.CreateBuilder();
var app = builder.Build();

app.Run(async (context) =>
{
 Person tom = new("Tom", 22);
 await context.Response.WriteAsJsonAsync(tom);
});

app.Run();

public record Person(string Name, int Age);

```


В данном случае клиенту отправляется объект типа Person, который представляет класс-record, однако это может быть и обычный класс:
![Отправка json с помощью WriteAsJson в ASP.NET Core и C#](https://metanit.com./pics/2.10.png)


Хотя можно было бы воспользоваться и стандартным методом `WriteAsync()`:

```

app.Run(async (context) =>
{
 var response = context.Response;
 response.Headers.ContentType = "application/json; charset=utf-8";
 await response.WriteAsync("{\"name\":\"Tom\",\"age\":37}");
});

```


### Получение JSON. Метод ReadFromJsonAsync


Для получения из запроса объект в формате JSON в классе HttpRequest определен метод ReadFromJsonAsync(). Он позволяет сериализовать данные в объект
определенного типа.


Например, создадим в проекте папку html, в которой определим новый файл index.html.
![Отправка объекта json на сервер ASP.NET Core в C#](https://metanit.com./pics/2.31.png)


В файле index.html определим следующий код:

```

<!DOCTYPE html>
<html>
<head>
 <meta charset="utf-8" />
 <title>METANIT.COM</title>
</head>
<body>
 <h2>User form</h2>
 <div id="message"></div>
 <div>
 <p>Name: <br />
 <input name="userName" id="userName" />
 </p>
 <p>Age: <br />
 <input name="userAge" id="userAge" type="number" />
 </p>
 <button id="sendBtn">Send</button>
 </div>
 <script>
 document.getElementById("sendBtn").addEventListener("click", send);
 async function send() {
 const response = await fetch("/api/user", {
 method: "POST",
 headers: { "Accept": "application/json", "Content-Type": "application/json" },
 body: JSON.stringify({
 name: document.getElementById("userName").value,
 age: document.getElementById("userAge").value
 })
 });
 const message = await response.json();
 document.getElementById("message").innerText = message.text;
 }
 </script>
</body>
</html>

```


Здесь по нажатию на кнопку с помощью функции fetch() по адресу "/api/user" будет отправляться объект со свойствами name и age,
значения для которых берутся из полей формы. В ответ от сервера веб-страница также получает объект в формате json, в котором имеется свойство `text` -
свойство, которое хранит сообщение от сервера.


Теперь в файле Program.cs определим код для получения данных, отправляемых веб-страницей:

```

var builder = WebApplication.CreateBuilder();
var app = builder.Build();

app.Run(async (context) =>
{
 var response = context.Response;
 var request = context.Request;
 if (request.Path == "/api/user")
 {
 var message = "Некорректные данные"; // содержание сообщения по умолчанию
 try
 {
 // пытаемся получить данные json
 var person = await request.ReadFromJsonAsync<Person>();
 if (person != null) // если данные сконвертированы в Person
 message = $"Name: {person.Name} Age: {person.Age}";
 }
 catch { }
 // отправляем пользователю данные
 await response.WriteAsJsonAsync(new { text = message });
 }
 else
 {
 response.ContentType = "text/html; charset=utf-8";
 await response.SendFileAsync("html/index.html");
 }
});

app.Run();

public record Person(string Name, int Age);

```


В данном случае, если обращение идет по адресу "/api/user", то получаем данные в формате json. При обращениях по другим адресам просто посылаем
веб-страницу index.html.


Метод ReadFromJsonAsync() десериализует полученные данные в объект определенного типа - в данном случае типа Person:

```

var person = await request.ReadFromJsonAsync<Person>();
if (person != null) // если данные сконвертированы в Person
 message = $"Name: {person.Name} Age: {person.Age}";

```


Таким образом, здесь результат вызова этого метода - значение переменной person будет представлять объект Person.


Но стоит отметить, что если данные запроса не представляют объект JSON, либо если метод ReadFromJsonAsync() не смог связать данные запроса со свойствами
класса Person, то вызов этого метода сгенерирует исключение. Поэтому в данном случае вызов метода помещается в конструкцию try..catch. Однако нельзя не отметить,
что try..catch здесь является узким местом, и далее мы посмотрим, как от него избавиться.


И в конце в ответ посылаем анонимный объект, который также сериализуется в json с некоторым сообщением, которое хранится в свойстве text. При получении этого сообщения оно выводится на веб-страницу.
![ReadFromJsonAsync и чтение данных json в ASP.NET Core и C#](https://metanit.com./pics/2.32.png)


Стоит отметить, что проверять на наличие json в запросе можно с помощью метода HasJsonContentType() - он возвращает
`true`, если клиент прислал json.

```

if (request.HasJsonContentType())
{
 var person = await request.ReadFromJsonAsync<Person>();
 if (person != null)
 responseText = $"Name: {person.Name} Age: {person.Age}";
}

```


### Настройка сериализации


При получении данных в формате json мы можем столкнуться с рядом проблем. Хотя бы взять предыдущий пример, где мы вынуждены были помещать вызов
метода ReadFromJsonAsync в конструкцию - try..catch. Например, если мы не введем в поля формы никаких значений, то стандартный механизм привязки значений
не сможет связать данные запроса со свойством Age. И мы получим исключение.


Аналогичный пример, когда данные json не совсем соответствуют определению типа,
в который надо выполнить десериализацию:

```

const response = await fetch("/api/user", {
 method: "POST",
 headers: { "Accept": "application/json", "Content-Type": "application/json" },
 body: JSON.stringify({
 userName: "Tom",
 userAge: 22
 })
});

```


Здесь названия свойств отправляемого объекта не соответствуют названиям свойств типа Person в C#. Однако объект Person все равно будет создан, просто его свойства получат значения
по умолчанию (null для свойства Name и 0 для свойства Age).


Другой пример - отправляемые данные не соответствуют по типу:

```

const response = await fetch("/api/user", {
 method: "POST",
 headers: { "Accept": "application/json", "Content-Type": "application/json" },
 body: JSON.stringify({
 name: "Tom",
 age: "twenty-two"
 })
});

```


Здесь свойство "age" представляет строку и не сможет быть сконвертировано в значение типа `int`. В итоге при отправке подобных данных на сервере возникнет исключение типа System.Text.Json.JsonException, а
клиент получит информацию об исключении.


В обоих выше приведенных примерах в зависимости от задачи можно использовать различные решения - обрабатывть исключения, встраивать дополнительные middleware для отлова подобных ситуаций и так далее.
Одним из решений подобных проблем также может быть настройка сериализации/десериализации с помощью параметра типа JsonSerializerOptions, которое может передаваться в метод
ReadFromJsonAsync()

```
ReadFromJsonAsync<T>(JsonSerializerOptions options);
```


Так, изменим код файла Program.cs:

```

using System.Text.Json;
using System.Text.Json.Serialization;

var builder = WebApplication.CreateBuilder();
var app = builder.Build();

app.Run(async (context) =>
{
 var response = context.Response;
 var request = context.Request;
 if (request.Path == "/api/user")
 {
 var responseText = "Некорректные данные"; // содержание сообщения по умолчанию

 if (request.HasJsonContentType())
 {
 // определяем параметры сериализации/десериализации
 var jsonoptions = new JsonSerializerOptions();
 // добавляем конвертер кода json в объект типа Person
 jsonoptions.Converters.Add(new PersonConverter());
 // десериализуем данные с помощью конвертера PersonConverter
 var person = await request.ReadFromJsonAsync<Person>(jsonoptions);
 if (person != null)
 responseText = $"Name: {person.Name} Age: {person.Age}";
 }
 await response.WriteAsJsonAsync(new {text = responseText});
 }
 else
 {
 response.ContentType = "text/html; charset=utf-8";
 await response.SendFileAsync("html/index.html");
 }
});

app.Run();

public record Person(string Name, int Age);
public class PersonConverter : JsonConverter<Person>
{
 public override Person Read(ref Utf8JsonReader reader, Type typeToConvert, JsonSerializerOptions options)
 {
 var personName = "Undefined";
 var personAge = 0;
 while (reader.Read())
 {
 if (reader.TokenType == JsonTokenType.PropertyName)
 {
 var propertyName = reader.GetString();
 reader.Read();
 switch (propertyName?.ToLower())
 {
 // если свойство age и оно содержит число
 case "age" when reader.TokenType == JsonTokenType.Number:
 personAge = reader.GetInt32(); // считываем число из json
 break;
 // если свойство age и оно содержит строку
 case "age" when reader.TokenType == JsonTokenType.String:
 string? stringValue = reader.GetString();
 // пытаемся конвертировать строку в число
 if (int.TryParse(stringValue, out int value))
 {
 personAge = value;
 }
 break;
 case "name": // если свойство Name/name
 string? name = reader.GetString();
 if(name!=null)
 personName = name;
 break;
 }
 }
 }
 return new Person(personName, personAge);
 }
 // сериализуем объект Person в json
 public override void Write(Utf8JsonWriter writer, Person person, JsonSerializerOptions options)
 {
 writer.WriteStartObject();
 writer.WriteString("name", person.Name);
 writer.WriteNumber("age", person.Age);

 writer.WriteEndObject();
 }
}

```


Поскольку настройка параметров сериализации/десериализации - это отдельная большая тема, то пройдемся вкратце по коду, который вовлекается в процесс
конвертации и прежде всего по конвертеру Person в json.


#### Определение конвертера для сериализации/десериализации объекта в json


Класс конвертера для сериализации/десериализации объекта определенного типа в JSON должен наследоваться от класса JsonConverter<T>. Абстрактный класс JsonConverter типизируется
типом, для объекта которого надо выполнить сериализацию/десериализацию. В коде выше такой реализацией является класс `PersonConverter`.


При наследовании класса JsonConverter необходимо реализовать его абстрактные методы Read() (выполняет десериализацию из JSON в Person) и
Write() (выполняет сериализацию из Person в JSON).


Метод Write, который записывает данные Person в формат JSON, выглядит относительно просто:

```

public override void Write(Utf8JsonWriter writer, Person person, JsonSerializerOptions options)
{
 writer.WriteStartObject();
 writer.WriteString("name", person.Name);
 writer.WriteNumber("age", person.Age);
 writer.WriteEndObject();
}

```


Он принимает три параметра:


-

Utf8JsonWriter - объект, который записывает данные в json

-

Person - объект, который надо сериализовать

-

JsonSerializerOptions - дополнительные параметры сериализации


Сначала с помощью объекта Utf8JsonWriter открываем запись объекта в формате json:

```
writer.WriteStartObject();
```


Последовательно записываем данные объекта Person:

```

writer.WriteString("name", person.Name);
writer.WriteNumber("age", person.Age);

```


И завершаем запись объекта:

```
writer.WriteEndObject();
```


Чтение или десериализация выглядит несколько сложнее. Метод Read() также принимает три параметра:


-

Utf8JsonReader - объект, который читает данные из json

-

Type - тип, в который надо выполнить конвертацию

-

JsonSerializerOptions - дополнительные параметры сериализации


Результатом метода Read() должен быть десериализованный объект (в данном случае объект типа Person).


В начале определяем данные объекта Person по умолчанию, которые будут применяться, если в процессе десериализации произойдут проблемы:

```

 var personName = "Undefined";
var personAge = 0;

```


Далее в цикле считываем каждый токен в строке json с помощью метода `Read()` объекта Utf8JsonReader:

```
 while (reader.Read())
```


Затем, если считанный токен представляет название свойства, то считываем его и считываем следующий токен:

```

if (reader.TokenType == JsonTokenType.PropertyName)
{
 var propertyName = reader.GetString();
 reader.Read();

```


После этого мы можем узнать, как называется свойство и какое значение оно имеет. Для этого применяем конструкцию switch:

```

switch (propertyName?.ToLower())
{

```


Посольку регистр символов название свойства может отличаться (например, "Age", "age" или "AGE"), то, чтобы упростить сравнение, приводим
название свойства к нижнему регистру.


Например, мы ожидаем, что json будет содержать свойство с именем "age", которое будет хранить некоторое число. Для его получения применяем следующий блок case:

```

case "age" when reader.TokenType == JsonTokenType.Number:
 personAge = reader.GetInt32();
 break;

```


То есть если свойство называется "age" и представляет число (JsonTokenType.Number), то вызываем метод `reader.GetInt32()`


Но свойство "age" также может содержать строку, например, "23". Такая строка может конвертироваться в число. И для подобного случая добавляем
дополнительный блок case:

```

case "age" when reader.TokenType == JsonTokenType.String:
 string? stringValue = reader.GetString();
 if (int.TryParse(stringValue, out int value))
 {
 personAge = value;
 }
 break;

```


Подобным образом считываем из json значение для свойства Name:

```

 case "name":
 string? name = reader.GetString();
 if(name!=null)
 personName = name;

```


В конце полученными данными инициализируем объект Person и возвращаем его из метода:

```
return new Person(personName, personAge);
```


Таким образом, мы можем проверить, какие свойства имеет объект json, какие значения они несут и принять решения, передавать эти значения в объект Person.
И в данном случае, даже если в присланном json не будет нужных свойств, или свойство age будет содержать строку, которая не конвертируется в число, объект Person все равно будет создан.


Чтобы использовать конвертер json, его надо добавить в коллекцию конвертеров:

```

 var jsonoptions = new JsonSerializerOptions();
jsonoptions.Converters.Add(new PersonConverter());
var person = await request.ReadFromJsonAsync<Person>(jsonoptions);

```











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

**Источник:** [https://metanit.com/sharp/aspnet6/2.10.php](https://metanit.com/sharp/aspnet6/2.10.php)
