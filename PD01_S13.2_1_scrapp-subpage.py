import requests
from Utilities.api_resources import imdb_header
from bs4 import BeautifulSoup

action_url = "https://www.imdb.com/find/?s=tt&q=action&ref_=nv_sr_sm"
actionExactMatchUrl = "https://www.imdb.com/find/?q=action&s=tt&exact=true&ref_=fn_tt_ex"

resp_get = requests.get(url=action_url,
                        headers=imdb_header.headers)

#resp_get = requests.get(url=actionExactMatchUrl,
#                        headers=imdb_header.headers)

htmlWebContent = BeautifulSoup(resp_get.content,'html.parser')

table = htmlWebContent.find('ul',{"role":"presentation"})

rows = table.findAll('li',{"class":"ipc-metadata-list-summary-item ipc-metadata-list-summary-item--click find-result-item find-title-result"})

for value_row in rows:
    subrow1 = value_row.find('div',{'class':"ipc-metadata-list-summary-item__c"})
    subrow2 = subrow1.find('div',{'class':'ipc-metadata-list-summary-item__tc'})
    subrow3 = subrow2.find('a',{'role':'button'})
    print(subrow3.text,end='    ')
    subUrl = subrow3['href']

    base_url = "https://www.imdb.com"
    subpage_address = base_url+subUrl
    subpage_resp_get = requests.get(url=subpage_address,
                 headers=imdb_header.headers)

    subpage_htmlcontent = BeautifulSoup(subpage_resp_get.content,'html.parser')
    para_about = subpage_htmlcontent.find('p', {'class': "sc-466bb6c-3 llCpwq"})
    try:
        if para_about:
            about_data = para_about.find('span',{"role":"presentation"})
            print(about_data.text)
    except Exception as e:
        print(e)
