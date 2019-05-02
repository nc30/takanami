#!/usr/bin/env python3

import sys

from takanami.dynamodb import getStack
from takanami.lambda_controll import invoke

TABLE_NAME = 'infra.status'
KEY_NAME = 'takanami_stack'

constractors = {
    "1": 'CH4JWCPNY',
    "2": 'C9TNT0Q0P'
}

def main():
    stack = getStack()

    item = stack.stack()

    for v in sys.argv[1:]:
        if v in constractors.keys():
            item['slack'][constractors[v]] = None

    stack.save(item)

    invoke(
        FunctionName="notice_check",
    )

if __name__ == '__main__':
    main()
