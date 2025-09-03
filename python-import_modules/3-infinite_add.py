#!/usr/bin/python3
import sys
# prints the summation of all its numeric command line arguments
if __name__ == "__main__":
    count = len(sys.argv)
    count -= 1
    result = 0
    if count == 0:
        print("{}".format(count))
    else:
        for i in range(1, len(sys.argv)):
            result += int(sys.argv[i])
        print("{}".format(result))
