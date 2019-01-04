import sys

from flask import _app_ctx_stack


class RealtimeImport(object):

    IMPORTED_PACKAGES = 'flask_realtime_import_imported_packages'

    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.before_request(self.before_request)
        app.teardown_request(self.teardown_request)

    def before_request(self):
        ctx = _app_ctx_stack.top
        if ctx is not None:
            if not hasattr(ctx, self.IMPORTED_PACKAGES):
                setattr(ctx, self.IMPORTED_PACKAGES, list(sys.modules.keys()))

    def teardown_request(self, exception):
        ctx = _app_ctx_stack.top
        if hasattr(ctx, self.IMPORTED_PACKAGES):
            after = sys.modules.keys()
            del_list = [
                i for i in after
                if i not in getattr(ctx, self.IMPORTED_PACKAGES)
            ]
            for i in del_list:
                del sys.modules[i]
