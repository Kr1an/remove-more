"""Clean Path.

Module offers possibility to copy/move/delete by path does
not matter what is with in this path.

Example:
    clean_path.delete(path)

Todo:
    * add option upgrade with different politics.
    * write unittests
"""

import os
import shutil


def delete(path, options=None):
    try:
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
        return 0
    except Exception as e:
        print(e)
        return 1


def copy(src, dest, options=None):
    try:
        if os.path.isdir(src):
            shutil.copytree(src)
        else:
            shutil.copytree(src, dest)
        return 0
    except Exception as e:
        print(e)
        return 1


def move(src, dest, options=None):
    try:
        shutil.move(src, dest)
        return 0
    except Exception as e:
        print(e)
        return 1
