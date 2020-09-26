import unittest
from unittest import TestCase
from utils import *


class TestUtils(TestCase):
    def test_parsing_of_files(self):
        lines = parse('standard.md')
        self.assertIsNot(0, len(lines))
    
    def test_replacing_tokens(self):
        test_line = "something ${Few lines describing your project.} other thing ${cerva}"
        tokens = parse_into_tokens(test_line)
        for token in tokens:
            self.assertNotIn(token.question ,replace(token, "now", test_line))

unittest.main()