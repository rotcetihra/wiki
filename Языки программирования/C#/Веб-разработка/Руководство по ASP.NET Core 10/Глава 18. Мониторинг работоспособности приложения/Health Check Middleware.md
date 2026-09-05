# Health Check Middleware

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10|Руководство по ASP.NET Core 10]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 18. Мониторинг работоспособности приложения|Глава 18. Мониторинг работоспособности приложения]] / Health Check Middleware

[[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 17. Кэширование/Кэширование ответа и OutputCache|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET Core 10/Глава 18. Мониторинг работоспособности приложения|Содержание]]

**Дата написания:** 05.09.2026

## Health Check Middleware

Последнее обновление: 02.12.2022




-

-

-














Любое приложение не защищено от ошибок и снижения работоспособности в силу ряда причин, некоторые из которых трудно спрогнозировать на
этапе разработки. И соответственно возникает вопрос мониторинга рабоспособности приложения. Фреймворк ASP.NET Core предоставляет специальный компонент middleware для отслеживания работоспособности приложения. С помощью данного middleware мы можем настроить проверку различных метрик и показателей,
которые нам важны в рамках конкретного приложения. Например, можно проверять доступность какого-то сетевого сервиса, базы данных, использование физических ресурсов сервера (памяти, диска и т.д.)


### Добавление Health Checks Middleware


Для добавления функционала проверки работоспособности прежде всего необходимо добавить в коллекцию сервисов приложения сервис HealthCheckService с помощью метода AddHealthChecks()

```
builder.Services.AddHealthChecks();
```


Проверка работоспособности доступна через специальные конечные точки. Для задания конечной точки применяются два метода:

```
app.UseHealthChecks("/health");
```


и

```
app.MapHealthChecks("/health");
```


В реальности разница между этими не большая. Первый метод принимает, как минимум, строку пути, запрос по которому будет обрабатываться. Второй метод принимает шаблон пути. В случаях выше оба
метода позволяют обрабатывать запросы по пути "/health"


### Пример применения Health Check Middleware


Рассмотрим небольшой пример, где имитириуется применение этой функционость. Допустим, наше приложение разделено на два слоя. Первый слой (первое приложение) генерирует некоторые данные,
а второй слой (второе приложение) получает данные и непосредственно взаимодействует с клиентом.


В первом проекте, который будет отвечать за генерацию данных (допустим, он будет называться DataApp) определим следующий код:

```

var builder = WebApplication.CreateBuilder(args);
builder.WebHost.UseUrls("https://[::]:33333");

var app = builder.Build();

app.MapGet("/reset", () =>
{
 Latency.ResetLatency();
 return "Application reset";
});
app.MapGet("/data", async () =>
{
 int latency = Latency.GetLatency();
 await Task.Delay(latency);
 return $"Application latency: {latency}";
});

app.Run();

static class Latency
{
 static int counter = 1;
 // увеличиваем счетчик
 public static int GetLatency() => counter++ * 500;
 // сбрасываем счетчик
 public static void ResetLatency() => counter = 1;
}

```


Это приложение будет имитировать латентность или задержки при получении и обработке запросов. Для этого определяем вспомогательный статический класс Latency. Его метод
`GetLatency()` увеличивает счетчик и возвращает значение `counter++ * 500`. Метод `ResetLatency()` сбрасывает значение счетчика к начальному.


Для простоты данное приложение будет запускаться по адресу `https://localhost:33333`.


Приложение определяет две конечные точки. Конечная точка `app.MapGet("/reset"...` обрабатывает запросы по пути "reset" и условно осуществляет восстановление сервера
(по сути сбрасывает значение счетчика к начальному).


Вторая конечная точка - `app.MapGet("/data"...` собственно посылает данные. Но для имитации все повыщаеющеся латентности приложения ее обработчик получает новое значение из метода
`Latency.GetLatency()`, осуществляет задержку и отправляет ответ.

```

int latency = Latency.GetLatency();
await Task.Delay(latency);
return $"Application latency: {latency}";

```


То есть таким образом, мы имитируем повышение латентности с каждым новым запросом. Соответственно с каждым новым запросом при вызове метода
`Latency.GetLatency()` будет все больше увеличиваться значение счетчика и будет возвращаться все большее значение. И сервер будет все медленнее и медленнее обрабатывать запросы.


Теперь определим второй проект ASP.NET Core, который будет обращаться к предыдущему приложению DataApp и проверять его работоспособность:

```

using Microsoft.Extensions.Diagnostics.HealthChecks;
using System.Diagnostics;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddHealthChecks()
 .AddCheck<RequestTimeHealthCheck>("RequestTimeCheck"); // проверяем работоспособность с RequestTimeCheck

builder.Services.AddHttpClient(); // подключаем HttpClient
builder.WebHost.UseUrls("https://[::]:44444"); // обрабатываем запросы по адресу https://localhost:44444

var app = builder.Build();
app.MapHealthChecks("/health");

app.MapGet("/", async (HttpClient httpClient) =>
{
 // отправляем запрос к другому сервису и возвращаем его ответ
 var response = await httpClient.GetAsync("https://localhost:33333/data");
 return await response.Content.ReadAsStringAsync();
});

app.Run();

public class RequestTimeHealthCheck : IHealthCheck
{
 int degraded_level = 2000; // уровень плохой работы
 int unhealthy_level = 5000; // нерабочий уровень
 HttpClient httpClient;
 public RequestTimeHealthCheck(HttpClient client) => httpClient = client;
 public async Task<HealthCheckResult> CheckHealthAsync(HealthCheckContext context,
 CancellationToken cancellationToken = default)
 {
 // получаем время запроса
 Stopwatch sw = Stopwatch.StartNew();
 await httpClient.GetAsync("https://localhost:33333/data");
 sw.Stop();
 var responseTime = sw.ElapsedMilliseconds;
 // в зависимости от времени запроса возвращаем определенный результат
 if (responseTime < degraded_level)
 {
 return HealthCheckResult.Healthy("Система функционирует хорошо");
 }
 else if (responseTime < unhealthy_level)
 {
 return HealthCheckResult.Degraded("Снижение качества работы системы");
 }
 else
 {
 return HealthCheckResult.Unhealthy("Система в нерабочем состоянии. Необходим ее перезапуск.");
 }
 }
}

```


Здесь прежде всего подключаем сервис проверки работоспособности:

```
builder.Services.AddHealthChecks()
```


Этот метод возвращает объект `IHealthCheckBuilder`, который применяется для создания и настройки сервиса HealthCheckService. Но сама проверка работоспособоности применяется
объект IHealthCheck. И для добавления такого объекта применяется метод AddCheck():

```
.AddCheck<RequestTimeHealthCheck>("RequestTimeCheck");
```


Этот метод типизируется типом, который реализует интерфейс IHealthCheck, а в качества параметра принимает строку - имя для сервиса проверки.


В нашем случае в качестве реализации IHealthCheck применяется класс RequestTimeCheck. Класс должен реализовать метод интерфейса CheckHealthAsync. В примере выше
в этом методе отправляем запрос к первому приложению к его конечной точке "/data" и проверяем время запроса:

```

Stopwatch sw = Stopwatch.StartNew();
await httpClient.GetAsync("https://localhost:33333/data");
sw.Stop();
var responseTime = sw.ElapsedMilliseconds;

```


Если время запроса превосходит определенные предустоновленые пределы, то возвращает соответствующее сообщение о работоспособности приложения:

```

 if (responseTime < degraded_level)
{
 return HealthCheckResult.Healthy("Система функционирует хорошо");
}
else if (responseTime < unhealthy_level)
{
 return HealthCheckResult.Degraded("Снижение качества работы системы");
}
else
{
 return HealthCheckResult.Unhealthy("Система в нерабочем состоянии. Необходим ее перезапуск.");
}

```


Метод возвращает результат проверки работоспособности - структура HealthCheckResult. Конкретный результат устанавливается с помощью одного из методов структуры:
`Healthy()` (приложение работает нормально), `Degraded()` (работоспособность снижается) и `Unhealthy()` (приложение неработоспособно).
Каждый метод возвращает соответствующий экземпляр структуры, который сигнализирует о состоянии приложения.


Когда, при каких условиях считать приложение неработоспособным - это зависит от нашей задачи, логики нашего приложения, метрик, которые мы применяем для оценки и конкретной ситуации.
В данном случае все зависит от времени запроса.


Для получения информации о работоспособности приложении определена конечная точка "/health" посредством метода

```
app.MapHealthChecks("/health");
```

![Health Check Middleware в приложении на ASP.NET Core и C#](https://metanit.com./pics/18.1.png)


Запустим сначала приложение DataApp, а затем AggregationApp. Обратимся в браузере по адресу "https://localhost:44444/" (то есть к AggregationApp):
![Проверка работоспособности приложения на ASP.NET Core и C#](https://metanit.com./pics/18.2.png)


В данном случае AggregationApp будет обращаться по адресу "https://localhost:33333/data" к DataApp и получает данные. Но внутри DataApp это приведет к увеличению задержки
при обработки запроса. И каждый последующий запрос будет обрабатываться все медленнее и медленнее.


Если после 5 запросов мы обратимся в браузере по адресу "https://localhost:44444/health", то консоль браузера выведет предупреждение о снижении работоспособности
![Degraded application на ASP.NET Core и C#](https://metanit.com./pics/18.3.png)


Еще после нескольких запросов приложение сигнализирует об условно нерабочем состоянии, что свидетельствует, что латентность в приложении DataApp превысила сколь-нибудь допустимые пределы.
![Unhealthy application на ASP.NET Core и C#](https://metanit.com./pics/18.4.png)


Таким образом, на основании некоторых метрик мы можем определить мехнизм уведомления о состоянии системы.


### Сервис мониторинга


Следует отметить, что, как правило, за мониторинг приложения отвечает какое-то внешнее приложение. Такие приложения мониторинга еще называют "watchdog" (дословно "сторожевой пёс",
но в русскоязычной литературе для этого обычно используется понятие "Сторожевой таймер"). Так, в примере выше и DataApp и AggregationApp можно рассматривать как слои/уровни
одного общего приложения. Для мониторинга определим третий проект. Если речь идет о C#, то нередко для этой цели определяется фоновый сервис. Но для простоты и текста мы определим простое консольное приложение:

```

HttpClient client = new HttpClient();

while (true)
{
 using var response = await client.GetAsync("https://localhost:44444/health");
 var status = await response.Content.ReadAsStringAsync();
 if (status == "Unhealthy")
 {
 Console.WriteLine($"{DateTime.Now.ToLongTimeString()} : сервер в нерабочем состоянии, осуществляется перезапуск.");
 await client.GetAsync("https://localhost:33333/reset");
 }
 else
 {
 Console.WriteLine($"{DateTime.Now.ToLongTimeString()} : все норм");
 }
 await Task.Delay(10000); // задержка на 10 секунд
}

```


В данном случае сначала осуществляем запрос по адресу "https://localhost:44444/health" и получаем статус. Если приложение в нерабочем состоянии, то обращаемся по адресу "https://localhost:33333/reset" и
условно перезапускаем приложение DataApp (фактически сбрасываем счетчик, что увеличивает скорость обработки запросов).
![watchdog для приложения на ASP.NET Core и C#](https://metanit.com./pics/18.5.png)










- Глава 1. Введение в ASP.NET Core


 - [Что такое ASP.NET Core](//metanit.com/sharp/aspnet6/1.1.php)

 - [Первое приложение на ASP.NET Core с .NET CLI](//metanit.com/sharp/aspnet6/1.3.php)

 - [Первое приложение в Visual Studio](//metanit.com/sharp/aspnet6/1.2.php)



- Глава 2. Основы в ASP.NET Core


 - [Создание и запуск приложения. WebApplication и WebApplicationBuilder](//metanit.com/sharp/aspnet6/2.1.php)

 - [Конвейер обработки запроса и middleware](//metanit.com/sharp/aspnet6/2.2.php)

 - [Метод Run и определение терминального middleware](//metanit.com/sharp/aspnet6/2.3.php)

 - [HttpResponse. Отправка ответа](//metanit.com/sharp/aspnet6/2.4.php)

 - [HttpRequest. Получение данных запроса](//metanit.com/sharp/aspnet6/2.5.php)

 - [Отправка файлов](//metanit.com/sharp/aspnet6/2.6.php)

 - [Отправка форм](//metanit.com/sharp/aspnet6/2.8.php)

 - [Переадресация](//metanit.com/sharp/aspnet6/2.9.php)

 - [Отправка и получение json](//metanit.com/sharp/aspnet6/2.10.php)

 - [Создание простейшего API](//metanit.com/sharp/aspnet6/2.11.php)

 - [Загрузка файлов на сервер](//metanit.com/sharp/aspnet6/2.12.php)

 - [Метод Use](//metanit.com/sharp/aspnet6/2.7.php)

 - [Создание ветки конвейера. UseWhen и MapWhen](//metanit.com/sharp/aspnet6/2.13.php)

 - [Метод Map](//metanit.com/sharp/aspnet6/2.14.php)

 - [Классы middleware](//metanit.com/sharp/aspnet6/2.15.php)

 - [Построение конвейера обработки запроса](//metanit.com/sharp/aspnet6/2.16.php)

 - [IWebHostEnvironment и окружение](//metanit.com/sharp/aspnet6/2.17.php)



- Глава 3. Dependency Injection


 - [Внедрение зависимостей и IServiceCollection](//metanit.com/sharp/aspnet6/4.1.php)

 - [Создание сервисов](//metanit.com/sharp/aspnet6/4.2.php)

 - [Получение зависимостей](//metanit.com/sharp/aspnet6/4.3.php)

 - [Жизненный цикл зависимостей](//metanit.com/sharp/aspnet6/4.4.php)

 - [Применение сервисов в классах middleware](//metanit.com/sharp/aspnet6/4.5.php)

 - [Scoped-сервисы в singleton-объектах](//metanit.com/sharp/aspnet6/4.6.php)

 - [Множественная регистрация сервисов](//metanit.com/sharp/aspnet6/4.7.php)



- Глава 4. Маршрутизация


 - [Конечные точки. Метод Map](//metanit.com/sharp/aspnet6/3.1.php)

 - [Параметры маршрута](//metanit.com/sharp/aspnet6/3.2.php)

 - [Ограничения маршрутов](//metanit.com/sharp/aspnet6/3.3.php)

 - [Создание ограничений маршрутов](//metanit.com/sharp/aspnet6/3.4.php)

 - [Передача зависимостей в конечные точки](//metanit.com/sharp/aspnet6/3.5.php)

 - [Сопоставление запроса с конечной точкой](//metanit.com/sharp/aspnet6/3.6.php)

 - [Сочетание конечных точек с другими middleware](//metanit.com/sharp/aspnet6/3.7.php)

 - [Получение параметров строки запроса](//metanit.com/sharp/aspnet6/3.8.php)



- Глава 5. Статические файлы


 - [Установка каталога статических файлов. UseStaticFiles](//metanit.com/sharp/aspnet6/5.1.php)

 - [Работа со статическими файлами](//metanit.com/sharp/aspnet6/5.2.php)

 - [Статические файлы и MapStaticAssets](//metanit.com/sharp/aspnet6/5.3.php)



- Глава 6. Конфигурация


 - [Основы конфигурации](//metanit.com/sharp/aspnet6/6.1.php)

 - [Нефайловые провайдеры конфигурации](//metanit.com/sharp/aspnet6/6.2.php)

 - [Конфигурация в файлах JSON, XML и Ini](//metanit.com/sharp/aspnet6/6.3.php)

 - [Конфигурация по умолчанию и объединение конфигураций](//metanit.com/sharp/aspnet6/6.4.php)

 - [Анализ конфигурации](//metanit.com/sharp/aspnet6/6.5.php)

 - [Создание провайдера конфгурации](//metanit.com/sharp/aspnet6/6.6.php)

 - [Проекция конфигурации на классы](//metanit.com/sharp/aspnet6/6.7.php)

 - [Передача конфигурации через IOptions](//metanit.com/sharp/aspnet6/6.8.php)



- Глава 7. Логгирование


 - [Ведение лога и ILogger](//metanit.com/sharp/aspnet6/7.1.php)

 - [Фабрика логгера и провайдеры логгирования](//metanit.com/sharp/aspnet6/7.2.php)

 - [Конфигурация и фильтрация логгирования](//metanit.com/sharp/aspnet6/7.3.php)

 - [Создание провайдера логгирования](//metanit.com/sharp/aspnet6/7.4.php)



- Глава 8. Состояние приложения. Куки. Сессии


 - [HttpContext.Items](//metanit.com/sharp/aspnet6/8.1.php)

 - [Куки](//metanit.com/sharp/aspnet6/8.2.php)

 - [Сессии](//metanit.com/sharp/aspnet6/8.3.php)



- Глава 9. Обработка ошибок


 - [Обработка исключений](//metanit.com/sharp/aspnet6/9.1.php)

 - [Обработка ошибок HTTP](//metanit.com/sharp/aspnet6/9.2.php)



- Глава 10. Results API


 - [Введение в Results API](//metanit.com/sharp/aspnet6/10.1.php)

 - [Отправка текста и json в Results API](//metanit.com/sharp/aspnet6/10.2.php)

 - [Переадресация в Results API](//metanit.com/sharp/aspnet6/10.3.php)

 - [Отправка статусных кодов в Results API](//metanit.com/sharp/aspnet6/10.4.php)

 - [Отправка файлов в Results API](//metanit.com/sharp/aspnet6/10.5.php)

 - [Определение своего типа IResult](//metanit.com/sharp/aspnet6/10.6.php)



- Глава 11. Web API


 - [Пример приложения Web API](//metanit.com/sharp/aspnet6/11.1.php)



- Глава 12. Работа с базой данных и Entity Framework


 - [Подключение Entity Framework](//metanit.com/sharp/aspnet6/12.1.php)

 - [Основные операции с данными в Entity Framework Core](//metanit.com/sharp/aspnet6/12.2.php)



- Глава 13. Аутентификация и авторизация


 - [Введение в аутентификацию и авторизацию](//metanit.com/sharp/aspnet6/13.1.php)

 - [Аутентификация с помощью JWT-токенов](//metanit.com/sharp/aspnet6/13.2.php)

 - [Авторизация с помощью JWT-токенов в клиенте JavaScript](//metanit.com/sharp/aspnet6/13.3.php)

 - [Аутентификация с помощью куки](//metanit.com/sharp/aspnet6/13.4.php)

 - [HttpContext.User, ClaimPrincipal и ClaimsIdentity](//metanit.com/sharp/aspnet6/13.5.php)

 - [ClaimPrincipal и объекты Claim](//metanit.com/sharp/aspnet6/13.6.php)

 - [Авторизация по ролям](//metanit.com/sharp/aspnet6/13.7.php)

 - [Авторизация на основе Claims](//metanit.com/sharp/aspnet6/13.8.php)

 - [Создание ограничений для авторизации](//metanit.com/sharp/aspnet6/13.9.php)



- Глава 14. CORS и кросс-доменные запросы


 - [Подключение CORS в приложении](//metanit.com/sharp/aspnet6/14.1.php)

 - [Конфигурация CORS](//metanit.com/sharp/aspnet6/14.2.php)

 - [Политики CORS](//metanit.com/sharp/aspnet6/14.3.php)

 - [Глобальная и локальная настройка CORS](//metanit.com/sharp/aspnet6/14.4.php)



- Глава 15. URL Rewriting


 - [Введение в URL Rewriting](//metanit.com/sharp/aspnet6/15.1.php)

 - [Правила IIS для URL Rewriting](//metanit.com/sharp/aspnet6/15.2.php)

 - [Применение правил Apache для URL Rewriting](//metanit.com/sharp/aspnet6/15.3.php)

 - [Создание правил URL Rewriting](//metanit.com/sharp/aspnet6/15.4.php)



- Глава 16. Клиентская разработка


 - [Бандлинг и минификация](//metanit.com/sharp/aspnet6/16.1.php)

 - [Пакетный менеджер Libman](//metanit.com/sharp/aspnet6/16.2.php)

 - [Пакетный менеджер NPM](//metanit.com/sharp/aspnet6/16.3.php)



- Глава 17. Кэширование


 - [Кэширование с помощью MemoryCache](//metanit.com/sharp/aspnet6/17.1.php)

 - [Распределенное кэширование. Redis](//metanit.com/sharp/aspnet6/17.2.php)

 - [Сжатие ответа](//metanit.com/sharp/aspnet6/17.3.php)

 - [Кэширование статических файлов](//metanit.com/sharp/aspnet6/17.4.php)

 - [Кэширование ответа и OutputCache](//metanit.com/sharp/aspnet6/17.5.php)



- Глава 18. Мониторинг работоспособности приложения


 - [Health Check Middleware](//metanit.com/sharp/aspnet6/18.1.php)










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

**Источник:** [https://metanit.com/sharp/aspnet6/18.1.php](https://metanit.com/sharp/aspnet6/18.1.php)
