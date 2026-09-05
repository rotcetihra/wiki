# DatePicker и TimePicker

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Графические программы|Графические программы]] / [[Языки программирования/C#/Графические программы/Руководство по UWP|Руководство по UWP]] / [[Языки программирования/C#/Графические программы/Руководство по UWP/Глава 4. Элементы управления|Глава 4. Элементы управления]] / DatePicker и TimePicker

[[Языки программирования/C#/Графические программы/Руководство по UWP/Глава 4. Элементы управления/CalendarDatePicker и CalendarView|Назад]] | [[Языки программирования/C#/Графические программы/Руководство по UWP/Глава 4. Элементы управления|Содержание]] | [[Языки программирования/C#/Графические программы/Руководство по UWP/Глава 4. Элементы управления/Flyout|Вперёд]]

**Дата написания:** 05.09.2026

DatePicker и TimePickerПоследнее обновление: 11.02.2016
 
 
 

 
- 
 
- 
 
- 
 
 

 
 

 
 
 
 
 

 
### DatePicker

Элемент DatePicker используется для выбора даты:

```

```

![DatePicker в Universal Windows Platform](pics/4.27.png)

При нажатии на элемент появляется список для выбора даты, месяца, года:
![Элемент DatePicker в UWP](pics/4.28.png)

Среди свойств DatePicker можно отметить следующие:

- 

DayFormat: формат отображения дней

- 

MonthFormat: формат отображения месяцев

- 

YearFormat: формат отображения годов

- 

CalendarIdentifier: идентификатор календаря, который имеет те же самые значения, что и у CalendarDatePicker

- 

MaxYear: максимальный год для выбора

- 

MinYear: наименьший год для выбора

- 

Header: заголовок над элементом управления

Для обработки выбора даты мы можем использовать событие DateChanged:

```

 
 

```

И обработчик в файле кода C#:

```
private void datePicker_DateChanged(object sender, DatePickerValueChangedEventArgs e)
{
 DateTimeOffset dateOffset = datePicker1.Date;
 textBlock1.Text = dateOffset.Date.ToString("dd.MM.yyyy");
}
```

![Выбор даты в DatePicker в UWP](pics/4.29.png)

### TimePicker

TimePicker применяется для отображения или установки времени:

```

```

![TimePicker в Universal Windows Platform](pics/4.19.png)

Свойство `Header` задает заголовок, а свойство `ClockIdentifier` формат отображения времени. Оно принимает два 
значения: `12HourClock` (12-часовой формат) и `24HourClock` (24-часовой формат). При нажатии на часы или минуты произойдет открытие 
списка, в котором можно установить новое время:
![](pics/4.20.png)

Чтобы отследить изменение времени в TimePicker мы можем обрабатывать событие TimeChanged:

```

 
 

```

В обработчике будем выводить выбранное время в текстовый блок:

```
private void TimePicker_TimeChanged(object sender, TimePickerValueChangedEventArgs e)
{
 TimeSpan time = timePicker1.Time;
 textBlock1.Text = $"{time.Hours} : {time.Minutes}";
}
```

Свойство `Time` хранит выбранное время в виде объекта TimeSpan. Получив этот объект, мы можем использовать его свойства и методы:
![Установка времени в TimePicker в UWP](pics/4.21.png)

---

**Источник:** [https://metanit.com/sharp/uwp/4.8.php](https://metanit.com/sharp/uwp/4.8.php)
