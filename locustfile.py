import time
from locust import HttpUser, task, between
import json

with open('post_data.json') as f:
    post_data = json.load(f)

class QuickstartUser(HttpUser):
    @task
    def send_query(self):
        self.client.post("/v1/chat/completions", json = post_data)