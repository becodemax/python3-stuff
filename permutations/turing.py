
import time, os

class Turing:
    def __init__(self) -> None:
        self.word = ""
        self.wlist = []
        self.exit = False
        self.dir = os.path.dirname(os.path.abspath(__file__))

    def getPerms(self, string) -> list:
        s = string
        if len(s) == 0:
            return ['']
        
        first_char = s[0]
        rest = s[1:]
        permutations = self.getPerms(rest)
        result = []

        for perm in permutations:
            for i in range(len(perm) + 1):
                new_perm = perm[:i] + first_char + perm[i:]
                result.append(new_perm)
        
        return result
    
    def rmDuplicateAdjacent(self, list) -> list:
        result = []
        prev = None

        for i in list:
            if i != prev:
                result.append(i)
                prev = i
        
        return result

    def savePerms(self) -> None:
        try:
            self.file_path = os.path.join(self.dir, f"{self.word}.txt")
            with open(self.file_path, 'w+') as f:
                for p in self.wlist:
                    f.write(f"{p}\n")
            print(f"File saved at {self.file_path}.")
        except:
            print("Error: saving file not found.")

    def mesureTime(self, start, end) -> str:
        t = end - start
        return f"Time taken: {t:.6f}s."
    
    def prompt(self) -> None:
        i = input("Enter a word or type [ exit ]: ")
        if i == "exit":
            self.exit = True
        else:
            self.word = i
    
    def exec(self) -> int:
        while self.exit is False:
            self.prompt()
            if self.exit is False:
                print("Permutating, please wait...")
                start_time = time.time()
                perms_list = self.getPerms(self.word)
                end_time = time.time()
                print("Done.")
                print(self.mesureTime(start_time, end_time))

                print("Removing duplicates...")
                start_time = time.time()
                self.wlist = self.rmDuplicateAdjacent(perms_list)
                end_time = time.time()
                removed_number = len(perms_list) - len(self.wlist)
                print(f"Duplicates removed: {removed_number}")
                print(self.mesureTime(start_time, end_time))
                print(f"Total permutations: {len(self.wlist)}")

                print("Saving file...")
                start_time = time.time()
                self.savePerms()
                end_time = time.time()
                print(self.mesureTime(start_time, end_time))
            else:
                print("Quitting...")

script = Turing()
script.exec()