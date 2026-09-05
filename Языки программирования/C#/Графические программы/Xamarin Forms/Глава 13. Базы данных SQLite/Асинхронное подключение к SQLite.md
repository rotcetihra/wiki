[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Графические программы|Графические программы]] / [[Языки программирования/C#/Графические программы/Xamarin Forms|Xamarin Forms]] / [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 13. Базы данных SQLite|Глава 13. Базы данных SQLite]] / Асинхронное подключение к SQLite

[[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 13. Базы данных SQLite/Основные операции с SQLite|Назад]] | [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 13. Базы данных SQLite|Содержание]] | [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 13. Базы данных SQLite/Подключение к существующей базе данных|Вперёд]]

**Дата написания:** 05.09.2026

Последнее обновление: 14.01.2021
	
	
	
	- 

	- 

	- 

	
	
	
	

	
		
		
		
	

	
В прошлой теме для подключения к базе данных SQLite мы использовали синхронные методы, которые на время вызова и выполнения операций с данными 
блокировали основной поток графического приложения. Однако библиотека SQLite.NET предоставляет также асинхронный API. Он предоставляет методы, которые во многом похожи на синхронные.

Асинхронное подключение в SQLite.NET представляет объект класса SQLiteAsyncConnection. А весь асинхронный API раскрывается через методы этого класса:

- CreateTableAsync(): создание таблицы

- DropTableAsync(): удаление таблицы

- Table<T>(): получение данных из таблицы

- GetAsync<T>(): получение объекта

- DeleteAsync(): удаление объекта

- UpdateAsync(): обновление существующего объекта

- InsertAsync(): добавление нового элемента

- ExecuteAsync(): выполнение sql-выражения

- ExecuteScalarAsync(): выполнение sql-выражения и получение результата

- FindAsync(): поиск объекта в БД

- QueryAsync(): выполнение запроса SQL

- InsertAllAsync(): добавление нескольких объектов

- UpdateAllAsync(): обновление нескольких объектов

Для применения асинхронного API возьмем проект из прошлой темы и добавим в него новый класс FriendsAsyncRepository:

```

using System.Collections.Generic;
using System.Threading.Tasks;
using SQLite;
using Xamarin.Forms;

namespace HelloApp
{
    public class FriendAsyncRepository
    {
        SQLiteAsyncConnection database;
        
        public FriendAsyncRepository(string databasePath)
        {
            database = new SQLiteAsyncConnection(databasePath);
        }

        public async Task CreateTable()
        {
            await database.CreateTableAsync();
        }
        public async Task> GetItemsAsync()
        {
            return await database.Table().ToListAsync();

        }
        public async Task GetItemAsync(int id)
        {
            return await database.GetAsync(id);
        }
        public async Task DeleteItemAsync(Friend item)
        {
            return await database.DeleteAsync(item);
        }
        public async Task SaveItemAsync(Friend item)
        {
            if (item.Id != 0)
            {
                await database.UpdateAsync(item);
                return item.Id;
            }
            else
            {
                return await database.InsertAsync(item);
            }
        }
    }
}

```

В отличие от синхронной версии здесь создание таблицы вынесено в отдельный метод.

И далее похожим образом мы сможем использовать этот репозиторий. Установим его в классе App:

```

using System;
using System.IO;
using Xamarin.Forms;

namespace HelloApp
{
    public partial class App : Application
    {
        public const string DATABASE_NAME = "friends2.db";
        public static FriendAsyncRepository database;
        public static FriendAsyncRepository Database
        {
            get
            {
                if (database == null)
                {
                    database = new FriendAsyncRepository(
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

И затем используем на главной странице приложения:

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

		protected override async void OnAppearing()
		{
			// создание таблицы, если ее нет
			await App.Database.CreateTable();
			// привязка данных
			friendsList.ItemsSource = await App.Database.GetItemsAsync();
			
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

Xaml-код страницы MainPage выглядит следующим образом:

```

  
    
      
        
          
            
              
                
              
            
          
        
      
    
    
  

```

При переходе на любую страницу у нее вызывается метод `OnAppearing()`, поэтому тут мы можем установить привязку и настроить другие начальные данные.

Интерфейс страницы FriendPage для отображения одного объекта:

```

  
    
    
    
    
    
    
    
      
      
      
    
  

```

А в файле связанного кода FriendPage.xaml.cs определим обработчики нажатия кнопок:

```

using System;
using Xamarin.Forms;
using Xamarin.Forms.Xaml;

namespace HelloApp
{
    public partial class FriendPage : ContentPage
    {
        public FriendPage()
        {
            InitializeComponent();
        }
        private async void SaveFriend(object sender, EventArgs e)
        {
            var friend = (Friend)BindingContext;
            if (!String.IsNullOrEmpty(friend.Name))
            {
                await App.Database.SaveItemAsync(friend);
            }
            await this.Navigation.PopAsync();
        }
        private async void DeleteFriend(object sender, EventArgs e)
        {
            var friend = (Friend)BindingContext;
            await App.Database.DeleteItemAsync(friend);
            await this.Navigation.PopAsync();
        }
        private async void Cancel(object sender, EventArgs e)
        {
            await this.Navigation.PopAsync();
        }
    }
}

```

### ConfigureAwait

Часто данные извлекаются и обрабатываются в фоновом потоке. В этом случае, чтобы после выполнения операции await обработка продолжилась в фоновом потоке, 
применяется метод ConfigureAwait(false):

```

public async Task GetItemsAsync()
{
	var friends = await database.Table().ToListAsync().ConfigureAwait(false);
	// Операции продолжают выполняться в фоновом потоке, а не в UI-потоке
	for(var friend in friends){ ... }
}

```

---

**Источник:** [https://metanit.com/sharp/xamarin/7.4.php](https://metanit.com/sharp/xamarin/7.4.php)

[[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 13. Базы данных SQLite/Основные операции с SQLite|Назад]] | [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 13. Базы данных SQLite|Содержание]] | [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 13. Базы данных SQLite/Подключение к существующей базе данных|Вперёд]]
