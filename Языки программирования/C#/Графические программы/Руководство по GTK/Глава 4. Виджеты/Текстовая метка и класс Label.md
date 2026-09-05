# Текстовая метка и класс Label

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Графические программы|Графические программы]] / [[Языки программирования/C#/Графические программы/Руководство по GTK|Руководство по GTK]] / [[Языки программирования/C#/Графические программы/Руководство по GTK/Глава 4. Виджеты|Глава 4. Виджеты]] / Текстовая метка и класс Label

[[Языки программирования/C#/Графические программы/Руководство по GTK/Глава 3. Макет и позиционирование/Контейнер Fixed|Назад]] | [[Языки программирования/C#/Графические программы/Руководство по GTK/Глава 4. Виджеты|Содержание]] | [[Языки программирования/C#/Графические программы/Руководство по GTK/Глава 4. Виджеты/Кнопка Button|Вперёд]]

**Дата написания:** 05.09.2026

Класс Label в GTK предназначенный для отображения статического текста.

Для создания объекта `Label` применяется статический метод `Label.New()`, в который передается текст метки:

```csharp
Label label = Label.New("Hello World");
```

Если мы хотим создать метку, но без текста (например, для последующей динамической установки текста), то можно передать значение `null`.

Базовый пример создания метки:

```csharp
using Gtk;

var app= Application.New("com.metanit", Gio.ApplicationFlags.DefaultFlags);

app.OnActivate += (sender, _) =>
{
    var window = new Window();
    window.Title = "METANIT.COM";
    window.DefaultWidth = 250;
    window.DefaultHeight = 200;

    // Создание метки
    Label label = Label.New("Hello, GTK!");

    window.Child = label;
    window.Application = (Application) sender;
    window.Show();
};

app.RunWithSynchronizationContext(null);
```

![Текстовая метка и класс Label в GTK на языке программирования C#](./pics/2.15.png)

Определение аналогичной метки в XML:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<interface>
  <object class="GtkWindow" id="window">
    <property name="title">METANIT.COM</property>
    <property name="default-width">250</property>
    <property name="default-height">200</property>
    <child>
      <object class="GtkLabel" id="label">
        <property name="label">Hello, GTK!</property>
      </object>
    </child>
  </object>
</interface>
```

## Свойства метки

Рассмотрим базовую функциональность метка, которая представлена свойствами класса:

- Attributes: список атрибутов стиля в виде объекта `AttrList` для применения к тексту метки
- Ellipsize: предпочтительное место для многоточия строки, если в метке недостаточно места для отображения всей строки (перечисление `EllipsizeMode`)
- Justify: выравнивание строк в тексте метки относительно друг друга
- Label\_: содержимое метки (текст)
- Lines: количество строк, которым должна быть ограничен многострочный текст метки
- MaxWidthChars: желаемая максимальная ширина в символах
- NaturalWrapMode: способ переноса строк
- Selectable: можно ли выделить текст метки мышью
- SingleLineMode : является ли текст однострочным
- UseMarkup: использует ли текст метки вразметку Pango
- UseUnderline: подчеркивается ли текст
- WidthChars: желаемая ширина в символах
- Wrap: указывает, будет ли текст метки будет переноситься, если станет слишком широким
- WrapMode: управляет тем, как выполняется перенос строк
- Xalign: горизонтальное выравнивание текста метки
- Yalign: вертикальное выравнивание текста

## Текст метки

Текст метки хранится в свойстве Label\_. Установка и получение текста метки:

```csharp
label.Label_ = "Новый текст";
string currentText = label.Text;
```

В качестве альтернативы для установки текста можно использовать метод `SetText(string str)`

## Перенос текста

По умолчанию метка растягивается на такую доступную длину, которая достаточна, чтобы вместить весь ее текст. Но передав свойству Wrap значение `true`, можно установить перенос текста:

```csharp
using Gtk;

var app= Application.New("com.metanit", Gio.ApplicationFlags.DefaultFlags);

app.OnActivate += (sender, _) =>
{
    var window = new Window();
    window.Title = "METANIT.COM";
    window.DefaultWidth = 250;
    window.DefaultHeight = 200;

    // Создание метки
    Label label = Label.New(null);
    // расположение метки в верхнем левом углу
    label.Halign = Align.Start;
    label.Valign = Align.Start;
    // отступы по 10 единиц
    label.MarginTop = 10;
    label.MarginStart = 10;
    label.MarginEnd = 10;

    label.Label_ = "Ежели, положим, вы едете с охоты домой и желаете с аппетитом пообедать, " +
                    "то никогда не нужно думать об умном; умное да ученое всегда аппетит отшибает.";
    label.Wrap = true; // Включить перенос текста
    window.Child = label;
    window.Application = (Application) sender;
    window.Show();
};

app.RunWithSynchronizationContext(null);
```

![Перенос текста и класс Label в GTK на языке программирования C#](./pics/2.17.png)

Кроме того, для меток доступно свойство WrapMode, которое представляет перечисление `Pango.WrapMode` и управляет переносом слов с помощью следующих значений:

- `WrapMode.Word`: переносит текст, разрывая строки между словами (значение по умолчанию)
- `WrapMode.Char`: переносит текст, разрывая строки везде, где может появиться курсор (обычно между символами)
- `WrapMode.WordChar`: переносит текст, разрывая строки между словами или, если этого недостаточно, также между графемами

Например, в примере выше идет перенос по словам. Но установим перенос с разрывом между символами и для этого к определению метки доабвим строку:

```csharp
label.WrapMode = Pango.WrapMode.Char; // переносы между символами
```

![Перенос текста по буквам и класс Label в GTK на языке программирования C#](./pics/2.40.png)

## Выравнивание

За выравнивание метки отвечают свойства Xalign (горизонтальное выравнивание) и Yalign (вертикальное выравнивание). Оба этих свойства принимают значение типа `float` от 0.0 до 1.0. Для свойства `Xalign`: 0.0 - слева, а 1.0 - справа. Для свойства `Yalign`: 0.0 - сверху, 1.0 - снизу. 0.5 для обоих свойств устанавливает метку по центру. Например, расположим метку ближе к верхнему левому углу окнау:

```csharp
Label label = new Label("Hello, GTK");
// Горизонтальное выравнивание
label.Xalign = 0.1f; // 0.0 - слева, 1.0 - справа, 0.5 - по центру

// Вертикальное выравнивание
label.Yalign = 0.15f; // 0.0 - сверху, 1.0 - снизу, 0.5 - по центру
```

![Выравнивание и класс Label в GTK на языке программирования C#](./pics/2.16.png)

Аналог в XML:

```xml
<object class="GtkLabel" id="label">
    <property name="xalign">0.1</property>
    <property name="yalign">0.15</property>
    <property name="label">Hello, GTK</property>
</object>
```

Для выравнивания текста в классе Label определено свойство Justify. Оно представляет перечисление `Justification`, которое принимает следующие значения:

- `Justification.Left` Текст размещается по левому краю метки. Это значение по умолчанию
- `Justification.Right` Текст размещается по правому краю метки
- `Justification.Center` Текст размещается по центру метки
- `Justification.Fill` Текст размещается и распределяется по всей метке

Например, выравнивание текста по центру:

```csharp
using Gtk;

var app= Application.New("com.metanit", Gio.ApplicationFlags.DefaultFlags);

app.OnActivate += (sender, _) =>
{
    var window = new Window();
    window.Title = "METANIT.COM";
    window.DefaultWidth = 250;
    window.DefaultHeight = 200;

    Label label = Label.New(null);

    // расзмещение в верхнем левом углу с отступами в 10 единиц
    label.Halign = Align.Start;
    label.Valign = Align.Start;
    label.MarginTop = 10;
    label.MarginStart = 10;
    label.MarginEnd = 10;

    label.Wrap = true;  // установка переносов

    label.Label_ = "Ежели, положим, вы едете с охоты домой и желаете с аппетитом пообедать, " +
                    "то никогда не нужно думать об умном; умное да ученое всегда аппетит отшибает.";
    label.Justify = Justification.Center; // выравнивание по центру

    window.Child = label;
    window.Application = (Application) sender;
    window.Show();
};
```

![Выравнивание текста и класс Label в GTK на языке программирования C#](./pics/2.18.png)

Аналог в XML:

```xml
<object class="GtkLabel" id="label">
    <property name="wrap">true</property>
    <property name="justify">GTK_JUSTIFY_CENTER</property>
    <property name="label">Ежели, положим, вы едете с охоты домой и желаете с аппетитом пообедать,...</property>
</object>
```

## Форматирование текста

Класс `Label` позволяет применять форматирование к тексту. Для этого мы можем применять в тексте разметку, во многом аналогичную html. В частности, разметка должна быть допустимым XML; например, литеральные символы <, > и & должны быть экранированы как &lt;, &gt; и &amp;. Например, применим форматирование шрифта текста на метке:

```csharp
using Gtk; var app= Application.New("com.metanit", Gio.ApplicationFlags.DefaultFlags); app.OnActivate += (sender, _) => { var window = new Window(); window.Title = "METANIT.COM"; window.DefaultWidth = 250; window.DefaultHeight = 200; Label label = Label.New(null); label.Label_ = "<span font=\"Verdana 14\"><b>Hello</b></span> <span foreground=\"navy\" weight=\"bold\" font=\"Verdana 14\">METANIT.COM</span>"; label.UseMarkup = true; window.Child = label; window.Application = (Application) sender; window.Show(); }; app.RunWithSynchronizationContext(null);
```

![Форматирование текста и класс Label в GTK на языке программирования C#](./pics/2.19.png)

При форматировании передаем разметку в xml, устанавливая три атрибута метки - foreground, weight и font:

`foreground` устанавливает цвет текста (используются наименования цветов CSS). `weight` устанавливает толщину текста. Так, значение "bold" устанавливает жирный текст. А атрибуту `font` передаются название стиля шрифта и размер шрифта (можно использовать одно из этих значений)

Аналогичный пример в XML:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<interface>
  <object class="GtkWindow" id="window">
    <property name="title">METANIT.COM</property>
    <property name="default-width">300</property>
    <property name="default-height">250</property>
    <child>
      <object class="GtkLabel" id="label">
        <property name="use-markup">true</property>
        <property name="label"><span font="Verdana 14"><b>Hello</b></span> <span foreground="navy" weight="bold" font="Verdana 14">METANIT.COM</span></property>
      </object>
    </child>
  </object>
</interface>
```

## Другие полезные свойства

Свойство Selectable при значении `true` позволяет выбирать текст:

```csharp
label.Selectable = true; // Разрешить выделение текста
```

**Источник:** [https://metanit.com/sharp/gtk/4.1.php](https://metanit.com/sharp/gtk/4.1.php)