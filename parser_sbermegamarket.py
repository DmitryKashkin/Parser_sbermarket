from bs4 import BeautifulSoup
from selenium import webdriver

# # from selenium.webdriver.chrome.options import Options
# from selenium.webdriver import ChromeOptions
# from requests_html import HTMLSession
# from pyppeteer import launch

URL = 'https://sbermegamarket.ru/catalog'
PATH = 'C:/Program Files/Google/Chrome/Application/chrome.exe'


def get_content(url):
    with webdriver.Chrome() as driver:
        driver.get(URL)
        soup = BeautifulSoup(driver.page_source, "lxml")
        for item in soup.find_all('div', class_='catalog-category-cell catalog-department__category-item'):
            # print(item)
            url2 = item.find('a').get('href')
            print(url2)


def main():
    get_content(URL)


if __name__ == '__main__':
    main()
