#scrapp titles with genre action
from bs4 import BeautifulSoup
import requests
from Utilities.api_resources import imdb_header


title_list = []
base_url = 'https://www.imdb.com'
top250_url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"

resp_get = requests.get(url=top250_url,
                        headers=imdb_header.headers)

html_webcontent = BeautifulSoup(resp_get.content,'html.parser')
table = html_webcontent.find('ul',{'role':'presentation'})

rows = table.findAll('li',{'class':'ipc-metadata-list-summary-item sc-bca49391-0 eypSaE cli-parent'})
for value_row in rows:
    title = value_row.find('h3', {'class': 'ipc-title__text'})
    suburl_attr = value_row.find('a',{'class':'ipc-title-link-wrapper'})
    suburl = suburl_attr['href']
    url = base_url+suburl

    requests.get(url)



    title_list.append(title.text)


'''
unfinished code --- 

'''