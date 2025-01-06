#!/usr/bin/env python3

import sys
import os
from pathlib import Path

ROOT_DIR = Path(__file__).absolute().parent
DEPLOY_DIR = ROOT_DIR.joinpath('public')
DEFAULT_COMMIT_MESSAGE = 'Automatic deploy'


def info(msg: str) -> None:
    print()
    print(f'** {msg} ** ')
    print()


if __name__ == '__main__':
    if len(sys.argv) < 2:
        commit_msg = DEFAULT_COMMIT_MESSAGE
        print(f'No commit message given, using default "{commit_msg}"')
    else:
        commit_msg = sys.argv[1]

    info('Building pages')
    os.system(f'cd {ROOT_DIR} && hugo')

    info(f'Deploying pages with commit message "{commit_msg}"')
    os.system(f'cd {DEPLOY_DIR} && git add . && git commit -m "{commit_msg}" && git push -f origin gh-pages')

    info('Done')