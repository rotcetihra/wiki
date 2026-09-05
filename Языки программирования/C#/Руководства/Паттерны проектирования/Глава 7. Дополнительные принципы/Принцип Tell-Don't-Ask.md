# Принцип Tell-Don't-Ask

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Руководства|Руководства]] / [[Языки программирования/C#/Руководства/Паттерны проектирования|Паттерны проектирования]] / [[Языки программирования/C#/Руководства/Паттерны проектирования/Глава 7. Дополнительные принципы|Дополнительные принципы]] / Принцип Tell-Don't-Ask

[[Языки программирования/C#/Руководства/Паттерны проектирования/Глава 6. Дополнительные паттерны/Fluent Builder|Назад]] | [[Языки программирования/C#/Руководства/Паттерны проектирования/Глава 7. Дополнительные принципы|Дополнительные принципы]]

**Дата написания:** 05.09.2026

## Принцип Tell-Don't-Ask

Принцип  Tell-Don't-Ask  позволяет объединить данные и связанное с ними поведение.  Применение этого принципа позволяет вместо опроса данных и 
последующих действий напрямую выполнять данные действия.

Например, рассмотрим сначала пример с опросом данных объекта:

```csharp
AlarmClock clock = new AlarmClock(6);
clock.CurrentHour = 6;

if (clock.CurrentHour == clock.GetUpHour)   // ask
    clock.Alarm();

class AlarmClock
{
    public int GetUpHour { get; set; }
    public int CurrentHour { get; set; }
    public AlarmClock(int hour) => GetUpHour = hour;

    public void Alarm() => Console.WriteLine("Рота! Подъем!");
}
```

Здесь определен класс условного будильника - класс AlarmClock. Свойство GetUpHour хранит час, когда будильник даст сигнал. Свойство CurrentHour 
хранит текущий час. А метод Alarm собственно выполняет сигнал будильника.

В основной части программы проверяем текущий час и, если он равен времени звонка будильника, то вызываем метод Alarm.

```csharp
if (clock.CurrentHour == clock.GetUpHour)   // ask
    clock.Alarm();
```

Это стандартный опрос данных, за котором действуют некоторое связанные с ними действия. То что называется  ask

Теперь уберем в соответствии с принципом  Tell-Don't-Ask  изменим программу:

```csharp
AlarmClock clock = new AlarmClock(6);
clock.CurrentHour = 6;

class AlarmClock
{
    int currentHour;
    public int GetUpHour { get; set; }
    public int CurrentHour
    {
        get => currentHour;
        set
        {
            if (value == GetUpHour) Alarm(); // tell
            currentHour = value;
        }
    }
    public AlarmClock(int hour) => GetUpHour = hour;

    public void Alarm() => Console.WriteLine("Рота! Подъем!");
}
```

Теперь проверка времени перемещена непосредственно в сам объект AlarmClock. Соответственно вне объекта теперь нам не надо запрашивать его данные.

Обычно подобное решение является предпочтительным, так данные и действия над ними тесно связаны. А изменения одного аспекта (данных или поведения) 
приведет к изменению второго аспекта.

Другой распространенный пример, где можно применить подобный принцип, связан с иерархиями классов. Например, пусть имеется следующая программа:

```csharp
IMessage[] messages = new IMessage[]
{
    new VoiceMessage(Array.Empty<byte>(), "tom", "sam"), // условное голосовое сообщение
    new TextMessage("Hello", "sam", "tom") // текстовое сообщение
};

foreach(var message in messages)
{
    if (message is TextMessage textMessage) // ask
        textMessage.Print();
    else if (message is VoiceMessage voiceMessage)  // ask
        voiceMessage.Play();
}

interface IMessage
{
    string Sender { get;}
    string Receiver { get; }
}

class TextMessage : IMessage
{
    public string Sender { get;}
    public string Receiver { get;}
    public string Text { get;}
    public TextMessage(string text, string sender, string receiver)
    {
        Text = text;
        Receiver = receiver;
        Sender = sender;
    }
    public void Print() => Console.WriteLine($"Текстовое сообщение: {Text}");
}

class VoiceMessage : IMessage
{
    public string Sender { get;}
    public string Receiver { get;}
    public byte[] Voice { get; }
    public VoiceMessage(byte[] voice, string sender, string receiver)
    {
        Voice = voice;
        Receiver = receiver;
        Sender = sender;
    }
    public void Play() => Console.WriteLine($"Воспроизведение голосового сообщения");
}
```

Здесь определен интерфейс IMessage, который представляет условное сообщение. И есть две реализации данного интерфейса: класс текстового сообщения TextMessage и класс 
голосового сообщения VoiceMessage. Оба класса реализуют некоторый общий функционал. Однако для вывода текстового сообщения на консоль применяется метод Print, 
а для воспроизведения голосового сообщения применяется метод Play.

Если у нас есть набор сообщений, и мы хотим узнать, что за контент они содержат, нам необходимо выполнить опрос - проверить их типы и затем выполнить 
соответствующий метод:

```csharp
foreach(var message in messages)
{
    if (message is TextMessage textMessage) // ask
        textMessage.Print();
    else if (message is VoiceMessage voiceMessage)  // ask
        voiceMessage.Play();
}
```

И вместо опроса мы можем напрямую выполнить определенное действия:

```csharp
IMessage[] messages = new IMessage[]
{
    new VoiceMessage(Array.Empty<byte>(), "tom", "sam"), // условное голосовое сообщение
    new TextMessage("Hello", "sam", "tom") // текстовое сообщение
};

foreach(var message in messages)
{
    message.Launch();
}

interface IMessage
{
    string Sender { get;}
    string Receiver { get; }
    void Launch();
}

class TextMessage : IMessage
{
    public string Sender { get;}
    public string Receiver { get;}
    public string Text { get;}
    public TextMessage(string text, string sender, string receiver)
    {
        Text = text;
        Receiver = receiver;
        Sender = sender;
    }
    private void Print() => Console.WriteLine($"Текстовое сообщение: {Text}");
    public void Launch() => Print();     // tell
}

class VoiceMessage : IMessage
{
    public string Sender { get;}
    public string Receiver { get;}
    public byte[] Voice { get; }
    public VoiceMessage(byte[] voice, string sender, string receiver)
    {
        Voice = voice;
        Receiver = receiver;
        Sender = sender;
    }
    private void Play() => Console.WriteLine($"Воспроизведение голосового сообщения");
    public void Launch() => Play();  // tell
}
```

Теперь в интерфейсе IMessage определен метод Launch(), в котором каждый из классов-сообщений выполняет соответствующий метод.

**Источник:** [https://metanit.com/sharp/patterns/7.1.php](https://metanit.com/sharp/patterns/7.1.php)

[[Языки программирования/C#/Руководства/Паттерны проектирования/Глава 6. Дополнительные паттерны/Fluent Builder|Назад]] | [[Языки программирования/C#/Руководства/Паттерны проектирования/Глава 7. Дополнительные принципы|Дополнительные принципы]]
