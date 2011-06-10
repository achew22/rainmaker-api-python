import rainmaker

from mock import patch

import json
import mock
import unittest

class TestRainmakerHelper(unittest.TestCase):
    def setUp(self):
        self.rainmaker = rainmaker.RainMaker("aef190bfcecd13fc")

    @patch.object('helper')
    def testSampleData(self, helper):
        helper.return_value = json.loads(BART_SAMPLE)
        
        self.assertEqual(self.rainmaker.do_lookup(), BART_OBJ)
    
    #Test the helper functions
