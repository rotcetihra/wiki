[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Графические программы|Графические программы]] / [[Языки программирования/C#/Графические программы/Xamarin Forms|Xamarin Forms]] / [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 2. Графический интерфейс в Xamarin Forms|Глава 2. Графический интерфейс в Xamarin Forms]] / Расширения разметки XAML

[[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 2. Графический интерфейс в Xamarin Forms/Метод LoadFromXaml и загрузка XAML|Назад]] | [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 2. Графический интерфейс в Xamarin Forms|Содержание]]

**Дата написания:** 05.09.2026

Последнее обновление: 08.01.2021
	
	
	
	- 

	- 

	- 

	
	
	
	

	
		
		
		
	

	
Расширения разметки (Markup extensions) дают большую гибкость над тем, как устанавливать значения атрибутов в XAML.

Все классы расширений должны реализовать интерфейс IMarkupExtension. Он имеет две версии:

```

public interface IMarkupExtension
{
	object ProvideValue(IServiceProvider serviceProvider);
}
public interface IMarkupExtension : IMarkupExtension
{
    new T ProvideValue(IServiceProvider serviceProvider);
}

```

Метод `ProvideValue()` вызывается во время загрузки кода xaml и возвращает собственно то значение, которое присваивается атрибуту элемента.

В Xamarin Forms есть ряд встроенных расширений:

- x:Static

- x:Type

- x:Array

- x:Null

- x:Reference

- StaticResource

- DynamicResource

- Binding

- ConstraintExpression

Расмотрим некоторые из них. А в последующих темах так или иначе затронем и остальные.

### x:Static

x:Static позволяет привязать к атрибуту значение константы, статической переменной, статического свойства или значения перечисления. 
Например, в коде C# у страницы определим константу или статическую переменную:

```

using Xamarin.Forms;

namespace HelloApp
{
    public partial class MainPage : ContentPage
    {
        public const string HEADER = "Xamarin";

        public static double staticVar = 28;

        public MainPage()
        {
            InitializeComponent();
        }
    }
}

```

Тогда мы сможем использовать их значения следующим образом:

```

    

```

Чтобы ссылаться на типы и их члены, которые определены в текущем проекте в коде C#, нам надо подключить пространство имен текущего проекта:

```
xmlns:local="clr-namespace:HelloApp"
```

В данном случае весь функционал, который определен в коде C# в текущем проекте, будет сопоставляться с префиксом local. После 
параметра clr-namespace указывается пространство имен текущего проекта. Обычно оно совпадает с названием проекта (в моем случае HelloApp). 
После этого в коде XAML мы можем через префикс local ссылаться на типы и их доступные переменные и свойства:

```
Text="{x:Static local:MainPage.HEADER}"
```

### x:Array и x:Type

Расширение разметки x:Array позволяет определить массив данных. А расширение x:Type позволяет указать тип данных. Например, 
воспользуемся элементом ListView для вывода содержимого массива:

```

    
        
            
                iPhone 12 Pro
                Samsung Galaxy S20
                Nokia 9
            
        
    

```

Сложное свойство `ListView.ItemsSource` в качестве значения принимает массив. В данном случае в определении массива атрибут `Type="{x:Type x:String}"` указывает, что массив будет содержать данные типа String.

### Создание расширений XAML

Иногда может возникнуть необходимость создать какое-то свое расширение для XAML. В этом случае нам надо создать класс, который будет реализовать интерфейс 
IMarkupExtension.

К примеру, мы хотим чтобы через XAML можно было установить для фона элемента цвет из четырех компонент - ARGB. В этом случае мы можем создать следующий класс:

```

using System;
using Xamarin.Forms;
using Xamarin.Forms.Xaml;

namespace HelloApp
{
    public class ARGBColor : IMarkupExtension
    {
        public int Alpha { get; set; }
        public int Red { get; set; }
        public int Green { get; set; }
        public int Blue { get; set; }

        public object ProvideValue(IServiceProvider serviceProvider)
        {
            return Color.FromRgba(Red, Green, Blue, Alpha);
        }
    }
}

```

Затем используем этот класс в XAML:

```

    
        
    

```

Свойства `TextColor` и `BackgroundColor` в качестве значения принимают объект Color. И именно подобный объект генерируется 
методом `ProvideValue()` из класса ARGBColor. То есть значение "{local:ARGBColor Alpha=255, Red=0, Green77, Blue=64}" 
по сути будет возвращать должным образом инициализованный объект Color.

В результате мы увидим на странице метку, к которой применены цвета по настройкам ARGB:

---

**Источник:** [https://metanit.com/sharp/xamarin/2.11.php](https://metanit.com/sharp/xamarin/2.11.php)

[[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 2. Графический интерфейс в Xamarin Forms/Метод LoadFromXaml и загрузка XAML|Назад]] | [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 2. Графический интерфейс в Xamarin Forms|Содержание]]
