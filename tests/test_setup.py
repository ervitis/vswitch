# -*- coding: utf-8 -*-

import unittest
from .data_tests import PROJECT_PATH
from setup import setup_params


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

    def test_setup_file_imports_setuptools(self):
        with open(self.path_setup_script) as setup_file:
            self.assertTrue(any('setuptools' in _ for _ in setup_file.readlines()))

    def test_setup_file_imports_setup_function(self):
        with open(self.path_setup_script) as setup_file:
            self.assertTrue(any('setup' in _ for _ in setup_file.readlines()))

    def test_setup_params_has_version(self):
        self.assertIn('version', setup_params)

    def test_setup_params_version_has_value(self):
        self.assertIsNotNone(setup_params['version'])
        self.assertIn('version', setup_params)

    def test_setup_params_is_dict(self):
        self.assertIsInstance(setup_params, dict)


if __name__ == '__main__':
    unittest.main()
