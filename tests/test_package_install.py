# -*- coding: utf-8 -*-

import unittest
from .data_tests import PROJECT_PATH
from vswitch import install_params


class TestInstallVSwitch(unittest.TestCase):

    def setUp(self):
        import os
        self.path_install_script = os.path.join(PROJECT_PATH, 'setup.py')

    def tearDown(self):
        pass

    def test_install_exists(self):
        self.assertTrue(self.path_install_script)

    def test_install_file_is_not_empty(self):
        with open(self.path_install_script) as setup_file:
            self.assertGreater(len(setup_file.readlines()), 0)

    def test_install_file_imports_setuptools(self):
        with open(self.path_install_script) as setup_file:
            self.assertTrue(any('setuptools' in _ for _ in setup_file.readlines()))

    def test_install_file_imports_install_function(self):
        with open(self.path_install_script) as setup_file:
            self.assertTrue(any('setup' in _ for _ in setup_file.readlines()))

    def test_install_params_has_version(self):
        self.assertIn('version', install_params)

    def test_install_params_version_has_value(self):
        self.assertIsNotNone(install_params['version'])
        self.assertIn('version', install_params)

    def test_install_params_is_dict(self):
        self.assertIsInstance(install_params, dict)

    def test_install_params_has_name(self):
        self.assertIn('name', install_params)

    def test_install_params_name_has_value(self):
        self.assertIsNotNone(install_params['name'])
        self.assertIn('name', install_params)


if __name__ == '__main__':
    unittest.main()
