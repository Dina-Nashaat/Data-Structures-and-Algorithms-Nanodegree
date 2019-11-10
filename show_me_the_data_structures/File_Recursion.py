import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    paths_list = []
    for entry in os.listdir(path):
        full_path = path + '/' + entry
        if os.path.isdir(full_path):
            paths_list = paths_list + find_files(suffix, full_path)
        else:
            if (entry.endswith(suffix)):
                paths_list.append(full_path)
    return paths_list
    
print(find_files('.c', './testdir'))