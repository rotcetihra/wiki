# SqlDataAdapter и загрузка данных в DataSet

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Базы данных|Базы данных]] / [[Языки программирования/C#/Базы данных/Руководство по ADO.NET Core|Руководство по ADO.NET Core]] / [[Языки программирования/C#/Базы данных/Руководство по ADO.NET Core/Глава 2. DataSet|Глава 2. DataSet]] / SqlDataAdapter и загрузка данных в DataSet

[[Языки программирования/C#/Базы данных/Руководство по ADO.NET Core/Глава 1. MS SQL Server в .NET/Сохранение и извлечение файлов из базы данных|Назад]] | [[Языки программирования/C#/Базы данных/Руководство по ADO.NET Core/Глава 2. DataSet|Содержание]] | [[Языки программирования/C#/Базы данных/Руководство по ADO.NET Core/Глава 2. DataSet/Работа с DataSet без базы данных|Вперёд]]

**Дата написания:** 05.09.2026

DataSet представляет хранилище или кэш данных в памяти, извлеченных из источника данных. Для заполнения DataSet применяется класс SqlDataAdapter.

```csharp
string connectionString = "Server=(localdb)\\mssqllocaldb;Database=adonetdb;Trusted_Connection=True;";
string sql = "SELECT * FROM Users";
using (SqlConnection connection = new SqlConnection(connectionString))
{
    SqlDataAdapter adapter = new SqlDataAdapter(sql, connection);
    DataSet ds = new DataSet();
    adapter.Fill(ds);

    foreach (DataTable dt in ds.Tables)
    {
        foreach (DataColumn column in dt.Columns)
            Console.Write($"{column.ColumnName}\t");
        Console.WriteLine();
        foreach (DataRow row in dt.Rows)
        {
            var cells = row.ItemArray;
            foreach (object cell in cells)
                Console.Write($"{cell}\t");
            Console.WriteLine();
        }
    }
}
```

**Источник:** [https://metanit.com/sharp/adonetcore/3.1.php](https://metanit.com/sharp/adonetcore/3.1.php)
