[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Графические программы|Графические программы]] / [[Языки программирования/C#/Графические программы/Xamarin Forms|Xamarin Forms]] / [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 20. Realm|Глава 20. Realm]] / Основные операции с базой данных Realm

[[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 20. Realm|Содержание]]

**Дата написания:** 05.09.2026

## Основные операции с базой данных Realm
Последнее обновление: 11.01.2021
	
	
	
	- 

	- 

	- 

	
	
	
	

	
		
		
		
	

	
Realm представляет локальную базу данных на подобие SQLite, предназначенную прежде всего для мобильных платформ (хотя Realm также работает и на декстопах). 
Официальный сайт компании [https://realm.io/](https://realm.io). Рассмотрим, как использовать Realm в связке с Xamarin.

Прежде всего установим пакет Realm через Nuget во все проекты решения:

### Определение модели

Вначале определим модель данных, с которым будем работать. Добавим в главный проект класс Friend:

```

using Realms;

namespace RealmApp
{
    public class Friend : RealmObject
    {
        [PrimaryKey]
        public string Id { get; set; }

        public string Name { get; set; }
        public string Email { get; set; }
        public string Phone { get; set; }
    }
}

```

Сущности, которые храняться в базе данных Realm, должны представлять класс RealmObject. Поэтому класс Friend наследуется от 
класса RealmObject.

По умолчанию Realm никак не устанавливает первичные ключи. Чтобы отметить свойство как первичный ключ, к нему применяется атрибут Id. 
Стоит отметить, что Realm сам не устанавливает значение первичного ключа вне зависимости от того, какой тип это свойство представляет. То есть если свойство 
первичного ключа представляет тип int, то автоинкремента значения свойства при добавлении нового объекта не будет. Нам самим потребуется перед добавлением объекта в бд присваивать этому свойтву значение.

### Основные операции в Realm

Ключевым для работы с данными является объект Realm. Для получения данного объекта применяется статический метод Realm.GetInstance():

```

Realm _realm = Realm.GetInstance();

```

Далее, используя методы этого объекта, мы можем выполнять операции с базой данных.

- Add(): добавляет объект в базу данных

- All(): получает все объекты из базы данных

- BeginWrite(): создает транзакцию на запись изменений в бд

- Find(): возвращает объект с определенным первичным ключом

- Refresh()/RefreshAsync(): обновляет объект Realm

- Remove(): удаляет один объект из базы данных

- RemoveAll(): удаляет все объекты из базы данных

- Write()/WriteAsync(): запускает транзакцию на запись изменений в бд

Для получения данных из бд мы можем комбинировать метод All с методами LINQ:

```

var allFriends = _realm.All();
var allToms = _realm.All().Where(f => f.Name=="Tom");

```

Если для модели определен первичный ключ, то мы можем получить объект по первичному ключу:

```

var friend = _realm.Find("43667r47747");

```

Остальные операции - добавление, изменение, удаление - операции записи изменений чуть менее интуитивны. Ключевым здесь является создание и выполнение транзакции. 
И все изменения мы можем делать в рамках транзакции. Например, добавление нового объекта:

```

Realm _realm = Realm.GetInstance();
_realm.Write(() => _realm.Add(new Friend {Name="Tom"}));

```

Удаление

```

Realm _realm = Realm.GetInstance();
_realm.Write(() => _realm.Remove(friend));

```

Изменение

```

Realm _realm = Realm.GetInstance();
_realm.Write(() => friend.Email = "tom@gmail.com");

```

Кроме использования метода Write мы можем явным образом создавать и выполнять транзакцию:

```

Realm _realm = Realm.GetInstance();
// создание транзакции
Transaction _transaction = _realm.BeginWrite

// производим некоторые изменения с объектами - удаление, добавление
_realm.Add(new Friend {Name="Tom"});
_realm.Remove(friend);

// подтверждаем транзакцию
_transaction.Commit();

// удаляем транзакцию
_transaction.Dispose();

```

Сначала мы создаем транзакцию с помощью метода BeginWrite. Затем выполняются некоторые изменения. Далее подтверждаем эти изменения с помощью метода Commit. Если мы 
не вызовем этот метод, соответственно никаких изменений не будет. И в конце необходимо для транзакции вызвать метод Dispose.

### Пример приложения

Добавим в проект новую страницу FriendPage.xaml:

```

    
        
        
        
        
        
        
        
            
            
        
    

```

Здесь будет выводиться информация об одном объекте Friend с кнопками для сохранения изменений и удаления. 
В файле FriendPage.xaml.cs пропишем логику работу с данными:

```

using Realms;
using System;
using Xamarin.Forms;
using Xamarin.Forms.Xaml;

namespace RealmApp
{
	public partial class FriendPage : ContentPage
	{
        Realm _realm;
        Transaction _transaction;
		
		public FriendPage()
		{
			InitializeComponent ();
            _realm = Realm.GetInstance();
            _transaction = _realm.BeginWrite();
        }
		
        private void SaveFriend(object sender, EventArgs e)
        {
            var friend = (Friend)BindingContext;
            if (!String.IsNullOrEmpty(friend.Name))
            {
                if (friend.Id == null)
                {
                    friend.Id = Guid.NewGuid().ToString();
                    _realm.Add(friend);
                }

                _transaction.Commit();
            }
            this.Navigation.PopAsync();
        }
        private void DeleteFriend(object sender, EventArgs e)
        {
            var friend = (Friend)BindingContext;
            _realm.Remove(friend);
            _transaction.Commit();

            this.Navigation.PopAsync();
        }

        protected override void OnDisappearing()
        {
            _transaction?.Dispose();
            base.OnDisappearing();
        }
    }
}

```

Страница будет привязана к одному объекту Friend. В конструкторе страницы создается транзакция.

При нажатии на кнопку сохранения мы смотрим на наличие 
Id объекта Friend. Если Id равен null, то есть еще не установлен, то мы имеем дело с добавлением объекта. Поэтому генерируем значение для Id и ставим объект на добавление. 
Для редактирования объекта ничего дополнительно делать не надо. В конце подтверждаем транзакцию вызовом метода Commit.

При нажатии на кнопку удаления ставим объект на удаление с помощью метода _realm.Remove() и также подтверждаем транзакцию.

В методе OnDisappearing, который вызывается при завершении работы страницы, удаляем транзакцию.

На странице MainPage.xaml, которая есть по умолчанию в проекте, определим интерфейс для вывода списка объктов Friend:

```

    
        
            
                
                    
                        
                            
                                
                            
                        
                    
                
            
        
        
    

```

В файле MainPage.xaml.cs определим следующую программную логику:

```

using Realms;
using System;
using Xamarin.Forms;

namespace RealmApp
{
	public partial class MainPage : ContentPage
	{
        private Realm _realm;

        public MainPage()
		{
			InitializeComponent();
            _realm = Realm.GetInstance();
        }
        protected override void OnAppearing()
        {
            friendsList.ItemsSource = _realm.All();
            base.OnAppearing();
        }
        // обработка нажатия элемента в списке
        private async void TapItem(object sender, ItemTappedEventArgs e)
        {
            Friend selectedFriend = (Friend)e.Item;
            FriendPage friendPage = new FriendPage
            {
                BindingContext = selectedFriend
            };
            await Navigation.PushAsync(friendPage);
        }
        // обработка нажатия кнопки добавления
        private async void CreateFriend(object sender, EventArgs e)
        {
            FriendPage friendPage = new FriendPage
            {
                BindingContext = new Friend()
            };
            await Navigation.PushAsync(friendPage);
        }
    }
}

```

Таким образом, при выборе объекта в списке будет создаваться страница FriendPage, у которой в качестве контекста устанавливается выбранный объект Friend.

В конце изменим файл App.xaml.cs, чтобы указать, что мы будем использовать NavigationPage:

```

using Xamarin.Forms;

namespace RealmApp
{
    public partial class App : Application
    {
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

Запустим проект и добавим несколько объектов:

Стоит отметить, что при первой компиляции в проект автоматически добавляется файл FodyWeavers.xml со следующим содержимым:

```

  

```

Этот файл не надо удалять - он используется инфраструктурой Realm.

---

**Источник:** [https://metanit.com/sharp/xamarin/18.1.php](https://metanit.com/sharp/xamarin/18.1.php)

[[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 20. Realm|Содержание]]
