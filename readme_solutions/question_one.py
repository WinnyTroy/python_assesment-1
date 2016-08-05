class QuestionOne(object):
    """
    Split the string by commas and sort them alphabetically
    join the strings by commas
    """
    def __init__(self, user_input):
        self.input = user_input

    def sorter(self):
        m = self.input.split(",")
        return ",".join(sorted(m))


print("--" * 10)


def printer():
    sentence = input("Please enter a list of your words, separate by commas ")
    que = QuestionOne(str(sentence))
    return que.sorter()


print(printer())
print("--" * 10)
