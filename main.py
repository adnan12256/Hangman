from wonderwords import RandomSentence

hangman = [""" 
               +--+
               |  |
                  |
                  |
                  |
                  |
                  |
              =====""",
           """ 
               +--+
               |  |
               0  |
                  |
                  |
                  |
                  |
              =====""",
           """ 
               +--+
               |  |
               0  |
               |  |
                  |
                  |
                  |
              =====""",
           """ 
                +--+
               |  |
               0  |
              /|  |
                  |
                  |
                  |
              =====""",
           """ 
               +--+
               |  |
               0  |
              /|\ |
                  |
                  |
                  |
              =====""",
           """
               +--+
               |  |
               0  |
              /|\ |
               |  |
                  |
                  |
              =====""",
           """
               +--+
               |  |
               0  |
              /|\ |
               |  |
              /   |
                  |
              =====""",
           """
               +--+
               |  |
               0  |
              /|\ |
               |  |
              / \ |
                  |
              ====="""]


print("```````````````````````````````````````````````````````````````````````````````````````````````````````````````")
print("Welcome to the Hangman Game!")


# This function generates a random sentence
def get_sentence():
    gen = RandomSentence()
    sentence = gen.sentence()
    # sentence = "The filthy sail pumps tear."
    return sentence


# This function converts the sentence passed to it into dashed format
def sentence_to_dashes(sentence):
    new_string = ""
    for letter in sentence:
        if letter.isalnum():
            letter = "_"
            new_string += letter
        else:
            new_string += letter
    return new_string


# This function updates the dashed sentence with the letter included if the letter is in the sentence
def update_dashed(sentence, index, matched_letter):
    temp_str = ""
    for i, letter in enumerate(sentence):
        if i in index:
            if i == 0:
                temp_str += matched_letter.upper()
            else:
                temp_str += matched_letter
        else:
            temp_str += letter
    return temp_str


# This function gets the index of when the inputted letter occurs in the generated sentence
def get_letter_index(input):
    index = []
    for i, letter in enumerate(sent):
        letter = letter.lower()
        if letter == input.lower():
            matched_letter = letter
            index.append(i)
    return index


# sent contains the generated sentence
sent = get_sentence()

# dashed_sent contains the sentence letters dashed out in a new string
dashed_sent = sentence_to_dashes(sent)

game = True
fail = 0
while True:
    fail = 0
    success_turn = 0
    guessed_letters = []
    input_settings = input("Press 1 to play, 2 for instructions or anything else to quit: ")
    print(hangman[fail])
    if input_settings == "1":
        print(dashed_sent + "\n")
        while game:
            # Exiting Case
            letter_input = input("Guess your letter or \"exit\" to quit: ")
            if letter_input == "exit":
                exit(0)

            # Invalid Input Case
            elif len(letter_input) > 1 or letter_input == " " or letter_input == "":
                print("```````````````````````````````````````````````````````````````````````````````````````````````````````````````")
                print("Invalid input! Try again")
                print("```````````````````````````````````````````````````````````````````````````````````````````````````````````````")

            # Letter Already Guessed Case
            elif letter_input in guessed_letters:
                print("```````````````````````````````````````````````````````````````````````````````````````````````````````````````")
                print("You already guessed this letter! Try again")
                print("```````````````````````````````````````````````````````````````````````````````````````````````````````````````")
                pass

            # Letter Not Guessed And Not In The Sentence Case
            elif letter_input not in sent:
                fail += 1
                print(hangman[fail])
                print("\n```````````````````````````````````````````````````````````````````````````````````````````````````````````````")
                print(f"Worng letter! Fail count = {fail}")
                guessed_letters.append(letter_input)
                print("```````````````````````````````````````````````````````````````````````````````````````````````````````````````\n")
                if fail == 7:
                    print("Game ended! You couldnt guess the sentence!\n")
                    print(f"Your Sentence was: {sent}")
                    break

            # Letter Not Guessed And Is In Sentence Case
            elif letter_input not in guessed_letters and letter_input in sent:
                guessed_letters.append(letter_input.lower())
                index = get_letter_index(letter_input)
                success_turn += 1
                if success_turn > 1:
                    update_sentence = update_dashed(update_sentence, index, letter_input)
                    print(update_sentence)
                    print(f"Guessed letters : {', '.join(map(str, guessed_letters))}\n")
                    if update_sentence == sent:
                        print("You guessed the sentence successfully!\n")
                        break
                else:
                    update_sentence = update_dashed(dashed_sent, index, letter_input)
                    print(update_sentence)
                    print(f"Guessed letters : {', '.join(map(str, guessed_letters))}\n")

    elif input_settings == "2":
        print("\nYou will have to guess the random computer generated sentence one letter at a time. You can only guess"
              " wrong upto 7 times. After 7 wrong guesses, the game will end!\n")

    else:
        exit(0)
