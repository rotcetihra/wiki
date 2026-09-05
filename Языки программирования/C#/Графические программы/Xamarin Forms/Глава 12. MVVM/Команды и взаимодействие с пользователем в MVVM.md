[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Графические программы|Графические программы]] / [[Языки программирования/C#/Графические программы/Xamarin Forms|Xamarin Forms]] / [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 12. MVVM|Глава 12. MVVM]] / Команды и взаимодействие с пользователем в MVVM

[[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 12. MVVM/Паттерн Model-View-ViewModel|Назад]] | [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 12. MVVM|Содержание]] | [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 12. MVVM/Пример MVVM|Вперёд]]

**Дата написания:** 05.09.2026

Последнее обновление: 13.01.2021
	
	
	
	- 

	- 

	- 

	
	
	
	

	
		
		
		
	

	
В прошлой теме описывался паттерн MVVM, позволяющий отображать связанные данные. Однако, как правило, необходимо не только отображать данные, но 
и использовать какую-то логику взаимодействия с пользователем, обрабатывать пользовательский ввод. Рассмотрим, как это сделать в рамках 
паттерна MVVM.

Ключевой идеей паттерна является взаимодействие с моделью через ViewModel, то есть в данном случае использование событий визуальных компонентов и их 
обработчиков нежелательно. Чтобы решить эту задачу, в платформе Xamarin Forms имеется механизм команд.

Механизм команд раскрывается через интерфейс ICommand:

```

public interface ICommand 
{ 
	void Execute(object arg); 
	bool CanExecute(object arg); 
	event EventHandler CanExecuteChanged; 
}

```

Интерфейс ICommand определен в пространстве имен `System.Windows.Input` и расположен в сборке `System.ObjectModel`.

Встроенную поддержку команд имеют следующие элементы управления:

- `Button`

- `MenuItem`

- `ToolbarItem`

- `SearchBar`

- `TextCell`

- `ImageCell`

- `ListView`

- `TapGestureRecognizer`

Итак, для применения команд возьмем проект приложения из прошлой темы и определим в нем простейшую команду. Для этого добавим в проект класс 
IncreasePriceCommand:

```

using System;
using System.Windows.Input;

namespace HelloApp
{
    public class IncreasePriceCommand : ICommand
    {
        public event EventHandler CanExecuteChanged;
        PhoneViewModel viewModel;
        public IncreasePriceCommand(PhoneViewModel vm)
        {
            viewModel = vm;
        }

        public bool CanExecute(object parameter)
        {
            return viewModel.Price 

    
        
        
        
        
    

```

С помощью свойства Command и выражения привязки кнопка связывается с командой Increase. И при нажатии на кнопку происходит действие, заложенное в связанной команде, то есть произойдет увеличение цены товара.

Также стоит отметить, что если мы хотим использовать команды, то нам необязательно определять новый класс команды. В Xamarin.Forms есть встроенный класс Command, 
который реализует всю функциональность. Нам же достаточно передать в его конструктор нужно действие, которое соответствует делегату Action. Например, 
изменим класс PhoneViewModel следующим образом:

```

using System.ComponentModel;
using System.Windows.Input;
using Xamarin.Forms;

namespace HelloApp
{
    public class PhoneViewModel : INotifyPropertyChanged
    {
        public event PropertyChangedEventHandler PropertyChanged;
        private Phone phone;
        public ICommand Increase { get; }

        public PhoneViewModel()
        {
           phone = new Phone();
            Increase = new Command(IncreasePrice);
        }

        public void IncreasePrice()
        {
            if (phone != null)
                Price += 100;
        }

        public string Title
        {
            get { return phone.Title; }
            set
            {
                if (phone.Title != value)
                {
                    phone.Title = value;
                    OnPropertyChanged("Title");
                }
            }
        }
        public string Company
        {
            get { return phone.Company; }
            set
            {
                if (phone.Company != value)
                {
                    phone.Company = value;
                    OnPropertyChanged("Company");
                }
            }
        }
        public int Price
        {
            get { return phone.Price; }
            set
            {
                if (phone.Price != value)
                {
                    phone.Price = value;
                    OnPropertyChanged("Price");
                }
            }
        }
        protected void OnPropertyChanged(string propName)
        {
            if (PropertyChanged != null)
                PropertyChanged(this, new PropertyChangedEventArgs(propName));
        }
    }
}

```

И приложение будет также работать.

---

**Источник:** [https://metanit.com/sharp/xamarin/4.3.php](https://metanit.com/sharp/xamarin/4.3.php)

[[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 12. MVVM/Паттерн Model-View-ViewModel|Назад]] | [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 12. MVVM|Содержание]] | [[Языки программирования/C#/Графические программы/Xamarin Forms/Глава 12. MVVM/Пример MVVM|Вперёд]]
