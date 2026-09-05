# Класс Builder. Обращение к XML в коде С#

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Графические программы|Графические программы]] / [[Языки программирования/C#/Графические программы/Руководство по GTK|Руководство по GTK]] / [[Языки программирования/C#/Графические программы/Руководство по GTK/Глава 2. Определение интерфейса в XML|Глава 2. Определение интерфейса в XML]] / Класс Builder. Обращение к XML в коде С#

[[Языки программирования/C#/Графические программы/Руководство по GTK/Глава 2. Определение интерфейса в XML/Определение XML|Назад]] | [[Языки программирования/C#/Графические программы/Руководство по GTK/Глава 2. Определение интерфейса в XML|Содержание]] | [[Языки программирования/C#/Графические программы/Руководство по GTK/Глава 3. Макет и позиционирование/Позиционирование виджетов|Вперёд]]

**Дата написания:** 05.09.2026

Для работы с интерфейсом XML в C# предназначен класс Builder, который выполняет парсинг текстового описания пользовательского интерфейса в формате XML.

Для создания объекта `Builder` применяется конструктор, который принимает название файла-ресурса:

```csharp
public Builder(string embeddedTemplateName)
```

Но кроме конструктора есть также ряд статических методов, которые создают объект Builder:

- Builder.New(): создает новый пустой объект Builder
- Builder.NewFromFile(): создает новый объект Builder по определению из файла, путь к которому передается в метод.

```csharp
public static Builder NewFromFile(string filename)
```

Причем файл не является встроенным ресурсом и может располагаться в произвольном месте файловой системы, а в метод передается путь к нему

- Builder.NewFromResource(): создает новый объект Builder по определению из ресурса, путь к которому передается в метод.

```csharp
public static Builder NewFromResource(string resourcePath)
```

- Builder.NewFromString(): создает новый объект Builder по определению из строки, которая передается в метод.

```csharp
public static Builder NewFromString(string @string, nint length)
```

Если добавить описания пользовательского интерфейса из нескольких источников в один и тот же Builder, можно создать объект Builder с помощью вызова `Builder.New()` или одного из других выше описанных методов, а затем выполнить один или неколько вызовов следующих методов:

- AddFromFile(): добавляет определение из файла, путь к которому передается в метод.

```csharp
public bool AddFromFile(string filename)
```

- AddFromResource(): создает новый объект Builder по определению из ресурса.

```csharp
public bool AddFromResource(string resourcePath)
```

- AddFromString(): создает новый объект Builder по определению из строки, которая передается в функцию.

```csharp
public bool AddFromString(string buffer, nint length)
```

В качестве возвращаемого результата все эти методы возвращают `true` в случае успешного выполнения и `false` при ошибке.

## Получение объектов из Builder

Builder хранит ссылку на все объекты, которые он сконструировал. Для доступа к виджетам в интерфейсе по id можно использовать функцию GetObject() и GetPointer(). Метод GetObject() принимает идентификатор объекта в виде строки и возвращает соответствующий объект:

```csharp
public Object? GetObject(string name)
```

Метод GetPointer() также принимает идентфиикатор объекта и возвращает указатель на объект в виде значения `nint`:

```csharp
public nint GetPointer(string name)
```

## Определение интерфейса в строке

Определение интерфейса по файле XML рассматривалось в прошлых статьях, поэтому посмотрим вкратце определение интерфейса в виде простой строки:

```csharp
using Gtk;

var app= Application.New("com.metanit", Gio.ApplicationFlags.DefaultFlags);

// определение интерфейса
string xml = """
        <?xml version="1.0" encoding="UTF-8"?>
            <interface>
            <object class="GtkWindow" id="window">
                <property name="title">METANIT.COM</property>
                <property name="default-width">250</property>
                <property name="default-height">200</property>
            </object>
        </interface>
        """;

app.OnActivate += (sender, _) =>
{
    Builder builder = Builder.NewFromString(xml, xml.Length);
    Window? window = (Window?) builder.GetObject("window");
    if(window is null) return;

    window.Application = (Application) sender;
    window.Show();
};

app.RunWithSynchronizationContext(null);
```

В данном случае определение интерфейса определено в переменной xml, которая передается в метод `Builder.NewFromString()`. В качестве второго параметра передается длина строки

## Загрузка интерфейса из нескольких источников

Рассмотрим другую ситуацию, когда нам надо загрузить определение интерфейса из нескольких источников. Например, у нас есть несколько файлов с определением интерфейса, где мы независимо друг от друга создаем несколько отдельных компонентов и теперь решили использовать их в одном приложении. Для примера определим следующий файл builder.ui:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<interface>
  <object class="GtkWindow" id="window">
    <property name="title">METANIT.COM</property>
    <property name="default-width">250</property>
    <property name="default-height">200</property>
  </object>
</interface>
```

Используем этот файл в качестве одного из источников:

```csharp
using Gtk;

var app= Application.New("com.metanit", Gio.ApplicationFlags.DefaultFlags);

app.OnActivate += (sender, _) =>
{
    // определение интерфейса метки Label
    const string xml_label = """
        <interface>
            <object class="GtkLabel" id="label">
                <property name="label">Hello Work</property>
            </object>
        </interface>
    """;
    // Создаем объект GtkBuilder и загружаем определение интерфейса из файла
    Builder builder = Builder.NewFromFile("builder.ui");
    // загружаем определение интерфейса из xml_label
    builder.AddFromString(xml_label, xml_label.Length);

    // получаем объект Window по идентификатору "window"
    Window? window = (Window?) builder.GetObject("window");
    if(window is null) return;

    Label? label = (Label?) builder.GetObject("label");
    if(label is null) return;

    // добавляем Label в Window программным образом
    window.Child = label;

    window.Application = (Application) sender;
    window.Show();
};

app.RunWithSynchronizationContext(null);
```

Для примера Builder создается по файлу "builder.ui", а затем добавляет определение интерфейса из константы xml\_label. С помощью метода `GetObject()` можно получить объекты через их идентификаторы из обоих определений и некоторым образом использовать их. Так, в данном случае получаем `Label` и добавляем этот объект в окно приложения:

```csharp
// получаем объект Window по идентификатору "window"
    Window? window = (Window?) builder.GetObject("window");
    if(window is null) return;

    Label? label = (Label?) builder.GetObject("label");
    if(label is null) return;

    // добавляем Label в Window программным образом
    window.Child = label;
```

![Добавление виджетов из xml в приложение GTK и C#](./pics/4.3.png)

**Источник:** [https://metanit.com/sharp/gtk/2.3.php](https://metanit.com/sharp/gtk/2.3.php)