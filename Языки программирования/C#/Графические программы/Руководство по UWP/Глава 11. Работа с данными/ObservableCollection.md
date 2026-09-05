# ObservableCollection

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Графические программы|Графические программы]] / [[Языки программирования/C#/Графические программы/Руководство по UWP|Руководство по UWP]] / [[Языки программирования/C#/Графические программы/Руководство по UWP/Глава 11. Работа с данными|Глава 11. Работа с данными]] / ObservableCollection

[[Языки программирования/C#/Графические программы/Руководство по UWP/Глава 11. Работа с данными/ItemTemplate и DataTemplate|Назад]] | [[Языки программирования/C#/Графические программы/Руководство по UWP/Глава 11. Работа с данными|Содержание]] | [[Языки программирования/C#/Графические программы/Руководство по UWP/Глава 11. Работа с данными/Адаптивные триггеры и шаблоны данных|Вперёд]]

**Дата написания:** 05.09.2026

ObservableCollectionПоследнее обновление: 14.04.2017
 
 
 

 
- 
 
- 
 
- 
 
 

 
 

 
 
 
 
 

 

Как правило, привязка в элементах управления данными осуществляется не к стандартным спискам, а к объектам класса ObservableCollection. 
Почему используется именно этот класс, а не список типа List? Потому что ObservableCollection уже реализует интерфейс INotifyPropertyChanged и поэтому 
может уведомлять элементы, которые применяют привязку, в результате чего обновляется не только сам объект ObservableCollection, но и привязанные к нему элементы интерфейса.

К примеру, возьмем проект из прошлой темы и изменим xaml-код страницы MainPage:

```

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

```

Здесь также идет привязка к свойству Phones, которое представляет коллекцию объектов Phone.

Кроме того, во второй строке грида определена форма для добавления данных.

Теперь изменим код в файле MainPage.xaml.cs следующим образом:

```
using System;
using System.Collections.ObjectModel;
using Windows.UI.Xaml.Controls;

namespace DataApp
{
 public sealed partial class MainPage : Page
 {
 public ObservableCollection Phones { get; set; }

 public MainPage()
 {
 this.InitializeComponent();

 Phones = new ObservableCollection
 {
 new Phone {Id=1, Title="iPhone 6S", Company="Apple" },
 new Phone {Id=2, Title="Lumia 950", Company="Microsoft" },
 new Phone {Id=3, Title="Nexus 5X", Company="Google" },
 };
 }
 private async void phonesList_SelectionChanged(object sender, SelectionChangedEventArgs e)
 {
 Phone selectedPhone = (Phone)phonesList.SelectedItem;
 await new Windows.UI.Popups.MessageDialog($"Выбран {selectedPhone.Title}").ShowAsync();
 }
 // обработчик кнопки
 private void Button_Click(object sender, Windows.UI.Xaml.RoutedEventArgs e)
 {
 string title = titleTextBox.Text;
 string company = companyTextBox.Text;
 // добавление нового объекта
 Phones.Add(new Phone { Title = title, Company = company, Id = Phones.Count + 1 });
 companyTextBox.Text= titleTextBox.Text = String.Empty;
 }
 }
}
```

Теперь свойство Phones представляет объект ObservableCollection. Поэтому при добавлении данных новый элемент автоматически будет отображен в списке:
![Добавление в ObservableCollection](pics/11.2.png)
![ObservableCollection в UWP](pics/11.3.png)

В случае, если бы мы использовали класс List, у нас бы не происходило обновление пользовательского интерфейса при добавлении объекта.

---

**Источник:** [https://metanit.com/sharp/uwp/11.2.php](https://metanit.com/sharp/uwp/11.2.php)
