#!/usr/bin/env python3
import sys
from . import stubber


def main(*args, **kwargs):
    target = sys.argv[1]
    print(stubber.get_stubfile(target))


if __name__ == '__main__':
    main()
