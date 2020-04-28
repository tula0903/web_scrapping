import requests
import bs4


url1 = input("url : ")
data = requests.get(url1)
soup = bs4.BeautifulSoup(data.text, 'html.parser')
#print(soup.prettify())
for para1 in soup.find_all("h3", {"class" : "lister-item-header"}):
    print(para1.text)
