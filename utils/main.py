import json
from funcs import sorted_dict, client_report

'''14.10.2018 Перевод организации
Visa Platinum 7000 79** **** 6361 -> Счет **9638
82771.72 руб.'''

FILE = "dict.json"


def main():
    with open(FILE, 'r', encoding='utf-8') as f:
        dict_ = json.load(f)
        dict_ = sorted_dict(dict_)
        for i in range(5):
            print(client_report(dict_[i]))


if __name__ == '__main__':
    main()
