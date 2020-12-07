import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
from celery.schedules import crontab
from django.core.mail import send_mail

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")

app = Celery("myproject")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def test_user_count(self):
    from myproject.users.models import User
    count = User.objects.count()
    send_mail('testing', 'testing mail', 'adhi.viki@gmail.com', ['vikas@madhuinfotech.com'])
    print(count, 'count')
    return count

# @app.on_after_configure.connect()
# def set_up_periodic_tasks(sender, **kwargs):
#     sender.add_periodic_task(crontab(minute=1), test_user_count(), )
