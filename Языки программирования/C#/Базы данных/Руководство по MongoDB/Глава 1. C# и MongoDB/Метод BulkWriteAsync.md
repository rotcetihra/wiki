# Метод BulkWriteAsync

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Базы данных|Базы данных]] / [[Языки программирования/C#/Базы данных/Руководство по MongoDB|Руководство по MongoDB]] / [[Языки программирования/C#/Базы данных/Руководство по MongoDB/Глава 1. C# и MongoDB|Глава 1. C# и MongoDB]] / Метод BulkWriteAsync

[[Языки программирования/C#/Базы данных/Руководство по MongoDB/Глава 1. C# и MongoDB/Удаление документов|Назад]] | [[Языки программирования/C#/Базы данных/Руководство по MongoDB/Глава 1. C# и MongoDB|Содержание]] | [[Языки программирования/C#/Базы данных/Руководство по MongoDB/Глава 1. C# и MongoDB/Хранение файлов в базе данных и GridFS|Вперёд]]

**Дата написания:** 05.09.2026

Для увеличения производительности для массовой записи данных мы можем применять метод BulkWriteAsync(). Метод принимает массив объектов WriteModel:

-   DeleteOneModel / DeleteManyModel: удаление
-   UpdateOneModel / UpdateManyModel: обновление
-   InsertOneModel: добавление
-   ReplaceOneModel: замена

```csharp
await collection.BulkWriteAsync(new WriteModel<BsonDocument>[]
{
    new InsertOneModel<BsonDocument>(new BsonDocument{{"Name", "Sam"}, {"Age", 28 } }),
    new InsertOneModel<BsonDocument>(new BsonDocument{{"Name", "Bob"}, {"Age", 42 } }),
    new InsertOneModel<BsonDocument>(new BsonDocument{{"Name", "Alice"}, {"Age", 33 } })
});
```

**Источник:** [https://metanit.com/sharp/mongodb/1.16.php](https://metanit.com/sharp/mongodb/1.16.php)
