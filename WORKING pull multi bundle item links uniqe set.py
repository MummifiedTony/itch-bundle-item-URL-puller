import time
from selenium import webdriver
from bs4 import BeautifulSoup

# List of URLs for the different pages
bundle_urls = [
    "https://itch.io/b/520/bundle-for-racial-justice-and-equality",
    "https://itch.io/b/902/indie-bundle-for-palestinian-aid",
    "https://itch.io/b/1314/the-ttrpg-community-stands-with-ukraine-bundle",
    "https://itch.io/b/1308/ttrpgs-for-trans-rights-in-texas",
    "https://itch.io/b/1316/bundle-for-ukraine",
    "https://itch.io/b/1375/ttrpgs-for-reproductive-rights",
    "https://itch.io/b/1405/queer-games-bundle-2022-pay-what-you-can-edition",
    "https://itch.io/b/1753/ttrpgs-for-trans-rights-in-florida",
    "https://itch.io/b/1805/trkiye-syria-earthquake-relief-mega-bundle",
    # Add more URLs for additional pages
]

# Web scrapper for infinite scrolling page
driver = webdriver.Chrome(executable_path=r"E:\Chromedriver\chromedriver_win32_chrome83\chromedriver.exe")

all_item_links = set()  # Set to store all item links

for url in bundle_urls:
    driver.get(url)
    time.sleep(2)  # Allow 2 seconds for the web page to open

    # Scroll to the bottom of the page
    scroll_pause_time = 1
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(scroll_pause_time)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    # Extract the item links
    soup = BeautifulSoup(driver.page_source, "html.parser")
    item_links = set()  # Set to store item links for the current bundle
    for item in soup.find_all("a", class_="title"):
        item_links.add(item["href"])

    all_item_links.update(item_links)  # Add item links to the set of all item links

driver.quit()

# Save the unique item links to a plain text document
with open("unique_item_links.txt", "w", encoding="utf-8") as file:
    for link in all_item_links:
        file.write(link + "\n")