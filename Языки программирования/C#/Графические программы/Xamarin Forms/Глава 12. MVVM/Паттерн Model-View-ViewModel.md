[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Графические программы|Графические программы]] / [[Языки программирования/C#/Графические программы/Xamarin Forms|Xamarin Forms]] / [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 12. MVVM|Глава 12. MVVM]] / Паттерн Model-View-ViewModel

[[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 12. MVVM|Содержание]] | [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 12. MVVM/Команды и взаимодействие с пользователем в MVVM|Вперёд]]

**Дата написания:** 05.09.2026

## Паттерн Model-View-ViewModel
Последнее обновление: 13.01.2021
	
	
	
	- 

	- 

	- 

	
	
	
	

	
		
		
		
	

	
Паттерн MVVM (Model - View - ViewModel) основывается на разделении функциональной части приложения на три ключевых компонента:

- View - представление или пользовательский интерфейс

- Model - модель или данные, которые используются в приложении

- ViewModel - промежуточный слой между представлением и данными, который обеспечивает их взаимодействие

Преимуществом использования данного паттерна является меньшая связанность между компонентами и разделение ответственности между ними. То есть Model отвечает 
за данные, View отвечает за графический интерфейс, а ViewModel - за логику приложения.

Легкость реализации паттерна MVVM  в Xamarin Forms стала возможной благодаря ранее рассмотренному механизму привязки.

Рассмотрим простейший пример. Определим класс данных или модели:

```

public class Phone
{
    public string Title { get; set; }
    public string Company { get; set; }
    public int Price { get; set; }
}

```

Также добавим в проект класс, который назовем PhoneViewModel со следующим содержимым:

```

using System.ComponentModel;

public class PhoneViewModel :INotifyPropertyChanged
{
    public event PropertyChangedEventHandler PropertyChanged;
    private Phone phone;

    public PhoneViewModel()
    {
        phone = new Phone();
    }
        
    public string Title
    {
        get { return phone.Title; }
        set
        {
            if (phone.Title != value)
            {
                phone.Title = value;
                OnPropertyChanged("Title");
            }
        }
    }
    public string Company
    {
        get { return phone.Company; }
        set
        {
            if (phone.Company != value)
            {
                phone.Company = value;
                OnPropertyChanged("Company");
            }
        }
    }
    public int Price
    {
        get { return phone.Price; }
        set
        {
            if (phone.Price != value)
            {
                phone.Price = value;
                OnPropertyChanged("Price");
            }
        }
    }
    protected void OnPropertyChanged(string propName)
    {
        if (PropertyChanged != null)
            PropertyChanged(this, new PropertyChangedEventArgs(propName));
    }
}

```

Это и будет компонент ViewModel, который связывает данные и визуальный интерфейс. По большому счету она представляет обертку над классом Phone, 
определяя все те же свойства. Для упрощения задачи сам объект Phone создается в конструкторе, хотя в реальности там могла бы быть более сложная логика, 
например, по получению объекта из базы данных.

Важно, что данный класс реализует интерфейс INotifyPropertyChanged, что позволяет уведомлять систему об изменении его свойств с помощью события 
`PropertyChanged`.

Теперь создадим визуальную часть. Определим на главной странице MainPage.xaml следующее содержимое:

```

  
    
    
    
  

```

Здесь определена привязка к свойству ViewModel.

А в конструкторе страницы в файле кода c# пропишем в качестве контекста данных для страницы определенную ранее ViewModel:

```

public partial class MainPage : ContentPage
{
    public MainPage()
    {
        InitializeComponent();
        this.BindingContext = new PhoneViewModel
        {
            Title = "iPhone 7", 
            Company = "Apple",
            Price=52000
        };
    }
}

```

И при запуске приложение выведет нам все данные о viewmodel, переданной во view:

При использовании паттерна в качестве представления обычно выступает страница, и, как правило, одно представление (одна страница) связана с одной моделью представления (ViewModel). 
При этом одну и ту же VıewModel могут использовать несколько представлений.

Стоит отметить, что в этом отношении ViewModel ничего не знает о представлении, что это, какие элементы управления оно содержит. ViewModel только определяет 
логику обработку без какой-либо связи с графическим интерфейсом.

---

**Источник:** [https://metanit.com/sharp/xamarin/4.2.php](https://metanit.com/sharp/xamarin/4.2.php)

[[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 12. MVVM|Содержание]] | [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 12. MVVM/Команды и взаимодействие с пользователем в MVVM|Вперёд]]
