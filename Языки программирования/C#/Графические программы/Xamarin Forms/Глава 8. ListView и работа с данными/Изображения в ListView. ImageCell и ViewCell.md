[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Графические программы|Графические программы]] / [[Языки программирования/C#/Графические программы/Xamarin Forms|Xamarin Forms]] / [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 8. ListView и работа с данными|Глава 8. ListView и работа с данными]] / Изображения в ListView. ImageCell и ViewCell

[[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 8. ListView и работа с данными/TextCell|Назад]] | [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 8. ListView и работа с данными|Содержание]] | [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 8. ListView и работа с данными/Создание класса ячейки для ListView|Вперёд]]

**Дата написания:** 05.09.2026

Последнее обновление: 12.01.2021
	
	
	
	- 

	- 

	- 

	
	
	
	

	
		
		
		
	

	
Для отображения изображений в ListView в простых случаях мы можем использовать класс ImageCell, а в более сложных можно воспользоваться 
ViewCell.

Класс ImageView расширяет класс TextCell, добавляя свойство `ImageSource`, которое указывает на источник изображения.

Ранее в теме [Работа с изображениями. Элемент Image](./3.9.php) уже рассматривалось, как добавлять изображения проект и выводить их на страницу. 
И аналогичным образом добавим в проекты несколько изображений:

В проект для Android изображения добавляются в папку Drawables, в проект для iOS - через папку папке Assets Catalogs, в проект для UWP - в корневую папку проекта.

Теперь определим класс страницы, которая будет выводить эти изображения через ImageCell:

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
            Phones = new List
            {
                new Phone {Title="Galaxy S8", Company="Samsung", Price=48000, ImagePath="galaxys6.jpg" },
                new Phone {Title="Huawei P10", Company="Huawei", Price=35000, ImagePath="mate8.jpg" },
                new Phone {Title="HP Elite z3", Company="HP", Price=42000, ImagePath="lumia950.jpg" },
                new Phone {Title="LG G 6", Company="LG", Price=42000, ImagePath="nexus5x.jpg" },
                new Phone {Title="iPhone 7", Company="Apple", Price=52000, ImagePath="iphone6s.jpg" }
            };
            Label header = new Label
            {
                Text = "Список моделей",
                FontSize = Device.GetNamedSize(NamedSize.Large, typeof(Label))
            };
            ListView listView = new ListView
            {
                HasUnevenRows = true,
                ItemsSource = Phones,
                // Определяем формат отображения данных
                ItemTemplate = new DataTemplate(() =>
                {
                    ImageCell imageCell = new ImageCell { TextColor = Color.Red, DetailColor = Color.Green };
                    imageCell.SetBinding(ImageCell.TextProperty, "Title");
                    Binding companyBinding = new Binding { Path = "Company", StringFormat="Флагман от компании {0}"};
                    imageCell.SetBinding(ImageCell.DetailProperty, companyBinding);
                    imageCell.SetBinding(ImageCell.ImageSourceProperty, "ImagePath");
                    return imageCell;
                })
            };
            listView.ItemTapped += OnItemTapped;
            this.Content = new StackLayout { Children = { header, listView } };
        }
        public async void OnItemTapped(object sender, ItemTappedEventArgs e)
        {
            Phone selectedPhone = e.Item as Phone;
            if (selectedPhone != null)
                await DisplayAlert("Выбранная модель", $"{selectedPhone.Company} - {selectedPhone.Title}", "OK");
        }
    }
    public class Phone
    {
        public string Title { get; set; }
        public string ImagePath { get; set; }
        public string Company { get; set; }
        public int Price { get; set; }
    }
}

```

По сравнению с прошлой темой в класс Phone было добавлено свойство ImagePath, которое хранит путь к изображению в проекте. К этому свойству осуществляется 
привязка свойства ImageSource объекта ImageCell.

Аналогичный пример в Xaml:

```

    
        
        
            
                
                    
                
            
        
    

```

И в файле кода происходит создание источника данных:

```

public partial class MainPage : ContentPage
{
    public List
Phones { get; set; }

    public MainPage()
    {
        InitializeComponent();
        Phones = new List
        {
            new Phone {Title="Galaxy S8", Company="Samsung", Price=48000, ImagePath="galaxys6.jpg" },
            new Phone {Title="Huawei P10", Company="Huawei", Price=35000, ImagePath="mate8.jpg" },
            new Phone {Title="HP Elite z3", Company="HP", Price=42000, ImagePath="lumia950.jpg" },
            new Phone {Title="LG G 6", Company="LG", Price=42000, ImagePath="nexus5x.jpg" },
            new Phone {Title="iPhone 7", Company="Apple", Price=52000, ImagePath="iphone6s.jpg" }
        };
        this.BindingContext = this;
    }
}

```

### Вывод изображения в ViewCell

В то же время следует отметить, что на UWP, в отличие от Android и iOS, отсутствует масштабирование изображения. И оно отображается в тех размерах, которые имеет. 
В этом случае мы можем выводить элементы списка через ViewCell, задавая у элемента Image явным образом высоту и ширину:

```

    
        
        
            
                
                    
                        
                            
                            
                                
                                
                                
                            
                        
                    
                
            
        
    

```

---

**Источник:** [https://metanit.com/sharp/xamarin/4.13.php](https://metanit.com/sharp/xamarin/4.13.php)

[[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 8. ListView и работа с данными/TextCell|Назад]] | [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 8. ListView и работа с данными|Содержание]] | [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 8. ListView и работа с данными/Создание класса ячейки для ListView|Вперёд]]
