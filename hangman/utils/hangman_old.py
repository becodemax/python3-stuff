
class Hangman:

    def play():

        import random
        possible_words = ["becode", "learning", "mathematics", 
                          "sessions", "easter", "skyrim", 
                          "minecraft", "water", "hashtag", 
                          "python", "coding", "script"]
        word_to_find = random.choice(possible_words)
        lives = 5
        turn_count = 0
        error_count = 0
        correct_guessed_letters = ["_"]*len(word_to_find)
        well_guessed_letters = []
        correct_letters = []
        wrongly_guessed_letters = []
        
        # adding all letters of the word to the list correct_letters 
        for char in word_to_find:
            correct_letters.append(char)

        # game loop start
        while True:

            # displays status of the game (optionnal)
            print("--> ", " ".join(correct_guessed_letters), " <--")
            print("Found letters : ", " ".join(well_guessed_letters))
            print("Wrong letters : ", " ".join(wrongly_guessed_letters))
            print(f"Error count : {error_count}")
            print(f"Turn count : {turn_count}")
            print(f"Lives left : {lives}")

            # input and turn count
            input_letter = str(input("Enter a letter : "))
            turn_count += 1

            # conditions verifying that the input is nothing but alpha
            if input_letter == word_to_find:
                print(f'You already found the word! It was "{word_to_find}"!')
                break
            elif input_letter.isalpha() and len(input_letter) == 1:
                print(f"You chose {input_letter}!")
            else:
                print(f"--- {input_letter} not valid! Please only enter a letter! ---")
                continue

            # for loop and conditions to verify if the input letter is in the word to find
            for char in word_to_find:

                if input_letter not in correct_letters:
                    if input_letter not in wrongly_guessed_letters:
                        lives -= 1
                        wrongly_guessed_letters.append(input_letter)
                else:
                    if input_letter not in well_guessed_letters:
                        well_guessed_letters.append(input_letter)

            # errors count = length of the wrongly_guest_letters list
            error_count = len(wrongly_guessed_letters)

            # condition that stops the game if lives < 0
            if lives < 0:
                print(f'Oh oh! No lives left! The word was "{word_to_find}". Try again!')
                break
            
            # for loop of visual list in terminal gradually filling underscores with letters
            for n, l in enumerate(word_to_find):
                if l == input_letter:
                    correct_guessed_letters[n] = input_letter

            # condition making the game stop if all letters have been found
            if correct_guessed_letters == correct_letters:
                print(f'You found the word "{word_to_find}" in {turn_count} turns with {error_count} errors!')
                break