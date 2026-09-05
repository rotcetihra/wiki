# Создание и настройка проекта для MongoDB

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Базы данных|Базы данных]] / [[Языки программирования/C#/Базы данных/Руководство по MongoDB|Руководство по MongoDB]] / [[Языки программирования/C#/Базы данных/Руководство по MongoDB/Глава 2. ASP.NET и MongoDB|Глава 2. ASP.NET и MongoDB]] / Создание и настройка проекта для MongoDB

[[Языки программирования/C#/Базы данных/Руководство по MongoDB/Глава 1. C# и MongoDB/Хранение файлов в базе данных и GridFS|Назад]] | [[Языки программирования/C#/Базы данных/Руководство по MongoDB/Глава 2. ASP.NET и MongoDB|Содержание]] | [[Языки программирования/C#/Базы данных/Руководство по MongoDB/Глава 2. ASP.NET и MongoDB/Основные операции с данными в MongoDB и ASP.NET Web API|Вперёд]]

**Дата написания:** 05.09.2026

Для взаимодействия с сервером Mongo через пакетный менеджер Nuget установим пакет MongoDB.Driver.

Согласно документации MongoDB предпочтительно создавать один экземпляр MongoClient и использовать его внутри остальных частей приложения. Для этого можно определить его как синглтон:

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services.AddSingleton(new MongoClient("mongodb://localhost:27017"));
var app = builder.Build();
```

**Источник:** [https://metanit.com/sharp/mongodb/2.1.php](https://metanit.com/sharp/mongodb/2.1.php)
