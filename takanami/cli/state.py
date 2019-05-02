#!/usr/bin/env python3
import os
import sys

def main():
    state = sys.argv[1] if len(sys.argv) == 2 else 'normal'

    from takanami.kishinami import Kishinami
    kishinami = Kishinami('kishinami')
    kishinami.changeState(state)

if __name__ == '__main__':
    main()
