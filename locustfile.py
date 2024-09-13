import time
import threading
from locust import HttpUser, task, between
import json
import random
import QuerySelector



with open('post_data.json') as f:
    post_data_schema = json.load(f)

query_selector = QuerySelector.QuerySelector(json.load(open('config.json')))

class QuickstartUser(HttpUser):

    @task
    def send_query(self):
        post_data = dict(post_data_schema)
        post_data["messages"][0]["content"] = query_selector.get_query()
        self.client.post("/v1/chat/completions", json = post_data)

def refresh_questions():
    while True:
        query_selector.refresh_questions()
        time.sleep(query_selector.refresh_rate)

threading.Thread(target=refresh_questions).start()
    