[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Графические программы|Графические программы]] / [[Языки программирования/C#/Графические программы/Xamarin Forms|Xamarin Forms]] / [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 3. Контейнеры компоновки|Глава 3. Контейнеры компоновки]] / Контейнер Grid

[[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 3. Контейнеры компоновки/RelativeLayout|Назад]] | [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 3. Контейнеры компоновки|Содержание]]

**Дата написания:** 05.09.2026

Последнее обновление: 09.01.2021
	
	
	
	- 

	- 

	- 

	
	
	
	

	
		
		
		
	

	
Контейнер Grid располагает вложенные элементы в виде таблицы:

```

class MainPage : ContentPage
{
    public MainPage()
    {
        Grid grid = new Grid
        {
            RowDefinitions = 
            {
                new RowDefinition { Height = new GridLength(1, GridUnitType.Star) },
                new RowDefinition { Height = new GridLength(1, GridUnitType.Star) },
                new RowDefinition { Height = new GridLength(1, GridUnitType.Star) }
            },
            ColumnDefinitions = 
            {
                new ColumnDefinition { Width = new GridLength(1, GridUnitType.Star) },
                new ColumnDefinition { Width = new GridLength(1, GridUnitType.Star) },
                new ColumnDefinition { Width = new GridLength(1, GridUnitType.Star) }
            }
        };
		grid.Children.Add(new BoxView { Color = Color.Red}, 0, 0);
        grid.Children.Add(new BoxView { Color = Color.Blue }, 0, 1);
        grid.Children.Add(new BoxView { Color = Color.Fuchsia }, 0, 2);

        grid.Children.Add(new BoxView { Color = Color.Teal}, 1, 0);
        grid.Children.Add(new BoxView { Color = Color.Green }, 1, 1);
        grid.Children.Add(new BoxView { Color = Color.Maroon }, 1, 2);

        grid.Children.Add(new BoxView { Color = Color.Olive }, 2, 0);
        grid.Children.Add(new BoxView { Color = Color.Pink }, 2, 1);
        grid.Children.Add(new BoxView { Color = Color.Yellow }, 2, 2);

        Content = grid;
    }
}

```

С помощью свойств `RowDefinitions` и `ColumnDefinitions` грид создает набор строк и столбцов соответственно. Так, 
здесь задается три строки и три столбца, то есть в итоге 9 ячеек.

Для высоты строк и ширины столбцов задается значение `new GridLength(1, GridUnitType.Star)`. Число 1 указывает на то, что 
данный столбец или строка будет занимать одну долю от всего пространства (так как все три строки или столбца имеют значение 1, то все пространство 
условно будет равно 1+1+1=3, а одна строка или столбец будет занимать 1/3). А параметр `GridUnitType.Star` как раз указывает, что размеры будут 
вычисляться пропорционально.

Чтобы добавить элемент в определенную ячейку, мы указываем номер строки и столбца: `grid.Children.Add(new BoxView { Color = Color.Blue }, 0, 1);` - 
элемент BoxView добавляется в ячейку таблицы, которая находится на пересечении первого столбца и второй строки (исчисление начинается с 0, 
поэтому 1 будет представлять второй столбец или строку)

Употребление Grid в xaml:

```

    
        
            
            
            
        
        
            
            
            
        
        
        
        

        
        
        

        
        
        
    

```

Использование звездочки в xaml аналогично параметру `GridUnitType.Star`. Но кроме пропорциональных размеров мы можем задать 
автоматические размеры или абсолютные размеры, например:

```

  
    
    
    
  
  
    
    
  

```

Аналогичное определение разных типов размеров в коде C#:

```

Grid grid = new Grid
{
    RowDefinitions =
    {
        new RowDefinition { Height = new GridLength(2, GridUnitType.Star) },
        new RowDefinition { Height = new GridLength(1, GridUnitType.Star) },
        new RowDefinition { Height = 200 }
    },
    ColumnDefinitions =
    {
        new ColumnDefinition { Width = GridLength.Auto },
        new ColumnDefinition { Width = new GridLength(1, GridUnitType.Star) }
    }
};

```

### Отступы

Класс Grid определяет два специальных свойства для создания отступов:

- ColumnSpacing: определяет пространство между столбцами

- RowSpacing: определяет пространство между строками

Например:

```

  
    
    
  

```

Или в коде C#:

```

var grid = new Grid { ColumnSpacing = 5 };
grid.ColumnDefnitions.Add(new ColumnDefinition { Width = new GridLength (1, GridUnitType.Star)});
grid.ColumnDefnitions.Add(new ColumnDefinition { Width = new GridLength (1, GridUnitType.Star)});

```

### Объединение ячеек

С помощью свойства ColumnSpan можно объединить несколько столбцов, а с помощью свойства RowSpan - 
объединить ячейки:

```

public class MainPage : ContentPage
{
    public MainPage()
    {
        Grid grid = new Grid
        {
            RowDefinitions =
            {
                new RowDefinition { Height = new GridLength(1, GridUnitType.Star) },
                new RowDefinition { Height = new GridLength(1, GridUnitType.Star) }
            },
            ColumnDefinitions =
            {
                new ColumnDefinition { Width = new GridLength(1, GridUnitType.Star) },
                new ColumnDefinition { Width = new GridLength(1, GridUnitType.Star) }
            }
        };
        BoxView redBox = new BoxView { Color = Color.Red };
        BoxView blueBox = new BoxView { Color = Color.Blue };
        BoxView yellowBox = new BoxView { Color = Color.Yellow };
        grid.Children.Add(redBox, 0, 0);
        grid.Children.Add(blueBox, 1, 0);
        grid.Children.Add(yellowBox, 0, 1);
        Grid.SetColumnSpan(yellowBox, 2);	// растягиваем на два столбца

        Content = grid;
    }
}

```

Аналог в XAML:

```

  
    
      
      
    
    
      
      
    
    
    
    
   

```

---

**Источник:** [https://metanit.com/sharp/xamarin/3.6.php](https://metanit.com/sharp/xamarin/3.6.php)

[[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 3. Контейнеры компоновки/RelativeLayout|Назад]] | [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 3. Контейнеры компоновки|Содержание]]
