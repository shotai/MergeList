import heapq
import requests
import json

__author__ = 'mmgu'


class MergeList:
    def __init__(self, name1=None, name2=None):
        self.stream1_name = name1
        self.stream2_name = name2
        self.cache = []
        self.service_endpoint = "https://test.com/quiz/next/"
        self.last_value = None
        self.stream_list = []


    def get_stream_data(self, stream_name):
        try:
            res = requests.get(self.service_endpoint + stream_name, headers={"Accept": "application/json"})
            res = res.json()
        except json.JSONDecodeError:
            return

        heapq.heappush(self.cache, (res["current"], res["stream"]))
        self.stream_list.append(stream_name)

    def get_last_value(self, num = None):
        return num

    def get_smallest(self):
        #print(self.last_value)
        try:
            key, value = heapq.heappop(self.cache)
        except IndexError:
            return {"last": self.last_value, "current": None,"stream": None}
        response = {"last": self.last_value, "current": key, "stream": value}
        self.last_value = str(key)
        #print(self.last_value)
        self.stream_list.remove(value)
        # print(self.cache)
        # print(key)
        # print(value)
        # print(self.last_value)
        # print(self.stream_list)
        return response

    def cleanup_old_stream(self, new_stream_name, old_stream_name):
        for i,v in self.cache:
            if v == old_stream_name:
                self.cache.remove((i,v))
        if old_stream_name in self.stream_list:
            self.stream_list.remove(old_stream_name)
        return new_stream_name

    def start(self, name1=None, name2=None):
        # if name1 and name1 != self.stream1_name:
        #     self.stream1_name = self.cleanup_old_stream(name1,self.stream1_name)
        # if name2 and name2 != self.stream2_name:
        #     self.stream2_name = self.cleanup_old_stream(name2,self.stream2_name)
        self.get_stream_data(self.stream1_name)
        self.get_stream_data(self.stream2_name)
        return self.get_smallest()
        # if not self.cache:
        #     print("drained")
        #     print(self.stream_list)
        #     self.get_stream_data(self.stream1_name)
        #     self.get_stream_data(self.stream2_name)
        #     return self.get_smallest()
        # elif self.stream1_name not in self.stream_list:
        #     self.get_stream_data(self.stream1_name)
        # elif self.stream2_name not in self.stream_list:
        #     self.get_stream_data(self.stream2_name)
        # return self.get_smallest()

# stream1 = [1, 2, 3, 4, 5]
# stream2 = [2, 3, 4, 4, 5]
# #stream3 = [3, 4, 5]
# print(sorted(stream1+stream2))
# test = MergeList("stream1","stream2")
# # print(test.start())
# # print(test.start())
# # print(test.start())
# # print(test.start())
# # print(test.start())
# #test.stream1_name = "b"
# # print(sorted(stream2+stream3))
# # print(test.start(name1="b"))
# # print(test.start())
# # print(test.start())
# # print(test.start())
# print(test.start())
# print(test.start())
# #
# print(test.start())
# print(test.start())
# test.get_stream_data("a")
# print(test.last_value)
# test.get_stream_data("b")
# print(test.last_value)
# print(test.get_smallest())
# print(test.get_smallest())
