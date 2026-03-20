import os
import random

def main():
    with open("slowa_correct.txt", "r") as f:
        words_list = f.read().splitlines()

    word = random.choice(words_list)
    guesses = []
    user_guess = ""

    ZOLTY = "\033[1;43m"
    CZERWONY = "\033[1;41m"
    ZIELONY = "\033[1;42m"
    RESET = "\033[0m"
    whitespace = " "

    while (user_guess != word) and (len(guesses) < 5):
        result = ""
        print(f"{whitespace * 10}Próba: {len(guesses) + 1}")
        user_guess = input("Wprowadź pięcioliterowe słowo: \n").strip()

        while len(user_guess) != 5:
            user_guess = input("Wpisz tylko 5 liter: \n").strip()
            if len(user_guess) != 5:
                user_guess = input("Introduce 5 letras aqui!!:").strip()
        os.system('clear')
        print("\n")
        if user_guess != word:
            for i in range(len(user_guess)):
                if user_guess[i] == word[i]:
                    result += ZIELONY + user_guess[i] + RESET
                elif user_guess[i] in word:
                    result += ZOLTY + user_guess[i] + RESET
                else:
                    result += CZERWONY +user_guess[i] + RESET
            guesses.append(result)
        else:
            result += ZIELONY + user_guess + RESET
            guesses.append(result)
            print(f"{whitespace * 4}Brawo zgadłeś słowo!")
            for guess in guesses:
                print(f"{whitespace * 10}" + guess)
            return
        
        print(f"{whitespace * 2}Twoje próby odgadnięcia:")
        for guess in guesses:
            print(f"{whitespace * 10}" + guess)
        print("\n")
        


    print(f"Niestety, nie udało się odgadnąć słowa. Prawidłowe słowo to: {word}")

main()

