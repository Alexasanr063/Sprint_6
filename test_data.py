from Sprint_6.locators import FaqSectionLocators

TEST_DATA = [
    (FaqSectionLocators.HEADING_0, FaqSectionLocators.PANEL_0, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
    (FaqSectionLocators.HEADING_1, FaqSectionLocators.PANEL_1, "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."),
    (FaqSectionLocators.HEADING_2, FaqSectionLocators.PANEL_2, "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."),
    (FaqSectionLocators.HEADING_3, FaqSectionLocators.PANEL_3, "Только начиная с завтрашнего дня. Но скоро станем расторопнее."),
    (FaqSectionLocators.HEADING_4, FaqSectionLocators.PANEL_4, "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."),
    (FaqSectionLocators.HEADING_5, FaqSectionLocators.PANEL_5, "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."),
    (FaqSectionLocators.HEADING_6, FaqSectionLocators.PANEL_6, "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."),
    (FaqSectionLocators.HEADING_7, FaqSectionLocators.PANEL_7, "Да, обязательно. Всем самокатов! И Москве, и Московской области."),
]

ORDER_TEST_DATA = [
    {
        "name": "Иван",
        "lastname": "Иванов",
        "address": "ул. Пушкина, д. Колотушкина, кв. 10",
        "phone": "+79991234567",

    },
    {
        "name": "Мария",
        "lastname": "Петрова",
        "address": "пр. Ленина, д. 15, кв. 5",
        "phone": "+79876543210",

    },
]
