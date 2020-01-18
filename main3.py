from selenium import webdriver
import re
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True
#driver = webdriver.Firefox(options=options, executable_path=r'C:\Utility\BrowserDrivers\geckodriver.exe')
driver = webdriver.Firefox(options=options)

print('Going to webpage')
driver.get("https://www.ikea.com/ca/en/")
try:
    print('Start Search')
    zz = driver.page_source
    numbResults = len(re.findall(r"storage", zz, re.IGNORECASE))
    print(numbResults)
    ll = driver.find_elements_by_xpath("//*[contains(text(), 'Storage Event')]")
    print(len(ll))
    for ii in ll:
        # print ii.tag_name
        print(ii.text)  # id name as string
    # print(len(re.findall(r"storage", zz, re.IGNORECASE)))
    print('Search Done')
finally:
    driver.quit()
    print('DONE')