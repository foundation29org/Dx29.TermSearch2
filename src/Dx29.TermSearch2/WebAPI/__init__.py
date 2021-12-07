import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property

import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func

from .api import API
