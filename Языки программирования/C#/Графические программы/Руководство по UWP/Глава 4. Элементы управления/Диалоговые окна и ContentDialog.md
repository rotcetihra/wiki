# Диалоговые окна и ContentDialog

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Графические программы|Графические программы]] / [[Языки программирования/C#/Графические программы/Руководство по UWP|Руководство по UWP]] / [[Языки программирования/C#/Графические программы/Руководство по UWP/Глава 4. Элементы управления|Глава 4. Элементы управления]] / Диалоговые окна и ContentDialog

[[Языки программирования/C#/Графические программы/Руководство по UWP/Глава 4. Элементы управления/ScrollViewer|Назад]] | [[Языки программирования/C#/Графические программы/Руководство по UWP/Глава 4. Элементы управления|Содержание]] | [[Языки программирования/C#/Графические программы/Руководство по UWP/Глава 5. Привязка/Введение в привязку данных|Вперёд]]

**Дата написания:** 05.09.2026

ContentDialogПоследнее обновление: 13.04.2017
 
 
 

 
- 
 
- 
 
- 
 
 

 
 

 
 
 
 
 

 

Класс ContentDialog используется для создания диалоговых окон. Диалоговое окно можно создать в виде кода или разметки.

Например, определим на странице текстовое поле и кнопку:

```

 
 
 
 

```

В файле кода пропишем для кнопки обработчик Button_Click:

```
using System;
using Windows.UI.Xaml;
using Windows.UI.Xaml.Controls;

namespace ControlsApp
{
 public sealed partial class MainPage : Page
 {
 public MainPage()
 {
 this.InitializeComponent();
 }

 private async void Button_Click(object sender, RoutedEventArgs e)
 {
 ContentDialog deleteFileDialog = new ContentDialog()
 {
 Title = "Подтверждение действия",
 Content = "Вы действительно хотите удалить файл?",
 PrimaryButtonText = "ОК",
 SecondaryButtonText = "Отмена"
 };

 ContentDialogResult result = await deleteFileDialog.ShowAsync();
 
 if (result == ContentDialogResult.Primary)
 {
 header.Text = "Файл удален"; 
 }
 else if (result == ContentDialogResult.Secondary)
 {
 header.Text = "Отмена действия";
 }
 }
 }
}
```

Для диалогового окна можно задать ряд свойств. Прежде всего, свойство Title устанавливает заголовок окна, 
а свойство Content - его текст. Свойство PrimaryButtonText определяет текст на первой кнопке, 
а SecondaryButtonText - на второй.

Для отображения диалогового окна надо вызвать асинхонный метод ShowAsync(). Его результатом является объект 
ContentDialogResult, из которого мы можем узнать какую кнопку нажал пользователь. Если результат равен `ContentDialogResult.Primary`, 
то нажата первая кнопка.

Запустим приложение и нажмем на кнопку:
![Модальное окно ContentDialog в UWP](pics/4.60.png)

При этом диалоговое окно будет модальным и будет занимать всю страницу. И пока мы не нажмем на определенную кнопку, работать с приложением мы не сможем.

---

**Источник:** [https://metanit.com/sharp/uwp/4.22.php](https://metanit.com/sharp/uwp/4.22.php)
