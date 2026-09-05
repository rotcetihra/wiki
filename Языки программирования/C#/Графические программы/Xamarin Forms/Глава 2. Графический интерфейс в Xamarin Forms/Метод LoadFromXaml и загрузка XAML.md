[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Графические программы|Графические программы]] / [[Языки программирования/C#/Графические программы/Xamarin Forms|Xamarin Forms]] / [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 2. Графический интерфейс в Xamarin Forms|Глава 2. Графический интерфейс в Xamarin Forms]] / Метод LoadFromXaml и загрузка XAML

[[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 2. Графический интерфейс в Xamarin Forms/Взаимодействие XAML и C#|Назад]] | [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 2. Графический интерфейс в Xamarin Forms|Содержание]] | [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 2. Графический интерфейс в Xamarin Forms/Расширения разметки XAML|Вперёд]]

**Дата написания:** 05.09.2026

Последнее обновление: 08.01.2021
	
	
	
	- 

	- 

	- 

	
	
	
	

	
		
		
		
	

	
В прошлых темах были рассмотренны генерируемые по умолчанию при создании проекта файлы MainPage.xaml и MainPage.xaml.cs. Если файл MainPage.xaml 
содержит визуальный интерфейс, то MainPage.xaml.cs предазначен преимущественно для организации программной логики страницы. Но каким образом происходит 
загрузка XAML?

По умолчанию файл MainPage.xaml.cs содержит следующее определение класса MainPage:

```

public partial class MainPage : ContentPage
{
	public MainPage()
	{
		InitializeComponent();
	}
}

```

По сути, все, что делает класс - это вызов метода InitializeComponent(), благодаря которому страница получает определенный в связанном 
xaml-файле графический интерфейс.

При построении проекта Visual Studio парсит файлы с кодом XAML и генерирует файл, название которого заканчивается на 
.g.cs (например, MainPage.xaml.g.cs, его можно найи в папке проекта в подкаталоге 
obj\Debug\netstandard2.0). То есть генерируется обычный класс C#, который содержит определение метода InitializeComponent():

```

[assembly: global::Xamarin.Forms.Xaml.XamlResourceIdAttribute("HelloApp.MainPage.xaml", "MainPage.xaml", typeof(global::HelloApp.MainPage))]

namespace HelloApp {
    
    [global::Xamarin.Forms.Xaml.XamlFilePathAttribute("MainPage.xaml")]
    public partial class MainPage : global::Xamarin.Forms.ContentPage {
        
        [global::System.CodeDom.Compiler.GeneratedCodeAttribute("Xamarin.Forms.Build.Tasks.XamlG", "2.0.0.0")]
        private void InitializeComponent() {
            global::Xamarin.Forms.Xaml.Extensions.LoadFromXaml(this, typeof(MainPage));
        }
    }
}

```

Мы видим, что метод `InitializeComponent()` вызывает другой метод - LoadFromXaml(). 
Этот метод извлекает файл XAML (или его скомпилированную бинарную версию) из файла dll, в который скомпилировано приложение.

После извлечения кода графического интерфейса метод инициализирует все объекты, определенные в файле XAML, устанавливает структуру элементов (какой элемент какие элементы содержит), 
прикрепляет обработчики событий, определенные в файле кода C#, и создает дерево объектов. Таким образом, код из XAML используется для построения интерфейса.

### Динамическая загрузка XAML

Однако мы сами можем загружать код XAML, причем динамически в процессе выполнения программы, используя тот же самый метод LoadFromXaml(). 
Подобный способ может применяться, например, при получении кода XAML от веб-сервиса или, когда в зависимости от хода программы необходимо предоставить альтернативные 
версии интерфейса. Но вместе с тем стоит отметить, что динамическая загрузка XAML снижает производительность приложения, поэтому по возможности ее следует избегать.

Например, динамически загрузим интерфейс для всей страницы:

```

using Xamarin.Forms;
using Xamarin.Forms.Xaml;

namespace HelloApp
{
    public partial class MainPage : ContentPage
    {
        public MainPage()
        {
            string pageXAML = "\r\n" +
                "\n" +
                "" +
                "";

            this.LoadFromXaml(pageXAML);
        }
    }
}

```

Метод LoadFromXaml() является методом расширения, определенным для всех визуальных элементов управления в пространстве имен 
Xamarin.Forms.Xaml. После загрузки страницы она будет выглядеть следующим образом:

Может возникнуть необходимость, обращаться к элементам подобного интерфейса в коде C#. Для нахождения элементов по имени можно применять метод 
FindByName(). Например, изменим тест метки:

```

using Xamarin.Forms;
using Xamarin.Forms.Xaml;

namespace HelloApp
{
    public partial class MainPage : ContentPage
    {
        public MainPage()
        {
            string pageXAML = "\r\n" +
                "\n" +
                "" +
                "";

            this.LoadFromXaml(pageXAML);
            Label lbl = this.FindByName("lbl");
            lbl.Text = "Changed";
        }
    }
}

```

Метод `FindByName()` типизированный - он типизируется типом элемента, который надо найти. Например, в даном случае мы ищем элемент Label с именем 
lbl. Соответственно метод `FindByName()` тизируется типом Label, а в качестве параметра в него предается строка lbl.

Загружать XAML мы можем не только для страницы в целом, но и для отдельных элементов. Например, определим в MainPage.xaml следующую разметку:

```

    
        
        
    

```

Здесь определены метка и кнопка. У кнопки задан обработчик события нажатия.

Теперь изменим файл MainPage.xaml.cs:

```

using Xamarin.Forms;
using Xamarin.Forms.Xaml;

namespace HelloApp
{
    public partial class MainPage : ContentPage
    {
        public MainPage()
        {
            InitializeComponent();
        }

        private void Button_Clicked(object sender, System.EventArgs e)
        {
            string xaml = "";
            lbl.LoadFromXaml(xaml);
        }
    }
}

```

В обработчике нажатия кнопки здесь изменяется разметка элемента Label.

---

**Источник:** [https://metanit.com/sharp/xamarin/2.12.php](https://metanit.com/sharp/xamarin/2.12.php)

[[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 2. Графический интерфейс в Xamarin Forms/Взаимодействие XAML и C#|Назад]] | [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 2. Графический интерфейс в Xamarin Forms|Содержание]] | [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 2. Графический интерфейс в Xamarin Forms/Расширения разметки XAML|Вперёд]]
