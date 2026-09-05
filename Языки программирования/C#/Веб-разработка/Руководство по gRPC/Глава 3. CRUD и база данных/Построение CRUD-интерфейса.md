# Построение CRUD-интерфейса

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по gRPC|Руководство по gRPC]] / [[Языки программирования/C#/Веб-разработка/Руководство по gRPC/Глава 3. CRUD и база данных|Глава 3. CRUD и база данных]] / Построение CRUD-интерфейса

[[Языки программирования/C#/Веб-разработка/Руководство по gRPC/Глава 2. Основы gRPC/Получение и отправка заголовков на сервере и клиенте|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по gRPC/Глава 3. CRUD и база данных|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по gRPC/Глава 3. CRUD и база данных/Работа с базой данных через Entity Framework|Вперёд]]

**Дата написания:** 05.09.2026

## Построение CRUD-интерфейса

Последнее обновление: 16.01.2023




-

-

-














Работа с данными в стиле CRUD, в частности, добавление, получение, обновление и удаление данных, является достаточно распростренной задачей веб-приложений. И приложении на grpc
также можно определить функционал для работы с данными. Рассмотрим, как это сделать.


### Создание сервера


Вначале создадим проект сервиса по типу ASP.NET Core gRPC Service. В папке Protos определим файл crud.proto
со следующим содержимым:

```

syntax = "proto3";

package metanit;

import "google/protobuf/empty.proto";

service UserService{

 rpc ListUsers(google.protobuf.Empty) returns (ListReply);
 rpc GetUser(GetUserRequest) returns (UserReply);
 rpc CreateUser(CreateUserRequest) returns (UserReply);
 rpc UpdateUser(UpdateUserRequest) returns (UserReply);
 rpc DeleteUser(DeleteUserRequest) returns (UserReply);
}

message CreateUserRequest{
 string name=1;
 int32 age = 2;
}

message GetUserRequest{
 int32 id =1;
}

message UpdateUserRequest{
 int32 id=1;
 string name=2;
 int32 age = 3;
}

message DeleteUserRequest{
 int32 id =1;
}

message ListReply{
 repeated UserReply Users = 1;
}

message UserReply{
 int32 id = 1;
 string name=2;
 int32 age = 3;
}

```


Здесь определен сервис `UserService`, который будет получать данные от клиента. В сервисе определен ряд методов:


-

`ListUsers`: предназначен для отправки списка объектов из условной бд. Он получает в качестве параметра пустой ответ. Для этого используем специально определенный тип
`google.protobuf.Empty` из пакета `google/protobuf/empty.proto`, который в начале файла импортируется.

-

`GetUser`: предназначен для отправки одного объекта. В качестве параметра он получает сообщение `GetUserRequest`, которое содержит id запрошенного объекта.

-

`CreateUser`: для добавления объекта. В качестве параметра он получает сообщение `CreateUserRequest`, которое содержит добавляемые данные
в виде строки `name` и числа `age`. И возвращает созданный объект.

-

`UpdateUser`: предназначен для обновления объекта. В качестве параметра он получает сообщение `UpdateUserRequest` с новыми данными. В качестве результата возвращает
новое состояние объекта

-

`DeleteUser`: предназначен для удаления объекта. В качестве параметра он получает сообщение `DeleteUserRequest`, которое содержит id удаляемого объекта.
В качестве результата возвращает удаленный объект.


В качестве результата почти все методы возвращают объект `UserReply`, которое представляет сами данные:

```

message UserReply{
 int32 id = 1;
 string name=2;
 int32 age = 3;
}

```


И метод `ListUsers` объект, которое по сути представляет набор объектов UserReply:

```

message ListReply{
 repeated UserReply Users = 1;
}

```


Оператор repeated указывает, что это будет набор объектов типа UserReply.


Далее в проекте в папке Services определим класс сервиса, который назовем UserApiService и который будет иметь следующий код:

```

using Google.Protobuf.WellKnownTypes;
using Grpc.Core;
using Metanit; // пространство имен сервиса UserService.UserServiceBase

namespace CrudGrpcApp.Services;

public class UserApiService : UserService.UserServiceBase
{
 static int id = 0; // счетчик для генерации id
 // условная база данных
 static List<User> users = new() { new User(++id, "Tom", 38), new User(++id, "Bob", 42) };

 // отправляем список пользователей
 public override Task<ListReply> ListUsers(Empty request, ServerCallContext context)
 {
 var listReply = new ListReply(); // определяем список
 // преобразуем каждый объект из списка users в объект UserReply
 var userList = users.Select(item => new UserReply { Id = item.Id, Name = item.Name, Age = item.Age }).ToList();
 listReply.Users.AddRange(userList);
 return Task.FromResult(listReply);
 }
 // отправляем одного пользователя по id
 public override Task<UserReply> GetUser(GetUserRequest request, ServerCallContext context)
 {
 var user = users.Find(u => u.Id == request.Id);
 // если пользователь не найден, генерируем исключение
 if (user == null)
 {
 throw new RpcException(new Status(StatusCode.NotFound, "User not found"));
 }
 UserReply userReply = new UserReply() { Id = user.Id, Name = user.Name, Age = user.Age };
 return Task.FromResult(userReply);
 }
 // добавление пользователя
 public override Task<UserReply> CreateUser(CreateUserRequest request, ServerCallContext context)
 {
 // формируем из данных объект User и добавляем его в список users
 var user = new User(++id, request.Name, request.Age);
 users.Add(user);
 var reply = new UserReply() { Id = user.Id, Name = user.Name, Age = user.Age };
 return Task.FromResult(reply);
 }
 // обновление пользователя
 public override Task<UserReply> UpdateUser(UpdateUserRequest request, ServerCallContext context)
 {
 var user = users.Find(u => u.Id == request.Id);

 if (user == null)
 {
 throw new RpcException(new Status(StatusCode.NotFound, "User not found"));
 }
 // обновляем даннные
 user.Name = request.Name;
 user.Age = request.Age;

 var reply = new UserReply() { Id = user.Id, Name = user.Name, Age = user.Age };
 return Task.FromResult(reply);
 }
 // удаление пользователя
 public override Task<UserReply> DeleteUser(DeleteUserRequest request, ServerCallContext context)
 {
 var user = users.Find(u => u.Id == request.Id);

 if (user == null)
 {
 throw new RpcException(new Status(StatusCode.NotFound, "User not found"));
 }

 users.Remove(user);
 var reply = new UserReply() { Id = user.Id, Name = user.Name, Age = user.Age };
 return Task.FromResult(reply);
 }
}
// модель пользователя - класс User
class User
{
 public int Id { get; set; }
 public string Name { get; set; }
 public int Age { get; set; }
 public User(int id, string name, int age)
 {
 Id = id;
 Name = name;
 Age = age;
 }
}

```


В качестве модели данных здесь выступает класс `User` с тремя свойствами, который представляет условного пользователя. В классе `UserApiService` для простоты имитируем базу данных
в виде статического списка `users` с двумя начальными объектами.

```

static int id = 0; // счетчик для генерации id
static List<User> users = new() { new User(++id, "Tom", 38), new User(++id, "Bob", 42) };

```


Для генерации идентификаторов определена вспомогательная статическая переменная id.


В методе `ListUsers` возвращаем список объектов:

```

public override Task<ListReply> ListUsers(Empty request, ServerCallContext context)
{
 var listReply = new ListReply();
 var userList = users.Select(item => new UserReply { Id = item.Id, Name = item.Name, Age = item.Age }).ToList();
 listReply.Users.AddRange(userList);
 return Task.FromResult(listReply);
}

```


В качестве параметра получаем пустой ответ, для которого используем специальный тип `Google.Protobuf.WellKnownTypes.Empty`. В самом методе определяем объект ListReply,
в его свойство `Users` передаем все объекты из списка users, преобразуя их в тип UserReply. И отправляем сформированный объект ListReply клиенту.


В методе `GetUser` клиенту отправляем одного пользователя:

```

public override Task<UserReply> GetUser(GetUserRequest request, ServerCallContext context)
{
 var user = users.Find(u => u.Id == request.Id);
 if (user == null)
 {
 throw new RpcException(new Status(StatusCode.NotFound, "User not found"));
 }
 UserReply userReply = new UserReply() { Id = user.Id, Name = user.Name, Age = user.Age };
 return Task.FromResult(userReply);
}

```


Из параметра request получаем id запрошенного пользователя и ищем соответствующий объект в списке users. Вполне возможно, что пользователь с указанным id не будет найден. В этом
случае генерируем исключение RpcException. В конструктор исключения мы можем передать объект Status, в котором с помощью свойства
StatusCode можно указать статусный код, аналогично тому, как это делается для установки статусных кодов в http. Кроме того, можно указать строку статуса с указанием причины ошибки.
И если будет сгенерировано исключение, то клиент получит эти данные.


Если же пользователь найден в списке users, то преобразуем его в тип UserReply и отправляем клиенту.


Остальные методы однотипны. Метод `CreateUser` добавляет одного пользователя в список. Метод `UpdateUser` по полученным данным обновляет определенного пользователя.
И метод `DeleteUser` удаляет по полученному id пользователя из списка users. Во всех случаях результат метода отправляется пользователю.


В конце включим сервис UserApiService в конвейер обработки запроса в файле Program.cs:

```

using CrudGrpcApp.Services; // пространство имен сервиса UserApiService

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddGrpc();

var app = builder.Build();

app.MapGrpcService<UserApiService>();
app.MapGet("/", () => "Hello METANIT.COM");

app.Run();

```


То есть получится следующий проект:
![CRUD в сервисах ASP.NET GRPC на C#](https://metanit.com./pics/3.1.png)


### Создание клиента


Для тестирования сервиса определим проект консольного приложения. Добавим в него через Nuget все нужные пакеты:


-

Grpc.Net.Client

-

Google.Protobuf

-

Grpc.Tools


Далее создадим в проекте консольного приложения новую папку Protos и в нее скопируем из проекта сервиса файл crud.proto
![Создание консольного клиента для CRUD-интерфейса в gRPC-сервисе на языке C#](https://metanit.com./pics/3.2.png)


Далее нам надо отредактировать файл проекта с расширением csproj, который называется по имени проекта - узел `<Project>` добавим следующий элемент:

```

<ItemGroup>
 <Protobuf Include="Protos\crud.proto" GrpcServices="Client" />
</ItemGroup>

```


Для получения списка пользователей в файле Program.cs определим следующий код:

```

using Grpc.Net.Client;
using Metanit;

// создаем канал для обмена сообщениями с сервером
// параметр - адрес сервера gRPC
using var channel = GrpcChannel.ForAddress("https://localhost:7138");

// создаем клиент
var client = new UserService.UserServiceClient(channel);

// получение списка
ListReply users = await client.ListUsersAsync(new Google.Protobuf.WellKnownTypes.Empty());

foreach (var user in users.Users)
{
 Console.WriteLine($"{user.Id}. {user.Name} - {user.Age}");
}

```


Поскольку сервер возвращает объект ListReply, то cоответственно на клиенте мы получаем этот объект и с помощью его свойства Users можем получить все данные пользователя в виде объекта UserReply.


Для тестирования получения одного объекта по id определим следующий код:

```

using Grpc.Net.Client;
using Metanit;

using var channel = GrpcChannel.ForAddress("https://localhost:7138");
var client = new UserService.UserServiceClient(channel);

// получение одного объекта по id = 1
UserReply user = await client.GetUserAsync(new GetUserRequest { Id = 1 });
Console.WriteLine($"{user.Id}. {user.Name} - {user.Age}");

```


Однако, если пользователя по определенному id не окажется, то сервер генерирует исключение RpcException, отправляет клиенту соответствующий статус. Если на стороне сервера генерируется исключение,
то на клиенте тоже автоматически генерируется исключение. И в этом случае, чтобы программа не завершилась аварийно, мы можем обработь исключение, получив статус ответа:

```

using Grpc.Core;
using Grpc.Net.Client;
using Metanit;

using var channel = GrpcChannel.ForAddress("https://localhost:7138");
var client = new UserService.UserServiceClient(channel);

try
{
 // получение одного объекта по id = 4
 UserReply user = await client.GetUserAsync(new GetUserRequest { Id = 4 });
 Console.WriteLine($"{user.Id}. {user.Name} - {user.Age}");
}
catch (RpcException ex)
{
 Console.WriteLine(ex.Status.Detail); // получаем статус ответа
}

```


Создание нового объекта:

```

using Grpc.Core;
using Grpc.Net.Client;
using Metanit;

using var channel = GrpcChannel.ForAddress("https://localhost:7138");
var client = new UserService.UserServiceClient(channel);

// добавление одного объекта
UserReply user = await client.CreateUserAsync(new CreateUserRequest { Name = "Sam", Age = 28 });
Console.WriteLine($"{user.Id}. {user.Name} - {user.Age}");

```


Обновление объекта

```

using Grpc.Core;
using Grpc.Net.Client;
using Metanit;

using var channel = GrpcChannel.ForAddress("https://localhost:7138");
var client = new UserService.UserServiceClient(channel);

try
{
 //обновление одного объекта - изменим имя у объекта с id = 1 на Tomas
 UserReply user = await client.UpdateUserAsync(new UpdateUserRequest { Id = 1, Name = "Tomas", Age = 38 });
 Console.WriteLine($"{user.Id}. {user.Name} - {user.Age}");
}
catch (RpcException ex)
{
 Console.WriteLine(ex.Status.Detail);
}

```


И тестирование удаления объекта:

```

using Grpc.Core;
using Grpc.Net.Client;
using Metanit;

using var channel = GrpcChannel.ForAddress("https://localhost:7138");
var client = new UserService.UserServiceClient(channel);

try
{
 // удаление объекта с id = 2
 UserReply user = await client.DeleteUserAsync(new DeleteUserRequest { Id= 2 });
 Console.WriteLine($"{user.Id}. {user.Name} - {user.Age}");
}
catch (RpcException ex)
{
 Console.WriteLine(ex.Status.Detail);
}

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

**Источник:** [https://metanit.com/sharp/grpc/3.1.php](https://metanit.com/sharp/grpc/3.1.php)
