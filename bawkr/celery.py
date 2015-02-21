from __future__ import absolute_import

import os

from celery import Celery
from bawkr.models import Bawk

from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'realtime_demo.settings')

app = Celery('proj')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def save_bawk(self, user, message):
    Bawk.objects.create(username=user, message=message)