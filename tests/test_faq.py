import pytest
from Sprint_6.pages.main_page import FaqSection
from Sprint_6.test_data import TEST_DATA
from Sprint_6.conftest import browser
from Sprint_6.locators import OrderPageLocators

@pytest.mark.parametrize("heading_locator, panel_locator, expected_text", TEST_DATA)
def test_faq_questions(browser, heading_locator, panel_locator, expected_text):
    faq = FaqSection(browser)
    faq.open(OrderPageLocators.URL)
    faq.click_question(heading_locator)
    answer_text = faq.get_answer_text(panel_locator)
    assert answer_text == expected_text, f"Текст ответа не совпадает. Ожидалось: {expected_text!r}, Получено: {answer_text!r}"
