from selenium import webdriver
import os
import string
from selenium.webdriver.firefox.options import Options

# get current working directory
cwd = os.getcwd()
# set path to geckodriver
cwd=cwd+'/geckodriver'

# configure and start selenium webdriver
options = Options()
options.headless = True
driver = webdriver.Firefox(options=options, executable_path=cwd)

# serch configuration variables
url = "https://www.ikea.com/ca/en/"
searchTerm = "Storage Event"

# check number of word to determine all possible capitalization of the search term
if len(searchTerm.split()) > 1:
    possibleSearchTerms = [searchTerm.lower(), searchTerm.upper(), string.capwords(searchTerm), searchTerm.capitalize()]
else:
    possibleSearchTerms = [searchTerm.lower(), searchTerm.upper(), searchTerm.capitalize()]

print("Possible Search terms:", possibleSearchTerms)

# got to desired webpage
print('Going to webpage:', url)
driver.get(url)
try:
    print('Start Search')
    numbResults = 0
    for possibleSearchTerm in possibleSearchTerms:

        # search for term
        print("Searching for Term:", possibleSearchTerm)
        xpath = "//*[contains(text(), '" + possibleSearchTerm + "')]"
        results = driver.find_elements_by_xpath(xpath)

        # increment search results
        numbResults = numbResults + len(results)
        print(numbResults)
    print("Total Results Found:", numbResults)
    print('Search Done')
finally:
    driver.quit()
    print('DONE')