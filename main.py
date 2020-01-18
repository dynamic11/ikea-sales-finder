import requests

from requests.exceptions import HTTPError
from bs4 import BeautifulSoup

for url in ['https://www.ikea.com/ca/en/']:
    try:
        response = requests.get(url)

        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        print('Success!')
        text_file = open("Output.txt", "w")
        text_file.write(response.text)
        text_file.close()
        print(response.text.lower().find('storage event'));
        soup = BeautifulSoup(response.content, 'html.parser')

        print(soup.body.findAll(text='storage'))



