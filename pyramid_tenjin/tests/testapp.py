# -*- coding: utf-8 -*-

import datetime
from wsgiref.simple_server import make_server
from pyramid.config import Configurator


def view1(request):
    return {'aaa': u'テスト', 'bbb': datetime.datetime.now()}


def get_app():
    config = Configurator()
    config.include('pyramid_tenjin')
    config.add_route('root', '/')
    config.add_view(view1, route_name='root', renderer='view1.tenjin')
    return config.make_wsgi_app()

def run_app():
    app = get_app()
    server = make_server('127.0.0.1', 8000, app)
    server.serve_forever()

if __name__ == '__main__':
    run_app()
