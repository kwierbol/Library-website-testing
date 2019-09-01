#ZAMAWIANIE KSIAZKI
# change tr[x] for each order

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import pytest
import time
import datetime
import basefunc

#order first found copy
def test_ordering():

    searchphrase = 'Fizyka dla grafików komputerowych'

    browser = webdriver.Firefox()
    browser.get(basefunc.BASEURL)

    basefunc.login(browser, 'id', 'pass')
    time.sleep(2)
    basefunc.goToMainPage(browser)
    time.sleep(2)
    basefunc.search(browser, searchphrase)
    time.sleep(2)
    basefunc.getFirstBook(browser, searchphrase)
    time.sleep(2)
    basefunc.identifyBook(browser, searchphrase)
    basefunc.orderFirstCopy(browser, searchphrase)

    #walidacja/weryfikacja?
    my_account = browser.find_element_by_css_selector("#primary-nav > li:nth-child(1) > a")
    my_account.click()

    my_orders = browser.find_element_by_css_selector("#ui-id-2")
    my_orders.click()

    #start = datetime.datetime.now()
    current_order = browser.find_element_by_xpath("/html/body/div/div[2]/div[5]/div[3]/div[2]/form/table/tbody/tr[3]/td[1]/a").text
    assert searchphrase in current_order

    basefunc.logout(browser)
    browser.quit()

    #end = datetime.datetime.now()
    #print(end-start)
