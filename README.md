hacker calc
=================

A simple command line tool to aid in adding, subtracting, xor'ing, rol'ing, ror'ing, etc data of various sizes. ADD/SUB/ROT operations wrap as one would expect while debugging. 

**USAGE**

+ python hc.py [OPTIONS] CALCULATION
+ Options:
  + --wordsize INTEGER    Size of data being calculated (default: 8) [a byte]
  + --base INTEGER        Base of data being calculated (default: 16 (hex))
  + --ascii / --no-ascii  Print result as ASCII character (default: False)
  + --help                Show this message and exit.

+ Supports hex, decimal, and binary literals

+ Examples:
  + python hc.py 0x7F XOR 0x3B ROL 0x21
    + result: 0x88
  +  python hc.py --ascii 0x41 ROL 0x2d
    + result: (
    
+ Requirements: python 3.4, click
