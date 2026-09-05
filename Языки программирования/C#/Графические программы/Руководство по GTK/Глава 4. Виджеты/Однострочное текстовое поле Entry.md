# Однострочное текстовое поле Entry

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Графические программы|Графические программы]] / [[Языки программирования/C#/Графические программы/Руководство по GTK|Руководство по GTK]] / [[Языки программирования/C#/Графические программы/Руководство по GTK/Глава 4. Виджеты|Глава 4. Виджеты]] / Однострочное текстовое поле Entry

[[Языки программирования/C#/Графические программы/Руководство по GTK/Глава 4. Виджеты/Кнопка Button|Назад]] | [[Языки программирования/C#/Графические программы/Руководство по GTK/Глава 4. Виджеты|Содержание]] | [[Языки программирования/C#/Графические программы/Руководство по GTK/Глава 4. Виджеты/Обработка изменения свойств виджетов|Вперёд]]

**Дата написания:** 05.09.2026

Класс `Entry` в GTK представляет однострочное текстовое поле, которое позволяет пользователям вводить и редактировать текст. Это один из наиболее часто используемых виджетов в графических интерфейсах пользователя для ввода данных.

Для создания текстового поля Entry применяются две статические функции:

```csharp
public static Entry New();
public static Entry NewWithBuffer(EntryBuffer buffer);
```

Вторая функция принимает буфер в виде объекта `EntryBuffer`, в который добавляются вводимые символы.

Пример простейшего текстового поля:

```csharp
using Gtk;

var app= Application.New("com.metanit", Gio.ApplicationFlags.DefaultFlags);

app.OnActivate += (sender, _) =>
{
    var window = new Window();
    window.Title = "METANIT.COM";
    window.DefaultWidth = 250;
    window.DefaultHeight = 200;

    Entry entry = Entry.New();
    entry.Valign = Align.Start;

    window.Child = entry;
    window.Application = (Application) sender;
    window.Show();
};

app.RunWithSynchronizationContext(null);
```

![Текстовое поле Entry в GTK на языке программирования C#](./pics/2.20.png)

Определение аналогичного текстового поля в XML:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<interface>
  <object class="GtkWindow" id="window">
    <property name="title">METANIT.COM</property>
    <property name="default-width">250</property>
    <property name="default-height">200</property>
    <child>
      <object class="GtkEntry" id="text_box">
        <property name="valign">GTK_ALIGN_START</property>
      </object>
    </child>
  </object>
</interface>
```

## Основные свойства Entry

Класс `Entry` предоставляет множество свойств для настройки его внешнего вида и поведения:

- Attributes: список применяемых атрибутов Pango (объект `AttrList`).
- Buffer: буфер EntryBuffer, который фактически хранит текст.
- InvisibleChar: Замещающий символ для скрытого текста (по умолчанию "*")
- InvisibleCharSet : установлен ли невидимый символ для Entry.
- MaxLength: Максимальная длина ввода (0 - без ограничений)
- OverwriteMode: перезаписывается ли текст при вводе в Entry.
- TextLength: Длина текста в Entry.
- Visibility: булевое свойство, указывает на видимость вводимых символов (например, при вводе паролей). При значении `false` символы скрываются
- Alignment: Выравнивание текста, принимает значения: 0.0 (выравнивание слева), 1.0 (выравнивание справа), 0.5 - выравнивание по центру
- IsEditable: булевое свойство, которое указывает, разрешен ли редактирования (если равно `true`, то разрешено)
- PlaceholderText: текст-подсказка для ввода, которая отображается, когда в поле нет текста

И также стоит отметить ряд свойств, которые унаследованы от базового типа **Editable**:

- Editable: можно ли редактировать содержимое виджета
- EnableUndo: должны ли быть включены отмена/повтор для редактируемого элемента
- MaxWidthChars: максимальная ширина в символах
- Text\_: текст поля
- WidthChars: количество символов, для которых нужно оставить место в виджете
- Xalign: горизонтальное выравнивание от 0 (слева) до 1 (справа)

## Установка/получение текста

Получение и установка текста для текстового поля являются одними из распространенных задач при работе с полем ввода. И здесь мы можем использовать свойство Text\_. Рассмотрим простое приложение, где по нажатию на кнопку введенный текст передается на метку:

```csharp
using Gtk;

var app= Application.New("com.metanit", Gio.ApplicationFlags.DefaultFlags);

Entry entry = Entry.New();
Label label = Label.New(null);

app.OnActivate += (sender, _) =>
{
    var window = new Window();
    window.Title = "METANIT.COM";
    window.DefaultWidth = 250;
    window.DefaultHeight = 200;

    Box box =  Box.New(Orientation.Vertical, 10);
    box.Valign = Align.Start; // выравнивание по верхнему краю

    // устанавливаем текст по умолчанию
    string text = "Hello";
    entry.Text_ = text;
    label.Label_ = text;

    // кнопка для установки текста из Entry в Label
    Button button = Button.NewWithLabel("Set");
    // подключаем обработчик кнопки
    button.OnClicked +=Button_Click;

    box.Append(entry);
    box.Append(label);
    box.Append(button);

    window.Child = box;
    window.Application = (Application) sender;
    window.Show();
};

app.RunWithSynchronizationContext(null);
```

void Button_Click(Button sender, EventArgs e)

```csharp
{
    // получаем текст из текстового поля и передаем метке
    label.Label_ = entry.Text_;
}
```

Отмечу основные моменты. Прежде всего для упрощения кода метка и текстовое поле определены как глобальные переменные. При запуске приложения создаем текстовое поле и текстовую метку и устанавливаем для них текст по умолчанию:

```csharp
string text = "Hello";
entry.Text_ = text;
label.Label_ = text;
```

Для кнопки устанавливаем обработчик сигнала нажатия:

```csharp
button.OnClicked +=Button_Click;
```

В обработчике нажатия - функции Button_Click получаем введенный текст и передаем его в текстовую метку:

```csharp
void Button_Click(Button sender, EventArgs e)
{
    // получаем текст из текстового поля и передаем метке
    label.Label_ = entry.Text_;
}
```

Таким образом, после ввода текста в текстовое поле и нажатия на кнопку этот текст также отобразится на метке:

![получение введенного текста в Entry в GTK и C#](./pics/2.41.png)

Определение аналогичного интерфейса в XML:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<interface>
  <object class="GtkWindow" id="window">
    <property name="title">METANIT.COM</property>
    <property name="default-width">250</property>
    <property name="default-height">200</property>
    <child>
        <object class="GtkBox">
          <property name="orientation">vertical</property>
          <property name="spacing">10</property>
          <child>
              <object class="GtkEntry" id="entry">
                <property name="text">Hello</property>
              </object>
          </child>
          <child>
              <object class="GtkLabel" id="label"/>
          </child>
          <child>
              <object class="GtkButton" id="button">
                <property name="label">Set</property>
              </object>
          </child>
        </object>
    </child>
  </object>
</interface>
```

## Текст-подсказка

Для установки текста-подсказки, который отображается при отсутствии ввода, применяется свойство `PlaceholderText`:

```csharp
Entry text_box = Entry.New();
text_box.PlaceholderText = "Введите текст";
```

![плейсхолдер в текстовом поле ввода Entry в GTK b C#](./pics/2.43.png)

## Выравнивание

В зависимости от письменности может различаться направление письма. Например, в европейсиких и многих других языках применяется левостороннее письмо с направлением слева направо. Однако в ряде языков, как в арабском, фарси и т.д. применяется правостороннее письмо. Для управления направлением текста GTK предоставляет свойство `Xalign`. Это свойство принимает значение типа `float` - от 0 (выравнивание слева) до 1 (выравнивание справа). Например

```csharp
Entry entry = Entry.New();
entry.Xalign = 1; // выравнивание справа
```

![правостороннее письмо в Entry в GTK и C#](./pics/2.44.png)

## Максимальная длина текста

Свойство `MaxLength` позволяет установить и получить максимальную длину текста в символах, которая должна находиться в диапазоне 0-65536. Если значение 0, то ограничений на количество символов нет. Например, установим длину в 20 символов:

```csharp
Entry entry = Entry.New();
entry.MaxLength = 20;
```

## Управление видимостью символов

Свойство `Visibility` при значении `false` скрывает вводимые символы, заменяя их маскировочным символом. По умолчанию это символ "•" (то есть жирная точка). А свойство `InvisibleChar` позволяет установить другой маскировочный символ. Вкратце применение свойств:

```csharp
Entry entry = Entry.New();

// Видимость вводимых символов (полезно для паролей)
entry.Visibility = false; // Скрывает вводимые символы

// Замещающий символ для скрытого текста
entry.InvisibleChar = 'x';
```

В итоге все вводимые символы будут заменяться на символ "x".

## Управление текстом Entry

Рассмотрим основные методы класса `Entry`, которые позволяют управлять текстом:

- public void InsertText(string text, int length, ref int position)
  Вставка текста text длиной length (длина в байтах!) в текущую позицию курсора. Через параметр position возвращает позицию вставки. Если передается длина -1, то вставляется весь текст
- public void DeleteText(int startPos, int endPos)
  Удаление текста между указанными позициями startPos и endPos

Пример применения методов:

```csharp
Entry entry = Entry.New();

// Вставка текста в текущую позицию курсора
string text = "новый текст";
int pos = 0;
entry.InsertText(text, -1, ref pos);

int startPos = 0;  // начальная позиция
int endPos = 3;     // конечная позиция

// Удаление текста между указанными позициями
entry.DeleteText(startPos, endPos);
```

**Источник:** [https://metanit.com/sharp/gtk/4.3.php](https://metanit.com/sharp/gtk/4.3.php)