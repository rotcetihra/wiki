# Первый проект в Visual Studio

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по gRPC|Руководство по gRPC]] / [[Языки программирования/C#/Веб-разработка/Руководство по gRPC/Глава 1. Введение в gRPC|Глава 1. Введение в gRPC]] / Первый проект в Visual Studio

[[Языки программирования/C#/Веб-разработка/Руководство по gRPC/Глава 1. Введение в gRPC/Первый проект с .NET CLI|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по gRPC/Глава 1. Введение в gRPC|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по gRPC/Глава 2. Основы gRPC/Принцип построения сервиса gRPC|Вперёд]]

**Дата написания:** 05.09.2026

## Первый проект в Visual Studio

Последнее обновление: 26.11.2023




-

-

-














В прошлой теме рассматривалось создание проекта сервиса gRPC с помощью консольный команд .NET CLI. Теперь рассмотрим, как использовать Visual Studio для создания аналогичного проекта.


Visual Studio поддерживает специальный шаблон для создания сервисов gRPC - ASP.NET Core gRPC Service.
![Создание проекта сервиса gRPC на C# в Visual Studio](https://metanit.com./pics/1.6.png)


Используя данный тип проектов создадим новый проект, который, пусть называется GreeterServiceApp.
![Проект сервиса gRPC на C# в Visual Studio](https://metanit.com./pics/1.7.png)


Здесь создается та же структура проекта gRPC, что и при использовании .NET CLI:


-

Папка Properties содержит файл launchSettings.json, который определяет параметры запуска сервиса.

-

Папка Protos содержит файлы с определением сервисов и сообщений, используемых для взаимодействия по сети


По умолчанию в этой папке определен один файл greet.proto.


-

Папка Services содержит файлы с реализацией сервисов


По умолчанию в этой папке определен один файл GreeterService.cs.


-

Файл appsettings.json - стандартный файл конфигурации приложения ASP.NET Core.

-

Файл appsettings.Development.json - файл конфигурации приложения для стадии разработки.

-

Файл Program.cs содержит стандартный класс Program, с которого начинается выполнение приложения ASP.NET Core.

-

Файл GreeterServiceApp.csproj - стандартный файл конфигурации проекта C#.


### Определение сервиса


Вкратце пройдемся по всей функциональности сервиса


#### Контракт сервиса и файл greet.proto


gRPC использует подход "contract-first", то есть вначале определяется контракт - общее определение сервиса, которое определяет механизм взаимодействия.
Так, по умолчанию в папке Protos есть файл greet.proto со следующим кодом:

```

syntax = "proto3";

option csharp_namespace = "GreeterServiceApp";

package greet;

// определение сервиса
service Greeter {
 // отправка сообщения
 rpc SayHello (HelloRequest) returns (HelloReply);
}

// сообщение от клиента содержит name
message HelloRequest {
 string name = 1;
}

// сообщение клиенту содержит message
message HelloReply {
 string message = 1;
}

```


Определение этого файла может напоминать синтаксис C#, но в реальности это синтаксис proto, который используется
для описания сервиса gPRC. Хотя в целом это си-подобный синтаксис, поэтому ориентироваться в нем не так сложно.


Самая первая строка определяет тип используемого синтаксиса:

```
syntax = "proto3";
```


В данном случаем применяется синтаксис "proto3".


Далее указывается пространство имен, которое будет использоваться с этим сервисом:

```
option csharp_namespace = "GreeterServiceApp";
```


По умолчанию это название проекта. И соответственно генерируемые классы будут помещаться в даное пространство имен.


Следующая строка с помощью оператора package определяет название пакета:

```
package greet;
```


В данном случае пакет называется "greet". Установка имени пакета позволяет разрешить конфликты имен при наличие сущностей с одинаковыми именами.


Далее собственно определяется сервис:

```

service Greeter {
 rpc SayHello (HelloRequest) returns (HelloReply);
}

```


Сервис определяется с помощью ключевого слова service, после которого указывается название сервиса. То есть в данном случае
сервис называется "Greeter".


С помощью ключевого слова rpc в сервисе определяется метод `SayHello`. Данный метод отправляет
сообщение HelloRequest и сообщение HelloReply.


Далее идет определение используемых сообщений:

```

message HelloRequest {
 string name = 1;
}

message HelloReply {
 string message = 1;
}

```


Сообщение представляет специальную сущность, которая содержит пересылаемые данные. Сообщение определяет набор полей, для которых
определен тип. Каждое поле представляет некоторый кусочек информации, посылаемой в сообщении. Так, в обоих сообщениях определены два поля типа string, то есть в каждом сообщении будут отправляться некоторая строка.


Каждому полю в сообщении присваивается уникальное число, например, в примере выше полям обоих сообщений присваивается единица
(в `string name = 1` или в `string message = 1`). Эти значения позволяют идентифицировать непосредственные значения полей в бинарном формате при кодировании и получении
сообщений.


#### Реализация сервиса


В папке Services по умолчанию в файле GreeterService.cs определен класс GreeterService,
который представляет реализацию сервиса gPRC на языке C#:

```

using Grpc.Core;
using GreeterServiceApp;

namespace GreeterServiceApp.Services;

public class GreeterService : Greeter.GreeterBase
{
 private readonly ILogger<GreeterService> _logger;
 public GreeterService(ILogger<GreeterService> logger)
 {
 _logger = logger;
 }

 public override Task<HelloReply> SayHello(HelloRequest request, ServerCallContext context)
 {
 return Task.FromResult(new HelloReply
 {
 Message = "Hello " + request.Name
 });
 }
}

```


Класс сервиса (в данном случае GreeterService) наследуется от класса Greeter.GreeterBase. Greeter.GreeterBase - абстрактный класс, который автоматически генерируется по определению сервиса greeter в файле `greeter.proto`.


Класс GreeterService по сути представляет обычный класс C#. Так, по умолчанию он имеет конструктор, который посредством dependency injection получает
объект логгера и может его использовать для логирования.


Но основной момент класса сервиса - это реализация метода SayHello, коорый по сути отвечает за обмен сообщениями. Его первый параметр представляет
класс HelloRequest, который соответствует определению входящего сообщения в файле proto. То есть это те данные, которые мы получаем от клиента:

```

message HelloRequest {
 string name = 1;
}

```


Поскольку сообщение содержит одно поле name, которое представляет строку, то в коде C# мы можем получить эти данные через свойство Name.


Второй параметр метода - объект ServerCallContext, хранит информацию, связанную с контекстом, в котором работает сервер.


Возвращаемое значение метода - объект класса HelloReply, который представляет ответное сообщение сообщение:

```

message HelloReply {
 string message = 1;
}

```


Это те данные, которые мы посылаем клиенту в ответ. Поскольку сообщение содержит строковое поле message, то в соответствующем классе C# мы можем обращаться к нему
через свойство Message:

```

new HelloReply
{
 Message = "Hello " + request.Name
}

```


Класс HelloReply, как и все классы, которые представляют сообщения или сервисы из файла proto, также генерируется автоматически.


#### Подключение gRPC


Точкой входа в программу по умолчанию является класс Program, который определен неявно в файле Program.cs. И имеено здесь и происходит подключение всей
инфраструктуры gRPC:

```

using GreeterServiceApp.Services;

var builder = WebApplication.CreateBuilder(args);

// добавляем сервисы для работы с gRPC
builder.Services.AddGrpc();

var app = builder.Build();

// настраиваем обработку HTTP-запросов
app.MapGrpcService<GreeterService>();
app.MapGet("/", () => "Communication with gRPC endpoints must be made through a gRPC client...");

app.Run();

```


Для того, чтобы задействовать сервис gRPC, во-первых, добавляются необходимые сервисы:

```
builder.Services.AddGrpc();
```


Во-вторых, далее сервис gRPC встраивается в систему маршрутизации для обработки запроса:

```
app.MapGrpcService<GreeterService>();
```


Для встраивания сервиса применяется метод MapGrpcService(), который типизируется типом встраиваемого сервиса.


Теперь рассмотрим, как создать для данного сервиса примитивное консольное клиентское приложение для отправки сервису сообщений и получения от него ответа.


### Консольный клиент для gRPC-сервиса


Создадим проект клиентского приложения, который пусть называется GreeterClientApp
![Создание консольного клиента для сервиса gRPC в Visual Studio](https://metanit.com./pics/1.8.png)


#### Добавление Nuget-пакетов


Вначале прежде всего необходимо добавить в проект клиентского проекта клиентского приложения для gRPC необходимо через Nuget установить следующие пакеты:


-

Grpc.Net.Client: содержит функционал клиента .NET

-

Google.Protobuf: содержит API для сообщений protobuf для языка C#.

-

Grpc.Tools: содержит инструменты для поддержки protobuf-файлов в C#


#### Создание папки Protos и файла greet.proto


Далее создадим в проекте консольного приложения новую папку Protos, а в нее скопируем из проекта сервиса файл greet.proto,
который содержит определение используемого сервиса. Но после копирования изменим в этом файле строку

```
option csharp_namespace = "GreeterServiceApp";
```


на строку

```
option csharp_namespace = "GreeterClientApp";
```


То есть мы поменяли пространство имен с "GreeterServiceApp" (имени проекта сервиса) на "GreeterClientApp" (имя проекта клиента).
![создание клиента на C# для сервиса grpc в Visual Studio ](https://metanit.com./pics/1.9.png)


Далее нам надо отредактировать файл проекта. Для этого нажмем на название проекта правой кнопки мыши и выберем в контекстном меню пункт Edit Project File:
![добавление в клиент на C# для сервиса grpc в Visual Studio файла greet.proto](https://metanit.com./pics/1.10.png)


После установки Nuget-пакетов файл должен выглядеть следующим образом:

```

<Project Sdk="Microsoft.NET.Sdk">

 <PropertyGroup>
 <OutputType>Exe</OutputType>
 <TargetFramework>net8.0</TargetFramework>
 <ImplicitUsings>enable</ImplicitUsings>
 <Nullable>enable</Nullable>
 </PropertyGroup>

 <ItemGroup>
 <PackageReference Include="Google.Protobuf" Version="3.25.1" />
 <PackageReference Include="Grpc.Net.Client" Version="2.59.0" />
 <PackageReference Include="Grpc.Tools" Version="2.59.0">
 <PrivateAssets>all</PrivateAssets>
 <IncludeAssets>runtime; build; native; contentfiles; analyzers; buildtransitive</IncludeAssets>
 </PackageReference>
 </ItemGroup>

</Project>

```


В корневой узел `<Project>` добавим следующий элемент:

```

<ItemGroup>
 <Protobuf Include="Protos\greet.proto" GrpcServices="Client" />
</ItemGroup>

```


То есть после изменения файл проекта будет выглядеть следующим образом:

```

<Project Sdk="Microsoft.NET.Sdk">

 <PropertyGroup>
 <OutputType>Exe</OutputType>
 <TargetFramework>net8.0</TargetFramework>
 <ImplicitUsings>enable</ImplicitUsings>
 <Nullable>enable</Nullable>
 </PropertyGroup>

 <ItemGroup>
 <Protobuf Include="Protos\greet.proto" GrpcServices="Client" />
 </ItemGroup>

 <ItemGroup>
 <PackageReference Include="Google.Protobuf" Version="3.25.1" />
 <PackageReference Include="Grpc.Net.Client" Version="2.59.0" />
 <PackageReference Include="Grpc.Tools" Version="2.59.0">
 <PrivateAssets>all</PrivateAssets>
 <IncludeAssets>runtime; build; native; contentfiles; analyzers; buildtransitive</IncludeAssets>
 </PackageReference>
 </ItemGroup>

</Project>

```


Далее в проекте консольного клиента изменим код файла Program.cs следующим образом:

```

using Grpc.Net.Client;
using GreeterClientApp;

// создаем канал для обмена сообщениями с сервером
// параметр - адрес сервера gRPC
using var channel = GrpcChannel.ForAddress("https://localhost:7062");
// создаем клиент
var client = new Greeter.GreeterClient(channel);
Console.Write("Введите имя: ");
var name = Console.ReadLine();
// обмениваемся сообщениями с сервером
var reply = await client.SayHelloAsync(new HelloRequest { Name = name });
Console.WriteLine($"Ответ сервера: {reply.Message}");
Console.ReadKey();

```


Допустим, программа будет спрашивать у пользователя имя, отправлять его сервису gRPC и отображать ответ сервиса.


В файле greet.proto определено, что генерируемые классы будут помещаться в пространство имен GreeterClientApp:

```
option csharp_namespace = "GreeterClientApp";
```


Поэтому в коде клиентского приложения для подключения всех необходимых классов, связанных с сервисом grpc и автосгенерированных при построении
проекта, применяется соответствующая директива using:

```
using GreeterClientApp;
```


В каждом конкретном случае пространство имен может отличаться (по умолчанию оно равно названию проекта сервиса).


Для обмена сообщениями с сервером с помощью метода `GrpcChannel.ForAddress()` создается канал - объект GrpcChannel:

```
using var channel = GrpcChannel.ForAddress("https://localhost:7062");
```


В метод передается адрес сервиса. В данном случае поскольку сервис будет запускаться по адресу "https://localhost:7062", то
соответственно передается данный адрес. Адрес сервиса можно посмотреть в проекте сервиса в файле `Properties/launchSettings.json`


Для обращения к серверу необходимо создать объект клиента:

```
var client = new Greeter.GreeterClient(channel);
```


В конструктор клиента передается объект GrpcChannel.


Название конкретного класса клиента зависит от определения сервиса и устанавливается по шаблону `[имя_сервиса].[имя_сервиса]Client`.
То есть в данном случае сервис (согласно определению в файле proto) называется Greeter, поэтому класс клиента для этого сервиса называется
Greeter.GreeterClient.


Далее собственно выполняется взаимодействие с сервисом. Для этого вызывается метод `client.SayHelloAsync()`, определение которого в целом
совпадает с определением метода SayHello в сервисе Greeter за тем исключением, что метод клиента асинхронный:

```
var reply = await client.SayHelloAsync(new HelloRequest { Name = name });
```


В метод передается объект HelloRequest, который представляет отправляемую сервису информацию. Определение класса HelloRequest совпадает
с определением сообщения HelloRequest из файла proto.


Возвращает метод ответ сервера в виде объекта HelloReply, обернутого в объект Grpc.Core.AsyncUnaryCall. Класс HelloReply совпадает с
определением сообщения HelloReply из файла proto, поэтому через свойство Message мы можем собственно получить ответ от сервера.

```
Console.WriteLine($"Ответ сервера: {reply.Message}");
```


### Тестирование сервиса gRPC


Протестируем приложения. Сначала запустим сервис gRPC:
![Запуск сервиса gRPC на C# в Visual Studio](https://metanit.com./pics/1.11.png)


Затем запустим консольный клиент и в его консоли введем некоторое строковое значение:
![Обмен сообзениями между клиентом и сервисом gRPC в приложении на C# и .NET](https://metanit.com./pics/1.12.png)










- Глава 1. Введение в gRPC


 - [Первый проект с .NET CLI](//metanit.com/sharp/grpc/1.1.php)

 - [Первый проект в Visual Studio](//metanit.com/sharp/grpc/1.2.php)



- Глава 2. Основы gRPC


 - [Принцип построения сервиса gRPC](//metanit.com/sharp/grpc/2.1.php)

 - [Синтаксис Protobuf. Определение сообщений и сервиса](//metanit.com/sharp/grpc/2.2.php)

 - [Создание сервиса](//metanit.com/sharp/grpc/2.3.php)

 - [Работа с датами и временем](//metanit.com/sharp/grpc/2.4.php)

 - [Потоковая передача сервера](//metanit.com/sharp/grpc/2.5.php)

 - [Потоковая передача клиента](//metanit.com/sharp/grpc/2.6.php)

 - [Двунаправленная потоковая передача](//metanit.com/sharp/grpc/2.7.php)

 - [Получение и отправка заголовков на сервере и клиенте](//metanit.com/sharp/grpc/2.8.php)



- Глава 3. CRUD и база данных


 - [Построение CRUD-интерфейса](//metanit.com/sharp/grpc/3.1.php)

 - [Работа с базой данных через Entity Framework](//metanit.com/sharp/grpc/3.2.php)










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

**Источник:** [https://metanit.com/sharp/grpc/1.2.php](https://metanit.com/sharp/grpc/1.2.php)
