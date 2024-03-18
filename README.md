# scrapper exercices for bairesdev

> Scrapper used to capture data from www.freeimages.com

### Setup

* Python Verion 3.9.12
* Poetry
* Requests
* BeautifulSoap
* Selenium

### How to run this project

* install dependencies by running make dependencies
* enable poetry environment by running poetry shell
* Run the main code to execute the project
* Run make tests to execute tests


## About this Project ?

In this project I developed two different approaches to capture data from the freeimages website, by using BeautifulSoup and by using Selenium Webdriver. 
Both approaches brings 15 pages of the website and a total of ~1000 itens.
I also implemented unit tests to test the Requests Scrapper. Run make test to check it out.

#### Scrapper using Python Requests and BeautifulSoup:

In this approach, I'm making a http request in the API and parsing the html content by using BeautifulSoup library.
This is a good approach if the given API doesnt block our request by using captcha or other protection systems.
The advantages of using this approach is the high speed and simple usage.

#### Scrapper using Selenium

In this approach I'am collecting all the data from the site and also developing the login 


### Other possible approaches ( not implemented )

* Pyppeteer
* Playwright


## Questions !

## How can we automate login page ?

* The login page was automated by using Selenium, navigating to the login page and putting the credentials. I used dummy creds to implement this, so the website wont really log in, so the login function is just for letting know if its possible.

## How to scale ?

* I used the Threading library to make the get requests run parallellized in order to speed up the crawler.
* This is a code manner to scale up the crawler and bring more data.
* In this example, the crawler captured One thousand items in less than 10 seconds, then, based on this test, we would be able to capture 360K items from website per hour.

> 100 items/1sec * 60 secs * 60 min = 360K items per hour

* We just have to be carefull by using this approach because it can cause troubles to the crawled website, and the website owners can also block our IP.
