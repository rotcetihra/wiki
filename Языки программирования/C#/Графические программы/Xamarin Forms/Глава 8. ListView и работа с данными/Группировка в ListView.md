[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Графические программы|Графические программы]] / [[Языки программирования/C#/Графические программы/Xamarin Forms|Xamarin Forms]] / [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 8. ListView и работа с данными|Глава 8. ListView и работа с данными]] / Группировка в ListView

[[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 8. ListView и работа с данными/Настройка внешнего вида ListView|Назад]] | [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 8. ListView и работа с данными|Содержание]] | [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 8. ListView и работа с данными/Производительность ListView|Вперёд]]

**Дата написания:** 05.09.2026

Последнее обновление: 12.01.2021
	
	
	
	- 

	- 

	- 

	
	
	
	

	
		
		
		
	

	
Элемент ListView в Xamarin поддерживает возможности группировки. Рассмотрим, как мы можем сгруппировать элементы в списке

Для группировки в начале добавим в проект вспомогательный класс, который назовем Grouping:

```

using System.Collections.Generic;
using System.Collections.ObjectModel;

namespace HelloApp
{
    public class Grouping : ObservableCollection
    {
        public K Name { get; private set; }
        public Grouping(K name, IEnumerable items)
        {
            Name = name;
            foreach (T item in items)
                Items.Add(item);
        }
    }
}

```

Класс Grouping типизирован двумя параметрами. Параметр K представляет тип ключа группы, который будет храниться в свойстве `Name`. 
А параметр T представляет тип объектов, которые будут храниться в коллекции Items. Это свойство-коллекция унаследовано от базового класса ObservableCollection. 
А в конструкторе мы получаем все необходимые данные.

В качестве объектов возьмем опять же класс Phone:

```

public class Phone
{
    public string Title { get; set; }
    public string Company { get; set; }
    public int Price { get; set; }
}

```

В коде страницы MainPage создадим список групп:

```

using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using Xamarin.Forms;

namespace HelloApp
{
    public partial class MainPage : ContentPage
    {
        // список групп, к которым идет привязка
        public ObservableCollection> PhoneGroups { get; set; }
        public MainPage()
        {
            InitializeComponent();

            // начальные данные
            var phones = new List
{
                new Phone {Title="Galaxy S8", Company="Samsung", Price=60000 },
                new Phone {Title="Galaxy S7 Edge", Company="Samsung", Price=50000 },
                new Phone {Title="Huawei P10", Company="Huawei", Price=10000 },
                new Phone {Title="Huawe Mate 8", Company="Huawei", Price=29000 },
                new Phone {Title="Mi6", Company="Xiaomi", Price=55000 },
                new Phone {Title="iPhone 7", Company="Apple", Price=38000 },
                new Phone {Title="iPhone 6S", Company="Apple", Price=50000 }
            };
            // получаем группы
            var groups = phones.GroupBy(p => p.Company).Select(g => new Grouping(g.Key, g));
            // передаем группы в PhoneGroups
            PhoneGroups = new ObservableCollection>(groups);
            this.BindingContext = this;
        }
    }
}

```

В конструкторе переменная `phones` определяет общие данные, по которым создается коллекция групп в виде свойства `PhoneGroups`. Группировка 
в данном случае идет по свойству Company объекта Phone.

А в коде xaml у MainPage пропишем выражения привязки:

```

    
        
            
                
                    
                        
                            
                            
                        
                    
                
            
        
    

```

Привязка ListView здесь идет к свойству PhoneGroups, которое содержит группы. Установка свойства `IsGroupingEnabled="True"` добавляет в ListView поддержку групп.

С помошью свойства GroupDisplayBinding можно задать то значение, которое будет отображаться для каждой группы. В нашем случае идет 
привязка к имени группы, которое представляет критерий группировки.

И после запуска приложения все данные в списке будут сгруппированы по компаниям:

Однако по умолчанию заголовки групп выглядят не очень хорошо, мало отличимы от основного содержимого элементов. И в этом случае мы можем настроить шаблон отображения 
заголовков групп. Для этого изменим разметку xaml:

```

    
        
            
                
                    
                        
                            
                        
                    
                
            
            
                
                    
                        
                            
                            
                        
                    
                
            
        
    

```

Свойство GroupHeaderTemplate позволяет в корне изменить отображение заголовка, определив ему свой шаблон DataTemplate:

---

**Источник:** [https://metanit.com/sharp/xamarin/4.10.php](https://metanit.com/sharp/xamarin/4.10.php)

[[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 8. ListView и работа с данными/Настройка внешнего вида ListView|Назад]] | [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 8. ListView и работа с данными|Содержание]] | [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 8. ListView и работа с данными/Производительность ListView|Вперёд]]
