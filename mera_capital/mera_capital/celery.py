import os

from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mera_capital.settings')

app = Celery('mera_capital')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
app.conf.beat_schedule = {
    'create_calculation': {
        'task': 'pnls.tasks.calculation',
        "schedule": 30,
    },
    'update_token': {
        'task': 'pnls.tasks.update_token',
        "schedule": 50,
    }
}
