# -*- coding: utf-8 -*-

import unittest
from .data_tests import PROJECT_PATH


class TestSetupVSwitch(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_setup_exists(self):
        import os
        path_setup_script = os.path.join(PROJECT_PATH, 'setup.py')

        self.assertTrue(os.path.exists(path_setup_script))


if __name__ == '__main__':
    unittest.main()
