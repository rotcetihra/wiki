# Компоновщик (Composite)

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Руководства|Руководства]] / [[Языки программирования/C#/Руководства/Паттерны проектирования|Паттерны проектирования]] / [[Языки программирования/C#/Руководства/Паттерны проектирования/Глава 4. Структурные паттерны|Структурные паттерны]] / Компоновщик (Composite)

[[Языки программирования/C#/Руководства/Паттерны проектирования/Глава 4. Структурные паттерны/Фасад (Facade)|Назад]] | [[Языки программирования/C#/Руководства/Паттерны проектирования/Глава 4. Структурные паттерны|Структурные паттерны]] | [[Языки программирования/C#/Руководства/Паттерны проектирования/Глава 4. Структурные паттерны/Заместитель (Прокси)|Вперёд]]

**Дата написания:** 05.09.2026

## Компоновщик (Composite)

Паттерн Компоновщик (Composite) объединяет группы объектов в древовидную структуру по принципу "часть-целое и позволяет клиенту 
одинаково работать как с отдельными объектами, так и с группой объектов.

Образно реализацию паттерна можно представить в виде меню, которое имеет различные пункты. Эти пункты могут содержать подменю, в которых, в свою 
очередь, также имеются пункты. То есть пункт меню служит с одной стороны частью меню, а с другой стороны еще одним меню. В итоге мы 
однообразно можем работать как с пунктом меню, так и со всем меню в целом.

### Когда использовать компоновщик?

- Когда объекты должны быть реализованы в виде иерархической древовидной структуры
- Когда клиенты единообразно должны управлять как целыми объектами, так и их составными частями. То есть целое и его части должны 
реализовать один и тот же интерфейс

С помощью UML шаблон компоновщик можно представить следующим образом:

Формальное определение паттерна на C# могло бы выглядеть так:class Client
{
    public void Main()
    {
        Component root = new Composite("Root");
        Component leaf = new Leaf("Leaf");
        Composite subtree = new Composite("Subtree");
        root.Add(leaf);
		root.Add(subtree);
		root.Display();
    }
}
abstract class Component
{
    protected string name;

    public Component(string name)
    {
        this.name = name;
    }

    public abstract void Display();
    public abstract void Add(Component c); 
    public abstract void Remove(Component c);
}
class Composite : Component
{
    List<Component> children = new List<Component>();

    public Composite(string name)
        : base(name)
    {}

    public override void Add(Component component)
    {
        children.Add(component);
    }

    public override void Remove(Component component)
    {
        children.Remove(component);
    }

    public override void Display()
    {
        Console.WriteLine(name);

        foreach (Component component in children)
        {
            component.Display();
        }
    }
}
class Leaf : Component
{
    public Leaf(string name)
        : base(name)
    {}

    public override void Display()
    {
        Console.WriteLine(name);
	}

    public override void Add(Component component)
    {
        throw new NotImplementedException();
    }

    public override void Remove(Component component)
    {
        throw new NotImplementedException();
    }
}УчастникиComponent: определяет интерфейс для всех компонентов в древовидной структуреComposite: представляет компонент, который может содержать другие компоненты и реализует механизм 
для их добавления и удаленияLeaf: представляет отдельный компонент, который не может содержать другие компонентыClient: клиент, который использует компонентыРассмотрим простейший пример. Допустим, нам надо создать объект файловой системы. Файловую систему составляют папки и файлы. 
Каждая папка также может включать в себя папки и файлы. То есть получается древовидная иерархическая структура, 
где с вложенными папками нам надо работать также, как и с папками, которые их содержат. Для реализации данной задачи и воспользуемся паттерном Компоновщик:class Program
{
    static void Main(string[] args)
    {
        Component fileSystem = new Directory("Файловая система");
        // определяем новый диск
        Component diskC = new Directory("Диск С");
        // новые файлы
        Component pngFile = new File("12345.png");
        Component docxFile = new File("Document.docx");
        // добавляем файлы на диск С
        diskC.Add(pngFile);
        diskC.Add(docxFile);
        // добавляем диск С в файловую систему
        fileSystem.Add(diskC);
        // выводим все данные
        fileSystem.Print();
        Console.WriteLine();
        // удаляем с диска С файл
        diskC.Remove(pngFile);
        // создаем новую папку
        Component docsFolder = new Directory("Мои Документы");
        // добавляем в нее файлы
		Component txtFile = new File("readme.txt");
        Component csFile = new File("Program.cs");
        docsFolder.Add(txtFile);
        docsFolder.Add(csFile);
        diskC.Add(docsFolder);
        
		fileSystem.Print();

        Console.Read();
    }
}

abstract class Component
{
    protected string name;

    public Component(string name)
    {
        this.name = name;
    }

    public virtual void Add(Component component){}

    public virtual void Remove(Component component) { }

    public virtual void Print()
    {
        Console.WriteLine(name);
    }
}
class Directory :Component
{
    private List<Component> components = new List<Component>();

    public Directory(string name)
        : base(name)
    {
    }

    public override void Add(Component component)
    {
        components.Add(component);
    }

    public override void Remove(Component component)
    {
        components.Remove(component);
    }

    public override void Print()
    {
        Console.WriteLine("Узел " + name);
        Console.WriteLine("Подузлы:");
        for(int i=0; i<components.Count;i++)
        {
            components[i].Print();
        }
    }
}

class File : Component
{
    public File(string name)
            : base(name)
    {}
}В итоге подобная система обладает неплохой гибкостью: если мы захотим добавить новый вид компонентов, нам достаточно унаследовать новый класс от Component.И также применяя компоновщик, мы легко можем обойти все узлы древовидной структуры.

**Источник:** [https://metanit.com/sharp/patterns/4.4.php](https://metanit.com/sharp/patterns/4.4.php)

[[Языки программирования/C#/Руководства/Паттерны проектирования/Глава 4. Структурные паттерны/Фасад (Facade)|Назад]] | [[Языки программирования/C#/Руководства/Паттерны проектирования/Глава 4. Структурные паттерны|Структурные паттерны]] | [[Языки программирования/C#/Руководства/Паттерны проектирования/Глава 4. Структурные паттерны/Заместитель (Прокси)|Вперёд]]
