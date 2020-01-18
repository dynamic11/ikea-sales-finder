import string

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
user_name = "YOUR EMAILID"
password = "YOUR PASSWORD"
driver = webdriver.Firefox()
driver.get("https://www.ikea.com/ca/en/")
ll = driver.find_elements_by_xpath("//*[contains(text(), 'Storage Event')]")
print(ll)
pageText = driver.find_element_by_id('webcaHome').text
zz =driver.page_source
print(zz.lower().find('storage event'))
if 'Storage event' in zz:
    print('yay!')
else:
    print('nooo')
driver.quit()
