# Адреса Uri

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Руководства|Руководства]] / [[Языки программирования/C#/Руководства/Сетевое программирование|Сетевое программирование]] / [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 1. Основы работы с сетями|Основы работы с сетями]] / Адреса Uri

[[Языки программирования/C#/Руководства/Сетевое программирование/Глава 1. Основы работы с сетями/Адреса в .NET|Назад]] | [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 1. Основы работы с сетями|Основы работы с сетями]] | [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 1. Основы работы с сетями/DNS|Вперёд]]

**Дата написания:** 05.09.2026

## Адреса Uri

В прошлой статье были рассмотрены ip-адреса. Однако подобными адресами трудно оперировать в реальной жизни, например, их трудно запомнить. И 
чтобы упростить идентификацию и адресацию устройств в сети также используются URI/URL.

Uniform Resource Identifier (URI)  предоставляет строку, которая глобально и уникально идентифицирует ресурс в сети

Подвидом URI является  Uniform Resource Locator (URL)  - универсальный стандарт для определения размещения ресурсов в сети. Однако в реальности URI и URL частно 
отождествляют и используют взаимозаменяемо. Например, строка  `https://metanit.com`  представляет URL-адрес, по которому можно обращаться к данному сайту. Подобные адреса гораздно проще запомнить и использовать, нежели 
IP-адреса.

Рассмотрим из каких частей состоит URL. Общая форма адреса URL выглядит следующим образом:

```csharp
scheme:[//authority/]path[?query][#fragment]
```

authority включает домен и порт, а также возможные учетные данные пользователя как логин и пароль:

```csharp
//[access_credentials][@]host_domain[:port]
```

Символ @ отделяет учетные данные от домена. Параметр  `access_credentials` , который описывает учетные данные, задается в виде

```csharp
[user_id][:][password]
```

Параметр  `user_id`  предоставляет логин, а  `password`  - пароль для доступа к ресурсу. 
Они отделяются друг от друга двоеточием :

Компонент  query  имеет следующую форму:

```csharp
?[parameter1=value2][(;|&)parameter2=value2]...
```

В конце после символа решетки # может указываться фрагмент - необязательная строка для идентификации компонентов внутри URL. Обычно применяется в веб-браузерах для навигации по 
частям веб-страницы.

Но для протокола IP, через который идет взаимодействие, URI-адреса не существуют. Поэтому при отправке или передаче данных по доменному имени, компьютер еще обращается к 
системе доменных имен или  Domain Name System (DNS) , которая выполняют сопоставление между интернет-адресами в формате IPv4 или IPv6 и доменными названиями.

### System.Uri

За представление URI-адресов в .NET отвечает класс  System.Uri . Данный класс имеет ряд конструкторов. Самый простой принимает в качестве параметра строковый адрес ресурса, например:

```csharp
string uriString = "https://metanit.com/";
Uri myUri = new(uriString);
```

В данном случае создается Uri для адреса "https://metanit.com/".

Для получения информации об адресе, его различных компонентах класс Uri предоставляет ряд свойств. Рассмотрим базовые:

- AbsoluteUri : возвращает абсолютный адрес URI 
- Authority : возвращает либо имя хоста в соответствии с системой доменных имен DNS, либо IP-адрес и порт сервера.
- Fragment : возвращает фрагмент адреса URI.
- Host : возвращает хост.
- IsAbsoluteUri : возвращает true, если адрес абсолютный.
- IsDefaultPort : возвращает true, если адрес URI использует порт по умолчанию для своей схемы.
- IsFile : возвращает true, если адрес Uri представляет адрес файла.
- IsLoopback : возвращает true, если адрес Uri указывает на локальный хост.
- OriginalString : возвращает оригинальную строку адреса URI, которая передана в конструктор Uri.
- PathAndQuery : возвращает значения свойств  `AbsolutePath`  и  `Query` , разделяя их вопросительным знаком (?).
- Port : возвращает номер порта для текущего адреса URI.
- Query : возвращает строку запроса из текущего адреса URI.
- Scheme : возвращает схему текущего адреса URI.
- Segments : возвращает массив сегментов пути для текущего адреса URI. Каждый сегмент представляет часть пути, которая ограничена слешами
- UserInfo : возвращает имя и пароль пользователя.

Исследуем адрес:

```csharp
Uri uri = new Uri("https://user:password@www.somesite.com:443/home/index?q1=v1&q2=v2#fragmentName");

Console.WriteLine($"AbsolutePath: {uri.AbsolutePath}");
Console.WriteLine($"AbsoluteUri: {uri.AbsoluteUri}");
Console.WriteLine($"Fragment: {uri.Fragment}");
Console.WriteLine($"Host: {uri.Host}");
Console.WriteLine($"IsAbsoluteUri: {uri.IsAbsoluteUri}");
Console.WriteLine($"IsDefaultPort: {uri.IsDefaultPort}");
Console.WriteLine($"IsFile: {uri.IsFile}");
Console.WriteLine($"IsLoopback: {uri.IsLoopback}");
Console.WriteLine($"OriginalString: {uri.OriginalString}");
Console.WriteLine($"PathAndQuery: {uri.PathAndQuery}");
Console.WriteLine($"Port: {uri.Port}");
Console.WriteLine($"Query: {uri.Query}");
Console.WriteLine($"Scheme: {uri.Scheme}");
Console.WriteLine($"Segments: {string.Join(", ", uri.Segments)}");
Console.WriteLine($"UserInfo: {uri.UserInfo}");
```

Консольный вывод:

```csharp
AbsolutePath: /home/index
AbsoluteUri: https://user:password@www.somesite.com/home/index?q1=v1&q2=v2#fragmentName
Fragment: #fragmentName
Host: www.somesite.com
IsAbsoluteUri: True
IsDefaultPort: True
IsFile: False
IsLoopback: False
OriginalString: https://user:password@www.somesite.com:443/home/index?q1=v1&q2=v2#fragmentName
PathAndQuery: /home/index?q1=v1&q2=v2
Port: 443
Query: ?q1=v1&q2=v2
Scheme: https
Segments: /, home/, index
UserInfo: user:password
```

Стоит отметить, что адреса могут быть абсолютными, например, "http://metanit.com", и относительными, например, "home/index". Одна из версий конструктора Uri позволяет с помощью перечисления 
 UriKind  указать, какой именно адрес создается. UriKind может принимать три значения:

- `Absolute`  (абсолютный)
- `Relative`  (относительный)
- `RelativeOrAbsolute`  (абсолютный или относительный)

```csharp
Uri uri1 = new Uri("https://metanit.com", UriKind.Absolute);
Uri uri2 = new Uri("sharp/net", UriKind.Relative);
Uri uri3 = new Uri("https://metanit.com/sharp/net", UriKind.RelativeOrAbsolute);
```

Стоит отметь, что для относительных адресов могут быть недоступны некоторые свойства и методы класса Uri.

Вполне может быть, что в конструктор Uri будет передан некорректный адрес. При попытке использовать объект Uri, инициализированный некорректным адресом, мы столкнемся с исключением System.UriFormatException. 
И в этом случае мы можем проверять корректность абсолютного адреса с помощью метода статического метода  Uri.TryCreate() . Если создание uri прошло успешно, то метод возвращает  `true` t:

```csharp
string url = "yqz";

if (Uri.TryCreate(url, new UriCreationOptions(), out Uri? newUri))
{
    Console.WriteLine($"Uri создан: {newUri.OriginalString}");
}
else
	Console.WriteLine("Невозможно создать Uri. Некорректный адрес");
```

Первый параметр метода представляет строку адреса, второй - объект  `UriCreationOptions` , применяемый для создания адреса, и третий выходной параметр - создаваемый объект Uri.

### UriBuilder

Также для создания адреса можно использовать специальный класс-строитель  System.UriBuilder , который с помощью своих свойств позволяет задать отдельные аспекты Uri:

- Fragment : возвращает или задает фрагмент URI.
- Host : возвращает или задает имя хоста или IP-адрес сервера.
- Password : возвращает или задает пароль.
- Path : возвращает или задает путь к ресурсу, на который ссылается URI.
- Port : возвращает или задает номер порта URI.
- Query : возвращает или задает строку запроса.
- Scheme : возвращает или задает схему URI.
- UserName : возвращает или задает имя пользователя.
- Uri : возвращает созданный экземпляр Uri.

При необходимости все необходимые параметры Uri также можно задать через параметры конструктора UriBuilder. Одна из версий конструктора:

```csharp
public UriBuilder (string? scheme, string? host, int port, string? path, string? extraValue)
```

Примение класса:

```csharp
UriBuilder uriBuilder1 = new UriBuilder("https", "metanit.com", 443, "sharp/net");
Uri url1 = uriBuilder1.Uri;
Console.WriteLine(url1);    // https://metanit.com/sharp/net

UriBuilder uriBuilder2 = new UriBuilder();
uriBuilder2.Scheme = "https";
uriBuilder2.Host = "somesite.com";
uriBuilder2.Port = 80;
uriBuilder2.Path = "home";
uriBuilder2.Query = "name=Tom&age=38";
uriBuilder2.Fragment = "account-info";
Uri url2 = uriBuilder2.Uri;
Console.WriteLine(url2);    // https://somesite.com:80/home?name=Tom&age=38#account-info
```

**Источник:** [https://metanit.com/sharp/net/1.3.php](https://metanit.com/sharp/net/1.3.php)

[[Языки программирования/C#/Руководства/Сетевое программирование/Глава 1. Основы работы с сетями/Адреса в .NET|Назад]] | [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 1. Основы работы с сетями|Основы работы с сетями]] | [[Языки программирования/C#/Руководства/Сетевое программирование/Глава 1. Основы работы с сетями/DNS|Вперёд]]
