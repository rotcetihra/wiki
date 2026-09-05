# Хранение файлов в базе данных и GridFS

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Базы данных|Базы данных]] / [[Языки программирования/C#/Базы данных/Руководство по MongoDB|Руководство по MongoDB]] / [[Языки программирования/C#/Базы данных/Руководство по MongoDB/Глава 1. C# и MongoDB|Глава 1. C# и MongoDB]] / Хранение файлов в базе данных и GridFS

[[Языки программирования/C#/Базы данных/Руководство по MongoDB/Глава 1. C# и MongoDB/Метод BulkWriteAsync|Назад]] | [[Языки программирования/C#/Базы данных/Руководство по MongoDB/Глава 1. C# и MongoDB|Содержание]] | [[Языки программирования/C#/Базы данных/Руководство по MongoDB/Глава 2. ASP.NET и MongoDB/Создание и настройка проекта для MongoDB|Вперёд]]

**Дата написания:** 05.09.2026

Для хранения больших объемов информации, в частности, файлов, в MongoDB используется система GridFS. Для работы с ней необходимо установить через Nuget пакет MongoDB.Driver.GridFS.

```csharp
using MongoDB.Driver;
using MongoDB.Driver.GridFS;

MongoClient client = new MongoClient("mongodb://localhost:27017");
var db = client.GetDatabase("test");
IGridFSBucket gridFS = new GridFSBucket(db);
```

### Сохранение файлов в базу данных

```csharp
using Stream fs = File.OpenRead("D:\\cats.jpg");
ObjectId id = await gridFS.UploadFromStreamAsync("cats.jpg", fs);
Console.WriteLine($"id файла: {id}");
```

### Чтение файлов из GridFS

```csharp
using Stream fs = File.OpenWrite("D:\\new_cats.jpg");
await gridFS.DownloadToStreamByNameAsync("cats.jpg", fs);
```

### Поиск файла

```csharp
var filter = Builders<GridFSFileInfo>.Filter.Eq(info => info.Filename, "cats.jpg");
var fileInfos = await gridFS.FindAsync(filter);
var fileInfo = fileInfos.FirstOrDefault();
Console.WriteLine($"id = {fileInfo?.Id}");
```

### Удаление файлов

```csharp
await gridFS.DeleteAsync(fileInfo.Id);
```

**Источник:** [https://metanit.com/sharp/mongodb/1.17.php](https://metanit.com/sharp/mongodb/1.17.php)
