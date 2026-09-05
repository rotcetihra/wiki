# HttpClient в проекте Blazor WebAssembly

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по Blazor|Руководство по Blazor]] / [[Языки программирования/C#/Веб-разработка/Руководство по Blazor/Глава 5. Отправка http-запросов|Глава 5. Отправка http-запросов]] / HttpClient в проекте Blazor WebAssembly

[[Языки программирования/C#/Веб-разработка/Руководство по Blazor/Глава 5. Отправка http-запросов/HttpClient в проекте Blazor Server|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по Blazor/Глава 5. Отправка http-запросов|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по Blazor/Глава 5. Отправка http-запросов/Взаимодействие приложения Blazor с Web API|Вперёд]]

**Дата написания:** 05.09.2026

## HttpClient в проекте Blazor WebAssembly

Последнее обновление: 01.12.2023




-

-

-














Для взаимодействия с сервером компоненты Blazor WebAssembly, как и компоненты уровня сервера, также используют класс HttpClient. Однако
поскольку компоненты WebAssembly отрабатывают на клиенте, то в реальности
для отправки запросов они будут использовать Fetch API браузера. Соответственно принцип установки и получения HttpClient в компонентах WebAssembly будет немного различаться.


Пусть у нас есть следующие проекты
![Создание проекта ASP.NET Web API для тестирования приложения Blazor на C#](https://metanit.com./pics/5.7.png)


То есть у нас два проекта: главный проект BlazorApp и проект с компонентами WebAssembly - BlazorApp.Client. Поскольку на момент .NET 8
для хранения компонентов Blazor WebAssembly необходимо создавать дополнительный проект.


#### Настройка сервера


В главном проекте BlazorApp (на сервере) в файле Program.cs прописан следующий код:

```

using BlazorApp.Components;
using BlazorApp.Client;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddRazorComponents()
 .AddInteractiveWebAssemblyComponents(); // поддержка компонентов WebAssembly

builder.Services.AddHttpClient(); // регистрируем сервис файбрики HttpClient

var app = builder.Build();

app.UseAntiforgery();

app.MapGet("/time", () => DateTime.Now.ToShortTimeString());

app.MapRazorComponents<App>()
 .AddInteractiveWebAssemblyRenderMode() // рендеринг компонентов WebAssembly
 .AddAdditionalAssemblies(typeof(Home).Assembly); ; // подключаем поиск компонентов из BlazorApp.Client


app.Run();

```


Здесь добавлены сервисы компонентов WebAssembly, определена поддержка рендеринга на стороне клиента и добавлен поиск компонентов в сборке, где находится компонент Home из второго проекта.


Для использования HttpClient регистрируем сервис фабрики:

```
builder.Services.AddHttpClient();
```


Для теста здесь также определена конечная точка, которая при обращении по пути "/time" возвращает текущее время.

```
app.MapGet("/time", () => DateTime.Now.ToShortTimeString());
```


В главном проекте BlazorApp в папке "Components" есть один компонент - корневой компонент App, который загружает компонент Home из второго проекта:

```

@page "/"
@using BlazorApp.Client

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


#### Настройка клиента


И для работы с HttpClient нам надо добавить данный объект в качестве сервиса в приложение. Для этого во втором проекте - BlazorApp.Client определим следующий
файл Program.cs:

```

using Microsoft.AspNetCore.Components.WebAssembly.Hosting;

var builder = WebAssemblyHostBuilder.CreateDefault(args);

// добавляем HttpClient
builder.Services.AddScoped(sp =>
 new HttpClient
 {
 BaseAddress = new Uri("https://localhost:7066/")
 });

await builder.Build().RunAsync();


```


При добавлении HttpClient устанавливается свойство BaseAddress, которое определяет адрес веб-сервиса. В моем случае веб-приложение ASP.NET Core запущено
по адресу "https://localhost:7066/".


После этого мы можем получить объект HttpClient в коде компонентов, как и любой другой сервис, с помощью внедрения зависимостей. Так,
определим в проекте BlazorApp.Client следующий компонент Home:

```

@using Microsoft.AspNetCore.Components.Web
@using System.Net.Http.Json

@rendermode RenderMode.InteractiveWebAssembly
@inject HttpClient httpClient

<h2>Time: @time</h2>
<button @onclick="Submit">Click</button>

@code {
 string? time;
 async Task Submit()
 {
 var response = await httpClient.GetAsync("/time");
 time = await response.Content.ReadAsStringAsync();
 }
}

```


Здесь по нажатию на кнопку отправляем Get-запрос к веб-сервису по пути "/time" и получаем ответ в переменную response:

```
var response = await httpClient.GetAsync("/time");
```


Далее считываем содержимое ответа в строку в переменную time, значение которой выводится в заголовке на веб-страницу:

```
time = await response.Content.ReadAsStringAsync();
```

![Отправка запросов с помощью HttpClient в приложении Blazor Server на C#](https://metanit.com./pics/5.5.png)


В остальном работа с HttpClient будет идти также как и в принципе в .NET.


### Отправка данных


Отправка запросов и получение ответов с помощью HttpClient в Blazor WebAssembly будет идти также, как и в целом в .NET - [Отправка запросов с помощью HttpClient](https://metanit.com/sharp/net/2.2.php).
Поэтому рассмотрим лишь один сценарий - отправку данных в POST-запросе. Пусть файл Program.cs в главном проекте BlazorApp выглядит следующим образом:

```

using BlazorApp.Components;
using BlazorApp.Client;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddRazorComponents()
 ..AddInteractiveWebAssemblyComponents();

builder.Services.AddHttpClient(); // регистрируем сервис файбрики HttpClient
var app = builder.Build();

app.UseAntiforgery();

app.MapPost("/user", (Person user) =>
{
 // если длина имени меньше 3 или больше 20 символов
 if (user.Name.Length < 3 || user.Name.Length > 20)
 return Results.BadRequest(new { details = "Имя должно иметь не меньше 3 и не больше 20 символов" });
 // если возраст меньше 1 или больше 110
 if (user.Age < 1 || user.Age > 110)
 return Results.BadRequest(new { details = "Некорректный возраст" });
 // если все нормально, устанавливаем id для нового пользователя
 user.Id = Guid.NewGuid().ToString();
 // посылаем объект в виде json
 return Results.Json(user);
});

app.MapRazorComponents<App>()
 .AddInteractiveWebAssemblyRenderMode()
 .AddAdditionalAssemblies(typeof(Home).Assembly);


app.Run();


public class Person
{
 public string Id { get; set; } = "";
 public string Name { get; set; } = "";
 public int Age { get; set; }
}

```


Здесь предполагается, что клиент в POST-запросе по пути "/user" будет отправлять объект Person. При получении данных валидируем их (имя должно иметь от 3 до 20 символов, а возраст должен быть в диапазоне от 1 до 110). Если они не соответствуют некоторым ограничениям,
то посылаем ошибку 400 и объект json с сообщением об ошибке:

```

if(user.Name.Length < 3 || user.Name.Length > 20)
 return Results.BadRequest(new {details="Имя должно иметь не меньше 3 и не больше 20 символов" });
if (user.Age < 1 || user.Age > 110)
 return Results.BadRequest(new {details = "Некорректный возраст" });

```


Если данные корректны, то устанавливаем у объекта Person свойство Id и посылаем его в формате JSON обратно клиенту:

```

user.Id = Guid.NewGuid().ToString();
return Results.Json(user);

```


Для взаимодействия с этим веб-приложением в проекте BlazorApp.Client определим следующий компонент Home:

```

@using Microsoft.AspNetCore.Components.Web
@using System.Net.Http.Json

@rendermode RenderMode.InteractiveWebAssembly
@inject HttpClient httpClient

<div style="color:red;">@message</div>

<div>
 <p>
 Имя:<br />
 <input @bind-value="person.Name" />
 </p>
 <p>
 Возраст:<br />
 <input type="number" @bind-value="person.Age" />
 </p>
 <button @onclick="Submit">Click</button>
</div>

@code {
 string? message;
 Person person = new();
 async Task Submit()
 {
 message = "";
 var response = await httpClient.PostAsJsonAsync("https://localhost:7066/user", person);
 if (response.IsSuccessStatusCode)
 {
 var newPerson = await response.Content.ReadFromJsonAsync<Person>();
 if (newPerson != null) message = $"Создан объект Person с id = {newPerson.Id}";
 }
 else
 {
 var error = await response.Content.ReadFromJsonAsync<Error>();
 if (error != null) message = error.Details;
 }
 }
 class Error
 {
 public string Details { get; set; } = "";
 }
 class Person
 {
 public string Id { get; set; } = "";
 public string Name { get; set; } = "";
 public int Age { get; set; }
 }
}

```


Здесь определена форма с двумя полями ввода, которые привязаны к свойствам Name и Age объекта Person. По нажатию на кнопку срабатывает метод Submit, который в POST-запросе в виде кода json отправляет
на сервер объект Person.


При успешном запросе (если сервер возвращает статусный код 2хх) получаем отправленный сервером объект Person с установленным Id и этот Id выводим в сообщении:

```

if (response.IsSuccessStatusCode)
{
 var newPerson = await response.Content.ReadFromJsonAsync<Person> ();
 if (newPerson != null) message = $"Создан объект Person с id = {newPerson.Id}";
}

```


Если же сервер возвратил ошибку (в нашем случае ошибку 400 при некорректности данных), получаем сообщение об ошибке в объект Error, и затем также выводим сообщение об ошибке на страницу:

```

else
{
 var error = await response.Content.ReadFromJsonAsync<Error>();
 if (error != null) message = error.Details;
}

```


Пример работы:
![Создание проекта ASP.NET Web API для тестирования приложения Blazor на C#](https://metanit.com./pics/5.4.png)












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

**Источник:** [https://metanit.com/sharp/blazor/6.1.php](https://metanit.com/sharp/blazor/6.1.php)
