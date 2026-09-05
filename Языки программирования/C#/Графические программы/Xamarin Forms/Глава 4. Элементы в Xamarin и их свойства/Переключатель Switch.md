[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Графические программы|Графические программы]] / [[Языки программирования/C#/Графические программы/Xamarin Forms|Xamarin Forms]] / [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 4. Элементы в Xamarin и их свойства|Глава 4. Элементы в Xamarin и их свойства]] / Переключатель Switch

[[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 4. Элементы в Xamarin и их свойства/Stepper и Slider|Назад]] | [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 4. Элементы в Xamarin и их свойства|Содержание]] | [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 4. Элементы в Xamarin и их свойства/TableView|Вперёд]]

**Дата написания:** 05.09.2026

Последнее обновление: 10.01.2021
	
	
	
	- 

	- 

	- 

	
	
	
	

	
		
		
		
	

	
Элемент Switch представляет переключатель, который может находиться в двух состояниях: включенном и выключенном.

Среди свойств класса Switch стоит выделить следующие:

- IsToggled: указывает, находится ли Switch во включенном состоянии (значение true) или 
выключенном (значение false)

- ThumbColor: цвет кнопки переключателя

- OnColor: цвет переключателя во включенном состоянии

Создадим элемент Switch s коде C#:

```

using Xamarin.Forms;
using System;

namespace HelloApp
{
    public partial class MainPage : ContentPage
    {

        Label label;

        public MainPage()
        {
            Label header = new Label
            {
                Text = "Переключатель",
                FontSize = Device.GetNamedSize(NamedSize.Large, typeof(Label)),
                HorizontalOptions = LayoutOptions.Center
            };

            Switch switcher = new Switch
            {
                IsToggled = true,
                HorizontalOptions = LayoutOptions.Center,
                VerticalOptions = LayoutOptions.CenterAndExpand
            };
            switcher.Toggled += switcher_Toggled;
            label = new Label
            {
                FontSize = Device.GetNamedSize(NamedSize.Large, typeof(Label)),
                HorizontalOptions = LayoutOptions.Center,
                VerticalOptions = LayoutOptions.CenterAndExpand
            };
            this.Content = new StackLayout { Children = { header, switcher, label } };
        }

        private void switcher_Toggled(object sender, ToggledEventArgs e)
        {
            label.Text = $"Значение {e.Value}";
        }
    }
}

```

Если надо установить переключатель в определенное состояние, то применяется свойство `IsToggled`. По умолчанию оно имеет значение false. Чтобы отследить смену состояния, 
мы можем обработать событие `Toggled`

Аналог в xaml:

```

 
    
    
    
  

```

---

**Источник:** [https://metanit.com/sharp/xamarin/3.13.php](https://metanit.com/sharp/xamarin/3.13.php)

[[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 4. Элементы в Xamarin и их свойства/Stepper и Slider|Назад]] | [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 4. Элементы в Xamarin и их свойства|Содержание]] | [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 4. Элементы в Xamarin и их свойства/TableView|Вперёд]]
