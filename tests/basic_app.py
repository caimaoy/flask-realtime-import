from flask import Flask
from flask_realtime_import import RealtimeImport

app = Flask('basic_app')
RealtimeImport(app)


@app.route('/')
def index():
    return 'hello cloris'


if __name__ == '__main__':
    app.run()
