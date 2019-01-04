from flask import Flask
from flask_realtime_import import RealtimeImport
# from flask_sqlalchemy import SQLAlchemy

# from flask_debugtoolbar import DebugToolbarExtension

app = Flask('basic_app')
app.debug = True
app.config['SECRET_KEY'] = 'abc123'
# realtime_import = RealtimeImport()
# realtime_import.init_app(app)
RealtimeImport(app)

# make sure these are printable in the config panel
# app.config['BYTES_VALUE'] = b'\x00'
# app.config['UNICODE_VALUE'] = u'\uffff'

# toolbar = DebugToolbarExtension(app)
# db = SQLAlchemy(app)

# class Foo(db.Model):
#     __tablename__ = 'foo'
#     id = db.Column(db.Integer, primary_key=True)


@app.route('/')
def index():
    return 'hello cloris'


if __name__ == '__main__':
    app.run()
