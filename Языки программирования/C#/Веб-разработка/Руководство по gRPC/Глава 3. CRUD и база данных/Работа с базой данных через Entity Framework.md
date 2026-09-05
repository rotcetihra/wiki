# Работа с базой данных через Entity Framework

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по gRPC|Руководство по gRPC]] / [[Языки программирования/C#/Веб-разработка/Руководство по gRPC/Глава 3. CRUD и база данных|Глава 3. CRUD и база данных]] / Работа с базой данных через Entity Framework

[[Языки программирования/C#/Веб-разработка/Руководство по gRPC/Глава 3. CRUD и база данных/Построение CRUD-интерфейса|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по gRPC/Глава 3. CRUD и база данных|Содержание]]

**Дата написания:** 05.09.2026

## Работа с базой данных через Entity Framework

Последнее обновление: 19.11.2025




-

-

-














Рассмотрим, как подключаться в сервисах gRPC в приложении ASP.NET Core к базе данных через Entity Framework. Вначале создадим проект сервиса по типу ASP.NET Core gRPC Service. Для работы с базой данных выберем SQLite как самый простой вариант и для этого добавим в проект nuget-пакет Microsoft.EntityFrameworkCore.Sqlite


Добавим в проект класс User, который будет представлять пользователя:

```

public class User
{
 public int Id { get; set; }
 public string? Name { get; set; }
 public int Age { get; set; }
}

```


И также добавим класс контекста данных, который назовем ApplicationContext и который будет хранить следующий код:

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


Теперь определим grpc-сервис, который будет использовать данный класс контекста для взаимодействия с базой данных. В целом этот сервис будет повторять тот, что был описан в
прошлой теме. Так, в папке Protos определим файл crud.proto
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
 ApplicationContext db;
 public UserApiService(ApplicationContext db)
 {
 this.db = db;
 }
 // отправляем список пользователей
 public override Task<ListReply> ListUsers(Empty request, ServerCallContext context)
 {
 var listReply = new ListReply(); // определяем список
 // преобразуем каждый объект User в объект UserReply
 var userList = db.Users.Select(item => new UserReply { Id = item.Id, Name = item.Name, Age = item.Age }).ToList();
 listReply.Users.AddRange(userList);
 return Task.FromResult(listReply);
 }
 // отправляем одного пользователя по id
 public override async Task<UserReply> GetUser(GetUserRequest request, ServerCallContext context)
 {
 var user = await db.Users.FindAsync(request.Id);
 // если пользователь не найден, генерируем исключение
 if (user == null)
 {
 throw new RpcException(new Status(StatusCode.NotFound, "User not found"));
 }
 UserReply userReply = new UserReply() { Id = user.Id, Name = user.Name, Age = user.Age };
 return await Task.FromResult(userReply);
 }
 // добавление пользователя
 public override async Task<UserReply> CreateUser(CreateUserRequest request, ServerCallContext context)
 {
 // формируем из данных объект User и добавляем его в список users
 var user = new User {Name = request.Name, Age = request.Age};
 await db.Users.AddAsync(user);
 await db.SaveChangesAsync();
 var reply = new UserReply() { Id = user.Id, Name = user.Name, Age = user.Age };
 return await Task.FromResult(reply);
 }
 // обновление пользователя
 public override async Task<UserReply> UpdateUser(UpdateUserRequest request, ServerCallContext context)
 {
 var user = await db.Users.FindAsync(request.Id);
 if (user == null)
 {
 throw new RpcException(new Status(StatusCode.NotFound, "User not found"));
 }
 // обновляем даннные
 user.Name = request.Name;
 user.Age = request.Age;
 await db.SaveChangesAsync();
 var reply = new UserReply() { Id = user.Id, Name = user.Name, Age = user.Age };
 return await Task.FromResult(reply);
 }
 // удаление пользователя
 public override async Task<UserReply> DeleteUser(DeleteUserRequest request, ServerCallContext context)
 {
 var user = await db.Users.FindAsync(request.Id);
 if (user == null)
 {
 throw new RpcException(new Status(StatusCode.NotFound, "User not found"));
 }
 // удаляем пользователя из бд
 db.Users.Remove(user);
 await db.SaveChangesAsync();
 var reply = new UserReply() { Id = user.Id, Name = user.Name, Age = user.Age };
 return await Task.FromResult(reply);
 }
}

```


Поскольку класс контекста ApplicationContext будет внедряться через систему Dependency Injection, и каждый класс в программе через конструктор может получить внедренные в приложении
зависимости, то класс сервиса также может получить контекст данных через конструктор:

```

ApplicationContext db;
public UserApiService(ApplicationContext db)
{
 this.db = db;
}

```


В методе `ListUsers` получаем из базы данных список объектов User, преобразуя их в тип UserReply:

```

public override Task<ListReply> ListUsers(Empty request, ServerCallContext context)
{
 var listReply = new ListReply(); // определяем список
 // преобразуем каждый объект User в объект UserReply
 var userList = db.Users.Select(item => new UserReply { Id = item.Id, Name = item.Name, Age = item.Age }).ToList();
 listReply.Users.AddRange(userList);
 return Task.FromResult(listReply);
}

```


В качестве параметра получаем пустой ответ, для которого используем специальный тип `Google.Protobuf.WellKnownTypes.Empty`. В самом методе определяем объект ListReply,
в его свойство `Users` передаем все объекты из базы данных, преобразуя их в тип UserReply. И отправляем сформированный объект ListReply клиенту.


В методе `GetUser` клиенту отправляем одного пользователя:

```

public override async Task<UserReply> GetUser(GetUserRequest request, ServerCallContext context)
{
 var user = await db.Users.FindAsync(request.Id);
 // если пользователь не найден, генерируем исключение
 if (user == null)
 {
 throw new RpcException(new Status(StatusCode.NotFound, "User not found"));
 }
 UserReply userReply = new UserReply() { Id = user.Id, Name = user.Name, Age = user.Age };
 return await Task.FromResult(userReply);
}

```


Из параметра request получаем id запрошенного пользователя и ищем соответствующий объект в базе даннных. Вполне возможно, что пользователь с указанным id не будет найден. В этом
случае генерируем исключение RpcException. В конструктор исключения мы можем передать объект Status, в котором с помощью свойства
StatusCode можно указать статусный код, аналогично тому, как это делается для установки статусных кодов в http. Кроме того, можно указать строку статуса с указанием причины ошибки.
И если будет сгенерировано исключение, то клиент получит эти данные.


Если же пользователь найден в базе даннных, то преобразуем его в тип UserReply и отправляем клиенту.


Остальные методы во многом похожи, меняются только конкретные операции контекста данных. Метод `CreateUser` добавляет одного пользователя в список. Метод `UpdateUser` по полученным данным обновляет определенного пользователя.
И метод `DeleteUser` удаляет по полученному id пользователя из базы данных. Во всех случаях результат метода отправляется пользователю.


В конце добавим зависимость ApplicationContext в сервисы приложения и включим сервис UserApiService в конвейер обработки запроса в файле Program.cs:

```

using CrudGrpcApp.Services;
using Microsoft.EntityFrameworkCore;

var builder = WebApplication.CreateBuilder(args);

// строка подключения
string connStr = "Data Source=grpc.db";
// добавляем контекст ApplicationContext в качестве сервиса в приложение
builder.Services.AddDbContext<ApplicationContext>(options => options.UseSqlite(connStr));
builder.Services.AddGrpc();

var app = builder.Build();


app.MapGrpcService<UserApiService>();
app.MapGet("/", () => "Hello METANIT.COM");

app.Run();

```


То есть получится следующий проект:
![CRUD и работа с базой данных через Entity Framework в сервисах ASP.NET Core GRPC на C#](https://metanit.com./pics/3.3.png)


### Тестирование на примере консольного клиента


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

// получение списка объектов
ListReply users = await client.ListUsersAsync(new Google.Protobuf.WellKnownTypes.Empty());

foreach (var user in users.Users)
{
 Console.WriteLine($"{user.Id}. {user.Name} - {user.Age}");
}

```


Поскольку сервер возвращает объект ListReply, то cоответственно на клиенте мы получаем этот объект и с помощью его свойства Users можем получить все данные пользователя в виде объекта UserReply.


В итоге приложение выведет на консоль полученные данные:

```

1. Tom - 37
2. Bob - 41
3. Sam - 24

```


Для тестирования получения одного объекта по id определим следующий код:

```

using Grpc.Core;
using Grpc.Net.Client;
using Metanit;

using var channel = GrpcChannel.ForAddress("https://localhost:7138");
var client = new UserService.UserServiceClient(channel);

try
{
 // получение одного объекта по id = 2
 UserReply user = await client.GetUserAsync(new GetUserRequest { Id = 2 });
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
UserReply user = await client.CreateUserAsync(new CreateUserRequest { Name = "Alice", Age = 32 });
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

**Источник:** [https://metanit.com/sharp/grpc/3.2.php](https://metanit.com/sharp/grpc/3.2.php)
