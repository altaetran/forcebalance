import unittest
import sys, os
import forcebalance.parser

class TestParser(unittest.TestCase):
    def setUp(self):
        self.console = sys.stdout
        sys.stdout = open(os.devnull,'w')
    
    def tearDown(self):
        sys.stdout.close()        
        sys.stdout = self.console

    def test_parse_inputs_returns_tuple(self):
        """parse_inputs() returns a tuple"""
        output = forcebalance.parser.parse_inputs('../studies/001_water_tutorial/very_simple.in')
        self.assertEqual(type(output), tuple)

    def test_parse_inputs_generates_default_options(self):
        """parse_inputs() without arguments generates default options"""
        output = forcebalance.parser.parse_inputs()[0]
        defaults = forcebalance.parser.gen_opts_defaults
        defaults.update({'root':os.getcwd()})
        self.assertEqual(output, defaults)

if __name__ == '__main__':        
    unittest.main()