import unittest

from ../translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french("hello"), "bonjour")
        self.assertEqual(english_to_french("text"), "texte")


class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english("bonjour"), "hello")
        self.assertEqual(french_to_english("auto"), "car")

unittest.main()
