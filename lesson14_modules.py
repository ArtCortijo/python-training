# Lesson 14
# https://docs.python.org/3/py-modindex.html

import math  # or from math import pi and then print(pi)
# This module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter. It is always available.
import sys
import random as rdm  # import as alias
# Enumerations in Python are implemented by using the module named “enum“. Enumerations are created using classes. Enums have names and values associated with them. Let’s cover the different concepts of Python Enum in this article.
from enum import Enum
import lesson14_kansas  # import from another file
from lesson14_rps7 import rock_paper_scissors

print(math.pi)
print(rdm.choice("3216546954"))

# for item in dir(rdm):
#     print(item)

# print(lesson14_kansas.capital)
# lesson14_kansas.randomFunFact()

print(__name__)
print(lesson14_kansas.__name__)

rock_paper_scissors()
