#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv[1:]

    if args:
        result = sum(int(arg) for arg in args)
        print(result)
    else:
        print("0")
