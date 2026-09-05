[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Графические программы|Графические программы]] / [[Языки программирования/C#/Графические программы/Xamarin Forms|Xamarin Forms]] / [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 5. Платформо-зависимый код|Глава 5. Платформо-зависимый код]] / DependencyService

[[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 5. Платформо-зависимый код/Платформозависимость в XAML|Назад]] | [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 5. Платформо-зависимый код|Содержание]]

**Дата написания:** 05.09.2026

Последнее обновление: 11.01.2021
	
	
	
	- 

	- 

	- 

	
	
	
	

	
		
		
		
	

	
Механизм DependencyService представляет еще один способ использования платформо-зависимых 
вызовов в кроссплатформенном приложении на Xamarin Forms. Иногда нам приходится задействовать те классы, которые доступны для определенной платформы. И в этом 
случае мы можем определить набор методов, реализация которых будет различаться на разных платформах. А затем с помощью DependencyService применить эти методы в 
Portable-проекте.

Чтобы начать использовать DependencyService, нам надо определить интерфейс в главном проекте. Этот интерфейс будет определять сигнатуру методов, 
реализация которых будет зависеть от конкретной платформы. К примеру, нам надо вывести номер версии операционной системы. Для этого добавим в главный проект 
новый файл IDeviceInfo.cs и определим в нем следующий код:

```

public interface IDeviceInfo
{
    string GetInfo();
}

```

А в коде C# страницы MainPage используем данный интерфейс:

```

using Xamarin.Forms;

namespace HelloApp
{
    public class MainPage : ContentPage
    {
        public MainPage()
        {
            IDeviceInfo deviceInfo = DependencyService.Get();

            Label infoLabel = new Label();
            infoLabel.Text = deviceInfo.GetInfo();
			infoLabel.FontSize = Device.GetNamedSize(NamedSize.Large, typeof(Label));

            Content = new StackLayout
            {
                Children = { infoLabel}
            };
        }
    }
}

```

Для получения информации об устройстве здесь используется вызов:

```
IDeviceInfo deviceInfo = DependencyService.Get();
```

Здесь с помощью метода `Get()` мы получаем объект IDeviceInfo. При этом не важно, что в Portable-проекте нет конкретной реализации данного интерфейса. В качестве 
реализации будет использоваться объект класса, который будет определен в проекте для текущей платформы.

Но естественно, если мы сейчас запустим проект, то получим ошибку.

И теперь в каждом проекте для конкретной ОС нам надо определить реализацию этого интерфейса. Так, добавим в проект для Android новый класс 
DeviceInfo:

```

using Android.OS;
using Xamarin.Forms;

[assembly: Dependency(typeof(HelloApp.Droid.DeviceInfo))]
namespace HelloApp.Droid
{
    public class DeviceInfo : IDeviceInfo
    {
        public string GetInfo()
        {
            return $"Android {Build.VERSION.Release}";
        }
    }
}

```

Для получения версии системы здесь применяется класс `Android.OS.Build`, который доступен нам только на Android.

Кроме того, над пространством имен нам надо указать специальный атрибут:

```
[assembly: Dependency(typeof(HelloApp.Droid.DeviceInfo))]
```

Данный атрибут представлен встроенным классом DependencyAttribute из пространства имен `Xamarin.Forms`. 
Он используется в связке с классом DependencyService. В качестве параметра в конструктор атрибута передается тип объекта, который будет доступен для доступа 
из главного проекта, то есть класс DeviceInfo в нашем случае.

Подобным образом добавим новый класс DeviceInfo в проект для iOS:

```

using UIKit;
using Xamarin.Forms;

[assembly: Dependency(typeof(HelloApp.iOS.DeviceInfo))]
namespace HelloApp.iOS
{
    public class DeviceInfo : IDeviceInfo
    {
        public string GetInfo()
        {
			UIDevice device = new UIDevice();
            return $"{device.SystemName} {device.SystemVersion}";
        }
    }
}

```

Во многом аналогичный класс, как и на Android, только теперь для получения информации об устройстве применяется класс `UIKit.UIDevice`, который 
доступен только для iOS.

И далее в проект для UWP добавим также новый класс DeviceInfo:

```

using Windows.Security.ExchangeActiveSyncProvisioning;
using Windows.System.Profile;
using Xamarin.Forms;

[assembly: Dependency(typeof(HelloApp.UWP.DeviceInfo))]
namespace HelloApp.UWP
{
    public class DeviceInfo : IDeviceInfo
    {
        public string GetInfo()
        {
            EasClientDeviceInformation devInfo = new EasClientDeviceInformation();

            var deviceFamilyVersion = AnalyticsInfo.VersionInfo.DeviceFamilyVersion;
            var version = ulong.Parse(deviceFamilyVersion);
            var majorVersion = (version & 0xFFFF000000000000L) >> 48;
            var minorVersion = (version & 0x0000FFFF00000000L) >> 32;
            var buildVersion = (version & 0x00000000FFFF0000L) >> 16;
            var revisionVersion = (version & 0x000000000000FFFFL);
            var systemVersion = $"{majorVersion}.{minorVersion}.{buildVersion}.{revisionVersion}";

            return $"{devInfo.OperatingSystem} {systemVersion}";
        }
    }
}

```

Для получения полной версии сборки системы здесь применяются более сложные преобразования и совсем другие классы.

Таким образом, чтобы получить элементарную информацию об системе, мы вынуждены применять разные классы на разных платформах. Однако DependencyService позволяет 
с помощью интерфейса IDeviceInfo привести все эти классы общему знаменателю.

И после определения всех классов мы можем запустить проект, и для разных платформ мы получим разные результаты. Например, для Android:

А для проекта UWP будут другие значения:

---

**Источник:** [https://metanit.com/sharp/xamarin/12.3.php](https://metanit.com/sharp/xamarin/12.3.php)

[[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 5. Платформо-зависимый код/Платформозависимость в XAML|Назад]] | [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 5. Платформо-зависимый код|Содержание]]
