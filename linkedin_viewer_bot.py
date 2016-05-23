from selenium import webdriver
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from bs4 import BeautifulSoup
import re
import getpass

email = input("Enter your account email: ")
password = getpass.getpass("Enter your account password: ")
no_of_profiles = input("Enter how many LinkedIn profiles you wish to view")

def scraper():
    # Scrape page
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    page_urls = []
    for url in soup.find_all('a'):
        page_urls.append(str(url.get('href')))
    return page_urls


i = 20
page_max = round(no_of_profiles/10) + i

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()

# Navigate to LinkedIn home page and log in
try:
    driver.get("https://www.linkedin.com")
    email_form = driver.find_element_by_id("login-email")
    email_form.send_keys(email)
    password_form = driver.find_element_by_id("login-password")
    password_form.send_keys(password)
    password_form.submit()
except:
    print("Error logging in")

# Navigate to search page
search_box = driver.find_element_by_id("main-search-box")
search_box.submit()

# Get search page urls
page_urls = scraper()
for url in page_urls:
    if "page_num=2" in url:
        search_snippet = url[:-1]

# Scrape user profile urls from search

profile_urls_storage = []
while i <= page_max:
    search_page_url = "https://www.linkedin.com" + search_snippet + str(i)
    driver.get(search_page_url)
    i += 1
    time.sleep(5)
    urls_on_search_page = scraper()
    for url in urls_on_search_page:
        if ("view?id=ADEAAA" in url) and ("vsrp_people_res_name" in url): #Potentially something wrong here - not picking up all profiles
            profile_urls_storage.append(url)
# print(profile_urls_storage)

num_profiles_visited = 0
for url in profile_urls_storage:
    driver.get(url)
    time.sleep(5)
    num_profiles_visited += 1

print("Visited", num_profiles_visited, "profiles")
driver.quit()

    # profile_urls = soup.find("div", attrs={"id":"results-container"})
