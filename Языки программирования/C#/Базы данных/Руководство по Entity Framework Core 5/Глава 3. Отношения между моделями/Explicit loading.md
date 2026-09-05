# Explicit loading

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Базы данных|Базы данных]] / [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 5|Руководство по Entity Framework Core 5]] / [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 5/Глава 3. Отношения между моделями|Глава 3. Отношения между моделями]] / Explicit loading

[[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 5/Глава 3. Отношения между моделями/Загрузка связанных данных. Метод Include|Назад]] | [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 5/Глава 3. Отношения между моделями|Содержание]] | [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 5/Глава 3. Отношения между моделями/Lazy loading|Вперёд]]

**Дата написания:** 05.09.2026

Explicit loading предполагает явную загрузку данных с помощью метода Load():

```csharp
db.Entry(company).Collection(c => c.Users).Load();
```

Для одиночного объекта:

```csharp
db.Entry(user).Reference(u => u.Company).Load();
```

**Источник:** [https://metanit.com/sharp/entityframeworkcore/3.8.php](https://metanit.com/sharp/entityframeworkcore/3.8.php)
