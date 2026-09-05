# Работа с файлами из базы данных MongoDB и GridFS в ASP.NET

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Базы данных|Базы данных]] / [[Языки программирования/C#/Базы данных/Руководство по MongoDB|Руководство по MongoDB]] / [[Языки программирования/C#/Базы данных/Руководство по MongoDB/Глава 2. ASP.NET и MongoDB|Глава 2. ASP.NET и MongoDB]] / Работа с файлами из базы данных MongoDB и GridFS в ASP.NET

[[Языки программирования/C#/Базы данных/Руководство по MongoDB/Глава 2. ASP.NET и MongoDB/Основные операции с данными в MongoDB и ASP.NET Web API|Назад]] | [[Языки программирования/C#/Базы данных/Руководство по MongoDB/Глава 2. ASP.NET и MongoDB|Содержание]]

**Дата написания:** 05.09.2026

GridFS позволяет сохранять и получать из БД MongoDB файлы. Для работы в ASP.NET Core необходимо добавить в проект Nuget-пакет MongoDB.Driver.GridFS.

Основные конечные точки:

-   **GET /**: список файлов из GridFS
-   **GET /file/{id}**: получение файла по id
-   **POST /delete/{id}**: удаление файла по id
-   **GET /upload**: страница для загрузки файлов
-   **POST /upload**: загрузка файлов в GridFS

```csharp
IGridFSBucket gridFS = new GridFSBucket(db);

// получение файла
await gridFS.DownloadToStreamAsync(new ObjectId(id), context.Response.Body);

// удаление файла
await gridFS.DeleteAsync(new ObjectId(id));

// загрузка файла
foreach (var file in context.Request.Form.Files)
{
    using (var stream = file.OpenReadStream())
    {
        await gridFS.UploadFromStreamAsync(file.FileName, stream);
    }
}
```

**Источник:** [https://metanit.com/sharp/mongodb/2.3.php](https://metanit.com/sharp/mongodb/2.3.php)
