import unittest


class QuestionOne(object):
    """

    """
    def __init__(self, input):
        self.input = input

    def sorter(self):
        m = self.input.split(",")
        return ",".join(sorted(m))


class Tests(unittest.TestCase):
    def test1(self):
        que = QuestionOne("without,hello,bag,world")
        self.assertEqual("bag,hello,without,world", que.sorter())
