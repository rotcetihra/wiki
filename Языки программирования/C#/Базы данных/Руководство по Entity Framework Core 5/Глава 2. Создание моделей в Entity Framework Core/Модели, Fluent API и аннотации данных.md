# Модели, Fluent API и аннотации данных

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Базы данных|Базы данных]] / [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 5|Руководство по Entity Framework Core 5]] / [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 5/Глава 2. Создание моделей в Entity Framework Core|Глава 2. Создание моделей в Entity Framework Core]] / Модели, Fluent API и аннотации данных

[[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 5/Глава 1. Введение в Entity Framework Core/Провайдеры логгирования|Назад]] | [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 5/Глава 2. Создание моделей в Entity Framework Core|Содержание]] | [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 5/Глава 2. Создание моделей в Entity Framework Core/Управление схемой БД и миграции|Вперёд]]

**Дата написания:** 05.09.2026

Все сущности, с которыми работает EntityFramework Core, определяются в виде классов моделей. EF Core использует ряд условностей для сопоставления классов моделей с таблицами.

### Fluent API

Fluent API представляет набор методов, которые определяют сопоставление между классами и их свойствами и таблицами и их столбцами:

```csharp
protected override void OnModelCreating(ModelBuilder modelBuilder)
{
    // использование Fluent API
}
```

### Аннотации

Аннотации представляют настройку классов моделей с помощью атрибутов:

```csharp
using System.ComponentModel.DataAnnotations;

public class User
{
    public int Id { get; set; }
    [Required]
    public string Name { get; set; }
    public int Age { get; set; }
}
```

Таким образом, мы можем использовать три подхода к определению моделей:

-   Условности (conventions)
-   Fluent API
-   Аннотации данных

**Источник:** [https://metanit.com/sharp/entityframeworkcore/2.3.php](https://metanit.com/sharp/entityframeworkcore/2.3.php)
