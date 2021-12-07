import requests
from bs4 import BeautifulSoup as bs
import datetime


def date_to_str(date: datetime.date):
    """
    Format date from datetime class to string

    :param date: datetime.date
    :return: string
    """
    return "{:02d}/{:02d}/{:02d}".format(date.day, date.month, date.year)


def str_to_date(date: str):
    """
    Format date from string class to datetime

    :param date: string
    :return: datetime.date
    """
    date = date.split('.')
    return datetime.date(day=int(date[0]), month=int(date[1]), year=int(date[2]))


def get_xml_from_crb_api(date):
    """
    Getting xml document on current date from cbr.ru

    :param date: datetime.date
    :return: BeautifulSoup object
    """
    request = requests.get("https://www.cbr.ru/scripts/XML_daily_eng.asp?date_req={}".format(date_to_str(date)))
    return bs(request.text, "lxml")


def format_xml_to_dict(bs_xml):
    """
    Format xml doc to data dict and date from cbr

    :param date: BeautifulSoup object
    :return: dict, date
    """
    result = {}

    date = str_to_date(bs_xml.find("valcurs").get("date"))

    valutes = bs_xml.find_all("valute")

    for valute in valutes:
        val_id = valute.get("id")
        numcode = valute.find("numcode").text
        charcode = valute.find("charcode").text
        nominal = valute.find("nominal").text
        name = valute.find("name").text
        value = valute.find("value").text

        curs = float(value.replace(",", ".")) / float(nominal)

        result.update({val_id: {"numcode": numcode, "charcode": charcode, "name": name, "curs": curs, "date": date}})

    return result, date


def get_data_from_crb(date: datetime.date):
    """
    Getting data dict on current date from cbr
    :param date: datetime.date
    :return: dict
    """
    return format_xml_to_dict(get_xml_from_crb_api(date))
