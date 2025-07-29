import pytest
from Sprint_6.pages.order_page import OrderPage
from Sprint_6.test_data import ORDER_TEST_DATA
from Sprint_6.conftest import browser


@pytest.mark.parametrize("data", ORDER_TEST_DATA)
# Первая кнопка
def test_order_form(browser, data):
    order_page = OrderPage(browser)
    order_page.open()
    order_page.click_order_button()
    order_page.fill_name(data["name"])
    order_page.fill_lastname(data["lastname"])
    order_page.fill_address(data["address"])
    order_page.select_metro_station()
    order_page.fill_phone(data["phone"])
    order_page.click_next()

    # Выбор даты
    order_page.open_date_picker_and_select_24()
    # Выбор срока аренды
    order_page.select_rent_term_4_days()
    # Выбор цвета
    order_page.select_color_black_pearl()
    # Нажать кнопку "Заказать" внизу
    order_page.click_order_button_bottom()
    # Подтвердить заказ нажатием "Да"
    order_page.confirm_order()

    modal_header = order_page.wait_for_order_modal()
    assert modal_header.is_displayed(), "'Заказ оформлен' не отображается"
# Вторая кнопка
@pytest.mark.parametrize("data", ORDER_TEST_DATA)
def test_order_form_2(browser, data):
    order_page = OrderPage(browser)
    order_page.open()
    order_page.cuci()
    order_page.click_order_button_2()
    order_page.fill_name(data["name"])
    order_page.fill_lastname(data["lastname"])
    order_page.fill_address(data["address"])
    order_page.select_metro_station()
    order_page.fill_phone(data["phone"])
    order_page.click_next()

    # Выбор даты
    order_page.open_date_picker_and_select_24()
    # Выбор срока аренды
    order_page.select_rent_term_4_days()
    # Выбор цвета
    order_page.select_color_black_pearl()
    # Нажать кнопку "Заказать" внизу
    order_page.click_order_button_bottom()
    # Подтвердить заказ нажатием "Да"
    order_page.confirm_order()

    modal_header = order_page.wait_for_order_modal()
    assert modal_header.is_displayed(), "'Заказ оформлен' не отображается"

def test_logo_scooter(browser):
    main_page = OrderPage(browser)
    main_page.open()
    main_page.click_logo_scooter()
    assert main_page.get_current_url() == OrderPage.URL, "Ожидался переход на главную страницу"

def test_logo_yandex(browser):
    other_page = OrderPage(browser)
    other_page.open()
    original_window = browser.current_window_handle
    other_page.click_logo_yandex()
    assert browser.current_url.startswith("https://dzen.ru/?yredirect=true")
