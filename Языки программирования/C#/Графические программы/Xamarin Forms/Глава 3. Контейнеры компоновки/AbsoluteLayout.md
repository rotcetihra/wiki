[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Графические программы|Графические программы]] / [[Языки программирования/C#/Графические программы/Xamarin Forms|Xamarin Forms]] / [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 3. Контейнеры компоновки|Глава 3. Контейнеры компоновки]] / AbsoluteLayout

[[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 3. Контейнеры компоновки/StackLayout и ScrollView|Назад]] | [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 3. Контейнеры компоновки|Содержание]] | [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 3. Контейнеры компоновки/RelativeLayout|Вперёд]]

**Дата написания:** 05.09.2026

Последнее обновление: 09.01.2021
	
	
	
	- 

	- 

	- 

	
	
	
	

	
		
		
		
	

	
AbsoluteLayout позволяет задавать вложенным элементам абсолютные координаты расположения на странице и подходит больше для тех 
случаев, когда нам нужны элементы с точными координатами.

Для создания абсолютного позиционирования нам надо определить прямоугольную область, которую будет занимать элемент. Как правило, для этого используется 
структура Rectangle, которая представляет прямоугольник:

```

int x = 10;	// позиция координаты X на странице
int y = 10;	// позиция координаты Y на странице
int width = 100; // ширина блока элемента
int height = 80;	// высота блока элемента
Rectangle rect = new Rectangle(x, y, width, height);

```

Если нам неизвестна точная ширина и длина элемента, то мы можем ограничиться позицией, с которой начинается элемент, в виде структуры Point:

```

int x = 10;	// позиция координаты X на странице
int y = 10;	// позиция координаты Y на странице
Point point = new Point(x, y);

```

Непосредственно для добавления элементов в контейнер AbsoluteLayout мы можем использовать метод `AbsoluteLayout.Children.Add()`, который имеет ряд версий:

- `Add(View view)`: просто добавляет элемент в контейнер

- `Add(View view, Point point)`: элемент будет располагаться на странице, начиная с точки point

- `Add(View view, Rectangle rect)`: элемент будет располагаться на странице в области, ограниченной прямоугольником rect

Например, добавим пару элементов:

```

public class MainPage : ContentPage
{
    public MainPage()
    {
        AbsoluteLayout absoluteLayout = new AbsoluteLayout();
		absoluteLayout.Children.Add(
			new BoxView { Color = Color.LightBlue },
			new Rectangle(70, 70, 200, 70)
		);
		absoluteLayout.Children.Add(
			new Label { Text = "Xamarin Forms", FontSize = 20},
			new Rectangle(110, 90, 150, 60)
		);
		absoluteLayout.Children.Add(
			new Label { Text = "Welcome to Xamarin World!", FontSize = 16 },
			new Point(70, 150)
		);
		Content = absoluteLayout;
    }
}

```

В данном случае одна метка накладывается на элемент BoxView, который представляет прямоугольник, заполненный цветом. Таким образом, AbsoluteLayout позволяет нам осуществлять 
перекрытие одних элементов другими.

Для установки позиции в качестве альтернативы мы можем использовать статический метод AbsoluteLayout.SetLayoutBounds(), 
который в качестве параметров принимает элемент и прямоугольную область, выделяемую для этого элемента:

```

public class MainPage : ContentPage
{
    public MainPage()
    {
        BoxView boxView = new BoxView { Color = Color.LightBlue };
		Label headerLbl = new Label { Text = "Xamarin Forms", FontSize = 20 };
		Label contentLbl = new Label { Text = "Welcome to Xamarin World!", FontSize = 16 };

		// определяем позицию и размеры для BoxView
		AbsoluteLayout.SetLayoutBounds(boxView, new Rectangle(70, 70, 200, 70));
		// определяем позицию и размеры для первой метки
		AbsoluteLayout.SetLayoutBounds(headerLbl, new Rectangle(110, 90, 150, 60));
		// определяем позицию и размеры для второй метки
		AbsoluteLayout.SetLayoutBounds(contentLbl, new Rectangle(70, 150, AbsoluteLayout.AutoSize, AbsoluteLayout.AutoSize));
		
		AbsoluteLayout absoluteLayout = new AbsoluteLayout()
		{
			Children = { boxView, headerLbl, contentLbl }
		};
		
        Content = absoluteLayout;
    }
}

```

Для задания автоматических ширины и длины в данном случае мы можем использовать значение AbsoluteLayout.AutoSize. Поэтому для последней метки 
устанавливается только точка верхнего левого угла занимаемой области, а высота и ширина этой области расчитываются автоматически исходя из ширины и высоты элемента.

Для создания абсолютного позиционирования в XAML у элемента устанавливается свойство AbsoluteLayout.LayoutBounds, 
которое фактически представляет прямоугольную область:

```

    
        
        
        
    

```

В случае со второй меткой нам неизвестная точная ширина и длина, поэтому вместо конкретных размеров мы можем использвать автоматические 
размеры в виде значения `AutoSize`.

### Флаг AbsoluteLayoutFlags. Пропорциональные значения

Часто бывает сложно подобрать точные размеры для элементов. И в этом случае мы можем установить пропорциональные размеры. Для этого используется 
перечисление AbsoluteLayoutFlags, которое может принимать следующие значения:

- `None`: все значения интерпретируются как абсолютные

- `All`: все значения интерпретируются как пропорциональные

- `WidthProportional`: пропорциональной считается только ширина прямоугольной области элемента, а все остальные значения рассматриваются как абсолютные

- `HeightProportional`: пропорциональной считается только высота прямоугольной обласи элемента, а все остальные значения рассматриваются как абсолютные

- `XProportional`: пропорциональной считается только координата X элемента, а все остальные значения рассматриваются как абсолютные

- `YProportional`: пропорциональной считается только координата Y элемента, а все остальные значения рассматриваются как абсолютные

- `PositionProportional`: пропорциональными считаются только координаты X и Y позиции элемента

- `SizeProportional`: пропорциональными считаются только ширина и высота прямоугольной области элемента

При использовании пропорциональных значений все эти значения рассчитываются в диапазоне от 0.0 до 1.0. Например, если мы хотим, чтобы элемент занимал половину ширины 
контейнера и четверть высоты, то для ширины нужно установить значение 0.5, а для высоты - 0.25.

Таким образом, ширина элемента будет вычисляться по следющей формуле:

```
ширина_элемента = пропорциональная_ширина_элемента * ширина_контейнера
```

Аналогично с координатами. Например, координата X будет вычисляться по следующей формуле:

```
координатаХ_элемента = (ширина_контейнера - ширина_элемента) * пропорциональное_значениеХ_элемента
```

Например, пусть контейнер AbsoluteLayout имеет ширину в 400 единиц, и пусть вложенный элемент имеет ширину в 100 единиц и пропорциональное значение 
координаты X равное 0.2. Тогда реальная позиция координаты Х будет равна (400-100) * 0.2 = 60 пикселей от левого края контейнера AbsoluteLayout.

Для установки нужного флага для определенного элемента используется статический метод AbsoluteLayout.SetLayoutFlags().

```

public class MainPage : ContentPage
{
    public MainPage()
    {
        AbsoluteLayout absoluteLayout = new AbsoluteLayout();

        BoxView redBox = new BoxView { BackgroundColor = Color.Red };
        BoxView greenBox = new BoxView { BackgroundColor = Color.Green };
        BoxView blueBox = new BoxView { BackgroundColor = Color.Blue };
            
        AbsoluteLayout.SetLayoutBounds(redBox, new Rectangle(0.1, 0.2, 50, 80));
        // устанавливаем пропорциональные координаты
        AbsoluteLayout.SetLayoutFlags(redBox, AbsoluteLayoutFlags.PositionProportional);

        AbsoluteLayout.SetLayoutBounds(greenBox, new Rectangle(1, 0.2, 50, 80));
        AbsoluteLayout.SetLayoutFlags(greenBox, AbsoluteLayoutFlags.PositionProportional);

        AbsoluteLayout.SetLayoutBounds(blueBox, new Rectangle(0.4, 0.8, 0.2, 0.2));
        // пропорциональные координаты и размеры
        AbsoluteLayout.SetLayoutFlags(blueBox, AbsoluteLayoutFlags.All);

        absoluteLayout.Children.Add(redBox);
        absoluteLayout.Children.Add(greenBox);
        absoluteLayout.Children.Add(blueBox);

        Content = absoluteLayout;
    }
}

```

Аналогичный код в XAML будет выглядеть следующим образом:

```

  
    
    
    
   

```

---

**Источник:** [https://metanit.com/sharp/xamarin/3.4.php](https://metanit.com/sharp/xamarin/3.4.php)

[[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 3. Контейнеры компоновки/StackLayout и ScrollView|Назад]] | [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 3. Контейнеры компоновки|Содержание]] | [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 3. Контейнеры компоновки/RelativeLayout|Вперёд]]
