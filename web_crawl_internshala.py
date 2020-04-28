import requests
import bs4

url = "https://www.imdb.com/list/ls025929404/"
data = requests.get(url)
soup = bs4.BeautifulSoup(data.text, 'html.parser')
#print(soup.prettify())

for para in soup.find_all('p'):
    print(para.text)
#for links in  soup.find_all('a'):
 #   link  = links.get('href')
  #  print("https://www.imdb.com/list/ls025929404/" + link[2:len(link)])
       
    
