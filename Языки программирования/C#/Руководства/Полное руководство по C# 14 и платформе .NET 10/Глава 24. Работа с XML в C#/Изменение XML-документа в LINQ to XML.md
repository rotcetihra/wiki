# Изменение XML-документа в LINQ to XML

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Руководства|Руководства]] / [[Языки программирования/C#/Руководства/Полное руководство по C# 14 и платформе .NET 10|Полное руководство по C# 14 и платформе .NET 10]] / [[Языки программирования/C#/Руководства/Полное руководство по C# 14 и платформе .NET 10/Глава 24. Работа с XML в C#|Работа с XML в C#]] / Изменение XML-документа в LINQ to XML

[[Языки программирования/C#/Руководства/Полное руководство по C# 14 и платформе .NET 10/Глава 24. Работа с XML в C#/Выборка элементов в LINQ to XML|Назад]] | [[Языки программирования/C#/Руководства/Полное руководство по C# 14 и платформе .NET 10/Глава 24. Работа с XML в C#|Работа с XML в C#]] | [[Языки программирования/C#/Руководства/Полное руководство по C# 14 и платформе .NET 10/Глава 24. Работа с XML в C#/Сериализация в XML. XmlSerializer|Вперёд]]

**Дата написания:** 05.09.2026

## Изменение документа в LINQ to XML

Возьмем xml-файл  people.xml  из прошлых тем:

```csharp
<?xml version="1.0" encoding="utf-8"?>
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

### Добавление данных

Для добавления данных в документ xml у объекта XElement применяется метод  Add() , в который передается добавляемый объект:

```csharp
using System.Xml.Linq;

XDocument xdoc = XDocument.Load("people.xml");
XElement? root = xdoc.Element("people");

if(root != null)
{
    // добавляем новый элемент
    root.Add(new XElement("person",
                new XAttribute("name", "Sam"),
                new XElement("company", "JetBrains"),
                new XElement("age", 28)));

    xdoc.Save("people.xml");
}

// выводим xml-документ на консоль
Console.WriteLine(xdoc);
```

В результате сформируется и сохранится на диск новый документ:

```csharp
<people>
  <person name="Tom">
    <company>Microsoft</company>
    <age>37</age>
  </person>
  <person name="Bob">
    <company>Google</company>
    <age>41</age>
  </person>
  <person name="Sam">
    <company>JetBrains</company>
    <age>28</age>
  </person>
</people>
```

### Изменение данных

Для изменения данных в документ xml необходимо получить элемент, который надо изменить, и затем можно отредактировать значения его отдельных атрибутов 
или вложенных элементов. Изменим элемент person, в котором атрибут name = "Tom":

```csharp
using System.Xml.Linq;

XDocument xdoc = XDocument.Load("people.xml");

// получим элемент person с name = "Tom"
var tom = xdoc.Element("people")?
    .Elements("person")
    .FirstOrDefault(p => p.Attribute("name")?.Value == "Tom");

if(tom != null)
{
    //  меняем атрибут name
    var name = tom.Attribute("name");
    if (name != null) name.Value = "Tomas";

    //  меняем вложенный элемент age
    var age = tom.Element("age");
    if (age != null) age.Value = "22";

    xdoc.Save("people.xml");
}

// выводим xml-документ на консоль
Console.WriteLine(xdoc);
```

В результате сформируется и сохранится на диск новый документ:

```csharp
<people>
  <person name="Tomas">
    <company>Microsoft</company>
    <age>22</age>
  </person>
  <person name="Bob">
    <company>Google</company>
    <age>41</age>
  </person>
  <person name="Sam">
    <company>JetBrains</company>
    <age>28</age>
  </person>
</people>
```

### Удаление данных

Для удаления данных в документе xml у удаляемого объекта XElement вызывается метод  Remove() . 
Например, удалим элемент person, в котором атрибут name = "Bob":

```csharp
using System.Xml.Linq;

XDocument xdoc = XDocument.Load("people.xml");
XElement? root = xdoc.Element("people");

if (root != null)
{
    // получим элемент person с name = "Bob"
    var bob = root.Elements("person")
        .FirstOrDefault(p => p.Attribute("name")?.Value == "Bob");
    // и удалим его
    if (bob != null)
    {
        bob.Remove();
        xdoc.Save("people.xml");
    }
}

// выводим xml-документ на консоль
Console.WriteLine(xdoc);
```

В результате сформируется и сохранится на диск новый документ:

```csharp
<people>
  <person name="Tomas">
    <company>Microsoft</company>
    <age>22</age>
  </person>
  <person name="Sam">
    <company>JetBrains</company>
    <age>28</age>
  </person>
</people>
```

Соответственно, если необходимо удалить атрибут, то у удаляемого объекта XAttribute также вызывается метод Remove.

**Источник:** [https://metanit.com/sharp/tutorial/16.7.php](https://metanit.com/sharp/tutorial/16.7.php)

[[Языки программирования/C#/Руководства/Полное руководство по C# 14 и платформе .NET 10/Глава 24. Работа с XML в C#/Выборка элементов в LINQ to XML|Назад]] | [[Языки программирования/C#/Руководства/Полное руководство по C# 14 и платформе .NET 10/Глава 24. Работа с XML в C#|Работа с XML в C#]] | [[Языки программирования/C#/Руководства/Полное руководство по C# 14 и платформе .NET 10/Глава 24. Работа с XML в C#/Сериализация в XML. XmlSerializer|Вперёд]]
