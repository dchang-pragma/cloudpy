# 1. Limit all lines to a maximum of 79 characters.
# 2. Surround top-level function and class definitions with two blank lines.
# 3. Files using ASCII (in Python 2) or UTF-8 (in Python 3) should not have an encoding declaration.
# 4. Imports should usually be on separate lines; Imports are always put at the top of the file, just after any module comments and docstrings, and before module globals and constants.
# 5. Absolute imports are recommended, as they are usually more readable and tend to be better behaved
# 6. Module level "dunders" (i.e. names with two leading and two trailing underscores) such as __all__, __author__, __version__, etc. should be placed after the module docstring but before any import statements except from __future__ imports. Python mandates that future-imports must appear in the module before any other code except docstrings.
# 7. Note: When using acronyms in CapWords, capitalize all the letters of the acronym. HTTPServerErrors
# 8. Never use the characters 'l' (lowercase letter el), 'O' (uppercase letter oh), or 'I' (uppercase letter eye) as single character variable names. In some fonts, these characters are indistinguishable from the numerals one and zero. When tempted to use 'l', use 'L' instead.
# 9. Modules should have short, all-lowercase names. Underscores can be used in the module name if it improves readability. 
# 10 . Python packages should also have short, all-lowercase names, although the use of underscores is discouraged.
# 11. Constants are usually defined on a module level and written in all capital letters with underscores separating words. Examples include MAX_OVERFLOW and TOTAL.


# camelCasing - camelCasing for variable names. In general, Python prefers the underscore method but guides developers to defer to camelCasing if integrating into existing Python code that already uses that style. Readability counts


import os
import sys
from subprocess import Popen, PIPE

# Yes: easy to match operators with operands

TAX_RATE = 0.15 # constant

gross_wages = 120000
taxable_interest = 1000
dividends = 1000
qualified_dividends = 200
ira_deduction = 25000
student_loan_interest = 10000

income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)

print(income)

class CapWords:
	def __init__(self):
		self.word1='Cap'
		self.word2='Words'