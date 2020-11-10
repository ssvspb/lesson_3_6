from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import pytest

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

class TestMainPage():

    def test_guest_should_see_add_to_basket_button_on_the_main_page(self, browser):
        browser, user_language = browser
        browser.get(link)
        
        expected_text = {"ru": "Добавить в корзину", "es": "Añadir al carrito"}
        
        try:
            elem = browser.find_element_by_css_selector(".btn-add-to-basket")
        except NoSuchElementException as e:
            assert False, f'ERROR: {e}'
            
        elem_text = elem.text
        exp_text = expected_text[user_language]
        assert elem_text == exp_text, "ERROR: Expected '{exp_text}' got '{elem_text}'"
        

            
