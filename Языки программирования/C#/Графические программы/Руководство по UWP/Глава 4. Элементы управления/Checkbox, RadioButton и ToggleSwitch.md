# Checkbox, RadioButton и ToggleSwitch

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Графические программы|Графические программы]] / [[Языки программирования/C#/Графические программы/Руководство по UWP|Руководство по UWP]] / [[Языки программирования/C#/Графические программы/Руководство по UWP/Глава 4. Элементы управления|Глава 4. Элементы управления]] / Checkbox, RadioButton и ToggleSwitch

[[Языки программирования/C#/Графические программы/Руководство по UWP/Глава 4. Элементы управления/Текстовые поля|Назад]] | [[Языки программирования/C#/Графические программы/Руководство по UWP/Глава 4. Элементы управления|Содержание]] | [[Языки программирования/C#/Графические программы/Руководство по UWP/Глава 4. Элементы управления/Image и работа с изображениями|Вперёд]]

**Дата написания:** 05.09.2026

Checkbox, RadioButton и ToggleSwitchПоследнее обновление: 12.04.2017
 
 
 

 
- 
 
- 
 
- 
 
 

 
 

 
 
 
 
 

 
### CheckBox

Флажок или CheckBox применяется для выбора из двух вариантов по принципу "да-нет", а также когда нам надо выбрать несколько опций из группы опций.

Формально CheckBox может принимать три состояния: `Checked`, `Unchecked` и `Intermediate`. Для установки 
состояния применяется свойство IsChecked:

```

 
 
 

```

![CheckBox in Universal Windows Platform](pics/4.6.png)

Значение свойства `IsChecked="{x:Null}"` устанавливает флажок в неопределенное состояние. Остальные два состояния задаются с помощью значений `true` 
и `false`. Кроме того, чтобы можно было переключаться между всеми тремя состояниями, надо установить свойство `IsThreeState="True"`

С помощью событий Checked (генерируется при установке флажка в отмеченное состояние), Unchecked (генерируется при снятии отметки с флажка) и 
Indeterminate (флажок переведен в неопределенное состояние) мы можем отследить изменение состояния флажка. Например, определим элемент checkBox: 

```

```

И в файле кода c# определим все обработчики:

```
private void checkBox_Checked(object sender, RoutedEventArgs e)
{
 textBlock1.Text = checkBox.Content.ToString() + " отмечен";
}

private void checkBox_Unchecked(object sender, RoutedEventArgs e)
{
 textBlock1.Text = checkBox.Content.ToString() + " не отмечен";
}

private void checkBox_Indeterminate(object sender, RoutedEventArgs e)
{
 textBlock1.Text = checkBox.Content.ToString() + " в неопределенном состоянии";
}
```

![Обработка состояния CheckBox в UWP](pics/4.7.png)

Также для нас представляет интерес еще два события - Tapped и Click, которые возникают при нажатии на флажок. Мы можем обработать одно из них:

```

 
 

```

```
private void checkBox_Tapped(object sender, TappedRoutedEventArgs e)
{
 textBlock1.Text = checkBox.IsChecked.ToString();
}
```

Создание флажка в коде c#:

```
CheckBox chBox = new CheckBox();
chBox.IsChecked = true;
chBox.Content = "Новый флажок";
```

### RadioButton

RadioButton представляет переключатель или радиокнопку. Переключатель используется для выбора из двух и более взаимоисключающих вариантов. Элемент RadioButton, как и CheckBox, может быть в отмеченном, неотмеченном и неопределенном 
состоянии. Отличительной чертой этих элементов является свойство GroupName, которое задает группу радиокнопок. И в один момент времени 
мы можем отметить в одной группе только одну радиокнопку. Например,

```

 
 
 

```

![RadioButton in Universal Windows Platform](pics/4.8.png)

Если бы радиокнопки принадлежали бы к двум разным группам, то соответственно мы могли бы выбрать две радиокнопки:

```

 
 
 
 
 
 

```

![](pics/4.9.png)

Чтобы проследить за выбором того или иного элемента, мы также можем определить у элементов событие Checked и его обрабатывать в коде:

```

 
 
 
 

```

А в файле кода C# зададим обработчик:

```
private void RadioButton_Checked(object sender, RoutedEventArgs e)
{
 RadioButton pressed = (RadioButton)sender;
 textBlock1.Text = pressed.Content.ToString();
}
```

![](pics/4.10.png)

### ToggleSwitch

ToggleSwitch служит для переключения между двумя состояниями, которые вступают в силу сразу после изменения состояния переключателя. В этом плане элемент похож на CheckBox. Для определения текущего состояния используется 
свойство IsOn:

```

```

![ToggleSwitch in Universal Windows Platform](pics/4.11.png)

Свойство Header позволяет задать заголовок. При этом кроме заголовка элемент хранит текстовые метки для включенного и выключенного состояний. 
По умолчанию это "on" и "off". При выборе текстовые метки отображаются рядом с элементом. Но с помощью свойств OnContent и 
OffContent мы можем изменить эти метки или вложить более сложное содержимое, чем обычный текст:

```

```

![Кастомизация ToggleSwitch в UWP](pics/4.12.png)

Несмотря на то, что можно задать длинные метки в качестве текста, рекомендуется использовать короткие метки для обозначения состояния, не длиннее 4 символов, например, вкл. и выкл.

Для отслеживания изменения состояния элементы мы можем задействовать событие Toggled:

```

 
 

```

А в коде c# пропишем обработчик:

```
private void toggleSwitch1_Toggled(object sender, RoutedEventArgs e)
{
 textBlock1.Text = toggleSwitch1.IsOn.ToString();
}
```

![](pics/4.13.png)

Программное создание ToggleSwitch:

```
ToggleSwitch toggleSwitch2 = new ToggleSwitch();
toggleSwitch2.IsOn = true;
toggleSwitch2.OnContent = "Включено";
toggleSwitch2.OffContent = "Выключено";
toggleSwitch2.Header = "Переключатель";
```

---

**Источник:** [https://metanit.com/sharp/uwp/4.5.php](https://metanit.com/sharp/uwp/4.5.php)
