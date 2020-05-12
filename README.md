# Ikea Sales Finder
I developed this tool for fun to notify me if Ikea has a sale posted on their home page. At the time I was waiting for their "bedroom sale" so instead of signing up for their newsletter I decided to make a tool to search the Ikea home page for a predefined Keyword.

## Challenges:
- the Ikea website uses client-side rendering to serve the website. This prevents us from just visiting the site and parsing the HTML file. We need to use we headless web-browser to render the page then parse the code for the desired text.
- Setting up a notification system
- setting up a server to run this script periodically (can use one of my Digital Ocean instances or Heroku)

## Tools Used
* Language: Python
* [Selenium WebDriver](https://www.selenium.dev/documentation/en/webdriver/)
* [Mozilla Gecko](https://developer.mozilla.org/en-US/docs/Mozilla/Gecko)

## The implementation

1. Get a string to search for and a website URL run the search on
2. Generate all possible combination of the search term
    * ALL-CAPS
    * Capitalize the first word in the search string
    * Capitalize all words in the search string
    * lowercase
 3. Spin up a headless instance of Geko engine using Selenium WebDriver
 4. Navigate to user-provided URL
 5. Search for the defined term on the page
 6. If the search term is found then send an email or text notifications (TODO)
     * this still needs to be implemented. I will probably use sparkpost as my email engine 
 
## The Code

### Gecko Driver
The Gecko driver is already included in the project directory `Geckofriver`

### How To Run
To run this code run `main.py`.

There are two parameters that you can set *url* and *searchTerm*.

```python
url = "https://www.ikea.com/ca/en/"
searchTerm = "Storage Event"
```
