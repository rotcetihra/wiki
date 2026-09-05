# Сериализация в JSON. JsonSerializer

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Руководства|Руководства]] / [[Языки программирования/C#/Руководства/Полное руководство по C# 14 и платформе .NET 10|Полное руководство по C# 14 и платформе .NET 10]] / [[Языки программирования/C#/Руководства/Полное руководство по C# 14 и платформе .NET 10/Глава 23. Работа с JSON|Работа с JSON]] / Сериализация в JSON. JsonSerializer

[[Языки программирования/C#/Руководства/Полное руководство по C# 14 и платформе .NET 10/Глава 22. Работа с файловой системой/Архивация и сжатие файлов|Назад]] | [[Языки программирования/C#/Руководства/Полное руководство по C# 14 и платформе .NET 10/Глава 23. Работа с JSON|Работа с JSON]] | [[Языки программирования/C#/Руководства/Полное руководство по C# 14 и платформе .NET 10/Глава 24. Работа с XML в C#/XML-Документы|Вперёд]]

**Дата написания:** 05.09.2026

## Сериализация в JSON. JsonSerializer

JSON  (JavaScript Object Notation) является одним из наиболее популярных форматов для хранения и передачи данных. 
И платформа .NET предоставляет функционал для работы с JSON.

Основная функциональность по работе с JSON сосредоточена в пространстве имен  System.Text.Json . 
Ключевым типом является класс  JsonSerializer , который и позволяет сериализовать объект в json и, наоборот, десериализовать код 
json в объект C#.

Для сохранения объекта в json в классе JsonSerializer определен статический метод  Serialize()  и его асинхронный двойник 
 SerializeAsyc() , которые имеют ряд перегруженных версий. Некоторые из них:

- `string Serialize(Object obj, Type type, JsonSerializerOptions options)` : сериализует объект obj типа type и возвращает код json в виде строки. 
Последний необязательный параметр options позволяет задать дополнительные опции сериализации
- `string Serialize<T>(T obj, JsonSerializerOptions options)` : типизированная версия сериализует объект obj типа T и возвращает 
код json в виде строки.
- `Task SerializeAsync(Stream utf8Json, Object obj, Type type, JsonSerializerOptions options)` : сериализует объект obj типа type и записывает 
его в поток utf8Json. Последний необязательный параметр options позволяет задать дополнительные опции сериализации
- `Task SerializeAsync<T>(Stream utf8Json, T obj, JsonSerializerOptions options)` : типизированная версия сериализует объект obj типа T 
в поток utf8Json.

Для десериализации кода json в объект C# применяется метод  Deserialize()  и его асинхронный двойник  DeserializeAsync() , 
которые имеют различные версии. Некоторые из них:

- `object? Deserialize(string json, Type type, JsonSerializerOptions options)` : десериализует строку json в объект типа type и 
возвращает десериализованный объект. Последний необязательный параметр options позволяет задать дополнительные опции десериализации
- `T? Deserialize<T>(string json, JsonSerializerOptions options)` : десериализует строку json в объект типа T и 
возвращает его.
- `ValueTask<object?> DeserializeAsync(Stream utf8Json, Type type, JsonSerializerOptions options, CancellationToken token)` : 
десериализует данные из потока utf8Json, который представляет объект JSON, в объект типа type. Последние два параметра необязательны: options позволяет задать 
дополнительные опции десериализации, а token устанавливает CancellationToken для отмены задачи. Возвращается десериализованный объект, обернутый в ValueTask
- `ValueTask<T?> DeserializeAsync<T>(Stream utf8Json, JsonSerializerOptions options, CancellationToken token)` : 
десериализует данные из потока utf8Json, который представляет объект JSON, в объект типа T. Возвращается десериализованный объект, обернутый в ValueTask

Рассмотрим применение класса на простом примере. Сериализуем и десериализуем простейший объект:

```csharp
using System.Text.Json;

Person tom = new Person("Tom", 37);
string json = JsonSerializer.Serialize(tom);
Console.WriteLine(json);
Person? restoredPerson = JsonSerializer.Deserialize<Person>(json);
Console.WriteLine(restoredPerson?.Name); // Tom

class Person
{
    public string Name { get;}
    public int Age { get; set; }
    public Person(string name, int age)
    {
        Name = name;
        Age = age;
    }
}
```

Здесь вначале сериализуем с помощью метода  `JsonSerializer.Serialize()`  объект типа Person в стоку с кодом json. Затем обратно получаем из этой 
строки объект Person посредством метода  `JsonSerializer.Deserialize()` .

Консольный вывод:

```csharp
{"Name":"Tom","Age": 37}
Tom
```

Хотя в примере выше сериализовался/десериализовался объект класса, но подобным способом мы также можем сериализовать/десериализовать структуры.

### Некоторые замечания по сериализации/десериализации

Объект, который подвергается десериализации, должен иметь либо конструктор без параметров, либо конструктор, для всех параметров которого 
в десериализуемом json-объекте есть значения (соответствие между параметрами конструктора и свойствами json-объекта устанавливается на основе названий, причем регистр 
не играет значения).

Сериализации подлежат только публичные свойства объекта (с модификатором public).

### Запись и чтение файла json

Поскольку методы SerializeAsyc/DeserializeAsync могут принимать поток типа Stream, то соответственно мы можем использовать файловый поток для сохранения 
и последующего извлечения данных:

```csharp
using System.Text.Json;

// сохранение данных
using (FileStream fs = new FileStream("user.json", FileMode.OpenOrCreate))
{
    Person tom = new Person("Tom", 37);
    await JsonSerializer.SerializeAsync<Person>(fs, tom);
    Console.WriteLine("Data has been saved to file");
}

// чтение данных
using (FileStream fs = new FileStream("user.json", FileMode.OpenOrCreate))
{
    Person? person = await JsonSerializer.DeserializeAsync<Person>(fs);
    Console.WriteLine($"Name: {person?.Name}  Age: {person?.Age}");
}

class Person
{
    public string Name { get;}
    public int Age { get; set; }
    public Person(string name, int age)
    {
        Name = name;
        Age = age;
    }
}
```

В данном случае вначале данные сохраняются в файл user.json и затем считываются из него.

### Настройка сериализации с помощью JsonSerializerOptions

По умолчанию JsonSerializer сериализует объекты в минимифицированный код. С помощью дополнительного параметра типа  JsonSerializerOptions  
можно настроить механизм сериализации/десериализации, используя свойства JsonSerializerOptions. Некоторые из его свойств:

- AllowTrailingCommas : устанавливает, надо ли добавлять после последнего элемента в json запятую. Если равно  `true` , запятая добавляется
- DefaultIgnoreCondition : устанавливает, будут ли сериализоваться/десериализоваться в json свойства со значениями по умолчанию
- IgnoreReadOnlyProperties : аналогично устанавливает, будут ли сериализоваться свойства, предназначенные только для чтения
- WriteIndented : устанавливает, будут ли добавляться в json пробелы (условно говоря, для красоты). Если равно  `true`  устанавливаются дополнительные пробелы
- Encoder :  возвращает или задает кодировщик (объект  `JavaScriptEncoder` ), используемый при экранировании строк, или null для использования кодировщика по умолчанию.

Применение:

```csharp
using System.Text.Json;

Person tom = new Person("Tom", 37);

var options = new JsonSerializerOptions
{
    WriteIndented = true
};
string json = JsonSerializer.Serialize<Person>(tom, options);
Console.WriteLine(json);
Person? restoredPerson = JsonSerializer.Deserialize<Person>(json);
Console.WriteLine(restoredPerson?.Name);
```

Консольный вывод:

```csharp
{
	"Name": "Tom",
	"Age":  37
}
Tom
```

Еще одно полезное свойство, которое надо отметить - это  `Encoder`  или кодировщик. В частности, этот свойство может помочь при работе с различными наборами кодовых точек. Приведу простейший пример:

```csharp
using System.Text.Json;

Person tom = new Person("Евгений", 41);

var options = new JsonSerializerOptions WriteIndented = true};
string json = JsonSerializer.Serialize<Person>(tom, options);
Console.WriteLine(json);
Person? restoredPerson = JsonSerializer.Deserialize<Person>(json);
Console.WriteLine(restoredPerson?.Name);
```

Здесь пример аналогичен предыдущему, только имя указано кириллицей. Посмотрим на консольный вывод:

```csharp
{
  "Name": "\u0415\u0432\u0433\u0435\u043D\u0438\u0439",
  "Age": 41
}
Евгений
```

И по выводу мы видим, что хотя имя и корректно было восстановлено, но при сериализации строки с кириллицей сохраняются в набор кодов символов Unicode. Причем это касается и сериализации в файл. И, возможно, это не самое 
предпочтительное поведение. Но с помощью свойства  `Encoder`  можно указать необходимые кодировки. В частности, класс JavaScriptEncoder имеет статический метод-фабрика  `Create()` , который принимает 
набор применяемых наборов символов в виде массива UnicodeRange и возвращает объект кодировщика:

```csharp
public static JavaScriptEncoder Create(params System.Text.Unicode.UnicodeRange[] allowedRanges);
```

Так, изменим код следующим образом:

```csharp
using System.Text.Json;
using System.Text.Unicode;
using System.Text.Encodings.Web;

Person tom = new Person("Евгений", 41);

var options = new JsonSerializerOptions
{
    Encoder = JavaScriptEncoder.Create(UnicodeRanges.BasicLatin, UnicodeRanges.Cyrillic),
    WriteIndented = true
};
string json = JsonSerializer.Serialize<Person>(tom, options);
Console.WriteLine(json);
Person? restoredPerson = JsonSerializer.Deserialize<Person>(json);
Console.WriteLine(restoredPerson?.Name);
```

В данном случае используем две кодировки - латиницу и кириллицу. В итоге мы получим корреткный результат сериализации:

```csharp
{
  "Name": "Евгений",
  "Age": 41
}
Евгений
```

### Настройка сериализации с помощью атрибутов

По умолчанию сериализации подлежат все публичные свойства. Кроме того, в выходном объекте json все названия свойств соответствуют названиям свойств объекта C#. 
Однако с помощью атрибутов  JsonIgnore  и  JsonPropertyName .

Атрибут  JsonIgnore  позволяет исключить из сериализации определенное свойство. А  JsonPropertyName  позволяет замещать оригинальное название свойства. 
Пример использования:

```csharp
using System.Text.Json;
using System.Text.Json.Serialization;

Person tom = new Person("Tom", 37);

string json = JsonSerializer.Serialize<Person>(tom);
Console.WriteLine(json);
Person? person = JsonSerializer.Deserialize<Person>(json);
Console.WriteLine($"Name: {person?.Name}  Age: {person?.Age}");

class Person
{
    [JsonPropertyName("firstname")]
    public string Name { get;}
    [JsonIgnore]
    public int Age { get; set; }
    public Person(string name, int age)
    {
        Name = name;
        Age = age;
    }
}
```

В данном случае свойство Age будет игнорироваться, а для свойства Name будет использоваться псевдоним "firstname". Консольный вывод:

```csharp
{"firstname":"Tom"}
Name: Tom   Age: 0
```

Обратите внимание, что, поскольку свойство Age не было сериализовано, то при десериализации для него используется значение по умолчанию.

**Источник:** [https://metanit.com/sharp/tutorial/6.5.php](https://metanit.com/sharp/tutorial/6.5.php)

[[Языки программирования/C#/Руководства/Полное руководство по C# 14 и платформе .NET 10/Глава 22. Работа с файловой системой/Архивация и сжатие файлов|Назад]] | [[Языки программирования/C#/Руководства/Полное руководство по C# 14 и платформе .NET 10/Глава 23. Работа с JSON|Работа с JSON]] | [[Языки программирования/C#/Руководства/Полное руководство по C# 14 и платформе .NET 10/Глава 24. Работа с XML в C#/XML-Документы|Вперёд]]
