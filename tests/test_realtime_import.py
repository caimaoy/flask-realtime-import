import sys

import pytest


def load_app(name):
    app = __import__(name).app
    app.config['TESTING'] = True
    return app.test_client()


def test_basic_app():
    app = load_app('basic_app')
    index = app.get('/')
    assert index.status_code == 200
    assert b'cloris' in index.data


def test_app_2():
    app = __import__('basic_app').app
    with app.test_request_context('/'):
        app.preprocess_request()
        import package_for_test
        assert 'package_for_test' in sys.modules
    assert 'package_for_test' not in sys.modules