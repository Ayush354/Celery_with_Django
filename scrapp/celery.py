from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scrapp.settings')
app = Celery('scrapp')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
app.conf.broker_connection_retry_on_startup = True

app.conf.beat_schedule = {
    'scrape-every-day': {
        'task': 'scrapp.tasks.scrape_proxy',
        'schedule': crontab(hour=0, minute=0),  # run daily at midnight
    },
}
