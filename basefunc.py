#this file provides functions that execute basic SUT functionalities

'''
notes - for now the strings that let identify WebElements are hardcoded,
assuming it's tailored for this specific SUT and assuming they don't
change in subpages

TODO => make xpath and css selectors separate versions

'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
import time

BASEURL = "http://priam.umcs.lublin.pl:8080/search/query?theme=umcs"

def login(browser, login, password):
    
    username_elem_id = 'h_username'
    password_elem_id = 'h_password'

    #fill username
    login_elem = browser.find_element_by_id(username_elem_id)
    login_elem.send_keys(login)

    time.sleep(2)
    
    #fill password
    password_elem = browser.find_element_by_id(password_elem_id)
    password_elem.send_keys(password + Keys.RETURN)



def logout(browser):

    try:
        logout_elem = browser.find_element_by_xpath("/html/body/div/div[2]/div[1]/div/ul/li[7]/a")
        logout_elem.click()

    except NoSuchElementException:
        print("ERROR: No logout element found")

    except:
        print("ERROR: Could not log out")


def goToMainPage(browser):

    try:
        mainpage = browser.find_element_by_css_selector(".logo > a:nth-child(1)")
        mainpage.click()
    except NoSuchElementException:
        print("ERROR: No main page element found")


def search(browser, searchphrase):

    try:
        searchbox = browser.find_element_by_xpath("html/body/div/div[2]/div[2]/div/form/div[2]/input")
        searchbox.send_keys(searchphrase + Keys.RETURN)

    except NoSuchElementException:
        print("ERROR: No searchbox found")
        quit()


#zwraca pierwsza ksiazke z wynikow wyszukiwania
def getFirstBook(browser, searchphrase):

    try:
        firstElement = browser.find_element_by_xpath("//*[@id=\"itemlist\"]/span/ul/li[1]/div[2]/div[1]/a[1]")
        firstElement.click()

    except NoSuchElementException:
        print("no first element for " + searchphrase)
        time.sleep(3)
        browser.quit()
        quit()


def identifyBook(browser, searchphrase):

    try:
        title_elem = browser.find_element_by_class_name('title').text
        print(title_elem)
        assert searchphrase in browser.find_element_by_class_name('title').text
        print("Success identifying book!")

    except AssertionError:
        print("it's not the book you were looking for")
        browser.quit()
        quit()


def orderFirstCopy(browser, searchphrase):

    #watchout for id, it's likely to change
    try:
        #! id-based xpath
        #order_button = browser.find_element_by_xpath("//*[@id=\"id54\"]/table/tbody/tr[1]/td[9]/div/a")
        #WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='csv-button']"))).click()
        time.sleep(2)
        order_button = browser.find_element_by_xpath("/html/body/div/div[2]/div[5]/div[5]/div[1]/form/table/tbody/tr[1]/td[9]/div/a")
        #order_button = browser.find_element_by_css_selector("#id193 > table > tbody > tr.odd > td.buttonColumn > div > a")
        order_button.click()
    
    except NoSuchElementException:
        print("ERROR: No order button found")
        logout(browser)
        browser.quit()
        quit()

    #watchout for id
    next_button = browser.find_element_by_xpath("//*[@id=\"main\"]/div/form/ul[2]/li/input[1]")
    next_button.click()

    title = browser.find_element_by_css_selector("#main > div > ul > li > table > tbody > tr:nth-child(1) > td:nth-child(2)").text
    assert searchphrase in title

    #watchout for id
    next_button = browser.find_element_by_xpath("//*[@id=\"main\"]/div/form/ul/li/input[1]")
    next_button.click()


