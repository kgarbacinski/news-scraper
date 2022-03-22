from celery import Celery
import os
from scraper_api.computing.tasks import CustomTask

# celery_app = Celery(__name__)
# celery_app.conf.broker_url = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379")
# celery_app.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND", "redis://localhost:6379")
# celery_app.autodiscover_tasks(packages=['scraper_api.computing.tasks'])

celery_app = Celery('myproject', 
             backend = os.environ.get("CELERY_RESULT_BACKEND", "redis://localhost:6379"),
             broker = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379"))

CustomTask = celery_app.register_task(CustomTask())
