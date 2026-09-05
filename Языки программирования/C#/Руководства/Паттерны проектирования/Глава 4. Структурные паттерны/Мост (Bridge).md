# Мост (Bridge)

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Руководства|Руководства]] / [[Языки программирования/C#/Руководства/Паттерны проектирования|Паттерны проектирования]] / [[Языки программирования/C#/Руководства/Паттерны проектирования/Глава 4. Структурные паттерны|Структурные паттерны]] / Мост (Bridge)

[[Языки программирования/C#/Руководства/Паттерны проектирования/Глава 4. Структурные паттерны/Заместитель (Прокси)|Назад]] | [[Языки программирования/C#/Руководства/Паттерны проектирования/Глава 4. Структурные паттерны|Структурные паттерны]] | [[Языки программирования/C#/Руководства/Паттерны проектирования/Глава 4. Структурные паттерны/Приспособленец (Flyweight)|Вперёд]]

**Дата написания:** 05.09.2026

## Мост (Bridge)

Мост (Bridge) - структурный шаблон проектирования, который позволяет отделить абстракцию от реализации таким образом, чтобы и 
абстракцию, и реализацию можно было изменять независимо друг от друга.

Даже если мы отделим абстракцию от конкретных реализаций, то у нас все равно все наследуемые классы будут жестко привязаны к интерфейсу, 
определяемому в базовом абстрактном классе. Для преодоления жестких связей и служит паттерн Мост.

### Когда использовать данный паттерн?

- Когда надо избежать постоянной привязки абстракции к реализации
- Когда наряду с реализацией надо изменять и абстракцию независимо друг от друга. То есть изменения в абстракции не должно привести 
к изменениям в реализации

Общая реализация паттерна состоит в объявлении классов абстракций и классов реализаций в отдельных параллельных иерархиях классов.

Представление паттерна с помощью UML:

Связь агрегации между классами Abstraction и Implementor фактически и представляет некоторый мост между двумя параллельными иерархиями классов. 
Собственно поэтому паттерн получил название Мост.Формальное описание паттерна на языке C#:class Client
{
    static void Main()
    {
        Abstraction abstraction;
        abstraction = new RefinedAbstraction(new ConcreteImplementorA());
        abstraction.Operation();
        abstraction.Implementor=new ConcreteImplementorB();
        abstraction.Operation();
    }
}
abstract class Abstraction
{
    protected Implementor implementor;
    public Implementor Implementor
    {
        set { implementor = value; }
    }
    public Abstraction(Implementor imp)
    {
        implementor = imp;
    }
    public virtual void Operation()
    {
        implementor.OperationImp();
    }
}

abstract class Implementor
{
    public abstract void OperationImp();
}

class RefinedAbstraction : Abstraction
{
    public RefinedAbstraction(Implementor imp)
        : base(imp)
    {}
    public override void Operation()
    {
    }
}

class ConcreteImplementorA : Implementor
{
    public override void OperationImp()
    {
    }
}

class ConcreteImplementorB : Implementor
{
    public override void OperationImp()
    {
    }
}УчастникиAbstraction: определяет базовый интерфейс и хранит ссылку на объект Implementor. Выполнение операций в Abstraction 
делегируется методам объекта ImplementorRefinedAbstraction: уточненная абстракция, наследуется от Abstraction и расширяет унаследованный интерфейсImplementor: определяет базовый интерфейс для конкретных реализаций. Как правило, Implementor определяет только 
примитивные операции. Более сложные операции, которые базируются на примитивных, определяются в AbstractionConcreteImplementorAиConcreteImplementorB: конкретные реализации, которые унаследованы от ImplementorClient: использует объекты AbstractionТеперь рассмотрим реальное применение. Существует множество программистов, но одни являются фрилансерами, кто-то работает в компании 
инженером, кто-то совмещает работу в компании и фриланс. Таким образом, вырисовывается иерархия различных классов программистов. 
Но эти программисты могут работать с различными языками и технологиями. И в зависимости от выбранного языка деятельность программиста будет отличаться. 
Для решения описания данной задачи в программе на C# используем паттерн Мост:class Program
{
    static void Main(string[] args)
    {
        // создаем нового программиста, он работает с с++
        Programmer freelancer = new FreelanceProgrammer(new CPPLanguage());
        freelancer.DoWork();
        freelancer.EarnMoney();
        // пришел новый заказ, но теперь нужен c#
        freelancer.Language = new CSharpLanguage();
        freelancer.DoWork();
        freelancer.EarnMoney();

        Console.Read();
    }
}

interface ILanguage
{
    void Build();
    void Execute();
}

class CPPLanguage : ILanguage
{
    public void Build()
    {
        Console.WriteLine("С помощью компилятора C++ компилируем программу в бинарный код");
    }

    public void Execute()
    {
        Console.WriteLine("Запускаем исполняемый файл программы");
    }
}

class CSharpLanguage : ILanguage
{
    public void Build()
    {
        Console.WriteLine("С помощью компилятора Roslyn компилируем исходный код в файл exe");
    }

    public void Execute()
    {
        Console.WriteLine("JIT компилирует программу бинарный код");
        Console.WriteLine("CLR выполняет скомпилированный бинарный код");
    }
}

abstract class Programmer
{
    protected ILanguage language;
    public ILanguage Language
    {
        set { language = value; }
    }
    public Programmer (ILanguage lang)
    {
        language = lang;
    }
    public virtual void DoWork()
    {
        language.Build();
        language.Execute();
    }
    public abstract void EarnMoney();
}

class FreelanceProgrammer : Programmer
{
    public FreelanceProgrammer(ILanguage lang) : base(lang)
    {
    }
    public override void EarnMoney()
    {
        Console.WriteLine("Получаем оплату за выполненный заказ");
    }
}
class CorporateProgrammer : Programmer
{
    public CorporateProgrammer(ILanguage lang)
        : base(lang)
    {
    }
    public override void EarnMoney()
    {
        Console.WriteLine("Получаем в конце месяца зарплату");
    }
}В роли Abstraction выступает класс Programmer, а в роли Implementor - интерфейс ILanguage, который представляет язык программирования. 
В методеDoWork()класса Programmer вызываются методы объекта ILanguage.Языки CPPLanguage и CSharpLanguage определяют конкретные реализации, а классы FreelanceProgrammer и CorporateProgrammer представляют 
уточненные абстракции.Таким образом, благодаря применению паттерна реализация отделяется от абстракции. Мы можем развивать независимо две параллельные иерархии. Устраняются 
зависимости между реализацией и абстракцией во время компиляции, и мы можем менять конкретную реализацию во время выполнения.

**Источник:** [https://metanit.com/sharp/patterns/4.6.php](https://metanit.com/sharp/patterns/4.6.php)

[[Языки программирования/C#/Руководства/Паттерны проектирования/Глава 4. Структурные паттерны/Заместитель (Прокси)|Назад]] | [[Языки программирования/C#/Руководства/Паттерны проектирования/Глава 4. Структурные паттерны|Структурные паттерны]] | [[Языки программирования/C#/Руководства/Паттерны проектирования/Глава 4. Структурные паттерны/Приспособленец (Flyweight)|Вперёд]]
