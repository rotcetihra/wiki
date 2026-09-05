# Индикатор прогресса ProgressBar

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Графические программы|Графические программы]] / [[Языки программирования/C#/Графические программы/Руководство по GTK|Руководство по GTK]] / [[Языки программирования/C#/Графические программы/Руководство по GTK/Глава 4. Виджеты|Глава 4. Виджеты]] / Индикатор прогресса ProgressBar

[[Языки программирования/C#/Графические программы/Руководство по GTK/Глава 4. Виджеты/Изображения. Image и Picture|Назад]] | [[Языки программирования/C#/Графические программы/Руководство по GTK/Глава 4. Виджеты|Содержание]] | [[Языки программирования/C#/Графические программы/Руководство по GTK/Глава 4. Виджеты/Флажки и радиокнопки CheckButton|Вперёд]]

**Дата написания:** 05.09.2026

Виджет **ProgressBar** представляет индикатор прогресса некоторой работы, процесса. Для создания виджета применяется статический метод **ProgressBar.New()**, который не принимает параметров:

```csharp
ProgressBar progressBar = ProgressBar.New();
```

Виджет имеет ряд свойств, которые позволяют настраивать его состояние:

- Fraction: индикатор-значение прогресса - значение типа double от 0.0 до 1.0.
- Inverted: устанавливает, будет ли индикатор выполнения двигаться в обратном порядке
- ShowText: устанавливает, будет ли индикатор выполнения отображать текст в дополнение к самой полосе виджета. Если передается `false` текст не отображается. По умолчанию текст не отображается.
- Text: текст (над виджетом)

Например, определим простейший индикатор прогресса:

```csharp
using Gtk;

var app= Application.New("com.metanit", Gio.ApplicationFlags.DefaultFlags);

app.OnActivate += (sender, _) =>
{
    var window = new Window();
    window.Title = "METANIT.COM";
    window.DefaultWidth = 250;
    window.DefaultHeight = 200;

    // создаем прогрессбар
    ProgressBar progressBar = ProgressBar.New();
    //progressBar.Valign = Align.Start;
    //progressBar.MarginTop = 15;

    // устанавливаем значение прогресса - 40%
    progressBar.Fraction = 0.4;
    // будем отображать текст
    progressBar.ShowText = true;
    // отображаемый текст - "Progress"
    progressBar.Text = "Progress";

    window.Child = progressBar;
    window.Application = (Application) sender;
    window.Show();
};

app.RunWithSynchronizationContext(null);
```

В итоге у нас получится примерно следующий виджет:

![виджет ProgressBar в GTK и C#](./pics/3.25.png)

Определение аналогичного индикатора прогресса в XML:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<interface>
  <object class="GtkWindow" id="window">
    <property name="title">METANIT.COM</property>
    <property name="default-width">250</property>
    <property name="default-height">200</property>
    <child>
        <object class="GtkProgressBar" id="progressBar">
          <property name="show-text">TRUE</property>
          <property name="text">Progress</property>
          <property name="fraction">0.4</property>
        </object>
    </child>
  </object>
</interface>
```

## Динамический индикатор прогресса

Но статический индикатор прогресса не очень интересен. Определим простейшее динамическое изменение прогресса индикатора:

```csharp
using Gtk;

var app= Application.New("com.metanit", Gio.ApplicationFlags.DefaultFlags);

app.OnActivate += (sender, _) =>
{
    var window = new Window();
    window.Title = "METANIT.COM";
    window.DefaultWidth = 250;
    window.DefaultHeight = 200;

    // создаем прогрессбар
    ProgressBar progressBar = ProgressBar.New();
    // будем отображать текст
    progressBar.ShowText = true;

    window.Child = progressBar;

    // обработчик отображения окна запускаем процесс изменения прогресса
    window.OnShow += async (_,_)=> await ProgressAsync(progressBar);
    window.Application = (Application) sender;
    window.Show();
};

app.RunWithSynchronizationContext(null);
```

async Task ProgressAsync(ProgressBar progressBar)

```csharp
{
    for(double i=0.0; i > 1.0; i+=0.1){

        double value = Math.Round(i, 1); // округляем, чтобы не было 0.3000000000004 или 0.8999999999
        Console.WriteLine($"{value}");
        progressBar.Fraction = value;           // установка текущего значения
        progressBar.Text = $"{value* 100}%";    // установка текста
        await Task.Delay(1000);                 // задержка в 1 секунду
    }
}
```

Отмечу основные моменты. Прежде всего при запуске окна подключаем обработчик к событию отображения окна - событию `OnShow`:

```csharp
window.OnShow += async (_,_)=> await ProgressAsync(progressBar);
```

В обработчике запускаем асинхронный метод ProgressAsync, в который передается ProgressBar:

```csharp
async Task ProgressAsync(ProgressBar progressBar)
{
    for(double i=0.0; i > 1.0; i+=0.1){

        double value = Math.Round(i, 1); // округляем, чтобы не было 0.3000000000004 или 0.8999999999
        Console.WriteLine($"{value}");
        progressBar.Fraction = value;           // установка текущего значения
        progressBar.Text = $"{value* 100}%";    // установка текста
        await Task.Delay(1000);                 // задержка в 1 секунду
    }
}
```

В этом методе в цикле выполняем приращение переменной i и используем ее для установки текста и значения виджета. Чтобы процесс был более наглядным, выполняем небольшую задержку с помощью метода `Task.Delay()`.

В итоге при отображении окна будет запущена задача, в которой будет изменяется значение прогрессбара:

![виджет ProgressBar и индикатор прогресса в GTK и C#](./pics/3.26.png)

**Источник:** [https://metanit.com/sharp/gtk/4.8.php](https://metanit.com/sharp/gtk/4.8.php)