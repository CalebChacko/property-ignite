import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import Scrape.scrape_tools as st



def zillow_housing(browser):
    print('Accessing Zillow')

    browser.get('https://www.zillow.com/homes/Mississauga,-ON_rb/')
    time.sleep(20)

    # Collect all housing links
    page_html = browser.page_source
    p_soup = BeautifulSoup(page_html, 'html.parser') 

    posts = p_soup.find_all('div', attrs={'class': 'list-card-info'})
    for post in posts:
        print(post.contents)
        house_soup = BeautifulSoup(str(post.contents), 'html.parser')
        link_tag = house_soup.find('a')
        # print(link_tag)
        print(link_tag)

    print(len(posts))

    links = p_soup.find_all('a', attrs={'class': 'list-card-link'})
    # for link in links:
        # print(link)
    print(len(links))
    time.sleep(120)

    browser.find_element(By.XPATH, "//*[@title='Next page']").click()

    # Iterate through links to get housing data

def zillow_html():
    # Opening the html file
    HTMLFile = open('.\sauga_1.html', "r")

    # Reading the file
    index = HTMLFile.read()

    soup = BeautifulSoup(index, 'html.parser')

    posts = soup.find_all('div', attrs={'class': 'list-card-info'})
    for post in posts:
        # print(post.contents)
        house_soup = BeautifulSoup(str(post.contents), 'html.parser')
        link_tag = house_soup.find('a')
        # print(link_tag)
        if link_tag is None:
            continue
        print(link_tag.get('href'))
    print(len(posts))

# zillow_html()

def extract_house_data(posting_html, link_num):
    # Collect all housing links
    page_html = posting_html
    soup = BeautifulSoup(page_html, 'html.parser') 

    with open('html_test' + str(link_num) + '.txt', "w", encoding="utf-8") as f:
        f.write(page_html)

    # r = requests.get(link)
    # page_source = r.text
    # print(page_source)

    # soup = BeautifulSoup(page_source, 'html.parser')

    # Price
    e_price = soup.find('span', attrs={'class': 'frfoXM'})
    price = e_price.text

    details = soup.find_all('span', attrs={'data-testid': 'bed-bath-item'})
    # print(details)

    # Num Bed
    beds = details[0].text

    # Num Bath
    baths = details[1].text

    # Area
    area_ft = details[2].text

    # Address
    e_addr = soup.find('div', attrs={'class': 'jCfqsU'})
    addr = e_addr.text

    print(f'{price}, {beds}, {baths}, {area_ft}, {addr}')

def iterate_listings(browser):
    listings = [
        # 'https://www.zillow.com/homedetails/1873-Bonnymede-Dr-Mississauga-ON-L5J-1E2/2064209768_zpid/',
        'https://www.zillow.com/homedetails/81-Hammond-Rd-Mississauga-ON-L5M-2A3/2064206192_zpid/',
        'https://www.zillow.com/homedetails/3050-Erin-Centre-Blvd-69-Mississauga-ON-L5M-0P5/2064197211_zpid/',
        'https://www.zillow.com/homedetails/802-Spinning-Wheel-Cres-Mississauga-ON-L5W-1W4/2064193326_zpid/',
        'https://www.zillow.com/homedetails/128-Breton-Ave-Mississauga-ON-L4Z-4K5/2064193413_zpid/'
    ]

    i = 0
    for link in listings:
        browser.get(link)
        time.sleep(60)
        extract_house_data(browser.page_source, i)
        browser.close()
        browser = st.setup_browser(True, './')

        i += 1
