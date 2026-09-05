# Основные операции с данными в MongoDB и ASP.NET Web API

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Базы данных|Базы данных]] / [[Языки программирования/C#/Базы данных/Руководство по MongoDB|Руководство по MongoDB]] / [[Языки программирования/C#/Базы данных/Руководство по MongoDB/Глава 2. ASP.NET и MongoDB|Глава 2. ASP.NET и MongoDB]] / Основные операции с данными в MongoDB и ASP.NET Web API

[[Языки программирования/C#/Базы данных/Руководство по MongoDB/Глава 2. ASP.NET и MongoDB/Создание и настройка проекта для MongoDB|Назад]] | [[Языки программирования/C#/Базы данных/Руководство по MongoDB/Глава 2. ASP.NET и MongoDB|Содержание]] | [[Языки программирования/C#/Базы данных/Руководство по MongoDB/Глава 2. ASP.NET и MongoDB/Работа с файлами из базы данных MongoDB и GridFS в ASP.NET|Вперёд]]

**Дата написания:** 05.09.2026

Определим простейший Web API, который будет выполнять все основные операции с данными в бд MongoDB.

```csharp
var client = new MongoClient("mongodb://localhost:27017");
var db = client.GetDatabase("test");
var collectionName = "users";

app.MapGet("/api/users", () =>
    db.GetCollection<Person>(collectionName).Find("{}").ToListAsync());

app.MapGet("/api/users/{id}", async (string id) =>
{
    var user = await db.GetCollection<Person>(collectionName)
        .Find(p=>p.Id == id)
        .FirstOrDefaultAsync();
    if (user == null) return Results.NotFound(new { message = "Пользователь не найден" });
    return Results.Json(user);
});

app.MapPost("/api/users", async (Person user) => {
    await db.GetCollection<Person>(collectionName).InsertOneAsync(user);
    return user;
});

app.MapPut("/api/users", async (Person userData) => {
    var user = await db.GetCollection<Person>(collectionName)
        .FindOneAndReplaceAsync(p => p.Id == userData.Id, userData, new() { ReturnDocument = ReturnDocument.After });
    if (user == null) 
        return Results.NotFound(new { message = "Пользователь не найден" });
    return Results.Json(user);
});

app.MapDelete("/api/users/{id}", async (string id) =>
{
    var user = await db.GetCollection<Person>(collectionName).FindOneAndDeleteAsync(p=>p.Id==id);
    if (user is null) return Results.NotFound(new { message = "Пользователь не найден" });
    return Results.Json(user);
});
```

**Источник:** [https://metanit.com/sharp/mongodb/2.2.php](https://metanit.com/sharp/mongodb/2.2.php)
