import random

class Hangman:
    def __init__(self) -> None:
        self.wlist = ["becode", "learning", "mathematics", "sessions", "easter", "skyrim", "minecraft", "water", "hashtag", "python", "coding", "script"]
        self.w2find = str(random.choice(self.wlist))
        self.orgl = ["_" for _ in self.w2find]
        self.gsdl = []
        self.wrgl = []
        self.turn = 0
        self.lives = 5

    def displayGame(self) -> None:
        print("--> ", " ".join(self.orgl), " <--")
        print("Found letters : ", " ".join(self.gsdl))
        print("Wrong letters : ", " ".join(self.wrgl))
        print(f"Error count : {len(self.wrgl)}")
        print(f"Lives left : {self.lives}")
        
    def processLetter(self) -> None:
        if self.input not in self.w2find:
            if self.input not in self.wrgl:
                self.wrgl.append(self.input)
                self.lives -= 1
        else:
            if self.input not in self.gsdl:
                self.gsdl.append(self.input)

    def setCorrectLetters(self) -> None:
        for n, l in enumerate(self.w2find):
            if l == self.input:
                self.orgl[n] = self.input

    def processInput(self) -> bool:
        if self.input == self.w2find:
            self.message = f'You already found the word! It was "{self.w2find}"!'
            return True
        elif "_" not in self.orgl:
            self.message = f'You found the word "{self.w2find}" in {self.turn} turns with {len(self.wrgl)} errors!'
            return True
        elif self.input == "" or len(self.input) != 1 or not self.input.isalpha():
            self.message = f"{self.input} isn't valid!"
            return False
        else:
            self.setCorrectLetters()
            self.processLetter()
            
    def game(self) -> None:
        while True:

            self.turn += 1
            self.displayGame()
            self.input = input("Enter a letter: ")
            self.processInput()

            if self.processInput() == False:
                print(self.message)
            elif self.processInput() == True:
                print(self.message)
                break
            elif self.lives < 0:
                self.message = f'Oh oh! No lives left! The word was "{self.w2find}". Try again!'
                print(self.message)
                break

    def start(self) -> None:
        self.game()