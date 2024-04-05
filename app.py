from flask import Flask


class App:
    def __init__(self):
        self.app = Flask(__name__)

    def start_app(self):
        @self.app.route('/')
        def index():
            return '<h1>Start page</h1>'

        self.app.run(host='127.0.0.1', port=1488, debug=True)


if __name__ == '__main__':
    a = App()
    a.start_app()
