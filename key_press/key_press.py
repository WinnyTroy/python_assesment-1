class KeyPress(object):
    """
    Create the dictionary to store the numbers as keys and the list of strings as values
    """
    @staticmethod
    def presses(phrase):
        keys = {1: "1", 2: ["A", "B", "C", "2"], 3: []}
        # Your Code Here!



print(KeyPress.presses("V8")) # 7
print(KeyPress.presses("LOL")) # 9
print(KeyPress.presses("How R  2day")) #23
print(KeyPress.presses("i 8 2 Many mandazi 4 brekky"))

