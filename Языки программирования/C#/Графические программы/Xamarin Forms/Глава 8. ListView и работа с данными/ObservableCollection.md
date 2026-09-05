[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Графические программы|Графические программы]] / [[Языки программирования/C#/Графические программы/Xamarin Forms|Xamarin Forms]] / [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 8. ListView и работа с данными|Глава 8. ListView и работа с данными]] / ObservableCollection

[[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 8. ListView и работа с данными/Создание класса ячейки для ListView|Назад]] | [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 8. ListView и работа с данными|Содержание]] | [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 8. ListView и работа с данными/Настройка внешнего вида ListView|Вперёд]]

**Дата написания:** 05.09.2026

Последнее обновление: 12.01.2021
	
	
	
	- 

	- 

	- 

	
	
	
	

	
		
		
		
	

	
При работе со списком объектов мы можем столкнуться с проблемой добавления или удаления объектов в этом списке. Так, возьмем пример из прошлой темы и 
добавим в код визуального интерфейса пару кнопок, которые будут выполнять добавление и удаление:

```

    
        
        
            
                
                    
                        
                            
                                
                                
                                
                            
                        
                    
                
            
        
        
            
            
        
    

```

В файл кода C# добавим к странице обработчики кнопок:

```

using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using Xamarin.Forms;

namespace HelloApp
{
    public partial class MainPage : ContentPage
    {
        public List
Phones { get; set; }

        public MainPage()
        {
            InitializeComponent();
            Phones = new List
            {
                new Phone { Title = "HTC U Ultra", Company = "HTC", Price = 36000 },
                new Phone {Title="Huawei P10", Company="Huawei", Price=35000 },
                new Phone {Title="LG G 6", Company="LG", Price=42000 },
                new Phone {Title="iPhone 7", Company="Apple", Price=52000 }
            };

            this.BindingContext = this;
        }
        // добавление объекта
        private void AddItem(object sender, EventArgs e)
        {
            Phones.Add(new Phone { Title = "Galaxy S8", Company = "Samsung", Price = 48000 });
        }
        // удаление выделенного объекта
        private void RemoveItem(object sender, EventArgs e)
        {
            Phone phone = phonesList.SelectedItem as Phone;
            if (phone != null)
            {
                Phones.Remove(phone);
                phonesList.SelectedItem = null;
            }
        }
    }

    public class Phone
    {
        public string Title { get; set; }
        public string Company { get; set; }
        public int Price { get; set; }
    }
}

```

В данном случае типом коллекции является стандартный класс List, который поддерживает добавление и удаление с помощью методов `Add()` и `Remove()`. 
Однако при запуске приложения, если мы будем нажимать на кнопки, то никаких изменений в ListView, который отображает данный список, мы не увидим. 
Хотя в реальности коллекция Phones будет изменяться. Более того, мы можем столкнуться с исключением.

Чтобы решить эту проблемы в качестве типа коллекции, как правило, используется не класс List, а класс ObservableCollection из 
пространства имен `System.Collections.ObjectModel`. За счет реализации интерфейса `INotifyCollectionChanged` при добавлении или удалении 
объектов в ObservableCollection автоматически будут изменяться все привязанные к этой коллекции объекты, в том числе и ListView.

Итак, изменим определение коллекции Phones:

```

public ObservableCollection
Phones { get; set; }
public MainPage()
{
    InitializeComponent();
    Phones = new ObservableCollection
    {
        new Phone { Title = "HTC U Ultra", Company = "HTC", Price = 36000 },
        new Phone {Title="Huawei P10", Company="Huawei", Price=35000 },
        new Phone {Title="LG G 6", Company="LG", Price=42000 },
        new Phone {Title="iPhone 7", Company="Apple", Price=52000 }
    };
    this.BindingContext = this;
}

```

И теперь у нас не возникнет проблем с добавлением или удалением.

---

**Источник:** [https://metanit.com/sharp/xamarin/4.9.php](https://metanit.com/sharp/xamarin/4.9.php)

[[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 8. ListView и работа с данными/Создание класса ячейки для ListView|Назад]] | [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 8. ListView и работа с данными|Содержание]] | [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 8. ListView и работа с данными/Настройка внешнего вида ListView|Вперёд]]
