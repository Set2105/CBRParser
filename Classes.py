import datetime


class Curs:
    """
    Class contains exchange rate of currency on date
    """
    value: float
    date: datetime.date

    def __init__(self, value=None, date: datetime.date = None):
        self.value = value
        self.date = date


class CursSet:
    """
    Class with list of exchanging rates on dates
    """
    curses: list

    def __init__(self):
        self.curses = []

    def add(self, value=None, date: datetime.date = None):
        """
        Adding Curs in Class list
        :param value: float
        :param date: datetime:date
        :return: None
        """
        curse = Curs(value, date)
        if curse not in self.curses:
            self.curses.append(curse)

    def get_max(self):
        """
        Find max Exchanging rate
        :return: Curs class
        """
        try:
            result = self.curses[0]
            for curs in self.curses:
                if result.value < curs.value:
                    result = curs
            return result
        except Exception as e:
            print(e.args)
            return None

    def get_min(self):
        """
        Find min Exchanging rate
        :return: Curs class
        """
        try:
            result = self.curses[0]
            for curs in self.curses:
                if result.value > curs.value:
                    result = curs
            return result
        except Exception as e:
            print(e.args)
            return None

    def get_mean(self):
        """
        Find mean value of Exchanging rate
        :return: float
        """
        result = 0
        i = 0
        for curs in self.curses:
            i += 1
            result += curs.value
        try:
            return result / i
        except Exception as e:
            print(e.args)
            return None


class Valute:
    """
    Class containing information about currency
    """
    id: str
    name: str
    charcode: str
    numcode: str
    curse_set: CursSet

    def __init__(self, val_id, name, charcode, numcode):
        self.id = val_id
        self.name = name
        self.charcode = charcode
        self.numcode = numcode
        self.curse_set = CursSet()

    def add_curse(self, value, date):
        """
        Add exchanging rate to exchanging rate list
        :param value: float
        :param date: datetime.date
        :return:
        """
        self.curse_set.add(value, date)




