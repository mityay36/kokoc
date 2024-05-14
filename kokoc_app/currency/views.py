from django.shortcuts import render

from .models import Handbook


def currency_rates(request):
    # Получаем список всех доступных дат
    dates = Handbook.objects.values_list(
        'date', flat=True
    ).distinct().order_by('-date')

    # Проверяем, была ли отправлена форма с выбранной датой
    selected_date = request.GET.get('date')
    if selected_date:
        # Получаем все курсы валют на выбранную дату
        currency_rates = Handbook.objects.filter(date=selected_date)
    else:
        # Если форма не отправлена, выводим курсы на последнюю доступную дату
        currency_rates = Handbook.objects.filter(date=dates.first())

    return render(request, 'currency_rates.html',
                  {
                      'currency_rates': currency_rates,
                      'dates': dates,
                      'selected_date': selected_date
                  })
