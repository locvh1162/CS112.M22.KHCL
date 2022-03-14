# test_palindrome
import unittest
import unittest_2

class TestExercise(unittest.TestCase):
    MESSAGE_FMT = 'Kết quả mong muốn là `{0}`, nhận được `{1}`: `{2}`'

    def _test_all(self, func, cases):
        for input_, expect in cases:
            output = func(input_)
            msg = self.MESSAGE_FMT.format(expect, output, input_)
            self.assertEqual(output, expect, msg)


class TestPalindrome(TestExercise):

    def test_check_palindrome(self):
        cases = [('madam', True),
                 ('1221', True),
                 ('Python', False),
                 ('', False),
                 ('P', False),
                 ('Able was I ere I saw Elba', True)]
        self._test_all(unittest_2.check_palindrome, cases)


if __name__ == '__main__':
    unittest.main(verbosity=2)