# -*- coding: utf-8 -*-

import os
import logging
import tenjin
from tenjin.helpers import *


logger = logging.getLogger(__name__)


def renderer_factory(info):
    engine = tenjin.Engine(path=[os.path.dirname(info.package.__file__)])
    template = engine.get_template(info.name)
    def renderer(value, system):
        context = system.copy()
        context.update(value)
        html = template.render(context)
        return html
    return renderer


def includeme(config):
    """
    How to use:

    .. code-block:: python

      config = Configurator()
      config.include('pyramid_tenjin')

    TODO: Write more
    """
    config.add_renderer(name='.tenjin', factory=renderer_factory)
