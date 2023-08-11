
import os, sys, re, readline
from utils.errors import Errors
from utils.files import File

class tdlShell:
    
    def __init__(self) -> None:
        self.list = []
        self.done_list = []
        self.dir = os.path.dirname(os.path.abspath(__file__))
        self.list_path = os.path.join(self.dir, "../lists/list.txt")
        self.done_list_path = os.path.join(self.dir, "../lists/done.txt")
        self.help_file_path = os.path.join(self.dir, "../lists/help.txt")
        self.exit = False

    def doExit(self) -> bool:
        self.exit = True
        return self.exit

    def cmdShow(self) -> None:
        try:
            a2 = self.input.split(' ', 2)[1]
            if a2.isdigit():
                print(f"\n --- {self.list[int(a2)]} --- \n")
            elif a2 == "list":
                print("\n --- Objectives --- \n")
                for n, e in enumerate(self.list[1:]):
                    print(f"{n + 1}. {e}\n")
            elif a2 == "done":
                print("\n --- Completed --- \n")
                for n, e in enumerate(self.done_list[1:]):
                    print(f"{n + 1}. {e}\n")
            else:
                print(Errors.getErrorCmd("display_list"))
        except:
            print(Errors.getErrorCmd("display_list"))
            
    def cmdHelp(self) -> str:
        try:
            with open(self.help_file_path, 'r') as file:
                content = file.read()
                return content
        except FileNotFoundError:
            error = Errors.getErrorCmd("display_help")
            return error

    def cmdAdd(self) -> None:
        match = re.search(r'"([^"]*)"', self.input)
        if match:
            c = match.group(1)
            self.list.append(c)
            print(f"\n -- {c} -- \n --> Successfully added to the list!\n")
        else:
            print(Errors.getErrorCmd("add_to_list"))

    def cmdRemove(self) -> None:
        try:
            a2 = self.input.split(' ', 1)[1]
            r = self.list[int(a2)]
            self.list.pop(int(a2))
            print(f"\n -- {r} -- \n --> Successfully removed from the list!\n")
        except:
            print(Errors.getErrorCmd("remove_from_list"))

    def cmdDone(self) -> None:
        try:
            a2 = self.input.split(' ', 1)[1]
            if a2.isdigit():
                m = self.list[int(a2)]
                self.done_list.append(m)
                self.list.pop(int(a2))
                print(f"\n -- {m} -- \n --> Is now done!\n")
            elif a2 == "clear":
                self.done_list = [""]
                print("\n --> Completed list cleared!\n")
        except:
            print(Errors.getErrorCmd("done"))

    def cmdChange(self) -> None:
        try:
            a2 = self.input.split(' ', 2)[1]
            if a2.isdigit():
                o = self.list[int(a2)]
                
            def hook():
                readline.insert_text(o)
                readline.redisplay()

            readline.set_pre_input_hook(hook)
            i = str(input(f"\n --> "))
            readline.set_pre_input_hook()

            self.list[int(a2)] = i
            print(f"\n -- {i} -- \n --> Successfully changed!\n")
        except:
            print(Errors.getErrorCmd("change"))

    def cmdExit(self) -> None:
        while True:
            i = str(input("Save and quit? (y, N or c) "))
            match i:
                case "c":
                    print("Canceled.")
                    break
                case _ if re.search(r'^(N|[\s]*$).*', i):
                    print("Quiting without saving.")
                    self.doExit()
                    break
                case "y":
                    print("Saving files...")
                    File.overwriteFile(self.list_path, self.list)
                    File.overwriteFile(self.done_list_path, self.done_list)
                    self.doExit()
                    print("Quitting...")
                    break
                case _:
                    print(Errors.getErrorCmd("exit"))
                    pass
    
    def prompt(self) -> None:

        self.list = File.getLines(self.list_path, self.list)
        self.done_list = File.getLines(self.done_list_path, self.done_list)

        while self.exit is False:
            self.input = input("#TDL >>> ")
            a1 = self.input.split(' ', 2)[0]
            match a1:
                case "add":
                    self.cmdAdd()
                case "remove":
                    self.cmdRemove()
                case "change":
                    self.cmdChange()
                case "done":
                    self.cmdDone()
                case "show":
                    self.cmdShow()
                case "help":
                    print(self.cmdHelp())
                case "clear":
                    os.system('clear')
                case "exit":
                    self.cmdExit()
                case _:
                    print(Errors.getErrorCmd("prompt"))