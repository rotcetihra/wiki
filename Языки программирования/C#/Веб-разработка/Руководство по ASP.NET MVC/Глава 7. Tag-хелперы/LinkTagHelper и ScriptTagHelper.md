# LinkTagHelper и ScriptTagHelper

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Веб-разработка|Веб-разработка]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC|Руководство по ASP.NET MVC]] / [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 7. Tag-хелперы|Глава 7. Tag-хелперы]] / LinkTagHelper и ScriptTagHelper

[[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 7. Tag-хелперы/AnchorTagHelper. Создание ссылок|Назад]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 7. Tag-хелперы|Содержание]] | [[Языки программирования/C#/Веб-разработка/Руководство по ASP.NET MVC/Глава 7. Tag-хелперы/Tag-хелперы форм|Вперёд]]

**Дата написания:** 05.09.2026

## LinkTagHelper и ScriptTagHelper

Последнее обновление: 03.04.2022




-

-

-














Для подключения файлов скриптов применяется тег-хэлпер ScriptTagHelper. Данный тег может принимать ряд следующих атрибутов:


-

asp-append-version: если имеет значение true, то к пути к файлу скрипта добавляется номер версии

-

asp-fallback-src: указывает вспомогательный путь к скрипту, который используется, если загрузка скрипта, указанного
в атрибуте `src` пройдет неудачно

-

asp-fallback-test: определяет выражение, которое тестирует загрузку основного скрипта из атрибута src

-

asp-src-include: определяет шаблон подключаемых файлов, через запятую можно задать несколько шаблонов

-

asp-src-exclude: определяет через запятую набор шаблонов для тех файлов, которые следует исключить из загрузки

-

asp-fallback-src-include: определяет через запятую набор шаблонов файлов, которые подключаются в том случае, если загрузка основного скрипта из атрибута src
прошла неудачно

-

asp-fallback-src-exclude: определяет через запятую набор шаблонов файлов, которые следует исключить из загрузки
в том случае, если загрузка основного скрипта из атрибута src прошла неудачно


Например, можно определить следующий тег:

```

<script src="https://ajax.aspnetcdn.com/ajax/jquery/jquery-2.2.0.min.js"
 asp-fallback-src="~/lib/jquery/dist/jquery.min.js"
 asp-fallback-test="window.jQuery"
 crossorigin="anonymous"
 integrity="sha384-K+ctZQ+LL8q6tP7I94W+qzQsfRV2a+AfHIi9k8z8l9ggpc8X+Ytst4yBo/hH+8Fk">
</script>

```


Данный элемент представляет не просто стандартный тег script, но и класс тег-хэлпера ScriptTagHelper. Атрибут src
указывает на скрипт, который мы хотим подключить. Логично подключать скрипты из CDN, чтобы сократить нагрузку на собственный сайт.
Но CDN может не работать, например, произойдет какой-то временный сбой, и чтобы определить, что скрипт загружен, применяется атрибут
asp-fallback-test. Он тестирует загрузку с помощью выражения `window.jQuery`. Если объект `window.jQuery` определен,
то загрузка скрипта прошла успешно. Если же нет, то загружается скрипт, который указан в атрибуте asp-fallback-src.


Рассмотрим другие атрибуты. Допустим, у нас в проекте в папке wwwroot/js определено четыре скрипта и подпапка util с двумя скриптами:
![scripttagbuilder и подключение скриптов javascript in ASP.NET Core MVC и C#](https://metanit.com./pics/7.4.png)


Убедимся, что в файле Program.cs подключено middleware для работы со статическими файлами:

```
app.UseStaticFiles();
```


Теперь подключим все скрипты в представлении:

```

<script asp-src-include="~/js/**/*.js"></script>

```


Атрибут `asp-src-include` принимает шаблон, который в данном случае показывает, что подключаться будут все скрипты в
папке js, а также во всех ее подпапках. Если бы нам надо было подключить скрипты непосредственно из каталога js без учета подкаталогов,
то мы могли бы использовать следующий шаблон: "~/js/*.js". В итоге вместо этого элемента на веб-странице будут подключены все скрипты:

```

<script src="/js/script1.js"></script>
<script src="/js/script2.js"></script>
<script src="/js/script3.js"></script>
<script src="/js/site.js"></script>
<script src="/js/util/utilscript1.js"></script>
<script src="/js/util/utilscript2.js"></script>

```


Теперь изменим задачу. Допустим, нам надо подключить все скрипты из папки js и всех ее подпапок, кроме подпапки util:

```

<script asp-src-include="~/js/**/*.js" asp-src-exclude="~/js/util/**/*.js"></script>

```


Шаблон в атрибуте `asp-src-exclude` предотвращает подключение скриптов из папки js/util и всех ее подпапок.


#### Определение шаблона


Для создания шаблона мы можем применять следующие символы подстановки:


-

?: заменяет любой одиночный символ за исключением слеша.


Например выражение `js/script?.js` будет соответствовать таким файлам как `js/script1.js` или `js/scriptX.js`,
но не `js/script35.js`

-

*: заменяет любое количество символов за исключением слеша.


Например выражение `js/*.js` будет соответствовать таким файлам как `js/script.js` или `js/scriptX25.js`,
но не `js/bootstrap/script.js`

-

**: заменяет любое количество символов, в том числе и слеш.


Например выражение `js/**/script.js` будет соответствовать таким файлам как `js/script.js` или `js/bootstrap/script.js`,
но не `js/script35.js`


### LinkTagHelper


Класс LinkTagHelper определяет тег `link`, который используется для подключения файлов стилей. Он применяет следующие атрибуты:


-

asp-append-version: если имеет значение true, то к пути к названию файла стиля добавляется номер версии

-

asp-fallback-href: указывает вспомогательный путь к файлу стиля, который используется, если загрузка
файла, указанного в атрибуте `href` пройдет неудачно

-

asp-fallback-test-class: определяет класс, который используется для теста загрузки стиля из атрибута href

-

asp-fallback-test-property: определяет свойство, которое используется для тестирования загрузки стиля из атрибута href

-

asp-fallback-test-value: определяет значение свойства из атрибута asp-fallback-test-property, которое используется для теста загрузки стиля из атрибута href

-

asp-href-include: определяет через запятую набор шаблонов подключаемых файлов стилей

-

asp-href-exclude: определяет через запятую набор шаблонов для тех файлов, которые следует исключить из загрузки

-

asp-fallback-href-include: определяет через запятую набор шаблонов файлов, которые подключаются в том случае, если загрузка основного файла стиля из атрибута href
прошла неудачно

-

asp-fallback-href-exclude: определяет через запятую набор шаблонов файлов, которые следует исключить из загрузки
в том случае, если загрузка основного файла стиля из атрибута href прошла неудачно


Например, подключим библиотеку bootstrap:

```

<link rel="stylesheet" href="https://ajax.aspnetcdn.com/ajax/bootstrap/4.3.0/css/bootstrap.min.css"
 asp-fallback-href="~/lib/bootstrap/dist/css/bootstrap.min.css"
 asp-fallback-test-class="hidden" asp-fallback-test-property="visibility" asp-fallback-test-value="hidden" />

```


Здесь атрибут `href` указывает на файл стилей фреймворка bootstrap, который располагается в CDN. Если веб-браузер не сможет загрузить данный файл,
то загружается локальный файл стилей, путь к которому указан в атрибуте `asp-fallback-href`. Чтобы протестировать, что
файл стилей из атрибута `href` нормально загрузился, используются атрибуты `asp-fallback-test-class`,
`asp-fallback-test-property` и `asp-fallback-test-value`.


В конечном счете этот элемент будет генерировать следующий код, который будет включен на веб-страницу:

```

<link rel="stylesheet" href="https://ajax.aspnetcdn.com/ajax/bootstrap/3.0.0/css/bootstrap.min.css" />
<meta name="x-stylesheet-fallback-test" class="hidden" />
<script>!function(a,b,c){var d,e=document,f=e.getElementsByTagName("SCRIPT"),g=f[f.length-1].previousElementSibling,h=e.defaultView&&e.defaultView.getComputedStyle?e.defaultView.getComputedStyle(g):g.currentStyle;if(h&&h[a]!==b)for(d=0;d<c.length;d++)e.write('<link rel="stylesheet" href="'+c[d]+'"/>')}("visibility","hidden",["\/lib\/bootstrap\/dist\/css\/bootstrap.min.css"]);</script>

```


Для подключения множества файлов стилей из определенного каталога мы можем использовать атрибут `asp-href-include`:

```

<link asp-href-include="~/css/**/*.css" />

```


В данном случае подключаются все файлы css из каталога wwwroot/css и всех его подкаталогов:
![Класс LinkTagHelper и подключение стилей css в ASP.NET Core MVC и C#](https://metanit.com./pics/7.5.png)


Если нам надо исключить какие-то файлы, то мы можем использовать атрибут `asp-href-exclude`:

```

<link asp-href-include="~/css/**/*.css" asp-href-exclude="~/css/mystyles/**/*.css" />

```


Здесь предотвращается подключение стилей из папки wwwroot/css/mystyles.


### Cache busting


При работе со статическими файлами, в частности, со стилями css и скриптами js мы можем столкнуться со следующей проблемой. Допустим, у нас есть
файл стиля styles.css. Для увеличения производительности подобные статические файлы часто кэшируются на стороне клиента. А это значит,
что браузеру достаточно один раз за определенный период получить файл и затем при обращении к сайту он будет брать этот файл из кэша. Однако если мы внесем
в файл styles.css какие-то изменения, то браузер по прежнему будет брать данный файл из кэша и будет использовать старые данные, пока не закончится период кэширования.


Для решения этой проблемы мы можем использовать в ScriptTagHelper и LinkTagHelper параметр asp-append-version:

```

<link rel="stylesheet" href="~/css/site.css" asp-append-version="true" />

```


После обработки запроса будет сгенерирован элемент наподобие следующего:

```
<link rel="stylesheet" href="/css/site.css?v=1wp5zz4e-mOPFx4X2O8seW_DmUtePn5xFJk1vB7JKRc">
```


К пути к файлу после его имени добавляется параметр `?v=`, который указывает на версию файла. Если мы внесем изменения в файл, версия изменится.
Соответственно даже если файл и был закэширован ранее в браузере, то смена версии позволит использовать уже новую версию файла.











- Глава 1. Введение в ASP.NET Core MVC


 - [Фреймворк ASP.NET Core MVC](//metanit.com/sharp/aspnetmvc/1.1.php)

 - [Первый проект на ASP.NET Core MVC с .NET CLI](//metanit.com/sharp/aspnetmvc/1.4.php)

 - [Первый проект на ASP.NET Core MVC в Visual Studio](//metanit.com/sharp/aspnetmvc/1.2.php)

 - [Добавление MVC в пустой проект](//metanit.com/sharp/aspnetmvc/1.3.php)



- Глава 2. Контроллеры


 - [Контроллеры и их действия](//metanit.com/sharp/aspnetmvc/2.1.php)

 - [Контекст контроллера](//metanit.com/sharp/aspnetmvc/2.2.php)

 - [Передача данных в контроллер через строку запроса](//metanit.com/sharp/aspnetmvc/2.3.php)

 - [Передача данных в контроллер через формы](//metanit.com/sharp/aspnetmvc/2.4.php)

 - [Результаты действий](//metanit.com/sharp/aspnetmvc/2.5.php)

 - [ContentResult и JsonResult](//metanit.com/sharp/aspnetmvc/2.6.php)

 - [Переадресация](//metanit.com/sharp/aspnetmvc/2.7.php)

 - [Отправка статусных кодов](//metanit.com/sharp/aspnetmvc/2.8.php)

 - [Отправка файлов](//metanit.com/sharp/aspnetmvc/2.9.php)

 - [Передача зависимостей в контроллер](//metanit.com/sharp/aspnetmvc/2.10.php)

 - [Переопределение контроллеров](//metanit.com/sharp/aspnetmvc/2.11.php)



- Глава 3. Представления


 - [Введение в представления](//metanit.com/sharp/aspnetmvc/3.1.php)

 - [Движок представлений Razor](//metanit.com/sharp/aspnetmvc/3.2.php)

 - [Передача данных в представление](//metanit.com/sharp/aspnetmvc/3.3.php)

 - [Мастер-страницы](//metanit.com/sharp/aspnetmvc/3.4.php)

 - [Файл _ViewImports.cshtml](//metanit.com/sharp/aspnetmvc/3.5.php)

 - [Частичные представления](//metanit.com/sharp/aspnetmvc/3.6.php)

 - [Внедрение зависимостей в представления](//metanit.com/sharp/aspnetmvc/3.7.php)

 - [Работа с формами](//metanit.com/sharp/aspnetmvc/3.8.php)

 - [Создание движка представлений](//metanit.com/sharp/aspnetmvc/3.9.php)



- Глава 4. Маршрутизация


 - [Добавление маршрутизации](//metanit.com/sharp/aspnetmvc/4.1.php)

 - [Определение маршрутов](//metanit.com/sharp/aspnetmvc/4.2.php)

 - [Атрибуты маршрутизации](//metanit.com/sharp/aspnetmvc/4.3.php)

 - [Области](//metanit.com/sharp/aspnetmvc/4.4.php)



- Глава 5. Модели


 - [Модели в ASP.NET Core MVC](//metanit.com/sharp/aspnetmvc/5.1.php)

 - [Введение в определение и применение моделей](//metanit.com/sharp/aspnetmvc/5.2.php)

 - [Привязка модели](//metanit.com/sharp/aspnetmvc/5.3.php)

 - [Управление привязкой](//metanit.com/sharp/aspnetmvc/5.4.php)

 - [Создание привязчика модели](//metanit.com/sharp/aspnetmvc/5.5.php)



- Глава 6. HTML-хелперы


 - [Создание HTML-хелперов](//metanit.com/sharp/aspnetmvc/6.1.php)

 - [HTML-хелперы элементов форм](//metanit.com/sharp/aspnetmvc/6.2.php)

 - [Строго типизированные хелперы](//metanit.com/sharp/aspnetmvc/6.3.php)

 - [Шаблонные хелперы](//metanit.com/sharp/aspnetmvc/6.4.php)

 - [Генерация ссылок](//metanit.com/sharp/aspnetmvc/6.5.php)

 - [URL-хелперы](//metanit.com/sharp/aspnetmvc/6.6.php)



- Глава 7. Tag-хелперы


 - [Введение в tag-хелперы](//metanit.com/sharp/aspnetmvc/7.1.php)

 - [AnchorTagHelper. Создание ссылок](//metanit.com/sharp/aspnetmvc/7.2.php)

 - [LinkTagHelper и ScriptTagHelper](//metanit.com/sharp/aspnetmvc/7.3.php)

 - [Tag-хелперы форм](//metanit.com/sharp/aspnetmvc/7.4.php)

 - [EnvironmentTagHelper](//metanit.com/sharp/aspnetmvc/7.5.php)

 - [CacheTagHelper](//metanit.com/sharp/aspnetmvc/7.6.php)

 - [Создание tag-хелперов](//metanit.com/sharp/aspnetmvc/7.7.php)

 - [Управление выводом tag-хелпера](//metanit.com/sharp/aspnetmvc/7.8.php)

 - [Контекст хелпера и получение зависимостей](//metanit.com/sharp/aspnetmvc/7.9.php)

 - [Атрибут HtmlTargetElement](//metanit.com/sharp/aspnetmvc/7.10.php)

 - [Tag-хелперы и сложные объекты и коллекции](//metanit.com/sharp/aspnetmvc/7.11.php)



- Глава 8. View Component


 - [Определение компонента представлений](//metanit.com/sharp/aspnetmvc/8.1.php)

 - [Передача данных в View Component](//metanit.com/sharp/aspnetmvc/8.2.php)

 - [Генерация контента в View Component](//metanit.com/sharp/aspnetmvc/8.3.php)

 - [ViewComponentResult и представления](//metanit.com/sharp/aspnetmvc/8.4.php)

 - [ViewComponentContext](//metanit.com/sharp/aspnetmvc/8.5.php)



- Глава 9. Метаданные и валидация модели


 - [Валидация модели на стороне сервера](//metanit.com/sharp/aspnetmvc/9.1.php)

 - [Валидация на стороне клиента](//metanit.com/sharp/aspnetmvc/9.2.php)

 - [Атрибуты валидации](//metanit.com/sharp/aspnetmvc/9.3.php)

 - [Tag-хелперы валидации и стилизация ошибок](//metanit.com/sharp/aspnetmvc/9.4.php)

 - [Создание атрибута валидации. Самовалидация модели](//metanit.com/sharp/aspnetmvc/9.5.php)

 - [Аннотации данных](//metanit.com/sharp/aspnetmvc/9.6.php)



- Глава 10. Фильтры


 - [Введение в фильтры](//metanit.com/sharp/aspnetmvc/10.1.php)

 - [Область действия фильтров](//metanit.com/sharp/aspnetmvc/10.2.php)

 - [Передача параметров в фильтры и установка зависимостей](//metanit.com/sharp/aspnetmvc/10.3.php)

 - [Фильтры ресурсов](//metanit.com/sharp/aspnetmvc/10.4.php)

 - [Фильтры действий](//metanit.com/sharp/aspnetmvc/10.5.php)

 - [Фильтры результатов](//metanit.com/sharp/aspnetmvc/10.6.php)

 - [Фильтры исключений](//metanit.com/sharp/aspnetmvc/10.7.php)



- Глава 11. Работа с данными в Entity Framework


 - [Подключение Entity Framework Core](//metanit.com/sharp/aspnetmvc/11.1.php)

 - [Добавление и вывод данных](//metanit.com/sharp/aspnetmvc/11.2.php)

 - [Редактирование и удаление данных](//metanit.com/sharp/aspnetmvc/11.3.php)

 - [Сортировка](//metanit.com/sharp/aspnetmvc/11.4.php)

 - [Создание tag-хелпера сортировки](//metanit.com/sharp/aspnetmvc/11.5.php)

 - [Фильтрация](//metanit.com/sharp/aspnetmvc/11.6.php)

 - [Постраничная навигация](//metanit.com/sharp/aspnetmvc/11.7.php)

 - [Tag-хелпер для постраничной навигации](//metanit.com/sharp/aspnetmvc/11.8.php)

 - [Объединение сортировки, фильтрации и пагинации](//metanit.com/sharp/aspnetmvc/11.9.php)

 - [Tag-хелпер пагинации с сортировкой и фильтрацией](//metanit.com/sharp/aspnetmvc/11.10.php)










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

**Источник:** [https://metanit.com/sharp/aspnetmvc/7.3.php](https://metanit.com/sharp/aspnetmvc/7.3.php)
