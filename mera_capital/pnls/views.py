from __future__ import annotations
from django.db.models import Sum
from django.shortcuts import render

from pnls.forms import DateForm
from pnls.models import Calculation


def index(request):
    '''
    Генерирует главную страницу с доступным периодом по умолчанию.
    После ввода даты и времени в формы, выводятся данные согласно периоду.
    '''
    pnl_all = Calculation.objects.aggregate(Sum('pnl'))
    start = Calculation.objects.last()
    finish = Calculation.objects.first()
    pnl_index = finish.net_assets / start.net_assets * start.index_pnl
    pnl_percent = (finish.index_pnl / start.index_pnl - 1) * 100
    form = DateForm(request.POST or None, files=request.FILES or None)
    if form.is_valid():
        start_date = form.cleaned_data.get('start_date')
        finish_date = form.cleaned_data.get('finish_date')
        pnl_period = Calculation.objects.filter(
            date__gte=start_date
        ).filter(
            date__lte=finish_date
        ).aggregate(
            Sum('pnl')
        )
        start_period = Calculation.objects.filter(
            date__gte=start_date
        ).filter(
            date__lte=finish_date
        ).last()
        finish_period = Calculation.objects.filter(
            date__gte=start_date
        ).filter(
            date__lte=finish_date
        ).first()
        period_pnl_index = (finish_period.net_assets
                            / start_period.net_assets
                            * start_period.index_pnl)
        period_pnl_percent = (
            (finish_period.index_pnl / start_period.index_pnl - 1) * 100)
        context = {
            'form': form,
            'summ': pnl_period.get('pnl__sum'),
            'pnl_index': period_pnl_index,
            'pnl_percent': period_pnl_percent,
            'start_period': start_date,
            'finish_period': finish_date,
        }
        return render(request, 'pnls/index.html', context)
    else:
        context = {
            'form': form,
            'summ': pnl_all.get('pnl__sum'),
            'pnl_index': pnl_index,
            'pnl_percent': pnl_percent,
            'start_period': start.date,
            'finish_period': finish.date,
        }
        return render(request, 'pnls/index.html', context)
