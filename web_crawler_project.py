import requests
import bs4
import pandas as pd
import argparse

url1 = input("url1 : ")
data1 = requests.get(url1)
soup = bs4.BeautifulSoup(data1.text, 'html.parser')
#print(soup.prettify())
for para1 in soup.find_all("h3", {"class" : "lister-item-header"}):
    celeb_name = para1.text.replace("\n","")
    print(celeb_name)
    

# url2 = input("url2 : ")
# data2 = requests.get(url2)
# soup = bs4.BeautifulSoup(data2.text, 'html.parser')
# #print(soup.prettify())
# for para2 in soup.find_all("h3", {"class" : "lister-item-header"}):
#     row2 = [para2.text]
#   
#  


main

    
 







