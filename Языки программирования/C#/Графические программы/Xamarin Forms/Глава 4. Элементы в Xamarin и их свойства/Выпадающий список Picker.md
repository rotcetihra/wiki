[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Графические программы|Графические программы]] / [[Языки программирования/C#/Графические программы/Xamarin Forms|Xamarin Forms]] / [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 4. Элементы в Xamarin и их свойства|Глава 4. Элементы в Xamarin и их свойства]] / Выпадающий список Picker

[[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 4. Элементы в Xamarin и их свойства/Выбор даты и времени. DatePicker и TimePicker|Назад]] | [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 4. Элементы в Xamarin и их свойства|Содержание]] | [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 4. Элементы в Xamarin и их свойства/Stepper и Slider|Вперёд]]

**Дата написания:** 05.09.2026

Последнее обновление: 10.01.2021
	
	
	
	- 

	- 

	- 

	
	
	
	

	
		
		
		
	

	
Визуально Picker представляет собой обычное текстовое поле, по нажатию на которое открывается список для выбора, что-то наподобие выпадающего списка:

```

public partial class MainPage : ContentPage
{
    Label header;
    Picker picker;
    public MainPage()
    {
        header = new Label
        {
            Text = "Выберите язык",
            FontSize = Device.GetNamedSize(NamedSize.Large, typeof(Label))
        };

        picker = new Picker 
		{
			Title = "Язык"
        };
        picker.Items.Add("C#");
        picker.Items.Add("JavaScript");
        picker.Items.Add("Java");
        picker.Items.Add("PHP");

        picker.SelectedIndexChanged += picker_SelectedIndexChanged;

        this.Content = new StackLayout { Children = { header, picker } };
    }

    void picker_SelectedIndexChanged(object sender, EventArgs e)
    {
        header.Text = "Вы выбрали: " + picker.Items[picker.SelectedIndex];
    }
}

```

Picker содержит список для выбора, а отследить выбранный элемент мы можем с помощью обработчик события `SelectedIndexChanged`.

Аналог в xaml:

```

    
    
C#
        C/C++
        JavaScript
        PHP
      
    
  

```

И тогда в файл связанного кода надо добавить обработчик события:

```

void picker_SelectedIndexChanged(object sender, EventArgs e)
{
    header.Text = "Вы выбрали: " + picker.Items[picker.SelectedIndex];
}

```

---

**Источник:** [https://metanit.com/sharp/xamarin/3.11.php](https://metanit.com/sharp/xamarin/3.11.php)

[[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 4. Элементы в Xamarin и их свойства/Выбор даты и времени. DatePicker и TimePicker|Назад]] | [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 4. Элементы в Xamarin и их свойства|Содержание]] | [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 4. Элементы в Xamarin и их свойства/Stepper и Slider|Вперёд]]
