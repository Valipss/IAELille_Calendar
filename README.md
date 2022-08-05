# IAELille_Calendar
> Make sure to have BeautifulSoup4 installed before.
> ```bash
> pip3 install BeautifulSoup4
>```
Start the script with python3

To select dates, change these two lines :
```python
start_date = date(2022, 9, 1)
end_date = date(2023, 5, 26)
```
the script makes 2 requests a second to prevent over-requesting the site.
If you are from another promotion than M1127, just change the URL *`?formation=`*
```python
url = 'https://agendaiae.univ-lille.fr/?formation=M1217&date='+current_date
```
Once the sript has finished is job, you'll get a fulfilled .csv to import in __Google Calendar__.
