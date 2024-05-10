# https://www.cbr.ru/statistics/ddkp/infl/

# # Find the table with the key rate
# table = soup.find('table', {'class': 'data'})

import requests as rq
import pandas as pd
from bs4 import BeautifulSoup as bs

url = 'https://www.cbr.ru/statistics/ddkp/infl/'
response = rq.get(url)
soup = bs(response.text, 'html.parser')
table = soup.find('table', {'class': 'data'})
data = pd.DataFrame(columns=['Date', 'Key rate, % per year', 'Inflation, % year/year', 'Inflation target, %'])
for row in table.find_all('tr'):
    cells = row.find_all('td')
    if len(cells) == 4:
        date = cells[0].text
        rate = cells[1].text
        inflation = cells[2].text
        inflations_purpose = cells[3].text
        data = data._append({'Date': date, 'Key rate, % per year': rate, 'Inflation, % year/year': inflation, 'Inflation target, %': inflations_purpose}, 
                             ignore_index = True)
print(data.to_string(index=False))
