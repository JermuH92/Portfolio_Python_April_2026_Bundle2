import os

def get_dir_stats(path):
    total_size = 0
    total_files = 0
    
    
    try:
        items = os.listdir(path)
        # print(f"directory list is: {items}")

    except PermissionError:
        return 0, 0
    
    for item in items:
        # print(f"current singular item from list is: {item}")

        full_path = os.path.join(path, item)

        # If target path is a file, add it to total_size
        # If target path is directory, call this function again

        if os.path.isfile(full_path):
            total_size += os.path.getsize(full_path)
            total_files += 1

        elif os.path.isdir(full_path):
            # Recursive Call
            sub_size, sub_files = get_dir_stats(full_path)

            total_size += sub_size
            total_files += sub_files
            
    print(f"--- Managed to count directory: {path} (Size: {total_size}) ---")
    return total_size, total_files


def main():

    path_to_scan = ".." 
    size, files = get_dir_stats(path_to_scan)
    size_mb = size / (1024 * 1024)
    print(f"\nDirectory '{path_to_scan}' contains {files} files. Total size in {size_mb:.2f} MB.")
    print(f"Total size in bytes is: {size} bytes")

if __name__ == "__main__":
    main()