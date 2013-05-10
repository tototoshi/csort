import csort
import unittest

class CsortTest(unittest.TestCase):

    def test_csort(self):
        lines = csort.csort(iter(["a\tb\tc", "d\te\tf", "g\th\ti"]), [1, 2, 0])
        self.assertEqual(lines.next(), "\t".join(['b', 'c', 'a']))
        self.assertEqual(lines.next(), "\t".join(['e', 'f', 'd']))
        self.assertEqual(lines.next(), "\t".join(['h', 'i', 'g']))

def suite():
    return unittest.TestLoader().loadTestsFromTestCase(CsortTest)


