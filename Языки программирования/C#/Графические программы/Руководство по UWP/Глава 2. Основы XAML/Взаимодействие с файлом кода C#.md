# Взаимодействие с файлом кода C#

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Графические программы|Графические программы]] / [[Языки программирования/C#/Графические программы/Руководство по UWP|Руководство по UWP]] / [[Языки программирования/C#/Графические программы/Руководство по UWP/Глава 2. Основы XAML|Глава 2. Основы XAML]] / Взаимодействие с файлом кода C#

[[Языки программирования/C#/Графические программы/Руководство по UWP/Глава 2. Основы XAML/XAML в Universal Windows Platform|Назад]] | [[Языки программирования/C#/Графические программы/Руководство по UWP/Глава 2. Основы XAML|Содержание]] | [[Языки программирования/C#/Графические программы/Руководство по UWP/Глава 2. Основы XAML/Сложные свойства и конвертеры типов|Вперёд]]

**Дата написания:** 05.09.2026

Взаимодействие с файлом кода C#Последнее обновление: 12.04.2017
 
 
 

 
- 
 
- 
 
- 
 
 

 
 

 
 
 
 
 

 

Файлы XAML позволяют нам определить визуальный интерфейс, но для создания логики, например, для определения обработчиков событий элементов управления, 
все равно придется воспользоваться кодом C#. И вместе с файлом разметки xaml MainPage.xaml Visual Studio по умолчанию также создает файл 
отделенного кода MainPage.xaml.cs, который содержит логику на C#, связанную с файлом MainPage.xaml:

```
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Runtime.InteropServices.WindowsRuntime;
using Windows.Foundation;
using Windows.Foundation.Collections;
using Windows.UI.Xaml;
using Windows.UI.Xaml.Controls;
using Windows.UI.Xaml.Controls.Primitives;
using Windows.UI.Xaml.Data;
using Windows.UI.Xaml.Input;
using Windows.UI.Xaml.Media;
using Windows.UI.Xaml.Navigation;

namespace XamlApp
{
 public sealed partial class MainPage : Page
 {
 public MainPage()
 {
 this.InitializeComponent();
 }
 }
}
```

Во время компиляции этот класс объединяется с классом, сгенерированном из кода XAML. Чтобы такое слияние классов во время компиляции произошло, класс XamlApp.MainPage определяется как частичный с модификатором partial, а в коде XAML 
у элемента Page устанавливается атрибут x:Class, который в качестве значения принимает имя этого класса: `x:Class="XamlApp.MainPage"`. 
Через метод InitializeComponent() класс MainPage вызывает скомпилированный ранее код XAML, разбирает его и по нему строит графический интерфейс.

Нередко в приложении требуется обратиться к какому-нибудь элементу управления, который определен в коде XAML. Для этого надо установить у элемента в 
XAML атрибут `x:Name`.

Другой точкой взаимодействия между xaml и C# являются события. С помощью атрибутов в XAML мы можем указать для событий элеметов обработчики, 
которые определяются в коде C#.

Например, определим в коде XAML кнопку:

```

 
 
 

```

Атрибут `Click` связывает событие нажатия кнопки с обработчиком button_Click. Добавим этот обработчик в код MainPage.xaml.cs:

```
using Windows.UI.Xaml;
using Windows.UI.Xaml.Controls;

namespace XamlApp
{
 public sealed partial class MainPage : Page
 {
 public MainPage()
 {
 this.InitializeComponent();
 }

 private void button_Click(object sender, RoutedEventArgs e)
 {
 messageButton.Content = "Hello UWP!";
 }
 }
}
```

В обработчике получаем по имени кнопку messageButton и через ее свойство `Content` устанавливаем ее текст:
![Связь XAML и C# в Universal Windows Platform](pics/2.2.png)

Еще одной формой взаимодействия определение элементов страницы в коде C#. Например, изменим код xaml следующим образом:

```

 
 

```

Здесь для элемента Grid установлено свойство `x:Name`, через которое мы можем к нему обращаться в коде. И также изменим код C#:

```
using Windows.UI.Xaml;
using Windows.UI.Xaml.Controls;

namespace XamlApp
{
 public sealed partial class MainPage : Page
 {
 public MainPage()
 {
 this.InitializeComponent();
 // определение кнопки и ее свойств
 Button button1 = new Button();
 button1.Content = "Новая кнопка";
 button1.Width = 120;
 button1.Height = 40;
 // добавление кнопки в грид
 layoutGrid.Children.Add(button1);
 }
 }
}
```

В конструкторе странцы создается элемент Button и добавляется в Grid. И если мы запустим приложение, то увидим добавленную кнопку:
![Добавление элементов в XAML в Universal Windows Platform](pics/2.3.png)

В итоге мы можем определять визуальные компоненты как в коде XAML, можем XAML не использовать и делать все в коде C#, либо же мы можем совмещать оба подхода как в примере выше.

### Использование пространств имен из C#

В XAML по умолчанию применяется некоторый набор пространств имен xml, однако мы можем подключать любые другие пространства имен и их функциональность 
в том числе и из C#. Например, по умолчанию в определении страницы Page подключается локальное пространство имен:

```
xmlns:local="using:XamlApp"
```

Локальное пространство имен, как правило, называется по имени проекта (в моем случае проект называется XamlApp) и позволяет подключить все классы, 
которые определены в коде C# в нашем проекте. Например, добавим в проект следующий класс:

```
public class Phone
{
 public string Name { get; set; }
 public int Price { get; set; }
 
 public override string ToString()
 {
 return $"Смартфон {this.Name}; цена: {this.Price}";
 }
}
```

Используем этот класс в коде xaml:

```

 
 
 
 
 
 
 

```

Так как локальное пространство имен сопоставляется с префиксом `local`, то классы проекта используются в форме `local:Название_Класса`. 
В частности, здесь объект Phone устаавливается в качестве содержимого кнопки через свойство `Content`. Для сложных объектов это свойство принимает 
их строковое представление, которое возвращается методом `ToString()`:
![](pics/2.4.png)

---

**Источник:** [https://metanit.com/sharp/uwp/2.2.php](https://metanit.com/sharp/uwp/2.2.php)
