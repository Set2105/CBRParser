from Functions import get_data_from_crb
from Classes import Valute
import datetime


def main():
    # getting current date
    date = datetime.datetime.now().date()
    # set last checking day
    target_date = datetime.datetime.now().date() - datetime.timedelta(days=90)

    # Currency dict initialization
    valute_dict = {}

    # getting data from cbr
    while date > target_date:
        print("Getting data from crb on {}".format(date))
        data, checking_date = get_data_from_crb(date)
        date = checking_date

        # adding formated data to dict
        for valute_id in data.keys():
            valute_data = data[valute_id]
            # creating new Currency class if not existing
            if valute_id not in valute_dict.keys():
                valute_dict.update({
                    valute_id:
                        Valute(valute_id, valute_data["name"], valute_data["charcode"], valute_data["numcode"])
                })

            valute = valute_dict[valute_id]
            valute.add_curse(value=valute_data['curs'], date=valute_data["date"])

        date = date - datetime.timedelta(days=1)

    # calculating and print mean values
    print("\nMean valutes value in 90 days ")
    for valute in valute_dict.values():
        print("{:25} - {:25}".format(valute.name, valute.curse_set.get_mean()))

    # calculating max and min values
    max_value_dict = {}
    min_value_dict = {}
    for valute in valute_dict.values():
        value = valute.curse_set.get_max()
        max_value_dict.update({value.value: {"name": valute.name, "date": value.date, "value": value.value}})

        value = valute.curse_set.get_min()
        min_value_dict.update({value.value: {"name": valute.name, "date": value.date, "value": value.value}})

    # print max value
    max_value = max_value_dict[max(max_value_dict.keys())]
    print("Max valute curs: {:25} {} {:20}".format(max_value["name"], max_value["date"], max_value["value"]))

    # print min value
    min_value = min_value_dict[min(min_value_dict.keys())]
    print("Min valute curs: {:25} {} {:20}".format(min_value["name"], min_value["date"], min_value["value"]))


if __name__ == "__main__":
    main()
