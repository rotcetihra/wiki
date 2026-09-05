# Кнопка Button

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Графические программы|Графические программы]] / [[Языки программирования/C#/Графические программы/Руководство по GTK|Руководство по GTK]] / [[Языки программирования/C#/Графические программы/Руководство по GTK/Глава 4. Виджеты|Глава 4. Виджеты]] / Кнопка Button

[[Языки программирования/C#/Графические программы/Руководство по GTK/Глава 4. Виджеты/Текстовая метка и класс Label|Назад]] | [[Языки программирования/C#/Графические программы/Руководство по GTK/Глава 4. Виджеты|Содержание]] | [[Языки программирования/C#/Графические программы/Руководство по GTK/Глава 4. Виджеты/Однострочное текстовое поле Entry|Вперёд]]

**Дата написания:** 05.09.2026

Класс Button в GTK представляет кнопку - один из основных виджетов, используемых для создания интерактивных элементов пользовательского интерфейса. Кнопки позволяют пользователям взаимодействовать с приложением, выполняя определенные действия при нажатии.

Для создания кнопки применяется ряд статических методов:

- Button.New()
  Создает новый виджет Button без текста и иконки.
- Button.NewFromIconName(string iconName)
  Создает новую кнопку с определенной иконкой.
- Button.NewWithMnemonic(string label)
  Создает с определенной мнемоникой.
- Button.NewWithLabel(string label)
  Создает кнопку с определенным текстом, который передается через параметр

Создание простейшей кнопки:

```csharp
using Gtk;

var app= Application.New("com.metanit", Gio.ApplicationFlags.DefaultFlags);

app.OnActivate += (sender, _) =>
{
    var window = new Window();
    window.Title = "METANIT.COM";
    window.DefaultWidth = 250;
    window.DefaultHeight = 200;

    // создаем кнопку
    var button = Button.NewWithLabel("Click Me");

    window.Child = button;
    window.Application = (Application) sender;
    window.Show();
};

app.RunWithSynchronizationContext(null);
```

![Создание простейшей кнопки в GTK на языке программирования C#](./pics/1.7.png)

Определение аналогичной кнопки в XML (файл "builder.ui"):

```xml
<?xml version="1.0" encoding="UTF-8"?>
<interface>
  <object class="GtkWindow" id="window">
    <property name="title">METANIT.COM</property>
    <property name="default-width">250</property>
    <property name="default-height">200</property>
    <child>
      <object class="GtkButton" id="button">
        <property name="label">Click Me</property>
      </object>
    </child>
  </object>
</interface>
```

При создании кнопки необязательно тут же указывать текст. Кроме того, в любой момент мы можем изменить текст с помощью свойства Label:

```csharp
var button = Button.New();  // кнопка без текста
button.Label = "Hello";
```

## Обработка нажатия

Ключевым моментом кнопок является их способность реагировать на нажатия. Для этого у класса Button определено событие OnClicked:

```csharp
public event SignalHandler<Button> OnClicked
```

Обработчик этого события должен соответствовать сигнатуре ковариантного делегата SignalHandler:

```csharp
delegate void SignalHandler<in TSender>(TSender sender, EventArgs args) where TSender : Object
```

Где параметр `sender` - объект, который отправляет событие, а параметр `args` - дополнительные данные типа `EventArgs`, которые передаются с событием.

Например, обработаем нажатие кнопки:

```csharp
using Gtk;

var app= Application.New("com.metanit", Gio.ApplicationFlags.DefaultFlags);

app.OnActivate += (sender, _) =>
{
    var window = new Window();
    window.Title = "METANIT.COM";
    window.DefaultWidth = 250;
    window.DefaultHeight = 200;

    var button = Button.NewWithLabel("Click Me");
    // обработка события кнопки
    button.OnClicked += (_, _) =>
    {
        Console.WriteLine("Button clicked");
    };
    window.Child = button;
    window.Application = (Application) sender;
    window.Show();
};

app.RunWithSynchronizationContext(null);
```

В данном случае обработчик нажатия кнопки представляет лямбда-выражение, которое выводит уведомление на консоль

## Изображение кнопки

С помощью статического метода `Button.NewFromIconName()` можно создать кнопку с определенной иконкой. Также иконку можно установить с помощью свойства IconName. Но следует учитывать, что применяются предустановленные иконки из папки "usr/share/icons". Например:

```csharp
var button = Button.NewFromIconName("document-new-symbolic");
```

Здесь используется иконка из файла "document-new-symbolic.svg". В итоге получится следующая кнопка:

![Создание кнопки с картинкой в GTK на языке программирования C#](./pics/1.8.png)

## Установка обработчика сигнала в XML

Если кнопка определяется в XML, нам надо получить кнопку в коде C# и там же подключить к ней обработчик события OnClicked. Например, код в XML (файл "builder.ui"):

```xml
<?xml version="1.0" encoding="UTF-8"?>
<interface>
  <object class="GtkWindow" id="window">
    <property name="title">METANIT.COM</property>
    <property name="default-width">250</property>
    <property name="default-height">200</property>
    <child>
      <object class="GtkButton" id="button">
        <property name="label">Click Me</property>
      </object>
    </child>
  </object>
</interface>
```

И в основном файле приложения, где загружается интерфейс, получаем кнопку и прикрепляем к ней обработчик сигнала:

```csharp
using Gtk;

var app= Application.New("com.metanit", Gio.ApplicationFlags.DefaultFlags);

app.OnActivate += (sender, _) =>
{
    Builder builder = Builder.NewFromFile("builder.ui");
    Window? window = (Window?) builder.GetObject("window");
    if(window is null) return;
    // получаем кнопку
    Button? button = (Button?) builder.GetObject("button");
    if(button is null) return;
    // прикрепляем обработчик нажатия
    button.OnClicked += Button_Click;

    window.Application = (Application) sender;
    window.Show();
};

app.RunWithSynchronizationContext(null);
```

// обработчик нажатия кнопки

```csharp
void Button_Click(Button sender, EventArgs e)
{
    Console.WriteLine("Button clicked");
};
```

**Источник:** [https://metanit.com/sharp/gtk/4.2.php](https://metanit.com/sharp/gtk/4.2.php)