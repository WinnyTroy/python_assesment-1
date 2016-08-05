# Using the Python,
# have the function CaesarCipher(str, num) take the str parameter and perform a Caesar Cipher num on it using the num parameter as the numing number.
# A Caesar Cipher works by numing all letters in the string N places down in the alphabetical order (in this case N will be num).
# Punctuation, spaces, and capitalization should remain intact.

# For example if the string is "Caesar Cipher" and num is 2 the output should be "Ecguct Ekrjgt".

# more on cipher visit http://practicalcryptography.com/ciphers/caesar-cipher/
# happy coding :-)
import unittest


class CaesarCipher(object):
    """

    cipher: takes in string and numing number
    :returns the cipher as per the numing number

    """
    def __init__(self, caeser):
        self.caeser = caeser

    def cipher(self, num):
        string, out = self.caeser, []
        for word in string:
            for x in word:
                if x != " ":
                    out.append(chr(ord(x) + num))
                else:
                    out.append(x)
        return "".join(out)

    # variation two, using list compression in loop
    def cipher_two(self, num):
        ciph, out = self.caeser, []
        for word in ciph:
            out = [chr(ord(x) + num) for x in word if x != " "]
        return "".join(out)

c = CaesarCipher("A Crazy fool Z")
c1 = CaesarCipher("Caesar Cipher")
print(c.cipher(1))
print(c1.cipher(2))

class Tests(unittest.TestCase):
