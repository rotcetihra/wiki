# Основные операции с базой данных SQLite

[[Языки программирования/C#|C#]] / [[Языки программирования/C#/Графические программы|Графические программы]] / [[Языки программирования/C#/Графические программы/Руководство по UWP|Руководство по UWP]] / [[Языки программирования/C#/Графические программы/Руководство по UWP/Глава 16. SQLite и Entity Framework|Глава 16. SQLite и Entity Framework]] / Основные операции с базой данных SQLite

[[Языки программирования/C#/Графические программы/Руководство по UWP/Глава 16. SQLite и Entity Framework/Добавление SQLite и Entity Framework в проект UWP|Назад]] | [[Языки программирования/C#/Графические программы/Руководство по UWP/Глава 16. SQLite и Entity Framework|Содержание]] | [[Языки программирования/C#/Графические программы/Руководство по UWP/Глава 16. SQLite и Entity Framework/Работа со сложными данными|Вперёд]]

**Дата написания:** 05.09.2026

Основные операции с базой данных SQLiteПоследнее обновление: 14.03.2016
 
 
 

 
- 
 
- 
 
- 
 
 

 
 

 
 
 
 
 

 

После создания моделей и добавления Entity Framework создадим собственно элементы управления, которые позволят нам добавлять, обновлять, удалять и просматривать 
данные из базы данных.

По умолчанию у нас уже есть страница MainPage.xaml. Пусть она будет выводить список компаний, то есть объектов класса Company, а также будет содержать элементы 
для управления этими объектами. Итак, изменим MainPage.xaml следующим образом:

```

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

```

Для отображения списка определен элемент ListView, а для управления компаниями в нижней панели определены три кнопки. Теперь в файле кода MainPage.xaml.cs 
определим для них обработчики нажатия:

```
public sealed partial class MainPage : Page
{
 public MainPage()
 {
 this.InitializeComponent();
 this.Loaded += MainPage_Loaded;
 }

 private void MainPage_Loaded(object sender, RoutedEventArgs e)
 {
 using (MobileContext db = new MobileContext())
 {
 companiesList.ItemsSource = db.Companies.ToList();
 }
 }

 private void Add_Click(object sender, RoutedEventArgs e)
 {
 Frame.Navigate(typeof(CompanyPage));
 }

 private void Edit_Click(object sender, RoutedEventArgs e)
 {
 // получаем выделеный пункт меню
 if (companiesList.SelectedItem != null)
 {
 Company company = companiesList.SelectedItem as Company;
 if (company != null)
 Frame.Navigate(typeof(CompanyPage), company.Id);
 }
 }

 private void Delete_Click(object sender, RoutedEventArgs e)
 {
 // получаем выделеный пункт меню
 if (companiesList.SelectedItem != null)
 {
 Company company = companiesList.SelectedItem as Company;
 if (company != null)
 {
 using (MobileContext db = new MobileContext())
 {
 db.Companies.Remove(company);
 db.SaveChanges();
 companiesList.ItemsSource = db.Companies.ToList();
 }
 }
 }
 }
}
```

При загрузке страницы срабатывает обработчик `MainPage_Loaded`, в котором получаем список компаний из базы данных и устанавливаем его в качестве 
источника данных для ListView:

```
companiesList.ItemsSource = db.Companies.ToList();
```

Обработчик кнопки добавления `Add_Click` просто перенаправляет на страницу CompanyPage, которую мы чуть позже создадим.

Обработчик кнопки редактирования `Edit_Click` получает выделенный объект Company в списке и передает его id на страницу CompanyPage.

Обработчик кнопки удаления `Delete_Click` получает выделенный объект Company и передает его в метод Remove:

```
db.Companies.Remove(company);
```

Этот метод позволяет сгенерировать SQL-выражение DELETE для удаления данных из таблицы компаний. После этого надо сохранить все изменения, то есть 
выполнить это SQL-выражение с помощью вызова:

```
db.SaveChanges();
```

И далее переустанавливаем источник данных для ListView.

В итоге главная страница будет выглядеть примерно так:
![Работа с базой данных в UWP](pics/17.7.png)

Для добавления/редактирования добавим новую страницу по типу BlankPage, которую назовем CompanyPage:
![CRUD операции в UWP](pics/17.6.png)

Так как модель Company имеет по сути одно значимое свойство - Name, то много нам добавлять и редактировать не надо, и для обеих операций нам хватит одной страницы. 
Тем более эти операции у нас будут отличаться только наличием Id при редактировании.

Изменим начальный код страницы _CompanyPage.xaml_ на следующий:

```

 
 
 
 Название компании
 
 
 
 
 
 
 

```

Здесь одно текстовое поле для редактирования названия компании и две кнопки: для сохранения изменений и отмены действий.

Далее изменим код C#, добавив в него обработчики кнопок:

```
public sealed partial class CompanyPage : Page
{
 Company company;

 public CompanyPage()
 {
 this.InitializeComponent();
 }

 protected override void OnNavigatedTo(NavigationEventArgs e)
 {
 if (e.Parameter != null)
 {
 int id = (int)e.Parameter;
 using (MobileContext db = new MobileContext())
 {
 company = db.Companies.FirstOrDefault(c => c.Id == id);
 }
 }
 
 if (company != null)
 {
 headerBlock.Text = "Редактирование компании";
 nameBox.Text = company.Name;
 }
 }

 private void Save_Click(object sender, RoutedEventArgs e)
 {
 using (MobileContext db = new MobileContext())
 {
 if(company!=null)
 {
 company.Name = nameBox.Text;
 db.Companies.Update(company);
 }
 else
 {
 db.Companies.Add(new Company { Name = nameBox.Text });
 }
 db.SaveChanges();
 }
 GoToMainPage();
 }

 private void Cancel_Click(object sender, RoutedEventArgs e)
 {
 GoToMainPage();
 }

 private void GoToMainPage()
 {
 if (Frame.CanGoBack)
 Frame.GoBack();
 else
 Frame.Navigate(typeof(MainPage));
 }
}
```

При переходе на страницу срабатывает метод `OnNavigatedTo()`. В нем мы смотрим на переданный параметр. Если он не равен null, значит, нам надо отредактировать 
сушность, идентификатор которой равен параметру. В ином случае надо выполнить добавление. По этому идентифкатору мы получаем компанию из бд:

```
company = db.Companies.FirstOrDefault(c => c.Id == id);
```

При нажатии на кнопку сохранения смотрим, была ли получена ранее компания. Если она была получена, значит, нам надо отредактировать ее. Для этого объект компании 
передается в метод `Update()`:

```
db.Companies.Update(company);
```

Он генерирует выражение SQL UPDATE для обновления записей в базе данных.

Если же компания при загрузке страницы не была установлена, то выполняем добавление в базе данных с помощью метода `Add()`:

```
db.Companies.Add(new Company { Name = nameBox.Text });
```

Далее выполняем сгенерированное SQL-выражение с помощью метода `db.SaveChanges()`. И после всех изменений возвращаемся на главную страницу.

В итоге CompanyPage будет выглядеть примерно так:
![Добавление в базу данных на Universal Windows Platform](pics/17.8.png)

Таким образом, мы создали простейшее приложение, которое выполняет все базовые операции с данными: чтение, добавление, обновление и удаление.

---

**Источник:** [https://metanit.com/sharp/uwp/16.2.php](https://metanit.com/sharp/uwp/16.2.php)
