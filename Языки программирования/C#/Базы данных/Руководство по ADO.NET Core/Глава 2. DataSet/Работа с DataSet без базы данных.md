# Работа с DataSet без базы данных

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Базы данных|Базы данных]] / [[Языки программирования/C#/Базы данных/Руководство по ADO.NET Core|Руководство по ADO.NET Core]] / [[Языки программирования/C#/Базы данных/Руководство по ADO.NET Core/Глава 2. DataSet|Глава 2. DataSet]] / Работа с DataSet без базы данных

[[Языки программирования/C#/Базы данных/Руководство по ADO.NET Core/Глава 2. DataSet/SqlDataAdapter и загрузка данных в DataSet|Назад]] | [[Языки программирования/C#/Базы данных/Руководство по ADO.NET Core/Глава 2. DataSet|Содержание]] | [[Языки программирования/C#/Базы данных/Руководство по ADO.NET Core/Глава 2. DataSet/Сохранение изменений DataSet в базе данных|Вперёд]]

**Дата написания:** 05.09.2026

DataSet можно использовать без подключения к базе данных:

```csharp
DataSet usersSet = new DataSet("UsersSet");
DataTable users = new DataTable("Users");
usersSet.Tables.Add(users);

DataColumn idColumn = new DataColumn("Id", Type.GetType("System.Int32"));
idColumn.AutoIncrement = true;
idColumn.AutoIncrementSeed = 1;
idColumn.AutoIncrementStep = 1;

DataColumn nameColumn = new DataColumn("Name", Type.GetType("System.String"));
DataColumn ageColumn = new DataColumn("Age", Type.GetType("System.Int32"));

users.Columns.Add(idColumn);
users.Columns.Add(nameColumn);
users.Columns.Add(ageColumn);
users.PrimaryKey = new DataColumn[] { users.Columns["Id"] };

DataRow row = users.NewRow();
row.ItemArray = new object[] { null, "Tom", 36 };
users.Rows.Add(row);
users.Rows.Add(new object[] { null, "Bob", 29 });
```

**Источник:** [https://metanit.com/sharp/adonetcore/3.2.php](https://metanit.com/sharp/adonetcore/3.2.php)
