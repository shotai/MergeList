import heapq
import requests

__author__ = 'mmgu'


class MergeList:
    def __init__(self, name1, name2):
        self.stream1_name = name1
        self.stream2_name = name2
        self.cache = []
        self.service_endpoint = "http://localhost:5000/get/"
        self.last_value = None
        self.stream_list = [name1, name2]

    def get_stream_data(self, stream_name):
        res = requests.get(self.service_endpoint + stream_name, headers={"Accept": "application/json"})
        res = res.json()
        heapq.heappush(self.cache, (res["current"], res["stream"]))

    def get_smallest(self):
        key, value = heapq.heappop(self.cache)
        response = {"last": self.last_value, "current": key}
        self.get_stream_data(value)
        print(self.cache)
        print(key)
        print(value)
        return response

    def start(self):
        if self.cache is None:
            self.get_stream_data(self.stream1_name)
            self.get_stream_data(self.stream2_name)
            return self.get_smallest()
        else:
            return self.get_smallest()


test = MergeList("abc","abcc")
test.get_stream_data("a")
test.get_stream_data("a")
test.get_smallest()
