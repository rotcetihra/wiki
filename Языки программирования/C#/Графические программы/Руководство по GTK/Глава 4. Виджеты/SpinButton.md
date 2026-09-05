# SpinButton

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Графические программы|Графические программы]] / [[Языки программирования/C#/Графические программы/Руководство по GTK|Руководство по GTK]] / [[Языки программирования/C#/Графические программы/Руководство по GTK/Глава 4. Виджеты|Глава 4. Виджеты]] / SpinButton

[[Языки программирования/C#/Графические программы/Руководство по GTK/Глава 4. Виджеты/Слайдер Scale|Назад]] | [[Языки программирования/C#/Графические программы/Руководство по GTK/Глава 4. Виджеты|Содержание]] | [[Языки программирования/C#/Графические программы/Руководство по GTK/Глава 5. Списки|Вперёд]]

**Дата написания:** 05.09.2026

Виджет **SpinButton** представляет текстовое поле с кнопками для увеличения или уменьшения значения. Этот виджет позволяет пользователю выбирать числовое значение из определенного диапазона, вводить его вручную или использовать кнопки для регулировки.

Для создания виджета SpinButton применяется статический метод:

```csharp
public static SpinButton New(Adjustment? adjustment, double climbRate, uint digits)
```

- adjustment: объект Adjustment, который определяет диапазон значений
- climbRate: скорость изменения значения при нажатии кнопок
- digits: количество знаков после запятой

Пример создания простейшего SpinButton:

```csharp
using Gtk;

var app= Application.New("com.metanit", Gio.ApplicationFlags.DefaultFlags);

app.OnActivate += (sender, _) =>
{
    var window = new Window();
    window.Title = "METANIT.COM";
    window.DefaultWidth = 250;
    window.DefaultHeight = 200;

    // создаем Adjustment для определения диапазона значений
    var adjustment = Adjustment.New(0, 0, 100, 1, 10, 0);

    // создаем SpinButton
    var spinButton = SpinButton.New(adjustment, 1, 0);
    spinButton.Valign = Align.Start;

    window.Child = spinButton;
    window.Application = (Application) sender;
    window.Show();
};

app.RunWithSynchronizationContext(null);
```

![Виджет SpinButton в GTK и C#](./pics/3.35.png)

## Свойства виджета

Основные свойства SpinButton:

- Adjustment: объект Adjustment, который управляет диапазоном значений
- ClimbRate: скорость изменения значения
- Digits: количество знаков после запятой
- Numeric: является ли ввод числовым
- Wrap: должен ли виджет переключаться между максимальным и минимальным значениями

## Получение и установка значения

Для получения и установки значения SpinButton используется свойство `Value`:

```csharp
// Получение текущего значения
double currentValue = spinButton.Value;

// Установка значения
spinButton.Value = 50;
```

## Обработка изменения значения

Для отслеживания изменения значения SpinButton используется событие `OnValueChanged`:

```csharp
using Gtk;

var app= Application.New("com.metanit", Gio.ApplicationFlags.DefaultFlags);

Label label = Label.New("0");

app.OnActivate += (sender, _) =>
{
    var window = new Window();
    window.Title = "METANIT.COM";
    window.DefaultWidth = 250;
    window.DefaultHeight = 200;

    var adjustment = Adjustment.New(0, 0, 100, 1, 10, 0);
    var spinButton = SpinButton.New(adjustment, 1, 0);
    spinButton.Valign = Align.Start;

    // обработка изменения значения
    spinButton.OnValueChanged += (sender, _) => {
        label.Label_ = $"{sender.Value}";
    };

    var box = Box.New(Orientation.Vertical, 10);
    box.Append(spinButton);
    box.Append(label);

    window.Child = box;
    window.Application = (Application) sender;
    window.Show();
};

app.RunWithSynchronizationContext(null);
```

![Обработка изменения значения SpinButton в GTK и C#](./pics/3.36.png)

## Настройка поведения

Свойство `Numeric` определяет, является ли ввод числовым:

```csharp
spinButton.Numeric = true;  // только числа
```

Свойство `Wrap` определяет, должен ли виджет переключаться между максимальным и минимальным значениями:

```csharp
spinButton.Wrap = true;  // переключение при достижении границ
```

**Источник:** [https://metanit.com/sharp/gtk/4.11.php](https://metanit.com/sharp/gtk/4.11.php)