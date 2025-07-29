# tests/conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
#from Sprint_5.pages import MainPage


@pytest.fixture
def browser():
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")

    driver = webdriver.Edge(service=Service(), options=options)
    yield driver
    driver.quit()


# @pytest.fixture
# def main_page(browser):
#     return MainPage(browser)