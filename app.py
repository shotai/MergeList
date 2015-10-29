from flask import Flask
from flask import stream_with_context, make_response, request, Response
from flask import jsonify
from flask import g
import collections
import requests

__author__ = 'mmgu'


stream1 = [1, 2, 3, 4, 5]
stream2 = [2, 3, 4, 4, 5]

app = Flask(__name__)


class TestData:
    def __init__(self):
        self.current = 0
        self.last = 0

t = TestData()
t2 = TestData()

@app.route('/quiz/merge')
def merge():
    print(request.args['stream1'])
    print(request.args['stream2'])
    return 'Hello World!'


@app.route('/get/<stream_name>')
def get_stream(stream_name):
    #response = {"last": last, "current": current, "stream": stream_name}
    # last = current
    # print(current)
    # print(last)
    if stream_name == "a":
        response = generate_response(stream_name)
    else:
        response = generate_response2(stream_name)
    return jsonify(response)

def generate_response(stream_name):
    res = {"last":t.last, "current": stream1[t.current], "stream": stream_name}
    t.last = t.current
    t.current += 1
    return res

def generate_response2(stream_name):
    res = {"last":t2.last, "current": stream2[t2.current], "stream": stream_name}
    t2.last = t2.current
    t2.current += 1
    return res

if __name__ == '__main__':

    app.run(debug=True)
