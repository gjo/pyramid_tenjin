# -*- coding: utf-8 -*-

import unittest
import webtest


class PyramidTenjinTestCase(unittest.TestCase):

    def test_1(self):
        import pyramid_tenjin
        from .testapp import get_app
        testapp = webtest.TestApp(get_app())
        response = testapp.get('/', status=200)
        self.failUnless('PyramidTenjin' in response.body)
        return
