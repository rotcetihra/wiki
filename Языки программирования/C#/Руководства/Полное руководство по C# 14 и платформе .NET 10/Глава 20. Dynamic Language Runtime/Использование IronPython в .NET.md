# Использование IronPython в .NET

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Руководства|Руководства]] / [[Языки программирования/C#/Руководства/Полное руководство по C# 14 и платформе .NET 10|Полное руководство по C# 14 и платформе .NET 10]] / [[Языки программирования/C#/Руководства/Полное руководство по C# 14 и платформе .NET 10/Глава 20. Dynamic Language Runtime|Dynamic Language Runtime]] / Использование IronPython в .NET

[[Языки программирования/C#/Руководства/Полное руководство по C# 14 и платформе .NET 10/Глава 20. Dynamic Language Runtime/DynamicObject и ExpandoObject|Назад]] | [[Языки программирования/C#/Руководства/Полное руководство по C# 14 и платформе .NET 10/Глава 20. Dynamic Language Runtime|Dynamic Language Runtime]] | [[Языки программирования/C#/Руководства/Полное руководство по C# 14 и платформе .NET 10/Глава 21. Сборка мусора, управление памятью и указатели/Сборщик мусора в C#|Вперёд]]

**Дата написания:** 05.09.2026

## Использование IronPython в .NET

Одним из ключевых достоинств среды DLR является поддержка таких динамических языков как  IronPython  и 
 IronRuby . Казалось бы, зачем нам нужны еще языки, тем более которые применяются в рамках другого языка C#?

На самом деле динамические языки, возможно, не часто используются, однако есть сферы, где их применение является целесообразным. Например, 
написание клиентских сценариев. Возможно, пользователь нашей программы захочет внести какое-то дополнительное поведение в программу и для этого может 
использоваться IronPython. Можно даже сказать, что создание клиентских сценариев широко распространено в наши дни, многие программы и даже игры 
поддерживают добавление клиентских сценариев, написанных на различных языках.

Кроме того, возможно, есть библиотеки на Python, функциональность которых может отсутствовать в .NET. И в этом случае опять же нам может помочь IronPython.

Рассмотрим на примере применение IronPython. Но для начала необходимо добавить в проект несколько пакетов через пакетный менеджер NuGet. Для 
того нажмем в окне проекта на узел  Dependencies  правой кнопкой мыши и выберем в появившемся списке пункт  Manage NuGet Packages...  (Управление NuGet-пакетами):

И перед нами откроется окно пакетного менеджера. Чтобы найти нужный пакет, введем в поле поиска "DLR", и менеджер отобразит ряд результатов, из которых 
первый - пакетDynamicLanguageRuntimeнеобходимо установить.После этого в проект в узел Dependencies добавляется библиотекаMicrosoft.Scripting.Теперь также нам надо добавить пакетIronPython. Для этого введем в поле поиска "IronPython" и после этого установим одноименный 
пакет:После установки пакета в узле Dependencies добавляется библиотека IronPython.Теперь напишем примитивную программу:using IronPython.Hosting;
using Microsoft.Scripting.Hosting;

ScriptEngine engine = Python.CreateEngine();
engine.Execute("print('hello, world')");Консольный вывод:hello, worldЗдесь используется выражениеprint('hello, world')языка Python, которое выводит на консоль строку. Для создания движка, выполняющего скрипт, 
применяется классScriptEngine. А его методExecute()выполняет скрипт.Мы также могли бы определить файлhello.py, то есть обычный текстовый файл с кодом на языке Python, со следующим содержимым:print ("hello, metanit.com")И запустить его в программе:using IronPython.Hosting;
using Microsoft.Scripting.Hosting;

ScriptEngine engine = Python.CreateEngine();
engine.ExecuteFile("hello.py");В данном случае предполагается, что скрипт находится в проекте:Также можно использовать абсолютные пути, например, если скрипт располагается по пути "D://hello.py":ScriptEngine engine = Python.CreateEngine();
engine.ExecuteFile("D://hello.py");ScriptScopeОбъект ScriptScope позволяет взаимодействовать со скриптом, получая или устанавливая его переменные, получая ссылки на функции. Например, 
напишем простейший скриптhello2.py, который использует переменные:x = 10
z = x + y
print(z)Теперь напишем программу, которая будет взаимодействовать со скриптом:using IronPython.Hosting;
using Microsoft.Scripting.Hosting;

int y = 22;

ScriptEngine engine = Python.CreateEngine();
ScriptScope scope = engine.CreateScope();
scope.SetVariable("y", y);
engine.ExecuteFile("hello.py", scope);
dynamic x = scope.GetVariable("x");
dynamic z = scope.GetVariable("z");
Console.WriteLine($"{x} + {y} = {z}");Объект ScriptScope с  помощью методаSetVariableпозволяет установить переменные в скрипте, а с помощью методаGetVariable()- 
получить их.Консольный вывод:32
10 + 22 = 32Вызов функций из IronPythonОпределим в файлеhello.pyфункцию для вычисления квадрата числа:def square(n):
   return n * nТеперь обратимся к этой функции в коде C#:using IronPython.Hosting;
using Microsoft.Scripting.Hosting;

int number = 5;

ScriptEngine engine = Python.CreateEngine();
ScriptScope scope = engine.CreateScope();

engine.ExecuteFile("hello.py", scope);
dynamic square = scope.GetVariable("square");
// вызываем функцию и получаем результат
dynamic result = square(number);
Console.WriteLine(result);      // 25Получить объект функции можно также, как и переменную:scope.GetVariable("square");. Затем с этим объектом работаем также, как и с 
любым другим методом. В итоге при передаче в метод/функцию square числа 5 его результатом будет 25.

**Источник:** [https://metanit.com/sharp/tutorial/9.3.php](https://metanit.com/sharp/tutorial/9.3.php)

[[Языки программирования/C#/Руководства/Полное руководство по C# 14 и платформе .NET 10/Глава 20. Dynamic Language Runtime/DynamicObject и ExpandoObject|Назад]] | [[Языки программирования/C#/Руководства/Полное руководство по C# 14 и платформе .NET 10/Глава 20. Dynamic Language Runtime|Dynamic Language Runtime]] | [[Языки программирования/C#/Руководства/Полное руководство по C# 14 и платформе .NET 10/Глава 21. Сборка мусора, управление памятью и указатели/Сборщик мусора в C#|Вперёд]]
