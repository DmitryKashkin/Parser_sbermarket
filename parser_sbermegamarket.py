from bs4 import BeautifulSoup
from selenium import webdriver

URL = 'https://sbermegamarket.ru/catalog'
PATH = 'C:/Program Files/Google/Chrome/Application/chrome.exe'
PREFIX = 'https://sbermegamarket.ru'


def get_content(url, driver):
    print(url)
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, "lxml")
    for item in soup.find_all('div', class_='catalog-category-cell catalog-department__category-item'):
        get_content(PREFIX + item.find('a').get('href'), driver)
    # while True:
    #     if soup.find('div', class_='catalog-listing__items catalog-listing__items_divider-wide'):
    #         # for ...
    #     else:
    #         break


def main():
    with webdriver.Chrome() as driver:
        get_content(URL, driver)


if __name__ == '__main__':
    main()
