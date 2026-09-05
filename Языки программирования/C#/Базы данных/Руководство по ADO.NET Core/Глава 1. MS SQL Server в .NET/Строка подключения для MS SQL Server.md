# Строка подключения для MS SQL Server

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Базы данных|Базы данных]] / [[Языки программирования/C#/Базы данных/Руководство по ADO.NET Core|Руководство по ADO.NET Core]] / [[Языки программирования/C#/Базы данных/Руководство по ADO.NET Core/Глава 1. MS SQL Server в .NET|Глава 1. MS SQL Server в .NET]] / Строка подключения для MS SQL Server

[[Языки программирования/C#/Базы данных/Руководство по ADO.NET Core/Глава 1. MS SQL Server в .NET/Подключение к MS SQL Server|Вперёд]]

**Дата написания:** 05.09.2026

Для работы с MS SQL Server естественно нам потребуется MS SQL Server. Строка подключения представляет набор параметров в виде пар `ключ=значение`, которые отделяются друг от друга точкой с запятой.

Для подключения по логину и паролю:

```
Server=адрес_сервера;Database=имя_базы_данных;User Id=логин;Password=пароль;
```

Для доверенного подключения (trusted connection):

```
Server=адрес_сервера;Database=имя_базы_данных;Trusted_Connection=True;
```

Адреса серверов:
-   Полноценный SQL Server: `localhost` или `.`
-   SQL Server Express: `.\SQLEXPRESS`
-   LocalDB: `(localdb)\mssqllocaldb`

**Источник:** [https://metanit.com/sharp/adonetcore/2.1.php](https://metanit.com/sharp/adonetcore/2.1.php)
