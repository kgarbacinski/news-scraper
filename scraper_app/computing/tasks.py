from celery import Celery, Task
from typing import Dict

from scraper.scraper import ContentGetter
from .celeryconfig import Config
from app.history_handler import HistoryHandler

class ScrappingTask(Task):
    name = 'scrapping_task'

    def run(self, keyword):
        data: Dict = ContentGetter.get(keyword)
        result: Dict = None

        if all(not len(value) for value in data.values()):
            result = {"message": f"No info found for this keyword: {keyword}!"}
        else:
            result = data

        return result

    def on_success(self, retval, task_id, args, kwargs):
        task_id = task_id
        keyword = args[0]
        scraped_data = retval

        if 'message' in scraped_data.keys():
            content = scraped_data
        else: 
            content = {
                source: len(articles) 
                for source, articles in scraped_data.get('articles').items()
                }

        handler = HistoryHandler(task_id, keyword, content)
        
        return handler.add_new_record()


celery_app = Celery(__name__)
celery_app.config_from_object(Config)
celery_app.register_task(ScrappingTask())
