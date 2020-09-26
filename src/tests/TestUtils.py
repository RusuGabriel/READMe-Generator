import unittest
from unittest import TestCase
from utils import *


class TestUtils(TestCase):
    def test_parsing_of_files(self):
        lines = parse('standard.md')
        self.assertIsNot(0, len(lines))
    
    def test_replacing_tokens(self):
        test_line = "something ${Few lines describing your project.} other thing ${otherthing}"
        tokens = parse_into_tokens(test_line)
        self.assertNotEqual(len(tokens), 0)
        for token in tokens:
            self.assertNotIn(token.question ,replace(token, "now", test_line),'Failed the replacing of messages') 

    def test_get_question_from(self):
        test_line = "something ${Few lines describing your project.}"
        tokens = parse_into_tokens(test_line)
        self.assertEqual(len(tokens),1)
        self.assertEqual('Few lines describing your project.', get_question_from(tokens[0])[:-2])
unittest.main()