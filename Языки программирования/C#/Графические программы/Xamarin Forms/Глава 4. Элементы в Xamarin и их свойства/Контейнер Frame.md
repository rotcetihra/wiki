[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Графические программы|Графические программы]] / [[Языки программирования/C#/Графические программы/Xamarin Forms|Xamarin Forms]] / [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 4. Элементы в Xamarin и их свойства|Глава 4. Элементы в Xamarin и их свойства]] / Контейнер Frame

[[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 4. Элементы в Xamarin и их свойства/Текстовые поля|Назад]] | [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 4. Элементы в Xamarin и их свойства|Содержание]] | [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 4. Элементы в Xamarin и их свойства/BoxView|Вперёд]]

**Дата написания:** 05.09.2026

Последнее обновление: 10.01.2021
	
	
	
	- 

	- 

	- 

	
	
	
	

	
		
		
		
	

	
Контейнер Frame, как правило используется для оформления или создания фона для вложенного элемента.

Среди свойств класса Frame следует выделить следующие:

- BorderColor: представляет цвет границы фрейма с помощью структуры Color.

- CornerRadius: представляет радиус границы фрейма в виде значения типа float.

- HasShadow: хранит значение типа bool, которое указывает, будет ли фрейм отбрасывать тень.

Стоит учитывать, что фрейм может вмещать только один элемент. Например, создание фрейма в XAML:

```

  

```

Создание фрейма в коде C#:

```

Frame frame = new Frame
{
    Content = new Label { Text = "Hello Xamarin" }
};

```

Ключевым моментом использования фреймов является возможность установить некоторое внешнее оформление для вложенного элемента, 
например, с помощью установки цвета границы, ее радиуса, цвета фона.

```

    
        
            
        
    

```

Аналогичный пример в коде C#:

```

using Xamarin.Forms;

namespace HelloApp
{
    public partial class MainPage : ContentPage
    {
        public MainPage()
        {
            //InitializeComponent();
            Label label = new Label
            {
                Text = "Xamarin Forms",
                FontSize = Device.GetNamedSize(NamedSize.Large, typeof(Label)),
                HorizontalOptions = LayoutOptions.Center
            };
            Frame frame = new Frame 
            {
                Content = label,
                BorderColor = Color.Gray,
                BackgroundColor = Color.FromHex("#e1e1e1"),
                CornerRadius = 8
            };
            StackLayout stackLayout = new StackLayout() { Children = { frame }, Padding = 20 };
            Content = stackLayout;
        }

    }
}

```

---

**Источник:** [https://metanit.com/sharp/xamarin/3.3.php](https://metanit.com/sharp/xamarin/3.3.php)

[[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 4. Элементы в Xamarin и их свойства/Текстовые поля|Назад]] | [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 4. Элементы в Xamarin и их свойства|Содержание]] | [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 4. Элементы в Xamarin и их свойства/BoxView|Вперёд]]
