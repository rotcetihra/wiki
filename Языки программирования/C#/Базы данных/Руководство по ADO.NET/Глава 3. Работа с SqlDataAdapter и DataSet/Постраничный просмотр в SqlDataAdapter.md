# Постраничный просмотр в SqlDataAdapter

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Базы данных|Базы данных]] / [[Языки программирования/C#/Базы данных/Руководство по ADO.NET|Руководство по ADO.NET]] / [[Языки программирования/C#/Базы данных/Руководство по ADO.NET/Глава 3. Работа с SqlDataAdapter и DataSet|Глава 3. Работа с SqlDataAdapter и DataSet]] / Постраничный просмотр в SqlDataAdapter

[[Языки программирования/C#/Базы данных/Руководство по ADO.NET/Глава 3. Работа с SqlDataAdapter и DataSet/SqlDataAdapter и DataSet|Назад]] | [[Языки программирования/C#/Базы данных/Руководство по ADO.NET/Глава 3. Работа с SqlDataAdapter и DataSet|Содержание]] | [[Языки программирования/C#/Базы данных/Руководство по ADO.NET/Глава 3. Работа с SqlDataAdapter и DataSet/SqlCommandBuilder и сохранение изменений DataSet в базе данных|Вперёд]]

**Дата написания:** 05.09.2026

Для постраничного просмотра используется метод Fill() с параметрами Skip и Take:

```csharp
adapter.Fill(ds, startIndex, count, "Users");
```

**Источник:** [https://metanit.com/sharp/adonet/3.2.php](https://metanit.com/sharp/adonet/3.2.php)
