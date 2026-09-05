# Контекст данных и интерфейс INotifyPropertyChanged

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Графические программы|Графические программы]] / [[Языки программирования/C#/Графические программы/Руководство по UWP|Руководство по UWP]] / [[Языки программирования/C#/Графические программы/Руководство по UWP/Глава 5. Привязка|Глава 5. Привязка]] / Контекст данных и интерфейс INotifyPropertyChanged

[[Языки программирования/C#/Графические программы/Руководство по UWP/Глава 5. Привязка/Введение в привязку данных|Назад]] | [[Языки программирования/C#/Графические программы/Руководство по UWP/Глава 5. Привязка|Содержание]] | [[Языки программирования/C#/Графические программы/Руководство по UWP/Глава 5. Привязка/Конвертеры значений|Вперёд]]

**Дата написания:** 05.09.2026

Контекст данных и интерфейс INotifyPropertyChangedПоследнее обновление: 13.04.2017
 
 
 

 
- 
 
- 
 
- 
 
 

 
 

 
 
 
 
 

 
### Свойство DataContext

Одним из способов задания привязки к объекту является использование контекста данных или свойства DataContext. 
С его помощью мы можем задать элементу какой-то общий контекст, а все его вложенные элементы будут привязаны к отдельным свойствам этого контекста. 
Посмотрим на примере с объектом Phone:

```
public class Phone
{
 public string Title { get; set; }
 public string Company { get; set; }
 public int Price { get; set; }
}
```

Свяжем свойства объекта Phone элементами на странице через DataContext:

```

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

```

![DataContext в Universal Windows Platform](pics/6.3.png)

Таким образом мы задаем свойству DataContext некоторый ресурс, и затем осуществляется привязка к этому ресурсу.

Каждый объект класса FrameworkElement, а это практически все стандартные элементы управления, может определять свой собственный контекст данных. Например:

```

 
 
 
 
 
 
 
 
 
 
 
 

```

Здесь определены два элемента StackPanel, каждый из которых использует разные контексты данных: один использует контекст страницы, а другой определяет свой собственный.
![Свойство DataContext в UWP](pics/6.8.png)

Определение контекста в коде C#:

```
using Windows.UI.Xaml.Controls;
namespace BindingApp
{
 public sealed partial class MainPage : Page
 {
 public MainPage()
 {
 this.InitializeComponent();

 this.DataContext = new Phone { Title = "Samsung Galaxy S8", Company = "Samsung", Price = 50000 };
 }
 }
}
```

В этом случае все выражения Binding в XAML автоматически будут привязываться к свойствам этого объекта:

```

 
 
 

```

### Интерфейс INotifyPropertyChanged

В примерах выше привязка осуществлялась к объекту класса Phone. Но использование этого класса имело один минус. Даже если мы изменим значения 
его свойств, то содержимое привязанных текстовых блоков это никак не повлияет. Например, добавим на страницу пару кнопок для изменения состояния объекта Phone:

```

 
 
 
 
 
 
 
 +
 -
 
 

```

А в файле кода C# для этих кнопок определим обработчики Increase и Decrease, в которых будет меняться свойство Price:

```
private void Increase(object sender, Windows.UI.Xaml.RoutedEventArgs e)
{
 Phone phone = this.DataContext as Phone;
 phone.Price += 1000;
}

private void Decrease(object sender, Windows.UI.Xaml.RoutedEventArgs e)
{
 Phone phone = this.DataContext as Phone;
 phone.Price -= 1000;
}
```

В данном случае нажатия на кнопку изменят ресурс, но текстовые блоки, привязанные к этому ресурсу, не изменятся. Чтобы объект мог полноценно 
реализовать механизм привязки, нам надо реализовать в его классе интерфейс INotifyPropertyChanged. И для этого изменим класс Phone следующим образом:

```
using System.ComponentModel;
using System.Runtime.CompilerServices;

namespace BindingApp
{
 public class Phone : INotifyPropertyChanged
 {
 private string title;
 private string company;
 private int price;

 public string Title
 {
 get { return title; }
 set
 {
 if (title != value)
 {
 title = value;
 OnPropertyChanged("Title");
 }
 }
 }
 public string Company
 {
 get { return company; }
 set
 {
 if (company != value)
 {
 company = value;
 OnPropertyChanged("Company");
 }
 }
 }
 public int Price
 {
 get { return price; }
 set
 {
 if (price != value)
 {
 price = value;
 OnPropertyChanged("Price");
 }
 }
 }

 public event PropertyChangedEventHandler PropertyChanged;
 public void OnPropertyChanged([CallerMemberName]string prop = "")
 {
 if (PropertyChanged != null)
 PropertyChanged(this, new PropertyChangedEventArgs(prop));
 }
 }
}
```

Теперь при изменении значения свойства в объекте Phone срабатывает метод OnPropertyChanged, через который данный объект будет извещать систему об изменении через событие PropertyChanged. А система в свою очередь 
обновляет все привязанные объекты, в частности, элементы TextBlock.
![Интерфейс INotifyPropertyChanged в Universal Windows Platform](pics/6.9.png)

---

**Источник:** [https://metanit.com/sharp/uwp/5.2.php](https://metanit.com/sharp/uwp/5.2.php)
