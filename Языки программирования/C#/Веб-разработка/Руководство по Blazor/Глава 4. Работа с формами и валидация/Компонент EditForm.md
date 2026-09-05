# Компонент EditForm

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по Blazor|Руководство по Blazor]] / [[Языки программирования/C#/Веб-разработка/Руководство по Blazor/Глава 4. Работа с формами и валидация|Глава 4. Работа с формами и валидация]] / Компонент EditForm

[[Языки программирования/C#/Веб-разработка/Руководство по Blazor/Глава 4. Работа с формами и валидация/Встроенные компоненты ввода|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по Blazor/Глава 4. Работа с формами и валидация|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по Blazor/Глава 4. Работа с формами и валидация/Валидация на основе аннотаций данных|Вперёд]]

**Дата написания:** 05.09.2026

## Компонент EditForm

Последнее обновление: 30.11.2023




-

-

-














Для оформления всех элементов ввода в одну форму и упрощения валидации применяется компонент EditForm. Фактически он рендерится в элемент `<form>`


Класс EditForm предоставляет следующие свойства:


-

AdditionalAttributes: коллекция дополнительных атрибутов, которые применяются к форме

-

ChildContent: вложенное содержимое - набор компонентов ввода и элементов html

-

EditContext: контекст редактирования - по сути те данные, для работы с которыми применяется форма

-

Model: объект, привязанный к форме. Это свойство и `EditContext` - взаимоисключающиеся, нам нало установить только одно из этих свойств,
поскольку если установлено свойство `Model`, то `EditContext` создается на основе значения свойства `Model`

-

OnInvalidSubmit: метод-обработчик, который вызывается при отправке формы, если данные EditContext не проходят ввалидацию

-

OnSubmit: метод-обработчик, который вызывается при отправке формы (нажатии на кнопку типа `submit`)

-

OnValidSubmit: метод-обработчик, который вызывается при отправке формы, если данные EditContext проходят ввалидацию


Основная задача EditForm обеспечить валидацию введенных данных. Пример компонента, который использует EditForm:

```

@using Microsoft.AspNetCore.Components.Web
@using Microsoft.AspNetCore.Components.Forms
@rendermode RenderMode.InteractiveServer

<EditForm Model="@person" OnSubmit="Submit">
 <p>
 Name:<br />
 <InputText id="name" @bind-Value="person.Name" />
 </p>
 <p>
 Age:<br />
 <InputNumber id="age" @bind-Value="person.Age" />
 </p>
 <button type="submit">Submit</button>
</EditForm>
<h3>@message</h3>

@code {
 Person person = new();
 string message = "";

 void Submit()
 {
 message = $"Name: {person.Name} Age: {person.Age}";
 }

 public class Person
 {
 public string Name { get; set; } = "";
 public int Age { get; set; }
 }
}

```


Здесь данные представлены классом Person, который определяется в коде компонента App и имеет два свойства. В коде компонента App также определяется объект класса Person.
Этот объект выступает в качестве модели формы EditForm - для этого установлено свойство `Model`:

```
<EditForm Model="@person"
```


А поля ввода формы привязаны к свойствам объекта Person.


Кроме того, у EditForm установлен обработчик нажатия кнопки - метод `Submit()`, который выводит данные объекта Person на страницу.
![EditForm и создание формы в компонентах Blazor на C#](https://metanit.com./pics/4.14.png)


### EditContext


Вместо установки свойства `Model` у формы EditForm также можно использовать свойство EditContext, которое принимает объект одноименного типа
EditContext и которое устанавливает констект формы. Например:

```

@using Microsoft.AspNetCore.Components.Web
@using Microsoft.AspNetCore.Components.Forms
@rendermode RenderMode.InteractiveServer

<EditForm EditContext="editContext" OnSubmit="Submit">
 <p>
 Name:<br />
 <InputText id="name" @bind-Value="person.Name" />
 </p>
 <p>
 Age:<br />
 <InputNumber id="age" @bind-Value="person.Age" />
 </p>
 <button type="submit">Submit</button>
</EditForm>
<h3>@message</h3>

@code {
 string message = "";
 Person person = new();
 EditContext? editContext;

 protected override void OnInitialized()
 {
 editContext = new(person);
 }


 void Submit()
 {
 message = $"Name: {person.Name} Age: {person.Age}";
 }

 public class Person
 {
 public string Name { get; set; } = "";
 public int Age { get; set; }
 }
}

```


Для установки объекта EditContext у класса EditForm применяется одноименное свойство

```
<EditForm EditContext="editContext"
```


Стоит отметить, что если у EditForm устанавливается свойство EditContext, то свойство `Model` устанавливать не надо.


Здесь объект EditContext создается в методе `OnInitialized()`, который вызывается при инициализации компонента:

```

Person person = new();
EditContext? editContext;

protected override void OnInitialized()
{
 editContext = new(person);
}

```


В конструктор EditContext передается отслеживаемый объект - здесь объект Person (это может быть объет любого типа). В итоге результат работы приложения
будет тот же, что и при использовании свойства Model. Стоит также отметить, что у EditContext есть свойство Model, через которое можно получить отслеживаемую модель. Например:

```

void Submit()
{
 // преобразуем editContext.Model в тип Person
 if(editContext!=null && editContext.Model is Person p)
 message = $"Name: {p.Name} Age: {p.Age}";
}

```


Оба свойства - и `Model`, и `EditContext` применяются прежде всего для валидации данных, что будет рассмотрено в последующих статьях. Основная разница между ними,
что EditContext позволяет настроить некоторые моменты валидации, что может потребоваться в некоторых сценариях.











- Глава 1. Введение в Blazor


 - [Что такое Blazor](//metanit.com/sharp/blazor/1.1.php)

 - [Первое приложение на Blazor](//metanit.com/sharp/blazor/1.2.php)

 - [Рендеринг на сервере](//metanit.com/sharp/blazor/1.7.php)

 - [Рендеринг WebAssembly и авторендеринг](//metanit.com/sharp/blazor/1.8.php)

 - [Добавление Blazor в пустой проект ASP.NET Core](//metanit.com/sharp/blazor/1.4.php)

 - [Blazor WebAssembly. Первое приложение](//metanit.com/sharp/blazor/1.3.php)



- Глава 2. Компоненты


 - [Установка главного компонента](//metanit.com/sharp/blazor/2.2.php)

 - [Определение компонентов](//metanit.com/sharp/blazor/2.1.php)

 - [Вложенные компоненты. Параметры компонентов](//metanit.com/sharp/blazor/2.3.php)

 - [Передача произвольного набора атрибутов](//metanit.com/sharp/blazor/2.4.php)

 - [Обработка событий](//metanit.com/sharp/blazor/2.5.php)

 - [Обработка событий дочернего компонента в родительском](//metanit.com/sharp/blazor/2.6.php)

 - [Привязка данных](//metanit.com/sharp/blazor/2.7.php)

 - [Двусторонняя привязка и привязка параметров компонентов](//metanit.com/sharp/blazor/2.8.php)

 - [Каскадная передача значений](//metanit.com/sharp/blazor/2.9.php)

 - [Жизненный цикл компонентов](//metanit.com/sharp/blazor/2.10.php)

 - [Внедрение зависимостей в компоненты Blazor](//metanit.com/sharp/blazor/2.11.php)

 - [Привязка моделей](//metanit.com/sharp/blazor/2.12.php)

 - [Управление элементом head и компонент HeadOutlet](//metanit.com/sharp/blazor/2.13.php)

 - [Файл _Imports.razor и общие директивы компонентов](//metanit.com/sharp/blazor/2.14.php)



- Глава 3. Маршрутизация


 - [Маршрутизация между компонентами](//metanit.com/sharp/blazor/3.1.php)

 - [Компоновка](//metanit.com/sharp/blazor/3.2.php)

 - [Компонент NavLink](//metanit.com/sharp/blazor/3.3.php)

 - [Параметры маршрутов](//metanit.com/sharp/blazor/3.4.php)

 - [Параметры строки запроса](//metanit.com/sharp/blazor/3.5.php)

 - [Управление навигацией и NavigationManager](//metanit.com/sharp/blazor/3.6.php)



- Глава 4. Работа с формами и валидация


 - [Встроенные компоненты ввода](//metanit.com/sharp/blazor/4.1.php)

 - [Компонент EditForm](//metanit.com/sharp/blazor/4.2.php)

 - [Валидация на основе аннотаций данных](//metanit.com/sharp/blazor/4.3.php)

 - [Валидация и вывод сообщений об ошибках](//metanit.com/sharp/blazor/4.4.php)

 - [Программная валидация](//metanit.com/sharp/blazor/4.5.php)

 - [Кастомная валидации](//metanit.com/sharp/blazor/4.6.php)



- Глава 5. Отправка http-запросов


 - [HttpClient в проекте Blazor Server](//metanit.com/sharp/blazor/6.3.php)

 - [HttpClient в проекте Blazor WebAssembly](//metanit.com/sharp/blazor/6.1.php)

 - [Взаимодействие приложения Blazor с Web API](//metanit.com/sharp/blazor/6.2.php)



- Глава 6. Дополнительные статьи


 - [Конфигурация](//metanit.com/sharp/blazor/5.1.php)










 [Настройки](//metanit.com/settings.php)




 Помощь сайту


 [Помощь сайту](https://yoomoney.ru/to/410011174743222)



 Юмани:
 410011174743222



 Номер карты:
 4048415020898850











[Вконтакте](https://vk.com/metanit)|
[МАКС](https://max.ru/metanit)|
[Донаты/Помощь сайту](https://metanit.com/donations.php)


Contacts: metanit22@mail.ru


Copyright © Евгений Попов, metanit.com, 2026. Все права защищены.

---

**Источник:** [https://metanit.com/sharp/blazor/4.2.php](https://metanit.com/sharp/blazor/4.2.php)
