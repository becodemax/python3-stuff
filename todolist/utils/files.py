
from utils.errors import Errors
import sys, re

class File:

    def getLines(file, list) -> list:
        try:
            with open(file, 'r') as f:
                for line in f:
                    list.append(line.strip())
        except FileNotFoundError:
            print(Errors.getErrorFile("open_file", file))
            sys.exit(1)
        
        return list
    
    def overwriteFile(file, list) -> bool:
        print(f"Saving {file}...")
        try:
            with open(file, 'r+') as f:
                text = f.read()
                text = re.sub('foobar', 'bar', text)
                f.seek(0)
                for e in list:
                    f.write(f"{e}\n")
                f.truncate()
            print("Done.")
        except FileNotFoundError:
            print(Errors.getErrorFile("open_file", file))