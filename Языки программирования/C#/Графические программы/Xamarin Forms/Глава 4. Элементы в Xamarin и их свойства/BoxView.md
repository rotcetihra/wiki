[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Графические программы|Графические программы]] / [[Языки программирования/C#/Графические программы/Xamarin Forms|Xamarin Forms]] / [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 4. Элементы в Xamarin и их свойства|Глава 4. Элементы в Xamarin и их свойства]] / BoxView

[[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 4. Элементы в Xamarin и их свойства/Контейнер Frame|Назад]] | [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 4. Элементы в Xamarin и их свойства|Содержание]] | [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 4. Элементы в Xamarin и их свойства/Работа с изображениями. Элемент Image|Вперёд]]

**Дата написания:** 05.09.2026

Последнее обновление: 10.01.2021
	
	
	
	- 

	- 

	- 

	
	
	
	

	
		
		
		
	

	
BoxView представляет прямоугольник. Чаще всего BoxView используется для создания окрашенных областей, либо в качестве декоративного примитивного графического оформления к другим 
элементам.

Основные свойства класса BoxView:

- Color: представляет цвет элемента в виде структуры Color.

- CornerRadius: представляет радиус границы BoxView в виде значения типа float.

- WidthRequest: представляет ширину элемента (по умолчанию равна 40 единицам).

- HeightRequest: представляет высоту элемента (по умолчанию равна 40 единицам).

Создание BoxView в xaml:

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
            InitializeComponent();
            BoxView boxView = new BoxView
            {
                Color = Color.LightBlue,
                CornerRadius = 8,
                WidthRequest = 150,
                HeightRequest = 150,
                HorizontalOptions = LayoutOptions.Center,
                VerticalOptions = LayoutOptions.CenterAndExpand
            };
            StackLayout stackLayout = new StackLayout() { Children = { boxView }};
            Content = stackLayout;
        }
    }
}

```

Также можно использовать BoxView для создания прямоугольного графического декоративного орнамента там, где не нужна сложная графика, 
а стандартные свойства элементов не позволяют это сделать. Нередко подобным образом BoxView используется в контейнере AbsoluteLayout, 
так как тот позволяет определить фиксированное положение, но и в других контейнерах также можно применять. Например, нам надо начертить двойную линию:

Пример в xaml:

```

    
        
            
                
                
                
                
            
        
    

```

Аналогичный пример в C#:

```

using Xamarin.Forms;

namespace HelloApp
{
    public partial class MainPage : ContentPage
    {
        public MainPage()
        {
            //InitializeComponent();
            Label label1 = new Label
            {
                Text = "METANIT.COM",
                FontSize = Device.GetNamedSize(NamedSize.Title, typeof(Label)),
                HorizontalOptions = LayoutOptions.Center
            };
            Label label2 = new Label
            {
                Text = "Руководство по Xamarin Forms",
                FontSize = Device.GetNamedSize(NamedSize.Large, typeof(Label)),
                HorizontalOptions = LayoutOptions.Center
            };
            BoxView boxView1 = new BoxView
            {
                Color = Color.Gray,
                HeightRequest = 2,
                HorizontalOptions = LayoutOptions.Fill
            };
            BoxView boxView2 = new BoxView
            {
                Color = Color.Gray,
                HeightRequest = 2,
                HorizontalOptions = LayoutOptions.Fill
            };
            StackLayout innerStackLayout = new StackLayout { Children = { label1, boxView1, boxView2, label2 } };
            Frame frame = new Frame
            {
                Content = innerStackLayout,
                BorderColor = Color.Gray,
                BackgroundColor = Color.FromHex("#e1e1e1"),
                CornerRadius = 8
            };
            
            StackLayout stackLayout = new StackLayout() { Children = { frame }, Padding = 20};
            Content = stackLayout;
        }
    }
}

```

---

**Источник:** [https://metanit.com/sharp/xamarin/3.23.php](https://metanit.com/sharp/xamarin/3.23.php)

[[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 4. Элементы в Xamarin и их свойства/Контейнер Frame|Назад]] | [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 4. Элементы в Xamarin и их свойства|Содержание]] | [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 4. Элементы в Xamarin и их свойства/Работа с изображениями. Элемент Image|Вперёд]]
