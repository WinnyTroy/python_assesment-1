# Using the Python,
# have the function CaesarCipher(str, num) take the str parameter and perform a Caesar Cipher num on it using the num parameter as the numing number.
# A Caesar Cipher works by numing all letters in the string N places down in the alphabetical order (in this case N will be num).
# Punctuation, spaces, and capitalization should remain intact.

# For example if the string is "Caesar Cipher" and num is 2 the output should be "Ecguct Ekrjgt".

# more on cipher visit http://practicalcryptography.com/ciphers/caesar-cipher/
# happy coding :-)


class CaesarCipher(object):
    """
    cipher: takes in string and numing number
    :returns the cipher as per the numing number
    """
    def __init__(self, caesar, num):
        self.caesar = caesar
        self.num = num

    def cipher(self):
        string, out = self.caesar, []
        for word in string:
            for x in word:
                if x != " ":
                    out.append(chr(ord(x) + self.num))
                else:
                    out.append(x)
        return "".join(out)

    # variation two, using list compression in loop
    def cipher_two(self):
        ciph, out = self.caesar, []
        for word in ciph:
            out = [chr(ord(x) + self.num) for x in word if x != " "]
        return "".join(out)

# use raw_input() for Python 2.7
user_phrase = input("Caeser cipher for today? ")
user_numming = input("Number to cipher?")


# function to validate numming, must be an integer
def validate_numming(numming):
    return isinstance(numming, int)


# print cipher
def print_cipher():
    cc = CaesarCipher(user_phrase, user_numming)
    # check for validation pass
    if validate_numming(user_numming):
        print("Loading...")
        print(cc.cipher())
        print("*-*-*"*10)
    else:
        print("Please enter a valid number.")
