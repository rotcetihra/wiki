# Работа с SQLite через Entity Framework

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Графические программы|Графические программы]] / [[Языки программирования/C#/Графические программы/Руководство по WPF|Руководство по WPF]] / [[Языки программирования/C#/Графические программы/Руководство по WPF/Глава 21. Взаимодействие с базой данных|Глава 21. Взаимодействие с базой данных]] / Работа с SQLite через Entity Framework

[[Языки программирования/C#/Графические программы/Руководство по WPF/Глава 20. Паттерн MVVM/Работа с диалоговыми окнами|Назад]] | [[Языки программирования/C#/Графические программы/Руководство по WPF/Глава 21. Взаимодействие с базой данных|Содержание]] | [[Языки программирования/C#/Графические программы/Руководство по WPF/Глава 21. Взаимодействие с базой данных/MVVM и SQLite|Вперёд]]

**Дата написания:** 05.09.2026

## Работа с SQLite через Entity Framework
Последнее обновление: 26.07.2022





-

-

-














SQLite является одной из наиболее используемых систем управления базами данных. Главным преимуществом SQLite является то, что для базы данных не нужно сервера. База данных представляет собой обычный 
локальный файл, который мы можем перемещать вместе с главным файлом приложения. Кроме того, для запросов к базе данных мы можем использовать стандартные выражения 
языка SQL, которые равным образом с некоторыми изменениями могут применяться и в других СУБД как Oracle, MS SQL Server, MySQL, Postgres и т.д.


Еще одним преимуществом является широкое распространение SQLite - область применения охватывает множество платфрм и технологий: WPF, Windows Forms, UWP, Android, iOS и т.д. 
И если мы, скажем, захотим создать копию приложения для ОС Android, то базу данных мы можем перенести в новое приложение такой, как она определена для приложения на WPF.


Но в данном случае для упрощения мы будет работать с базой данных SQLite через специальный ORM-фреймворк Entity Framework. В данном случае мы сосредоточимся на тех моментах, которые 
характерны для проекта WPF. Но при необходимости дополнительную информацию можно найти по следующим ссылкам: [SQLite в C# и .NET](https://metanit.com/sharp/adonetcore/4.1.php) 
и [Руководство по Entity Framework](https://metanit.com/sharp/efcore/)


Итак, создадим новый проект WPF, который назовем SQLiteApp. В первую очередь нам надо добавить функциональность SQLite и Entity Framework в проект. Для этого 
необходимо добавить в проект через пакетный менеджер Nuget пакет Microsoft.EntityFrameworkCore.Sqlite. Итак, перейдем к Nuget, нажав в проекте правой кнопкой 
на узел Dependences и выбрав в открывшемся контекстном меню пункт Manage NuGet Packages...:



В окне менеджера Nuget введем в окно поиска "Microsoft.EntityFrameworkCore.Sqlite", и менеджер отобразит нам ряд результатов. Из них нам надо установить пакет под названием 
Microsoft.EntityFrameworkCore.Sqlite:



Итак, для работы с базой данных нам естественно понадобится сама база данных. Однако если у нас нет никакой БД, как в данном случае, мы можем воспользоваться подходом Code First, 
чтобы Entity Framework сам автоматически создал нам базу данных по определению используемых классов.


Вначале определим в проекте класс, объекты которого будут храниться в базе данных. Пусть это будет класс User:


```

namespace SQLiteApp
{
 public class User
 {
 public int Id { get; set; }
 public string? Name { get; set; }
 public int Age { get; set; }
 }
}

```


В данном случае класс User содержит свойство Id, которое будет выполнять роль уникального идентификатора пользователя. Кроме того, класс определяет 
свойство Name (имя пользователя) и Age (возраст пользователя).


Ключевым компонентом для взаимодействия с базой данных является контекст данных. Поэтому добавим в проект новый класс, который назовем ApplicationContext и 
который будет выполнять роль контекста данных:


```

using Microsoft.EntityFrameworkCore;

namespace SQLiteApp
{
 public class ApplicationContext : DbContext
 {
 public DbSet Users {get;set; } = null!;
 protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
 {
 optionsBuilder.UseSqlite("Data Source=helloapp.db");
 }
 }
}

```


Класс контекста должен наследоваться от DbContext. И для взаимодействия с таблицей, которая будет хранить данные объектов User, здесь также определено 
свойство `Users`. Чтобы указать анализатору кода, что данное свойство не будет равно null, свойству Users присваивается значение `null!`


Кроме того, чтобы связать контекст данных с конкретной базой данных, в методе `OnConfiguring` с помощью вызова


```
optionsBuilder.UseSqlite("Data Source=helloapp.db");
```


устанавливается используемая база данных. В частности методу UseSqlite передается строка подключения, в которой есть только один параметр - `Data Source`, 
который указывает на имя базы данных. То есть приложение будет использовать базу данных с именем "helloapp.db". Причем не важно, что сейчас такой базы данных не существует - она будет 
создана автоматически.



Теперь все готово для работы с базой данных. Стандартный набор операций по работе с БД включает получение объектов, добавление, изменение и удаление. 
Для получения и просмотра списка объектов из бд мы будем использовать главное окно. А для добавления и изменения создадим новое окно.


Итак, добавим в проект новое окно, которое назовем UserWindow.xaml. В итоге общая конфигурация проекта у нас будет выглядеть следующим образом:



В коде xaml у страницы UserWindow.xaml определим следующее содержимое:


```


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

 
 

 
 OK
 Отмена
 
 


```


Здесь определены два поля ввода для каждого свойства модели User и две кнопки для сохранения и отмены.


В файле связанного кода UserWindow.xaml.cs определим контекст для этой страницы:


```

using System.Windows;
namespace SQLiteApp
{
 public partial class UserWindow : Window
 {
 public User User { get; private set; }
 public UserWindow(User user)
 {
 InitializeComponent();
 User = user;
 DataContext = User;
 }

 void Accept_Click(object sender, RoutedEventArgs e)
 {
 DialogResult = true;
 }
 }
}

```


Данное окно будет диалоговым. Через конструктор оно будет получать объект User, который устанавливается в качестве контекста данных.


В коде xaml у главного окна MainWindow определим вывод списка телефонов и набор кнопок для управления этим списком:


```


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 


```









В коде C# у этого окна пропишем обработчики кнопок, через которые будем взаимодействовать с базой данных SQLite:


```

using Microsoft.EntityFrameworkCore;
using System.Windows;
namespace SQLiteApp
{
 public partial class MainWindow : Window
 {
 ApplicationContext db = new ApplicationContext();
 public MainWindow()
 {
 InitializeComponent();

 Loaded += MainWindow_Loaded;
 }

 // при загрузке окна
 private void MainWindow_Loaded(object sender, RoutedEventArgs e)
 {
 // гарантируем, что база данных создана
 db.Database.EnsureCreated();
 // загружаем данные из БД
 db.Users.Load();
 // и устанавливаем данные в качестве контекста
 DataContext = db.Users.Local.ToObservableCollection();
 }

 // добавление
 private void Add_Click(object sender, RoutedEventArgs e)
 {
 UserWindow UserWindow = new UserWindow(new User());
 if (UserWindow.ShowDialog() == true)
 {
 User User = UserWindow.User;
 db.Users.Add(User);
 db.SaveChanges();
 }
 }
 // редактирование
 private void Edit_Click(object sender, RoutedEventArgs e)
 {
 // получаем выделенный объект
 User? user = usersList.SelectedItem as User;
 // если ни одного объекта не выделено, выходим
 if (user is null) return;

 UserWindow UserWindow = new UserWindow(new User
 {
 Id = user.Id,
 Age = user.Age,
 Name = user.Name
 });

 if (UserWindow.ShowDialog() == true)
 {
 // получаем измененный объект
 user = db.Users.Find(UserWindow.User.Id);
 if (user != null)
 {
 user.Age = UserWindow.User.Age;
 user.Name = UserWindow.User.Name;
 db.SaveChanges();
 usersList.Items.Refresh();
 }
 }
 }
 // удаление
 private void Delete_Click(object sender, RoutedEventArgs e)
 {
 // получаем выделенный объект
 User? user = usersList.SelectedItem as User;
 // если ни одного объекта не выделено, выходим
 if (user is null) return;
 db.Users.Remove(user);
 db.SaveChanges();
 }
 }
}

```


В коде класса прежде всего определяется переменная db, которая представляет контекст данных ApplicationContext и через которую будет идти взаимодействие с базой данных.


В конструкторе окна определяем обработчик загрузки окна, в котором, во-первых, гарантируем, что база данных создана, и для этого вызываем метод


```
db.Database.EnsureCreated();
```


В итоге даже если базы данных не существует, она будет создана в той же папке, где расположен файл приложения. Если бд уже имеется, тогда она просто будет использоваться.


Далее выражение `db.Users.Load()` загружает данные из таблицы Users в локальный кэш контекста данных. И затем список загруженных объектов устанавливается 
в качестве контекста данных:


```
DataContext = db.Users.Local.ToObservableCollection();
```


Для добавления вызывается метод Add:


```

db.Users.Add(user);
db.SaveChanges();

```


Для удаления - метод Remove:


```

db.Users.Remove(user);
db.SaveChanges();

```


При изменении мы передаем в UserWindow копию выбранного объекта. Если мы передавали бы сам выделенный объект, то все изменения на форме автоматически 
синхронизировались со списком, и не было бы смысла в кнопке отмены.


После получения измененного объекта мы находим его в базе данных и устанавливаем у него новые значения свойств, после чего сохраняем все изменения:


```

user = db.Users.Find(UserWindow.User.Id);
if (user != null)
{
 user.Age = UserWindow.User.Age;
 user.Name = UserWindow.User.Name;
 db.SaveChanges();
 usersList.Items.Refresh();
}

```


Здесь надо обратить внимание на вызов `usersList.Items.Refresh()`, который после обновления объекта в бд обновляется отображение списка. В качестве альтернативы мы бы могли 
реализовать интерфейс INotifyPropertyChanged и уведомлять систему при изменении значения свойства Name и/или Age.


Запустим приложение. И добавим какой нибудь объект:



И после добавления объект отобразится в списке:









 <div

**Источник:** [https://metanit.com/sharp/wpf/21.1.php](https://metanit.com/sharp/wpf/21.1.php)
