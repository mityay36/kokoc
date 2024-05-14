import requests
from django.core.management.base import BaseCommand

from currency.models import Currency, Handbook


class Command(BaseCommand):
    help = 'Загрузка данных курсов со страницы'

    def handle(self, *args, **kwargs):
        ans = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
        date = ans['Date'][0:10]
        currencies = ans['Valute']

        for currency in currencies:
            instance = currencies[currency]
            try:
                obj, created = Currency.objects.get_or_create(
                    char_code=instance['CharCode'], name=instance['Name']
                )
                Handbook.objects.get_or_create(
                    currency=obj, date=date, value=float(instance['Value'])
                )
            except Exception as error:
                print(f'Ошибка заполнения базы данных. {error}')
        print('Данные загружены')
