import glob
import time
import sys
import os.path

monitored_paths = ['folder1', 'folder2', 'folder3', 'folder1/subfolder']
check_interval = 1

if __name__ == "__main__":
    while True:
        time.sleep(check_interval)
        for path in monitored_paths:
            if os.path.exists(path):
                files = glob.glob(path + '/' + '*', recursive=True)
                if files:
                    print(path + ' ' + "Folder is not empty")
                print("Total files in " + path + ' : ' + str(len(files)))
                for file in files:
                    print(file)
            else:
                print(path + " path does not exist")
                sys.exit(1)
