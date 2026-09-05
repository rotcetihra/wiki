# Lazy loading

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Базы данных|Базы данных]] / [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 5|Руководство по Entity Framework Core 5]] / [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 5/Глава 3. Отношения между моделями|Глава 3. Отношения между моделями]] / Lazy loading

[[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 5/Глава 3. Отношения между моделями/Explicit loading|Назад]] | [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 5/Глава 3. Отношения между моделями|Содержание]] | [[Языки программирования/C#/Базы данных/Руководство по Entity Framework Core 5/Глава 3. Отношения между моделями/Отношение один к одному|Вперёд]]

**Дата написания:** 05.09.2026

Lazy loading предполагает автоматическую загрузку связанных данных при обращении к навигационному свойству. Требует пакет Microsoft.EntityFrameworkCore.Proxies и виртуальных свойств:

```csharp
optionsBuilder.UseLazyLoadingProxies();

public virtual Company? Company { get; set; }
```

**Источник:** [https://metanit.com/sharp/entityframeworkcore/3.9.php](https://metanit.com/sharp/entityframeworkcore/3.9.php)
