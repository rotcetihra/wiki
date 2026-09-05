# Сопоставление типов C# и SQLite. Типизация SqliteDataReader

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Базы данных|Базы данных]] / [[Языки программирования/C#/Базы данных/Руководство по ADO.NET Core|Руководство по ADO.NET Core]] / [[Языки программирования/C#/Базы данных/Руководство по ADO.NET Core/Глава 3. SQLite в C# и .NET|Глава 3. SQLite в C# и .NET]] / Сопоставление типов C# и SQLite

[[Языки программирования/C#/Базы данных/Руководство по ADO.NET Core/Глава 3. SQLite в C# и .NET/Чтение результатов запроса и SqliteDataReader|Назад]] | [[Языки программирования/C#/Базы данных/Руководство по ADO.NET Core/Глава 3. SQLite в C# и .NET|Содержание]] | [[Языки программирования/C#/Базы данных/Руководство по ADO.NET Core/Глава 3. SQLite в C# и .NET/Параметризация запросов к БД Sqlite|Вперёд]]

**Дата написания:** 05.09.2026

Для получения типизированных данных применяются методы GetInt32(), GetString() и т.д.:

```csharp
while (reader.Read())
{
    int id = reader.GetInt32(0);
    String name = reader.GetString(1);
    int age = reader.GetInt32(2);
    Console.WriteLine($"{id} \t {name} \t {age}");
}
```

SQLite имеет только четыре примитивных типа: INTEGER, REAL, TEXT и BLOB.

| Тип C# | Тип SQLite |
|--------|-----------|
| int | INTEGER |
| string | TEXT |
| double | REAL |
| byte[] | BLOB |
| bool | INTEGER (0 или 1) |
| DateTime | TEXT |

**Источник:** [https://metanit.com/sharp/adonetcore/4.4.php](https://metanit.com/sharp/adonetcore/4.4.php)
