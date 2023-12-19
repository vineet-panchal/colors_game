import random

colors = ["R", "G", "B", "W", "P", "O"]
tries = 10
codeLength = 4

def generate_secret():
    code = []
    for _ in range(codeLength):
        color = random.choice(colors)
        code.append(color)
    return code

def guess_secret():
    while True:
        guess = input("Guess: ").upper().split(" ")
        if len(guess) != codeLength:
            print(f"You must guess {codeLength} colors.")
            continue
        for item in guess:
            if item not in colors:
                print(f"Invalid color: {item}. Try again.")
                break
        else:
            break
    return guess

def check_code(guess, realCode):
    count = {}
    correctPOS = 0
    incorrectPOS = 0
    
    for item in realCode:
        if item not in count:
            count[item] = 0
        count[item] += 1
    
    for guess_color, real_color in zip(guess, realCode):
        if guess_color == real_color:
            correctPOS += 1
            count[guess_color] -= 1
    
    for guess_color, real_color in zip(guess, realCode):
        if guess_color in count and count[guess_color] > 0:
            incorrectPOS += 1
            count[guess_color] -= 1
            
    return correctPOS, incorrectPOS

def game():
    print("Welcome to the Color Game!")
    print("")
    print(f"You have {tries} to guess the secret code.")
    print("The valid colors are", *colors)
    print("")
    
    code = generate_secret()
    for attempts in range(1, tries + 1):
        guess = guess_secret()
        correctPOS, incorrectPOS = check_code(guess, code)
        
        if correctPOS == codeLength:
            print(f"Congratulations! You've guessed it right in {attempts} tries.")
            break
        
        print(f"Correct Positions: {correctPOS} | Incorrect Positions: {incorrectPOS}")
    else:
        print("Sorry, you didn't guess it. The secret code was: ", *code)

if __name__ == "__main__":
    game()