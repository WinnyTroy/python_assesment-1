import unittest


class KeyPress(object):
    """
    Create the dictionary to store the numbers as keys and the list of strings as values
    Create a counter variable to store counts whenever a letter is found in the key-value pairing.
    Convert the input string to uppercase for easier dictionary 'parsing'
    loop through dictionary keys and loop through the strings, checking if each letter in the string is in the value of the key.
    """
    def __init__(self, phrase):
        self.phrase = phrase

    def presses(self):
        # converts the string to upper and stores in variable,
        phrase = self.phrase.upper()
        # creates a counter variable
        key_count = 0
        KEYS = {"1": ["1"], "2": ["A", "B", "C", "2"], "3": ["D", "E", "F", "3"],
                "4": ["G", "H", "I", "4"], "5": ["J", "K", "L", "5"], "6": ["M", "N", "O", "6"],
                "7": ["P", "Q", "R", "S", "7"], "8": ["T", "U", "V", "8"], "9": ["W", "X", "Y", "Z", "9"],
                "*": ["*"], "0": [" ", "0"], "#": ["#"]
                }
        # perform loop
        for k in KEYS.keys():
            for letter in phrase:
                if letter in KEYS.get(k):

class Tests(unittest.TestCase):
    def test1(self):
        press = KeyPress("V8")
        self.assertEqual(7, press.presses())

    def test2(self):
        press = KeyPress("LOL")
        self.assertEqual(9, press.presses())

    def test3(self):
        press = KeyPress("How R  2day")
        self.assertEqual(23, press.presses())

    def test4(self):
        press = KeyPress("i 8 2 Many mandazi 4 brekky")
        self.assertEqual(45, press.presses())

