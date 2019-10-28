import analysis
import unittest


class TestPattern(unittest.TestCase):
    # test file contains single bad string comparison.
    def testpattern1_1(self):
        file = 'testPattern1-1.java'
        result = analysis.analysis_string_cmp(file)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].line, 4)
        self.assertEqual(result[0].column, 20)

    # test file contains multiple bad string comparisons.
    def testpattern1_2(self):
        file = 'testPattern1-2.java'
        result = analysis.analysis_string_cmp(file)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].line, 4)
        self.assertEqual(result[0].column, 20)
        self.assertEqual(result[1].line, 7)
        self.assertEqual(result[1].column, 20)

    # test file contains comparison between string and string identifier
    def testpattern1_3(self):
        file = 'testPattern1-3.java'
        result = analysis.analysis_string_cmp(file)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].line, 5)
        self.assertEqual(result[0].column, 12)


if __name__ == '__main__':
    unittest.main()
