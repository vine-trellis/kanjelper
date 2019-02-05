from flask import Flask, request, jsonify
import sys, os
sys.path.append(os.getcwd() + '/core/interact')
import query


app = Flask(__name__)


@app.route('/')
def hello_world():
    table_name = request.args.get('table')
    kanji = request.args.get('kanji')
    data = query.queryTable(table_name, kanji)
    return jsonify(data)