This project will listen to localhost:3000 as default.
You can define the environment variable 'PORT' to change the listening port.
The endpoint url is localhost:3000/quiz/merge. Need to provide 2 variables, stream1 and stream2.
i.e. http://localhost:3000/quiz/merge?stream1=a&stream2=b

The project will first check the last popped stream name,get that stream data and push into heap queue.
If the last popped stream name is None, it will query from both two streams and push into heap queue.
Then it will pop from the heap queue, which is the smallest one and save the popped stream name.

The project will also save the last_value when popping from the heap queue.
If it is the first time to visit the endpoint, the last value will be None.
i.e.
{
  "current": 113,
  "last": null
}

This project will assume that during the querying, the stream1 and stream2 's name cannot be changed.
If you want to query different streams, you need to restart the endpoint.
I can also enhance this project to support changeable stream names if you need.



Environment: Python 3.5.0
Package: flask, requests, os, json, heapq
To start: $ python app.py

