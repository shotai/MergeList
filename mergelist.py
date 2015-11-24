import heapq
import requests
import json


class MergeList:
    def __init__(self, name1=None, name2=None):
        self.stream1_name = name1
        self.stream2_name = name2
        self.merged_queue = []
        self.service_endpoint = "https://test.com/quiz/next/"
        self.last_value = None
        self.popped_stream = None

    # send one get request to get one data from the stream
    def get_stream_data(self, stream_name):
        try:
            res = requests.get(self.service_endpoint + stream_name, headers={"Accept": "application/json"})
            res = res.json()
        except json.JSONDecodeError:
            print("Json Decode Error")
            return
        heapq.heappush(self.merged_queue, (res["current"], res["stream"]))

    # pop the smallest one from cache
    def get_smallest(self):
        try:
            key, value = heapq.heappop(self.merged_queue)
        except IndexError:
            print("Stream drained")
            return {"last": self.last_value, "current": None}
        response = {"last": self.last_value, "current": key}
        self.last_value = str(key)
        self.popped_stream = value
        return response

    # entry function
    def start(self):
        if not self.popped_stream:
            self.get_stream_data(self.stream1_name)
            self.get_stream_data(self.stream2_name)
        elif self.popped_stream == self.stream1_name:
            self.get_stream_data(self.stream1_name)
        elif self.popped_stream == self.stream2_name:
            self.get_stream_data(self.stream2_name)
        return self.get_smallest()



