import unittest


class QuestionThree(object):
    def __init__(self, binary_lst):
        self.binary_lst = binary_lst

    def div_five(self):
        return ",".join([x for x in self.binary_lst.split(",") if int(x, 2) % 5 == 0])

    def div_five_tw0(self):
        lst = []
        for x in self.binary_lst.split(","):
            if int(x, 2) % 5 == 0:
                lst.append(x)
        return ",".join(lst)


class Tests(unittest.TestCase):
    def test1(self):
        que = QuestionThree("0100,0011,1010,1001")
        self.assertEqual("1010", que.div_five())

    def test2(self):
        que = QuestionThree("0100,0011,1010,1001")
        self.assertEqual("1010", que.div_five_tw0())
