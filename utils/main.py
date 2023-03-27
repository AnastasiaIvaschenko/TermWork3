import json
from utils.funcs import sorted_dict, client_report

FILE = 'dict.json'


def main(data):
    with open(data, 'r', encoding='utf-8') as f:
        data = json.load(f)
        data = sorted_dict(data)
        for i in range(5):
            print(client_report(data[i]))
            print()

if __name__ == '__main__':
    main(FILE)


'''14.10.2018 Перевод организации
Visa Platinum 7000 79** **** 6361 -> Счет **9638
82771.72 руб.'''