from flask import Flask
from flask import request
from flask import jsonify
import os
import mergelist

app = Flask(__name__)
merge_list = mergelist.MergeList()


@app.route('/quiz/merge')
def merge():
    merge_list.stream1_name = request.args['stream1']
    merge_list.stream2_name = request.args['stream2']
    return jsonify(merge_list.start())


if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 3000)))
