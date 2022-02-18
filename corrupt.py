from sys import argv
import os

ZWS = '​'
PREFIX = 'c_'


# This function Corrupts the source_file
# returns True if successfully corrupted otherwise returns False
def corrupt(path: str, source_file: str) -> bool:
    FULL_PATH = path + os.sep + source_file
    try:
        reader = open(FULL_PATH, 'r', encoding='utf-8')
    except:
        print("File {} not found".format(FULL_PATH))
        return False

    print(f"😈 Corrupting file {source_file} ... ")
    writer = open(path + os.sep + PREFIX + source_file, 'w', encoding='utf-8')

    while True:
        line = reader.readline()
        if not line:
            break

        writer.write(line
                     .replace('(', '{0}{1}'.format('(', ZWS))
                     .replace(')', '{1}{0}'.format(')', ZWS))
                     .replace('{', '{0}{1}'.format('{', ZWS))
                     .replace('}', '{1}{0}'.format('}', ZWS))
                     )

    reader.close()
    writer.close()
    return True


def main():
    if len(argv) < 2:
        print("Usage: python corrupt.py path_of_file")
        print("\nThe path of file can be absolute path")
        print("\nExample: python corrupt.py corrupt.py")
        print("This corrupts the corrupted and stores it as c_corrupt.py")
    else:
        for i in range(len(argv) - 1):
            split = os.path.split(argv[i + 1])

            if split[0] == '':
                split = ('./', split[1])

            if not os.path.exists(argv[-1]):
                print(f"🔍 The file {argv[-1]} does not exist")
            elif not corrupt(split[0], split[1]):
                print(f"😩 Could not corrupt {argv[i + 1]}")
            else:
                print(f"💀 Corrupted {split[1]} into {PREFIX}{split[1]}")

if __name__ == '__main__':
    main()
