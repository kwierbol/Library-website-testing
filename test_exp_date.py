from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import pytest
import time
import basefunc

def test_order_exp_date():

    browser = webdriver.Firefox()
    browser.get(basefunc.BASEURL)

    basefunc.login(browser, 'id', 'pass')
    time.sleep(2)

    my_orders = browser.find_element_by_xpath("//*[@id=\"ui-id-2\"]")
    my_orders.click()

    order_date = browser.find_element_by_xpath("//*[@id=\"request\"]/tbody/tr[1]/td[3]/div").text
    expiry_date = browser.find_element_by_xpath("//*[@id=\"request\"]/tbody/tr[1]/td[4]/div").text

    a = int(order_date[1])
    b = int(expiry_date[1])
    assert (b-a) == 6

    basefunc.logout(browser)
    time.sleep(2)
    browser.quit()