# Сохранение изменений DataSet в базе данных

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Базы данных|Базы данных]] / [[Языки программирования/C#/Базы данных/Руководство по ADO.NET Core|Руководство по ADO.NET Core]] / [[Языки программирования/C#/Базы данных/Руководство по ADO.NET Core/Глава 2. DataSet|Глава 2. DataSet]] / Сохранение изменений DataSet в базе данных

[[Языки программирования/C#/Базы данных/Руководство по ADO.NET Core/Глава 2. DataSet/Работа с DataSet без базы данных|Назад]] | [[Языки программирования/C#/Базы данных/Руководство по ADO.NET Core/Глава 2. DataSet|Содержание]] | [[Языки программирования/C#/Базы данных/Руководство по ADO.NET Core/Глава 3. SQLite в C# и .NET/Подключение к базе данных SQLite|Вперёд]]

**Дата написания:** 05.09.2026

Для сохранения изменений DataSet в базу данных используется метод Update() объекта SqlDataAdapter. SqlCommandBuilder автоматически генерирует нужные sql-выражения:

```csharp
DataTable dt = ds.Tables[0];
// добавим новую строку
DataRow newRow = dt.NewRow();
newRow["Name"] = "Rick";
newRow["Age"] = 24;
dt.Rows.Add(newRow);

// Изменим значение в столбце Age для первой строки
dt.Rows[0]["Age"] = 17;

SqlCommandBuilder commandBuilder = new SqlCommandBuilder(adapter);
adapter.Update(ds);

ds.Clear();
adapter.Fill(ds);
```

**Источник:** [https://metanit.com/sharp/adonetcore/3.3.php](https://metanit.com/sharp/adonetcore/3.3.php)
