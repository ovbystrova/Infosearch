from flask import Flask, render_template, request
from search import search

app = Flask(__name__)

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():

    if request.args:
        query = request.args['query']
        metric = request.args['metric']

        result = search(query, metric)

        return render_template('index_response.html', res=result)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=False)