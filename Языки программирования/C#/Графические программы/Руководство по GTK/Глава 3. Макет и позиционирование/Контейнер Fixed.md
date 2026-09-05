# Контейнер Fixed

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Графические программы|Графические программы]] / [[Языки программирования/C#/Графические программы/Руководство по GTK|Руководство по GTK]] / [[Языки программирования/C#/Графические программы/Руководство по GTK/Глава 3. Макет и позиционирование|Глава 3. Макет и позиционирование]] / Контейнер Fixed

[[Языки программирования/C#/Графические программы/Руководство по GTK/Глава 3. Макет и позиционирование/Контейнер Grid|Назад]] | [[Языки программирования/C#/Графические программы/Руководство по GTK/Глава 3. Макет и позиционирование|Содержание]] | [[Языки программирования/C#/Графические программы/Руководство по GTK/Глава 4. Виджеты/Текстовая метка и класс Label|Вперёд]]

**Дата написания:** 05.09.2026

Контейнер Fixed в GTK представляет контейнер для размещения виджетов с абсолютным позиционированием. В отличие от других контейнеров, таких как `Box` или `Grid`, Fixed позволяет точно указывать координаты (X, Y) для каждого дочернего элемента.

Основные характеристики `Fixed`:

- Абсолютное позиционирование: виджеты размещаются по точным координатам
- Фиксированный размер: контейнер не изменяет размеры автоматически
- Простота концепции и соответственно использования. Лучше использовать для простых форм или когда нужен полный контроль над позиционированием.
- Низкая гибкость: не подходит для адаптивных интерфейсов, в частности, для окон, которые должны менять размер, так как виджеты не будут перемещаться автоматически.

Для создания контейнера `Fixed` применяется статический метод `Fixed.New()`, который не принимает параметров:

```csharp
Fixed fix = Fixed.New();
```

Основные методы класса `Fixed`:

- `Put(Widget widget, int x, int y)`: добавляет виджет на указанные координаты x и y
- `Move(Widget widget, int x, int y)`: перемещает существующий виджет на точку с координатами x и y
- `Remove(Widget widget)`: удаляет виджет
- `GetChildPosition(Widget widget, out int x, out int y)`: получает текущие координаты виджета

Таким образом, для добавления виджетов используется метод `Put()`, который принимает сам виджет и координаты X, Y:

```csharp
using Gtk;

var app= Application.New("com.metanit", Gio.ApplicationFlags.DefaultFlags);

app.OnActivate += (sender, _) =>
{
    var window = new Window();
    window.Title = "METANIT.COM";
    window.DefaultWidth = 250;
    window.DefaultHeight = 200;

    Fixed fix = Fixed.New();

    // Создание кнопки
    Button button1 = Button.NewWithLabel("Button 1");
    // Размещение кнопки в контейнере Fixed на координатах (50, 50)
    fix.Put(button1, 50, 50);

    // Еще одна кнопка
    Button button2 = Button.NewWithLabel("Button 2");
    // Размещение кнопки в контейнере Fixed на координатах (150, 100)
    fix.Put(button2, 150, 100);

    window.Child = fix;

    window.Application = (Application) sender;
    window.Show();
};

app.RunWithSynchronizationContext(null);
```

![контейнер Fixed в GTK на языке программирования C#](./pics/2.13.png)

При абсолютном позиционировании мы можем применять у виджетов метод `SetSizeRequest(width, height)` для установки абсолютных значений ширины и высоты:

```csharp
using Gtk;

var app= Application.New("com.metanit", Gio.ApplicationFlags.DefaultFlags);

app.OnActivate += (sender, _) =>
{
    var window = new Window();
    window.Title = "METANIT.COM";
    window.DefaultWidth = 250;
    window.DefaultHeight = 200;

    Fixed fix = Fixed.New();

    // Создание кнопки
    Button button1 = Button.NewWithLabel("Button 1");
    // ширина - 120 пикселей, высота - 30
    button1.SetSizeRequest(120, 30);
    // Размещение кнопки в контейнере Fixed на координатах (50, 50)
    fix.Put(button1, 50, 50);

    // Еще одна кнопка
    Button button2 = Button.NewWithLabel("Button 2");
    // ширина - 90 пикселей, высота - 50
    button2.SetSizeRequest(90, 50);
    // Размещение кнопки в контейнере Fixed на координатах (150, 100)
    fix.Put(button2, 150, 100);

    window.Child = fix;

    window.Application = (Application) sender;
    window.Show();
};

app.RunWithSynchronizationContext(null);
```

![абсолютные размеры в контейнере Fixed в GTK на языке программирования C#](./pics/2.14.png)

Вместо использования метода `SetSizeRequest()` у виджетов также можно напрямую установить свойства `WidthRequest` и `HeightRequest` для установки соответственно желательной ширины и высоты.

Пример определения аналогичного контейнера в XML:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<interface>
  <object class="GtkWindow" id="window">
    <property name="visible">True</property>
    <property name="title">METANIT.COM</property>
    <property name="default-width">250</property>
    <property name="default-height">200</property>
    <child>
        <object class="GtkFixed">
          <child>
            <object class="GtkButton">
              <property name="label">Button 1</property>
              <property name="width-request">120</property>
              <property name="height-request">30</property>
              <property name="margin-start">50</property>
              <property name="margin-top">50</property>
            </object>
          </child>

          <child>
            <object class="GtkButton">
              <property name="label">Button 2</property>
              <property name="width-request">90</property>
              <property name="height-request">50</property>
              <property name="margin-start">150</property>
              <property name="margin-top">100</property>
            </object>
          </child>

        </object>
      </child>
  </object>
</interface>
```

## Перемещение виджетов

С помощью метода `Move()` можно перемещать уже добавленные виджеты:

```csharp
// Перемещение button1 на новые координаты (70, 70)
fix.Move(button1, 70, 70);
```

**Источник:** [https://metanit.com/sharp/gtk/3.4.php](https://metanit.com/sharp/gtk/3.4.php)