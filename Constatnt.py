# To make something constant make sure to Use Capital or Upper case naming convention
CONST=62
print(CONST)
CONST=63
print(CONST)
# From above example it is clear that we are not able to make Constatnt using UPPERCASE Naming convention

#Solution to make anything Constant 
# Approach one 
from typing import Final
VERSION:Final[str]="6.25.35"
VERSION="7.6.52"
print(VERSION) 
"""The code will run without errors, and it will print 7.6.52, even though VERSION was originally declared as a Final. This is because Python does not prevent you from reassigning a variable marked as Final."""


