from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import pytest
import time
import basefunc

searchphrase = 'Gra o tron'
filter_searchphrase = 'Gra o tron [Dokument dźwiękowy]'

def test_searchWithoutLog():

    browser = webdriver.Firefox()
    browser.get(basefunc.BASEURL)

    basefunc.search(browser, searchphrase)
    time.sleep(2)
    basefunc.getFirstBook(browser, searchphrase)
    time.sleep(2)
    basefunc.identifyBook(browser, searchphrase)
    basefunc.logout(browser)
    browser.quit()

def test_searchWithLog():

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
    browser.quit()

def test_searchWithFilter():
    
    browser = webdriver.Firefox()
    browser.get(basefunc.BASEURL)

    basefunc.search(browser, searchphrase)
    time.sleep(2)
    browser.find_element_by_partial_link_text("Nagranie dźwiękowe").click()
    time.sleep(1)
    browser.find_element_by_xpath("/html/body/div/div[2]/div[5]/div[3]/form/span/ul/li/div[2]/div[1]/a[1]").click()
    title_elem = browser.find_element_by_class_name('title').text
    assert filter_searchphrase in title_elem
    browser.quit()

