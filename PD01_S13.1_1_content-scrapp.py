import requests
from Utilities.api_resources import imdb_header
from bs4 import BeautifulSoup

action_url = "https://www.imdb.com/find/?s=tt&q=action&ref_=nv_sr_sm"


resp_get = requests.get(url=action_url,
                        headers=imdb_header.headers)

webpage_html_content_obj = BeautifulSoup(resp_get.content,"html.parser")
table = webpage_html_content_obj.find('ul',{"role":"presentation"})


rows = table.findAll('li',{'class':"ipc-metadata-list-summary-item ipc-metadata-list-summary-item--click find-result-item find-title-result"})

# for value_row in rows:
#     title = value_row.find('a',{'role':'button'})
#     print(title.text)

'''
OR
'''

for value_row in rows:
    row_sub1 = value_row.find('div',{'class':'ipc-metadata-list-summary-item__c'})
    row_sub2 = row_sub1.find('div',{'class':'ipc-metadata-list-summary-item__tc'})
    title = row_sub2.find('a',{'role':'button'})


    print(title.text)