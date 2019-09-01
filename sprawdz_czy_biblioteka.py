from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://priam.umcs.lublin.pl:8080/search/query?theme=umcs')

try:
    assert 'Katalog Biblioteki UMCS' in browser.title
except AssertionError:
    print("Wrong site title")

browser.quit()