#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from subprocess import check_output
import os
from analysis import analysis_ret_empty_array_rather_than_null, analysis_string_cmp


def apply_analysis(analysis, filename):
    analysis(filename)


if __name__ == '__main__':
    test_dir = 'joda-time'

    output = check_output("find joda-time | grep \\\\.java$", shell=True).decode('utf-8')
    filenames = output.split('\n')[:-1]
    for filename in filenames:
        print('checking', filename)
        apply_analysis(analysis_ret_empty_array_rather_than_null, filename)
        apply_analysis(analysis_string_cmp, filename)


