#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from subprocess import check_output
from analysis import analysis_ret_empty_array_rather_than_null, analysis_string_cmp


def apply_analysis(analysis, filename):
    return analysis(filename)


if __name__ == '__main__':
    test_dir = 'joda-time'

    output = check_output("find joda-time | grep \\\\.java$", shell=True).decode('utf-8')
    filenames = output.split('\n')[:-1]
    for filename in filenames:
        print('checking', filename)
        apply_analysis(analysis_ret_empty_array_rather_than_null, filename)
        string_result = apply_analysis(analysis_string_cmp, filename)
        if len(string_result) > 0:
            print("There are {} bad string comparison in the file.".format(len(string_result)))
            print(string_result)

