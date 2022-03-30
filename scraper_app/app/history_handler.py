from datetime import datetime
import requests
import json

class HistoryHandler:
    def __init__(self, task_id, keyword, scraped_data):
        self.task_id = task_id
        self.keyword = keyword
        self.scraped_data = scraped_data
        self.timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def add_new_record(self):
        URL = 'http://history-app:8000/new_record'
        headers = {'Content-type': 'application/json'}
        payload = {
            'task_id': self.task_id,
            'keyword': self.keyword,
            'content': json.dumps(self.scraped_data),
            'timestamp': self.timestamp
        }

        response = requests.post(url=URL, headers=headers, json=payload)

        return response.status_code