import glob
import ntpath

def install_and_import(package):
    import importlib
    try:
        importlib.import_module(package)
    except ImportError:
        import pip
        pip.main(['install', package])
    finally:
        globals()[package] = importlib.import_module(package)

# import a library to detect encodings
install_and_import('chardet')

from tkinter import filedialog
from tkinter import *
from pathlib import Path

root = Tk()
root.withdraw()


def main():
    directory = Path(filedialog.askdirectory()).glob('*.*')
    
    # for every file in the given directory, print the file name & a gues of its file encoding
    print("File".ljust(45), "Encoding")
    for filename in directory:
        with open(filename, 'rb') as rawdata:
            result = chardet.detect(rawdata.read())
        print(ntpath.basename(filename).ljust(45), result['encoding'])


if __name__ == '__main__': main()
    