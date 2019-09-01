from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import pytest
import time
import sys
import basefunc

def put_real_postal(element):
    element.send_keys("250")

def put_replacement_postal(element):
    element.send_keys("000")

def test_change_data():

    browser = webdriver.Firefox()
    browser.get(basefunc.BASEURL)

    basefunc.login(browser, 'id', 'pass')
    time.sleep(2)

    #reszta danych kontaktowych
    browser.find_element_by_css_selector("#ui-id-4").click()
    browser.find_element_by_css_selector("#tabContents-6 > h2 > span:nth-child(1) > a").click()
    time.sleep(1)
    postal_code = browser.find_element_by_css_selector("#primaryAddress\.postalCode")
    postal_code.click()
    postal_code_text = postal_code.text

    for i in range(0,3):
        postal_code.send_keys(Keys.BACK_SPACE)

    if(postal_code_text == "00-250"):
        put_replacement_postal(postal_code)
    else:
        put_real_postal(postal_code)

    browser.find_element_by_css_selector("#save").click()

    time.sleep(1)

    #weryfikacja
    new_data = browser.find_element_by_css_selector("#patronContactInfo > div > div > span:nth-child(5)").text
    assert new_data != postal_code_text
    
    basefunc.logout(browser)
    browser.quit()