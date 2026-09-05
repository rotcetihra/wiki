# Многострочное текстовое поле TextView

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Графические программы|Графические программы]] / [[Языки программирования/C#/Графические программы/Руководство по GTK|Руководство по GTK]] / [[Языки программирования/C#/Графические программы/Руководство по GTK/Глава 4. Виджеты|Глава 4. Виджеты]] / Многострочное текстовое поле TextView

[[Языки программирования/C#/Графические программы/Руководство по GTK/Глава 4. Виджеты/Создание прокрутки и ScrolledWindow|Назад]] | [[Языки программирования/C#/Графические программы/Руководство по GTK/Глава 4. Виджеты|Содержание]] | [[Языки программирования/C#/Графические программы/Руководство по GTK/Глава 4. Виджеты/Изображения. Image и Picture|Вперёд]]

**Дата написания:** 05.09.2026

Класс TextView в GTK представляет виджет для отображения и редактирования многострочного текста с поддержкой форматирования. `TextView` обладает довольно большими возможностями:

- Отображение и редактирование многострочного текста
- Поддержка различных шрифтов и стилей текста
- Возможность вставки изображений и других виджетов
- Прокрутка текста
- Буфер обмена (копирование/вставка)
- Поддержка отмены/повтора действий (undo/redo)

Для создания `TextView` применяются две статические функции:

```csharp
TextView.New();
TextView.NewWithBuffer(TextBuffer buffer);
```

Второй метод в качестве параметра принимает объект TextBuffer - своего рода текстовый буфер для текстового поля.

Например, создадим данный виджет в самой простейшей форме:

```csharp
using Gtk;

var app= Application.New("com.metanit", Gio.ApplicationFlags.DefaultFlags);

app.OnActivate += (sender, _) =>
{
    var window = new Window();
    window.Title = "METANIT.COM";
    window.DefaultWidth = 250;
    window.DefaultHeight = 200;

    // Создаем TextView
    var textView = TextView.New();

    window.Child = textView;
    window.Application = (Application) sender;
    window.Show();
};

app.RunWithSynchronizationContext(null);
```

В результате мы получим пустое многострочное текстовое поле, в которое можем вводить текст:

![Многострочное текстовое поле TextView в GTK на языке программирования C#](./pics/2.22.png)

Аналогичное создание виджета в XML:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<interface>
  <object class="GtkWindow" id="window">
    <property name="title">METANIT.COM</property>
    <property name="default-width">250</property>
    <property name="default-height">200</property>
    <child>
      <object class="GtkTextView" id="textView" />
    </child>
  </object>
</interface>
```

## Свойства TextView

Для настройки различных параметров отображения и поведения `TextView` определяет ряд свойств. Рассмотрим основные из них:

- Buffer: объект класса `TextBuffer`, который содержит собственно текст и управляет им
- CursorVisible: отображается ли курсор (если `true`, то отображается)
- Editable: доступно ли текстовое поле для редактирования
- Indent: величина отступа абзаца в пикселях
- Justification: выравнивание по левому или правому краю или по центру
- Monospace: должен ли текст отображаться моноширинным шрифтом
- Overwrite: перезаписывает ли введенный текст существующее содержимое
- BottomMargin: отступ снизу
- LeftMargin: отступ слева
- RightMargin: отступ справа
- TopMargin: отступ сверху
- WrapMode: управляет переносом слов. Представляет перечисление `WrapMode`.

## Текстовый буфер TextBuffer

Для работы с текстом в `TextView` используется связанный с ним класс `TextBuffer`, который содержит собственно текст и управляет им. Например, получение и установка текста:

```csharp
// Получаем TextBuffer
TextBuffer? buffer = textView.Buffer;

// Устанавливаем текст
buffer.Text = "Это пример текста в TextView\nВторая строка";

// Получаем текст
string currentText = buffer.Text;
Console.WriteLine(currentText);
```

Единственное, что надо учитывать, что свойство Buffer теоретически может быть равно `null`. Общий пример:

```csharp
using Gtk;

var app= Application.New("com.metanit", Gio.ApplicationFlags.DefaultFlags);

app.OnActivate += (sender, _) =>
{
    var window = new Window();
    window.Title = "METANIT.COM";
    window.DefaultWidth = 250;
    window.DefaultHeight = 200;

    // Создаем TextView
    var textView = TextView.New();
    // Получаем TextBuffer
    TextBuffer? buffer = textView.Buffer;

    if(buffer is not null)
    {
        // Устанавливаем текст
        buffer.Text = "Это пример текста в TextView\nВторая строка";

        // Получаем текст
        string currentText = buffer.Text;
        Console.WriteLine(currentText);
    }
    window.Child = textView;
    window.Application = (Application) sender;
    window.Show();
};

app.RunWithSynchronizationContext(null);
```

Причем весь установленный через свойство Buffer текст сразу отобразится в текстовом поле, соответственно таким образом мы можем установить начальный текст в текстовом поле:

![TextBuffer и текстовое поле TextView в GTK на языке программирования C#](./pics/2.23.png)

Аналогичный пример в XML:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<interface>
  <object class="GtkWindow" id="window">
    <property name="title">METANIT.COM</property>
    <property name="default-width">250</property>
    <property name="default-height">200</property>
    <child>
        <object class="GtkTextView" id="textView">
          <property name="buffer">
            <object class="GtkTextBuffer" id="textBuffer">
              <property name="text">Это пример текста в TextView\nВторая строка</property>
            </object>
          </property>
        </object>
    </child>
  </object>
</interface>
```

## Перенос строк

Для установки переносов применяется свойство `WrapMode`, которому передается одно из значений перечисления **WrapMode**:

- `WrapMode.None`: переносы отсутствуют (значение по умолчанию)
- `WrapMode.Char`: переносит текст, разрывая строки везде, где может появиться курсор (обычно между символами)
- `WrapMode.Word`: переносит текст, разрывая строки между словами
- `WrapMode.WordChar`: переносит текст, разрывая строки между словами или, если этого недостаточно, также между графемами

Включение переноса строк:

```csharp
textView.WrapMode = WrapMode.WordChar;
```

## Размер строк

Свойство PixelsInsideWrap позволяет управлять высотой строк в рамках параграфа:

```csharp
using Gtk;

var app= Application.New("com.metanit", Gio.ApplicationFlags.DefaultFlags);

app.OnActivate += (sender, _) =>
{
    var window = new Window();
    window.Title = "METANIT.COM";
    window.DefaultWidth = 250;
    window.DefaultHeight = 200;

    var textView = TextView.New();
    // текст для вывода в текстовом поле
    string text =
      "Полноте, сударь! Катар желудка доктора выдумали! Больше от вольнодумства да от гордости бывает эта болезнь. " +
      "Вы не обращайте внимания. Положим, вам кушать не хочется или тошно, а вы не обращайте внимания и кушайте себе. " +
      "Ежели, положим, подадут к жаркому парочку дупелей, да ежели прибавить к этому куропаточку или парочку перепелочек жирненьких, "+
      "то тут про всякий катар забудете, честное благородное слово. ";

    TextBuffer? buffer = textView.Buffer;
    if(buffer is not null) buffer.Text = text;

    // устанавливаем перенос по словам
    textView.WrapMode = WrapMode.Word;
    // устанавливаем отступы
    textView.TopMargin = 10;
    textView.LeftMargin = 15;
    textView.RightMargin = 10;

    // устанавливаем отступы между строками в 5 пикселей
    textView.PixelsInsideWrap = 5;

    window.Child = textView;
    window.Application = (Application) sender;
    window.Show();
};

app.RunWithSynchronizationContext(null);
```

![высота строк текста в текстовом поле TextView и WrapMode в GTK и C#](./pics/2.46.png)

## Добавление прокрутки

Проблема `TextView` заключается в том, что по умолчанию при увеличении количества строк, многострочное поле автоматически увеличивает в длине, чтобы вместить все строки. В примерах выше это автоматически приведет к увеличению длины окна, которое должно вместить удлинившееся многострочное поле. Это не очень удобно. Поэтому обычный сценарий заключается в том, чтобы поместить многострочное поле в виджет с прокруткой - ScrolledWindow:

```csharp
using Gtk;

var app= Application.New("com.metanit", Gio.ApplicationFlags.DefaultFlags);

app.OnActivate += (sender, _) =>
{
    var window = new Window();
    window.Title = "METANIT.COM";
    window.DefaultWidth = 250;
    window.DefaultHeight = 200;

    var textView = TextView.New();
    // текст для вывода в текстовом поле
    string text =
      "Полноте, сударь! Катар желудка доктора выдумали! Больше от вольнодумства да от гордости бывает эта болезнь. " +
      "Вы не обращайте внимания. Положим, вам кушать не хочется или тошно, а вы не обращайте внимания и кушайте себе. " +
      "Ежели, положим, подадут к жаркому парочку дупелей, да ежели прибавить к этому куропаточку или парочку перепелочек жирненьких, "+
      "то тут про всякий катар забудете, честное благородное слово. ";

    TextBuffer? buffer = textView.Buffer;
    if(buffer is not null) buffer.Text = text;

    // устанавливаем перенос по словам
    textView.WrapMode = WrapMode.Word;
    // устанавливаем отступы
    textView.TopMargin = 10;
    textView.LeftMargin = 15;
    textView.RightMargin = 10;

    // устанавливаем отступы между строками в 5 пикселей
    textView.PixelsInsideWrap = 5;

    // Добавляем TextView в ScrolledWindow для прокрутки
    var scrolledWindow = ScrolledWindow.New();
    scrolledWindow.Child = textView;

    window.Child = scrolledWindow;
    window.Application = (Application) sender;
    window.Show();
};

app.RunWithSynchronizationContext(null);
```

В итоге если текст выйдет за пределы области обзора, то будут добавляться полосы прокрутки:

![Прокрутка в текстовое поле TextView в GTK на языке программирования C#](./pics/2.27.png)

## Запрет редактирования

Из остальных свойств GtkTextView также можно отметить свойство Editable, которое позволяет запретить или, наоборот, разрешить редактирование текста: если передается значение `false`, то редактирование запрещено, текст доступен только для просмотра. Если передается `true`, то редактирование разрешено. Например:

```csharp
textView.Editable = false;
```

## Обработка изменения текста

С помощью события OnChanged класса TextBuffer можно отслеживать изменения текста:

```csharp
public event SignalHandler<TextBuffer> OnChanged
```

Это событие представляет делегат SignalHandler, а в качестве первого параметра в обработчик события передается объект TextBuffer, который сгенерировал событие. ПРимер обработки изменения текста:

```csharp
using Gtk;

var app= Application.New("com.metanit", Gio.ApplicationFlags.DefaultFlags);

app.OnActivate += (sender, _) =>
{
    var window = new Window();
    window.Title = "METANIT.COM";
    window.DefaultWidth = 250;
    window.DefaultHeight = 200;

    var textView = TextView.New();


    TextBuffer? buffer = textView.Buffer;
    if(buffer is not null){

        // Обработка изменения текста
        buffer.OnChanged += (sender, e) => {
            Console.WriteLine($"Новый текст: {sender.Text}");
        };
    }

    window.Child = textView;
    window.Application = (Application) sender;
    window.Show();
};

app.RunWithSynchronizationContext(null);
```

В данном случае просто выводим новый текст на консоль.

**Источник:** [https://metanit.com/sharp/gtk/4.6.php](https://metanit.com/sharp/gtk/4.6.php)