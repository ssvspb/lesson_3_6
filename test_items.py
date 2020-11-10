from selenium import webdriver
import pytest

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

class TestMainPage():

    def test_check_add_to_basket_button_type(self, browser):
        browser.get(link)
        
        elem = browser.find_element_by_css_selector(".btn-add-to-basket")
        
        exp_type = "submit"
        elem_type = elem.get_attribute("type")    
        assert elem_type == exp_type, f"Wrong element type: expected '{exp_type}' got '{elem_type}'"

