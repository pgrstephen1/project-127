from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd
import requests
import csv

# NASA Exoplanet URL
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

# Webdriver
browser = webdriver.Edge("C:/Whitehat_jr/PRO-127-130/msedgedriver.exe")
browser.get(START_URL)

time.sleep(10)

star_data = []

headers = ["name", "distance", "mass", "radius"]

def scrape():
    for i in range(1,5):
        while True:
            time.sleep(2)

            soup = BeautifulSoup(browser.page_source, "html.parser")

            # Check page number    
            current_page_num = int(soup.find_all("input", attrs={"class", "page_num"})[0].get("value"))

            if current_page_num < i:
                browser.find_element(By.XPATH, value='//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
            elif current_page_num > i:
                browser.find_element(By.XPATH, value='//*[@id="primary_column"]/footer/div/div/div/nav/span[1]/a').click()
            else:
                break

        for tr_tag in soup.find_all("tr", attrs={"class", "exoplanet"}):
            td_tags = tr_tag.find_all("tdd")
            temp_list = []
            for index, td_tag in enumerate(td_tags):
                if index == 0:
                    temp_list.append(td_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(td_tag.contents[0])
                    except:
                        temp_list.append("")

            star_data.append(temp_list)

        browser.find_element(By.XPATH, value='//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()

        print("scraping completed")


# Calling Method
scrape()


print(star_data[0:10])

with open("final.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(star_data)