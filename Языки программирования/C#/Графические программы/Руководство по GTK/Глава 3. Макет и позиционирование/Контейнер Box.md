# Контейнер Box

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Графические программы|Графические программы]] / [[Языки программирования/C#/Графические программы/Руководство по GTK|Руководство по GTK]] / [[Языки программирования/C#/Графические программы/Руководство по GTK/Глава 3. Макет и позиционирование|Глава 3. Макет и позиционирование]] / Контейнер Box

[[Языки программирования/C#/Графические программы/Руководство по GTK/Глава 3. Макет и позиционирование/Позиционирование виджетов|Назад]] | [[Языки программирования/C#/Графические программы/Руководство по GTK/Глава 3. Макет и позиционирование|Содержание]] | [[Языки программирования/C#/Графические программы/Руководство по GTK/Глава 3. Макет и позиционирование/Контейнер Grid|Вперёд]]

**Дата написания:** 05.09.2026

Контейнер Box в библиотеке GTK является одним из ключевых элементов для создания пользовательских интерфейсов. Он размещает дочерние виджеты в одном направлении: либо в виде строки (горизонтально), либо в виде столбца (вертикально). Он наследуется от абстрактного класса `Container` и предоставляет гибкий способ управления расположением и размерами виджетов.

Для создания объекта `Box` применяется статический метод:

```csharp
public static Box New(Orientation orientation, int spacing)
```

Он принимает два параметра:

- `orientation`: направление дочерних виджетов. Оно представляет перечисление Orientation и может иметь два значения:
  - `Orientation.Horizontal`: расположение в строку (значение 0, а в XML также `GTK_ORIENTATION_HORIZONTAL`)
  - `Orientation.Vertical`: расположение в столбик (значение 1, а в XML также `GTK_ORIENTATION_VERTICAL`)
- `spacing`: расстояние между виджетами

Например, создание GtkBox расположением в строку и отступом между элементами в 10 единиц:

```csharp
Box box =  Box.New(Orientation.Horizontal, 10);
```

Для добавления виджетов в `Box` можно применять ряд методов, среди которых наиболее распространенный - метод **Append()**:

```csharp
public void Append(Widget child)
```

В этот метод передается параметр добавляемый виджет. Например, определим ряд кнопок:

```csharp
using Gtk;

var app= Application.New("com.metanit", Gio.ApplicationFlags.DefaultFlags);

app.OnActivate += (sender, _) =>
{
    var window = new Window();
    window.Title = "METANIT.COM";
    window.DefaultWidth = 250;
    window.DefaultHeight = 200;

    // создаем вертикальный Box с расстоянияем в 10 пикселей между элементами
    var box = Box.New(Orientation.Vertical, 10);
    box.Halign = Align.Start; // выравнивание по левому краю

    // создаем набор кнопок
    var csharp = Button.NewWithLabel("C#");
    var java = Button.NewWithLabel("Java");
    var python = Button.NewWithLabel("Python");

    // добавляем кнопки в контейнер Box
    box.Append(csharp);
    box.Append(java);
    box.Append(python);

    window.Child = box;  // Box - корневой элемент окна

    window.Application = (Application) sender;
    window.Show();
};

app.RunWithSynchronizationContext(null);
```

Здесь создаем три кнопки и последовательно добавляем их в Box:

![Вертикальный контейнер Box в GTK на языке программирования C#](./pics/2.1.png)

Изменим направление контейнера на горизонтальное:

```csharp
using Gtk;

var app= Application.New("com.metanit", Gio.ApplicationFlags.DefaultFlags);

app.OnActivate += (sender, _) =>
{
    var window = new Window();
    window.Title = "METANIT.COM";
    window.DefaultWidth = 250;
    window.DefaultHeight = 200;

    // создаем горизонтальный Box с расстоянияем в 10 пикселей между элементами
    var box = Box.New(Orientation.Horizontal, 10);
    box.Valign = Align.Start; // выравнивание по верхнему краю

    // создаем набор кнопок
    var csharp = Button.NewWithLabel("C#");
    var java = Button.NewWithLabel("Java");
    var python = Button.NewWithLabel("Python");

    // добавляем кнопки в контейнер Box
    box.Append(csharp);
    box.Append(java);
    box.Append(python);

    window.Child = box;  // Box - корневой элемент окна

    window.Application = (Application) sender;
    window.Show();
};

app.RunWithSynchronizationContext(null);
```

И мы получим строку кнопок, которые выстраиваются в горизонтальный ряд

![Горизонтальный контейнер Box в GTK на языке программирования C#](./pics/2.2.png)

Аналогичное определение GitBox в XML:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<interface>
  <object class="GtkWindow" id="window">
    <property name="title">METANIT.COM</property>
    <property name="default-width">300</property>
    <property name="default-height">250</property>
    <child>
      <object class="GtkBox" id="box">
        <property name="valign">GTK_ALIGN_START</property>
        <property name="orientation">GTK_ORIENTATION_HORIZONTAL</property>
        <property name="spacing">10</property>
        <child>
          <object class="GtkButton" id="btn1">
            <property name="label">C</property>
          </object>
        </child>
        <child>
          <object class="GtkButton" id="btn2">
            <property name="label">Java</property>
          </object>
        </child>
        <child>
          <object class="GtkButton" id="btn3">
            <property name="label">Python</property>
          </object>
        </child>
      </object>
    </child>
  </object>
</interface>
```

Для установки параметров GtkBox для виджета определено два свойства:

- **orientation**: направление виджета
- **spacing**: расстояние между вложенными виджетами

## Равномерное распределение пространства

Как видно на скриншоте выше, виджеты размещаются последовательно друг за другом с фиксированными отступами, но после последнего виджета есть много не занятого пространства. И может потребоваться равномерно распределить все виджеты по всей длине контейнера. Для этого применяется свойство Homogeneous. Оно хранит булевые значения и если оно равно `true`, то для всех дочерних элементов будет одинаково распределяться пространство контейнера:

```csharp
using Gtk;

var app= Application.New("com.metanit", Gio.ApplicationFlags.DefaultFlags);

app.OnActivate += (sender, _) =>
{
    var window = new Window();
    window.Title = "METANIT.COM";
    window.DefaultWidth = 250;
    window.DefaultHeight = 200;

    // создаем горизонтальный Box с расстоянияем в 10 пикселей между элементами
    var box = Box.New(Orientation.Horizontal, 10);
    box.Valign = Align.Start; // выравнивание по верхнему краю
    box.Homogeneous = true;  // равномерное распределение виджетов

    // создаем набор кнопок
    var csharp = Button.NewWithLabel("C#");
    var java = Button.NewWithLabel("Java");
    var python = Button.NewWithLabel("Python");

    // добавляем кнопки в контейнер Box
    box.Append(csharp);
    box.Append(java);
    box.Append(python);

    window.Child = box;  // Box - корневой элемент окна

    window.Application = (Application) sender;
    window.Show();
};

app.RunWithSynchronizationContext(null);
```

![Homogeneous и равномерное распределение в контейнере Box в GTK на языке программирования C#](./pics/2.3.png)

## Установка отступов

Из остальных свойств элемента Box следует отметить свойство **Spacing**, которое позволяет установить отступы между элементами после создания контейнера:

```csharp
var box = Box.New(Orientation.Horizontal, 10);
box.Spacing = 30;
```

## Управление дочерними виджетами

Класс `Box` также предоставляет ряд методов для управления вложенными виджетами:

- `Prepend(Widget child)`: добавляет дочерний элемент в начало
- `Remove(Widget child)`: удаляет дочерний виджет
- `InsertChildAfter(Widget child, Widget? sibling)`: вставляет виджет child сразу после виджета sibling

Пример применения:

```csharp
using Gtk;

var app= Application.New("com.metanit", Gio.ApplicationFlags.DefaultFlags);

app.OnActivate += (sender, _) =>
{
    var window = new Window();
    window.Title = "METANIT.COM";
    window.DefaultWidth = 250;
    window.DefaultHeight = 200;

    var box = Box.New(Orientation.Vertical, 10);
    box.Halign = Align.Start;

    // добавляем в пустой контейнер java
    var java = Button.NewWithLabel("Java");
    box.Append(java);

    // добавляем С# в самое начало
    var csharp = Button.NewWithLabel("C#");
    box.Prepend(csharp);

    // добавляем python после java
    var python = Button.NewWithLabel("Python");
    box.InsertChildAfter(python, java);

    // удаляем java
    box.Remove(java);

    window.Child = box;  // Box - корневой элемент окна

    window.Application = (Application) sender;
    window.Show();
};

app.RunWithSynchronizationContext(null);
```

![Box и управление виджетами в GTK и C#](./pics/2.7.png)

**Источник:** [https://metanit.com/sharp/gtk/3.2.php](https://metanit.com/sharp/gtk/3.2.php)