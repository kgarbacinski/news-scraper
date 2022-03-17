import os
from celery import Celery
from celery.utils.log import get_task_logger

from api.scraper import ContentGetter

celery = Celery(__name__)
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379")
celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND", "redis://localhost:6379")


celery_log = get_task_logger(__name__)

@celery.task(name='get_response')
def get_response(keyword: str):
    data = ContentGetter.get(keyword)
    result = None

    if all(not len(value) for value in data.values()):
        result = {"message": f"No info found for: {keyword}!"}
    else:
        result = data

    return result


