# Строитель (Builder)

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Руководства|Руководства]] / [[Языки программирования/C#/Руководства/Паттерны проектирования|Паттерны проектирования]] / [[Языки программирования/C#/Руководства/Паттерны проектирования/Глава 2. Порождающие паттерны|Порождающие паттерны]] / Строитель (Builder)

[[Языки программирования/C#/Руководства/Паттерны проектирования/Глава 2. Порождающие паттерны/Прототип (Prototype)|Назад]] | [[Языки программирования/C#/Руководства/Паттерны проектирования/Глава 2. Порождающие паттерны|Порождающие паттерны]] | [[Языки программирования/C#/Руководства/Паттерны проектирования/Глава 3. Паттерны поведения/Стратегия (Strategy)|Вперёд]]

**Дата написания:** 05.09.2026

## Строитель (Builder)

Строитель (Builder) - шаблон проектирования, который инкапсулирует создание объекта и позволяет разделить его на различные этапы.

### Когда использовать паттерн Строитель?

- Когда процесс создания нового объекта не должен зависеть от того, из каких частей этот объект состоит и как эти части связаны между собой
- Когда необходимо обеспечить получение различных вариаций объекта в процессе его создания

Формально в UML паттерн мог бы выглядеть следующим образом:

Формальное определение на C# могло бы выглядеть так:class Client
{
    void Main()
    {
        Builder builder = new ConcreteBuilder();
        Director director = new Director(builder);
        director.Construct();
        Product product = builder.GetResult();
    }
}
class Director
{
    Builder builder;
    public Director(Builder builder)
    {
        this.builder = builder;
    }
    public void Construct()
    {
        builder.BuildPartA();
        builder.BuildPartB();
        builder.BuildPartC();
    }
}

abstract class Builder
{
    public abstract void BuildPartA();
	public abstract void BuildPartB();
	public abstract void BuildPartC();
    public abstract Product GetResult();
}

class Product
{
    List<object> parts = new List<object>();
    public void Add(string part)
    {
        parts.Add(part);
    }
}

class ConcreteBuilder : Builder
{
    Product product = new Product();
    public override void BuildPartA()
    {
        product.Add("Part A");
    }
	public override void BuildPartB()
	{
		product.Add("Part B");
	}
	public override void BuildPartC()
	{
		product.Add("Part C");
	}
    public override Product GetResult()
    {
        return product;
    }
}УчастникиProduct: представляет объект, который должен быть создан. В данном случае все части объекта заключены 
в списке parts.Builder: определяет интерфейс для создания различных частей объекта ProductConcreteBuilder: конкретная реализация Buildera. Создает объект Product и определяет интерфейс 
для доступа к немуDirector: распорядитель - создает объект, используя объекты BuilderРассмотрим применение паттерна на примере выпечки хлеба. Как известно, даже обычный хлеб включает множество компонентов. 
Мы можем использовать для представления хлеба и его компонентов следующие классы://мука
class Flour
{
    // какого сорта мука
    public string Sort { get; set; }
}
// соль
class Salt
{}
// пищевые добавки
class Additives
{
    public string Name { get; set; }
}

class Bread
{
    // мука
    public Flour Flour { get; set; }
    // соль
    public Salt Salt { get; set; }
    // пищевые добавки
    public Additives Additives { get; set; }
    public override string ToString()
    {
        StringBuilder sb = new StringBuilder();

        if (Flour != null)
            sb.Append(Flour.Sort + "\n");
        if (Salt != null)
            sb.Append("Соль \n");
        if (Additives != null)
            sb.Append("Добавки: "+Additives.Name+" \n");
        return sb.ToString();
    }
}Кстати в данном случае для построения строки используется класс StringBuilder.Хлеб может иметь различную комбинацию компонентов: ржаной и пшеничной муки, соли, пищевых добавок. И нам надо обеспечить выпечку 
разных сортов хлеба. Для разных сортов хлеба может варьироваться конкретный набор компонентов, не все компоненты могут использоваться. 
И для этой задачи применим паттерн Builder:class Program
{
    static void Main(string[] args)
    {
		// содаем объект пекаря
        Baker baker = new Baker();
		// создаем билдер для ржаного хлеба
        BreadBuilder builder = new RyeBreadBuilder();
		// выпекаем
        Bread ryeBread = baker.Bake(builder);
        Console.WriteLine(ryeBread.ToString());
		// оздаем билдер для пшеничного хлеба
        builder = new WheatBreadBuilder();
        Bread wheatBread = baker.Bake(builder);
        Console.WriteLine(wheatBread.ToString());

        Console.Read();
    }
}
// абстрактный класс строителя
abstract class BreadBuilder
{
    public Bread Bread { get; private set; }
    public void CreateBread()
    {
        Bread = new Bread();
    }
    public abstract void SetFlour();
    public abstract void SetSalt();
    public abstract void SetAdditives();
}
// пекарь
class Baker
{
    public Bread Bake(BreadBuilder breadBuilder)
    {
        breadBuilder.CreateBread();
        breadBuilder.SetFlour();
        breadBuilder.SetSalt();
        breadBuilder.SetAdditives();
        return breadBuilder.Bread;
    }
}
// строитель для ржаного хлеба
class RyeBreadBuilder : BreadBuilder
{
    public override void SetFlour()
    {
        this.Bread.Flour = new Flour { Sort = "Ржаная мука 1 сорт" };
    }

    public override void SetSalt()
    {
        this.Bread.Salt = new Salt();
    }

    public override void SetAdditives()
    {
        // не используется
    }
}
// строитель для пшеничного хлеба
class WheatBreadBuilder : BreadBuilder
{
    public override void SetFlour()
    {
        this.Bread.Flour = new Flour { Sort = "Пшеничная мука высший сорт" };
    }

    public override void SetSalt()
    {
        this.Bread.Salt = new Salt();
    }

    public override void SetAdditives()
    {
        this.Bread.Additives = new Additives { Name = "улучшитель хлебопекарный" };
    }
}Консольный вывод программы:Ржаная мука 1 сорт
Соль

Пшеничная мука высший сорт
Соль
Добавки: улучшитель хлебопекарныйВ данном случае с помощью конкретных строителей RyeBreadBuilder и WheatBreadBuilder создаются объекты Bread с определенным набором. 
В роли распорядителя выступает класс пекаря Baker, который вызывает методы конкретных строителей для построения нового объекта.

**Источник:** [https://metanit.com/sharp/patterns/2.5.php](https://metanit.com/sharp/patterns/2.5.php)

[[Языки программирования/C#/Руководства/Паттерны проектирования/Глава 2. Порождающие паттерны/Прототип (Prototype)|Назад]] | [[Языки программирования/C#/Руководства/Паттерны проектирования/Глава 2. Порождающие паттерны|Порождающие паттерны]] | [[Языки программирования/C#/Руководства/Паттерны проектирования/Глава 3. Паттерны поведения/Стратегия (Strategy)|Вперёд]]
