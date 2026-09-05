# HttpListener. HTTP-сервер

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Руководства|Руководства]] / [[Языки программирования/C#/Руководства/Сетевое программирование|Сетевое программирование]] / [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 2. Протокол HTTP|Протокол HTTP]] / HttpListener. HTTP-сервер

[[Языки программирования/C#/Руководства/Сетевое программирование/Глава 2. Протокол HTTP/Отправка и получение куки с HttpClient|Назад]] | [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 2. Протокол HTTP|Протокол HTTP]] | [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 3. Протокол TCP/TCP-клиент на сокетах|Вперёд]]

**Дата написания:** 05.09.2026

## HttpListener. HTTP-сервер

Для прослушивания подключений по протоколу HTTP и ответа на HTTP-запросы предназначен класс  HttpListener  
из пространства имен  `System.Net` . Данный класс построен на базе библиотеки 
HTTP.sys, которая является слушателем режима ядра и обрабатывает весь трафик HTTP для Windows. (Исходный код класса 
 [HttpListener](https://github.com/dotnet/runtime/blob/main/src/libraries/System.Net.HttpListener/src/System/Net/HttpListener.cs) )

Для создания объекта HttpListener применяется его единственный конструктор без параметров:

```csharp
HttpListener server = new HttpListener();
```

### Свойства  и методы HttpListener

Для получения информации или установки различных аспектов HttpListener можно применять свойства класса, основные из них:

- AuthenticationSchemes : возвращает или задает схему аутентификации клиентов
- IsListening : указывает, был ли запущен объект HttpListener
- IsSupported : указывает, можно ли использовать прослушиватель HttpListener в текущей операционной системе.
- Prefixes : возвращает префиксы URI, обрабатываемые этим объектом HttpListener.

Для управления HttpListener применяются методы класса. Некоторые из них:

- Close() : завершает работу HttpListener.
- GetContext() / GetContextAsync() : ожидает входящие запросы
- Start() : запускает прослушивание входящих запросов
- Stop() : останавливает получение новых входящих запросов и завершает обработку всех текущих запросов.

### Запуск HttpListener

Для работы с HttpListener нам надо вначале задать адреса, которые будут использоваться для обращения к приложению. 
Адреса задаются через свойство  Prefixes  класса HttpListener. При этом адрес должен оканчиваться на слеш, например: 
 
using System.Net;

HttpListener server = new HttpListener();
// установка адресов прослушки
server.Prefixes.Add("http://127.0.0.1:8888/connection/");
 В данном случае сервер будет прослушивать подключения по адресу "http://127.0.0.1:8888/connection/". Чтобы начать прослушивать входящие подключения, надо вызвать метод  Start() , для остановки сервера - метод  Stop() , а для окончательного закрытия 
HttpListener - метод  Close() . 
using System.Net;

HttpListener server = new HttpListener();
// установка адресов прослушки
server.Prefixes.Add("http://127.0.0.1:8888/connection/");
server.Start(); // начинаем прослушивать входящие подключения
// ............
server.Stop(); // останавливаем сервер
server.Close(); // закрываем HttpListener
 Контекст С помощью метода  GetContext()/GetContextAsync()  можно получить контекст входящего подключения в виде объекта  HttpListenerContext . С помощью свойств этого объекта 
можно получить информацию о входящем запросе и установить ответ: Request : возвращает информацию о запросе в виде объекта  `HttpListenerRequest` Response : устанавливаливает ответ сервера в виде объекта  `HttpListenerResponse` User : представляет данные об аутентифицированном пользователе в виде объекта  `System.Security.Principal.IPrincipal?` 
using System.Net;

HttpListener server = new HttpListener();
// установка адресов прослушки
server.Prefixes.Add("http://127.0.0.1:8888/connection/");
server.Start(); // начинаем прослушивать входящие подключения

// получаем контекст
var context = await server.GetContextAsync();

var request = context.Request;  // получаем данные запроса
var response = context.Response;    // получаем объект для установки ответа
var user = context.User;        // получаем данные пользователя

server.Stop(); // останавливаем сервер@media(min-width: 760px) {}
@media(min-width: 900px) {}
@media(min-width: 1100px) {}
@media(min-width: 1400px) {}
  Yandex.RTB R-A-201190-9  Отправка ответа Свойство  Response  объекта HttpListenerContext представляет объект  HttpListenerResponse , который позволяет настроить и 
отправить клиенту некоторый ответ. Для настройки ответа можно применять свойства HttpListenerResponse: ContentEncoding : устанавливает кодировку ответа в виде объекта Encoding  из заголовка Content-Type в виде объекта System.Text.Encoding. ContentLength64 : устанавливает заголовок Content-Length (размер ответа). ContentType : устанавливает значение заголовка Content-Type. Cookies : устанавливает файлы cookie, которые отправляются клиенту в виде объекта  `System.Net.CookieCollection` . Headers : устанавливает заголовки в виде коллекцию  `WebHeaderCollection`  (аналоги словаря, где названия заголовков служат ключами). KeepAlive : устанавливает значение  `bool` , которое указывает, требуется ли постоянное 
подключение. OutputStream : представляет поток ответа. ProtocolVersion : устанавливает версию протокола HTTP, которая используется в ответе. RedirectLocation : устанавливает адрес для переадресации. SendChunked : представляет значение bool, которое указывает, будет ли ответ разбиваться на чанки/части. StatusCode : устанавливает статусный код ответа. StatusDescription : устанавливает описание к статусному коду (строку статуса). Кроме того, класс предоставляет ряд методов для настройки поведения при отправке ответа: `void AddHeader (string name, string value)` : добавляет в ответ заголовок с именем name и значением value `void AppendCookie (System.Net.Cookie cookie);` : добавляет в ответ куки `void AppendHeader (string name, string value)` : добавляет к заголовоку с именем name значение value `void Redirect (string url)` : выполняет редирект на адрес url `void SetCookie (System.Net.Cookie cookie)` : устанавливает куки Например, отправим ответ клиенту: 
using System.Net;
using System.Text;

HttpListener server = new HttpListener();
// установка адресов прослушки
server.Prefixes.Add("http://127.0.0.1:8888/connection/");
server.Start(); // начинаем прослушивать входящие подключения

// получаем контекст
var context = await server.GetContextAsync();

var response = context.Response;
// отправляемый в ответ код htmlвозвращает
string responseText =
    @"<!DOCTYPE html>
    <html>
        <head>
            <meta charset='utf8'>
            <title>METANIT.COM</title>
        </head>
        <body>
            <h2>Hello METANIT.COM</h2>
        </body>
    </html>";
byte[] buffer = Encoding.UTF8.GetBytes(responseText);
// получаем поток ответа и пишем в него ответ
response.ContentLength64 = buffer.Length;
using Stream output = response.OutputStream;
// отправляем данные
await output.WriteAsync(buffer);
await output.FlushAsync();

Console.WriteLine("Запрос обработан");

server.Stop();
 В данном случае наша программа будет прослушивать все обращения по локальному адресу  `http://localhost:8888/connection/` При вызове метода  `listener.GetContextAsync()`  текущий поток блокируется, и слушатель начинает ожидать входящие подключения. Из этого метода 
получаем контекста HttpListenetContext, а у него объект ответа -  `context.Response` . После получения ответа получаем выходной поток через свойство response.OutputStream и пишем в него массив байтов: 
await output.WriteAsync(buffer);
 В итоге, если мы запустим приложение и обратимся в каком-нибудь браузере по адресу  `http://localhost:8888/connection/` , то нам отобразится 
сформированный в приложении код html: Получение информации о запросе Свойство Request возвращает информацию о запросе в виде объекта  `HttpListenerRequest` . Вся эта информация хранится в свойствах класса, которые в основном возвращают 
значения тех или иных заголовоков запроса: AcceptTypes : возвращает значение заголовка Accept в виде массива string[]. ClientCertificateError : возвращает код ошибки, связанной с сертификатом X509Certificate, предоставленным клиентом. ContentEncoding : возвращает значение кодировки из заголовка Content-Type в виде объекта System.Text.Encoding. ContentLength64 : возвращает заголовка Content-Length (если он не установлен, то возвращается -1). ContentType : возвращает значение заголовка Content-Type. Cookies : возвращает файлы cookie, отправленные вместе с запросом в виде объекта  `System.Net.CookieCollection` . HasEntityBody : возвращает  `true` , если в запросе кроме заголовоков переданы какие-нибудь данные (тело запроса). Headers : возвращает все заголовки в виде коллекцию  `System.Collections.Specialized.NameValueCollection`  (аналоги словаря, где названия заголовков служат ключами). HttpMethod : возвращает метод HTTP, использованный для отправки запроса клиентом. InputStream : возвращает поток, которые содержит данные тела запроса. IsAuthenticated : возвращает значение  `bool` , которое указывает, аутентифицирован ли клиент, отправивший этот запрос. IsLocal : возвращает значение  `bool` , которое указывает, был ли запрос отправлен с локального компьютера. IsSecureConnection : возвращает значение  `bool` , которое указывает, применяется ли для запроса протокол SSL. IsWebSocketRequest : возвращает значение  `bool` , которое указывает, использовался ли при запросе WebSocket. KeepAlive : возвращает значение  `bool` , которое указывает, требует ли клиент постоянного подключения. LocalEndPoint : возвращает IP-адрес сервера и номер порта, на который будет перенаправлен запрос. ProtocolVersion : возвращает версию протокола HTTP, которая используется в запросе. QueryString : возвращает строку запроса. RawUrl : возвращает URL-адрес запроса (без узла и порта). RemoteEndPoint : возвращает IP-адрес клиента, который отправил запрос. RequestTraceIdentifier : возвращает идентификатор HTTP-запроса. Url : возвращает адрес запроса в виде объекта  `Uri` . UrlReferrer : возвращает URI ресурса, который перенаправляет клиент на сервер. UserAgent : возвращает заголовок User-Agent. UserHostAddress : возвращает IP-адрес, на который будет перенаправлен запрос. UserHostName : возвращает DNS-хост, указанный клиентом. UserLanguages : возвращает значение заголовка AcceptLanguage (при его отсутствии возвращается null). Так, обработаем входящее подключение и получим эту информацию 
using System.Net;
using System.Text;

HttpListener server = new HttpListener();
// установка адресов прослушки
server.Prefixes.Add("http://127.0.0.1:8888/connection/");
server.Start(); // начинаем прослушивать входящие подключения
Console.WriteLine("Сервер запущен. Ожидание подключений...");

// получаем контекст
var context = await server.GetContextAsync();

var request = context.Request;  // получаем данные запроса

Console.WriteLine($"адрес приложения: {request.LocalEndPoint}");
Console.WriteLine($"адрес клиента: {request.RemoteEndPoint}");
Console.WriteLine(request.RawUrl);
Console.WriteLine($"Запрошен адрес: {request.Url}");
Console.WriteLine("Заголовки запроса:");
foreach(string item in request.Headers.Keys)
{
    Console.WriteLine($"{item}:{request.Headers[item]}");
}

var response = context.Response;    // получаем объект для установки ответа
byte[] buffer = Encoding.UTF8.GetBytes("Hello METANIT");
// получаем поток ответа и пишем в него ответ
response.ContentLength64 = buffer.Length;
using Stream output = response.OutputStream;
// отправляем данные
await output.WriteAsync(buffer);
await output.FlushAsync();

server.Stop(); // останавливаем сервер
 Также обратимся в браузере к приложению по адресу "http://127.0.0.1:8888/connection/", и консоль приложения выведет данные запроса. Консольный вывод в моем случае: 
Сервер запущен. Ожидание подключений...
адрес приложения: 127.0.0.1:8888
адрес клиента: 127.0.0.1:52913
/connection/
Запрошен адрес: http://127.0.0.1:8888/connection/
Заголовки запроса:
sec-ch-ua:"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"
sec-ch-ua-mobile:?0
sec-ch-ua-platform:"Windows"
Upgrade-Insecure-Requests:1
Sec-Fetch-Site:none
Sec-Fetch-Mode:navigate
Sec-Fetch-User:?1
Sec-Fetch-Dest:document
Connection:keep-alive
Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding:gzip, deflate, br
Accept-Language:ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,fr;q=0.6
Host:127.0.0.1:8888
User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36}
}
}
}

**Источник:** [https://metanit.com/sharp/net/7.1.php](https://metanit.com/sharp/net/7.1.php)

[[Языки программирования/C#/Руководства/Сетевое программирование/Глава 2. Протокол HTTP/Отправка и получение куки с HttpClient|Назад]] | [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 2. Протокол HTTP|Протокол HTTP]] | [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 3. Протокол TCP/TCP-клиент на сокетах|Вперёд]]
