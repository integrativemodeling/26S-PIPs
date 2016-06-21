#!/usr/bin/env python

import unittest
import os
import sys
import subprocess
import glob



class Tests(unittest.TestCase):
    def run_imp_script(self, script_name):
        """Run IMP modeling"""
        p = subprocess.check_call(["python", "modeling.py", "--test"])

if __name__ == '__main__':
unittest.main()
