from django.db import models


class Currency(models.Model):
    char_code = models.CharField(
        max_length=128, verbose_name='Сокращенное название'
    )
    name = models.CharField(max_length=128, verbose_name='Название валюты')

    class Meta:
        ordering = ['name', ]
        verbose_name = 'Валюта'
        verbose_name_plural = 'Валюты'

    def __str__(self):
        return self.name


class Handbook(models.Model):
    currency = models.ForeignKey(
        Currency, on_delete=models.CASCADE,
        related_name='currency', verbose_name='Валюта'
    )
    date = models.DateField('Дата')
    value = models.DecimalField('Стоимость', decimal_places=2, max_digits=10
)

    class Meta:
        ordering = ['-date', ]
        verbose_name = 'Курса валюты'
        verbose_name_plural = 'Курсы валют'
        constraints = [
            models.UniqueConstraint(
                fields=('currency', 'date'),
                name='unique_object_of_currency_on_date'
            )
        ]

    def __str__(self):
        return f'{self.currency} {self.date}'
