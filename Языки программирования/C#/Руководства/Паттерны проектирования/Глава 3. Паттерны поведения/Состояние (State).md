# Состояние (State)

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Руководства|Руководства]] / [[Языки программирования/C#/Руководства/Паттерны проектирования|Паттерны проектирования]] / [[Языки программирования/C#/Руководства/Паттерны проектирования/Глава 3. Паттерны поведения|Паттерны поведения]] / Состояние (State)

[[Языки программирования/C#/Руководства/Паттерны проектирования/Глава 3. Паттерны поведения/Итератор (Iterator)|Назад]] | [[Языки программирования/C#/Руководства/Паттерны проектирования/Глава 3. Паттерны поведения|Паттерны поведения]] | [[Языки программирования/C#/Руководства/Паттерны проектирования/Глава 3. Паттерны поведения/Цепочка обязанностей (Chain of Responsibility)|Вперёд]]

**Дата написания:** 05.09.2026

## Состояние (State)

Состояние (State) - шаблон проектирования, который позволяет объекту изменять свое поведение в зависимости от внутреннего состояния.

### Когда применяется данный паттерн?

- Когда поведение объекта должно зависеть от его состояния и может изменяться динамически во время выполнения
- Когда в коде методов объекта используются многочисленные условные конструкции, выбор которых зависит от текущего состояния объекта

UML-диаграмма данного шаблона проектирования предлагает следующую систему:

Формальное определение паттерна на C#:class Program
{
    static void Main()
    {
        Context context = new Context(new StateA());
        context.Request(); // Переход в состояние StateB
        context.Request();	// Переход в состояние StateA
    }
}
abstract class State
{
    public abstract void Handle(Context context);
}
class StateA : State
{
    public override void Handle(Context context)
    {
		context.State = new StateB();
	}
}
class StateB : State
{
    public override void Handle(Context context)
    { 
		context.State = new StateA();
	}
}

class Context
{
    public State State { get; set; }
    public Context(State state)
    {
        this.State = state;
    }
    public void Request()
    {
        this.State.Handle(this);
    }
}Участники паттернаState: определяет интерфейс состоянияКлассыStateAиStateB- конкретные реализации состоянийContext: представляет объект, поведение которого должно динамически изменяться в соответствии с состоянием. 
Выполнение же конкретных действий делегируется объекту состоянияНапример, вода может находиться в ряде состояний: твердое, жидкое, парообразное. Допустим, нам надо определить 
класс Вода, у которого бы имелись методы для нагревания и заморозки воды. Без использования паттерна Состояние мы 
могли бы написать следующую программу:class Program
{
    static void Main(string[] args)
    {
        Water water = new Water(WaterState.LIQUID);
        water.Heat();
        water.Frost();
        water.Frost();

        Console.Read();
    }
}
enum WaterState
{
    SOLID,
    LIQUID,
    GAS
}
class Water
{
    public WaterState State { get; set; }

    public Water(WaterState ws)
    {
		State = ws;
    }

    public void Heat()
    {
        if(State==WaterState.SOLID)
        {
            Console.WriteLine("Превращаем лед в жидкость");
            State = WaterState.LIQUID;
        }
        else if (State == WaterState.LIQUID)
        {
            Console.WriteLine("Превращаем жидкость в пар");
            State = WaterState.GAS;
        }
        else if (State == WaterState.GAS)
        {
            Console.WriteLine("Повышаем температуру водяного пара");
        }
    }
    public void Frost()
    {
        if (State == WaterState.LIQUID)
        {
            Console.WriteLine("Превращаем жидкость в лед");
            State = WaterState.SOLID;
        }
        else if (State == WaterState.GAS)
        {
            Console.WriteLine("Превращаем водяной пар в жидкость");
            State = WaterState.LIQUID;
        }
    }
}Вода имеет три состояния, и в каждом методе нам надо смотреть на текущее состояние, чтобы произвести действия. В итоге с трех состояний уже 
получается нагромождение условных конструкций. Да и самим методов в классе Вода может также быть множество, где также надо будет действовать в зависимости от состояния. Поэтому, 
чтобы сделать программу более гибкой, в данном случае мы можем применить паттерн Состояние:class Program
{
    static void Main(string[] args)
    {
        Water water = new Water(new LiquidWaterState());
        water.Heat();
        water.Frost();
        water.Frost();

        Console.Read();
    }
}
 class Water
    {
        public IWaterState State { get; set; }

        public Water(IWaterState ws)
        {
            State = ws;
        }

        public void Heat()
        {
            State.Heat(this);
        }
        public void Frost()
        {
            State.Frost(this);
        }
    }

interface IWaterState
{
    void Heat(Water water);
    void Frost(Water water);
}

class SolidWaterState : IWaterState
{
    public void Heat(Water water)
    {
        Console.WriteLine("Превращаем лед в жидкость");
        water.State = new LiquidWaterState();
    }

    public void Frost(Water water)
    {
        Console.WriteLine("Продолжаем заморозку льда");
    }
}
class LiquidWaterState : IWaterState
{
	public void Heat(Water water)
    {
        Console.WriteLine("Превращаем жидкость в пар");
        water.State = new GasWaterState();
    }

    public void Frost(Water water)
    {
        Console.WriteLine("Превращаем жидкость в лед");
        water.State = new SolidWaterState();
    }
}
class GasWaterState : IWaterState
{
	public void Heat(Water water)
    {
        Console.WriteLine("Повышаем температуру водяного пара");
    }

    public void Frost(Water water)
    {
        Console.WriteLine("Превращаем водяной пар в жидкость");
        water.State = new LiquidWaterState();
    }
}Таким образом, реализация паттерна Состояние позволяет вынести поведение, зависящее от текущего состояния объекта, в отдельные классы, и избежать 
перегруженности методов объекта условными конструкциями, как if..else или switch. Кроме того, при необходимости мы можем ввести в систему 
новые классы состояний, а имеющиеся классы состояний использовать в других объектах.

**Источник:** [https://metanit.com/sharp/patterns/3.6.php](https://metanit.com/sharp/patterns/3.6.php)

[[Языки программирования/C#/Руководства/Паттерны проектирования/Глава 3. Паттерны поведения/Итератор (Iterator)|Назад]] | [[Языки программирования/C#/Руководства/Паттерны проектирования/Глава 3. Паттерны поведения|Паттерны поведения]] | [[Языки программирования/C#/Руководства/Паттерны проектирования/Глава 3. Паттерны поведения/Цепочка обязанностей (Chain of Responsibility)|Вперёд]]
