from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def zillow_housing(browser):
    print('Accessing Zillow')

    browser.get('https://www.zillow.com/homes/Mississauga,-ON_rb/')

    # Collect all housing links
    page_html = browser.page_source
    p_soup = BeautifulSoup(page_html, 'html.parser') 

    links = p_soup.find_all('a', attrs={'class': 'list-card-link'})
    print(len(links))
    browser.find_element(By.XPATH, "//*[@title='Next page']").click()




    # Iterate through links to get housing data
