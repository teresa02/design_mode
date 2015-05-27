from flask import Flask
from werkzeug.routing import BaseConverter
from design.server.controllers.test import test_bp

DEFAULT_MODULES = (
    (test_bp, ''),
)


class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]


def create_app(config=None, modules=None):
    # resource_pool_init()

    if modules is None:
        modules = DEFAULT_MODULES

    app = Flask(__name__)
    app.url_map.converters['regex'] = RegexConverter
    app.config.from_object(config)
    configure_modules(app, modules)
    return app


def configure_modules(app, modules):
    for module, url_prefix in modules:
        app.register_blueprint(module, url_prefix=url_prefix)