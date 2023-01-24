from decimal import Decimal

from mera_capital.celery import app
from .models import Calculation
from .services import get_token, get_balance, get_dollar_rate


def previous_calc():
    '''Получаение последнего расчета из базы данных.'''
    try:
        return Calculation.objects.latest('id')
    except Calculation.DoesNotExist:
        return None

@app.task
def calculation():
    '''
    Расчет Pnl, Index PnL, курса доллара, активов каждые 10 секунд.
    Сохранение в базу.
    '''
    previous_calculation = previous_calc()
    rate = get_dollar_rate()
    balance = get_balance()
    net_assets = Decimal(rate * balance)
    if previous_calculation:
        start_assets = previous_calculation.net_assets
        pnl = net_assets - start_assets
        index_pnl = net_assets / start_assets * previous_calculation.index_pnl
    else:
        pnl = 0
        index_pnl = 1
    Calculation.objects.create(
        rate=rate,
        net_assets=net_assets,
        pnl=pnl,
        index_pnl=index_pnl,
    )

@app.task
def update_token():
    '''Обновление токена каждые 890 секунд.'''
    with open('./.env', 'w', encoding='utf-8') as file:
        token = get_token()
        print(f"TOKEN='{token}'", file=file)
