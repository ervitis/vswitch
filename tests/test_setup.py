# -*- coding: utf-8 -*-

import unittest
from .data_tests import PROJECT_PATH


class TestSetupVSwitch(unittest.TestCase):

    def setUp(self):
        import os
        self.path_setup_script = os.path.join(PROJECT_PATH, 'setup.py')

    def tearDown(self):
        pass

    def test_setup_exists(self):
        self.assertTrue(self.path_setup_script)

    def test_setup_file_is_not_empty(self):
        with open(self.path_setup_script) as setup_file:
            self.assertGreater(len(setup_file.readlines()), 0)


if __name__ == '__main__':
    unittest.main()
