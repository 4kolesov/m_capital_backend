from django.shortcuts import render
from django.http import HttpResponse
from .forms import DateForm
from .models import Calculation
from django.db.models import Max, Min, Sum


# def index():
#     '''Вывод PnL, PnL_%, Index PnL и Period на отдельную страницу.'''
#     pass


def index(request):
    pnl_all = Calculation.objects.aggregate(Sum('pnl'))
    start = Calculation.objects.last()
    finish = Calculation.objects.first()
    pnl_index = finish.net_assets / start.net_assets * start.index_pnl
    pnl_percent = (finish.index_pnl / start.index_pnl - 1) * 100
    form = DateForm()
    context = {
        'form': form,
        'summ': pnl_all,
        'pnl_index': pnl_index,
        'pnl_percent': pnl_percent,
        'start_period': start.date,
        'finish_period': finish.date
    }
    return render(request, 'pnls/index.html', context)
