# Флажки и радиокнопки CheckButton

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Графические программы|Графические программы]] / [[Языки программирования/C#/Графические программы/Руководство по GTK|Руководство по GTK]] / [[Языки программирования/C#/Графические программы/Руководство по GTK/Глава 4. Виджеты|Глава 4. Виджеты]] / Флажки и радиокнопки CheckButton

[[Языки программирования/C#/Графические программы/Руководство по GTK/Глава 4. Виджеты/Индикатор прогресса ProgressBar|Назад]] | [[Языки программирования/C#/Графические программы/Руководство по GTK/Глава 4. Виджеты|Содержание]] | [[Языки программирования/C#/Графические программы/Руководство по GTK/Глава 4. Виджеты/Слайдер Scale|Вперёд]]

**Дата написания:** 05.09.2026

Виджет **CheckButton** представляет кнопку, которая может находиться в отмеченном или неотмеченном состоянии. В традиционном пользовательском интерфейсе этот виджет может применяться для создания таких стандартных элементов управления как флажики и радиокнопки.

Для создания этого виджета применяется один из статических методов:

```csharp
public static CheckButton New()
public static CheckButton NewWithLabel(string? label)
public static CheckButton NewWithMnemonic(string? label)
```

Второй и третий методы в качестве параметра принимают текст, который будет отображаться рядом с кнопкой. При этом третий метод также устанавливает мнемонику для быстрого доступа к виджету - в качестве мнемоники применяется первая буква текста.

Создадим простейший CheckButton, используя второй метод:

```csharp
using Gtk;

var app= Application.New("com.metanit", Gio.ApplicationFlags.DefaultFlags);

app.OnActivate += (sender, _) =>
{
    var window = new Window();
    window.Title = "METANIT.COM";
    window.DefaultWidth = 250;
    window.DefaultHeight = 200;

     // создаем флажок
    CheckButton checkBox = CheckButton.NewWithLabel("Включено");

    // размещаем виджет по верхней границе
    checkBox.Valign = Align.Start;

    window.Child = checkBox;
    window.Application = (Application) sender;
    window.Show();
};

app.RunWithSynchronizationContext(null);
```

![Виджет GtkCheckButton в GTK и C#](./pics/3.27.png)

Определение аналогичной кнопки в XML:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<interface>
  <object class="GtkWindow" id="window">
    <property name="title">METANIT.COM</property>
    <property name="default-width">250</property>
    <property name="default-height">200</property>
    <child>
        <object class="GtkCheckButton" id="checkBox">
          <property name="label">Включено</property>
          <property name="valign">GTK_ALIGN_START</property>
        </object>
    </child>
  </object>
</interface>
```

## Свойства виджета

Вкратце рассмотрим функционал виджета. Основные свойства:

- Child: дочерний виджет
- Label: текст кнопки
- Group: группа кнопки
- Active: является ли кнопка отмеченной

Разберем вкратце основной функционал виджета.

## Выбор CheckButton

Как было сказано выше, виджет CheckButton может пребывать в отмеченном или неотмеченном состоянии. Для выделения кнопки свойству `Active` передается значение `true`

```csharp
CheckButton checkBox = CheckButton.NewWithLabel("Включено");
checkBox.Active = true;
```

![Выделяем виджет GtkCheckButton в GTK и C#](./pics/3.28.png)

В XML для отметки кнопки надо установить свойство active:

```xml
<object class="GtkCheckButton" id="checkBox">
    <property name="active">1</property>
    ..........................
</object>
```

## Установка содержимого

GTK предоставляет нам виджет CheckButton с некоторой базовой функциональностью. Так, метка кнопкиа имеет определенный шрифт и прочие характеристики. Однако, возможно, потребуется изменить эти характеристи как-то по своему. И GTK позволяет изименить содержимое кнопки - в частности, его метку, которая отображает текст. Для этого предназначено свойство `Child`. Например, изменим метку виджета:

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
    label.Label_ = "<span font=\"15\">active</span>";
    label.UseMarkup = true;

    CheckButton checkBox = CheckButton.NewWithLabel("Включено");
    checkBox.Valign = Align.Start;
    checkBox.Child = label;

    window.Child = checkBox;
    window.Application = (Application) sender;
    window.Show();
};

app.RunWithSynchronizationContext(null);
```

![Настройка виджета CheckButton в GTK и C#](./pics/3.30.png)

Аналогичная кнопка в XML:

```xml
<object class="GtkCheckButton" id="checkBox">
    <property name="valign">GTK_ALIGN_START</property>
    <child>
        <object class="GtkLabel" id="label">
            <property name="use-markup">true</property>
            <property name="label"><span font="15">active</span></property>
        </object>
    </child>
</object>
```

## Обработка переключения кнопки

При выбора виджета CheckButton или, наоборот, при снятии отметки GTK генерирует событие **OnToggled**:

```csharp
public event SignalHandler<CheckButton> OnToggled
```

Соответственно, если нам надо обработать изменение состояния виджета, то мы можем обрабатывать это событие:

```csharp
using Gtk;

const string ON = "Включено";
const string OFF = "Выключено";

var app= Application.New("com.metanit", Gio.ApplicationFlags.DefaultFlags);

app.OnActivate += (sender, _) =>
{
    var window = new Window();
    window.Title = "METANIT.COM";
    window.DefaultWidth = 250;
    window.DefaultHeight = 200;

    // по умолчанию кнопка отображает строку OFF
    Label label = Label.New(OFF);

    CheckButton checkBox = CheckButton.NewWithLabel("Включено");
    checkBox.Valign = Align.Start;
    checkBox.Child = label;
    // устанавливаем обработчик события OnToggled
    checkBox.OnToggled +=(sender, _) =>{
        if(sender.Active) label.Label_ = ON;
        else label.Label_ = OFF;
    };

    window.Child = checkBox;
    window.Application = (Application) sender;
    window.Show();
};

app.RunWithSynchronizationContext(null);
```

Для переключения текста при переключении состояния виджета определены две константы - ON и OFF. В обработчике события `OnToggled` в зависимости от состояния виджета устанавливаем для ее метки определенный текст:

```csharp
checkBox.OnToggled +=(sender, _) =>{
    if(sender.Active) label.Label_ = ON;
    else label.Label_ = OFF;
};
```

![Обработка перелючения флажка CheckButton в GTK и C#](./pics/3.29.png)

## Создание группы радиокнопок

Виджет **CheckButton** также позволяет создать группу радиокнопок - по сути набор кнопок, где пользователь одномоментно может выбрать только одну кнопку. Чтобы создать подобную группу кнопок, надо использовать свойство **Group**:

```csharp
public CheckButton? Group { set; }
```

Причем значение этого свойства представляет кнопку, на который проецируется вся группа. Рассмотрим небольшой пример:

```csharp
using Gtk;

var app= Application.New("com.metanit", Gio.ApplicationFlags.DefaultFlags);

app.OnActivate += (sender, _) =>
{
    var window = new Window();
    window.Title = "METANIT.COM";
    window.DefaultWidth = 250;
    window.DefaultHeight = 200;

    Box box =  Box.New(Orientation.Vertical, 10);
    box.Halign = Align.Start;

    // кнопка, на которую проецируется вся группа
    CheckButton langs = CheckButton.New();

    // создаем кнопки для выбора
    CheckButton java = CheckButton.NewWithLabel("Java");
    CheckButton csharp = CheckButton.NewWithLabel("C#");
    CheckButton python = CheckButton.NewWithLabel("Python");

    // добавляем кнопки в GtkBox
    box.Append(java);
    box.Append(csharp);
    box.Append(python);

    // добавляем кнопки в группу langs
    java.Group = langs;
    csharp.Group = langs;
    python.Group = langs;

    window.Child = box;
    window.Application = (Application) sender;
    window.Show();
};

app.RunWithSynchronizationContext(null);
```

Здесь вначале создаем кнопку, с которой будет ассоциироваться группа радиокнопок:

```csharp
CheckButton langs = CheckButton.New();
```

Далее создаем собственно те радиокнопки, которые будут входить в эту группу и из которых мы можем выбрать одну:

```csharp
CheckButton java = CheckButton.NewWithLabel("Java");
CheckButton csharp = CheckButton.NewWithLabel("C#");
CheckButton python = CheckButton.NewWithLabel("Python");
```

Добавляем эти кнопки в контейнер GtkBox и затем добавляем их в группу langs:

```csharp
java.Group = langs;
csharp.Group = langs;
python.Group = langs;
```

Таким образом, мы получим группу кнопок, где мы сможем выбрать только одну из них:

![Радиокнопки CheckButton в GTK и C#](./pics/3.31.png)

Определение аналогичного набора кнопок в XML:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<interface>
  <object class="GtkWindow" id="window">
    <property name="title">METANIT.COM</property>
    <property name="default-width">250</property>
    <property name="default-height">200</property>

    <child>
        <object class="GtkBox" id="box">
          <property name="valign">GTK_ALIGN_START</property>
          <property name="spacing">10</property>
          <property name="orientation">vertical</property>
          <child>
            <object class="GtkCheckButton" id="langs"></object>
            <object class="GtkCheckButton" id="java">
              <property name="label">Java</property>
              <property name="group">langs</property>
            </object>
          </child>
          <child>
            <object class="GtkCheckButton" id="csharp">
              <property name="label">C#</property>
              <property name="group">langs</property>
            </object>
          </child>
          <child>
            <object class="GtkCheckButton" id="python">
              <property name="label">Python</property>
              <property name="group">langs</property>
            </object>
          </child>
        </object>
    </child>
  </object>
</interface>
```

### Обработка выбора радиокнопки

Теперь посмотрим, как мы можем отследить выбранную кнопку:

```csharp
using Gtk;

var app= Application.New("com.metanit", Gio.ApplicationFlags.DefaultFlags);

Label label = Label.New(null);
// создаем кнопки для выбора
CheckButton java = CheckButton.NewWithLabel("Java");
CheckButton csharp = CheckButton.NewWithLabel("C#");
CheckButton python = CheckButton.NewWithLabel("Python");

app.OnActivate += (sender, _) =>
{
    var window = new Window();
    window.Title = "METANIT.COM";
    window.DefaultWidth = 250;
    window.DefaultHeight = 200;

    Box box =  Box.New(Orientation.Vertical, 10);
    box.Halign = Align.Start;

    // кнопка, на которую проецируется вся группа
    CheckButton langs = CheckButton.New();

    box.Append(label);
    box.Append(java);
    box.Append(csharp);
    box.Append(python);

    // добавляем кнопки в группу langs
    java.Group = langs;
    csharp.Group = langs;
    python.Group = langs;

    // добавляем обработчик события OnToggled для всех кнопок обоработчик
    csharp.OnToggled += Selected;
    java.OnToggled += Selected;
    python.OnToggled += Selected;

    window.Child = box;
    window.Application = (Application) sender;
    window.Show();
};

app.RunWithSynchronizationContext(null);
```

void Selected (CheckButton sender, EventArgs args){

```csharp
    // если кнопка активна (в отмеченном состоянии)
    if(csharp.Active) label.Label_ = "C#";
    else if(java.Active) label.Label_ = "Java";
    else if(python.Active) label.Label_ = "Python";
}
```

Здесь при запуске приложения для каждой кнопки в качестве обработчика события OnToggled устанавливается метод Selected:

```csharp
csharp.OnToggled += Selected;
java.OnToggled += Selected;
python.OnToggled += Selected;
```

В обработчике проверяем состояние кнопки - если она выбрана, то устанавливаем соответствующий текст на метке:

```csharp
void Selected (CheckButton sender, EventArgs args){
    // если кнопка активна (в отмеченном состоянии)
    if(csharp.Active) label.Label_ = "C#";
    else if(java.Active) label.Label_ = "Java";
    else if(python.Active) label.Label_ = "Python";
}
```

Причем стоит отметить, что этот метод срабатывает два раза - для кнопки, которая теряет выбор, и для кнопки которая получает выбор и становится активной. В результате при выборе одной из кнопок метка будет отображать соответствующий текст:

![Выбор радиокнопок CheckButton в GTK и C#](./pics/3.32.png)

**Источник:** [https://metanit.com/sharp/gtk/4.9.php](https://metanit.com/sharp/gtk/4.9.php)