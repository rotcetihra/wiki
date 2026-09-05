# XPath

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Руководства|Руководства]] / [[Языки программирования/C#/Руководства/Полное руководство по C# 14 и платформе .NET 10|Полное руководство по C# 14 и платформе .NET 10]] / [[Языки программирования/C#/Руководства/Полное руководство по C# 14 и платформе .NET 10/Глава 24. Работа с XML в C#|Работа с XML в C#]] / XPath

[[Языки программирования/C#/Руководства/Полное руководство по C# 14 и платформе .NET 10/Глава 24. Работа с XML в C#/Изменение XML-документа|Назад]] | [[Языки программирования/C#/Руководства/Полное руководство по C# 14 и платформе .NET 10/Глава 24. Работа с XML в C#|Работа с XML в C#]] | [[Языки программирования/C#/Руководства/Полное руководство по C# 14 и платформе .NET 10/Глава 24. Работа с XML в C#/Linq to Xml. Создание Xml-документа|Вперёд]]

**Дата написания:** 05.09.2026

## XPath

XPath  представляет язык запросов в XML. Он позволяет выбирать элементы, соответствующие определенному селектору.

Рассмотрим некоторые наиболее распространенные селекторы:

.выбор текущего узла..выбор родительского узла*выбор всех дочерних узлов текущего узлаpersonвыбор всех узлов с определенным именем, в данном случае с именем "person"@nameвыбор атрибута текущего узла, после знака @ указывается название атрибута (в данном случае "name")@*выбор всех атрибутов текущего узлаelement[3]выбор определенного дочернего узла по индексу, в данном случае третьего узла//personвыбор в документе всех узлов с именем "person"person[@name='Tom']выбор элементов с определенным значением атрибута. В данном случае выбираются все элементы "person" с атрибутом name='Tom'person[company='Microsoft']выбор элементов с определенным значением вложенного элемента. В данном случае выбираются все элементы "person", у которых дочерний элемент 
"company" имеет значение 'Microsoft'//person/companyвыбор в документе всех узлов с именем "company", которые находятся в элементах "person"

Действие запросов XPath основано на применении двух методов класса  XmlElement :

- SelectSingleNode() : выбор единственного узла из выборки. Если выборка по запросу содержит несколько узлов, то выбирается первый
- SelectNodes() : выборка по запросу коллекции узлов в виде объекта  `XmlNodeList`

Для запросов возьмем xml-документ из прошлых тем:

```csharp
<?xml version="1.0" encoding="utf-8" ?>
<people>
  <person name="Tom">
    <company>Microsoft</company>
    <age>37</age>
  </person>
  <person name="Bob">
    <company>Google</company>
    <age>41</age>
  </person>
</people>
```

Теперь выберем все узлы корневого элемента, то есть все элементы person:

```csharp
using System.Xml;

XmlDocument xDoc = new XmlDocument();
xDoc.Load("people.xml");
XmlElement? xRoot = xDoc.DocumentElement;

// выбор всех дочерних узлов
XmlNodeList? nodes = xRoot?.SelectNodes("*");
if (nodes is not null)
{
    foreach (XmlNode node in nodes)
        Console.WriteLine(node.OuterXml);
}
```

Консольный вывод:

```csharp
<person name="Tom"><company>Microsoft</company><age>37</age></person>
<person name="Bob"><company>Google</company><age>41</age></person>
```

Выберем все узлы  `<person>` :

```csharp
XmlNodeList? personNodes = xRoot?.SelectNodes("person");
```

Выведем на консоль значения атрибутов name у элементов person:

```csharp
using System.Xml;

XmlDocument xDoc = new XmlDocument();
xDoc.Load("people.xml");
XmlElement? xRoot = xDoc.DocumentElement;
XmlNodeList? personNodes = xRoot?.SelectNodes("person");
if(personNodes is not null)
{
    foreach (XmlNode node in personNodes)
        Console.WriteLine(node.SelectSingleNode("@name")?.Value);
}
```

Результатом выполнения будет следующий вывод:

```csharp
Tom
Bob
```

Выберем узел, у которого атрибут name имеет значение "Tom":

```csharp
XmlNode? tomNode = xRoot?.SelectSingleNode("person[@name='Tom']");
Console.WriteLine(tomNode?.OuterXml);
```

Допустим, нам надо получить только компании. Для этого надо осуществить выборку вниз по иерархии элементов:

```csharp
using System.Xml;

XmlDocument xDoc = new XmlDocument();
xDoc.Load("people.xml");
XmlElement? xRoot = xDoc.DocumentElement;

XmlNodeList? companyNodes = xRoot?.SelectNodes("//person/company");
if(companyNodes is not null)
{
    foreach (XmlNode node in companyNodes)
        Console.WriteLine(node.InnerText);
}
```

**Источник:** [https://metanit.com/sharp/tutorial/16.4.php](https://metanit.com/sharp/tutorial/16.4.php)

[[Языки программирования/C#/Руководства/Полное руководство по C# 14 и платформе .NET 10/Глава 24. Работа с XML в C#/Изменение XML-документа|Назад]] | [[Языки программирования/C#/Руководства/Полное руководство по C# 14 и платформе .NET 10/Глава 24. Работа с XML в C#|Работа с XML в C#]] | [[Языки программирования/C#/Руководства/Полное руководство по C# 14 и платформе .NET 10/Глава 24. Работа с XML в C#/Linq to Xml. Создание Xml-документа|Вперёд]]
