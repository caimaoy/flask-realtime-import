# flask-realtime-import

[![Build Status](https://travis-ci.org/caimaoy/flask-realtime-import.svg?branch=master)](https://travis-ci.org/caimaoy/flask-realtime-import)
[![Coverage Status](https://coveralls.io/repos/github/caimaoy/flask-realtime-import/badge.svg?branch=master)](https://coveralls.io/github/caimaoy/flask-realtime-import?branch=master)

This is a flask extension that make you can import modules in every request.

## Installation

Installing is simple with pip:

```shell
pip install flask-realtime-import
```

## Usage

Setting up the extension is simple:

```python
from flask import Flask
from flask_realtime_import import RealtimeImport

app = Flask(__name__)
realtime_import = RealtimeImport(app)
```
