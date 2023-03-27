from utils.funcs import sorted_dict, formatted_date, hidden_acc_number, client_report
import pytest


def test_sorted_dict():
    data = [{
    "id": 179194306,
    "state": "EXECUTED",
    "date": "2019-05-19T12:51:49.023880"
    },
  {
    "id": 27192367,
    "state": "CANCELED",
    "date": "2018-12-24T20:16:18.819037"
    },
  {
    "id": 957763565,
    "state": "EXECUTED",
    "date": "2019-01-05T00:52:30.108534"
  }]
    result = [{
    "id": 179194306,
    "state": "EXECUTED",
    "date": "2019-05-19T12:51:49.023880"
    },
   {
    "id": 957763565,
    "state": "EXECUTED",
    "date": "2019-01-05T00:52:30.108534"
  }]
    assert sorted_dict(data) == result


def test_form_date():
    assert formatted_date("2019-08-26T10:50:58.294041") == '26.08.2019'
    assert formatted_date("2018-12-24T20:16:18.819037") == '24.12.2018'
    assert formatted_date("2019-07-15T11:47:40.496961") == '15.07.2019'


def test_hidden_num():
    assert hidden_acc_number("Счет 26406253703545413262") == "Счет **3262"
    assert hidden_acc_number("Maestro 1308795367077170") == "Maestro 1308 79** **** 7170"
    assert hidden_acc_number("Visa Gold 3654412434951162") == "Visa Gold 3654 41** **** 1162"


@pytest.mark.parametrize('data, result', [({
    "id": 667307132,
    "state": "EXECUTED",
    "date": "2019-07-13T18:51:29.313309",
    "operationAmount": {
      "amount": "97853.86",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод с карты на счет",
    "from": "Maestro 1308795367077170",
    "to": "Счет 96527012349577388612"
  }, '13.07.2019 Перевод с карты на счет\nMaestro 1308 79** **** 7170 -> Счет **8612\n97853.86 руб.'),
    ({
    "id": 893507143,
    "state": "EXECUTED",
    "date": "2018-02-03T07:16:28.366141",
    "operationAmount": {
      "amount": "90297.21",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Открытие вклада",
    "to": "Счет 37653295304860108767"
  }, '03.02.2018 Открытие вклада\nСчет **8767\n90297.21 руб.')])



def test_client_report(data, result):
    assert client_report(data) == result
