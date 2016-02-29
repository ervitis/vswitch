# -*- coding: utf-8 -*-

import unittest

from vswitch import __version__ as version


class TestVSwitchMain(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_vswitch_has_version(self):
        self.assertIsNotNone(version)


if __name__ == '__main__':
    unittest.main()
