import gspread
from oauth2client import client

from oauth2client.service_account import ServiceAccountCredentials

from pprint import pprint
import requests
#p_img_url
#tlc_n,rating_info,p_img_url,p_brand,w,p_desc,absolute_url
scope=["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds=ServiceAccountCredentials.from_json_keyfile_name("cred.json",scope)
client=gspread.authorize(creds)
sheet=client.open("Bigbasket").sheet1
data=sheet.get_all_records()
#print(data)
#insertRow=["hi","jjj","jj","hi","jjj","jjj","jj","hi","jjj","jj"]
#sheet.insert_cols(insertRow,0)
from bs4 import BeautifulSoup as soup
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}
r = requests.get('https://www.bigbasket.com/custompage/sysgenpd/?type=pc&slug=potato-onion-tomato',headers=header)
#r = requests.get('https://www.bigbasket.com/cl/foodgrains-oil-masala/?nc=nb',headers=header)

bsobj = soup(r.content,features="html.parser")
import json
comp = json.loads(r.text)
comp=comp['tab_info']
a=[]
for i in comp[0]['product_info']['products']:
    a.append(i)


name = []
mrp = []
sp = []
categories=[]
imageurl=[]
brand=[]
url_prod=[]
prod_name=[]
skuid=[]
for j in a:
  skuid.append(j['rating_info']['sku_id'])
  name.append(j['p_desc'])
  mrp.append(j['mrp'])
  sp.append(j['sp'])
  categories.append(j['tlc_n'])
  imageurl.append(j['p_img_url'])
  brand.append(j['p_brand'])
  url_prod.append("https://www.bigbasket.com/"+j['absolute_url'])
  prod_name.append(j['p_desc'])


"""
print(name[:10])
print(mrp[:10])
print(sp[:10])
print(categories[:10])
print(imageurl[:10])
print(brand[:10])
print(url_prod[:10])
print(prod_name[:10])
print(skuid[:10])"""

"""insertRow=["vivek","jjj","jj","hi","jjj","jjj","jj","hi","jjj","jj"]
sheet.insert_row(insertRow,4)"""
for i in range(10):
  insertRow=[None,None,categories[i],None,skuid[i],imageurl[i],
  brand[i],prod_name[i],None,mrp[i],sp[i],url_prod[i],"YES","NO"]
  sheet.insert_row(insertRow,i+2)
