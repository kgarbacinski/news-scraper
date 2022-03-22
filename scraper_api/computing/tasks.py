from time import sleep
from celery import shared_task
from celery.app.task import Task
from typing import Dict

from api.scraper import ContentGetter

class CustomTask(Task):
    def run(self, keyword):
        data: Dict = ContentGetter.get(keyword)
        result: Dict = None

        if all(not len(value) for value in data.values()):
            result = {"message": f"No info found for: {keyword}!"}
        else:
            result = data

        return result

    def on_success(self, retval, task_id, args, kwargs):
        print ("Task id: ", task_id)
        print ("retval ", retval)    
        print ("Args ", args)
        print ("kwargs: ", kwargs)

