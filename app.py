from flask import Flask
from flask import stream_with_context, make_response, request, Response
from flask import jsonify
from flask import g
import collections
import requests
import mergelist

__author__ = 'mmgu'


stream1 = [1, 2, 3, 4, 5]
stream2 = [2, 3, 4, 4, 5]
stream3 = [3, 4, 5]

app = Flask(__name__)


class TestData:
    def __init__(self):
        self.current = 0
        self.last = None

t = TestData()
t2 = TestData()
t3 = TestData()

merge_list = mergelist.MergeList()


@app.route('/quiz/merge')
def merge():
    merge_list.stream1_name = request.args['stream1']
    merge_list.stream2_name = request.args['stream2']
    return jsonify(merge_list.start())


@app.route('/get/<stream_name>')
def get_stream(stream_name):
    #response = {"last": last, "current": current, "stream": stream_name}
    # last = current
    # print(current)
    # print(last)
    if stream_name == "a":
        response = generate_response(stream_name)
    elif stream_name == 'b':
        response = generate_response3(stream_name)
    else:
        response = generate_response2(stream_name)
    return jsonify(response)

def generate_response(stream_name):
    res = {"last":t.last, "current": stream1[t.current], "stream": stream_name}
    t.last = t.current
    t.current += 1
    print(res)
    return res

def generate_response2(stream_name):
    res = {"last":t2.last, "current": stream2[t2.current], "stream": stream_name}
    t2.last = t2.current
    t2.current += 1
    print(res)
    return res

def generate_response3(stream_name):
    res = {"last":t3.last, "current": stream3[t3.current], "stream": stream_name}
    t3.last = t3.current
    t3.current += 1
    print(res)
    return res

if __name__ == '__main__':
    app.run(debug=True)
