import analysis


# test file contains single bad string comparison.
def testpattern1_1():
    file = 'testPattern1-1.java'
    analysis.analysis_string_cmp(file)


# test file contains multiple bad string comparisons.
def testpattern1_2():
    file = 'testPattern1-2.java'
    analysis.analysis_string_cmp(file)


# test file contains comparison between string and string identifier
def testpattern1_3():
    file = 'testPattern1-3.java'
    analysis.analysis_string_cmp(file)


if __name__ == '__main__':
    testpattern1_1()
    testpattern1_2()
    testpattern1_3()
