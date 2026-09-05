[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Графические программы|Графические программы]] / [[Языки программирования/C#/Графические программы/Xamarin Forms|Xamarin Forms]] / [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 13. Базы данных SQLite|Глава 13. Базы данных SQLite]] / Основные операции с SQLite

[[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 13. Базы данных SQLite|Содержание]] | [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 13. Базы данных SQLite/Асинхронное подключение к SQLite|Вперёд]]

**Дата написания:** 05.09.2026

## Основные операции с SQLite
Последнее обновление: 14.01.2021
	
	
	
	- 

	- 

	- 

	
	
	
	

	
		
		
		
	

	
Кроме обычных файлов для хранения данных мы можем использовать локальные базы данных. Наиболее популярной системой баз данных для локальных приложений является 
SQLite, поэтому рассмотрим общие принципы работы с этой СУБД.

Для работы с SQLite можно использовать разные подходы и библиотеки. Рекомендуемой библиотекой является SQLite.NET, 
которая представляет простое ORM-решение (Object Relational Mapping) для Xamarin. Она позволяет работать с базой данных как с хранилищем объектов и манипулировать данными 
как объектами стандартных классов C# без использования выражений на языке SQL. И вначале добавим в главный проект в узел References 
с помощью менеджера NuGet эту библиотеку sqlite-net-pcl:

Следует отметить, что в Nuget можно найти много похожих библиотек с подобным названием. У нужной библиотеки будут следующие данные:

- Автор: SQLite-net

- Id: sqlite-net-pcl

Вначале определим класс, объекты которого будут храниться в базе данных. Добавим в главный проект следующий класс Friend:

```

using SQLite;

namespace HelloApp
{
    [Table("Friends")]
    public class Friend
    {
        [PrimaryKey, AutoIncrement, Column("_id")]
        public int Id { get; set; }

        public string Name { get; set; }
        public string Email { get; set; }
        public string Phone { get; set; }
    }
}

```

Класс Friend выступает в качестве модели приложения. Этот класс использует атрибуты, которые позволяют настроить его отображение на таблицу в бд. 
Для настройки мы можем использовать следующие атрибуты:

- [PrimaryKey]: применяется к свойству типа `int` и 
указывает, что столбец в таблице, который соответствует этому свойству, будет выполнять роль первичного ключа. Составные ключи не поддерживаются

- [AutoIncrement]: применяется к свойству типа `int` и 
указывает, что столбец в таблице, который соответствует этому свойству, будет инкрементировать значение на единицу при добавлении нового элемента

- [Column(name)]: задает сопоставление свойства со столбцом в таблице, который имеет имя name

- [Table(name)]: устанавливает название таблицы, которая будет соотвествовать данному классу

- [MaxLength(value)]: устанавливает максимальную длину для строковых свойств

- [Ignore]: указывает, что свойство будет игнорироваться. Это может быть полезно, если значение данного свойства не надо 
хранить в базе данных, и данное свойство не должно сопоставляться со столбцами из таблицы в бд

- [Unique]: гарантирует, что столбец, который соответствует свойству с этим атрибутом, будет иметь уникальные неповторяющиеся значения

При запросах к базе данных будет происходить автоматическое сопоставление типов данных из SQLite с типами данных из C#. Сопоставление типов 
можно описать следующей таблицей:

| C# | SQLite |
| --- | --- |
| int, long | integer, bigint |
| bool | integer (1 = true) |
| enum | integer |
| float | real |
| double | real |
| decimal | real |
| string | varchar, text |
| DateTime | numeric, text |
| byte[] | blob |

### Класс репозитория

Также создадим класс репозитория, через который будут идти все операции с данными:

```

using System.Collections.Generic;
using SQLite;

namespace HelloApp
{
    public class FriendRepository
    {
        SQLiteConnection database;
        public FriendRepository(string databasePath)
        {
            database = new SQLiteConnection(databasePath);
            database.CreateTable();
        }
        public IEnumerable GetItems()
        {
            return database.Table().ToList();
        }
        public Friend GetItem(int id)
        {
            return database.Get(id);
        }
        public int DeleteItem(int id)
        {
            return database.Delete(id);
        }
        public int SaveItem(Friend item)
        {
            if (item.Id != 0)
            {
                database.Update(item);
                return item.Id;
            }
            else
            {
                return database.Insert(item);
            }
        }
    }
}

```

В конструкторе класса происходит создание подключения и базы данных (если она отсутствует). В качестве параметра извне будет передаваться путь к базе данных. 
При желании путь к бд можно определить и в самом конструкторе.

Для всех операций с данными используются методы, определенные в классе SQLiteConnection:

- Insert: добавляет объект в таблицу

- Get<T>: позволяет получить элемент типа T по id

- Table<T>: возвращает все объекты из таблицы

- Delete<T>: удаляет объект по id

- Update<T>: обновляет объект

- Query<T>: выполняет SQL-выражение и возвращает строки из таблицы в виде объектов типа T (относится к выражениям SELECT)

- Execute: выполняет SQL-выражение, но ничего не возвращает (относится к операциям. где не надо возвращать результат -
 UPDATE, INSERT, DELETE)

Если предполагается, что к базе данных может обращаться сразу несколько потоков, то для блокирования одновременных операций с бд в классе репозитории 
можно использовать блок lock с заглушкой, например:

```

SQLiteConnection database;
static object locker = new object();
//......................
 
public int DeleteItem(int id)
{
	lock(locker)
	{
        return database.Delete(id);
	}
}

```

Создаваемое подключение будет общим для всего приложения, поэтому изменим файл App.xaml.cs следующим образом:

```

using System;
using System.IO;
using Xamarin.Forms;

namespace HelloApp
{
    public partial class App : Application
    {
        public const string DATABASE_NAME = "friends.db";
        public static FriendRepository database;
        public static FriendRepository Database
        {
            get
            {
                if (database == null)
                {
                    database = new FriendRepository(
                        Path.Combine(
                            Environment.GetFolderPath(Environment.SpecialFolder.LocalApplicationData), DATABASE_NAME));
                }
                return database;
            }
        }
        public App()
        {
            InitializeComponent();

            MainPage = new NavigationPage(new MainPage());
        }
        protected override void OnStart()
        {
        }
        protected override void OnSleep()
        {
        }
        protected override void OnResume()
        {
        }
    }
}

```

Статический объект репозитория, создаваемый при создании главной страницы приложения, будет доступен из любого места приложения.

Поскольку в нашем приложении мы будем переходить по страницам - к странице добавления или просмотра, то в качестве главной страницы устанавливается 
объект `NavigationPage`.

### Добавление страниц приложения

Теперь на главной странице MainPage.xaml следующий код:

```

  
    
      
        
          
            
              
                
              
            
          
        
      
    
    
  

```

Элемент ListView будет выводить список объектов, а при нажатии на элемент списка, будет срабатывать обработчик `OnItemSelected`. 
И также для добавления нового объекта определена кнопка.

И изменим файл кода MainPage.xaml.cs:

```

using System;
using Xamarin.Forms;

namespace HelloApp
{
    public partial class MainPage : ContentPage
    {
        public MainPage()
        {
            InitializeComponent();
        }
        protected override void OnAppearing()
        {
            friendsList.ItemsSource = App.Database.GetItems();
            base.OnAppearing();
        }
        // обработка нажатия элемента в списке
        private async void OnItemSelected(object sender, SelectedItemChangedEventArgs e)
        {
            Friend selectedFriend = (Friend)e.SelectedItem;
            FriendPage friendPage = new FriendPage();
            friendPage.BindingContext = selectedFriend;
            await Navigation.PushAsync(friendPage);
        }
        // обработка нажатия кнопки добавления
        private async void CreateFriend(object sender, EventArgs e)
        {
            Friend friend = new Friend();
            FriendPage friendPage = new FriendPage();
            friendPage.BindingContext = friend;
            await Navigation.PushAsync(friendPage);
        }
    }
}

```

При переходе на любую страницу у нее вызывается метод `OnAppearing()`, поэтому тут мы можем установить привязку и настроить другие начальные данные.

Остальные оба обработчика - OnItemSelected и CreateFriend предусматривают переход на страницу FriendPage, которая будет отвечать за работу с одним объектом из бд. 
Через свойство `BindingContext` мы можем установить полученный объект в качестве контекста страницы, а на самой странице использовать выражения привязки 
для изменения значений свойств объекта.

Теперь добавим эту страницу FriendPage. В ее коде xaml пропишем следующий интерфейс:

```

  
    
    
    
    
    
    
    
      
      
      
    
  

```

А в файле связанного кода FriendPage.xaml.cs добавим обработчики нажатия кнопок:

```

using System;
using Xamarin.Forms;

namespace HelloApp
{
    public partial class FriendPage : ContentPage
    {
        public FriendPage()
        {
            InitializeComponent();
        }

        private void SaveFriend(object sender, EventArgs e)
        {
            var friend = (Friend)BindingContext;
            if (!String.IsNullOrEmpty(friend.Name))
            {
                App.Database.SaveItem(friend);
            }
            this.Navigation.PopAsync();
        }
        private void DeleteFriend(object sender, EventArgs e)
        {
            var friend = (Friend)BindingContext;
            App.Database.DeleteItem(friend.Id);
            this.Navigation.PopAsync();
        }
        private void Cancel(object sender, EventArgs e)
        {
            this.Navigation.PopAsync();
        }
    }
}

```

Обработчики используют методы репозитория для сохранения и удаления объекта и после этого осуществляют переход назад на главную страницу.

В итоге главный проект будет выглядеть следующим образом:

Теперь с главной страницы мы можем попасть на страницу добавления и создать там новые объекты:

После добавления все объекты будут отображаться в списке на главной странице:

---

**Источник:** [https://metanit.com/sharp/xamarin/7.2.php](https://metanit.com/sharp/xamarin/7.2.php)

[[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 13. Базы данных SQLite|Содержание]] | [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 13. Базы данных SQLite/Асинхронное подключение к SQLite|Вперёд]]
