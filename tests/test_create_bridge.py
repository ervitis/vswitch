# -*- coding: utf-8 -*-

import unittest

from vswitch.bridge import add_br
from vswitch.templates import get_template


class TestCreateBridge(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_create_bridge(self):
        self.assertIsNotNone(add_br(name='test'))

    def test_template_add_br(self):
        self.assertIsNotNone(get_template(name='add-br'))


if __name__ == '__main__':
    unittest.main()
