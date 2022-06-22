import unittest
from translator import english_to_french, french_to_english


class TestTranslator(unittest.TestCase):
    def testEnglish2French(self):
        self.assertEqual(english_to_french(None), None)
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertEqual(english_to_french("Goodbye"), "Au revoir")
        self.assertNotEqual(english_to_french("Happy"), "Triste")
        self.assertNotEqual(english_to_french("None"), 0)
        self.assertNotEqual(english_to_french("Hello"), "Au revoir")

    def testFrench2English(self):
        self.assertEqual(french_to_english(None), None)
        self.assertEqual(french_to_english(""), "")
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertEqual(french_to_english("Au revoir"), "Goodbye")
        self.assertNotEqual(french_to_english("Triste"), "Happy")
        self.assertNotEqual(french_to_english("None"), 0)
        self.assertNotEqual(french_to_english("Hello"), "Au revoir")


unittest.main()