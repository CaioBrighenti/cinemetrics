# source: https://kite.com/python/examples/4420/beautifulsoup-parse-an-html-table-and-write-to-a-csv
from bs4 import BeautifulSoup
import csv
import requests
import os, time
import selenium
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from bs4 import BeautifulSoup
import re
import csv
from tqdm import tqdm

# start browser crawler
browser = webdriver.Firefox()

# page url
url = 'http://www.cinemetrics.lv/satltdb.php'

 # navigate to page
browser.get(url)

# find table
data_table = browser.find_elements_by_class_name('table')[2]

# grab html
html = browser.page_source
soup = BeautifulSoup(html)
table = soup.find("table")

output_rows = []
for table_row in table.findAll('tr'):
    columns = table_row.findAll('td')
    output_row = []
    for column in columns:
        output_row.append(column.text)
    output_rows.append(output_row)
    
with open('cinemetrics.csv', 'w', encoding="utf-8") as csvfile:
    for line in tqdm(output_rows):
        if line == []:
            continue
        line.pop()
        csvfile.write("\t".join(line))
        csvfile.write("\n")
