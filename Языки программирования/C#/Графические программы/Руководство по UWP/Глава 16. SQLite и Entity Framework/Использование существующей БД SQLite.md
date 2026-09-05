# Использование существующей БД SQLite

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Графические программы|Графические программы]] / [[Языки программирования/C#/Графические программы/Руководство по UWP|Руководство по UWP]] / [[Языки программирования/C#/Графические программы/Руководство по UWP/Глава 16. SQLite и Entity Framework|Глава 16. SQLite и Entity Framework]] / Использование существующей БД SQLite

[[Языки программирования/C#/Графические программы/Руководство по UWP/Глава 16. SQLite и Entity Framework/Работа со сложными данными|Назад]] | [[Языки программирования/C#/Графические программы/Руководство по UWP/Глава 16. SQLite и Entity Framework|Содержание]] | [[Языки программирования/C#/Графические программы/Руководство по UWP/Глава 17. Дополнительные элементы управления/Стрелочный датчик|Вперёд]]

**Дата написания:** 05.09.2026

Использование существующей БД SQLiteПоследнее обновление: 14.03.2016
 
 
 

 
- 
 
- 
 
- 
 
 

 
 

 
 
 
 
 

 

В предыдущих темах мы рассмотрели процесс работы с базой данных SQLite, которая создается при первом запуске приложения. 
Теперь рассмотрим ситуацию, если у нас уже есть некоторая база данных, в которой имеются начальные данные, и нам эту базу данных надо подключить к проекту.

Продолжим работу с проектом из прошлой темы и вначале создадим саму базу данных SQLite. Для этого воспользуемся специальной программой Sqlitebrowser, которая предоставляет графический 
интерфейс для работы с базой данных SQLite. Эту программу можно найти по адресу [http://sqlitebrowser.org](http://sqlitebrowser.org).

После установки Sqlitebrowser откроем его и нажмем в меню на кнопку New Database:
![Sqlitebrowser и Universal Windows Platform](pics/17.10.png)

Определим для базы данных место и имя. Пусть она будет называться phones.db.

После этого Sqlitebrowser открывает новую базу данных. В ней еще ничего нет, никаких таблиц. Поэтому перейдем на вкладку Execute SQL и введем на ней 
в поле ввода следующие sql-выражения:

```
CREATE TABLE Phones(
 Id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, 
 Title TEXT,
 Price INTEGER,
 CompanyId INTEGER,
 FOREIGN KEY(CompanyId) REFERENCES Company(Id) ON DELETE CASCADE
);
CREATE TABLE Companies(
 Id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
 Name TEXT
);
```

![Создание таблиц в Sqlitebrowser](pics/17.11.png)

Эти sql-выражения позволят создать две таблицы: Company и Phone, которые будут связаны внешним ключом.

После ввода sql-выражений нажмем на панели на кнопку "Execute" или на клавишу F5 на клавиатуре, чтобы выполнить sql-выражения. 
И после этого будут созданы необходимые таблицы. Выберем таблицу Company и добавим в нее какие-нибудь данные:
![](pics/17.12.png)

Также добавим начальные данные и в таблицу Phone:
![](pics/17.13.png)

Итак, база данных у нас уже имеется. Теперь добавим ее в проект и установим у нее в панели свойств для параметра Build Action 
значение Content:
![Добавление базы данных в UWP](pics/17.14.png)

Теперь изменим класс контекста данных MobileContext, чтобы он использовал эту бд:

```
public class MobileContext : DbContext
{
 public DbSet Companies { get; set; }
 public DbSet Phones { get; set; }

 protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
 {
 optionsBuilder.UseSqlite("Filename=phones.db");
 }
}
```

База данных будет устанавливаться вместе с приложением в папку . Однако базы данных приложение берет из папки ApplicationData.Current.LocalFolder. Поэтому 
при первом запуске приложения нам надо выполнить копирование базы данных в ApplicationData.Current.LocalFolder. Для этого изменим класс App:

```
using System;
using Windows.ApplicationModel;
using Windows.ApplicationModel.Activation;
using Windows.UI.Xaml;
using Windows.UI.Xaml.Controls;
using Windows.UI.Xaml.Navigation;
using Windows.Storage;

sealed partial class App : Application
{
 public App()
 {
 this.InitializeComponent();
 this.Suspending += OnSuspending;
 }
 
 protected override async void OnLaunched(LaunchActivatedEventArgs e)
 {
 if(await ApplicationData.Current.LocalFolder.TryGetItemAsync("phones.db")==null)
 {
 StorageFile databaseFile = await Package.Current.InstalledLocation.GetFileAsync("phones.db");
 await databaseFile.CopyAsync(ApplicationData.Current.LocalFolder);
 }
 //.... остальное содержимое метода OnLaunched
 }
 
 //.... остальное содержимое класса App
}
```

Весь остальной код с прошлой темы можно не изменять. И при запуске приложения мы увидим на главной странице наши начальные данные:
![](pics/17.15.png)

---

**Источник:** [https://metanit.com/sharp/uwp/16.4.php](https://metanit.com/sharp/uwp/16.4.php)
