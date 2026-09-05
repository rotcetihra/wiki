# Класс Builder и загрузка XML

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Графические программы|Графические программы]] / [[Языки программирования/C#/Графические программы/Руководство по GTK|Руководство по GTK]] / [[Языки программирования/C#/Графические программы/Руководство по GTK/Глава 2. Определение интерфейса в XML|Глава 2. Определение интерфейса в XML]] / Класс Builder и загрузка XML

[[Языки программирования/C#/Графические программы/Руководство по GTK/Глава 1. Введение в GTK/Введение в виджеты|Назад]] | [[Языки программирования/C#/Графические программы/Руководство по GTK/Глава 2. Определение интерфейса в XML|Содержание]] | [[Языки программирования/C#/Графические программы/Руководство по GTK/Глава 2. Определение интерфейса в XML/Определение XML|Вперёд]]

**Дата написания:** 05.09.2026

Если код приложения небольшой, то его можно удобно накидать непосредственно в файле кода на C#, но при создании более сложного пользовательского интерфейса с десятками или сотнями виджетов к од определения интерфейса становится громоздким, а внесение изменений становится практически невозможным. К счастью, GTK поддерживает разделение макета пользовательского интерфейса от бизнес-логики, используя описания пользовательского интерфейса в формате XML. А для загрузки этого интерфейса в программу применяется класс Builder.

Например, возьмем код приложения из прошлых статей:

```csharp
using Gtk;

var app= Application.New("com.metanit", Gio.ApplicationFlags.DefaultFlags);

app.OnActivate += (sender, args) =>
{
    Window window = new Window();  // Создаем новое окно
    window.Title = "METANIT.COM";  // Устанавливаем заголовок окна

    window.DefaultWidth = 250;      // Устанавливаем начальную ширину окна
    window.DefaultHeight = 200;     // Устанавливаем начальную высоту окна

    // Свойство Application окна указывает на текущий объект приложения
    window.Application = (Gtk.Application) sender;

    window.Show();    // Отображаем окно на экране
};

return app.RunWithSynchronizationContext(null);
```

Возьмем тот код, который касается определения интерфейса окна:

```csharp
Window window = new Window();  // Создаем новое окно
window.Title = "METANIT.COM";  // Устанавливаем заголовок окна

window.DefaultWidth = 250;      // Устанавливаем начальную ширину окна
window.DefaultHeight = 200;     // Устанавливаем начальную высоту окна
```

Если формализовать процесс определения интерфейса, то мы определяем визуальный объект (в нашем случае окно) и затем устанавливаем некоторые свойства, которые определяют различные аспекты визуального компонента (в данном случае заголовок, ширина и высота окна). Теперь посмотрим, как нам создать такой же объект, только в xml.

Пусть у нас будет файл builder.ui со следующим кодом:

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

Файл начинается со стандартного для xml-файлов элемента xml, который устанавливает версию и кодировку. А весь интерфейс представляет пустое окно. Обратите внимание на название класса (атрибут `class="GtkWindow"`) - здесь он называется "GtkWindow", то есть с учетом названия пространства имен без точки.

Теперь нам надо указать данный файл в качестве ресурса проекта. Для этого откроем главный файл проекта, который называется по типу `[название_проекта].csproj`. Например, в моем случае это файл "gtkapp.csproj". После добавления пакета "GirCore" этот файл имеет примерно следующее определение:

```xml
<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>net9.0</TargetFramework>
    <ImplicitUsings>enable</ImplicitUsings>
    <Nullable>enable</Nullable>
  </PropertyGroup>

  <ItemGroup>
    <PackageReference Include="GirCore.Gtk-4.0" Version="0.6.3" />
  </ItemGroup>

</Project>
```

И внутри элемента `<Project>`, например, в конце добавим новый элемент:

```xml
<ItemGroup>
    <EmbeddedResource Include="builder.ui">
      <LogicalName>builder.ui</LogicalName>
    </EmbeddedResource>
</ItemGroup>
```

В данном случае встраиваем файл "builder.ui" в проект в качестве внутреннего ресурса и далее в программе будем ссылаться на него через имя "builder.ui". То есть в итоге файл проекта будет выглядеть следующим образом:

```xml
<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>net9.0</TargetFramework>
    <ImplicitUsings>enable</ImplicitUsings>
    <Nullable>enable</Nullable>
  </PropertyGroup>

  <ItemGroup>
    <PackageReference Include="GirCore.Gtk-4.0" Version="0.6.3" />
  </ItemGroup>

  <ItemGroup>
    <EmbeddedResource Include="builder.ui">
      <LogicalName>builder.ui</LogicalName>
    </EmbeddedResource>
  </ItemGroup>

</Project>
```

Далее в файле кода Program.cs определелим слеудющий код

```csharp
using Gtk;

var app= Application.New("com.metanit", Gio.ApplicationFlags.DefaultFlags);

app.OnActivate += (sender, _) =>
{
    // Создаем объект Builder и загружаем определение интерфейса из файла builder.ui
    Builder builder = new Builder("builder.ui");

    // получаем объект GtkWindow по идентификатору "window"
    Window? window = (Window?) builder.GetObject("window");

    // если null, выходим из программы
    if(window is null) return;

    // устанавливаем окно приложения
    window.Application = (Application) sender;

    // Отображаем окно на экране
    window.Show();
};

app.RunWithSynchronizationContext(null);
```

Вначале создаем объект Builder с помощью конструктора, в который передается путь к файлу с определением интерфейса

```csharp
Builder builder = new Builder("builder.ui");
```

Важно, что этот файл определен как ресурс, как было сделано выше, а не просто лежит в папке проекта.

Затем получаем объект Window по идентификатору "window" с помощью метода `GetObject()`:

```csharp
Window? window = (Window?) builder.GetObject("window");
```

В метод передается идентификатор объекта из xml (в нашем случае идентификатор окна - "window")

Стоит учитывать, что метод `GetObject()` возвращает значение типа `Object?`. То есть это может быть любой объект либого типа или даже `null`. Мы знаем, что у нас в интерфейсе по идентификатору "window" определен объект GtkWindow, который в C# соответствует классу Window. И мы можем преобразовать полученный объект к типу Window и тем самым получить определение окна. Однако теоретически метод может возвратить и `null` (например, передан некорректный идентификатор). В этом случае мы можем проверить на null:

```csharp
if(window is null) return;
```

Что делать в случае, если передан `null`? Могут быть варианты. В данном случае просто выходим из обработчика события, тем самым окно не создается, приложение завершается. Однако в качестве альтурнативы мы могли бы создавать какое-то окно по умолчанию, либо использовать какую-нибудь другую логику.

Далее идут стандартные действия: gолучив окно, устанавливаем его в качестве главного окна приложения:

```csharp
window.Application = (Application) sender;
```

Дальше отображаем окно, и пользователь может взаимодействовать с приложением.

![Определение интерфейса в xml и GtkBuilder в GTK](./pics/1.4.png)

Таким образом мы отделяем построение интерфейса от собственно кода. В данном случае, конечно, мы имеем дело с простейшим интерфейсом, но по мере увеличения сложности интерфейса, увеличения количества визуальных компонентов соответственно будет увеличиваться выгола от подобного разделения.

**Источник:** [https://metanit.com/sharp/gtk/2.1.php](https://metanit.com/sharp/gtk/2.1.php)