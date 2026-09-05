[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Графические программы|Графические программы]] / [[Языки программирования/C#/Графические программы/Xamarin Forms|Xamarin Forms]] / [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 8. ListView и работа с данными|Глава 8. ListView и работа с данными]] / DataTemplate и сложные объекты в ListView

[[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 8. ListView и работа с данными/ListView|Назад]] | [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 8. ListView и работа с данными|Содержание]] | [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 8. ListView и работа с данными/TextCell|Вперёд]]

**Дата написания:** 05.09.2026

Последнее обновление: 12.01.2021
	
	
	
	- 

	- 

	- 

	
	
	
	

	
		
		
		
	

	
В прошлой теме был рассмотрен вывод в ListView простейших данных - массива строк. На самом деле в простейшем варианте ListView получает для 
каждого объекта списка стоковое представление и выводит его в отдельной ячейке. Однако, как правило, данные, которыми манипулируют приложения, 
представляют более сложные по структуре объекты, которые могут содержать множество свойств. И для организации отображения каждого объекта в ListView определяется 
шаблон данных или DataTemplate.

Рассмотрим, как выполнять привязку к списку объектов на примере ListView. Для создания объектов определим класс Phone:

```

public class Phone
{
    public string Title { get; set; }
    public string Company { get; set; }
    public int Price { get; set; }
}

```

Теперь определим следующий класс страницы:

```

public partial class MainPage : ContentPage
{
    public List
Phones { get; set; }

    public MainPage()
    {
        Label header = new Label
        {
            Text = "Список моделей",
            FontSize = Device.GetNamedSize(NamedSize.Large, typeof(Label)),
            HorizontalOptions = LayoutOptions.Center
        };

        Phones = new List
        {
            new Phone {Title="Galaxy S8", Company="Samsung", Price=48000 },
            new Phone {Title="Huawei P10", Company="Huawei", Price=35000 },
            new Phone {Title="HTC U Ultra", Company="HTC", Price=42000 },
            new Phone {Title="iPhone 7", Company="Apple", Price=52000 }
        };
        ListView listView = new ListView
        {
            HasUnevenRows = true,
            // Определяем источник данных
            ItemsSource = Phones,

            // Определяем формат отображения данных
            ItemTemplate = new DataTemplate(() =>
            {
                // привязка к свойству Name
                Label titleLabel = new Label { FontSize=18 };
                titleLabel.SetBinding(Label.TextProperty, "Title");

                // привязка к свойству Company
                Label companyLabel = new Label();
                companyLabel.SetBinding(Label.TextProperty, "Company");

                // привязка к свойству Price
                Label priceLabel = new Label();
                priceLabel.SetBinding(Label.TextProperty, "Price");

                // создаем объект ViewCell.
                return new ViewCell
                {
                    View = new StackLayout
                    {
                        Padding = new Thickness(0, 5),
                        Orientation = StackOrientation.Vertical,
                        Children = { titleLabel, companyLabel, priceLabel}
                    }
                };
            })
        };
        this.Content = new StackLayout { Children = { header, listView } };
    }
}

```

Для создания списков сложных объектов нам надо использовать три свойства. `ItemsSource` определяет, какие данные будет содержать список. 
Свойство `HasUnevenRows` со значением `true` позволит динамически устанавливать высоту строк в ListView в зависимости от размера содержимого. 
А свойство `ItemTemplate` определяет, как эти данные будут отображаться. ItemTemplate представляет объект DataTemplate, 
который в качестве параметра принимает делегат. Содержимое DataTemplate представляет одну из ячеек, то есть класс Cell. В данном случае это тип ViewCell, поэтому в качестве итога возвращается объект 
ViewCell, определяющий структуру строки в ListView.

Внутри ViewCell внутренние элементы упавляются контейнером StackLayout, а отдельные элементы Label внутри StackLayout привязаны к отдельным свойствам объекта Phone.

Определение DataTemplate в коде XAML:

```

    
        
        
            
                
                    
                        
                            
                                
                                
                                
                            
                        
                    
                
            
        
    

```

Здесь практически тоже самое, за исключением некоторых моментов. Так, атрибут `ItemsSource="{Binding Phones}"` устанавливает привязку к свойству Phones, которое мы длее определим.

И атрибут `ItemTapped="OnItemTapped"` устанавливает обработчик, который будет срабатывать при нажатии на один из элементов списка.

Для определения визуального шаблона выводимых данных применяется объект DataTemplate, в котором через элемент ViewCell устанавливается формат отображения - 
в виде вертикального стека элементов Label, каждый из которых привязан к одному из свойств объекта Phone:

```

   
      
        
           
           
           
        
      
   

```

Также надо отметить, что сверху определен элемент Label, текст которого привязан к названию выбранной в списке модели:

```

```

Затем в коде на c# определим свойство Phones, к которому будет привязан список ListView, и обработчик нажатия на объект списка:

```

using System.Collections.Generic;
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
                new Phone {Title="Galaxy S8", Company="Samsung", Price=48000 },
                new Phone {Title="Huawei P10", Company="Huawei", Price=35000 },
                new Phone {Title="HTC U Ultra", Company="HTC", Price=42000 },
                new Phone {Title="iPhone 7", Company="Apple", Price=52000 }
            };
            this.BindingContext = this;
        }

        public async void OnItemTapped(object sender, ItemTappedEventArgs e)
        {
            Phone selectedPhone = e.Item as Phone;
            if (selectedPhone != null)
                await DisplayAlert("Выбранная модель", $"{selectedPhone.Company} - {selectedPhone.Title}", "OK");
        }
    }
}

```

Установка в качестве контекста данных текущего объекта:

```
this.BindingContext = this;
```

Позволит использовать все свойства этого объекта (в данном случае свойство Phones) в коде XAML.

В обработчике события `OnItemTapped` получаем выбранный объект. И так как каждый объект в DataTemplate представляет тип Phone, то мы можем привести 
значение `e.Item` к типу Phone.

В итоге, когда мы запустим приложение, то в списке отобразится несколько начальных объектов, а название выбранного объекта появится в верхе страницы.

---

**Источник:** [https://metanit.com/sharp/xamarin/4.8.php](https://metanit.com/sharp/xamarin/4.8.php)

[[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 8. ListView и работа с данными/ListView|Назад]] | [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 8. ListView и работа с данными|Содержание]] | [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 8. ListView и работа с данными/TextCell|Вперёд]]
