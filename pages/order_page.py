import time
from selenium.webdriver.common.by import By
import random
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Sprint_6.locators import OrderPageLocators
from .base_page import BasePage

class OrderPage(BasePage):

    #URL = 'https://qa-scooter.praktikum-services.ru/'

    def cuci(self):
        button = self.wait.until(EC.visibility_of_element_located(OrderPageLocators.Cuci))
        button.click()


    def click_order_button(self):
        button = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.BUTTON_ORDER_TOP))
        button.click()

    def click_order_button_2(self):
        button = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.BUTTON_ORDER_LOW))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
        button.click()

    def fill_name(self, name):
        input_name = self.wait.until(EC.visibility_of_element_located(OrderPageLocators.INPUT_NAME))
        input_name.clear()
        input_name.send_keys(name)

    def fill_lastname(self, lastname):
        input_lastname = self.wait.until(EC.visibility_of_element_located(OrderPageLocators.INPUT_LASTNAME))
        input_lastname.clear()
        input_lastname.send_keys(lastname)

    def fill_address(self, address):
        input_address = self.wait.until(EC.visibility_of_element_located(OrderPageLocators.INPUT_ADDRESS))
        input_address.clear()
        input_address.send_keys(address)


    def fill_phone(self, phone):
        input_phone = self.wait.until(EC.visibility_of_element_located(OrderPageLocators.INPUT_PHONE))
        input_phone.clear()
        input_phone.send_keys(phone)

    def click_next(self):
        button_next = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.BUTTON_NEXT))
        button_next.click()

    def open_date_picker_and_select_24(self):
        input_date = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.INPUT_DATE))
        input_date.click()
        day_24 = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.DATE_DAY_24))
        day_24.click()

    def select_rent_term_4_days(self):
        dropdown = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.DROPDOWN_RENT_TERM))
        dropdown.click()
        option = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.DROPDOWN_OPTION_4_DAYS))
        option.click()

    def select_color_black_pearl(self):
        color = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.COLOR_BLACK_PEARL))
        color.click()

    def click_order_button_bottom(self):
        button = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.BUTTON_ORDER_BOTTOM))
        button.click()

    def confirm_order(self):
        button_yes = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.BUTTON_CONFIRM_YES))
        button_yes.click()

    def wait_for_order_modal(self):
        return self.wait.until(EC.visibility_of_element_located(OrderPageLocators.MODAL_HEADER))

    def click_view_status_button(self):
        button = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.BUTTON_VIEW_STATUS))
        button.click()

    def click_logo_scooter(self):
        logo = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.LOGO_SCOOTER))
        logo.click()

    def click_logo_yandex(self):
        logo = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.LOGO_YANDEX))
        original_window = self.driver.current_window_handle
        logo.click()
        # Ждём появления новой вкладки
        self.wait.until(EC.number_of_windows_to_be(2))
        new_window = [w for w in self.driver.window_handles if w != original_window][0]
        self.driver.switch_to.window(new_window)
        self.wait.until(EC.url_contains("https://dzen.ru/?yredirect=true"))
        return original_window

    def close_current_tab_and_switch_back(self, original_window):
        self.driver.close()
        self.driver.switch_to.window(original_window)

    def select_metro_station(self):
        self.wait.until(EC.presence_of_element_located(OrderPageLocators.INPUT_METRO)).click()
        self.wait.until(EC.element_to_be_clickable(OrderPageLocators.METRO_OPTION_PARK)).click()

    def get_current_url(self):
        return self.driver.current_url