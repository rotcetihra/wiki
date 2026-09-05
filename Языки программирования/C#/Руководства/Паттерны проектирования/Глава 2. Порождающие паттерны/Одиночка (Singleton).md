# Одиночка (Singleton)

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Руководства|Руководства]] / [[Языки программирования/C#/Руководства/Паттерны проектирования|Паттерны проектирования]] / [[Языки программирования/C#/Руководства/Паттерны проектирования/Глава 2. Порождающие паттерны|Порождающие паттерны]] / Одиночка (Singleton)

[[Языки программирования/C#/Руководства/Паттерны проектирования/Глава 2. Порождающие паттерны/Абстрактная фабрика (Abstract Factory)|Назад]] | [[Языки программирования/C#/Руководства/Паттерны проектирования/Глава 2. Порождающие паттерны|Порождающие паттерны]] | [[Языки программирования/C#/Руководства/Паттерны проектирования/Глава 2. Порождающие паттерны/Прототип (Prototype)|Вперёд]]

**Дата написания:** 05.09.2026

## Одиночка

Одиночка (Singleton, Синглтон) - порождающий паттерн, который гарантирует, что для определенного класса будет создан только один объект, а 
также предоставит к этому объекту точку доступа.

Когда надо использовать Синглтон? Когда необходимо, чтобы для класса существовал только один экземпляр

Синглтон позволяет создать объект только при его необходимости. Если объект не нужен, то он не будет создан. В этом отличие синглтона от 
глобальных переменных.

Классическая реализация данного шаблона проектирования на C# выглядит следующим образом:

```csharp
class Singleton
{
    private static Singleton instance;

    private Singleton()
    {}

    public static Singleton getInstance()
    {
        if (instance == null)
            instance = new Singleton();
        return instance;
    }
}
```

В классе определяется статическая переменная - ссылка на конкретный экземпляр данного объекта и приватный конструктор. В статическом методе 
 `getInstance()`  этот конструктор вызывается для создания объекта, если, конечно, объект отсутствует и равен null.

Для применения паттерна Одиночка создадим небольшую программу. Например, на каждом компьютере можно одномоментно запустить только одну операционную систему. 
В этом плане операционная система будет реализоваться через паттерн синглтон:

```csharp
class Program
{
    static void Main(string[] args)
    {
        Computer comp = new Computer();
        comp.Launch("Windows 8.1");
        Console.WriteLine(comp.OS.Name);
		
        // у нас не получится изменить ОС, так как объект уже создан    
        comp.OS = OS.getInstance("Windows 10");
        Console.WriteLine(comp.OS.Name);
		
        Console.ReadLine();
    }
}
class Computer
{
    public OS OS { get; set; }
    public void Launch(string osName)
    {
        OS = OS.getInstance(osName);
    }
}
class OS
{
    private static OS instance;

    public string Name { get; private set; }

    protected OS(string name)
    {
        this.Name=name;
    }

    public static OS getInstance(string name)
    {
        if (instance == null)
            instance = new OS(name);
        return instance;
    }
}
```

### Синглтон и многопоточность

При применении паттерна синглтон в многопоточным программах мы можем столкнуться с проблемой, которую можно описать следующим образом:

```csharp
static void Main(string[] args)
{
	(new Thread(() =>
	{
		Computer comp2 = new Computer();
		comp2.OS = OS.getInstance("Windows 10");
		Console.WriteLine(comp2.OS.Name);

	})).Start();

	Computer comp = new Computer();
	comp.Launch("Windows 8.1");
	Console.WriteLine(comp.OS.Name);
	Console.ReadLine();
}
```

Здесь запускается дополнительный поток, который получает доступ к синглтону. Параллельно выполняется тот код, который идет запуска потока и 
кторый также обращается к синглтону. Таким образом, и главный, и дополнительный поток пытаются инициализровать синглтон нужным значением - 
"Windows 10", либо "Windows 8.1". Какое значение сиглтон получит в итоге, пресказать в данном случае невозможно.

Вывод программы может быть такой:

```csharp
Windows 8.1
Windows 10
```

Или такой:

```csharp
Windows 8.1
Windows 8.1
```

В итоге мы сталкиваемся с проблемой инициализации синглтона, когда оба потока одновременно обращаются к коду:

```csharp
if (instance == null)
    instance = new OS(name);
```

Чтобы решить эту проблему, перепишем класс синглтона следующим образом:

```csharp
class OS
{
    private static OS instance;

    public string Name { get; private set; }
    private static object syncRoot = new Object();

    protected OS(string name)
    {
        this.Name = name;
    }

    public static OS getInstance(string name)
    {
        if (instance == null)
        {
            lock (syncRoot)
            {
                if (instance == null)
                    instance = new OS(name);
            }
        }
        return instance;
    }
}
```

Чтобы избежать одновременного доступа к коду из разных потоков критическая секция заключается в блок  lock .

### Другие реализации синглтона

Выше были рассмотрены общие стандартные реализации: потоконебезопасная и потокобезопасная реализации паттерна. Но есть еще ряд дополнительных реализаций, которые можно рассмотреть.

### Потокобезопасная реализация без использования lock

```csharp
public class Singleton
{
    private static readonly Singleton instance = new Singleton();

    public string Date { get; private set; }

    private Singleton()
    {
        Date = System.DateTime.Now.TimeOfDay.ToString();
    }

    public static Singleton GetInstance()
    {
        return instance;
    }
}
```

Данная реализация также потокобезопасная, то есть мы можем использовать ее в потоках так:

```csharp
(new Thread(() =>
{
    Singleton singleton1 = Singleton.GetInstance();
    Console.WriteLine(singleton1.Date);
})).Start();

Singleton singleton2 = Singleton.GetInstance();
Console.WriteLine(singleton2.Date);
```

### Lazy-реализация

Определение объекта синглтона в виде статического поля класса открывает нам дорогу к созданию Lazy-реализации паттерна Синглтон, то есть 
такой реализации, где данные будут инициализироваться только перед непосредственным использованием. Поскольку статические поля 
инициализируются перед первым доступом к статическому членам класса и перед вызовом статического конструктора (при его наличии). 
Однако здесь мы можем столкнуться с двумя трудностями.

Во-первых, класс синглтона может иметь множество статических переменных. Возможно, мы вообще не будем обращаться к объекту синглтона, а будем использовать 
какие-то другие статические переменные:

```csharp
public class Singleton
{
	private static readonly Singleton instance = new Singleton();
	public static string text = "hello";
	public string Date { get; private set; }
        
	private Singleton()
	{
		Console.WriteLine($"Singleton ctor {DateTime.Now.TimeOfDay}");
		Date = System.DateTime.Now.TimeOfDay.ToString();
	}

	public static Singleton GetInstance()
	{
		Console.WriteLine($"GetInstance {DateTime.Now.TimeOfDay}");
		Thread.Sleep(500);
		return instance;
	}
}
class Program
{
	static void Main(string[] args)
	{
		Console.WriteLine($"Main {DateTime.Now.TimeOfDay}");
		Console.WriteLine(Singleton.text);
	}
}
```

В данном случае идет только обращение к переменной text, однако статическое поле instance также будет инициализировано. Например, консольный вывод 
в данном случае мог бы выглядеть следующим образом:

```csharp
Singleton ctor 16:05:54.1469982
Main 16:05:54.2920316
hello
```

В данном случае мы видим, что статическое поле instance инициализировано.

Для решения этой проблемы выделим отдельный внутренний класс в рамках класса синглтона:

```csharp
public class Singleton
{
	public string Date { get; private set; }
	public static string text = "hello";
	private Singleton()
	{
		Console.WriteLine($"Singleton ctor {DateTime.Now.TimeOfDay}");
		Date = DateTime.Now.TimeOfDay.ToString();
	}

	public static Singleton GetInstance()
	{
		Console.WriteLine($"GetInstance {DateTime.Now.TimeOfDay}");
		return Nested.instance;
	}

	private class Nested
	{
		internal static readonly Singleton instance = new Singleton();
	}
}
class Program
{
	static void Main(string[] args)
	{
		Console.WriteLine($"Main {DateTime.Now.TimeOfDay}");
		Console.WriteLine(Singleton.text);
	}
}
```

Теперь статическая переменная, которая представляет объект синглтона, определена во вложенном классе Nested. Чтобы к этой переменной 
можно было обращаться из класса синглтона, она имеет модификатор internal, в то же время сам класс Nested имеет модификатор private, 
что позволяет гарантировать, что данный класс будет доступен только из класса Singleton.

Консольный вывод в данном случае мог бы выглядеть следующим образом:

```csharp
Main 16:11:40.1320873
hello
```

### Реализация через класс Lazy<T>

Еще один способ создания синглтона представляет использование класса Lazy<T>:

```csharp
public class Singleton
{
    private static readonly Lazy<Singleton> lazy = 
		new Lazy<Singleton>(() => new Singleton());

    public string Name { get; private set; }
        
    private Singleton()
    {
        Name = System.Guid.NewGuid().ToString();
    }
	
    public static Singleton GetInstance()
    {
        return lazy.Value;
    }
}
```

**Источник:** [https://metanit.com/sharp/patterns/2.3.php](https://metanit.com/sharp/patterns/2.3.php)

[[Языки программирования/C#/Руководства/Паттерны проектирования/Глава 2. Порождающие паттерны/Абстрактная фабрика (Abstract Factory)|Назад]] | [[Языки программирования/C#/Руководства/Паттерны проектирования/Глава 2. Порождающие паттерны|Порождающие паттерны]] | [[Языки программирования/C#/Руководства/Паттерны проектирования/Глава 2. Порождающие паттерны/Прототип (Prototype)|Вперёд]]
