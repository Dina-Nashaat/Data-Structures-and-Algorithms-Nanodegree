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
    if(os.path.exists(path)):
        for entry in os.listdir(path):
            full_path = path + '/' + entry
            if os.path.isdir(full_path):
                paths_list = paths_list + find_files(suffix, full_path)
            else:
                if (entry.endswith(suffix)):
                    paths_list.append(full_path)
        return paths_list
    else:
        print(f"{path} does not exist")
    
    
print('Test 1', find_files('.c', './testdir'))
print('Test 2', find_files('.c', './emptydir'))
print('Test 3', find_files('.txt', './testdir'))
print('Test 4', find_files('.c', './empty'))