https://sass-lang.com/documentation/modules/string/

# sass:string — Профессиональная обработка текста в Sass

Модуль `sass:string` предоставляет набор инструментов для манипуляции текстовыми данными. В CSS строки часто используются для путей к ресурсам, имен шрифтов, контента псевдоэлементов и селекторов. Использование встроенных функций позволяет автоматизировать создание этих строк, менять их регистр или динамически генерировать уникальные идентификаторы.

Для активации модуля используйте:

```SCSS
@use "sass:string";
```

---

## 1. Особенности индексации в Sass

Это самый важный технический аспект работы со строками в Sass, который часто сбивает с толку разработчиков, привыкших к JavaScript или Python:

1. **Индексация с единицы:** Первый символ строки имеет индекс `1`.
    
2. **Отрицательные индексы:** Позволяют отсчитывать символы с конца строки. Индекс `-1` — это последний символ, `-2` — предпоследний и так далее.

---

## 2. Поиск и извлечение данных

### string.length($string)

Возвращает количество символов в строке (включая пробелы и спецсимволы).

```SCSS
@debug string.length("Helvetica Neue"); // 14
```

### string.index($string, $substring)

Возвращает индекс первого вхождения `$substring` в `$string`. Если подстрока не найдена, возвращается `null`.

```SCSS
@debug string.index("Helvetica Neue", "Neue"); // 11
@debug string.index("Roboto", "Arial");         // null
```

### string.slice($string, $start-at, $end-at: -1)

Извлекает часть строки, начиная с индекса `$start-at` и заканчивая `$end-at` (включительно).

```SCSS
$font: "Roboto Mono";
@debug string.slice($font, 1, 6);  // "Roboto"
@debug string.slice($font, -4);    // "Mono" (от -4 до конца)
```

---

## 3. Модификация текста

### string.insert($string, $insert, $index)

Вставляет строку `$insert` в исходную строку `$string` на позицию `$index`.

```SCSS
@debug string.insert("Roboto", " Mono", 7); // "Roboto Mono"
@debug string.insert("Terminal", "!", -1);  // "Termina!l" (вставка ПЕРЕД последним символом)
```

### string.to-upper-case() и string.to-lower-case()

Меняют регистр всех символов в строке. Это полезно для нормализации значений, приходящих из внешних конфигураций.

```SCSS
@debug string.to-upper-case("bold"); // "BOLD"
@debug string.to-lower-case("ARIAL"); // "arial"
```

---

## 4. Работа с кавычками

Sass различает два типа строк: **quoted** (в кавычках) и **unquoted** (без кавычек, как обычные CSS-значения).

### string.quote($string)

Принудительно добавляет кавычки к строке.

```SCSS
@debug string.quote(Helvetica); // "Helvetica"
```

### string.unquote($string)

Удаляет кавычки. Это критически важно для передачи значений в CSS-свойства, которые не принимают кавычки (например, имена анимаций или типы начертания).

```SCSS
.element {
  font-family: string.unquote("Arial"); // font-family: Arial;
}
```

---

## 5. Генерация уникальных ID

### string.unique-id()

Генерирует случайную, уникальную для текущей сессии компиляции строку без кавычек. Она гарантированно будет уникальной в рамках одного прохода компилятора.

**Зачем это нужно?**

- Создание уникальных имен для анимаций (`@keyframes`), чтобы избежать конфликтов при объединении нескольких CSS-файлов.
    
- Генерация временных имен классов.

```SCSS
$id: string.unique-id();

@keyframes slide-#{$id} {
  from { opacity: 0; }
  to { opacity: 1; }
}

.modal {
  animation: slide-#{$id} 0.3s;
}
```

---

## Практический пример: Обработка путей к ассетам

С помощью `string.index` можно создать миксин, который автоматически определяет расширение файла и добавляет нужные параметры:

```SCSS
@use "sass:string";

@mixin smart-background($path) {
  background-image: url($path);
  
  // Проверяем, является ли файл вектором
  @if string.index($path, ".svg") {
    background-size: contain;
    background-repeat: no-repeat;
  }
}

.logo {
  @include smart-background("assets/logo.svg");
}
```

### Итог

Модуль `sass:string` превращает Sass в мощный текстовый процессор. Основное внимание стоит уделять **1-based индексации** и правильному использованию **unquote**, чтобы итоговый CSS оставался валидным и чистым.
