import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test_hello(self):
        print("english_to_french - assertEqual")
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        
    def test_null(self):
        print("english_to_french - assertNotEqual")
        self.assertNotEqual(english_to_french('None'), '')
        self.assertNotEqual(english_to_french(0), 0)
        print("english_to_french - assertIsNotNone")
        self.assertIsNotNone(english_to_french('None'))

class TestFrenchToEnglish(unittest.TestCase):
    def test_bonjour(self):
        print("french_to_english - assertNotEqual")
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

    def test_null(self):
        print("french_to_english - assertNotEqual")
        self.assertNotEqual(french_to_english('None'), '')
        self.assertNotEqual(french_to_english(0), 0)
        print("french_to_english - assertIsNotNone")
        self.assertIsNotNone(french_to_english('None'))

unittest.main()