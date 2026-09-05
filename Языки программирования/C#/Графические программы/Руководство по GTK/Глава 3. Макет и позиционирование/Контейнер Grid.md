# Контейнер Grid

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Графические программы|Графические программы]] / [[Языки программирования/C#/Графические программы/Руководство по GTK|Руководство по GTK]] / [[Языки программирования/C#/Графические программы/Руководство по GTK/Глава 3. Макет и позиционирование|Глава 3. Макет и позиционирование]] / Контейнер Grid

[[Языки программирования/C#/Графические программы/Руководство по GTK/Глава 3. Макет и позиционирование/Контейнер Box|Назад]] | [[Языки программирования/C#/Графические программы/Руководство по GTK/Глава 3. Макет и позиционирование|Содержание]] | [[Языки программирования/C#/Графические программы/Руководство по GTK/Глава 3. Макет и позиционирование/Контейнер Fixed|Вперёд]]

**Дата написания:** 05.09.2026

Контейнер Grid в GTK представляет мощный и гибкий инструмент для создания сложных макетов пользовательского интерфейса. В отличие от более простых контейнеров, таких как Box, `Grid` позволяет организовать виджеты в виде таблицы с строками и столбцами и расположить их в виде сетки, что делает его идеальным выбором для многих типов интерфейсов.

Для создания экземпляра `Grid` применяется статический метод `Grid.New()` без параметров:

```csharp
Grid grid = Grid.New();
```

## Добавление виджетов в Grid

Для добавления виджетов в `Grid` используются методы:

- Attach: добавляет виджет в следующую ячейку грида
- AttachNextTo: размещает виджет относительно другого виджета

Метод Attach() принимает 5 параметров:

```csharp
void Attach(Widget child, int column, int row, int width, int height)
```

- `child`: добавляемый виджет
- `column`: номер столбца виджета
- `row`: номер строки виджета
- `width`: количество столбцов, которые занимает виджет
- `height`: количество строк, которые занимает виджет

Например, определим сетку из кнопок:

```csharp
using Gtk;

var app= Application.New("com.metanit", Gio.ApplicationFlags.DefaultFlags);

app.OnActivate += (sender, _) =>
{
    var window = new Window();
    window.Title = "METANIT.COM";
    window.DefaultWidth = 250;
    window.DefaultHeight = 200;

    Grid grid = Grid.New();  // создаем Grid

    // Создаем несколько виджетов
    Button button1 = Button.NewWithLabel("Button 1");
    Button button2 = Button.NewWithLabel("Button 2");
    Button button3 = Button.NewWithLabel("Button 3");
    Button button4 = Button.NewWithLabel("Button 4");

    // Добавляем виджеты в Grid
    grid.Attach(button1, 0, 0, 1, 1);  // столбец 0, строка 0, ширина 1, высота 1
    grid.Attach(button2, 1, 0, 1, 1);  // столбец 1, строка 0, ширина 1, высота 1
    grid.Attach(button3, 0, 1, 1, 1);  // столбец 0, строка 1, ширина 1, высота 1
    grid.Attach(button4, 1, 1, 1, 1);  // столбец 1, строка 1, ширина 1, высота 1

    window.Child = grid;  // grid - корневой элемент окна

    window.Application = (Application) sender;
    window.Show();
};

app.RunWithSynchronizationContext(null);
```

Здесь создаем 4 кнопки и последовательно добавляем их в грид:

![Контейнер Grid в GTK на языке программирования C#](./pics/2.8.png)

Определение аналогичного грида в XML (файл "builder.ui"):

```xml
<?xml version="1.0" encoding="UTF-8"?>
<interface>
  <object class="GtkWindow" id="window">
    <property name="title">METANIT.COM</property>
    <property name="default-width">300</property>
    <property name="default-height">250</property>
    <child>
      <object class="GtkGrid" id="grid">
        <child>
          <object class="GtkButton" id="btn1">
            <property name="label">Button 1</property>
            <layout>
              <property name="column">0</property>
              <property name="row">0</property>
            </layout>
          </object>
        </child>
        <child>
          <object class="GtkButton" id="btn2">
            <property name="label">Button 2</property>
            <layout>
              <property name="column">1</property>
              <property name="row">0</property>
            </layout>
          </object>
        </child>
        <child>
          <object class="GtkButton" id="btn3">
            <property name="label">Button 3</property>
            <layout>
              <property name="column">0</property>
              <property name="row">1</property>
            </layout>
          </object>
        </child>
      </object>
    </child>
  </object>
</interface>
```

Для установки расположения каждого виджета в XML внутри кода виджета применяется элемент `<layout>`, в котором с помощью свойств `row` и `column` устанавливается ячейка виджета:

```xml
<layout>
    <property name="column">1</property>
    <property name="row">0</property>
</layout>
```

Альтернативный способ добавления представляет метод AttachNextTo, который размещает виджет относительно другого:

```csharp
void AttachNextTo(Widget child, Widget? sibling, PositionType side, int width, int height)
```

Этот метод добавляет виджет child относительно уже ранее добавленного виджета sibling. Куда именно добавляется виджет, определяется перечислением PositionType:

- `PositionType.Left`: в ячейку слева от `sibling`
- `PositionType.Right`: в ячейку справа от `sibling`
- `PositionType.Top`: в ячейку сверху от `sibling`
- `PositionType.Bottom`: в ячейку снизу от `sibling`

Пример вкратце:

```csharp
var grid = Grid.New();

Button button1 = Button.NewWithLabel("Button 1");
Button button2 = Button.NewWithLabel("Button 2");

grid.Attach(button1, 1, 0, 1, 1);  // столбец 1, строка 0, ширина 1, высота 1
// добавляем button2 перед button1 (то есть в ячейку слева)
grid.AttachNextTo(button2, button1, PositionType.Left, 1, 1);
```

## Растяжение ячеек на несколько строк/столбцов

При необходимости виджет можно растянуть на ряд строк/столбцов:

```csharp
using Gtk;

var app= Application.New("com.metanit", Gio.ApplicationFlags.DefaultFlags);

app.OnActivate += (sender, _) =>
{
    var window = new Window();
    window.Title = "METANIT.COM";
    window.DefaultWidth = 250;
    window.DefaultHeight = 200;

    Grid grid = Grid.New();

    Button button1 = Button.NewWithLabel("Button 1");
    Button button2 = Button.NewWithLabel("Button 2");
    Button button3 = Button.NewWithLabel("Button 3");

    grid.Attach(button1, 0, 0, 1, 1);  // столбец 0, строка 0, ширина 1, высота 1
    grid.Attach(button2, 1, 0, 1, 1);  // столбец 1, строка 0, ширина 1, высота 1
    grid.Attach(button3, 0, 1, 2, 1);  // столбец 0, строка 1, ширина 2, высота 1

    window.Child = grid;

    window.Application = (Application) sender;
    window.Show();
};

app.RunWithSynchronizationContext(null);
```

Здесь кнопку button3 растягиваем на 2 столбца:

```csharp
grid.Attach(button3, 0, 1, 2, 1);
```

![Контейнер Grid и растяжение виджетов в GTK на языке программирования C#](./pics/2.9.png)

## Свойства Grid

Рассмотрим основные свойства Grid:

- ColumnSpacing: расстояние между столбцами
- RowSpacing: расстояние между строками
- ColumnHomogeneous: если true, все столбцы будут одинаковой ширины
- RowHomogeneous: если true, все строки будут одинаковой высоты

### Установка отступов

Например, установим отступы между строками и столбцами:

```csharp
using Gtk;

var app= Application.New("com.metanit", Gio.ApplicationFlags.DefaultFlags);

app.OnActivate += (sender, _) =>
{
    var window = new Window();
    window.Title = "METANIT.COM";
    window.DefaultWidth = 250;
    window.DefaultHeight = 200;

    Grid grid = Grid.New();
    grid.ColumnSpacing = 10;  // расстояние между столбцами
    grid.RowSpacing = 15;     // расстояние между строками

    Button button1 = Button.NewWithLabel("Button 1");
    Button button2 = Button.NewWithLabel("Button 2");
    Button button3 = Button.NewWithLabel("Button 3");
    Button button4 = Button.NewWithLabel("Button 4");

    grid.Attach(button1, 0, 0, 1, 1);  // столбец 0, строка 0, ширина 1, высота 1
    grid.Attach(button2, 1, 0, 1, 1);  // столбец 1, строка 0, ширина 1, высота 1
    grid.Attach(button3, 0, 1, 1, 1);  // столбец 0, строка 1, ширина 1, высота 1
    grid.Attach(button4, 1, 1, 1, 1);  // столбец 1, строка 1, ширина 1, высота 1

    window.Child = grid;

    window.Application = (Application) sender;
    window.Show();
};

app.RunWithSynchronizationContext(null);
```

![Контейнер Grid и расстояния между виджетами в GTK на языке программирования C#](./pics/2.10.png)

Аналогичная установка отступов в XML:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<interface>
  <object class="GtkWindow" id="window">
    <property name="title">METANIT.COM</property>
    <property name="default-width">300</property>
    <property name="default-height">250</property>
    <child>
      <object class="GtkGrid" id="grid">
        <property name="row-spacing">20</property>
        <property name="column-spacing">10</property>

        <child>
          <object class="GtkButton" id="btn1">
            <property name="label">Button 1</property>
            <layout>
              <property name="column">0</property>
              <property name="row">0</property>
            </layout>
          </object>
        </child>
        <child>
          <object class="GtkButton" id="btn2">
            <property name="label">Button 2</property>
            <layout>
              <property name="column">1</property>
              <property name="row">0</property>
            </layout>
          </object>
        </child>
        <child>
          <object class="GtkButton" id="btn3">
            <property name="label">Button 3</property>
            <layout>
              <property name="column">0</property>
              <property name="row">1</property>
            </layout>
          </object>
        </child>
        <child>
          <object class="GtkButton" id="btn4">
            <property name="label">Button 1</property>
            <layout>
              <property name="column">1</property>
              <property name="row">1</property>
            </layout>
          </object>
        </child>

      </object>
    </child>
  </object>
</interface>
```

### Равномерное распределение виджетов

Установив свойства ColumnHomogeneous и/или RowHomogeneous в `true`, можно равномерно распределить виджеты по вертикали и/или горизонтали:

```csharp
using Gtk;

var app= Application.New("com.metanit", Gio.ApplicationFlags.DefaultFlags);

app.OnActivate += (sender, _) =>
{
    var window = new Window();
    window.Title = "METANIT.COM";
    window.DefaultWidth = 250;
    window.DefaultHeight = 200;

    Grid grid = Grid.New();
    grid.ColumnSpacing = 10;  // расстояние между столбцами
    grid.RowSpacing = 10;     // расстояние между строками
    grid.ColumnHomogeneous = true;  // равномерное распределение по вертикали
    grid.RowHomogeneous = true;  // равномерное распределение по горизонтали

    Button button1 = Button.NewWithLabel("Button 1");
    Button button2 = Button.NewWithLabel("Button 2");
    Button button3 = Button.NewWithLabel("Button 3");
    Button button4 = Button.NewWithLabel("Button 4");

    grid.Attach(button1, 0, 0, 1, 1);  // столбец 0, строка 0, ширина 1, высота 1
    grid.Attach(button2, 1, 0, 1, 1);  // столбец 1, строка 0, ширина 1, высота 1
    grid.Attach(button3, 0, 1, 1, 1);  // столбец 0, строка 1, ширина 1, высота 1
    grid.Attach(button4, 1, 1, 1, 1);  // столбец 1, строка 1, ширина 1, высота 1

    window.Child = grid;

    window.Application = (Application) sender;
    window.Show();
};

app.RunWithSynchronizationContext(null);
```

![Контейнер Grid и равномерное распределение виджетов в GTK на языке программирования C#](./pics/2.12.png)

В XML для грида устанавливаются соответствующие свойства:

```xml
<object class="GtkGrid" id="grid">
    <property name="row-spacing">10</property>
    <property name="column-spacing">10</property>
    <property name="row-homogeneous">TRUE</property>
    <property name="column-homogeneous">TRUE</property>

    <child>
      <object class="GtkButton" id="btn1">
        <property name="label">Button 1</property>
        <layout>
          <property name="column">0</property>
          <property name="row">0</property>
        </layout>
      </object>
    </child>
    <child>
      <object class="GtkButton" id="btn2">
        <property name="label">Button 2</property>
        <layout>
          <property name="column">1</property>
          <property name="row">0</property>
        </layout>
      </object>
    </child>
    <child>
      <object class="GtkButton" id="btn3">
        <property name="label">Button 3</property>
        <layout>
          <property name="column">0</property>
          <property name="row">1</property>
        </layout>
      </object>
    </child>
    <child>
      <object class="GtkButton" id="btn4">
        <property name="label">Button 4</property>
        <layout>
          <property name="column">1</property>
          <property name="row">1</property>
        </layout>
      </object>
    </child>
</object>
```

## Выравнивание виджетов в ячейках

По скриншоту из предыдущего примера можно увидеть, что виджеты (в данном случае кнопки) при помещении в ячейку грида растягиваются по всему пространству ячейки. Это стандртное поведение, тем не менее оно может быть нежелательным. Но с помощью стандартных свойств `Halign` и `Valign` мы можем управлять выравниванием виджетов внутри ячеек грида. Например, позиционируем один виджет строго в левом верхнем углу ячейки без растяжения на всю ячейку:

```csharp
using Gtk;

var app= Application.New("com.metanit", Gio.ApplicationFlags.DefaultFlags);

app.OnActivate += (sender, _) =>
{
    var window = new Window();
    window.Title = "METANIT.COM";
    window.DefaultWidth = 250;
    window.DefaultHeight = 200;

    Grid grid = Grid.New();
    grid.ColumnSpacing = 10;  // расстояние между столбцами
    grid.RowSpacing = 10;     // расстояние между строками
    grid.ColumnHomogeneous = true;  // равномерное распределение по вертикали
    grid.RowHomogeneous = true;  // равномерное распределение по горизонтали

    Button button1 = Button.NewWithLabel("Button 1");
    button1.Valign = Align.Start;   // позиционирование вверху
    button1.Halign = Align.Start;   // позиционирование слева

    Button button2 = Button.NewWithLabel("Button 2");
    Button button3 = Button.NewWithLabel("Button 3");
    Button button4 = Button.NewWithLabel("Button 4");

    grid.Attach(button1, 0, 0, 1, 1);  // столбец 0, строка 0, ширина 1, высота 1
    grid.Attach(button2, 1, 0, 1, 1);  // столбец 1, строка 0, ширина 1, высота 1
    grid.Attach(button3, 0, 1, 1, 1);  // столбец 0, строка 1, ширина 1, высота 1
    grid.Attach(button4, 1, 1, 1, 1);  // столбец 1, строка 1, ширина 1, высота 1

    window.Child = grid;

    window.Application = (Application) sender;
    window.Show();
};

app.RunWithSynchronizationContext(null);
```

В данном случае кнопка button1 позиционируется влевом верхнем углу ячейки:

![Выравнивание виджетов в ячейках контейнера Grid в GTK на языке программирования C#](./pics/2.11.png)

**Источник:** [https://metanit.com/sharp/gtk/3.3.php](https://metanit.com/sharp/gtk/3.3.php)