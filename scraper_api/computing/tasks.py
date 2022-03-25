from api.scraper import ContentGetter

from .celeryconfig import Config
from celery import Celery
from typing import Dict

celery_app = Celery(__name__)
celery_app.config_from_object(Config)
celery_app.autodiscover_tasks()

# class CustomTask(Task):
#     def run(self, keyword):
        # data: Dict = ContentGetter.get(keyword)
        # result: Dict = None

        # if all(not len(value) for value in data.values()):
        #     result = {"message": f"No info found for: {keyword}!"}
        # else:
        #     result = data

        # return result

#     def on_success(self, retval, task_id, args, kwargs):
#         print ("Task id: ", task_id)
#         print ("retval ", retval)    
#         print ("Args ", args)
#         print ("kwargs: ", kwargs)

@celery_app.task(name="scraper_task")
def scraper_task(keyword):
    data: Dict = ContentGetter.get(keyword)
    result: Dict = None

    if all(not len(value) for value in data.values()):
        result = {f"No info found for: {keyword}!"}
    else:
        result = data

    return result

