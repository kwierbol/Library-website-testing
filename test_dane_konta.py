from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import pytest
import time
import basefunc

def test_check_data():
    
    browser = webdriver.Firefox()
    browser.get(basefunc.BASEURL)

    basefunc.login(browser, 'id', 'pass')
    time.sleep(2)
    
    #matching name
    user = browser.find_element_by_css_selector("#main > h1").text

    try:
        assert user == "UID Surname, First name"
    except:
        print("User's name does not match")

    #reszta danych kontaktowych
    browser.find_element_by_css_selector("#ui-id-4").click()

    exp_date = browser.find_element_by_css_selector("#patron\.expirationDateField").text
    user_type = browser.find_element_by_css_selector("#patron\.patronTypeField").text
    account_number = browser.find_element_by_css_selector("#patron\.primaryBarcodeField").text
    communication_preference = browser.find_element_by_css_selector("#patron\.communicationPreference").text
    address_street = browser.find_element_by_css_selector("#patronContactInfo > div > div > span:nth-child(1)").text
    address_city = browser.find_element_by_css_selector("#patronContactInfo > div > div > span:nth-child(3)").text
    email = browser.find_element_by_css_selector("#patronContactInfo > div > div > label.element").text

    assert exp_date == "31-10-2019 00:15"
    assert user_type == "Student /st.dzienne"
    assert account_number == "id"
    assert communication_preference == "Email"
    assert address_street == "Address"
    assert address_city == "City"
    assert email == "email@email.com"

    basefunc.logout(browser)

    browser.quit()