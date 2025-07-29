from selenium.webdriver.common.by import By

class FaqSectionLocators:
    HEADING_0 = (By.ID, "accordion__heading-0")
    PANEL_0 = (By.ID, "accordion__panel-0")

    HEADING_1 = (By.ID, "accordion__heading-1")
    PANEL_1 = (By.ID, "accordion__panel-1")

    HEADING_2 = (By.ID, "accordion__heading-2")
    PANEL_2 = (By.ID, "accordion__panel-2")

    HEADING_3 = (By.ID, "accordion__heading-3")
    PANEL_3 = (By.ID, "accordion__panel-3")

    HEADING_4 = (By.ID, "accordion__heading-4")
    PANEL_4 = (By.ID, "accordion__panel-4")

    HEADING_5 = (By.ID, "accordion__heading-5")
    PANEL_5 = (By.ID, "accordion__panel-5")

    HEADING_6 = (By.ID, "accordion__heading-6")
    PANEL_6 = (By.ID, "accordion__panel-6")

    HEADING_7 = (By.ID, "accordion__heading-7")
    PANEL_7 = (By.ID, "accordion__panel-7")

class OrderPageLocators:
    BUTTON_ORDER_TOP = (By.XPATH, "//button[text()='Заказать']")
    BUTTON_ORDER_LOW = (By.CLASS_NAME, "Button_Button__ra12g.Button_Middle__1CSJM")
    Cuci = (By.CLASS_NAME,"App_CookieButton__3cvqF")
    INPUT_NAME = (By.CSS_SELECTOR, "input[placeholder='* Имя']")
    INPUT_LASTNAME = (By.CSS_SELECTOR, "input[placeholder='* Фамилия']")
    INPUT_ADDRESS = (By.CSS_SELECTOR, "input[placeholder='* Адрес: куда привезти заказ']")
    INPUT_METRO = (By.CSS_SELECTOR, ".select-search__input")
    METRO_OPTION_PARK = (By.XPATH, "//*[text()='Сокольники']")
    INPUT_PHONE = (By.CSS_SELECTOR, "input[placeholder='* Телефон: на него позвонит курьер']")
    BUTTON_NEXT = (By.XPATH, "//button[text()='Далее']")
    INPUT_DATE = (By.CSS_SELECTOR, "input[placeholder='* Когда привезти самокат']")
    DATE_DAY_24 = (By.XPATH, "//div[contains(@class,'react-datepicker__day') and contains(@class, 'react-datepicker__day--024')]")
    DROPDOWN_RENT_TERM = (By.XPATH, "//*[text()='* Срок аренды']")
    DROPDOWN_OPTION_4_DAYS = (By.XPATH, "//div[contains(@class,'Dropdown-option') and text()='четверо суток']")
    COLOR_BLACK_PEARL = (By.XPATH, "//*[text()='чёрный жемчуг']")
    BUTTON_ORDER_BOTTOM = (By.XPATH,
                           "//button[contains(@class,'Button_Button__ra12g') and contains(@class,'Button_Middle__1CSJM') and text()='Заказать']")
    BUTTON_CONFIRM_YES = (By.XPATH,
                          "//button[contains(@class,'Button_Button__ra12g') and contains(@class,'Button_Middle__1CSJM') and text()='Да']")
    MODAL_HEADER = (By.XPATH, "//div[contains(@class,'Order_ModalHeader__3FDaJ') and text()='Заказ оформлен']")
    BUTTON_VIEW_STATUS = (By.XPATH,
                          "//button[contains(@class,'Button_Button__ra12g') and contains(@class,'Button_Middle__1CSJM') and text()='Посмотреть статус']")
    LOGO_SCOOTER = (By.XPATH, "//img[@src='/assets/scooter.svg' and @alt='Scooter']")
    LOGO_YANDEX = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")





