# Посредник (Mediator)

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Руководства|Руководства]] / [[Языки программирования/C#/Руководства/Паттерны проектирования|Паттерны проектирования]] / [[Языки программирования/C#/Руководства/Паттерны проектирования/Глава 3. Паттерны поведения|Паттерны поведения]] / Посредник (Mediator)

[[Языки программирования/C#/Руководства/Паттерны проектирования/Глава 3. Паттерны поведения/Интерпретатор (Interpreter)|Назад]] | [[Языки программирования/C#/Руководства/Паттерны проектирования/Глава 3. Паттерны поведения|Паттерны поведения]] | [[Языки программирования/C#/Руководства/Паттерны проектирования/Глава 3. Паттерны поведения/Хранитель (Memento)|Вперёд]]

**Дата написания:** 05.09.2026

## Посредник (Mediator)

Паттерн Посредник (Mediator) представляет такой шаблон проектирования, который обеспечивает взаимодействие множества объектов 
без необходимости ссылаться друг на друга. Тем самым достигается слабосвязанность взаимодействующих объектов.

Когда используется паттерн Посредник?

- Когда имеется множество взаимосвязаных объектов, связи между которыми сложны и запутаны.
- Когда необходимо повторно использовать объект, однако повторное использование затруднено в силу сильных связей с другими объектами.

Схематично с помощью UML паттерн можно описать следующим образом:

Формальная структура классов и связей между ними с применением паттерна на языке C#:abstract class Mediator
{
    public abstract void Send(string msg, Colleague colleague);
}

abstract class Colleague
{
    protected Mediator mediator;

    public Colleague(Mediator mediator)
    {
        this.mediator = mediator;
    }
}

class ConcreteColleague1 : Colleague
{
    public ConcreteColleague1(Mediator mediator)
        : base(mediator)
    { }
 
    public void Send(string message)
    {
        mediator.Send(message, this);
    }
 
    public void Notify(string message)
    { }
}

class ConcreteColleague2 : Colleague
{
    public ConcreteColleague2(Mediator mediator)
        : base(mediator)
    { }
 
    public void Send(string message)
    {
        mediator.Send(message, this);
    }
 
    public void Notify(string message)
    { }
}

class ConcreteMediator : Mediator
{
    public ConcreteColleague1 Colleague1 { get; set; }
    public ConcreteColleague2 Colleague2 { get; set; }
    public override void Send(string msg, Colleague colleague)
    {
        if (Colleague1 == colleague)
            Colleague2.Notify(msg);
        else
            Colleague1.Notify(msg);
    }
}УчастникиMediator: представляет интерфейс для взаимодействия с объектами ColleagueColleague: представляет интерфейс для взаимодействия с объектом MediatorConcreteColleague1иConcreteColleague2: конкретные классы коллег, 
которые обмениваются друг с другом через объект MediatorConcreteMediator: конкретный посредник, реализующий интерфейс типа MediatorРассмотрим реальный пример. Система создания программных продуктов включает ряд акторов: заказчики, программисты, тестировщики и так далее. 
Но нередко все эти акторы взаимодействуют между собой не непосредственно, а опосредованно через менеджера проектов. То есть менеджер проектов 
выполняет роль посредника. В этом случае процесс взаимодействия между объектами мы могли бы описать так:class Program
{
    static void Main(string[] args)
    {
        ManagerMediator mediator = new ManagerMediator();
        Colleague customer = new CustomerColleague(mediator);
        Colleague programmer = new ProgrammerColleague(mediator);
        Colleague tester = new TesterColleague(mediator);
        mediator.Customer = customer;
        mediator.Programmer = programmer;
        mediator.Tester = tester;
        customer.Send("Есть заказ, надо сделать программу");
        programmer.Send("Программа готова, надо протестировать");
        tester.Send("Программа протестирована и готова к продаже");

        Console.Read();
    }
}

abstract class Mediator
{
    public abstract void Send(string msg, Colleague colleague);
}
abstract class Colleague
{
    protected Mediator mediator;

    public Colleague(Mediator mediator)
    {
        this.mediator = mediator;
    }

    public virtual void Send(string message)
    {
        mediator.Send(message, this);
    }
    public abstract void Notify(string message);
}
// класс заказчика
class CustomerColleague : Colleague
{
    public CustomerColleague(Mediator mediator)
        : base(mediator)
    { }

    public override void Notify(string message)
    {
        Console.WriteLine("Сообщение заказчику: " + message);
    }
}
// класс программиста
class ProgrammerColleague : Colleague
{
    public ProgrammerColleague(Mediator mediator)
        : base(mediator)
    { }

    public override void Notify(string message)
    {
        Console.WriteLine("Сообщение программисту: " + message);
    }
}
// класс тестера
class TesterColleague : Colleague
{
    public TesterColleague(Mediator mediator)
        : base(mediator)
    { }

    public override void Notify(string message)
    {
        Console.WriteLine("Сообщение тестеру: " + message);
    }
}

class ManagerMediator : Mediator
{
    public Colleague Customer { get; set; }
    public Colleague Programmer { get; set; }
    public Colleague Tester { get; set; }
    public override void Send(string msg, Colleague colleague)
    {
		// если отправитель - заказчик, значит есть новый заказ
		// отправляем сообщение программисту - выполнить заказ
        if (Customer == colleague)
            Programmer.Notify(msg);
		// если отправитель - программист, то можно приступать к тестированию
		// отправляем сообщение тестеру
        else if (Programmer == colleague)
            Tester.Notify(msg);
		// если отправитель - тест, значит продукт готов
		// отправляем сообщение заказчику
        else if (Tester == colleague)
            Customer.Notify(msg);
    }
}Класс менеджера - ManagerMediator в методеSend()проверяет, от кого пришло сообщение, и в зависимости от 
отправителя перенаправляет его другому объекту с помощью методовNotify(), определенных в классе Colleague.Консольный вывод программы:Сообщение программисту: Есть заказ, надо сделать программу
Сообщение тестеру: Программа готова, надо протестировать
Сообщение заказчику: Программа протестирована и готова к продажеВ итоге применение паттерна Посредник дает нам следующие преимущества:Устраняется сильная связанность между объектами ColleagueУпрощается взаимодействие между объектами: вместо связей по типу "все-ко-всем" применяется связь "один-ко-всем"Взаимодействие между объектами абстрагируется и выносится в отдельный интерфейсЦентрализуется управления отношениями между объектами

**Источник:** [https://metanit.com/sharp/patterns/3.9.php](https://metanit.com/sharp/patterns/3.9.php)

[[Языки программирования/C#/Руководства/Паттерны проектирования/Глава 3. Паттерны поведения/Интерпретатор (Interpreter)|Назад]] | [[Языки программирования/C#/Руководства/Паттерны проектирования/Глава 3. Паттерны поведения|Паттерны поведения]] | [[Языки программирования/C#/Руководства/Паттерны проектирования/Глава 3. Паттерны поведения/Хранитель (Memento)|Вперёд]]
