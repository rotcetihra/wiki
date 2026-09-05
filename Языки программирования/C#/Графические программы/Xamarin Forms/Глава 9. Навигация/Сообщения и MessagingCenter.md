[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Графические программы|Графические программы]] / [[Языки программирования/C#/Графические программы/Xamarin Forms|Xamarin Forms]] / [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 9. Навигация|Глава 9. Навигация]] / Сообщения и MessagingCenter

[[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 9. Навигация/Передача данных при навигации|Назад]] | [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 9. Навигация|Содержание]]

**Дата написания:** 05.09.2026

Последнее обновление: 13.01.2021
	
	
	
	- 

	- 

	- 

	
	
	
	

	
		
		
		
	

	
Xamarin Forms поддерживает такую функциональность, как отправку сообщений. Для этого в Xamarin определен класс 
MessagingCenter, который поддерживает ряд методов:

- Send<TSender>(TSender sender, string message): посылает сообщение message, в качестве отправителя выступает объект TSender

- Subscribe<TSender>(object subscriber, string message, Action<TSender> callback): 
устанавливает подписку для объекта subscriber на получение сообщения message. При получении события будет вызываться действие callback

- Unsubscribe<TSender>(object subscriber, string message): прекращает подписку для объекта subscriber на сообщение message

MessagingCenter работает по принципу подписки или Publisher-Subscriber:

Рассмотрим применение сообщений на примере. Добавим в проект класс страницы, который назовем MessagePage:

```

using System;
using Xamarin.Forms;

namespace HelloApp
{
    public class MessagePage : ContentPage
    {
        public MessagePage()
        {
            Title = "MessagePage";
            Button backBtn = new Button
            {
                Text = "Назад"
            };
            backBtn.Clicked += GoToBack;

            Content = new StackLayout { Children = { backBtn} };
        }
        // Переход обратно на MainPage
        private async void GoToBack(object sender, EventArgs e)
        {
            // отправляем сообщение
            MessagingCenter.Send
(this, "LabelChange");
            await Navigation.PopAsync();
        }
    }
}

```

Здесь определена одна кнопка для возврата на предыдущую страницу. При возврате с помощью метода `MessagingCenter.Send` отправляется сообщение. 
Название сообщения - "LabelChange". В качестве отправителя установлен текущий объект, поэтому метод типизирован типом `Page`. Хотя можно было бы и конкретизировать 
тип отправителя:

```

MessagingCenter.Send(this, "LabelChange");

```

Таким образом, сообщение отправляется. Теперь подпишемся на это событие. Пусть у нас есть главная страница MainPage:

```

using System;
using Xamarin.Forms;

namespace HelloApp
{
    public partial class MainPage : ContentPage
    {
        Label stackLabel;
        public MainPage()
        {
            Title = "Main Page";
            Button forwardButton = new Button
            {
                Text = "Вперед"
            };
            forwardButton.Clicked += GoToForward;

            stackLabel = new Label
            {
                FontSize = Device.GetNamedSize(NamedSize.Large, typeof(Label))
            };
            Content = new StackLayout { Children = { forwardButton, stackLabel } };
            // устанавливаем подписку на сообщения
            Subscribe();
        }
		// установка подписки на сообщения
        private void Subscribe()
        {
            MessagingCenter.Subscribe
(
                this, // кто подписывается на сообщения
                "LabelChange",   // название сообщения
                (sender)=> { stackLabel.Text = "Получено сообщение"; });    // вызываемое действие

        }
        // Переход вперед на MessagePage
        private async void GoToForward(object sender, EventArgs e)
        {
            MessagePage page = new MessagePage();
            await Navigation.PushAsync(page);
        }
    }
}

```

Здесь определена кнопка для перехода к странице MessagePage, и также определен метод подписки на сообщение, в котором вызывается 
`MessagingCenter.Subscribe`. Причем метод MessagingCenter.Subscribe типизирован именно тем типом, который является отправителем, то есть тип Page.

Получателем является текущий объект, поэтому в метод передается в качестве первого параметра this.

Название сообщения должно совпадать с тем, которое используется при отправке, то есть в нашем случае "LabelChange".

Третий параметр - действие просто выполняет установку текста метки, хотя тут могла бы быть и более сложная логика.

Ну и в главном классе приложения App страница MainPage должна передаваться в NavigationPage:

```

using Xamarin.Forms;

namespace HelloApp
{
    public partial class App : Application
    {
        public App()
        {
            MainPage = new NavigationPage(new MainPage());
        } 

        protected override void OnStart()
        {}

        protected override void OnSleep()
        {}

        protected override void OnResume()
        {}
    }
}

```

Теперь запустим приложение и перейдем с MainPage на MessagePage и обратно:

---

**Источник:** [https://metanit.com/sharp/xamarin/5.4.php](https://metanit.com/sharp/xamarin/5.4.php)

[[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 9. Навигация/Передача данных при навигации|Назад]] | [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 9. Навигация|Содержание]]
