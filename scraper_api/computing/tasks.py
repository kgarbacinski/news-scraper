from api.scraper import ContentGetter

from .celeryconfig import Config
from celery import Celery, Task
from typing import Dict


class ScrappingTask(Task):
    name = 'scrapping_task'

    def run(self, keyword):
        data: Dict = ContentGetter.get(keyword)
        result: Dict = None

        if all(not len(value) for value in data.values()):
            result = {"message": f"No info found for: {keyword}!"}
        else:
            result = data

        return result

    def on_success(self, retval, task_id, args, kwargs):
        celery_task_id = task_id
        keyword = args[0]
        scrapped_data = list(retval.values())[0]

        print(f"{celery_task_id} | {keyword} | {scrapped_data}")


celery_app = Celery(__name__)
celery_app.config_from_object(Config)
celery_app.register_task(ScrappingTask())
