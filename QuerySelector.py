import json
import os
import glob
import random

class QuerySelector():
    def __init__(self, config: dict) -> None:
        self.counter = 0
        self.refresh_limit = config["refresh_limit"],
        self.refresh_rate = config["refresh_rate"]
        self.QUESTION_TYPES = list(config["weights"].keys())
        self.weights = list(config["weights"].values())
        with open('post_data.json') as f:
            self.post_data_schema = json.load(f)
        self.queries = self.refresh_questions()
    
    def refresh_questions(self):
        tmp_queries = dict()
        for question_type in self.QUESTION_TYPES:
            tmp_queries[question_type] = list()
            text_files = glob.glob(os.path.join("questions_folder", question_type, '*.txt'), recursive=True)
            for text_file in text_files:
                with open(text_file) as f:
                    tmp_queries[question_type].extend(f.readlines())
        self.queries = tmp_queries

    def get_query(self):
        # if self.counter >= self.refresh_limit:
        #     self.counter = 0
        #     self.refresh_questions()
        question_type = random.choices(self.QUESTION_TYPES, weights=self.weights)[0]
        self.counter += 1
        return random.choice(self.queries[question_type])
    
if __name__ == "__main__":
    query_selector = QuerySelector(json.load(open('config.json')))
    print(query_selector.get_query())