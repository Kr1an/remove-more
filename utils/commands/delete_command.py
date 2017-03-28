import os
import glob


def delete(paths, options):
    deleting_list = get_list_of_files_to_delete(paths, options)
    if 'with_no_bin' in options['mods']:
        copy_to_bin(deleting_list)

    _delete(deleting_list)


def copy_to_bin(deleting_list):
    pass


def get_list_of_files_to_delete(paths, options):
    deleting_list = set([val for path in paths for val in glob.glob(path)])
    deleting_list = [os.path.abspath(rel_path) for rel_path in deleting_list]
    return deleting_list


def _delete(deleting_list):
    print(deleting_list)
