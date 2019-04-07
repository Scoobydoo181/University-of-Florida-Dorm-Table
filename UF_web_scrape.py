import requests
from bs4 import BeautifulSoup
import pandas as p


def get_html(url):
    """Gets raw html from a url and returns a BeautifulSoup object"""
    r = requests.get(url)
    html = r.content
    return BeautifulSoup(html, 'html.parser')


def parse_for_table(html):
    """Parses BeautifulSoup html object for a table containing dorm prices and room types"""
    first_column = []
    second_column = []
    third_column = []

    last_hall_name = ''

    for td in html.select('td'):
        if td['class'][0] == "column-1":
            if td.text:
                if 'village' or 'Village' in td.text:
                    continue
                    
                first_column.append(td.text)
                last_hall_name = td.text
            else:
                first_column.append(last_hall_name)

        elif td['class'][0] == 'column-2':
            second_column.append(td.text)

        elif td['class'][0] == 'column-3':
            third_column.append(td.text)
                
    table = {
        'Halls': first_column,
        'Room Types': second_column,
        'Prices': third_column
        }

    return p.DataFrame(table)

