#!/usr/bin/env python

import unittest
import os
import sys
import subprocess
import glob

TOPDIR = os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), '..'))

class Tests(unittest.TestCase):
    def test_basic(self):
        """Run IMP modeling"""
        os.chdir(TOPDIR)
        p = subprocess.check_call(["python", "modeling.py", "--test"])

if __name__ == '__main__':
    unittest.main()
