[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Графические программы|Графические программы]] / [[Языки программирования/C#/Графические программы/Xamarin Forms|Xamarin Forms]] / [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 22. Flyout|Глава 22. Flyout]] / FlyoutItem

[[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 22. Flyout/Первое приложение с Shell|Назад]] | [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 22. Flyout|Содержание]]

**Дата написания:** 05.09.2026

Последнее обновление: 12.01.2021
	
	
	
	- 

	- 

	- 

	
	
	
	

	
		
		
		
	

	
Объект FlyoutItem представляет группу объектов, для каждой из которых создается пункт в левом меню. Shell может содержать множество FlyoutItem. 
Например, FlyoutItem в xaml:

```

    
        
            
                
            
        
    
    
        
            
                
            
        
    
    
        
            
                
            
        
    

```

Каждый объект FlyoutItem будет представлен в левом меню соответствующим элементом. В качестве текста элемента используется значения 
свойства Text у FlyoutItem. Соответственно в данном случае создается меню из трех пунктов:

Аналогичное создание FlyoutItem в коде C#:

```

using Xamarin.Forms;

namespace FlyoutApp
{
    public partial class MainPage : Shell
    {
        public MainPage()
        {
            Items.Add(new FlyoutItem
            {
                Title = "Европа",
                Items =
                {
                    new Tab
                    {
                        Items = { new ShellContent {Content = new ContentPage()} }
                    }
                }
            });
            Items.Add(new FlyoutItem
            {
                Title = "Азия",
                Items =
                {
                    new Tab
                    {
                        Items = { new ShellContent {Content = new ContentPage()} }
                    }
                }
            });
            Items.Add(new FlyoutItem
            {
                Title = "Африка",
                Items =
                {
                    new Tab
                    {
                        Items = { new ShellContent {Content = new ContentPage()} }
                    }
                }
            });
        }
    }
}

```

Основные свойства FlyoutItem:

- FlyoutDisplayOptions: представляет перечисление FlyoutDisplayOptions и определяет как отображается элемент и его содержимое

- CurrentItem: представляет текущую выбранную вкладку в виде объекта типа Tab

- Items: коллекция вкладок в виде типа IList<Tab>

- FlyoutIcon: иконка, которая отображается в меню, представляет тип ImageSource

- IsChecked: представляет тип bool и определяет, выбран ли данный FlyoutItem в меню

- IsEnabled: представляет тип bool и определяет, доступен ли для выбора в меню данный 
FlyoutItem

- IsTabStop: представляет тип bool и определяет, доступен ли данный FlyoutItem для навигации. Если имеет значение 
`false`, то исключается из меню

- TabIndex: представляет тип int и определяет порядковый номер FlyoutItem в меню. По умолчанию все элементы FlyoutItem располагаются 
в порядке их добавления в Shell

- Title: заголовок, который отображается в меню и представляет данный FlyoutItem

- Route: представляет адрес в виде строки, по которому осуществляется переход

### Настройка внешнего вида

СвойствоFlyoutDisplayOptions отвечает за настройку внешнего вида. В качестве значения оно принимает одну из констант перечисления 
FlyoutDisplayOptions:

- `AsSingleItem`: значение по умолчанию - все объекты Tab в FlyoutItem в меню представлены одним элементом

- `AsMultipleItems`: для каждого объекта Tab в меню создается свой элемент

Применим AsMultipleItems:

```

    
        
            
                
            
        
        
            
                
            
        
    
    
        
            
                
            
        
        
            
                
            
        
    

```

### Установка иконки

За иконку в меню отвечает свойство FlyoutIcon. Например, добавим в проект для Android в папку Resources/drawable пару иконок - небольших изображений, 
например, в формате png. В проекте для iOS файлы изображений помещаются в папку Resources.

И используем изображения для объектов FlyoutItem:

```

    
        
            
                
            
        
        
            
                
            
        
    
    
        
            
                
            
        
    

```

Установка иконки в коде C#:

```

FlyoutItem europe = new FlyoutItem
{
	Title = "Европа",
	FlyoutIcon = ImageSource.FromFile("europa1.png"),  // установка иконки
	Items = 
	{
		//..........................
	}
};

```

### Настройка шаблона отображения

С помощью свойства Shell.ItemTemplate мы, до некоторой степени, можем настроить отображение FlyoutItem в левом меню. Данное свойство 
принимает объект DataTemplate:

```

    
        
            
                
                    
                    
                
                
                
            
        
    
    
        
            
                
            
        
        
            
                
            
        
    
    
        
            
                
            
        
    

```

В данном случае в качестве шаблона для отображения FlyoutItem выбран элемент Grid. В его первом столбце размещен элемент Image, который привязан к FlyoutIcon, 
а во втором столбце - Label, привязанный к свойству Title.

### Установка текущей страницы

По умолчанию при загрузке Shell отображает содержимое самого первого объекта ShellContent. Но мы можем это поведение переопределить, задав свойство CurrentItem у Shell:

```

    
        
            
                
            
        
        
            
                
            
        
    
    
        
            
                
            
        
    

```

Свойство CurrentItem принимает посредством расширения `x:Reference` ссылку на определенный ShellContent.

Теперь по умолчанию будет открываться последний элемент ShellContent.

Установка ShellContent в c#:

```

public partial class MainPage : Shell
{
	public MainPage()
	{
		InitializeComponent();
		CurrentItem = spain;
	}
}

```

---

**Источник:** [https://metanit.com/sharp/xamarin/20.2.php](https://metanit.com/sharp/xamarin/20.2.php)

[[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 22. Flyout/Первое приложение с Shell|Назад]] | [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 22. Flyout|Содержание]]
