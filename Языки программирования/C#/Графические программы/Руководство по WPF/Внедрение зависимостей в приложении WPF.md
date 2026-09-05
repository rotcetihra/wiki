# Внедрение зависимостей в приложении WPF

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Графические программы|Графические программы]] / [[Языки программирования/C#/Графические программы/Руководство по WPF|Руководство по WPF]] / [[Языки программирования/C#/Графические программы/Руководство по WPF/Глава 22. Хостирование приложения и внедрение зависимостей|Глава 22. Хостирование приложения и внедрение зависимостей]] / Внедрение зависимостей в приложении WPF

[[Языки программирования/C#/Графические программы/Руководство по WPF/Глава 21. Взаимодействие с базой данных/MVVM и SQLite|Назад]] | [[Языки программирования/C#/Графические программы/Руководство по WPF/Глава 22. Хостирование приложения и внедрение зависимостей|Содержание]]

**Дата написания:** 05.09.2026

## Внедрение зависимостей в приложении WPF
Последнее обновление: 08.12.2022





-

-

-














Хостинг приложения WPF представляет его развертывание в рамках некоторого хоста. Грубо говоря, хост представляет контейнер, который позволяет управлять, настраивать и 
запускать приложение. В рамках платформы .NET хост представлен классом Microsoft.Extensions.Hosting.Host, который позволяет воспользоваться некоторыми интересными возможностями, как, например, 
внедрение зависимостей


Итак, возьмем новый стандартный проект WPF. По умолчанию он имеет класс App, который представляет приложение, связанный с ним файл App.xaml, а также код главного окна 
MainWindow в файлах MainWindow.xaml и MainWindow.xaml.cs.



Стандартная модель приложения выглядит следующим образом - запускается приложение - 
класс App, а он запускает класс окна MainWindow. Теперь изменим эту модель, добавив хостирование приложения. Для этого вначала добавим через пакетный менеджер nuget 
пакет Microsoft.Extensions.Hosting. Затем добавим в проект новый класс, который назовем Program и в котором определим 
следующий код:


```

using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.DependencyInjection;
using System;

public class Program
{
 [STAThread]
 public static void Main()
 {
 // создаем хост приложения
 var host = Host.CreateDefaultBuilder()
 // внедряем сервисы
 .ConfigureServices(services =>
 {
 services.AddSingleton();
 services.AddSingleton();
 })
 .Build();
 // получаем сервис - объект класса App
 var app = host.Services.GetService();
 // запускаем приложения
 app?.Run();
 }
 }

```


Теперь мы делегируем создание приложения WPF классу Host. Для создания хоста необходим класс-строитель, который реализует интерфейс IHostBuilder и 
который возвращается методом `Host.CreateDefaultBuilder()`. По умолчанию этот метод возвращает встроенную реализацию в виде класса HostBuilder.


```
IHostBuilder hostBuilder = Host.CreateDefaultBuilder();
```


Далее у HostBuilder для настройки сервисов приложения вызывается метод `ConfigureServices()`:


```

.ConfigureServices(services =>
{
 services.AddSingleton();
 services.AddSingleton();
});

```


Метод ConfigureServices принимает делегат, параметр которого представляет объект IServiceCollection - коллекцию сервисов. Благодаря добавления сервисов в эту коллекцию мы можем затем получить 
добавленные сервисы в любом месте приложения.


Для добавления сервисов применяется метод `services.AddSingleton()`, который добавляет сервис в виде синглтона. Метод типизируется типом добавляемого сервиса. 
То есть в данном случае мы добавляем сервисы App и MainWindow. Это значит, что приложение будет создавать объекты-синглтоны App и MainWindow при обращении к ним. И при каждом получении 
объектов этих классов мы по сути будем получать один и тот же объект. Что впрочем логично, поскольку объект приложения App должен существовать в единственном виде. Обычно то же самое касается и 
главного окна приложения.


Затем создаем хост - объект IHost с помощью метода `Build()` объекта IHostBuilder


Далее получаем из коллекции сервисов объект App:


```
var app = host.Services.GetService();
```


И с помощью метода `Run()` запускаем приложение:


```
app?.Run();
```









### Настройка класса App


Теперь настроем класс App. Прежде всего удалим файлы App.xaml и App.xaml.cs и 
добавим в проект новый класс App со следующим содержанием:


```

using System.Windows;

public class App : Application
{
 readonly MainWindow mainWindow;

 // через систему внедрения зависимостей получаем объект главного окна
 public App(MainWindow mainWindow)
 {
 this.mainWindow = mainWindow;
 }
 protected override void OnStartup(StartupEventArgs e)
 {
 mainWindow.Show(); // отображаем главное окно на экране
 base.OnStartup(e);
 }
}

```



Поскольку мы добавили класс главного окна MainWindow в сервисы приложения, то мы можем получить этот сервис в любом месте приложения в том числе через параметр конструктора - в данном случае 
конструктора класса App. Здесь сохраняем объект MainWindow в переменную и в методе OnStartup, который запускается при старте приложения, с помощью метода `mainWindow.Show()` 
отображаем окно на экране.


И если мы запустим приложение, то отобразится главное окно:



### Создание и внедрение сервисов


Подобным образом мы можем внедрять в приложение WPF и другие сервисы. Рассмотрим на примере. Определим в файле Program.cs следующий код:


```

using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.DependencyInjection;
using System;
public class Program
{
 [STAThread]
 public static void Main()
 {
 var host = Host.CreateDefaultBuilder()
 .ConfigureServices(services =>
 {
 services.AddSingleton();
 services.AddSingleton();
 // добавляем сервис IDateService
 services.AddTransient();
 })
 .Build();
 var app = host.Services.GetService();
 app?.Run();
 }
}
public interface IDateService
{
 string FormatedDate { get; }
}
public class RuDateService : IDateService
{
 public string FormatedDate => $"Сегодня: {DateTime.Now.ToString("dd.MM.yyyy")}";
}
public class EnDateService : IDateService
{
 public string FormatedDate => $"Today: {DateTime.Now.ToString("MM.dd.yyyy")}";
}

```


Для теста здесь определен сервим-интерфейс IDateService, в котором свойство `FormatedDate` будет возвращать отформатированную текущую дату.


Также определены две реализации этого интерфейса. Одна реализация - класс RuDateService через свойство FormatedDate возвращает дату на русском языке, а вторая реализация 
EnDateService возвращает дату на английском языке.


С помощью метода AddTransient сервис IDateService внедряется в приложение, причем при обращении к этому сервису будет использоваться реализация RuDateService:


```
services.AddTransient();
```


Поскольку мы внедрели сервис в приложение, то мы можем его получить через параметр конструктора любого определенного нами класса в приложении. Например, подлучим его 
в классе окна приложения. Для этого изменим класс MainWindow в файле MainWindow.xaml.cs:


```

public partial class MainWindow : Window
{
 IDateService dateService;
 
 public MainWindow(IDateService dateService)
 {
 this.dateService = dateService;
 InitializeComponent();
 }
 private void Button_Click(object sender, RoutedEventArgs e)
 {
 MessageBox.Show(dateService.FormatedDate);
 }
}

```


Здесь мы получаем в конструкторе сервис IDateService. Причем мы точно не знаем, какая именно реализация будет использоваться для этого сервиса. Затем в методе Button_Click, 
который будет обработчиком кнопки, отображаем окно с датой из сервиса.


И в конце добавим в код xaml в файле MainWindow.xaml код кнопки, по нажатию на которую будет вызываться вышеопределенный метод Button_Click:


```

```


Запустим приложение и нажмем на кнопку:









 <div

**Источник:** [https://metanit.com/sharp/wpf/23.1.php](https://metanit.com/sharp/wpf/23.1.php)
