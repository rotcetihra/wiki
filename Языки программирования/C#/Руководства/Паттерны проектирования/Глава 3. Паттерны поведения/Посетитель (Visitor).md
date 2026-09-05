# Посетитель (Visitor)

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Руководства|Руководства]] / [[Языки программирования/C#/Руководства/Паттерны проектирования|Паттерны проектирования]] / [[Языки программирования/C#/Руководства/Паттерны проектирования/Глава 3. Паттерны поведения|Паттерны поведения]] / Посетитель (Visitor)

[[Языки программирования/C#/Руководства/Паттерны проектирования/Глава 3. Паттерны поведения/Хранитель (Memento)|Назад]] | [[Языки программирования/C#/Руководства/Паттерны проектирования/Глава 3. Паттерны поведения|Паттерны поведения]] | [[Языки программирования/C#/Руководства/Паттерны проектирования/Глава 4. Структурные паттерны/Декоратор (Decorator)|Вперёд]]

**Дата написания:** 05.09.2026

## Посетитель (Visitor)

Паттерн Посетитель (Visitor) позволяет определить операцию для объектов других классов без изменения этих классов.

При использовании паттерна Посетитель определяются две иерархии классов: одна для элементов, для которых надо определить новую операцию, и 
вторая иерархия для посетителей, описывающих данную операцию.

Когда использовать данный паттерн?

- Когда имеется много объектов разнородных классов с разными интерфейсами, и требуется выполнить ряд операций 
над каждым из этих объектов
- Когда классам необходимо добавить одинаковый набор операций без изменения этих классов
- Когда часто добавляются новые операции к классам, при этом общая структура классов стабильна и практически не изменяется

Общая структура классов паттерна, описанная с помощью диаграмм UML:

Формальная структура на C#:class Client
{
    void Main()
    {
        var structure = new ObjectStructure();
        structure.Add(new ElementA());
        structure.Add(new ElementB());
        structure.Accept(new ConcreteVisitor1());
        structure.Accept(new ConcreteVisitor2());
    }
}

abstract class Visitor
{
    public abstract void VisitElementA(ElementA elemA);
    public abstract void VisitElementB(ElementB elemB);
}

class ConcreteVisitor1 : Visitor
{
    public override void VisitElementA(ElementA elementA)
    {
        elementA.OperationA();
    }
    public override void VisitElementB(ElementB elementB)
    {
            elementB.OperationB();
    }
}
class ConcreteVisitor2 : Visitor
{
    public override void VisitElementA(ElementA elementA)
    {
        elementA.OperationA();
    }
    public override void VisitElementB(ElementB elementB)
    {
        elementB.OperationB();
    }
}

class ObjectStructure
{
    List<Element> elements = new List<Element>();
    public void Add(Element element)
    {
        elements.Add(element);
    }
    public void Remove(Element element)
    {
        elements.Remove(element);
    }
    public void Accept(Visitor visitor)
    {
        foreach (Element element in elements)
            element.Accept(visitor);
    }
}

abstract class Element
{
    public abstract void Accept(Visitor visitor);
    public string SomeState { get; set; }
}

class ElementA : Element
{
    public override void Accept(Visitor visitor)
    {
        visitor.VisitElementA(this);
    }
    public void OperationA()
    { }
}

class ElementB : Element
{
    public override void Accept(Visitor visitor)
    {
        visitor.VisitElementB(this);
    }
    public void OperationB()
    { }
}УчастникиVisitor: интерфейс посетителя, который определяет методVisit()для каждого объекта ElementConcreteVisitor1 / ConcreteVisitor2: конкретные классы посетителей, реализуют интерфейс, определенный в Visitor.Element: определяет методAccept(), в котором в качестве параметра принимается объект VisitorElementA / ElementB: конкретные элементы, которые реализуют методAccept()ObjectStructure: некоторая структура, которая хранит объекты Element и предоставляет к ним доступ. 
Это могут быть и простые списки, и сложные составные структуры в виде деревьевСущность работы паттерна состоит в том, что вначале создает объект посетителя, который обходит или посещает все элементы в структуре 
ObjectStructure, у которой вызывается методAccept():public void Accept(Visitor visitor)
{
    foreach (Element element in elements)
                element.Accept(visitor);
}При посещении каждого элемента посещаемый элемент вызывает у посетителя метод, соответствующий данному элементу:public override void Accept(Visitor visitor)
{
    visitor.VisitElementA(this);
}В этот метод элемент передает ссылку на себя, чтобы посетитель мог получить доступ к состоянию элемента. 
А в самом посетителе уже могут вызываться методы элемента или производиться различные действия над элементом:public override void VisitElementA(ElementA elementA)
{
    elementA.OperationA();
}Данная техника еще называетсядвойной диспетчеризацией (double dispatch), когда выполнение операции зависит от имени запроса и двух 
типов получателей (объект Visitor и объект Element).Рассмотрим на примере. Как известно, нередко для разных категорий вкладчиков банки имеют свои правила: оформления вкладов, выдача кредитов, начисления 
процентов и т.д. Соответственно классы, описывающие данные объекты, тоже будут разными. Но что важно, как правило, правила обслуживания 
четко описает весь набор категорий клиентов. Например, есть физические лица, есть юридические, отдельные правила для индивидуальных или частных предпринимателей и т.д. 
Поэтому структура классов, представляющая клиентов будет относительно фиксированной, то есть не склонной к изменениям.И допустим, в какой-то момент мы решили добавить в классы клиентов функционал сериализации в html. В этом случае мы могли бы построить следующую структуру классов:interface IAccount
{
    void ToHtml();
}
// физическое лицо
class Person : IAccount
{
	public string FIO { get; set; } //Фамилия Имя Отчество
    public string AccNumber { get; set; } // номер счета

    public void ToHtml()
    {
        string result = "<table><tr><td>Свойство<td><td>Значение</td></tr>";
        result += "<tr><td>FIO<td><td>" + FIO + "</td></tr>";
        result += "<tr><td>Number<td><td>" + Number + "</td></tr></table>";
        Console.WriteLine(result);
    }
}
// юридическое лицо
class Company : IAccount
{
    public string Name { get; set; } // название
    public string RegNumber { get; set; } // гос регистрационный номер
    public string Number { get; set; } // номер счета

    public void ToHtml()
    {
        string result = "<table><tr><td>Свойство<td><td>Значение</td></tr>";
        result += "<tr><td>Name<td><td>" + Name + "</td></tr>";
        result += "<tr><td>RegNumber<td><td>" + RegNumber + "</td></tr>";
        result += "<tr><td>Number<td><td>" + Number + "</td></tr></table>";
        Console.WriteLine(result);
    }
}Каждый класс имеет свой набор свойств и с помощью методаToHtml()создает таблицу со значениями этих свойств. 
Но допустим, мы решили добавить потом еще сериализацию в формат xml. Задача относительно проста: добавить в интерфейс IAccount новый 
методToXml()и реализовать его в классах Person и Company.Но еще через некоторое время мы захотим добавить сериализацию в формат json. Однако в будущем могут появиться новые форматы, 
которые мы также захотим поддерживать. Частое внесение изменение в фиксированную структуру классов в данном случае не будет оптимально. 
И для решения этой задачи воспользуемся паттерном Посетитель:class Program
{
    static void Main(string[] args)
    {
        var structure = new Bank();
        structure.Add(new Person { Name = "Иван Алексеев", Number = "82184931" });
        structure.Add(new Company {Name="Microsoft", RegNumber="ewuir32141324", Number="3424131445"});
        structure.Accept(new HtmlVisitor());
        structure.Accept(new XmlVisitor());

        Console.Read();
    }
}

interface IVisitor
{
    void VisitPersonAcc(Person acc);
    void VisitCompanyAc(Company acc);
}

// сериализатор в HTML
class HtmlVisitor : IVisitor
{
    public void VisitPersonAcc(Person acc)
    {
        string result = "<table><tr><td>Свойство<td><td>Значение</td></tr>";
        result += "<tr><td>Name<td><td>" + acc.Name + "</td></tr>";
        result += "<tr><td>Number<td><td>" + acc.Number + "</td></tr></table>";
        Console.WriteLine(result);
    }

    public void VisitCompanyAc(Company acc)
    {
        string result = "<table><tr><td>Свойство<td><td>Значение</td></tr>";
        result += "<tr><td>Name<td><td>" + acc.Name + "</td></tr>";
        result += "<tr><td>RegNumber<td><td>" + acc.RegNumber + "</td></tr>";
        result += "<tr><td>Number<td><td>" + acc.Number + "</td></tr></table>";
        Console.WriteLine(result);
    }
}

// сериализатор в XML
class XmlVisitor : IVisitor
{
    public void VisitPersonAcc(Person acc)
    {
        string result = "<Person><Name>"+acc.Name+"</Name>"+
			"<Number>"+acc.Number+"</Number><Person>";
        Console.WriteLine(result);
    }

    public void VisitCompanyAc(Company acc)
    {
        string result = "<Company><Name>" + acc.Name + "</Name>" + 
            "<RegNumber>" + acc.RegNumber + "</RegNumber>" + 
            "<Number>" + acc.Number + "</Number><Company>";
        Console.WriteLine(result);
    }
}

class Bank
{
    List<IAccount> accounts = new List<IAccount>();
    public void Add(IAccount acc)
    {
        accounts.Add(acc);
    }
    public void Remove(IAccount acc)
    {
        accounts.Remove(acc);
    }
    public void Accept(IVisitor visitor)
    {
        foreach (IAccount acc in accounts)
            acc.Accept(visitor);
    }
}

interface IAccount
{
    void Accept(IVisitor visitor);
}

class Person : IAccount
{
    public string Name { get; set; }
    public string Number { get; set; }

    public void Accept(IVisitor visitor)
    {
        visitor.VisitPersonAcc(this);
    }
}

class Company : IAccount
{
    public string Name { get; set; }
    public string RegNumber { get; set; }
    public string Number { get; set; }

    public void Accept(IVisitor visitor)
    {
        visitor.VisitCompanyAc(this);
    }
}В роли абстрактного класса Element здесь выступает интерфейс IAccount. Однако его реализации теперь не содержат методToHtml(), и любой 
другой метод для сериализации в какой-либо формат. Так как вся функциональность по сериализации вынесена в отдельные классы посетителей. В 
итоге классы Person и Company становятся намного чище и проще по структуре.И если нам надо добавить новый способ сериализации, достаточно просто определить еще один класс посетителя.

**Источник:** [https://metanit.com/sharp/patterns/3.11.php](https://metanit.com/sharp/patterns/3.11.php)

[[Языки программирования/C#/Руководства/Паттерны проектирования/Глава 3. Паттерны поведения/Хранитель (Memento)|Назад]] | [[Языки программирования/C#/Руководства/Паттерны проектирования/Глава 3. Паттерны поведения|Паттерны поведения]] | [[Языки программирования/C#/Руководства/Паттерны проектирования/Глава 4. Структурные паттерны/Декоратор (Decorator)|Вперёд]]
