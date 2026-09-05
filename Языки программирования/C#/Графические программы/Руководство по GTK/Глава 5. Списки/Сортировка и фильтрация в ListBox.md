# Сортировка и фильтрация в ListBox

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Графические программы|Графические программы]] / [[Языки программирования/C#/Графические программы/Руководство по GTK|Руководство по GTK]] / [[Языки программирования/C#/Графические программы/Руководство по GTK/Глава 5. Списки|Глава 5. Списки]] / Сортировка и фильтрация в ListBox

[[Языки программирования/C#/Графические программы/Руководство по GTK/Глава 5. Списки/Выбор и активация строки в ListBox|Назад]] | [[Языки программирования/C#/Графические программы/Руководство по GTK/Глава 5. Списки|Содержание]] | [[Языки программирования/C#/Графические программы/Руководство по GTK/Глава 5. Списки/Модель списка ListModel|Вперёд]]

**Дата написания:** 05.09.2026

## Сортировка

Класс ListBox предоставляет функционал для сортировки элементов в виде метода SetSortFunc()

```csharp
public void SetSortFunc(ListBoxSortFunc? sortFunc)
```

В качестве параметра в метод передается делегат ListBoxSortFunc:

```csharp
public delegate int ListBoxSortFunc(ListBoxRow row1, ListBoxRow row2)
```

Метод, который соответствует этому делегату, получает две сравниваемые строки ListBoxRow и возвращает число: если первая строка "больше" второй, то возвращается 1, если "меньше", то -1.

Если далее потребуется отменить результаты сортировки, то применяется метод без параметров InvalidateSort().

Причем сортировка идет динамически, даже если строки меняют свое содержимое. Например:

```csharp
using Gtk;

var app= Application.New("com.metanit", Gio.ApplicationFlags.DefaultFlags);

app.OnActivate += (sender, _) =>
{
    var window = new Window();
    window.Title = "METANIT.COM";
    window.DefaultWidth = 250;
    window.DefaultHeight = 200;

    var listBox = ListBox.New();

    // устанавливаем функцию сортировки
    listBox.SetSortFunc(SortList);

    // наполняем список
    string[] langs = {"Python", "C++", "JavaScript", "C#"};
    foreach(var lang in langs){
        Label label = Label.New(lang);
        label.Halign = Align.Start;
        listBox.Append(label);
    }

    window.Child = listBox;
    window.Application = (Application) sender;
    window.Show();
};

app.RunWithSynchronizationContext(null);
```

// метод для сортировки

```csharp
int SortList(ListBoxRow row1, ListBoxRow row2){

    Label? row1Label = (Label?) row1.GetChild();
    Label? row2Label = (Label?) row2.GetChild();
    string row1Text = row1Label?.Label_?? "";
    string? row2Text = row2Label?.Label_;

    // сравниваем в лексикографическом порядке
    return row1Text.CompareTo(row2Text);
}
```

В данном случае сортировка производится в функции SortList, где сравниваем текст строк с помощью метода `CompareTo()`, который определяется строками при реализации встроенного интерфейса `IComparable`. Таким образом, строки будут автоматически сортироваться:

![Сортировка списка ListBox в GTK и C#](./pics/3.43.png)

## Фильтрация

ListBox также позволяет отфильтровать элементы - для этого применяется метод SetFilterFunc()

```csharp
public void SetFilterFunc(ListBoxFilterFunc? filterFunc)
```

В качестве параметра метод принимает метод типа делегата ListBoxFilterFunc

```csharp
public delegate bool ListBoxFilterFunc(ListBoxRow row)
```

Метод, который соответствует этому делегату, получает строку ListBoxRow и проверяет ее на соответствие некоторому условию. Если строка соответствует условию, то метод возвращает `true`, иначе возвращается `false`.

Если далее потребуется отменить результаты фильтрации, то применяется метод без параметров InvalidateFilter().

Рассмотрим небольшой пример:

```csharp
using Gtk;

var app= Application.New("com.metanit", Gio.ApplicationFlags.DefaultFlags);

string term = "";  // критерий фильтрации
var listBox = ListBox.New();

app.OnActivate += (sender, _) =>
{
    var window = new Window();
    window.Title = "METANIT.COM";
    window.DefaultWidth = 250;
    window.DefaultHeight = 200;

    // наполняем список
    string[] langs = {"C", "Python", "C++", "C#", "JavaScript", "Java"};
    foreach(var lang in langs){
        Label label = Label.New(lang);
        label.Halign = Align.Start;
        listBox.Append(label);
    }


    Entry entry = Entry.New(); // текстовое поле для ввода критерия фильтрации
    // подключаем обработчик ввода текста
    Editable.Text_PropertyDefinition.Notify(
        sender: entry,
        signalHandler: OnTextChanged
    );

    Box box =  Box.New(Orientation.Vertical, 10);

    box.Append(entry);
    box.Append(listBox);

    window.Child = box;
    window.Application = (Application) sender;
    window.Show();
};

app.RunWithSynchronizationContext(null);
```

// функция фильтрации

```csharp
bool FilterList(ListBoxRow row){

    Label? rowLabel = (Label?) row.GetChild();
    // если текст в строке содержит значение term, то true
    string rowText = rowLabel?.Label_ ?? "";
    return rowText.Contains(term);
}

void OnTextChanged(GObject.Object sender, GObject.Object.NotifySignalArgs e)
{
    // получаем текст из текстового поля и устанавливаем значение term
    Entry entry = (Entry) sender;
    term = entry?.Text_ ?? "";
    // устанавливаем функцию фильтрации
    listBox.SetFilterFunc(FilterList);
}
```

В данном случае интерфейс представлен элементом Box, который содержит текстовое поле Entry для ввода ключа фильтрации и собственно фильтруемый список ListBox. При каждом вводе в текстовое поле будет срабатывать метод `OnTextChanged`

```csharp
void OnTextChanged(GObject.Object sender, GObject.Object.NotifySignalArgs e)
{
    // получаем текст из текстового поля и устанавливаем значение term
    Entry entry = (Entry) sender;
    term = entry?.Text_ ?? "";
    // устанавливаем функцию фильтрации
    listBox.SetFilterFunc(FilterList);
}
```

Здесь мы получаем введенный в текстовое поле текст и на его основе устанавливаем критерий фильтрации - строку term. И затем устанавливаем функцию фильтрации. Стоит отметить, что несмотря на то, что здесь функция фильтрации НЕ меняется вне зависимости от введенных значений - меняется только значение term, но нам все равно надо переустанавливать ее, по сути это и приведет к срабатыванию фильтрации.

В функции фильтрации - `FilterList` проверяем, имеет ли метка строки в списке введенный текст:

```csharp
bool FilterList(ListBoxRow row){

    Label? rowLabel = (Label?) row.GetChild();
    // если текст в строке содержит значение term, то true
    string rowText = rowLabel?.Label_ ?? "";
    return rowText.Contains(term);
}
```

![Фильтрация списка ListBox в GTK и C#](./pics/3.48.png)

**Источник:** [https://metanit.com/sharp/gtk/5.3.php](https://metanit.com/sharp/gtk/5.3.php)