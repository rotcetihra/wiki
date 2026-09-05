# Подключение к базе данных SQLite

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Базы данных|Базы данных]] / [[Языки программирования/C#/Базы данных/Руководство по ADO.NET Core|Руководство по ADO.NET Core]] / [[Языки программирования/C#/Базы данных/Руководство по ADO.NET Core/Глава 3. SQLite в C# и .NET|Глава 3. SQLite в C# и .NET]] / Подключение к базе данных SQLite

[[Языки программирования/C#/Базы данных/Руководство по ADO.NET Core/Глава 2. DataSet/Сохранение изменений DataSet в базе данных|Назад]] | [[Языки программирования/C#/Базы данных/Руководство по ADO.NET Core/Глава 3. SQLite в C# и .NET|Содержание]] | [[Языки программирования/C#/Базы данных/Руководство по ADO.NET Core/Глава 3. SQLite в C# и .NET/Выполнение запросов к БД SQLite и SqliteCommand|Вперёд]]

**Дата написания:** 05.09.2026

Для работы с SQLite в C# необходимо установить через Nuget пакет Microsoft.Data.Sqlite. Для подключения применяется класс SqliteConnection:

```csharp
using (var connection = new SqliteConnection("Data Source=usersdata.db"))
{
    connection.Open();
}
```

Параметры строки подключения:
-   **Data Source**: путь к файлу базы данных
-   **Mode**: ReadWriteCreate (по умолчанию), ReadWrite, ReadOnly, Memory
-   **Cache**: Default, Private, Shared

Если база данных из строки подключения не существует, то при вызове `Open()` она создается автоматически.

**Источник:** [https://metanit.com/sharp/adonetcore/4.1.php](https://metanit.com/sharp/adonetcore/4.1.php)
