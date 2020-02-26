from flask import Flask
from flask import g
from flask import render_template
from flask import request
from flask import Response


app = Flask(__name__)


@app.route('/hello')
@app.route('/hello/<username>')
def hello_world(username=None):
    return render_template('hello.html', username=username)


@app.route('/whattime<username>')
def timeis(username=None):
    return render_template('xmas.html', username=username)


@app.route('/post', methods=['POST', 'GET', 'PUT', 'DELETE'])
def show_post():
    return request.values


def main():
    app.debug = True
    app.run()


if __name__ == '__main__':
    main()
