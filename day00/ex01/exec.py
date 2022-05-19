
import sys


argLen = len(sys.argv)

if (argLen >= 2):
    ' '.join(sys.argv)[::-1].swapcase()
else:
    print("usage: <arg 1 , ..., arg n>")
