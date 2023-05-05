import unittest

from translator import englishtofrench, frenchtoenglish

class Testenglishtofrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishtofrench('Hello'), 'Bonjour') 
        #self.assertEqual(englishtofrench('None'), '')

class Testfrenchtoenglish(unittest.TestCase):
    def test2(self):
        self.assertEqual(frenchtoenglish('Bonjour'), 'Hello') 
        self.assertNotEqual(frenchtoenglish("None"), '')

unittest.main()