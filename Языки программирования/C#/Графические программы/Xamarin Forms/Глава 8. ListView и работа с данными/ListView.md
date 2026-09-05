[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Графические программы|Графические программы]] / [[Языки программирования/C#/Графические программы/Xamarin Forms|Xamarin Forms]] / [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 8. ListView и работа с данными|Глава 8. ListView и работа с данными]] / ListView

[[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 8. ListView и работа с данными|Содержание]] | [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 8. ListView и работа с данными/DataTemplate и сложные объекты в ListView|Вперёд]]

**Дата написания:** 05.09.2026

## ListView
Последнее обновление: 12.01.2021
	
	
	
	- 

	- 

	- 

	
	
	
	

	
		
		
		
	

	
ListView представляет очень мощный элемет управления Xamarin Forms, который позволяет отображать список объектов и 
при этом кастомизировать их отображение.

ListView связывается с набором данных через свойство ItemsSource, которое принимает объект `IEnumerable`.

### Создание ListView в коде C#
 

Определим в коде C# объект ListView, который выводит массив строк:

```

using Xamarin.Forms;

namespace HelloApp
{
    public partial class MainPage : ContentPage
    {
        public MainPage()
        {
            Label header = new Label
            {
                Text = "Список моделей",
                FontSize = Device.GetNamedSize(NamedSize.Large, typeof(Label)),
                HorizontalOptions = LayoutOptions.Center
            };

            string[] phones = new string[] {"iPhone 7", "Samsung Galaxy S8", "Huawei P10", "LG G6"};

            ListView listView = new ListView();
            // определяем источник данных
            listView.ItemsSource = phones;
            this.Content = new StackLayout { Children = { header, listView } };
        }
    }
}

```

При выводе каждого объекта ListView по умолчанию вызывает для него метод `ToString()`, поэтому мы увидим строковое отображение объекта.

### ListView в XAML

Аналогичный массив в XAML мы могли бы вывести следующим образом:

```

    
        
            
                iPhone 7
                Google Pixel 5
                Huawei P10
                Xiaomi Mi6
            
        
    
    
        
        
    

```

### Сочетание XAML и C#. Привязка к списку

Нередко источник данных для ListView определяется в коде C#. И в этом случае мы можем использовать привязку к источнику данных. Например, в коде C# определим 
массив, к которому будет производиться привязка:

```

using Xamarin.Forms;

namespace HelloApp
{
	public partial class MainPage : ContentPage
	{
        public string[] Phones { get; set; }

        public MainPage()
		{
            InitializeComponent();
            Phones = new string[] { "iPhone 8", "Samsung Galaxy S9", "Huawei P10", "LG G6" };
            this.BindingContext = this;
        }
	}
}

```

Стоит отметить, что источник данных определен как публичное свойство Phones. Другой важный момент - установка контекста привязки страницы: `this.BindingContext = this;`. 
Таким образом, в XAML мы можем обратиться ко всем публичным свойствам страницы.

В коде XAML пропишем привязку к этому свойству:

```

    
        
        
    

```

### Привязка к выбранному элементу

В примере выше мы вполне могли бы обойтись без обработки события и просто установить привязку элемента Label к выбранному объекту списка:

```

    
        
            
                iPhone 7
                Google Pixel 5
                Huawei P10
                Xiaomi Mi6
            
        
    
    
        
        
    

```

### Выбор элемента

Когда пользователь нажимает на элемент списка, он выделяется, а у ListView срабатывают два события: ItemTapped и ItemSelected. Между ними есть 
различия. Так, повторное нажатие на один и тот же элемент не вызовет повторного события ItemSelected, так как элемент остается выбанным. А вот событие ItemTapped будет срабатывать именно столько раз сколько 
пользователь нажал на него, даже повторно. Также событие ItemSelected будет вызвано, если с элемента будет снято выделение.

#### ItemSelected

Обработаем выделение элемента. Для этого определим следующий код в XAML:

```

    
        
        
    

```

А в файле кода MainPage.xaml.cs определим источник данных и обработчик события ItemSelected:

```

using Xamarin.Forms;

namespace HelloApp
{
    public partial class MainPage : ContentPage
    {
        public MainPage()
        {
            InitializeComponent();
            string[] phones = new string[] {"iPhone 7", "Samsung Galaxy S8", "Huawei P10", "LG G6"};
            phonesList.ItemsSource = phones;
        }
        private void phonesList_ItemSelected(object sender, SelectedItemChangedEventArgs e)
        {
            if(e.SelectedItem!=null)
                selected.Text = e.SelectedItem.ToString();
        }
    }
}

```

При выборе элемента мы можем получить выбранный элемент через свойство SelectedItem объекта SelectedItemChangedEventArgs, который передается в качестве параметра. 
Так как событие ItemSelected может срабатывать и при снятии выделения элемента, то в обработчике необходимо вначале проверить значение `e.SelectedItem` на null.

Поскольку список содержит массив строк, то каждый его элемент представляет строку, которую мы можем получить с помощью метода `e.SelectedItem.ToString()`.

Как можно увидеть на скриншоте, выбранный элемент выделяется цветом. Однако выделение на Android оранжевым цветом элементов списка, которые имеют по умолчанию розовые буквы, наверное, 
не самое удачное дизайнерское решение. Кроме того, возможно выделение в прицнипе неприемлимо, и в этом случае мы его можем сразу же снять после выбора элемента:

```

private void phonesList_ItemSelected(object sender, SelectedItemChangedEventArgs e)
{
    if(e.SelectedItem!=null)
        selected.Text = e.SelectedItem.ToString();
	((ListView)sender).SelectedItem = null;
}

```

#### ItemTapped

Похожим образом можно обработать событие ItemTapped. Определим в XAML следующий код:

```

    
        
        
    

```

А в файле кода MainPage.xaml.cs определим источник данных и обработчик события ItemTapped:

```

using Xamarin.Forms;

namespace HelloApp
{
	public partial class MainPage : ContentPage
	{
        public string[] Phones { get; set; }

        public MainPage()
		{
            InitializeComponent();
            string[] phones = new string[] { "iPhone 7", "Samsung Galaxy S8", "Huawei P10", "LG G6" };
            phonesList.ItemsSource = phones;
        }

        private void PhonesList_ItemTapped(object sender, ItemTappedEventArgs e)
        {
            if (e.Item != null)
                selected.Text = e.Item.ToString();
            ((ListView)sender).SelectedItem = null;
        }
    }
}

```

---

**Источник:** [https://metanit.com/sharp/xamarin/3.16.php](https://metanit.com/sharp/xamarin/3.16.php)

[[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 8. ListView и работа с данными|Содержание]] | [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 8. ListView и работа с данными/DataTemplate и сложные объекты в ListView|Вперёд]]
