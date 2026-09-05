# DispatcherTimer, ProgressBar и ProgressRing

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Графические программы|Графические программы]] / [[Языки программирования/C#/Графические программы/Руководство по UWP|Руководство по UWP]] / [[Языки программирования/C#/Графические программы/Руководство по UWP/Глава 4. Элементы управления|Глава 4. Элементы управления]] / DispatcherTimer, ProgressBar и ProgressRing

[[Языки программирования/C#/Графические программы/Руководство по UWP/Глава 4. Элементы управления/Slider|Назад]] | [[Языки программирования/C#/Графические программы/Руководство по UWP/Глава 4. Элементы управления|Содержание]] | [[Языки программирования/C#/Графические программы/Руководство по UWP/Глава 4. Элементы управления/WebView|Вперёд]]

**Дата написания:** 05.09.2026

DispatcherTimer, ProgressBar и ProgressRingПоследнее обновление: 11.02.2016
 
 
 

 
- 
 
- 
 
- 
 
 

 
 

 
 
 
 
 

 
### DispatcherTimer

DispatcherTimer не является элементом управления, однако мы можем его использовать для процессов в графическом приложении, которые должны выполняться с определенной периодичностью. 
Наиболее важные свойства и методы таймера:

- 

Свойство Enabled при значении true указывает, что таймер будет запускаться вместе с формой

- 

Свойство Interval устанавливает интервал таймера в виде объекта TimeSpan

- 

Метод Start() запускает таймер

- 

Метод Stop() останавливает таймер

- 

Событие Tick срабатывает по истечении интервала из свойства Interval

Далее на примере индикатора процесса рассмотри использование таймера

### ProgressBar

ProgressBar представляет индикатор выполнения какого-либо процесса. Например, зададим следующий ProgressBar:

```

 
 

```

Свойство `Maximum` указывает на максимально возможное значение индикатора. При изменении значения генерируется событие ValueChanged. 
Определим в файле кода для него обработчик:

```
using System;
using Windows.UI.Xaml;
using Windows.UI.Xaml.Controls;
using Windows.UI.Xaml.Controls.Primitives;

namespace ControlsApp
{
 public sealed partial class MainPage : Page
 {
 DispatcherTimer timer;
 public MainPage()
 {
 this.InitializeComponent();
 
 timer = new DispatcherTimer() { Interval = new TimeSpan(0,0,1) }; // 1 секунда
 timer.Tick += Timer_Tick;
 timer.Start();
 }

 private void Timer_Tick(object sender, object e)
 {
 progressBar.Value++;
 if (progressBar.Value == 100)
 timer.Stop();
 }

 private void progressBar_ValueChanged(object sender, RangeBaseValueChangedEventArgs e)
 {
 textBlock1.Text = progressBar.Value.ToString();
 }
 }
}
```

В данном случае при запуске приложения будет запускаться таймер, который будет срабатывать раз в секунду. В обработчике таймера происходит приращение 
значения индикатора: `progressBar.Value++`

В ответ на изменение значения индикатора генерируется событие ValueChanged и срабатывает его обработчик, который изменяет текст в текстовом блоке.
![ProgressBar в UWP](pics/4.37.png)

### ProgressRing

ProgressRing представляет кольцо с анимацией, которое отображается во время некоторого длительного процесса:

```

```

Если свойство `IsActive` равно `true`, значит кольцо будет отображаться. При завершении процесса мы можем программно отключить отображение, задав 
этому свойству значение `false`
![ProgressRing в UWP](pics/4.38.png)

---

**Источник:** [https://metanit.com/sharp/uwp/4.11.php](https://metanit.com/sharp/uwp/4.11.php)
