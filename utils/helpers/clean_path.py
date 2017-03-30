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
    """Delete Function
    
    Function allow deleting object by path. Work similar with file/dir/link.
    If dir, remove recursively.
    
    Parameters:
        path: object location.
        options: list of deleting politics.
    
    Returns:
        value: 0 - successful, 1 - fail.
    
    """
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
    """Copy Function

        Function allow to copy object by path. 
        Work similar with file/dir/link. If dir, copy recursively.

        Parameters:
            src: object location.
            dest: object copying path.
            options: list of copying politics.

        Returns:
            value: 0 - successful, 1 - fail.

        """
    try:
        if os.path.isdir(src):
            shutil.copytree(src, dest)
        else:
            shutil.copy(src, dest)
        return 0
    except Exception as e:
        print(e)
        return 1


def move(src, dest, options=None):
    """Delete Function

    Function allow deleting object by path. Work similar with file/dir/link.
    If dir, move recursively.

    Parameters:
        src: object location.
        dest: object destination location.
        options: list of moving politics.

    Returns:
        value: 0 - successful, 1 - fail.

    """
    try:
        shutil.move(src, dest)
        return 0
    except Exception as e:
        print(e)
        return 1
