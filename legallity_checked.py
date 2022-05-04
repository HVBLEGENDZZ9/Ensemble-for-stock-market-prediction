#code to check if website allows scrapping
import requests

from bs4 import BeautifulSoup 

r=requests.get("https://www.moneycontrol.com/india/stockpricequote/steel-large/tatasteel/TIS")

r.status_code