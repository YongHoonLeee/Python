from flask import Flask
# from flask import g
# from flask import render_template
# from flask import Request
# from flask import Response


app = Flask(__name__)


@app.route('/hello')
def hello_world():
    return 'hello world!'


@app.route('/')
def top():
    return 'Top.'


def main():
    app.debug = True
    app.run()


if __name__ == '__main__':
    main()
