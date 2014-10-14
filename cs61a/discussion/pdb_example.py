#import pdb # Not necessary if you do `python3 -m pdb classes.py`
#pdb.set_trace() # Call this when you want to start a debugging session in the middle of your program
class A:
    a = 2
    def __init__(self, tag):
        self.tag = tag

a = A(4)
b = A(4)

# For more information about pdb, go to https://docs.python.org/3.4/library/pdb.html
