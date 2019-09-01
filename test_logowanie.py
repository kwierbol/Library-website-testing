from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest
import time
import basefunc

def test_login_successfull():

    browser = webdriver.Firefox()
    browser.get(basefunc.BASEURL)

    basefunc.login(browser, 'id', 'pass')
    time.sleep(2)

    try:
        assert 'Moje konto' in browser.title
        #? should I log out here?
        basefunc.logout(browser)
        browser.quit()
    except AssertionError:
        print("ERROR: Failed log in")
        quit()


def test_login_unsuccessfull():

    browser = webdriver.Firefox()
    browser.get(basefunc.BASEURL)

    basefunc.login(browser, 'id', 'wrongpass')
    time.sleep(2)

    error_popup = browser.find_element_by_css_selector("#feedback-template > ul > li > span")
    error_text = error_popup.text

    assert error_text == "Nieprawidłowa nazwa użytkownika i/lub hasło, proszę spróbować ponownie."
    