[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Графические программы|Графические программы]] / [[Языки программирования/C#/Графические программы/Xamarin Forms|Xamarin Forms]] / [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 12. MVVM|Глава 12. MVVM]] / Пример MVVM

[[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 12. MVVM/Команды и взаимодействие с пользователем в MVVM|Назад]] | [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 12. MVVM|Содержание]] | [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 12. MVVM/Контекстное меню|Вперёд]]

**Дата написания:** 05.09.2026

Последнее обновление: 14.01.2021
	
	
	
	- 

	- 

	- 

	
	
	
	

	
		
		
		
	

	
Рассмотрим на конкретном примере применение паттерна MVVM. Итак, создадим новое приложение, которое назовем MvvmApp. 
Задача нашего приложения будет заключаться в создании списка друзей, а также их добавлении, редактировании и удалении. Вобщем управление списком друзей.

Вначале добавим в главный проект три новых папки для каждого из компонентов паттерна:

- Папка Models

- Папка ViewModels

- Папка Views

Страницу MainPage.xaml, если она имется в проекте по умолчанию, можно удалить.

Финальная структура проекта будет выглядеть следующим образом:

Вначале определим в папке Models модель, которая будет представлять данные - класс Friend:

```

namespace HelloApp.Models
{
    public class Friend
    {
        public string Name { get; set; }
        public string Email { get; set; }
        public string Phone { get; set; }
    }
}

```

Чтобы работать с данными этой модели добавим в папку Views две страницы XAML по типу Content Page: 
FriendsListPage.xaml (для вывода списка друзей) и FriendPage.xaml (для управления одним другом).

Далее добавим в другую папку ViewModels класс FriendViewModel:

```

using System.ComponentModel;
using HelloApp.Models;

namespace HelloApp.ViewModels
{
    public class FriendViewModel : INotifyPropertyChanged
    {
        public event PropertyChangedEventHandler PropertyChanged;
        FriendsListViewModel lvm;

        public Friend Friend { get; private set; }

        public FriendViewModel()
        {
            Friend = new Friend();
        }

        public FriendsListViewModel ListViewModel
        {
            get { return lvm; }
            set
            {
                if (lvm != value)
                {
                    lvm = value;
                    OnPropertyChanged("ListViewModel");
                }
            }
        }
        public string Name
        {
            get { return Friend.Name; }
            set
            {
                if (Friend.Name != value)
                {
                    Friend.Name = value;
                    OnPropertyChanged("Name");
                }
            }
        }
        public string Email
        {
            get { return Friend.Email; }
            set
            {
                if(Friend.Email != value)
                {
                    Friend.Email = value;
                    OnPropertyChanged("Email");
                }
            }
        }
        public string Phone
        {
            get { return Friend.Phone; }
            set
            {
                if (Friend.Phone != value)
                {
                    Friend.Phone = value;
                    OnPropertyChanged("Phone");
                }
            }
        }

        public bool IsValid
        {
            get
            {
                return ((!string.IsNullOrEmpty(Name.Trim())) ||
                    (!string.IsNullOrEmpty(Phone.Trim())) ||
                    (!string.IsNullOrEmpty(Email.Trim())));
            }
        }
        protected void OnPropertyChanged(string propName)
        {
            if (PropertyChanged != null)
                PropertyChanged(this, new PropertyChangedEventArgs(propName));
        }
    }
}

```

Фактически этот класс является надстройкой над объектом Friend.

Затем добавим в папку ViewModels новый класс, который будет представлять список друзей и который будет использоваться на странице FriendsListPage - класс FriendsListViewModel:

```

using System.Collections.ObjectModel;
using System.Windows.Input;
using Xamarin.Forms;
using System.ComponentModel;
using HelloApp.Views;

namespace HelloApp.ViewModels
{
    public class FriendsListViewModel : INotifyPropertyChanged
    {
        public ObservableCollection Friends { get; set; }

        public event PropertyChangedEventHandler PropertyChanged;

        public ICommand CreateFriendCommand { protected set; get; }
        public ICommand DeleteFriendCommand { protected set; get; }
        public ICommand SaveFriendCommand { protected set; get; }
        public ICommand BackCommand { protected set; get; }
        FriendViewModel selectedFriend;

        public INavigation Navigation { get; set;}

        public FriendsListViewModel()
        {
            Friends = new ObservableCollection();
            CreateFriendCommand = new Command(CreateFriend);
            DeleteFriendCommand = new Command(DeleteFriend);
            SaveFriendCommand = new Command(SaveFriend);
            BackCommand = new Command(Back);
        }

        public FriendViewModel SelectedFriend
        {
            get { return selectedFriend; }
            set
            {
                if (selectedFriend != value)
                {
                    FriendViewModel tempFriend = value;
                    selectedFriend = null;
                    OnPropertyChanged("SelectedFriend");
                    Navigation.PushAsync(new FriendPage(tempFriend));
                }
            }
        }
        protected void OnPropertyChanged(string propName)
        {
            if (PropertyChanged != null)
                PropertyChanged(this, new PropertyChangedEventArgs(propName));
        }

        private void CreateFriend()
        {
            Navigation.PushAsync(new FriendPage(new FriendViewModel() { ListViewModel = this }));
        }
        private void Back()
        {
            Navigation.PopAsync();
        }
        private void SaveFriend(object friendObject)
        {
            FriendViewModel friend = friendObject as FriendViewModel;
            if (friend != null && friend.IsValid && !Friends.Contains(friend))
            {
                Friends.Add(friend);
            }
            Back();
        }
        private void DeleteFriend(object friendObject)
        {
            FriendViewModel friend = friendObject as FriendViewModel;
            if (friend != null)
            {
                Friends.Remove(friend);
            }
            Back();
        }
    }
}

```

Для хранения списка друзей, который будет выводится на страницу, здесь определена коллекция `Friends`.

Навигация также является частью логики приложения, которая не относится к визуальной части, поэтому для хранения сервиса навигации здесь определено свойство 
`Navigation`. В дальнейшем через это свойство будет производиться переход к FriendPage.

Для управлением списком друзей в классе определено четыре команды. Команда добавления нового друга приводит в действие метод `CreateFriend()`, 
в котором производится переход к FriendPage. В конструктор FriendPage передается текущий объект FriendViewModel, который мы далее создадим.

По команде возвращения назад выполняется метод `Back()`, который производит переход назад.

Команда сохранения объекта выполняет метод `SaveFriend()`. В этом методе новый объект добавляется в коллекцию Friends.

По команде удаления вызывается метод `DeleteFriend`, который удаляет объект из списка.

Теперь изменим код страниц из папки Views. В коде C# страницы FriendsListPage пропишем следующее содержимое:

```

using Xamarin.Forms;
using HelloApp.ViewModels;

namespace HelloApp.Views
{
    public partial class FriendsListPage : ContentPage
    {
        public FriendsListPage()
        {
            InitializeComponent();
            BindingContext = new FriendsListViewModel() { Navigation = this.Navigation };
        }
    }
}

```

Здесь создается объект FriendsListViewModel, который устанавливается в качестве контекста страницы.

В коде XAML у этой страницы пропишем выражения привязки к этому объекту:

```

  
    
    
      
        
          
            
              
                
                
                
              
            
          
        
      
    
  

```

Несмотря на то, что тут определена кнопка для добавления нового объекта, код страницы не содержит никаких обработчиков, потому что всю обработку будет выполнять 
команда CreateFriendCommand, определенная в FriendsListViewModel.

Затем изменим код c# у страницы FriendPage:

```

using HelloApp.ViewModels;
using Xamarin.Forms;

namespace HelloApp.Views
{
    public partial class FriendPage : ContentPage
    {
        public FriendViewModel ViewModel { get; private set; }
        public FriendPage(FriendViewModel vm)
        {
            InitializeComponent();
            ViewModel = vm;
            this.BindingContext = ViewModel;
        }
    }
}

```

Теперь страница в качестве параметра в конструкторе принимает объект FriendViewModel, устанавливает его в качестве контекста и также не содержит никакой другой логики.

И в коде xaml у страницы определим выражения привязки:

```

  
    
      
      
      
      
      
      
    
    
      
      
      
    
  

```

И при нажатии на кнопки будет вызываться соответствующая команда. Кроме того, первые две кнопки передают в команды параметр, который представляет привязанный объект - то есть 
тот объект FriendViewModel, который передан в конструктор и установлен в качестве контекста страницы. Выражение `{Binding}` 
без указания свойства объекта выполняет привязку к объекту, который является контекстом для данного элемента управления. Таким образом, команды в FriendsListViewModel получат 
добавляемый или удаляемый объект FriendViewModel.

При этому для редактирования в данном случае не надо нажимать никакую кнопку, так как при изменении значений в текстовых полях 
сразу же изменяться значения у этого объекта в списке. И после изменения значений достаточно нажать на кнопку Назад для возврата на главную страницу. Правда, такое поведение не всегда бывает удобно. В этом случае мы можем добавить к объекту Friend/FriendViewModel 
какой-нибудь идентификатор. А при редактировании передавать не объект из списка, а его копию. Затем при сохранении данных в зависимости от Id выполнять либо 
добавление (если Id не установлен), либо редактирование. Удаление в этом случае также бы производилось бы по Id.

И в конце в классе App установим страницу FriendsListPage в качестве главной:

```

using Xamarin.Forms;
using HelloApp.Views;

namespace HelloApp
{
    public partial class App : Application
    {
        public App()
        {
            MainPage = new NavigationPage(new FriendsListPage());
        }

        protected override void OnStart()
        { }

        protected override void OnSleep()
        { }

        protected override void OnResume()
        { }
    }
}

```

Запустим приложение и добавим какой-нибудь объект.

И после добавления мы увидим этот объект в списке на главной странице:

---

**Источник:** [https://metanit.com/sharp/xamarin/11.1.php](https://metanit.com/sharp/xamarin/11.1.php)

[[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 12. MVVM/Команды и взаимодействие с пользователем в MVVM|Назад]] | [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 12. MVVM|Содержание]] | [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 12. MVVM/Контекстное меню|Вперёд]]
