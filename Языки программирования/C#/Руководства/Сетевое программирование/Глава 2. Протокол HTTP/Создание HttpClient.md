# Создание HttpClient

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Руководства|Руководства]] / [[Языки программирования/C#/Руководства/Сетевое программирование|Сетевое программирование]] / [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 2. Протокол HTTP|Протокол HTTP]] / Создание HttpClient

[[Языки программирования/C#/Руководства/Сетевое программирование/Глава 2. Протокол HTTP/Введение в протокол HTTP|Назад]] | [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 2. Протокол HTTP|Протокол HTTP]] | [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 2. Протокол HTTP/Отправка запросов с помощью HttpClient|Вперёд]]

**Дата написания:** 05.09.2026

## Создание HttpClient

Для отправки HTTP-запросов в .NET применяется класс  HttpClient  из пространства имен  System.Net.Http .

### Создание HttpClient

Для создания объекта HttpClient естественно можно использовать один из его конструкторов:

- 
public HttpClient (System.Net.Http.HttpMessageHandler handler);
 В качестве параметра передается объект HttpMessageHandler, применяемый для отправки сообщений по протоколу HTTP. Данный класс абстрактный, поэтому обычно передается объект одного из классов-наследников, 
например, HttpClientHandler или SocketsHttpHandler. Класс HttpMessageHandler реализует метод Dispose и утилизауется вместе с основным объектом HttpClient.
- public HttpClient (System.Net.Http.HttpMessageHandler handler, bool disposeHandler); Здесь добавляется второй параметр - disposeHandler. Если он равен  `true` , то объект HttpMessageHandler удаляется вместе с вызовом  `HttpClient.Dispose()` . 
Если же мы хотим и после удаления HttpClient продолжать использовать объект HttpMessageHandler, то этому параметру следует передать значение  `false`
- public HttpClient (); Этот вызов фактически эквивалентен вызову HttpClient(new HttpClientHandler(), true)

### Исчерпание сокетов

При создании объекта HttpClient следует учитывать, что он нацелен на многоразовое использование в течение всей жизни приложения. 
Создание отдельного объекта для каждого запроса может привести к исчерпанию количества доступных сокетов и приведет к ошибкам SocketException. Чтобы было понимание того, в чем проблема, 
рассмотрим следующий пример.

```csharp
Console.WriteLine("Приложение начало работу");
for (int i = 0; i < 10; i++)
{
    using (var client = new HttpClient())
    {
        using var result = await client.GetAsync("https://google.com");
        Console.WriteLine(result.StatusCode);
    }
}
Console.WriteLine("Приложение завершило работу");
```

Здесь в цикле 10 раз создается объект HttpClient. Казалось бы, в коде все нормально - класс HttpClient реализует интерфейс IDisposable, и применение конструкции using вроде должно гарантировать, 
что после завершения работы с HttpClient все связанные с ним ресурсы будут освобождены. В самой конструкции using запускаем запрос к ресурсу ("https://google.com" с помощью метода 
 `GetAsync()`  (далее мы рассмотрим этот метод). Данный метод возвращает некоторый результат, из которого с помощью свойства StatusCode мы можем получить статусный код ответа. 
Далее мы подробнее рассмотрим взаимодействие с интернет-ресурсами, а пока посмотрим в чем проблема. Запустим данный код:

Как видно из консольного вывода, код нормально отработал, было успешно выполнено 10 http-запросов, и приложение завершило свою работу.Но если мы запустим консольную утилитуnetstat, то мы увидим кучу висязих подключений:Так, мы видим, что ряд подключений имеют состояниеTIME_WAIT. Дело в том, что когда вызывается методDispose()у HttpClient, вместе с ним вызывается метод 
Dispose у используемого объекта HttpMessageHandler, который собственно и управляет отправкой сообщений и использует сокеты. При этом подключение в течение 240 секунд остается открытым в состоянии TIME_WAIT
Кроме того, есть ограничение на количество сокетов, которые можно использовать одновременно. И если объект HttpClient создается для каждого запроса, то число доступных сокетов при интенсивной нагрузке может быть быстро исчерпано, что 
приведет к ошибкам SocketException.Конкретно в данном случае можно было бы использовать обработчик HttpMessageHandler для всех создаваемых клиентов:HttpMessageHandler handler = new HttpClientHandler();

Console.WriteLine("Приложение начало работу");
for (int i = 0; i < 10; i++)
{
    using (var client = new HttpClient(handler, false))
    {
        using var result = await client.GetAsync("https://google.com");
        Console.WriteLine(result.StatusCode);
    }
}
Console.WriteLine("Приложение завершило работу");Но чтобы в принципе избежать возможной проблемы нехватки сокетов, Microsoft рекомендует для определения HttpClient один из следующих подходов:Долговременные экземпляры HttpClient в виде статических объектов или синглтонов, которые существуют в течение всей жизни приложения.Кратковременные экземпляры HttpClient, созданные с помощью фабрикиIHttpClientFactory.Вкратце рассмотрим эти подходы.HttpClient как статический объект/синглтонВ этом случае один объект HttpClient, который существует в течение всей жизни приложения:class Program
{
    static HttpClient client = new HttpClient();

    static async Task Main(string[] args)
    {
        // использование HttpClient
    }
}При этом следует учитывать, что HttpClient устанавливает записи DNS только при создании подключения. Он не отслеживает срок жизни (TTL), указанный DNS-сервером для определенной dns-записи, 
которая позволяет определить адрес хоста для создания запроса. Если записи DNS регулярно меняются, что 
может произойти в некоторых сценариях, клиент HttpClient не будет учитывать эти изменения. Поэтому для решения этой проблемы рекомендуется устанавливать свойство с настройкойSocketsHttpHandler.PooledConnectionLifetime, чтобы при замене подключения производился поиск DNS.
Например:class Program
{
    static HttpClient? httpClient;

    static async Task Main(string[] args)
    {
        var socketsHandler = new SocketsHttpHandler
        {
            PooledConnectionLifetime = TimeSpan.FromMinutes(2)
        };
        httpClient = new HttpClient(socketsHandler);
        
        // использование HttpClient
    }
}Здесь когда завершает интервал, указанный для свойства PooledConnectionLifetime (в данном случае 2 минуты), текущее подключение закрывается и создается новое.Создание HttpClient с помощью IHttpClientFactoryФабрика IHttpClientFactory управляет пулом объектов HttpMessageHandler. Если некоторый объект 
HttpMessageHandler продолжает существовать в этом пуле, то он может повторно использоваться для создания нового объекта HttpClient. Это позволяет снизить вероятность исчерпания сокетов.Для создания объекта HttpClient у фабрики IHttpClientFactory вызывается методCreateClient. Например, если у нас простое консольное или десктопное приложение, то нам надо добавить 
через nuget пакетыMicrosoft.Extensions.DependencyInjectionиMicrosoft.Extensions.Http:Если у нас проект веб-приложения, то подобные пакеты уже по умолчанию установлены в проект.Пример создания HttpClient для консольного приложения:using Microsoft.Extensions.DependencyInjection;

// определяем коллекцию сервисов
var services = new ServiceCollection();
// добавляем сервисы, связанные с HttpClient, в том числе IHttpClientFactory
services.AddHttpClient();
// создаем провайдер сервисов
var serviceProvider = services.BuildServiceProvider();
// получаем сервис IHttpClientFactory
var httpClientFactory = serviceProvider.GetService<IHttpClientFactory>();
// создаем объект HttpClient
var httpClient = httpClientFactory?.CreateClient();

// использование HttpClientСначала получаем коллекцию сервисов приложения. Затем используя встроенный механизм Dependency Injection, внедряем сервисы, связанные с HttpClient (в том числе IHttpClientFactory) в 
приложение. Для этого применяется методservices.AddHttpClient()После этого мы можем получить внедренный сервис IHttpClientFactory любыми доступными способами, которые применяются в .NET для получения внедренных зависимостей. В данном случае для 
простоты применяется паттерн Service locator:var httpClientFactory = serviceProvider.GetService<IHttpClientFactory>();В других ситуациях можно использовать другие способы, например, получение сервиса через параметр конструктора.Получив IHttpClientFactory, вызываем методCreateClient()и создаем HttpClient:var httpClient = httpClientFactory?.CreateClient()

**Источник:** [https://metanit.com/sharp/net/2.1.php](https://metanit.com/sharp/net/2.1.php)

[[Языки программирования/C#/Руководства/Сетевое программирование/Глава 2. Протокол HTTP/Введение в протокол HTTP|Назад]] | [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 2. Протокол HTTP|Протокол HTTP]] | [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 2. Протокол HTTP/Отправка запросов с помощью HttpClient|Вперёд]]
