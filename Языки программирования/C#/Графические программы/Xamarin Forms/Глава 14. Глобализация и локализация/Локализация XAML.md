[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Графические программы|Графические программы]] / [[Языки программирования/C#/Графические программы/Xamarin Forms|Xamarin Forms]] / [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 14. Глобализация и локализация|Глава 14. Глобализация и локализация]] / Локализация XAML

[[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 14. Глобализация и локализация/Определение языковой культуры|Назад]] | [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 14. Глобализация и локализация|Содержание]]

**Дата написания:** 05.09.2026

Последнее обновление: 14.01.2021
	
	
	
	- 

	- 

	- 

	
	
	
	

	
		
		
		
	

	
В прошлых темах мы рассмотрели локализацию в коде C#, но гораздо проще было бы локализовать элементы интерфейса сразу же в xaml. Для этого возьмем проект из прошлой темы.

Чтобы добавить в приложение возможность локализации элементов xaml, надо добавить класс расширения разметки. Итак, добавим в главный проект следующий 
класс:

```

using System;
using Xamarin.Forms;
using Xamarin.Forms.Xaml;
using System.Resources;
using System.Globalization;
using System.Reflection;

namespace HelloApp
{
    [ContentProperty("Text")]
    public class TranslateExtension : IMarkupExtension
    {
        readonly CultureInfo ci;
        const string ResourceId = "HelloApp.Resource";

        public TranslateExtension()
        {
            ci = DependencyService.Get().GetCurrentCultureInfo();
        }

        public string Text { get; set; }

        public object ProvideValue(IServiceProvider serviceProvider)
        {
            if (Text == null)
                return "";

            ResourceManager resmgr = new ResourceManager(ResourceId, 
						typeof(TranslateExtension).GetTypeInfo().Assembly);

            var translation = resmgr.GetString(Text, ci);

            if (translation == null)
            {
                translation = Text; 
            }
            return translation;
        }
    }
}

```

В строке `const string ResourceId = "HelloApp.Resource";` устанавливаются ресурсы для локализации. Так как у меня пространство имен проекта 
называется `HelloApp`, а файл ресурсов по умолчанию размещен в корне проекта и называется `Resource.resx`, 
то полное имя ресурса будет `HelloApp.Resource`.

Для извлечения ресурсов используется класс `ResourceManager` и его метод `GetString()`

Теперь применим данный класс в xaml:

```

  
    
	
    
    
  

```

Чтобы получить доступ к классу, надо подключить текущее пространство имен проекта: `xmlns:local="clr-namespace:HelloApp;assembly=HelloApp"`

Затем мы можем использовать привязку у тех свойствам элементов, которые надо локализовать: `Text="{local:Translate Header}"`. В данном случае 
local ссылается на текущее пространство имен, "Translate" ссылается на класс `TranslateExtension` - по умолчанию суффикс Extension отбрасывается. 
И затем указывается называется имя ресурса, к которому идет привязка.

В итоге мы можем убрать локализацию из класса приложения App, которая была определена в прошлых темеах, теперь он будет просто создавать стартовую страницу:

```

public partial class App : Application
{
    public App()
    {
		InitializeComponent();
		
        MainPage = new MainPage();
    }
}

```

---

**Источник:** [https://metanit.com/sharp/xamarin/8.3.php](https://metanit.com/sharp/xamarin/8.3.php)

[[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 14. Глобализация и локализация/Определение языковой культуры|Назад]] | [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 14. Глобализация и локализация|Содержание]]
