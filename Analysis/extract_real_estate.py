import os
import pandas as pd
import Scrape.scrape_tools as st
import Scrape.zillow as zi

download_path = os.getcwd() + './Data/'

view_browser = True
browser = st.setup_browser(view_browser, download_path)
print(type(browser))
# zi.zillow_housing(browser)
zi.iterate_listings(browser)
