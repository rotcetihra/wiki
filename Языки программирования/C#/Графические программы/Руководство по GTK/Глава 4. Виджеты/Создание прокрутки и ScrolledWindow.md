# Создание прокрутки и ScrolledWindow

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Графические программы|Графические программы]] / [[Языки программирования/C#/Графические программы/Руководство по GTK|Руководство по GTK]] / [[Языки программирования/C#/Графические программы/Руководство по GTK/Глава 4. Виджеты|Глава 4. Виджеты]] / Создание прокрутки и ScrolledWindow

[[Языки программирования/C#/Графические программы/Руководство по GTK/Глава 4. Виджеты/Обработка изменения свойств виджетов|Назад]] | [[Языки программирования/C#/Графические программы/Руководство по GTK/Глава 4. Виджеты|Содержание]] | [[Языки программирования/C#/Графические программы/Руководство по GTK/Глава 4. Виджеты/Многострочное текстовое поле TextView|Вперёд]]

**Дата написания:** 05.09.2026

Виджет **ScrolledWindow** представляет контейнер, который позволяет прокручивать свое содержимое. Для создания окна с прокруткой применяется статический метод `ScrolledWindow.New()`

```csharp
ScrolledWindow scrolledWindow = ScrolledWindow.New();
```

Для установки содержимого контейнер прокрутки применяет свойство **Child**:

```csharp
public Widget? Child { get; set; }
```

В качестве прокручиваемого содержимого может выступать любой виджет.

Прежде чем применить прокрутку, посмотрим, с какой распространенной проблемой мы можем столкнуться. Пусть у нас есть следующее приложение:

```csharp
using Gtk;

var app= Application.New("com.metanit", Gio.ApplicationFlags.DefaultFlags);

app.OnActivate += (sender, _) =>
{
    var window = new Window();
    window.Title = "METANIT.COM";
    window.DefaultWidth = 250;
    window.DefaultHeight = 200;

    Box box = Box.New(Orientation.Vertical, 10);
    box.Valign = Align.Start;
    box.Halign = Align.Start;

    // создаем и добавляем в Box 15 меток
    for(int i=0; i < 15; i++){
        var label = Label.New($"Label {i}");
        box.Append(label);
    }
    window.Child = box;
    window.Application = (Application) sender;
    window.Show();
};

app.RunWithSynchronizationContext(null);
```

Здесь мы создаем и добавляем в контейнер Box 15 текстовых меток. В итоге контейнер Box будет растягиваться, чтобы вместить все текстовые метки, а вместе с ним будет расятиваться окно, чтобы вместить Box.

![прокрутка виджетов в ScrolledWindow в GTK и C#](./pics/2.42.png)

Теперь применим `ScrolledWindow` для создания прокрутки:

```csharp
using Gtk;

var app= Application.New("com.metanit", Gio.ApplicationFlags.DefaultFlags);

app.OnActivate += (sender, _) =>
{
    var window = new Window();
    window.Title = "METANIT.COM";
    window.DefaultWidth = 250;
    window.DefaultHeight = 200;

    Box box = Box.New(Orientation.Vertical, 10);
    box.Valign = Align.Start;
    box.Halign = Align.Start;

    for(int i=0; i < 15; i++){
        var label = Label.New($"Label {i}");
        box.Append(label);
    }

    var scrolledWindow = ScrolledWindow.New();
    scrolledWindow.Child = box;

    window.Child = scrolledWindow;
    window.Application = (Application) sender;
    window.Show();
};

app.RunWithSynchronizationContext(null);
```

В итоге, если окно не вмещает все содержимое вложенного компонента, то добавляются полосы прокрутки:

![прокрутка виджетов в  ScrolledWindow в GTK и C#](./pics/2.45.png)

Создание аналогичного интерфейса в XML:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<interface>
  <object class="GtkWindow" id="window">
    <property name="title">METANIT.COM</property>
    <property name="default-width">250</property>
    <property name="default-height">200</property>
    <child>
      <object class="GtkScrolledWindow" id="scrollView">
          <child>
            <object class="GtkBox">
                <property name="valign">GTK_ALIGN_START</property>
                <property name="halign">GTK_ALIGN_START</property>
                <property name="orientation">GTK_ORIENTATION_VERTICAL</property>
                <property name="spacing">10</property>
                <child>
                    <object class="GtkLabel">
                      <property name="label">Label 0</property>
                    </object>
                </child>
                <child>
                    <object class="GtkLabel">
                      <property name="label">Label 1</property>
                    </object>
                </child>
                <child>
                    <object class="GtkLabel">
                      <property name="label">Label 2</property>
                    </object>
                </child>
                <child>
                    <object class="GtkLabel">
                      <property name="label">Label 3</property>
                    </object>
                </child>
                <child>
                    <object class="GtkLabel">
                      <property name="label">Label 4</property>
                    </object>
                </child>
                <child>
                    <object class="GtkLabel">
                      <property name="label">Label 5</property>
                    </object>
                </child>
                <child>
                    <object class="GtkLabel">
                      <property name="label">Label 6</property>
                    </object>
                </child>
                <child>
                    <object class="GtkLabel">
                      <property name="label">Label 7</property>
                    </object>
                </child>
            </object>
          </child>
      </object>
    </child>
  </object>
</interface>
```

## Основные свойства виджета

Отмечу некоторые основные свойства виджета:

- `MaxContentHeight`: максимальная высота содержимого scrolled_window
- `MaxContentWidth`: максимальная ширина содержимого scrolled_window
- `MinContentHeight`: минимальная высота содержимого scrolled_window
- `MinContentWidth`: минимальная ширина содержимого scrolled_window
- `OverlayScrolling`: указывает, включена ли прокрутка наложения или нет. Если равно `TRUE` (по умолчанию), то прокрутка накладывается на содержимое динамически, если `FALSE`, то прокрутка фиксированная
- `WindowPlacement`: управляет размещением полос прокрутки и представляет перечисление `CornerType`. Данное перечисление определяет следующее константы:
  - `TopLeft`: полосы прокрутки по правой и нижней границе виджета (поведение по умолчанию). Значение: 0
  - `BottomLeft`: полосы прокрутки по верхней и правой границе виджета. Значение: 1
  - `GTK_CORNER_TOP_RIGHT`: полосы прокрутки по левой и нижней границе виджета. Значение: 2
  - `TopRight`: полосы прокрутки по верхней и левой границе виджета. Значение: 3

Краткий пример применения свойств:

```csharp
var scrolledWindow = ScrolledWindow.New();
// минимальная высота - 150 единиц
scrolledWindow.MinContentHeight = 150;

// устанавливаем фиксированные полосы прокрутки
scrolledWindow.OverlayScrolling = false;

// Расположение полос прокрутки справа и внизу
scrolledWindow.WindowPlacement = CornerType.BottomRight;
```

**Источник:** [https://metanit.com/sharp/gtk/4.5.php](https://metanit.com/sharp/gtk/4.5.php)