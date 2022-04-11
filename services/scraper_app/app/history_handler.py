from datetime import datetime
import requests
from decouple import config
import os


class HistoryHandler:
    def __init__(self, task_id, keyword, scraped_data):
        self.task_id = task_id
        self.keyword = keyword
        self.scraped_data = scraped_data
        self.timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    @staticmethod
    def get_auth_token():
        credentials_login = config(
            "CREDENTIALS_LOGIN", os.environ["CREDENTIALS_PASSWORD"]
        )
        credentials_password = config(
            "CREDENTIALS_LOGIN", os.environ["CREDENTIALS_PASSWORD"]
        )

        URL = f"http://tokenizator-app:8000/get_auth_token/{credentials_login}/{credentials_password}"
        headers = {"Content-type": "application/json"}

        response = requests.get(URL, headers=headers)
        data = response.json()
        token = data["auth_token"]

        return token

    def add_new_record(self):
        URL = "http://history-app:8000/new_record"
        headers = {
            "Content-type": "application/json",
            "Authorization": f"Bearer {self.get_auth_token()}",
        }
        payload = {
            "task_id": self.task_id,
            "keyword": self.keyword,
            "content": self.scraped_data,
            "timestamp": self.timestamp,
        }

        response = requests.post(url=URL, headers=headers, json=payload)

        return response.status_code
