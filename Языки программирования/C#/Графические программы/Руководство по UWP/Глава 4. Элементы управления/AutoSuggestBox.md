# AutoSuggestBox

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Графические программы|Графические программы]] / [[Языки программирования/C#/Графические программы/Руководство по UWP|Руководство по UWP]] / [[Языки программирования/C#/Графические программы/Руководство по UWP/Глава 4. Элементы управления|Глава 4. Элементы управления]] / AutoSuggestBox

[[Языки программирования/C#/Графические программы/Руководство по UWP/Глава 4. Элементы управления/FlipView|Назад]] | [[Языки программирования/C#/Графические программы/Руководство по UWP/Глава 4. Элементы управления|Содержание]] | [[Языки программирования/C#/Графические программы/Руководство по UWP/Глава 4. Элементы управления/CommandBar|Вперёд]]

**Дата написания:** 05.09.2026

AutoSuggestBoxПоследнее обновление: 15.04.2017
 
 
 

 
- 
 
- 
 
- 
 
 

 
 

 
 
 
 
 

 

AutoSuggestBox представляет сложный элемент, который содержит текстовое поле и подключаемый к нему список. 
При вводе в текстовое поле могут автоматически подставляться похожие результаты из некоторого предопределенного списка.

Чтобы задействовать функциональные возможности данного элемента управления, надо обработать его событие TextChanged. 
В обработчике события необходимо лимитировать список предопределенных вариантов таким образом, чтобы они соответствовали введенному в поле тексту.

Итак, определим AutoSuggestBox:

```

```

В файле отделенного кода определим обработчик:

```
using System.Collections.ObjectModel;
using System.Linq;
using Windows.UI.Xaml.Controls;

namespace DataApp
{
 public sealed partial class MainPage : Page
 {
 ObservableCollection phones;
 public MainPage()
 {
 this.InitializeComponent();

 phones = new ObservableCollection { "iPhone 6S", "iPhone 6s Plus", "Nexus 5X", "Nexus 6P", "Lumia 950", "Lumia 550" };
 }

 private void suggestBox_TextChanged(AutoSuggestBox sender, AutoSuggestBoxTextChangedEventArgs args)
 {
 if (args.CheckCurrent())
 {
 var term = suggestBox.Text.ToLower();
 var results = phones.Where(i =>i.ToLower().Contains(term)).ToList();
 suggestBox.ItemsSource = results;
 }
 }
 }
}
```

Итак, здесь определяется список смартфонов - исходных значений для списка. В обработчике `suggestBox_TextChanged` с помощью метода `args.CheckCurrent()` 
проверяем, а были ли изменения в текстовом поле. Если они были, то получаем введенное значение и проверяем, есть ли оно в списке. В конце список отфильтрованных значений 
устанавливается в качестве источника для AutoSuggestBox:
![AutoSuggestBox в UWP](pics/4.33.png)

При этом без обработки события TextChanged список не будет автоматически отфильтровывать результаты. Все надо делать программно.

Если нам надо, чтобы при вводе пользователя ему сразу автоматически открывался список всех возможных результатов, то мы можем в конструкторе сразу указать источник для 
AutoSuggestBox:

```
public MainPage()
{
 this.InitializeComponent();
 phones = new List { "iPhone 6S", "iPhone 6s Plus", "Nexus 5X", "Nexus 6P", "Lumia 950", "Lumia 550" };
 suggestBox.ItemsSource = phones;
}
```

Также стоит выделить события SuggestionChosen и QuerySubmitted. Событие `SuggestionChosen` генерируется, 
когда пользователь выбирает из списка похожих результатов один из них. Данное событие может использоваться для обновления значений, которые связаны с AutoSuggestBox. 
А событие `QuerySubmitted` генерируется, когда пользователь нажимает в AutoSuggestBox на кнопку поиска или на клавишу Enter. то событие используется, 
как правило, для определения, существует ли в списке введенное значение.

Например, добавим текстовый блок и определим обработчики:

```

 
 

```

И изменим файл отделенного кода:

```
using System.Collections.Generic;
using System.Linq;
using Windows.UI.Xaml.Controls;

namespace ControlsApp
{
 public sealed partial class MainPage : Page
 {
 List phones;
 public MainPage()
 {
 this.InitializeComponent();

 phones = new List { "iPhone 6S", "iPhone 6s Plus", "Nexus 5X", "Nexus 6P", "Lumia 950", "Lumia 550" };
 }

 private void suggestBox_QuerySubmitted(AutoSuggestBox sender, AutoSuggestBoxQuerySubmittedEventArgs args)
 {
 var term = args.QueryText.ToLower();
 var results = phones.Where(i => i.ToLower().Contains(term)).ToList();
 suggestBox.ItemsSource = results;
 suggestBox.IsSuggestionListOpen = true;
 }

 private void suggestBox_SuggestionChosen(AutoSuggestBox sender, AutoSuggestBoxSuggestionChosenEventArgs args)
 {
 textBlock1.Text = args.SelectedItem as string;
 }
 }
}
```

В обработчике `suggestBox_QuerySubmitted` делается фактически то же самое, что и при изменении текста: получаем введенное значение с помощью 
`args.QueryText` и фильтруем список. Для раскрытия отфильтрованного списка устанавливаем `suggestBox.IsSuggestionListOpen = true`

В обработчике `suggestBox_SuggestionChosen` просто присваиваем выбранное значение текстовому блоку.
![AutoSuggestBox в Universal Windows Platform](pics/4.34.png)

Из свойств AutoSuggestBox можно отметить следующие:

- 

Header: заголовок

- 

PlaceholderText: временный текст по умолчанию

- 

QueryIcon: иконка кнопки поиска. Может принимать множество значений, но наиболее часто используемое "Find"

---

**Источник:** [https://metanit.com/sharp/uwp/4.19.php](https://metanit.com/sharp/uwp/4.19.php)
