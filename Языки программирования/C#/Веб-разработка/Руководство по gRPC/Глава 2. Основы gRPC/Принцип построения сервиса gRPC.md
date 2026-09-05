# Принцип построения сервиса gRPC

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по gRPC|Руководство по gRPC]] / [[Языки программирования/C#/Веб-разработка/Руководство по gRPC/Глава 2. Основы gRPC|Глава 2. Основы gRPC]] / Принцип построения сервиса gRPC

[[Языки программирования/C#/Веб-разработка/Руководство по gRPC/Глава 1. Введение в gRPC/Первый проект в Visual Studio|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по gRPC/Глава 2. Основы gRPC|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по gRPC/Глава 2. Основы gRPC/Синтаксис Protobuf. Определение сообщений и сервиса|Вперёд]]

**Дата написания:** 05.09.2026

## Принцип построения сервиса gRPC

Последнее обновление: 22.11.2022




-

-

-














gRPC использует подход contract-first для построения API. То есть есть некоторый контракт, которому сервер и клиент должны следовать. Этот контракт описывается с помощью
файлов с расширением .proto. proto-файлы выполняют две основные задачи:


-

Описание сервиса gRPC

-

Описание формата сообщений, которыми обмениваются клиент и сервер


Собственно формат сервиса и формат сообщений - это и есть контракт, которому клиент и сервер должны следовать.


Например, возьмем файл greeter.proto, который генерируется по умолчанию в проекте по типу grpc в .NET CLI или по шаблону `ASP.NET Core gRPC Service` в Visual Studio:
![Файлы proto в проекте сервиса grpc на C# и .NET](https://metanit.com./pics/2.1.png)

```

syntax = "proto3";

option csharp_namespace = "GreeterServiceApp";

package greet;

// Определение сервиса Greeter
service Greeter {
 // определение метода SayHello,
 // который получает сообщение HelloRequest
 // и отправляет сообщение HelloReply
 rpc SayHello (HelloRequest) returns (HelloReply);
}

// определение сообщения HelloRequest
message HelloRequest {
 string name = 1;
}

// определение сообщения HelloReply
message HelloReply {
 string message = 1;
}

```


Для описания сервиса gPRC и сообщений используется специальный синтаксис proto.


Самая первая строка определяет тип используемого синтаксиса:

```
syntax = "proto3";
```


В данном случаем применяется синтаксис "proto3". Если явным образом не указать версию, то по умолчанию будет использоваться более старая версия - proto2.


Далее указывается пространство имен, которое будет использоваться с этим сервисом:

```
option csharp_namespace = "GreeterServiceApp";
```


По умолчанию это название проекта. И соответственно генерируемые классы будут помещаться в даное пространство имен. Если не указать эту настройку, то в качестве пространства имен будет использоваться
название пакета в PascalCase.


Следующая строка с помощью оператора package определяет название пакета:

```
package greet;
```


В данном случае пакет называется "greet". Установка имени пакета позволяет разрешить конфликты имен при наличие сущностей с одинаковыми именами.


Затем определяется сервис Greeter:

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


Поскольку данный файл описывает обязательный контракт для сервера и клиента, то проект клиента также должен содержать этот файл. Единственное в проекте клиента меняется пространство имен.


### Добавление файла proto в проект


Для добавления файла .proto в проект в файле проекта .csproj должен быть добавлен элемент <Protobuf>

```

<ItemGroup>
 <Protobuf Include="Protos\greet.proto" GrpcServices="Server" />
</ItemGroup>

```


В проект сервиса grpc, который создается по шаблону, данный элемент добавляется автоматически. Для проектов клиентов этот пункт необходимо добавлять вручную.


С помощью атрибута `Include` указывается путь к файлу proto. А атрибут `GrpcServices` описывает тип генерируемых
классов на основе файла proto. `GrpcServices` может принимать следующие значения:


-

`Server` (генерируются файлы стороны сервера)

-

`Client` (генерируются файлы стороны клиента)

-

`Both` (значение по умолчанию, при котром генерируются файлы как для сервера, так и для клиента)

-

`None` (файлы не генерируются)


Например, значение `GrpcServices="Server"` указывает, что будут генерироваться файлы, которые необходимы для работы сервиса на стороне сервера.


### Генерация классов C#


Proto-файл описывает контракт и не зависит от конкретного языка приложения. Однако в приложении на C# мы работаем именно с типами на языке C#. И для работы сервиса и клиента
инструменты .NET самостоятельно на основании proto-файла при необходимости автоматически генерируют ряд классов при каждом построении проекта. Причем генерация производится
как в проекте сервера, так и в проекте клиента.


Для генерации подобных классов в проект добавляется пакет Grpc.Tools (как в проект сервера, так и в проект клиента). Но на стороне сервера ASP.NET
также применяется метапакет `Grpc.AspNetCore`, который включает в том числе Grpc.Tools и который добавляется по умолчанию в проект grpc-сервиса.

```

<ItemGroup>
 <PackageReference Include="Grpc.AspNetCore" Version="2.57.0" />
 </ItemGroup>

```


В проект же клиента нам необходимо вручную добавлять `Grpc.Tools`:

```

<ItemGroup>
 <PackageReference Include="Google.Protobuf" Version="3.25.1" />
 <PackageReference Include="Grpc.Net.Client" Version="2.59.0" />
 <PackageReference Include="Grpc.Tools" Version="2.59.0">
 <IncludeAssets>runtime; build; native; contentfiles; analyzers; buildtransitive</IncludeAssets>
 <PrivateAssets>all</PrivateAssets>
 </PackageReference>
</ItemGroup>

```


Причем для пакета `Grpc.Tools` применяется настрока `PrivateAssets="All"`, которая говорит, что данный пакет нужен только в процессе построения проекта, но не в процесса выполнения.


#### Автогенерируемые файлы


После построения проекта в папке `obj\Debug\net8.0\Protos` мы можем найти ряд автосгенерированных файлов:
![Генерация классов сервисов grpc на основании файла proto в приложении на языке C#](https://metanit.com./pics/2.2.png)


Какие классы генерируется? На строне сервера это абстрактный класс сервиса, который содержит определение всех вызовов gRPC из файла `.proto`. Например, в случае
с файлом `greeter.proto` это абстрактный класс

```

public static partial class Greeter
{
 //..........................
 public abstract partial class GreeterBase
 {
 [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
 public virtual global::Task<global::GreeterServiceApp.HelloReply> SayHello(global::GreeterServiceApp.HelloRequest request, grpc::ServerCallContext context)
 {
 throw new grpc::RpcException(new grpc::Status(grpc::StatusCode.Unimplemented, ""));
 }

 }
 // остальное содержимое класса Greeeter
}

```


Кроме того, автогенерируются классы сообщений. В случае со стандартным файлом `greeter.proto` это классы HelloRequest и HelloReply:

```

public sealed partial class HelloRequest { ......... }
public sealed partial class HelloReply { ......... }

```


При создании проекта сервиса в проект в папку Services добавляется файл GreeterService.cs с конкретной реализацией
класса сервиса:
![Определение сервиса grpc в C# и ASP.NET Core](https://metanit.com./pics/2.3.png)

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


По умолчанию в конструкторе через dependency injection класс получает объект логгера для логирования. Кроме того, класс сервиса реализует метод SayHello. В этом методе
через первый параметр - объект HelloRequest сервис получает сообщения. Метод возвращает объект класса HelloReply, который представляет ответное сообщение клиенту.


На строне клиента также генерируются файлы сообщений. Но вместо абстрактного класса сервиса генерируется класс клиента grpc для обмена сообщениями с сервисов. Так, в случае с выше определенным
файлом `greeter.proto` это класс GreeterClient:

```

public static partial class Greeter
{
 // .......................
 public partial class GreeterClient : grpc::ClientBase<GreeterClient>
 {
 //....................
 }
}

```


Далее на стороне клиента этот класс применяется для отправки данных сервису:

```

using var channel = GrpcChannel.ForAddress("https://localhost:7062");
var client = new Greeter.GreeterClient(channel);
var reply = await client.SayHelloAsync(new HelloRequest { Name = "Tom" });

```











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

**Источник:** [https://metanit.com/sharp/grpc/2.1.php](https://metanit.com/sharp/grpc/2.1.php)
