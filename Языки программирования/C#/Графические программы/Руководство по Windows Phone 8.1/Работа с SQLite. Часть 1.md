# Работа с SQLite. Часть 1

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Графические программы|Графические программы]] / [[Языки программирования/C#/Графические программы/Руководство по Windows Phone 8.1|Руководство по Windows Phone 8.1]] / [[Языки программирования/C#/Графические программы/Руководство по Windows Phone 8.1/Глава 14. SQLite в Windows Phone 8.1|Глава 14. SQLite в Windows Phone 8.1]] / Работа с SQLite. Часть 1

[[Языки программирования/C#/Графические программы/Руководство по Windows Phone 8.1/Глава 13. Локализация приложений/Локализация приложений|Назад]] | [[Языки программирования/C#/Графические программы/Руководство по Windows Phone 8.1/Глава 14. SQLite в Windows Phone 8.1|Содержание]] | [[Языки программирования/C#/Графические программы/Руководство по Windows Phone 8.1/Глава 14. SQLite в Windows Phone 8.1/Работа с SQLite. Часть 2|Вперёд]]

**Дата написания:** 05.09.2026

## Работа с SQLite. Часть 1
Последнее обновление: 31.10.2015





-

-

-














**SQLite** представляет одну из наиболее распространенных реляционных СУБД, которая обладает такими преимуществами, как компактность, 
кроссплатформенность, переносимость. Поэтому базы данных SQLite нередко используются в мобильной разработке для разных ОС. Рассмотрим,
как мы можем использовать SQLite при программирования для Windows Phone 8.1.


### Добавление расширений


Для работы с SQLite создадим проект по типу Blank App. И вначале нам надо подключить в Visual Studio расширения. Для этого в главном меню Visual Studio выберем пункты 
TOOLS -> Extensions and Updates


Здесь нам надо установить два расширения: **SQLite for Windows Phone 8.1** и **SQLite for Windows Runtime (Windows 8.1)**

_

После их установки добавим в проект соответствующую библиотеку. Для этого нажмем правой кнопкой мыши на узел References ->Add Reference 
и в списке выберем библиотеку **SQLite for Windows Phone 8.1**:



После этого в проект будет добавлена данная библиотека. Для взаимодействия с кодом c# также надо добавить еще одну библиотеку, которая 
позволит нам создавать запросы к базе данных. Для этого нажмем правой кнопкой мыши на узел References ->Manage NuGet Packages... 
и в поле поиска введем sqlite-pcl_:



В списке найдем библиотеку **Portable Class Library for SQLite** и установим ее.


После добавления в узле References окажутся две одинаковые библиотеки, но с разными версиями:



Библиотеку с более ранней версией мы можем удалить.


Рядом со второй библиотекой будет отображаться желтый треугольник, который показывает, что библиотека не может применяться к любому процессору. 
А если мы посмотрим на настройки отладки проекта, то увидим, что для проекта установлено Any CPU. Так как цель нашего приложения 
- смартфон, то изменим тип процессора на ARM:



Создаваемое приложение будет очень простым. Пусть оно будет выводить список книг из библиотеки, а также предоставлять функционал для управления обектами - 
их созданием, удалением, редактированием и т.д.


И первым делом добавим в проект класс модели, которая будет использоваться - класс Book:


```

public class Book
{
 public long Id { get; set; }
 public string Name { get; set; }
 public string Author { get; set; }
 public long Year { get; set; }
}

```


Чтобы легче управлять объектами, было бы лучше создать какую-нибудь абстракцию наподобие репозитория. Поэтому добавим в проект 
еще один класс BookRepository:


```

using SQLitePCL;
using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;

namespace SQLLiteApp
{
 public class BookRepository
 {
 public SQLiteConnection con;
 public BookRepository(string dbname)
 {
 this.con = new SQLiteConnection(dbname);
 }
 public void CreateTable()
 {
 string sql = @"CREATE TABLE IF NOT EXISTS
 Book (Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
 Name VARCHAR(100),
 Author VARCHAR(100),
 Year INTEGER);";
 using (var statement = con.Prepare(sql))
 {
 statement.Step();
 }
 }

 public void Insert(Book book)
 {
 using (var statement = con.Prepare("INSERT INTO Book(Name, Author, Year) VALUES (?,?,?)"))
 {
 statement.Bind(1, book.Name);
 statement.Bind(2, book.Author);
 statement.Bind(3, book.Year);
 statement.Step();
 }
 }

 public ObservableCollection GetBooks()
 {
 ObservableCollection books = new ObservableCollection();

 using (var statement = con.Prepare("SELECT Id, Name, Author, Year FROM Book"))
 {
 while (statement.Step() == SQLiteResult.ROW)
 {
 Book book = new Book();
 book.Id = (long)statement[0];
 book.Name = (string)statement[1];
 book.Author = (string)statement[2];
 book.Year = (long)statement[3];
 books.Add(book);
 }
 }
 return books;
 }

 public Book GetBook(long id)
 {
 Book book = null;

 using (var statement = con.Prepare("SELECT Id, Name, Author, Year FROM Book WHERE Id=?"))
 {
 statement.Bind(1, id);
 if (statement.Step()==SQLiteResult.ROW)
 {
 book = new Book();
 book.Id = (long)statement[0];
 book.Name = (string)statement[1];
 book.Author = (string)statement[2];
 book.Year = (long)statement[3];
 }
 }

 return book;
 }

 public void Update(Book book)
 {
 using (var statement = con.Prepare("UPDATE Book SET Name=?, Author=?, Year=? WHERE Id=?"))
 {
 statement.Bind(1, book.Name);
 statement.Bind(2, book.Author);
 statement.Bind(3, book.Year);
 statement.Bind(4, book.Id);
 statement.Step();
 }
 }

 public void Delete(long id)
 {
 using (var statement = con.Prepare("DELETE FROM Book WHERE Id=?"))
 {
 statement.Bind(1, id);
 statement.Step();
 }
 }
 }
}

```


Этот класс производит основную работу с базой данных, и все взаимодействие будет идти через его методы.


Для управления бд в классе определяется переменная типа SQLiteConnection


Метод `CreateTable()` создает таблицу в бд, если таблица еще не создана. Для выполенния sql-запросов используются методы 
`Prepare` и `Step()`:


```

using (var statement = con.Prepare(sql))
{
 statement.Step();
}

```


Методы `Insert()`, `Update()` и `Delete()` соответственно добавляют, обновляют и удаляют объекты. Здесь 
опять же используется практически стандартный синтаксис запросов sql за тем исключением, что для связи параметров с запросом используется метод 
`Bind`. Он связывает значения с параметрами, например, `statement.Bind(1, book.Name)`


И методы `GetBooks()` и `GetBook()` соответственно получают набор объектов и один единственный объект по id.


Теперь добавим в проект страницы и определим логику для манипуляции объектами из пользовательского интерфейса.








 <div

**Источник:** [https://metanit.com/sharp/windowsphone/14.1.php](https://metanit.com/sharp/windowsphone/14.1.php)
