def sorted_dict(data): #data: dict.json
    dict = []
    for item in data:
        if item.get('state') == 'EXECUTED':
            dict.append(item)
    dict = sorted(dict, key=lambda dt: dt.get('date'), reverse=True)
    return dict


def formatted_date(data):  #data: "2019-08-26T10:50:58.294041"
    dt = data[:10].split('-')
    dt.reverse()
    dt = '.'.join(dt)

    return dt


def hidden_acc_number(data): #data: 'MasterCard 7158300734726758'
    dt = data.split(' ')
    if dt[0] == 'Счет':
        return dt[0] + ' **' + dt[-1][-4:]
    elif dt[0] != 'Счет':
        return ' '.join(dt[:-1]) + ' ' + dt[-1][:4] + ' ' + dt[-1][4:6] + '** **** ' + dt[-1][-4:]

#print(hidden_acc_number('MasterCard 7158300734726758'))

'''14.10.2018 Перевод организации
Visa Platinum 7000 79** **** 6361 -> Счет **9638
82771.72 руб.'''

def client_report(data): #data: {"id": 441945886,"state": "EXECUTED","date": "2019-08-26T10:50:58.294041",
                         #"operationAmount": {"amount": "31957.58","currency": {"name": "руб.","code": "RUB"}
    date_ = formatted_date(data['date'])
    description_ = data['description']
    from_ = hidden_acc_number(data['from']) + ' -> ' if data.get('from') else ''
    to_ = hidden_acc_number(data['to']) if data.get('to') else ''
    amount_ = data['operationAmount'].get('amount')
    currency_ = data.get('operationAmount').get('currency').get('name')

    return(f'{date_} {description_}\n{from_}{to_}\n{amount_} {currency_}')