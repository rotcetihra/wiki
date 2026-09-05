# Внедрение зависимостей в компоненты Blazor

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по Blazor|Руководство по Blazor]] / [[Языки программирования/C#/Веб-разработка/Руководство по Blazor/Глава 2. Компоненты|Глава 2. Компоненты]] / Внедрение зависимостей в компоненты Blazor

[[Языки программирования/C#/Веб-разработка/Руководство по Blazor/Глава 2. Компоненты/Жизненный цикл компонентов|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по Blazor/Глава 2. Компоненты|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по Blazor/Глава 2. Компоненты/Привязка моделей|Вперёд]]

**Дата написания:** 05.09.2026

## Внедрение зависимостей в компоненты Blazor

Последнее обновление: 30.11.2023




-

-

-














Фреймворк Blazor позволяет воспользоваться систмой внедрения зависимостей, которая используется в ASP.NET Core и в целом в .NET. Рассомтрим только те моменты механизма DI, которые характерны
именно для приложения Blazor. Пусть у нас есть следующий проект с одним компонентом App.razor и файлом TimeService.cs
![Внедрение зависимостей в компоненты Blazor в C#](https://metanit.com./pics/2.48.png)


В файле TimeService.cs определен одноименный сервис:

```

public interface ITimeService
{
 string GetTime();
}
public class TimeService : ITimeService
{
 public string GetTime() => DateTime.Now.ToShortTimeString();
}

```


Класс TimeService представляет интерфейс ITimeService и реализует его метод GetTime(), который возвращает текущее время.


В главном файле программы - Program.cs добавим сервис ITimeService в коллекцию сервисов приложения:

```

using BlazorApp.Components;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddRazorComponents()
 .AddInteractiveServerComponents();

// добавляем сервис TimeService
builder.Services.AddTransient<ITimeService, TimeService>();

var app = builder.Build();

app.UseAntiforgery();

app.MapRazorComponents<App>()
 .AddInteractiveServerRenderMode();

app.Run();

```


Для установки сервисов через свойство `Services` получаем коллекцию сервисов приложения - объект IServiceCollection. Далее
у него вызываем методы `AddTransient/AddScoped/AddSingleton` для добавления сервиса. В данном случае посредством метода `AddTransient` добавляем для
сервиса ITimeService в качестве реализации класс TimeService.


Для получения сервиса в компоненте применяется директива @inject. Например, получим сервис ITimeService в компоненте App:

```

@page "/"
@inject ITimeService Timer

<!DOCTYPE html>
<html>
<head>
 <title>METANIT.COM</title>
 <meta charset="utf-8" />
</head>
<body>
 <h2>Time: @Timer.GetTime()</h2>
 <script src="_framework/blazor.web.js"></script>
</body>
</html>

```


После директивы `@inject` указывается название сервиса (ITimeService), а затем название переменной (Timer), через которую можно получить реализацию сервиса.

```
@inject ITimeService Timer
```


Используя название переменной, можно обращаться к функциональности сервиса в коде компонента:

```
<h2>Time: @Timer.GetTime()</h2>
```


В итоге после запуска проекта на веб-странице в заголовке мы увидим текущее время, которое получено через сервис ITimeService:
![Получение сервисов в компонентах Blazor на C#](https://metanit.com./pics/2.49.png)


### Атрибут [Inject]


Для получения сервисов в компоненте также можно использовать атрибут [Inject]. Этот атрибут применяется к свойству, в которое получаем сервис.
Например, изменим компонент App следующим образом:

```

@page "/"

<!DOCTYPE html>
<html>
<head>
 <title>METANIT.COM</title>
 <meta charset="utf-8" />
</head>
<body>
 <h2>Time: @Timer.GetTime()</h2>
 <script src="_framework/blazor.web.js"></script>
</body>
</html>

@code {

 [Inject]
 public required ITimeService Timer { get; set; }
}

```


Поскольку к свойству Timer применяется атрибут `[Inject]`, то значение для данного свойства будет обеспечивать система внедрения зависимостей. Поскольку это свойство
представляет ITimeService, то механиз DI будет искать в коллекции сервисов реализацию именно этого типа.


### Получение сервисов в других сервисах


Если сервис предполагается использовать в другом сервисе, то один сервис может получить другой, как и вобще в .NET, через конструктор. Например, пусть у нас есть еще один сервис -


```

public class TimeFormatter
{
 ITimeService timeService;
 public TimeFormatter(ITimeService timeService)
 {
 this.timeService = timeService;
 }
 public string FormatTime() => $"Current Time: {timeService.GetTime()}";
}

```


Он использует сервис ITimeService, который он получает через механизм DI через параметр конструктора.


В файле Program.cs оба сервиса добавляются в коллекцию сервисов приложения:

```

using BlazorApp.Components;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddRazorComponents()
 .AddInteractiveServerComponents();

// добавляем сервисы
builder.Services.AddTransient<ITimeService, TimeService>();
builder.Services.AddTransient<TimeFormatter>();

var app = builder.Build();

app.UseAntiforgery();

app.MapRazorComponents<App>()
 .AddInteractiveServerRenderMode();

app.Run();

```


В компоненте App также получим сервис TimeFormatter для рендеринга содержимого:

```

@page "/"
@inject TimeFormatter Formatter

<!DOCTYPE html>
<html>
<head>
 <title>METANIT.COM</title>
 <meta charset="utf-8" />
</head>
<body>
 <h2>@Formatter.FormatTime()</h2>
 <script src="_framework/blazor.web.js"></script>
</body>
</html>

```

![Получение сервисов в других сервисах в приложении Blazor на C#](https://metanit.com./pics/2.51.png)


### Сервисы по умолчанию


Ряд сервисов фреймворк Blazor предоставляет по умолчанию. Например, выведем все сервисы на консоль в файле Program.cs:

```

using BlazorApp.Components;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddRazorComponents()
 .AddInteractiveServerComponents();

// добавляем сервисы
builder.Services.AddTransient<ITimeService, TimeService>();
builder.Services.AddTransient<TimeFormatter>();

// выводим все сервисы на консоль
foreach (var service in builder.Services)
{
 Console.WriteLine(service.ServiceType);
}

var app = builder.Build();

app.UseAntiforgery();

app.MapRazorComponents<App>()
 .AddInteractiveServerRenderMode();

app.Run();


```

![Сервисы по умолчанию в приложении Blazor на C#](https://metanit.com./pics/2.52.png)











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

**Источник:** [https://metanit.com/sharp/blazor/2.11.php](https://metanit.com/sharp/blazor/2.11.php)
