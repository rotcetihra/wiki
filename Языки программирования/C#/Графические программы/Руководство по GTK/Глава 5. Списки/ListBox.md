# ListBox

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Графические программы|Графические программы]] / [[Языки программирования/C#/Графические программы/Руководство по GTK|Руководство по GTK]] / [[Языки программирования/C#/Графические программы/Руководство по GTK/Глава 5. Списки|Глава 5. Списки]] / ListBox

[[Языки программирования/C#/Графические программы/Руководство по GTK/Глава 4. Виджеты/SpinButton|Назад]] | [[Языки программирования/C#/Графические программы/Руководство по GTK/Глава 5. Списки|Содержание]] | [[Языки программирования/C#/Графические программы/Руководство по GTK/Глава 5. Списки/Выбор и активация строки в ListBox|Вперёд]]

**Дата написания:** 05.09.2026

Для работы со списками данных GTK предоставляет ряд специальных виджетов для работы. Эти виджеты позволяют отобразить множество объектов унифицированным образом, причем диапазон элементов в списке может вариироваться от 2-3 элементов до сотен тысяч элементов. Подобные виджеты могут отображать как статичные неизменяющиеся данные, так и данные, которые подверженые изменению - либо при добавлении/удалении элементов в списке, либо при редактировании уже существующих элементов.

Самым простым и в тже время распространенным виджетом для отображения списка является класс ListBox. Он представляет вертикальный список, где каждый элемент представлен объектом типа ListBoxRow - своего рода строкой. Эти строки можно динамически сортировать и фильтровать, осуществлять по строкам навигацию и выбор с помощью клавиатуры и мыши.

Хотя `ListBox` должен иметь только дочерние элементы ListBoxRow, в него можно добавить любой виджет, тогда он неявно будет обернут в `ListBoxRow`.

Для создания виджета применяется статический метод `ListBox.New()` без параметров:

```csharp
ListBox listBox = ListBox.New();
```

## Добавление элементов

Для добавления элементов в ListBox применяется ряд функций:

- `Append(Widget child)`: добавляет виджет в конец списка
- `Prepend(Widget child)`: добавляет виджет в начало списка
- `Insert(Widget child, int position)`: вставляет указанный виджет на определенную позицию в списке

Обратите внимание, что в любом случае добавляемый элемент должен представлять виджет. Рассмотрим применение этих функций:

```csharp
using Gtk;

var app= Application.New("com.metanit", Gio.ApplicationFlags.DefaultFlags);

app.OnActivate += (sender, _) =>
{
    var window = new Window();
    window.Title = "METANIT.COM";
    window.DefaultWidth = 250;
    window.DefaultHeight = 200;

    ListBox listBox = ListBox.New();

    // добавляем в конец списка
    listBox.Append(Label.New("C++"));
    listBox.Append(Label.New("Python"));
    // добавляем в начало списка
    listBox.Prepend(Label.New("C#"));
    // вставляем по индексу 1 (то есть второй элемент)
    listBox.Insert(Label.New("JavaScript"), 1);

    window.Child = listBox;
    window.Application = (Application) sender;
    window.Show();
};

app.RunWithSynchronizationContext(null);
```

Здесь все добавляемые элементы представляют метки `Label` с некоторым текстом. В итоге мы получим следующий список:

![Список ListBox в GTK и C#](./pics/3.40.png)

Но, как можно увидеть из скриншота, по умолчанию ListBox растягивается по всей ширине/высоте окна-контейнера, и, кроме того, растягиваются и добавляемые метки. В итоге мы получаем растянутые метки с текстом по центру виджета. Чтобы должным образом упорядочить виджеты, мы можем использовать стандартные способы позиционирования, в частности, свойства `Halign` и `Valign`. Например:

```csharp
using Gtk;

var app= Application.New("com.metanit", Gio.ApplicationFlags.DefaultFlags);

app.OnActivate += (sender, _) =>
{
    var window = new Window();
    window.Title = "METANIT.COM";
    window.DefaultWidth = 250;
    window.DefaultHeight = 200;

    ListBox listBox = ListBox.New();

    string[] langs = {"C#", "C++", "JavaScript", "Python"};
    foreach(var lang in langs){
        Label label = Label.New(lang);
        label.Halign = Align.Start; // выравнивание по левому краю
        listBox.Append(label);
    }

    window.Child = listBox;
    window.Application = (Application) sender;
    window.Show();
};

app.RunWithSynchronizationContext(null);
```

![Добавление элементов в список ListBox в GTK и C#](./pics/3.41.png)

## Получение элементов

Для получения элементов списка класс ListBox предоставляет пару методов:

- `ListBoxRow? GetRowAtIndex(int index)`
  получает элемент в списке по индексу index. Если index\_ отрицателен или больше количества элементов в списке, возвращается NULL.
- `ListBoxRow? GetRowAtY(int y)`
  получает строку в позиции y.

Обратите внимание, что каждая из этих методов возвращает объект типа ListBoxRow, в который оборачивается добавляемый виджет. Однако этот тип имеет метод GetChild(), который позволяет получить непосредственно содержимое в виде объекта `Widget?`.

Для примера просто выведем все элементы из списка на консоль сразу после его создания:

```csharp
using Gtk;

var app= Application.New("com.metanit", Gio.ApplicationFlags.DefaultFlags);

app.OnActivate += (sender, _) =>
{
    var window = new Window();
    window.Title = "METANIT.COM";
    window.DefaultWidth = 250;
    window.DefaultHeight = 200;

    ListBox listBox = ListBox.New();

    string[] langs = {"C#", "C++", "JavaScript", "Python"};
    foreach(var lang in langs){
        Label label = Label.New(lang);
        label.Halign = Align.Start; // выравнивание по левому краю
        listBox.Append(label);
    }

    ListBoxRow? row;
    int i = 0;
    // пока есть строки, получаем их в переменную row
    while((row = listBox.GetRowAtIndex(i++)) is not null){

        // получаем содержимое строки - выше добавленные метки
        Label? label = (Label?) row.GetChild();
        Console.WriteLine($"Row {i}: {label?.Label_}");
    }
    window.Child = listBox;
    window.Application = (Application) sender;
    window.Show();
};

app.RunWithSynchronizationContext(null);
```

В итоге консоль выведет:

```
Row 1: C#
Row 2: C++
Row 3: JavaScript
Row 4: Python
```

## Удаление элементов

Для удаления строк GTK предоставляет ряд функций:

- `void Remove(Widget child)`
  удаляет дочерний элемент, который передается через второй параметр.
- `void RemoveAll()`
  удаляет все строки из виджета

Например, удаление второй строки (с индексом 1):

```csharp
ListBox listBox = ListBox.New();

string[] langs = {"C#", "C++", "JavaScript", "Python"};
foreach(var lang in langs){
    Label label = Label.New(lang);
    label.Halign = Align.Start; // выравнивание по левому краю
    listBox.Append(label);
}

// удаление второй строки
ListBoxRow? row = listBox.GetRowAtIndex(1);
if (row is not null) listBox.Remove(row);
```

**Источник:** [https://metanit.com/sharp/gtk/5.1.php](https://metanit.com/sharp/gtk/5.1.php)