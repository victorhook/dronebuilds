#!/usr/bin/env python3

import sys
from pathlib import Path
from datetime import datetime

ROOT_DIR = Path(__file__).absolute().parent


if __name__ == '__main__':
    print('Creating new post')
    name = input('Name: ')
    
    posts_dir = ROOT_DIR.joinpath('content', 'posts')
    new_dir = posts_dir.joinpath(name)
    if new_dir.exists():
        print(f'Post with name "{name}" already exists, aborting.')
        sys.exit(0)

    title = input('Title: ')

    new_dir.mkdir()
    new_dir.joinpath('resources').mkdir()
    index_md = new_dir.joinpath('index.md')

    current_time = datetime.now().astimezone().isoformat(timespec='seconds')

    with open(index_md, 'w') as f:
        f.write('+++\n')
        f.write(f'date = \'{current_time}\'\n')
        f.write('draft = false\n')
        f.write(f'title = \'{title}\'\n')
        f.write('tags = []\n')
        f.write('+++\n')

    print(f'New post created at {new_dir}')