# CalendarDatePicker и CalendarView

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Графические программы|Графические программы]] / [[Языки программирования/C#/Графические программы/Руководство по UWP|Руководство по UWP]] / [[Языки программирования/C#/Графические программы/Руководство по UWP/Глава 4. Элементы управления|Глава 4. Элементы управления]] / CalendarDatePicker и CalendarView

[[Языки программирования/C#/Графические программы/Руководство по UWP/Глава 4. Элементы управления/Image и работа с изображениями|Назад]] | [[Языки программирования/C#/Графические программы/Руководство по UWP/Глава 4. Элементы управления|Содержание]] | [[Языки программирования/C#/Графические программы/Руководство по UWP/Глава 4. Элементы управления/DatePicker и TimePicker|Вперёд]]

**Дата написания:** 05.09.2026

CalendarDatePicker и CalendarViewПоследнее обновление: 11.02.2016
 
 
 

 
- 
 
- 
 
- 
 
 

 
 

 
 
 
 
 

 

CalendarDatePicker представляет календарь, в котором можно выбрать дату.

```

 

```

Свойство PlaceholderText задает текст для ввода в календаре. По умолчанию равно строке "select a date".

Свойство CalendarIdentifier задает тип календаря в зависимости от региональных предпочтений. Может принимать следующие значения:

- 

GregorianCalendar: григорианский календарь, значение по умолчанию

- 

HebrewCalendar: еврейский календарь

- 

HijriCalendar: мусульманский календарь

- 

JapaneseCalendar: японский календарь

- 

JulianCalendar: юлианский календарь

- 

KoreanCalendar: корейский календарь

- 

TaiwanCalendar: тайваньский календарь

- 

ThaiCalendar: тайский календарь

- 

UmAlQuraCalendar: другая версия мусульманского календаря

В итоге после запуска приложения мы увидим поле:
![CalendarDatePicker в Universal Windows Platform](pics/4.22.png)

При нажатие на это поле отобразится календарик, в котором мы сможем установить дату:
![](pics/4.23.png)

Календарь использует языковые настройки проекта, которые по умолчанию настроены на применение англоязычной культуры. Поэтому, чтобы локализовать на нужную нам культуру, 
нам может потребоваться изменить язык приложения по умолчанию в файле манифеста:
![Локализация календаря в UWP](pics/4.24.png)

Для отслеживания изменения выбранной даты в календаре мы можем обрабатывать событие DateChanged:

```

 
 

```

В файле кода c# в обработчике выведем выбранную дату в текстовый блок:

```
private void calendar_DateChanged(CalendarDatePicker sender, CalendarDatePickerDateChangedEventArgs args)
{
 DateTime selectedDate = calendar.Date.Value.DateTime;
 textBlock1.Text = selectedDate.ToString("dd/MM/yyyy");
 
 // также мы можем получить старую и новую дату таким образом
 //DateTime? newDate = args.NewDate.Value.DateTime;
 //DateTime? oldDate = args.OldDate.Value.DateTime;
}
```

![Изменение даты в календаре в UWP](pics/4.25.png)

Еще пара свойств, которые мы можем использовать у календаря: DateFormat и DisplayMode.

DateFormat определяет формат отображения даты:

- 

`{}{day.integer} {month.full} {year.full}`: формат "1 февраля 2016"

- 

`{}{day.integer}/{month.integer}/{year.full}`: формат "1/2/2016"

- 

`{}{month.full} {day.integer}, {year.full}`: формат "февраль 1, 2016"

- 

`{}{month.integer}/{day.integer}/{year.full}`: формат "2/1/2016"

- 

`{}{year.full}/{month.integer}/{day.integer}`: формат "2016/2/1"

DisplayMode определяет формат диапазонов в календаре:

- 

`Decade`: календарь разделен по десятилетиям

- 

`Month`: разделение по месяцам

- 

`Year`: разделение по годам

Программное создание календаря в коде c#:

```
CalendarDatePicker calendar = new CalendarDatePicker();
calendar.Date = DateTime.Now.Date;
calendar.DisplayMode = CalendarViewDisplayMode.Month;
calendar.PlaceholderText = "Выберите дату";
```

### CalendarView

CalendarView в многом похож на CalendarDatePicker, только представляет открытый календарь без текстового поля ввода. Главная его особенность - 
возможность выделения дат. Для настройки выделения дат используется множество разных свойств. Так, свойство SelectionMode 
устанавливает режим выделения дат и может принимать следующие значения:

- 

`None`: нельзя выделять даты

- 

`Single`: можно выделить только одну дату

- 

`Multiple`: можно выделять сразу несколько дат

Еще набор свойств устанавливает настройки цветов, шрифтов и т.д.: SelectedBorderBrush (цвет границы выделенной даты), 
SelectedForeground (цвет шрифта выделенной даты), SelectedHoverBorderBrush (цвет границы при наведении).

Еще ряд свойств устанавливают шрифты дат: DayItemFontFamily (семейство шрифтов дат), 
DayItemFontSize (размер шрифта дат) и т.д.

Через событие мы можем отследить выделение дат в CalendarView:

```

 
 

```

И обработчик в файле кода:

```
private void CalendarView_SelectedDatesChanged(CalendarView sender, CalendarViewSelectedDatesChangedEventArgs args)
{
 textBlock1.Text = "";

 foreach (var d in calendarView.SelectedDates)
 textBlock1.Text += d.ToString("dd/MM/yyyy") + "\n";

 // args.AddedDates - новые выделенные даты
 //args.RemovedDates - даты с которых сняты выделения
}
```

![CalendarView in Universal Windows Platform](pics/4.26.png)

---

**Источник:** [https://metanit.com/sharp/uwp/4.7.php](https://metanit.com/sharp/uwp/4.7.php)
