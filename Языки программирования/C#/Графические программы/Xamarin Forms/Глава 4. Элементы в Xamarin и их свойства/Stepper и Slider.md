[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Графические программы|Графические программы]] / [[Языки программирования/C#/Графические программы/Xamarin Forms|Xamarin Forms]] / [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 4. Элементы в Xamarin и их свойства|Глава 4. Элементы в Xamarin и их свойства]] / Stepper и Slider

[[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 4. Элементы в Xamarin и их свойства/Выпадающий список Picker|Назад]] | [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 4. Элементы в Xamarin и их свойства|Содержание]] | [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 4. Элементы в Xamarin и их свойства/Переключатель Switch|Вперёд]]

**Дата написания:** 05.09.2026

Последнее обновление: 10.01.2021
	
	
	
	- 

	- 

	- 

	
	
	
	

	
		
		
		
	

	
### Stepper

Stepper позволяет устанавливать числовое значение:

```

using Xamarin.Forms;
using System;

namespace HelloApp
{
    public partial class MainPage : ContentPage
    {

        Label header;
        public MainPage()
        {
            header = new Label
            {
                Text = "Stepper",
                FontSize = Device.GetNamedSize(NamedSize.Large, typeof(Label)),
                HorizontalOptions = LayoutOptions.Center
            };

            Stepper stepper = new Stepper
            {
                Minimum = 0,
                Maximum = 10,
                Increment = 0.1,
                HorizontalOptions = LayoutOptions.Center,
                VerticalOptions = LayoutOptions.CenterAndExpand
            };
            stepper.ValueChanged += OnStepperValueChanged;
            this.Content = new StackLayout { Children = { header, stepper } };
        }

        private void OnStepperValueChanged(object sender, ValueChangedEventArgs e)
        {
            header.Text = String.Format("Выбрано: {0:F1}", e.NewValue);
        }
    }
}

```

Stepper позволяет установить ряд свойств, который настраивают его поведение:

- Minimum: устанавливает минимальное значение

- Maximum: устанавливает максимальное значение

- Increment: устанавливает шаг изменения значения

Для отслеживания изменения значения можно обработать событие `ValueChanged`

Stepper в xaml:

```

  
  

```

А в файле связанного кода прописать обработчик OnStepperValueChanged:

```

private void OnStepperValueChanged(object sender, ValueChangedEventArgs e)
{
    if (header != null)
        header.Text = String.Format("Выбрано: {0:F1}", e.NewValue);
}

```

### Slider

Slider представляет собой горизонтальный ползунок и во многих аспектах он похож на Stepper. Среди его свойств можно выделить следующие:

- Minimum: устанавливает минимальное значение

- Maximum: устанавливает максимальное значение

- Value: текущее значение

- ThumbColor: цвет указателя текущего значения

- MinimumTrackColor: цвет ползунка до указателя значения

- MaximumTrackColor: цвет ползунка после указателя значения

Например, определение в коде C#

```

using Xamarin.Forms;
using System;

namespace HelloApp
{
    public partial class MainPage : ContentPage
    {
        Label header;

        public MainPage()
        {
            header = new Label
            {
                Text = "Slider",
                FontSize = Device.GetNamedSize(NamedSize.Large, typeof(Label)),
                HorizontalOptions = LayoutOptions.Center
            };

            Slider slider = new Slider 
			{ 
				Minimum = 0, 
				Maximum = 50, 
				Value = 30 
				ThumbColor=Color.DeepPink, 
				MinimumTrackColor=Color.DeepPink, 
				MaximumTrackColor=Color.Gray 
			};
            slider.ValueChanged += slider_ValueChanged;

            this.Content = new StackLayout { Children = { header, slider } };
        }

        void slider_ValueChanged(object sender, ValueChangedEventArgs e)
        {
            header.Text = String.Format("Выбрано: {0:F1}", e.NewValue);
        }
    }
}

```

Slider также позволяет установить минимальное и максимальное, а также текущее значение. И также изменение значения можно обработать с 
помощью обработки события `ValueChanged`

Аналогичный слайдер в xaml:

```

    
    

```

И в файле связанного кода пропишем обработчик slider_ValueChanged:

```

void slider_ValueChanged(object sender, ValueChangedEventArgs e)
{
    if(header!=null)
        header.Text = String.Format("Выбрано: {0:F1}", e.NewValue);
}

```

---

**Источник:** [https://metanit.com/sharp/xamarin/3.12.php](https://metanit.com/sharp/xamarin/3.12.php)

[[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 4. Элементы в Xamarin и их свойства/Выпадающий список Picker|Назад]] | [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 4. Элементы в Xamarin и их свойства|Содержание]] | [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 4. Элементы в Xamarin и их свойства/Переключатель Switch|Вперёд]]
