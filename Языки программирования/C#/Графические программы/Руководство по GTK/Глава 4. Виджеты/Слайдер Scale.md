# Слайдер Scale

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Графические программы|Графические программы]] / [[Языки программирования/C#/Графические программы/Руководство по GTK|Руководство по GTK]] / [[Языки программирования/C#/Графические программы/Руководство по GTK/Глава 4. Виджеты|Глава 4. Виджеты]] / Слайдер Scale

[[Языки программирования/C#/Графические программы/Руководство по GTK/Глава 4. Виджеты/Флажки и радиокнопки CheckButton|Назад]] | [[Языки программирования/C#/Графические программы/Руководство по GTK/Глава 4. Виджеты|Содержание]] | [[Языки программирования/C#/Графические программы/Руководство по GTK/Глава 4. Виджеты/SpinButton|Вперёд]]

**Дата написания:** 05.09.2026

Виджет **Scale** представляет слайдер, который позволяет пользователю выбирать числовое значение из определенного диапазона. Этот виджет полезен для настройки параметров, таких как громкость, яркость, размер шрифта и т.д.

Для создания виджета Scale применяется статический метод:

```csharp
public static Scale New(Orientation orientation, Adjustment? adjustment)
```

- orientation: направление виджета (горизонтальное или вертикальное)
- adjustment: объект Adjustment, который определяет диапазон значений

Пример создания простейшего слайдера:

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

    // создаем горизонтальный слайдер
    var scale = Scale.New(Orientation.Horizontal, adjustment);
    scale.Valign = Align.Start;

    window.Child = scale;
    window.Application = (Application) sender;
    window.Show();
};

app.RunWithSynchronizationContext(null);
```

![Виджет Scale в GTK и C#](./pics/3.33.png)

## Свойства виджета

Основные свойства Scale:

- Adjustment: объект Adjustment, который управляет диапазоном значений
- DrawValue: отображает ли виджет текущее значение
- ValuePos: позиция отображаемого значения
- Digits: количество знаков после запятой

## Получение и установка значения

Для получения и установки значения слайдера используется свойство `Value`:

```csharp
// Получение текущего значения
double currentValue = scale.Value;

// Установка значения
scale.Value = 50;
```

## Обработка изменения значения

Для отслеживания изменения значения слайдера используется событие `OnValueChanged`:

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
    var scale = Scale.New(Orientation.Horizontal, adjustment);
    scale.Valign = Align.Start;

    // обработка изменения значения
    scale.OnValueChanged += (sender, _) => {
        label.Label_ = $"{sender.Value}";
    };

    var box = Box.New(Orientation.Vertical, 10);
    box.Append(scale);
    box.Append(label);

    window.Child = box;
    window.Application = (Application) sender;
    window.Show();
};

app.RunWithSynchronizationContext(null);
```

![Обработка изменения значения слайдера Scale в GTK и C#](./pics/3.34.png)

## Настройка внешнего вида

Свойство `DrawValue` управляет отображением текущего значения:

```csharp
scale.DrawValue = true;  // отображать значение
scale.DrawValue = false; // не отображать значение
```

Свойство `ValuePos` определяет позицию отображаемого значения:

```csharp
scale.ValuePos = PositionType.Top;    // сверху
scale.ValuePos = PositionType.Bottom; // снизу
scale.ValuePos = PositionType.Left;   // слева
scale.ValuePos = PositionType.Right;  // справа
```

Свойство `Digits` определяет количество знаков после запятой:

```csharp
scale.Digits = 2;  // два знака после запятой
```

**Источник:** [https://metanit.com/sharp/gtk/4.10.php](https://metanit.com/sharp/gtk/4.10.php)