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

    # test file contains function returning array of integers
    def testpattern2_1(self):
        file = 'testpattern2-1.java'
        result = analysis.analysis_ret_empty_array_rather_than_null(file)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][0], 9) # line
        self.assertEqual(result[0][1], 7) # column
    
    # test file contains function returning array of doubles
    def testpattern2_2(self):
        file = 'testpattern2-2.java'
        result = analysis.analysis_ret_empty_array_rather_than_null(file)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][0], 10) # line
        self.assertEqual(result[0][1], 7) # column

    # test file contains function returning array of custom classes
    def testpattern2_3(self):
        file = 'testpattern2-3.java'
        result = analysis.analysis_ret_empty_array_rather_than_null(file)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][0], 15) # line
        self.assertEqual(result[0][1], 7) # column




if __name__ == '__main__':
    unittest.main()
