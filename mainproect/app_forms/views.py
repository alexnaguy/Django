from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.shortcuts import render
from abc import ABC, abstractmethod
from django.views.generic import CreateView

from selenium.webdriver import Chrome, ChromeOptions, Firefox, FirefoxOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from fake_useragent import UserAgent
import csv


class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('home')


class FormManage:

    @staticmethod
    def auto(request):
        return render(request, 'my_form.html')

    @staticmethod
    def home(request):
        return render(request, 'home.html')

    @staticmethod
    def contacts(request):
        return render(request, 'contacts.html')

    @staticmethod
    def pars_table(request):
        return render(request, 'pars_table.html')

    @staticmethod
    def get_info(request):
        brand = request.POST.get("brand")
        model = request.POST.get("model")
        price_one = request.POST.get("price_one")
        price_two = request.POST.get("price_two")
        year_one = request.POST.get("year_one")
        year_two = request.POST.get("year_two")
        city = request.POST.get("city")

        filter_data = FilterData(
            brand,
            model,
            price_one,
            price_two,
            year_one,
            year_two,
            city
        )
        try:
            filter_one = FilterAvitoCar('https://www.avito.ru/', filter_data)
            # Должен активировать все методы класса FilterAvitoCar:
            # Собрал все методы WebdriverChrome
            filter_one.activate_browser()

            filter_one.search_button_input()
            #filter_one.change_city_search()
            filter_one.input_price_from_filter()
            filter_one.input_price_to_filter()
            filter_one.input_year_release_from_filter()
            filter_one.input_year_release_to_filter()
            filter_one.change_number_owners()
            #filter_one.change_private_ads()
            filter_one.search_button_show_ads()

            # В этом методе я получу новый url-адрес
            url_current = filter_one.switch_url_avito()
            #Создаем объект Парсинга
            parsing_one = AvitoParse(url_current, 5)
            parsing_one.activate_browser()
            parsing_one.parse()

        except Exception as ex:
            print(ex)

        return render(request, 'get.html', {"brand": brand,
                                            "model": model,
                                            "price_one": price_one,
                                            "price_two": price_two,
                                            "year_one": year_one,
                                            "year_two": year_two,
                                            "city": city
                                            })
#Вспоомгательный класс-для соединения
class FilterData:
    def __init__(self, brand, model, price_one, price_two, year_one, year_two, city):

        self.brand = brand
        self.model = model
        self.price_one = price_one
        self.price_two = price_two
        self.year_one = year_one
        self.year_two = year_two
        self.city = city


class WebdriverAbstract(ABC):
    @abstractmethod
    def connect_proxy(self):
        """
        Подключает различные IPI адреса (прокси серверы)
        """
        pass

    @abstractmethod
    def connect_options_webdriver(self):
        """
        Подключает вебдрайвер и добавляет опции различных IPI адрессов
        """
        pass

    @abstractmethod
    def include_browser(self):
        """
        Подключили вэбдрайвер и применили опции
        """
        pass

    @abstractmethod
    def get_url(self):
        pass


class WebdriverChrome(WebdriverAbstract):
    # Прописать параметры класса- self.options , self.browser
    user_agent: UserAgent()
    options: webdriver.ChromeOptions()
    browser: webdriver.Chrome()

    def __init__(self, url: str):
        self.url = url

    def connect_proxy(self):
        """
        Подключает различные IPI адресса (прокси серверы)
        """
        self.user_agent = UserAgent()


    def connect_options_webdriver(self):
        """
        Подключает вебдрайвер и добавляет опции различных IPI адрессов
        """
        # Запуск браузера Chrome
        self.options = webdriver.ChromeOptions()

        # Добавил опции для вэбдрайвера
        self.options.add_argument(f"user-agent= {self.user_agent.chrome}")
        # Отключение контроля автоматизации
        self.options.add_argument("--disable-blink-features=AutomationControlled")

    def include_browser(self):
        """
        Подключили вэбдрайвер и применили опции
        """
        self.browser = webdriver.Chrome(options=self.options)


    def get_url(self):
        """
        Браузер переходит на URL, который передает пользователь
        :return:
        """
        self.browser.get(self.url)


class AbstractClassFilter(ABC):

    @abstractmethod
    def search_button_input(self):
        pass

    @abstractmethod
    def change_city_search(self):
        pass

    @abstractmethod
    def input_price_from_filter(self):
        pass

    @abstractmethod
    def input_price_to_filter(self):
        pass

    @abstractmethod
    def input_year_release_from_filter(self):
        pass

    @abstractmethod
    def input_year_release_to_filter(self):
        pass

    @abstractmethod
    def change_number_owners(self):
        pass

    @abstractmethod
    def change_private_ads(self):
        pass

    @abstractmethod
    def search_button_show_ads(self):
        pass


class FilterAvitoCar(WebdriverChrome, AbstractClassFilter, FormManage):

    def __init__(self, url, filter_data):
        super().__init__(url)
        self.filter_data = filter_data

    def activate_browser(self):
        self.connect_proxy()
        self.connect_options_webdriver()
        self.include_browser()
        self.get_url()
        print("Браузер успешно подключен!")

    def search_button_input(self):
        """
        Находит главную кнопку поиска на сайте Авито,куда затем передаются параметры поиска.
        :return: None
        """
        # Нашли кнопку ввода марки и модели автомобиля
        inp = self.browser.find_element(By.CSS_SELECTOR, "[data-marker='search-form/suggest']")
        # Ввели в поисковик марку и модель автомобиля (Renault Logan)
        inp.send_keys(self.filter_data.brand + " " + self.filter_data.model)
        inp.send_keys(Keys.ENTER)
        sleep(3)
        print("Успешно введена модель авто!")

    def change_city_search(self):
        """
        Находит кнопку "Изменить город". Меняет город, на указанный пользователем и
        делает поиск по Объявлениям.
        :return: None
        """
        # Нашли кнопку "Поменять город"
        input = self.browser.find_element(By.CSS_SELECTOR, "[class='desktop-nev1ty']").click()
        sleep(2)
        # Нашли кнопку для ввода своего города
        button_city_inp = self.browser.find_element(By.CSS_SELECTOR, "[data-marker='popup-location/region/input']")
        button_city_inp.send_keys(Keys.CONTROL, "a")

        # Нужно передать город, из класса FormManage
        button_city_inp.send_keys(self.filter_data.city)
        sleep(2)
        # Нашли кнопку "Показать обьявления"
        sear = self.browser.find_element(By.CSS_SELECTOR, "[data-marker='popup-location/save-button']").click()
        sleep(1)
        # Дублирую кнопку "Показать обьявления"
        sear = self.browser.find_element(By.CSS_SELECTOR, "[data-marker='popup-location/save-button']").click()
        sleep(5)



    def input_price_from_filter(self):
        """
        Находит кнопку ввода "Цена от" и вводит, указанное пользователем значение цены.
        :return: None
        """
        # Нашли кнопку "Цена от"
        inp = self.browser.find_element(By.CSS_SELECTOR, "[data-marker='price/from']")
        # Ожидание
        #wait = WebDriverWait(self.browser, timeout=2)
        # Нашли кнопку "Цена от" еще раз
        #inp = self.browser.find_element(By.CSS_SELECTOR, "[data-marker='price/from']").click()
        # Ждем пока кнопка не станет доступной для нажатия
        #wait.until(lambda d: inp.is_displayed())
        inp.send_keys(self.filter_data.price_one)
        inp.send_keys(Keys.ENTER)

    def input_price_to_filter(self):
        """
        Находит кнопку ввода "Цена до" и вводит свое значение цены.
        :return: None
        """
        inp = self.browser.find_element(By.CSS_SELECTOR, "[data-marker='price/to']")
        inp.send_keys(self.filter_data.price_two)
        inp.send_keys(Keys.ENTER)
        print("Успешно введены цены !")
        sleep(2)

    def input_year_release_from_filter(self):
        """
         Находит кнопку ввода "Год выпуска от" и вводит свое значение года.
        :return: None
        """
        inp = self.browser.find_element(By.CSS_SELECTOR, "[data-marker='params[188]/from/input']")
        inp.send_keys(self.filter_data.year_one)
        inp.send_keys(Keys.ENTER)

    def input_year_release_to_filter(self):
        """
        Находит кнопку ввода "Год выпуска оо" и вводит свое значение года.

        :return: None
        """
        inp = self.browser.find_element(By.CSS_SELECTOR, "[data-marker='params[188]/to/input']")
        inp.send_keys(self.filter_data.year_two)
        inp.send_keys(Keys.ENTER)
        sleep(3)
        print("Успешно введены года !")

    def change_number_owners(self):
        """
        Выбирает число владельцев автомобиля "Не более двух".
        :return: None
        """
        inp = self.browser.find_element(By.CSS_SELECTOR, "[data-marker='option(19984)']")
        inp.click()
        sleep(3)
        print("Успешно выбрано число  владельцев!")

    def change_private_ads(self):
        """
        Выбирает "Частные объявления".
        :return: None
        """
        inp = self.browser.find_element(By.CSS_SELECTOR, "[data-marker='user(1)']")
        inp.click()
        sleep(3)
        print("Частные объявления выбраны")

    def search_button_show_ads(self):
        """
        Нажимает кнопку "Показать объявления".
        :return: None
        """
        inp = self.browser.find_element(By.CSS_SELECTOR, "[data-marker='search-filters/submit-button']")
        inp.click()
        sleep(15)
        print("Идет поиск объявлений по заданным параметрам")

    def switch_url_avito(self):
        """
        Перемещает на другую вкладку браузера.
        :return: None
        """
        link = self.browser.current_url
        return link

    #Этот метод вызывает все методы FilterAviroCar
    def activate_func_filter(self):
        self.search_button_input()
        #self.change_city_search()
        self.input_price_from_filter()
        self.input_price_to_filter()
        self.input_year_release_from_filter()
        self.input_year_release_to_filter()
        self.change_number_owners()
        self.change_private_ads()
        self.search_button_show_ads()


class AvitoParse(WebdriverChrome):
    def __init__(self, url, count=100):
        super().__init__(url)
        self.count = count
        self.data = []

    def activate_browser(self):
        self.connect_proxy()
        self.connect_options_webdriver()
        self.include_browser()
        self.get_url()
        print("Браузер успешно подключен!")

    def __paginator(self):
        # Находим в браузере кнопку "Следующая страница"
        while self.browser.find_elements(By.CSS_SELECTOR,"[data-marker='pagination-button/next']")\
            and self.count > 0:
            self.__parse_page()
            # Если есть делаем клик на кнопку Next
            self.browser.find_element(By.CSS_SELECTOR, "[data-marker='pagination-button/next']").click()
            self.count -= 1

    # Парсинг одной страницы
    def __parse_page(self, request):

        """
        Берет все объвления на одной странице и парсит (собирает данные) для каждого значения:
        name, description, url, price, date_car.
        Затем собирает их в список и сохраняет в формате json.
        :return: List
        """

        # Находим все объявления
        titles = self.browser.find_elements(By.CSS_SELECTOR, "[data-marker='item']")

        for title in titles:
            # Находим название объявления
            name = title.find_element(By.CSS_SELECTOR, "[itemprop='name']").text
            description = title.find_element(By.CSS_SELECTOR, "[data-marker='item-specific-params']").text
            url = title.find_element(By.CSS_SELECTOR, "[data-marker= 'item-title']").get_attribute("href")
            price = title.find_element(By.CSS_SELECTOR, "[itemprop='price']").get_attribute("content")
            price = price + " " + "руб."
            date_car_par = title.find_element(By.CSS_SELECTOR, "[data-marker='item-date/tooltip/reference']").text

            list_date = ["секунд", "секунды", "минут", "минуту", "минуты", "час", "часа", "часов" ]
            dates = date_car_par.split()[1]
            if dates in list_date:
                print(date_car_par)
                data = [name, url, price, description, date_car_par]

                self.data.append(data)

        self.save_data()
        return render(request, 'pars_table.html')



        


    def parse(self):
        self.__paginator()
        self.__parse_page()
        #self.close_browser()

    def save_data(self):
        """
        Сохраняет записанные данные в формате json.
        :return:
        """
        for car in self.data:
            with open("cars_ads.csv", "a") as file:
                writer = csv.writer(file)
                writer.writerow(car)
        print(f"Запись произведена успешно.")



    def close_browser(self):
        self.browser.close()
        self.browser.quit()
