import os
import unittest
import json

import pywear
from test import utils

DATA = 'data/sample.cwa.gz'
OUTPUTS = 'test/outputs/axivity/'
TESTS = utils.create_tests()


class TestAxivity(unittest.TestCase):

    maxDiff = None

    @classmethod
    def setUpClass(cls):
        data, info = pywear.read_device(DATA)
        cls.data = data
        cls.info = info

    @classmethod
    def tearDownClass(cls):
        del cls.data
        del cls.info

    def test_process(self):

        for testname, testparam in TESTS.items():

            with self.subTest("Testing processing...", **testparam):

                _, info = pywear.reader.process(TestAxivity.data,
                                                TestAxivity.info,
                                                **testparam)

                with open(os.path.join(OUTPUTS, testname + '.json')) as f:
                    _info = json.load(f)
                self.assertDictEqual(info, _info)
