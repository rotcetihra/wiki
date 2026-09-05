# Изменение XML-документа

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Руководства|Руководства]] / [[Языки программирования/C#/Руководства/Полное руководство по C# 14 и платформе .NET 10|Полное руководство по C# 14 и платформе .NET 10]] / [[Языки программирования/C#/Руководства/Полное руководство по C# 14 и платформе .NET 10/Глава 24. Работа с XML в C#|Работа с XML в C#]] / Изменение XML-документа

[[Языки программирования/C#/Руководства/Полное руководство по C# 14 и платформе .NET 10/Глава 24. Работа с XML в C#/Работа с XML с помощью классов System.Xml|Назад]] | [[Языки программирования/C#/Руководства/Полное руководство по C# 14 и платформе .NET 10/Глава 24. Работа с XML в C#|Работа с XML в C#]] | [[Языки программирования/C#/Руководства/Полное руководство по C# 14 и платформе .NET 10/Глава 24. Работа с XML в C#/XPath|Вперёд]]

**Дата написания:** 05.09.2026

## Изменение XML-документа

Для редактирования xml-документа (изменения, добавления, удаления элементов) мы можем воспользоваться методами класса  XmlNode :

- AppendChild : добавляет в конец текущего узла новый дочерний узел
- InsertAfter : добавляет новый узел после определенного узла
- InsertBefore : добавляет новый узел до определенного узла
- RemoveAll : удаляет все дочерние узлы текущего узла
- RemoveChild : удаляет у текущего узла один дочерний узел и возвращает его

Класс  XmlDocument  добавляет еще ряд методов, которые позволяют создавать новые узлы:

- CreateNode : создает узел любого типа
- CreateElement : создает узел типа XmlDocument
- CreateAttribute : создает узел типа XmlAttribute
- CreateTextNode : создает узел типа XmlTextNode
- CreateComment : создает комментарий

Возьмем xml-документ people.xml из прошлой темы:

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

Добавим в этот xml-документ новый элемент <person>:

```csharp
using System.Xml;

XmlDocument xDoc = new XmlDocument();
xDoc.Load("people.xml");
XmlElement? xRoot = xDoc.DocumentElement;

// создаем новый элемент person
XmlElement personElem = xDoc.CreateElement("person");

// создаем атрибут name
XmlAttribute nameAttr = xDoc.CreateAttribute("name");

// создаем элементы company и age
XmlElement companyElem = xDoc.CreateElement("company");
XmlElement ageElem = xDoc.CreateElement("age");

// создаем текстовые значения для элементов и атрибута
XmlText nameText = xDoc.CreateTextNode("Mark");
XmlText companyText = xDoc.CreateTextNode("Facebook");
XmlText ageText = xDoc.CreateTextNode("30");

//добавляем узлы
nameAttr.AppendChild(nameText);
companyElem.AppendChild(companyText);
ageElem.AppendChild(ageText);

// добавляем атрибут name
personElem.Attributes.Append(nameAttr);
// добавляем элементы company и age
personElem.AppendChild(companyElem);
personElem.AppendChild(ageElem);
// добавляем в корневой элемент новый элемент person
xRoot?.AppendChild(personElem);
// сохраняем изменения xml-документа в файл
xDoc.Save("people.xml");
```

Добавление элементов происходит по одной схеме. Сначала создаем элемент ( `xDoc.CreateElement("person")` ). Если элемент сложный, то есть содержит в 
себе другие элементы, то создаем эти элементы. Если элемент простой, содержащий внутри себя некоторое текстовое значение, то создаем этот текст 
( `XmlText companyText = xDoc.CreateTextNode("Facebook");` ).

Затем все элементы добавляются в основной элемент person, а тот добавляется в корневой элемент ( `xRoot.AppendChild(personElem);` ).

Чтобы сохранить измененный документ на диск, используем метод  `Save` :  `xDoc.Save("people.xml")`

После этого в xml-файле появится следующий элемент:

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
  <people name="Mark">
    <company>Facebook</company>
    <age>30</age>
  </people>
</people>
```

### Удаление узлов

Удалим первый узел xml-документа:

```csharp
using System.Xml;

XmlDocument xDoc = new XmlDocument();
xDoc.Load("people.xml");
XmlElement? xRoot = xDoc.DocumentElement;
XmlNode? firstNode = xRoot?.FirstChild;
if(firstNode is not null) xRoot?.RemoveChild(firstNode);
xDoc.Save("people.xml");
```

**Источник:** [https://metanit.com/sharp/tutorial/16.3.php](https://metanit.com/sharp/tutorial/16.3.php)

[[Языки программирования/C#/Руководства/Полное руководство по C# 14 и платформе .NET 10/Глава 24. Работа с XML в C#/Работа с XML с помощью классов System.Xml|Назад]] | [[Языки программирования/C#/Руководства/Полное руководство по C# 14 и платформе .NET 10/Глава 24. Работа с XML в C#|Работа с XML в C#]] | [[Языки программирования/C#/Руководства/Полное руководство по C# 14 и платформе .NET 10/Глава 24. Работа с XML в C#/XPath|Вперёд]]
