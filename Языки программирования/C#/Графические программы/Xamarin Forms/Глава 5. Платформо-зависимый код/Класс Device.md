[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Графические программы|Графические программы]] / [[Языки программирования/C#/Графические программы/Xamarin Forms|Xamarin Forms]] / [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 5. Платформо-зависимый код|Глава 5. Платформо-зависимый код]] / Класс Device

[[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 5. Платформо-зависимый код|Содержание]] | [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 5. Платформо-зависимый код/Платформозависимость в XAML|Вперёд]]

**Дата написания:** 05.09.2026

## Класс Device
Последнее обновление: 11.01.2021
	
	
	
	- 

	- 

	- 

	
	
	
	

	
		
		
		
	

	
Несмотря на то, что проект Xamarin Forms позволяет обеспечить единую логику приложения и единый графический интерфейс, иногда возникает необходимость 
подстроить некоторые аспекты под конкретную операционную систему. Одним из механизмов, который позволяет это сделать, представляет класс Device.

### Свойство RuntimePlatform

Прежде всего, свойство RuntimePlatform класса Device позволяет получить платформу, на которой запущено приложение. 
В качестве значения свойство хранит название платформы. В частности, это может быть одна из встроенных констант класса Device:

- `Device.Android`

- `Device.iOS`

- `Device.UWP`

- `Device.WPF`

- `Device.Tizen`

- `Device.GTK`

- `Device.macOS`

Например, определим в коде метку, текст которой зависит от текущей пдатформы:

```

Label appLabel = new Label { HorizontalTextAlignment = TextAlignment.Center};
switch (Device.RuntimePlatform)
{
	case Device.Android:
		appLabel.Text = "Android";
		break;
	case Device.iOS:
		appLabel.Text = "iOS";
		break;
	case Device.UWP:
		appLabel.Text = "UWP";
		break;
	case Device.WPF:
		appLabel.Text = "WPF";
		break;
	case Device.GTK:
		appLabel.Text = "GTK";
		break;
	default:
		appLabel.Text = "Undefined";
		break;
}

```

### Свойство Idiom

Свойство Idiom класса Device позволяет проверить тип устройства. В качестве значения оно принимает 
одно из значений перечисления TargetIdiom:

- `TargetIdiom.Phone`: устройства iPhone, iPod и Android с шириной менее 600 dip

- `TargetIdiom.Tablet`: устройства iPad, Windows и Android с шириной более 600 dip

- `TargetIdiom.Desktop`: настольные компьютеры

- `TargetIdiom.TV`: телевизоры на платформе Tizen

- `TargetIdiom.Watch`: часы на платформе Tizen

- `TargetIdiom.Unsupported`: не поддерживается

В зависимости от результатов проверки значения свойства можно выполнить тот или иной набор инструкций:

```

if(Device.Idiom == TargetIdiom.Phone)
{
	// код для смартфонов
}
else if (Device.Idiom == TargetIdiom.Tablet)
{
	// код для планшетов
}
else if (Device.Idiom == TargetIdiom.Desktop)
{
	// код для настольных компьютеров
}

```

---

**Источник:** [https://metanit.com/sharp/xamarin/12.1.php](https://metanit.com/sharp/xamarin/12.1.php)

[[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 5. Платформо-зависимый код|Содержание]] | [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 5. Платформо-зависимый код/Платформозависимость в XAML|Вперёд]]
