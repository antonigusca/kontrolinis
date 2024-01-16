import unittest


def reverse_and_upper(s):
    return s[::-1].upper()

class Tests(unittest.TestCase):

    def test_revert_and_upper(self):
        self.assertEqual(reverse_and_upper("abcd"), "DCBA")
        self.assertEqual(reverse_and_upper(""), "")
        self.assertEqual(reverse_and_upper("zxcv"), "vcxz")


