# Получение скалярных значений в SQLite

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Базы данных|Базы данных]] / [[Языки программирования/C#/Базы данных/Руководство по ADO.NET Core|Руководство по ADO.NET Core]] / [[Языки программирования/C#/Базы данных/Руководство по ADO.NET Core/Глава 3. SQLite в C# и .NET|Глава 3. SQLite в C# и .NET]] / Получение скалярных значений в SQLite

[[Языки программирования/C#/Базы данных/Руководство по ADO.NET Core/Глава 3. SQLite в C# и .NET/Параметризация запросов к БД Sqlite|Назад]] | [[Языки программирования/C#/Базы данных/Руководство по ADO.NET Core/Глава 3. SQLite в C# и .NET|Содержание]] | [[Языки программирования/C#/Базы данных/Руководство по ADO.NET Core/Глава 3. SQLite в C# и .NET/Сохранение и извлечение файлов из базы данных SQLite|Вперёд]]

**Дата написания:** 05.09.2026

Метод ExecuteScalar() позволяет получать из SQLite скалярный результат:

```csharp
string sqlExpression = "SELECT COUNT(*) FROM Users";
SqliteCommand command = new SqliteCommand(sqlExpression, connection);
object count = command.ExecuteScalar();

command.CommandText = "SELECT MIN(Age) FROM Users";
object minAge = command.ExecuteScalar();

command.CommandText = "SELECT AVG(Age) FROM Users";
object avgAge = command.ExecuteScalar();
```

**Источник:** [https://metanit.com/sharp/adonetcore/4.6.php](https://metanit.com/sharp/adonetcore/4.6.php)
