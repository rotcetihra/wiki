https://sass-lang.com/documentation/modules/selector/

# sass:selector — Глубокая манипуляция CSS-селекторами

Модуль `sass:selector` предоставляет уникальный набор инструментов для анализа и изменения селекторов прямо во время компиляции. Это особенно полезно при создании сложных библиотек компонентов или систем, где нужно динамически изменять специфичность, объединять селекторы или проверять их иерархию.

Для работы с модулем подключите его:

```SCSS
@use "sass:selector";
```

---

## 1. Логический анализ селекторов

Функции анализа позволяют сравнивать селекторы и определять их взаимоотношения без необходимости рендеринга CSS.

### selector.is-superselector($super, $sub)

Возвращает `true`, если селектор `$super` охватывает все элементы, которые выбирает `$sub`.

- `div` является суперселектором для `div.active`.
    
- `.btn` не является суперселектором для `.container`, так как они выбирают разные элементы.

```SCSS
@debug selector.is-superselector("div", "div.active"); // true
@debug selector.is-superselector(".btn", ".btn-primary"); // true
@debug selector.is-superselector(".a", ".b"); // false
```

### selector.unify($selector1, $selector2)

Находит «пересечение» двух селекторов. Она возвращает селектор, который выбирает только те элементы, которые подходят под оба условия одновременно. Если объединение невозможно (например, `div` и `span`), возвращает `null`.

```SCSS
@debug selector.unify(".btn", ".active"); // .btn.active
@debug selector.unify("div", "span");      // null
@debug selector.unify("input", "[type=text]"); // input[type=text]
```

---

## 2. Разбор и деконструкция

Иногда нужно «разобрать» сложный селектор на составляющие, чтобы изменить его часть.

### selector.simple-selectors($selector)

Разбивает **составной** селектор (compound selector) на список индивидуальных простых селекторов.

- **Важно:** работает только с составными селекторами (без пробелов и комбинаторов типа `>`).

```SCSS
@debug selector.simple-selectors("div.active:hover"); // ("div", ".active", ":hover")
```

### selector.parse($selector)

Преобразует строку в структуру данных, которую понимает Sass (список списков). Это позволяет программно обрабатывать сложные цепочки селекторов.

---

## 3. Манипуляция и модификация

### selector.append($selector, $suffixes...)

Добавляет суффиксы к **последнему** составному селектору в цепочке.

```SCSS
@debug selector.append(".user", "-active"); // .user-active
@debug selector.append(".card .title", ":hover"); // .card .title:hover
```

### selector.nest($selectors...)

Имитирует стандартное вложение Sass (nesting), объединяя несколько селекторов в одну иерархическую цепочку.

```SCSS
@debug selector.nest(".card", "&:hover", ".title"); 
// .card:hover .title
```

### selector.replace($selector, $pattern, $replacement)

Ищет `$pattern` внутри `$selector` и заменяет его на `$replacement`. Это мощный способ переписать контекст селектора.

```SCSS
$sel: ".admin-panel .button";
// Заменим .admin-panel на .user-panel
@debug selector.replace($sel, ".admin-panel", ".user-panel"); 
// .user-panel .button
```

---

## 4. Имитация наследования: `selector.extend`

Функция `selector.extend($selector, $extender, $target)` работает аналогично директиве `@extend`, но возвращает результат в виде строки. Она говорит: «Верни мне селектор `$selector`, но сделай так, будто элементы, подходящие под `$extender`, теперь также ведут себя как `$target`».

```SCSS
@debug selector.extend(".error", ".error", ".message"); 
// .error, .message
```

---

## Практический пример: Миксин для предотвращения конфликтов

С помощью `selector.unify` можно создать миксин, который проверяет, не пытаемся ли мы применить несовместимые стили.

```SCSS
@use "sass:selector";

@mixin combine-with($other-selector) {
  $unified: selector.unify(&, $other-selector);
  
  @if $unified {
    @at-root #{$unified} {
      @content;
    }
  } @else {
    @warn "Селектор #{&} не может быть объединен с #{$other-selector}";
  }
}

.icon {
  @include combine-with(".active") {
    color: red; // Сгенерирует .icon.active
  }
}
```

### Итог

Модуль `sass:selector` незаменим при создании:

- **Динамических тем:** когда нужно заменить базовый класс-контейнер во всей библиотеке.
    
- **Валидаторов:** для проверки корректности вложенности селекторов.
    
- **Сложных БЭМ-генераторов:** для автоматической сборки имен классов.
    

Работа с селекторами как с объектами данных позволяет избежать «грязных» манипуляций со строками и гарантирует, что итоговый CSS будет валидным.
