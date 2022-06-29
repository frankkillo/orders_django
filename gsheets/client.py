import requests
from xml.etree import ElementTree
import gspread
import datetime
from pprint import pprint
import json


class GsheetsOrder:
    """A simple class to represent order info data 
    coming back from Google Sheets API
    and transform to Python types."""
    
    def __init__(self, data):
        self.data = data

    @property
    def id(self):
        return self.data['№']

    @property
    def order_id(self):
        return self.data['заказ №']

    @property
    def usd_price(self):
        return self.data['стоимость,$']

    @property
    def rub_price(self):
        return self.data['ruble_price']

    @property
    def expiration(self):
        try:
            date = list(map(int, self.data['срок поставки'].split('.')))
            return datetime.date(year=date[2], month=date[1], day=date[0])
        except:
            return datetime.date(2022, 1, 1)


class GsheetsClient:
    def __init__(self, servise_account):
        self.servise_account = servise_account

    def get_records(self):
        """
            Func get all records from table with name and wokrsheet
        """
        sa = gspread.service_account_from_dict(self.servise_account)
        sh = sa.open('TestSheet')
        wks = sh.worksheet('Лист1')
    
        return wks.get_all_records()

    def get_ruble_rate(self):
        """
            Func get actual price of USD/RUB from Central Bank of Russia.
        """
        response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
        root = ElementTree.fromstring(response.content)
        ruble_rate = root.find(".//*[@ID='R01235']/Value").text

        return ruble_rate

    def records(self):
        rub_rate = self.get_ruble_rate()

        for record in self.get_records():
            try:
                id = int(record['№'])
                order_id = int(record['заказ №'])
                usd_price = float(record['стоимость,$'])
                expiration = record['срок поставки']
            except:
                continue
            if id and order_id and usd_price and expiration:
                rub = float(record['стоимость,$']) * float(rub_rate.replace(',', '.'))
                record['ruble_price'] = round(rub, 2)
                yield GsheetsOrder(record)