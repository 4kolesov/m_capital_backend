from django.db import models


class Calculation(models.Model):
    date = models.DateTimeField(
        verbose_name='Дата расчета',
        auto_now_add=True
    )
    rate = models.DecimalField(
        verbose_name='Курс доллара к биткоину',
        max_digits=50,
        decimal_places=2
    )
    net_assets = models.DecimalField(
        verbose_name='Стоимость чистых активов',
        max_digits=50,
        decimal_places=4
    )
    pnl = models.DecimalField(
        verbose_name='Прибыль / убыток',
        max_digits=50,
        decimal_places=4
    )
    index_pnl = models.DecimalField(
        verbose_name='Отношение чистых активов',
        max_digits=50,
        decimal_places=28
    )

    class Meta:
        verbose_name = 'Расчет'
        verbose_name_plural = 'Расчеты'
        ordering = ('-date',)

    def __str__(self) -> str:
        return (
        f'Дата: {self.date},'
        f'PnL: {self.pnl}, Index PnL: {self.index_pnl}'
        )
