import os

# ==========================================
# RECURSIVE DFS EXPLORER (Depth-First Search)
# ==========================================

def get_dir_stats(path):

    
    # Goes through the given directory and it's subdirectories
    # recursively and counts the total amount of files and their total size.
    

    total_size = 0
    total_files = 0
    
    # BASE CASE. PermissionError check to make sure program doesn't crash
    # because of insufficient permissions, but rather returns 0 files and 0
    # directories instead and stops the recursion here.
    
    try:
        items = os.listdir(path)
        # print(f"directory list is: {items}")

    except PermissionError:
        return 0, 0
    
    # Traversal

    for item in items:
        # print(f"current singular item from list is: {item}")
        # os.path.join is save way to combine the path and file name
        # E.g, "directory" + "file.txt" -> "directory/file.txt"

        full_path = os.path.join(path, item)

        # If target path is a file, add it to total_size
        # Base Case

        if os.path.isfile(full_path):
            total_size += os.path.getsize(full_path)
            total_files += 1

        # If target path is directory, call this function again recursively
        elif os.path.isdir(full_path):
            # Recursive Call: calls the same function with a new path
            # Program stops here to wait that all the subdirectories and
            # their sub-directories have been gone through

            sub_size, sub_files = get_dir_stats(full_path)

            # After recursion returns, add the results from subdirectory to the count
            total_size += sub_size
            total_files += sub_files

    # Optional Debugging-print: shows the order of completion for the directories
    # Because this is DFS, we see the deepest directories first and, after that the root directory.        
    # print(f"--- Managed to count directory: {path} (Size: {total_size}) ---")

    return total_size, total_files


def main():

    path_to_scan = ".." # one-directory above current (parent)

    # start recursion
    size, files = get_dir_stats(path_to_scan)

    # change bytes in to megabytes for readability
    size_mb = size / (1024 * 1024)
    print(f"\nDirectory '{path_to_scan}' contains {files} files. Total size in {size_mb:.2f} MB.")
    print(f"Total size in bytes is: {size} bytes")

if __name__ == "__main__":
    main()