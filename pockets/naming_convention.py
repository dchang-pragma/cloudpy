# 1. Limit all lines to a maximum of 79 characters.
# 2. Surround top-level function and class definitions with two blank lines.
# 3. Files using ASCII (in Python 2) or UTF-8 (in Python 3) should not have an encoding declaration.
# 4. Imports should usually be on separate lines; Imports are always put at the top of the file, just after any module comments and docstrings, and before module globals and constants.
# 5. Absolute imports are recommended, as they are usually more readable and tend to be better behaved
# 6. Module level "dunders" (i.e. names with two leading and two trailing underscores) such as __all__, __author__, __version__, etc. should be placed after the module docstring but before any import statements except from __future__ imports. Python mandates that future-imports must appear in the module before any other code except docstrings.

import os
import sys
from subprocess import Popen, PIPE

# Yes: easy to match operators with operands

income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)


class CapWords:
	def __init__(self):
		self.word1='Cap'
		self.word2='Words'