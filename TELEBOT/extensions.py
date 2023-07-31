import requests
import json
from config import keys


class APIException(Exception):
    pass


class GetPrice:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}!')
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {quote}')
        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Неудалось обработать валюту {base}')
        try:
            sum = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {sum}')

        r = requests.get(
            f'https://v6.exchangerate-api.com/v6/0dd5ef33d8841058544ab992/pair/{base_ticker}/{quote_ticker}')
        total_base = json.loads(r.content)['conversion_rate']

        return total_base
