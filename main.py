import requests
from bs4 import BeautifulSoup

URL = "https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22north%22%3A37.86885493321513%2C%22east%22%3A-122.31488314990234%2C%22south%22%3A37.68161041679897%2C%22west%22%3A-122.55177585009766%7D%2C%22mapZoom%22%3A12%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%7D"
FORM = "https://docs.google.com/forms/d/e/1FAIpQLSfFT4KXah2jy-JpdMZ5gajwha_zpQhC-YdP_JWWHFf9iQP5Hg/viewform?usp=sf_link"
HEADERS = {
    "Accept_Language":"en-GB,en;q=0.7",
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                 "Chrome/105.0.0.0 Safari/537.36"
}

response = requests.get(url=URL, headers=HEADERS)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
print(soup.prettify())
links = soup.find_all(name="a", class_="StyledPropertyCardDataArea-c11n-8-69-2__sc-yipmu-0")
print(links)