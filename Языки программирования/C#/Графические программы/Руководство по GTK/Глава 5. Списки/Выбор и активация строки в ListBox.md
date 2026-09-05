# Выбор и активация строки в ListBox

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Графические программы|Графические программы]] / [[Языки программирования/C#/Графические программы/Руководство по GTK|Руководство по GTK]] / [[Языки программирования/C#/Графические программы/Руководство по GTK/Глава 5. Списки|Глава 5. Списки]] / Выбор и активация строки в ListBox

[[Языки программирования/C#/Графические программы/Руководство по GTK/Глава 5. Списки/ListBox|Назад]] | [[Языки программирования/C#/Графические программы/Руководство по GTK/Глава 5. Списки|Содержание]] | [[Языки программирования/C#/Графические программы/Руководство по GTK/Глава 5. Списки/Сортировка и фильтрация в ListBox|Вперёд]]

**Дата написания:** 05.09.2026

## Выделение строк

Для выбора строк и получения выбранных строк виджет ListBox предоставляет ряд методов:

- `ListBoxRow? GetSelectedRow()`
  возвращает выбранную строку или NULL, если не выбрано ни одной строки.
- `gtk_list_box_get_selected_rows`
  возвращает список всех выбранных строк
- `void SelectAll()`
  выбирает все строки
- `void SelectRow(ListBoxRow? row)`
  выбирает определенную строку
- `void SelectedForeach(ListBoxForeachFunc func)`
  выполняет для всех выбранных строк метод, который представляет делегат `ListBoxForeachFunc`
- `void UnselectAll()`
  отменяет выбор всех выбранных строк
- `void UnselectRow(ListBoxRow row)`
  отменяет выбор одной строки

Например, выбор второй строки:

```csharp
ListBox listBox = ListBox.New();

ListBoxRow? row = listBox.GetRowAtIndex(1);
listBox.SelectRow(row);
```

Другой пример - получим выделенную строку. Для этого определим простейшее приложение:

```csharp
using Gtk;

var app= Application.New("com.metanit", Gio.ApplicationFlags.DefaultFlags);

var label = Label.New(null); // метка для вывода выбранного элемента
var listBox = ListBox.New();

app.OnActivate += (sender, _) =>
{
    var window = new Window();
    window.Title = "METANIT.COM";
    window.DefaultWidth = 250;
    window.DefaultHeight = 200;

    // наполняем список
    string[] langs = {"C#", "C++", "JavaScript", "Python"};
    foreach(var lang in langs){
        Label label = Label.New(lang);
        label.Halign = Align.Start;
        listBox.Append(label);
    }
    listBox.Valign = Align.Start;

    label.Halign = Align.Start;
    label.Valign = Align.Start;

    Button button = Button.NewWithLabel("Get");
    button.Halign = Align.Start;
    button.OnClicked += SelectLang;

    Box box =  Box.New(Orientation.Vertical, 10);

    box.Append(label);
    box.Append(button);
    box.Append(listBox);

    window.Child = box;
    window.Application = (Application) sender;
    window.Show();
};

app.RunWithSynchronizationContext(null);
```

// обработчик нажатия кнопки

```csharp
void SelectLang(Button sender, EventArgs e) {

    // получаем выбранную строку
    ListBoxRow? selected = listBox.GetSelectedRow();
    // получаем метку из выбранной строки
    Label? rowLabel = (Label?) selected?.GetChild();
    // получаем текст на метке из выбранной строки и передаем его на верхней метке
    label.Label_ = rowLabel?.Label_;
}
```

В данном случае при нажатии на кнопку в обработчике события нажатия - методе SelectLang получаем выбранную строку и передаем ее текст на метку выше списка:

![Выбор строк в списке ListBox в GTK и C#](./pics/3.42.png)

## Настройка выбора строк

По умолчанию пользователь может выбрать только одну строку, но с помощью свойства SelectionMode можно настроить этот аспект. Данное свойство представляет значение перечисления SelectionMode, которое может принимать следующие значения:

- `None`: выбор невозможен. Значение: 0
- `Single`: можно выбрать только один элемент или ноль элементов. Значение: 1
- `Browse`: можно выбрать ровно один элемент. Значение: 2
- `Multiple`: доступен выбор множества строк. Значение: 3

Например, установка возможности выбора нескольких строк:

```csharp
var listBox = ListBox.New();
listBox.SelectionMode = SelectionMode.Multiple;
```

## Получение всех выбранных строк

Даже если мы установили множественный выбор и можем выбрать одномоментно сразу несколько строк, то встает вопрос, как получить все эти строки, тем более что класс ListBox не предоставляет для этого специального свойства или метода. Но в качестве решения мы можем использовать метод SelectedForeach(), который в качестве параметра принимает метод, соответствующий делегату `ListBoxForeachFunc`. Данный делегат принимает два параметра:

```csharp
public delegate void ListBoxForeachFunc(ListBox box, ListBoxRow row)
```

Первый параметр представляет сам список ListBox, а второй - выбранную строку `ListBoxRow`.

И при выполнении SelectedForeach() будет выполнять переданный ему метод-делегат ListBoxForeachFunc для каждой выбранной строки. Выбранные строки будут передаваться в качестве второго параметра.

Например, установим множественный выбор и выведем на консоль все выбранные строки:

```csharp
using Gtk;

var app= Application.New("com.metanit", Gio.ApplicationFlags.DefaultFlags);

var listBox = ListBox.New();

app.OnActivate += (sender, _) =>
{
    var window = new Window();
    window.Title = "METANIT.COM";
    window.DefaultWidth = 250;
    window.DefaultHeight = 200;

    // наполняем список
    string[] langs = {"C#", "C++", "JavaScript", "Python"};
    foreach(var lang in langs){
        Label label = Label.New(lang);
        label.Halign = Align.Start;
        listBox.Append(label);
    }
    listBox.Valign = Align.Start;
    listBox.SelectionMode = SelectionMode.Multiple;

    Button button = Button.NewWithLabel("Selected");
    button.Halign = Align.Start;
    button.OnClicked += GetSelectedLangs; // обрабатываем все выделенные строки

    Box box =  Box.New(Orientation.Vertical, 10);

    box.Append(button);
    box.Append(listBox);

    window.Child = box;
    window.Application = (Application) sender;
    window.Show();
};

app.RunWithSynchronizationContext(null);
```

// обработчик нажатия кнопки

```csharp
void GetSelectedLangs(Button sender, EventArgs e) {

    listBox.SelectedForeach(PrintLang);
}

void PrintLang(ListBox _, ListBoxRow selectedRow){
    // получаем метку из выбранной строки
    Label? rowLabel = (Label?) selectedRow.GetChild();
    // получаем текст на метке из выбранной строки
    Console.WriteLine(rowLabel?.Label_);
}
```

Здесь по нажатию на кнопку будет срабатывать метод-обработчик GetSelectedLangs, который выполняет метод `listBox.SelectedForeach()`. В этот метод передается другой метод - PrintLang, который соответствует делегату ListBoxForeachFunc. В PrintLang получаем выбранную строку и выводим ее текст на консоль.

## Обработка выбора и активации строки

Чтобы строку можно было выбрать или нажать на нее, соответствующий элемент `ListBoxRow` можно пометить как активируемый или выбираемый. Для этой цели класс `ListBoxRow` предоставляет соответственно методы SetActivatable(bool) и SetSelectable(bool), которые в принципе однотипны и в качестве второго параметра принимают булевое значение `true` или `false`.

Если строка активируемая, и пользователь нажимает на нее, то для нее ListBox сгенерирует событие OnRowActivated:

```csharp
event SignalHandler<ListBox, ListBox.RowActivatedSignalArgs> OnRowActivated
```

Второй параметр представляет нажатую строку, а третий параметр - передаваемые в обработчик сигнала данные. Например, выведем текст нажатой строки в метку:

```csharp
using Gtk;

var app= Application.New("com.metanit", Gio.ApplicationFlags.DefaultFlags);

var label = Label.New(null);
var listBox = ListBox.New();

app.OnActivate += (sender, _) =>
{
    var window = new Window();
    window.Title = "METANIT.COM";
    window.DefaultWidth = 250;
    window.DefaultHeight = 200;

    // наполняем список
    string[] langs = {"C#", "C++", "JavaScript", "Python"};
    foreach(var lang in langs){
        Label label = Label.New(lang);
        label.Halign = Align.Start;
        listBox.Append(label);
    }
    listBox.Valign = Align.Start;
    listBox.OnRowActivated += GetSelectedLang;

    label.Halign = Align.Start;

    Box box =  Box.New(Orientation.Vertical, 10);

    box.Append(label);
    box.Append(listBox);

    window.Child = box;
    window.Application = (Application) sender;
    window.Show();
};

app.RunWithSynchronizationContext(null);
```

// обработчик нажатия кнопки

```csharp
void GetSelectedLang(ListBox sender, ListBox.RowActivatedSignalArgs e) {

    ListBoxRow? row = e.Row; // получаем выбранную строку
    Label? rowLabel = (Label?) row?.GetChild();
    label.Label_ = rowLabel?.Label_;
}
```

В данном случае за обработку события OnRowActivated отвечает метод GetSelectedLang, в который в качестве второго параметра передаются аргументы события в виде объекта `ListBox.RowActivatedSignalArgs`. Через свойство `Row` этого объекта мы можем получить выбранную строку, для которой было сгенерировано событие, и далее получить ее текст и вывести его на текстовой метке:

![Обработка нажатия на строку в списке ListBox в GTK и C#](./pics/3.44.png)

Если строка выбираемая (как это происходит по умолчанию), то строка будет помечена как выбранная, когда пользователь попытается ее выбрать, а ListBox сгенерирует событие OnRowSelected:

```csharp
event SignalHandler<ListBox, ListBox.RowSelectedSignalArgs> OnRowSelected
```

Здесь аналогичное событие, только в этом случае пользователь может отменить выбор, и параметр row в этом случае будет равен `null`

**Источник:** [https://metanit.com/sharp/gtk/5.2.php](https://metanit.com/sharp/gtk/5.2.php)