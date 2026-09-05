# Команда (Command)

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Руководства|Руководства]] / [[Языки программирования/C#/Руководства/Паттерны проектирования|Паттерны проектирования]] / [[Языки программирования/C#/Руководства/Паттерны проектирования/Глава 3. Паттерны поведения|Паттерны поведения]] / Команда (Command)

[[Языки программирования/C#/Руководства/Паттерны проектирования/Глава 3. Паттерны поведения/Наблюдатель (Observer)|Назад]] | [[Языки программирования/C#/Руководства/Паттерны проектирования/Глава 3. Паттерны поведения|Паттерны поведения]] | [[Языки программирования/C#/Руководства/Паттерны проектирования/Глава 3. Паттерны поведения/Шаблонный метод (Template Method)|Вперёд]]

**Дата написания:** 05.09.2026

## Команда (Command)

Паттерн "Команда" (Command) позволяет инкапсулировать запрос на выполнение определенного действия в виде отдельного объекта. Этот объект запроса 
на действие и называется командой. При этом объекты, инициирующие запросы на выполнение действия, отделяются от объектов, которые выполняют это действие.

Команды могут использовать параметры, которые передают ассоциированную с командой информацию. Кроме того, команды могут ставиться в очередь и также 
могут быть отменены.

### Когда использовать команды?

Когда надо передавать в качестве параметров определенные действия, вызываемые в ответ на другие действия. То есть когда необходимы 
функции обратного действия в ответ на определенные действия.

Когда необходимо обеспечить выполнение очереди запросов, а также их возможную отмену.

Когда надо поддерживать логгирование изменений в результате запросов. Использование логов может помочь восстановить состояние системы - 
для этого необходимо будет использовать последовательность запротоколированных команд.

Схематично в UML паттерн Команда представляется следующим образом:

Формальное определение на языке C# может выглядеть следующим образом:abstract class Command
{
    public abstract void Execute();
    public abstract void Undo();
}
// конкретная команда
class ConcreteCommand : Command
{
    Receiver receiver;
    public ConcreteCommand(Receiver r)
    {
        receiver = r;
    }
    public override void Execute()
    {
        receiver.Operation();
    }

    public override void Undo()
    {}
}

// получатель команды
class Receiver
{
    public void Operation()
    { }
}
// инициатор команды
class Invoker
{
    Command command;
    public void SetCommand(Command c)
    {
        command = c;
    }
    public void Run()
    {
        command.Execute();
    }
	public void Cancel()
    {
        command.Undo();
    }
}
class Client
{  
    void Main()
    {
        Invoker invoker = new Invoker();
        Receiver receiver = new Receiver();
        ConcreteCommand command=new ConcreteCommand(receiver);
        invoker.SetCommand(command);
        invoker.Run();
    }
}УчастникиCommand: интерфейс, представляющий команду. Обычно определяет методExecute()для выполнения 
действия, а также нередко включает методUndo(), реализация которого должна заключаться в отмене действия командыConcreteCommand: конкретная реализация команды, реализует методExecute(), в котором вызывается определенный метод, 
определенный в классе ReceiverReceiver: получатель команды. Определяет действия, которые должны выполняться в результате запроса.Invoker: инициатор команды - вызывает команду для выполнения определенного запросаClient: клиент - создает команду и устанавливает ее получателя с помощью методаSetCommand()Таким образом, инициатор, отправляющий запрос, ничего не знает о получателе, который и будет выполнять команду. Кроме того, если нам потребуется 
применить какие-то новые команды, мы можем просто унаследовать классы от абстрактного класса Command и реализовать его методы Execute и Undo.В программах на C# команды находят довольно широкое применение. Так, в технологии WPF и других технологиях, которые используют XAML и подход MVVM, 
на командах во многом базируется взаимодействие с пользователем. В некоторых архитектурах, например, в архитектуре CQRS, команды являются одним из 
ключевых компонентов.Нередко в роли инициатора команд выступают панели управления или кнопки интерфейса. Самая простая ситуация - надо программно 
организовать включение и выключение прибора, например, телевизора. Решение данной задачи с помощью команд могло бы выглядеть так:class Program
{
	static void Main(string[] args)
    {
        Pult pult = new Pult();
        TV tv = new TV();
        pult.SetCommand(new TVOnCommand(tv));
        pult.PressButton();
        pult.PressUndo();
        
        Console.Read();
    }
}

interface ICommand
{
    void Execute();
    void Undo();
}

// Receiver - Получатель
class TV
{ 
    public void On()
    {
        Console.WriteLine("Телевизор включен!");
    }

    public void Off()
    {
        Console.WriteLine("Телевизор выключен...");
    }
}

class TVOnCommand : ICommand
{
    TV tv;
    public TVOnCommand(TV tvSet)
    {
        tv = tvSet;
    }
    public void Execute()
    {
        tv.On();
    }
    public void Undo()
    {
        tv.Off();
    }
}

// Invoker - инициатор
class Pult
{
    ICommand command;

    public Pult() { }

    public void SetCommand(ICommand com)
    {
        command = com;
    }

    public void PressButton()
    {
        command.Execute();
    }
    public void PressUndo()
    {
        command.Undo();
    }
}Итак, в этой программе есть интерфейс команды - ICommand, есть ее реализация в виде класса TVOnCommand, есть инициатор команды - класс 
Pult, некий прибор - пульт, управляющий телевизором. И есть получатель команды - класс TV, представляющий телевизор. В качестве клиента используется класс Program.При этом пульт ничего не знает об объекте TV. Он только знает, как отправить команду. В итоге мы получаем гибкую систему, в которой мы легко можем заменять 
одни команды на другие, создавать последовательности команд. Например, в нашей программе кроме телевизора появилась микроволновка, которой тоже неплохо было бы управлять с 
помощью одного интерфейса. Для этого достаточно добавить соответствующие классы и установить команду:class Program
{
    static void Main(string[] args)
    {
        Pult pult = new Pult();
        TV tv = new TV();
        pult.SetCommand(new TVOnCommand(tv));
        pult.PressButton();
        pult.PressUndo();

        Microwave microwave = new Microwave
		// 5000 - время нагрева пищи
        pult.SetCommand(new MicrowaveCommand(microwave, 5000));
        pult.PressButton();
        
        Console.Read();
    }
}
//.....ранее описанные классы

class Microwave
{
    public void StartCooking(int time)
    {
        Console.WriteLine("Подогреваем еду");
        // имитация работы с помощью асинхронного метода Task.Delay
        Task.Delay(time).GetAwaiter().GetResult();
    }

    public void StopCooking()
    {
        Console.WriteLine("Еда подогрета!");
    }
}
class MicrowaveCommand : ICommand
{
    Microwave microwave;
    int time;
    public MicrowaveCommand(Microwave m, int t)
    {
        microwave = m;
        time = t;
    }
    public void Execute()
    {
        microwave.StartCooking(time);
        microwave.StopCooking();
    }

    public void Undo()
    {
        microwave.StopCooking();
    }
}Теперь еще одним получателем запроса является класс Microwave, функциональностью которого можно управлять через команды MicrowaveCommand.Правда, в вышеописанной системе есть один изъян: если мы попытаемся выполнить команду до ее назначения, то программа выдаст исключение, 
так как команда будет не установлена. Эту проблему мы могли бы решить, проверяя команду на значение null в классе инициатора:class Pult
{
    ICommand command;

    public Pult() { }

    public void SetCommand(ICommand com)
    {
        command = com;
    }

    public void PressButton()
    {
        if(command!=null)
            command.Execute();
    }
    public void PressUndo()
    {
		if(command!=null)
            command.Undo();
    }
}Либо можно определить класс пустой команды, которая будет устанавливаться по умолчанию:class NoCommand : ICommand
{
    public void Execute()
    {
    }
    public void Undo()
    {
    }
}
class Pult
{
    ICommand command;

    public Pult() 
	{ 
		command = new NoCommand();
	}

    public void SetCommand(ICommand com)
    {
        command = com;
    }

    public void PressButton()
    {
        command.Execute();
    }
    public void PressUndo()
    {
		command.Undo();
    }
}При этом инициатор необязательно указывает на одну команду. Он может управлять множеством команд. Например, на пульте от телевизора есть 
как кнопка для включения, так и кнопки для регулировки звука:class Program
{
    static void Main(string[] args)
    {
        TV tv = new TV();
        Volume volume = new Volume();
        MultiPult mPult = new MultiPult();
        mPult.SetCommand(0, new TVOnCommand(tv));
        mPult.SetCommand(1, new VolumeCommand(volume));
		// включаем телевизор
        mPult.PressButton(0);
		// увеличиваем громкость
        mPult.PressButton(1);
        mPult.PressButton(1);
        mPult.PressButton(1);
		// действия отмены
        mPult.PressUndoButton();
        mPult.PressUndoButton();
        mPult.PressUndoButton();
        mPult.PressUndoButton();

		Console.Read();
    }
}
interface Command
{
    void Execute();
    void Undo();
}

class TV
{ 
    public void On()
    {
        Console.WriteLine("Телевизор включен!");
    }

    public void Off()
    {
        Console.WriteLine("Телевизор выключен...");
    }
}

class TVOnCommand : ICommand
{
    TV tv;
    public TVOnCommand(TV tvSet)
    {
        tv = tvSet;
    }
    public void Execute()
    {
        tv.On();
    }
    public void Undo()
    {
        tv.Off();
    }
}
class Volume
{
    public const int OFF = 0;
    public const int HIGH = 20;
    private int level;

    public Volume()
    {
        level = OFF;
    }

    public void RaiseLevel()
    {
        if (level < HIGH)
            level++;
        Console.WriteLine("Уровень звука {0}", level);
    }
    public void DropLevel()
    {
        if (level > OFF)
            level--;
        Console.WriteLine("Уровень звука {0}", level);
    }
}

class VolumeCommand : ICommand
{
    Volume volume;
    public VolumeCommand(Volume v)
    {
        volume = v;
    }
    public void Execute()
    {
        volume.RaiseLevel();
    }

    public void Undo()
    {
        volume.DropLevel();
    }
}

class NoCommand : ICommand
{
    public void Execute()
    {
    }
    public void Undo()
    {
    }
}

class MultiPult
{
    ICommand[] buttons;
    Stack<ICommand> commandsHistory;

    public MultiPult()
    {
        buttons = new ICommand[2];
        for (int i = 0; i < buttons.Length; i++)
        {
            buttons[i] = new NoCommand();
        }
        commandsHistory = new Stack<ICommand>();
    }

    public void SetCommand(int number, ICommand com)
    {
        buttons[number] = com;
    }

    public void PressButton(int number)
    {
        buttons[number].Execute();
		// добавляем выполненную команду в историю команд
        commandsHistory.Push(buttons[number]);
    }
    public void PressUndoButton()
    {
        if(commandsHistory.Count>0)
        {
            ICommand undoCommand = commandsHistory.Pop();
            undoCommand.Undo();
        }
    }
}Здесь два получателя команд - классы TV и Volume. Volume управляет уровнем звука и сохраняет текущий уровень в переменной level. 
Также есть две команды TVOnCommand и VolumeCommand.Инициатор - MultiPult имеет две кнопки в виде массива buttons: первая предназначена 
для TV, а вторая - для увеличения уровня звука. Чтобы сохранить историю команд используется стек. При отправке команды в стек добавляется 
новый элемент, а при ее отмене, наоборот, происходит удаление из стека. В данном случае стек выполняет роль примитивного лога команд.Телевизор включен!
Уровень звука 1
Уровень звука 2
Уровень звука 3
Уровень звука 2
Уровень звука 1
Уровень звука 0
Телевизор выключен...МакрокомандыДля управления набором команд используются макрокоманды. Макрокоманда должна реализовать тот же интерфейс, что и другие команды, 
при этом макрокоманда инкапсулирует в одной из своих переменных весь набор используемых команд. Рассмотрим на примере.Для создания и развития программного продукта необходимо несколько исполнителей, выполняющих различные функции: программист пишет код, 
тестировщик выполняет тестирование продукта, а маркетолог пишет рекламные материалы и проводит кампании по рекламированию продукта. Управляет 
всем процессом менеджер. Программа на C#, описывающая создание программного продукта с помощью паттерна команд, могла бы выглядеть следующим образом:class Program
{
    static void Main(string[] args)
    {
        Programmer programmer = new Programmer();
        Tester tester = new Tester();
        Marketolog marketolog = new Marketolog();

        List<ICommand> commands = new List<ICommand> 
        {
            new CodeCommand(programmer),
            new TestCommand(tester),
            new AdvertizeCommand(marketolog)
        };
        Manager manager = new Manager();
        manager.SetCommand(new MacroCommand(commands));
        manager.StartProject();
        manager.StopProject();
        
		Console.Read();
    }
}
interface ICommand
{
    void Execute();
    void Undo();
}
// Класс макрокоманды
class MacroCommand : ICommand
{
    List<ICommand> commands;
    public MacroCommand(List<ICommand> coms)
    {
        commands = coms;
    }
    public void Execute()
    {
        foreach(ICommand c in commands)
            c.Execute();
    }

    public void Undo()
    {
        foreach (ICommand c in commands)
            c.Undo();
    }
}

class Programmer
{
    public void StartCoding()
    {
        Console.WriteLine("Программист начинает писать код");
    }
    public void StopCoding()
    {
        Console.WriteLine("Программист завершает писать код");
    }
}

class Tester
{
    public void StartTest()
    {
        Console.WriteLine("Тестировщик начинает тестирование");
    }
    public void StopTest()
    {
        Console.WriteLine("Тестировщик завершает тестирование");
    }
}

class Marketolog
{
    public void StartAdvertize()
    {
        Console.WriteLine("Маркетолог начинает рекламировать продукт");
    }
    public void StopAdvertize()
    {
        Console.WriteLine("Маркетолог прекращает рекламную кампанию");
    }
}

class CodeCommand : ICommand
{
    Programmer programmer;
    public CodeCommand(Programmer p)
    {
        programmer = p;
    }
    public void Execute()
    {
        programmer.StartCoding();
    }
	public void Undo()
    {
        programmer.StopCoding();
    }
}

class TestCommand : ICommand
{
    Tester tester;
    public TestCommand(Tester t)
    {
        tester = t;
    }
    public void Execute()
    {
        tester.StartTest();
    }
	public void Undo()
    {
        tester.StopTest();
    }
}

class AdvertizeCommand : ICommand
{
    Marketolog marketolog;
    public AdvertizeCommand(Marketolog m)
    {
        marketolog = m;
    }
    public void Execute()
    {
        marketolog.StartAdvertize();
    }

    public void Undo()
    {
        marketolog.StopAdvertize();
    }
}

class Manager
{
    ICommand command;
    public void SetCommand(ICommand com)
    {
        command = com;
    }
    public void StartProject()
    {
        if (command != null)
            command.Execute();
    }
    public void StopProject()
    {
        if (command != null)
            command.Undo();
    }
}В роли инициатора здесь выступает менеджер, а в роли получателей запросов - программист, маркетолог и тестеровщик. Запуская проект, менеджер тем 
самым запускает макрокоманду, которая содержит ряд отдельных команд. Выполнение этих команд делегируется получателям.

**Источник:** [https://metanit.com/sharp/patterns/3.3.php](https://metanit.com/sharp/patterns/3.3.php)

[[Языки программирования/C#/Руководства/Паттерны проектирования/Глава 3. Паттерны поведения/Наблюдатель (Observer)|Назад]] | [[Языки программирования/C#/Руководства/Паттерны проектирования/Глава 3. Паттерны поведения|Паттерны поведения]] | [[Языки программирования/C#/Руководства/Паттерны проектирования/Глава 3. Паттерны поведения/Шаблонный метод (Template Method)|Вперёд]]
