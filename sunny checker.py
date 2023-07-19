import requests
from plyer import *
from bs4 import *

bbc = requests.get("https://www.bbc.co.uk/weather/3530597")
bbc_soup = BeautifulSoup(bbc.text,"html.parser")
find = bbc_soup.find("span",{"class":"wr-time-slot-secondary__weather-type-text gel-pica-bold"})
x = "Sunny" in find.string or "sunny" in find.string
match x:
    case True:
        notification.notify(
    title="Sunny today😁!",
    message="Clean the shoes!",
    app_icon=None,
    timeout=10, 
        )
    case False:
        notification.notify(
    title="Not sunny today😞!",
    message="wait another day!",
    app_icon=None,
    timeout=10, 
        )