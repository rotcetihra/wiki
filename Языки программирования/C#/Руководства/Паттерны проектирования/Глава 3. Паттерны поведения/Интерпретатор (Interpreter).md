# Интерпретатор (Interpreter)

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Руководства|Руководства]] / [[Языки программирования/C#/Руководства/Паттерны проектирования|Паттерны проектирования]] / [[Языки программирования/C#/Руководства/Паттерны проектирования/Глава 3. Паттерны поведения|Паттерны поведения]] / Интерпретатор (Interpreter)

[[Языки программирования/C#/Руководства/Паттерны проектирования/Глава 3. Паттерны поведения/Цепочка обязанностей (Chain of Responsibility)|Назад]] | [[Языки программирования/C#/Руководства/Паттерны проектирования/Глава 3. Паттерны поведения|Паттерны поведения]] | [[Языки программирования/C#/Руководства/Паттерны проектирования/Глава 3. Паттерны поведения/Посредник (Mediator)|Вперёд]]

**Дата написания:** 05.09.2026

## Интерпретатор (Interpreter)

Паттерн Интерпретатор (Interpreter) определяет представление грамматики для заданного языка и интерпретатор предложений этого языка. Как правило, 
данный шаблон проектирования применяется для часто повторяющихся операций.

Хотя паттерн требует понимания теории формальных языков и грамматик, на самом деле он не так сложен в понимании.

С помощью диаграмм UML паттерн можно описать так:

На языке C# формальная структура программы могла бы выглядеть следующим образом:class Client
{
    void Main()
    {
        Context context = new Context();

        var expression = new NonterminalExpression();
        expression.Interpret(context);

    }
}

class Context
{
}

abstract class AbstractExpression
{
    public abstract void Interpret(Context context);
}

class TerminalExpression : AbstractExpression
{
    public override void Interpret(Context context)
    {
    }
}

class NonterminalExpression : AbstractExpression
{
    AbstractExpression expression1;
    AbstractExpression expression2;
    public override void Interpret(Context context)
    {
            
    }
}УчастникиAbstractExpression: определяет интерфейс выражения, объявляет методInterpret()TerminalExpression: терминальное выражение, реализует методInterpret()для терминальных 
символов грамматики. Для каждого символа грамматики создается свой объект TerminalExpressionNonterminalExpression: нетерминальное выражение, представляет 
правило грамматики. Для каждого отдельного правила грамматики создается свой объект NonterminalExpression.Context: содержит общую для интерпретатора информацию. Может использоваться объектами терминальных и 
нетерминальных выражений для сохранения состояния операций и последующего доступа к сохраненному состояниюClient: строит предложения языка с данной грамматикой в виде абстрактного синтаксического дерева, 
узлами которого являются объекты TerminalExpression и NonterminalExpressionМетоды Interpret в нетерминальных выражениях позволяют реализовать правила грамматики. При этом мы легко может добавить 
новые правила грамматики, определив новые объекты NonterminalExpression со своей реализацией метода Interpret. Однако 
данный паттерн подходит только для тех случаев, когда правила грамматики относительно простые. В более сложных случаях 
следует выбирать другие способы проектирования приложения.Например, нам надо разработать программ для вычислений простейших операций сложения и вычитания с помощью переменных:x + y - z. Для этого 
можно определить следующую грамматику:IExpression ::= NumberExpression | Constant | AddExpression | SubtractExpression
AddExpression ::= IExpression + IExpression
SubtractExpression ::= IExpression - IExpression
NumberExpression ::= [A-Z,a-z]+
Constant ::= [1-9]+Реализация этой грамматики на языке C# будет следующая программа:class Program
{
    static void Main(string[] args)
    {
        Context context = new Context();
		// определяем набор переменных
        int x = 5;
        int y = 8;
        int z = 2;
		
		// добавляем переменные в контекст
        context.SetVariable("x", x);
        context.SetVariable("y", y);
        context.SetVariable("z", z);
		// создаем объект для вычисления выражения x + y - z
        IExpression expression = new SubtractExpression(
            new AddExpression(
                new NumberExpression("x"), new NumberExpression("y")
			),
            new NumberExpression("z")
		);

        int result = expression.Interpret(context);
        Console.WriteLine("результат: {0}", result);

        Console.Read();
    }
}

class Context
{
    Dictionary<string, int> variables;
    public Context()
    {
        variables = new Dictionary<string, int>();
    }
	// получаем значение переменной по ее имени
    public int GetVariable(string name)
    {
        return variables[name];
    }

    public void SetVariable(string name, int value)
    {
        if (variables.ContainsKey(name))
            variables[name] = value;
        else
            variables.Add(name, value);
    }
}
// интерфейс интерпретатора
interface IExpression
{
    int Interpret(Context context);
}
// терминальное выражение
class NumberExpression : IExpression
{
    string name; // имя переменной
    public NumberExpression(string variableName)
    {
        name = variableName;
    }
    public int Interpret(Context context)
    {
        return context.GetVariable(name);
    }
}
// нетерминальное выражение для сложения
class AddExpression : IExpression
{
    IExpression leftExpression;
    IExpression rightExpression;

    public AddExpression(IExpression left, IExpression right)
    {
        leftExpression = left;
        rightExpression = right;
    }

    public int Interpret(Context context)
    {
        return leftExpression.Interpret(context) + rightExpression.Interpret(context);
    }
}
 // нетерминальное выражение для вычитания
class SubtractExpression : IExpression
{
    IExpression leftExpression;
    IExpression rightExpression;

    public SubtractExpression(IExpression left, IExpression right)
    {
        leftExpression = left;
        rightExpression = right;
    }

    public int Interpret(Context context)
    {
        return leftExpression.Interpret(context) - rightExpression.Interpret(context);
    }
}В данном случае все действия интерпретатора можно описать следующим деревом:Класс Context определяет методы для установки значений переменных и для получения их значений.В качестве интерпретатора используется интерфейсIExpression. Его реализация - класс NumberExpression предназначен 
для выражения отдельных переменных - это терминальные объекты.Другие реализации интерфейса - классы AddExpression и SubtractExpression представляют нетерминальные объекты. 
Они реализуют простейшие операции сложения и вычитания и могут рекурсивно обращаться к методам Interpret используемых 
терминальных и нетерминальных объектов.Клиент, в роли которого выступает класс Program, инициализирует контекст и для вычисления выражения x + y - z создается объект SubtractExpression, который в качестве параметров принимает другие объекты IExpression.

**Источник:** [https://metanit.com/sharp/patterns/3.8.php](https://metanit.com/sharp/patterns/3.8.php)

[[Языки программирования/C#/Руководства/Паттерны проектирования/Глава 3. Паттерны поведения/Цепочка обязанностей (Chain of Responsibility)|Назад]] | [[Языки программирования/C#/Руководства/Паттерны проектирования/Глава 3. Паттерны поведения|Паттерны поведения]] | [[Языки программирования/C#/Руководства/Паттерны проектирования/Глава 3. Паттерны поведения/Посредник (Mediator)|Вперёд]]
