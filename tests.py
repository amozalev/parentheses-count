import unittest
from parentheses import with_regexp, without_regexp


class Test(unittest.TestCase):
    def test_without_regexp1(self):
        self.assertEqual(without_regexp('abra((esdf)(esdf'), 'abra((esdf)')

    def test_without_regexp2(self):
        self.assertEqual(without_regexp('abra((esdf(esdf'), 'abra')

    def test_without_regexp3(self):
        self.assertEqual(without_regexp('abra((esdf)abc((esdf)'), 'abra((esdf)abc((esdf)')

    def test_without_regexp4(self):
        self.assertEqual(without_regexp('abra((esdf)abc(hjkk(vsdf))'), 'abra((esdf)abc(hjkk(vsdf))')

    def test_without_regexp5(self):
        self.assertEqual(without_regexp('abra((esdf)abc(hjkk(vsdf)'), 'abra((esdf)abc')

    def test_without_regexp6(self):
        self.assertEqual(without_regexp('abra((esdf)abc(hjkk(vsdf'), 'abra((esdf)abc')

    def test_without_regexp7(self):
        self.assertEqual(without_regexp('abra((esdf)abc((vsdf)'), 'abra((esdf)abc((vsdf)')

    def test_without_regexp8(self):
        self.assertEqual(without_regexp('abra((esdf)abc((vsdf)((fgj))hjk((((ghj)'), 'abra((esdf)abc((vsdf)((fgj))hjk')

    def test_with_regexp1(self):
        self.assertEqual(with_regexp('abra((esdf)(esdf'), 'abra((esdf)')

    def test_with_regexp2(self):
        self.assertEqual(with_regexp('abra((esdf(esdf'), 'abra')

    def test_with_regexp3(self):
        self.assertEqual(with_regexp('abra((esdf)abc((esdf)'), 'abra((esdf)abc((esdf)')

    def test_with_regexp4(self):
        self.assertEqual(with_regexp('abra((esdf)abc(hjkk(vsdf))'), 'abra((esdf)abc(hjkk(vsdf))')

    def test_with_regexp5(self):
        self.assertEqual(with_regexp('abra((esdf)abc(hjkk(vsdf)'), 'abra((esdf)abc')

    def test_with_regexp6(self):
        self.assertEqual(with_regexp('abra((esdf)abc(hjkk(vsdf'), 'abra((esdf)abc')

    def test_with_regexp7(self):
        self.assertEqual(with_regexp('abra((esdf)abc((vsdf)'), 'abra((esdf)abc((vsdf)')

    def test_with_regexp8(self):
        self.assertEqual(with_regexp('abra((esdf)abc((vsdf)((fgj))hjk((((ghj)'), 'abra((esdf)abc((vsdf)((fgj))hjk')


if __name__ == '__main__':
    unittest.main()
