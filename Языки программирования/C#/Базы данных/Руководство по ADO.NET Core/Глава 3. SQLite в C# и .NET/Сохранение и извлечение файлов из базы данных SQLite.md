# Сохранение и извлечение файлов из базы данных SQLite

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Базы данных|Базы данных]] / [[Языки программирования/C#/Базы данных/Руководство по ADO.NET Core|Руководство по ADO.NET Core]] / [[Языки программирования/C#/Базы данных/Руководство по ADO.NET Core/Глава 3. SQLite в C# и .NET|Глава 3. SQLite в C# и .NET]] / Сохранение и извлечение файлов из базы данных SQLite

[[Языки программирования/C#/Базы данных/Руководство по ADO.NET Core/Глава 3. SQLite в C# и .NET/Получение скалярных значений в SQLite|Назад]] | [[Языки программирования/C#/Базы данных/Руководство по ADO.NET Core/Глава 3. SQLite в C# и .NET|Содержание]]

**Дата написания:** 05.09.2026

### Сохранение файлов

```csharp
byte[] imageData;
using (FileStream fs = new FileStream(filename, FileMode.Open))
{
    imageData = new byte[fs.Length];
    fs.Read(imageData, 0, imageData.Length);
}
using (var connection = new SqliteConnection("Data Source=filesdata.db"))
{
    connection.Open();
    SqliteCommand command = new SqliteCommand();
    command.Connection = connection;
    command.CommandText = @"INSERT INTO Files (Title, FileName, ImageData) VALUES (@FileName, @Title, @ImageData)";
    command.Parameters.Add(new SqliteParameter("@FileName", shortFileName));
    command.Parameters.Add(new SqliteParameter("@Title", title));
    command.Parameters.Add(new SqliteParameter("@ImageData", imageData));
    int number = command.ExecuteNonQuery();
}
```

### Извлечение файлов

```csharp
using (SqliteDataReader reader = command.ExecuteReader())
{
    if (reader.HasRows)
    {
        while (reader.Read())
        {
            int id = reader.GetInt32(0);
            string filename = reader.GetString(1);
            string title = reader.GetString(2);
            byte[] data = (byte[])reader.GetValue(3);
        }
    }
}
```

**Источник:** [https://metanit.com/sharp/adonetcore/4.7.php](https://metanit.com/sharp/adonetcore/4.7.php)
