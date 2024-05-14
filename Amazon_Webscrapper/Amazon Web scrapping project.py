import pandas as pd 
import requests as rq
from bs4 import BeautifulSoup as bs
import time
import datetime
import smtplib

url = 'https://www.amazon.de/Python-Crash-Course-Eric-Matthes/dp/1718502702/ref=sr_1_1?__mk_de_DE=ÅMÅŽÕÑ&crid=CNHXKCTHT4S8&dib=eyJ2IjoiMSJ9.q4BJTBL3FeISqAh0xVPR-0xFA5rSmQ2wzH_kdV6K5R-PC1MjD4TksVdjcBPJdATditnxxTQgKWeysM7k4FC7TUJJmz-0v205c915uQL_FdA4HLUo6CYzk4QhqPrtRBkG_cLmUEE4EPIFy9ZHljZT1sLrL16TkrE_38a6D3pR5pT9OUSNoND90QsSoZwFdrlPQN-DT33zs7AphYxj37KS5Pj-ts9yVWt3DM-TomvLzVM.1hInZ5WDCh_m3GMweMfn0qqZg51uvcIo5Z6rh9Tya_U&dib_tag=se&keywords=python+books&qid=1712079436&sprefix=python+books%2Caps%2C129&sr=8-1'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 YaBrowser/24.1.0.0 Safari/537.36', 'Accept-Encoding' : 'gzip, deflate, br', 'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'Dnt' : '1', 'Connection' : 'close', 'Upgrade-Insecure-Requests' : '1'}
page = rq.get(url, headers=headers)
soup = bs(page.content, 'html.parser')
soup_pro = bs(soup.prettify(),'html.parser')
title = soup_pro.find(id='productTitle').get_text()
title = title.strip()
price = soup_pro.find(id='corePriceDisplay_desktop_feature_div').text
price = price.strip()[:5]
rate = soup_pro.find(id='acrPopover',).text
rate = rate.strip()[:3]
today = datetime.date.today()
print(title)
print(price)
print(rate)
print(today)

import csv
header = ['Title', 'Price', 'Rate', 'Date']
data = [title, price, rate, today]

with open('AmazonWebscrapper.csv', 'w', newline = '', encoding = 'UTF8') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(header)
    writer.writerow(data)

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
df = pd.read_csv(r'C:\Users\79607\Documents\Python\tasks\AmazonWebscrapper.csv')
print(df)

with open('AmazonWebscrapper.csv', 'w', newline = '', encoding = 'UTF8') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(data)

def send_mail():
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    server.login('79607908772@gmail.com', 'XXXXXXXXXX')

    subject = 'The Book is below 30 euro!'
    body = 'now is your chance'

    msg = f"subject: {subject}\n\n{body}"
    
    server.sendmail('79607908772k@gmail.com'. msg)

def check():
    url = 'https://www.amazon.de/Python-Crash-Course-Eric-Matthes/dp/1718502702/ref=sr_1_1?__mk_de_DE=ÅMÅŽÕÑ&crid=CNHXKCTHT4S8&dib=eyJ2IjoiMSJ9.q4BJTBL3FeISqAh0xVPR-0xFA5rSmQ2wzH_kdV6K5R-PC1MjD4TksVdjcBPJdATditnxxTQgKWeysM7k4FC7TUJJmz-0v205c915uQL_FdA4HLUo6CYzk4QhqPrtRBkG_cLmUEE4EPIFy9ZHljZT1sLrL16TkrE_38a6D3pR5pT9OUSNoND90QsSoZwFdrlPQN-DT33zs7AphYxj37KS5Pj-ts9yVWt3DM-TomvLzVM.1hInZ5WDCh_m3GMweMfn0qqZg51uvcIo5Z6rh9Tya_U&dib_tag=se&keywords=python+books&qid=1712079436&sprefix=python+books%2Caps%2C129&sr=8-1'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 YaBrowser/24.1.0.0 Safari/537.36', 'Accept-Encoding' : 'gzip, deflate, br', 'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'Dnt' : '1', 'Connection' : 'close', 'Upgrade-Insecure-Requests' : '1'}
    page = rq.get(url, headers=headers)
    soup = bs(page.content, 'html.parser')
    soup_pro = bs(soup.prettify(),'html.parser')
    title = soup_pro.find(id='productTitle').get_text()
    title = title.strip()
    price = soup_pro.find(id='corePriceDisplay_desktop_feature_div').text
    price = price.strip()[:5]
    rate = soup_pro.find(id='acrPopover',).text
    rate = rate.strip()[:3]

    import datetime
    today = datetime.date.today()

    import csv
    header = ['Title','Price','Rate', 'Date']
    data = [title, price, rate, today]

    with open('AmazonWebscrapper.csv', 'w', newline = '', encoding = 'UTF8') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(header)
        writer.writerow(data)

    price = price.strip()[:2]
    price1 = int(price)
    if (price1 < 30):
        send_mail()

while(True):
    check()
    time.sleep(86400)

df = pd.read_csv(r'C:\Users\79607\Documents\Python\tasks\AmazonWebscrapper.csv')
print(df)