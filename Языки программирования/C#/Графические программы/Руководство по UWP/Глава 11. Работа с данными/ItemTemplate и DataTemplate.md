# ItemTemplate и DataTemplate

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Графические программы|Графические программы]] / [[Языки программирования/C#/Графические программы/Руководство по UWP|Руководство по UWP]] / [[Языки программирования/C#/Графические программы/Руководство по UWP/Глава 11. Работа с данными|Глава 11. Работа с данными]] / ItemTemplate и DataTemplate

[[Языки программирования/C#/Графические программы/Руководство по UWP/Глава 10. Адаптивный дизайн/Адаптивный код C#|Назад]] | [[Языки программирования/C#/Графические программы/Руководство по UWP/Глава 11. Работа с данными|Содержание]] | [[Языки программирования/C#/Графические программы/Руководство по UWP/Глава 11. Работа с данными/ObservableCollection|Вперёд]]

**Дата написания:** 05.09.2026

ItemTemplate и DataTemplateПоследнее обновление: 14.04.2017
 
 
 

 
- 
 
- 
 
- 
 
 

 
 

 
 
 
 
 

 

Элемент ListBox позволяет легко установить привязку к коллекции объектов, однако по умолчанию каждый элемент ListBox отображает строку. 
Если же нам необходимо отобразить более сложные объекты в ListBox, то для этого надо использовать объект DataTemplate.

Ключевым свойством для отображения данных во всех элементах-списках (не только в ListBox) является свойство ItemTemplate. Оно задает шаблон 
данных. В качестве значения этого свойства устанавливается объект DataTemplate - именно этот объект и управляет отображением данных.

В качестве самих данных, которые отображаются в DataTemplate, как правило, выступают объекты пользовательских классов, создаваемых самим разработчиком. Например, 
определим в проекте следующий класс Phone, который будет представлять модель телефона:

```
public class Phone
{
 public int Id { get; set; }
 public string Title { get; set; } // модель телефона
 public string Company { get; set; } // производитель
 public string ImagePath { get; set; } // путь к изображению
}
```

Далее создадим в классе MainPage свойство, которое будет представлять коллекцию смартфонов:

```
using System;
using System.Collections.Generic;
using Windows.UI.Xaml.Controls;

namespace DataApp
{
 public sealed partial class MainPage : Page
 {
 public List Phones { get; set; }

 public MainPage()
 {
 this.InitializeComponent();

 Phones = new List
 {
 new Phone {Id=1, ImagePath="/Assets/iphone6s.jpg", Title="iPhone 7", Company="Apple" },
 new Phone {Id=2, ImagePath="/Assets/mate8.jpg", Title="Huawei P10", Company="Huawei" },
 new Phone {Id=3, ImagePath="/Assets/nexus5x.jpg", Title="Pixel", Company="Google" },
 new Phone {Id=4, ImagePath="/Assets/galaxys6.jpg", Title="Galaxy S8", Company="Samsung"}
 };
 }
 private async void phonesList_SelectionChanged(object sender, SelectionChangedEventArgs e)
 {
 Phone selectedPhone = (Phone)phonesList.SelectedItem;
 await new Windows.UI.Popups.MessageDialog($"Выбран {selectedPhone.Title}").ShowAsync();
 }
 }
}
```

Здесь создается 4 объекта Phone. Для каждого объекта устанавливаются необходимые значения. Причем свойство `ImagePath` указывает на 
путь к изображению в папке Assets. Предполагается, что в папке Assets есть четыре изображения для каждой из моделей.

Теперь изменим разметку MainPage.xaml:

```

 
 
 
 
 
 
 
 
 
 
 
 
 

```

С помощью атрибута `ItemsSource="{x:Bind Phones}"` задаем привязку к свойству Phones из MainPage. А с помощью свойства `ListBox.ItemTemplate` задаем, как этот список Phones будет отображаться.

Элемент DataTemplate устанавливает, как будет отображаться один элемент Phone из списка Phones. Чтобы создать привязку именно к объекту Phone, в 
DataTemplate устанавливается атрибут ` x:DataType="data:Phone"`. То есть префикс `data` указывает на то пространство имен, в 
котором определен класс Phone. После этой установки мы можем задать привязку у вложенных элементов к конкретным свойствам класса Phone:

```

```

А с помощью атрибута `SelectionChanged="phonesList_SelectionChanged"` устанавливается обработчик выделения элементов. Определим в классе MainPage этот обработчик:

```
private async void phonesList_SelectionChanged(object sender, SelectionChangedEventArgs e)
{
 Phone selectedPhone = (Phone)phonesList.SelectedItem;
 await new Windows.UI.Popups.MessageDialog($"Выбран {selectedPhone.Title}").ShowAsync();
}
```

Мы можем получить выделенный элемент через свойство `phonesList.SelectedItem`. И так как DataTemplate отображает объекты Phone, то выделенный элемент 
мы можем привести к типу Phone.

В итоге получится следующее приложение:
![Data Binding и DataTemplate в UWP](pics/11.1.png)

---

**Источник:** [https://metanit.com/sharp/uwp/11.1.php](https://metanit.com/sharp/uwp/11.1.php)
