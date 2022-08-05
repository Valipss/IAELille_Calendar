import csv
import time
import requests
from bs4 import BeautifulSoup
from datetime import timedelta, date

f = open('export.csv', 'w')
writer = csv.writer(f)
writer.writerow(['Subject', 'Start Date', 'Start Time', 'End Date', 'End Time', 'All Day Event', 'Description', 'Location', 'Private'])

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

start_date = date(2022, 9, 1)
end_date = date(2022, 9, 2)
for single_date in daterange(start_date, end_date):
    current_date = single_date.strftime("%Y-%m-%d")

    url = 'https://agendaiae.univ-lille.fr/?formation=M1217&date='+current_date
    print('starting scraping on url: '+ url)

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    table = soup.find('table', id='tblcours')
    if (table is not None):
        for body in table.find_all('tbody'):
            rows = body.find_all('tr')
            for row in rows:
                to_write = [None] * 9 
                cells = row.find_all('td')
                to_write[0] = cells[5].text.strip() #Subject
                to_write[1] = current_date
                to_write[2] = cells[0].text.strip() #Start Time
                to_write[3] = current_date
                to_write[4] = cells[1].text.strip() #End Time
                to_write[5] = False #AllDayEvent
                to_write[6] = cells[2].text.strip() #Teacher
                to_write[6] += (' | ' if to_write[6] else '') + cells[3].text.strip() #Group
                to_write[7] = cells[4].text.strip() #Location
                to_write[8] = False #Private
                writer.writerow(to_write)
    time.sleep(0.5)
f.close()