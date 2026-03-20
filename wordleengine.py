import os
import random
from collections import Counter

def filter_not_in_list(words_list: list, chars: str) -> list:
    return [word for word in words_list if not any(char in word for char in chars)]

def filter_appear_in_list(words_list: list, chars: str) -> list:
    return [word for word in words_list if all(char in word for char in chars)]

def filter_correct_place_in_list(words_list: list, chars: str) -> list:
    filtered_list = []
    for word in words_list:
        match = True
        for i, char in enumerate(chars):
            if char != " " and word[i] != char:
                match = False
                break
        if match:
            filtered_list.append(word)

    return filtered_list
                   
def suggested_best_words(words_list: list) -> list:
    if not words_list:
        return []

    freqs = get_letter_frequencies(words_list)
    
    scored_list = []
    for word in words_list:
        score = score_word(word, freqs)
        scored_list.append((word, score))
    
    scored_list.sort(key=lambda x: x[1], reverse=True)
    return [word for word, score in scored_list[:5]]

def score_word(word: str, frequencies: dict) -> int:
    score = 0

    for char in set(word):
        score += frequencies.get(char, 0)
    return score

def get_letter_frequencies(words_list: list) -> dict:
    all_letters = "".join(words_list)
    return Counter(all_letters)
    
def last_correction(words_list: list, char: str, index: int) -> list:
    return [word for word in words_list if char in word and word[index] != char]

def main():
    with open("slowa_correct.txt", "r") as f:
        words_list = f.read().splitlines()
    os.system('clear')
    print("Możesz wpisać maksymalnie 5 liter!")
    print(f"Schemat wpisywania liter - przykład: ab{"\033[48;5;189m"} {"\033[0m"}e{"\033[48;5;189m"} {"\033[0m"}d")
    print("Gdzie szare tła to spacje\n")


    not_in_list = input("Wpisz litery, które nie występują w wyrazie: ")
    
    appear_in_list = input("Wpisz litery, które występują w wyrazie, ale nie są na odpowiednim miejscu: ")
    while len(appear_in_list) > 5:
        appear_in_list = input("Wpisz litery, które nie występują w wyrazie: ")

    correct_place_in_list = input("Wpisz litery, które są na swoim miejscu: ")
    while len(correct_place_in_list) > 5:
        appear_in_list = input("Wpisz litery, które nie występują w wyrazie: ")
    
    first_filter = filter_correct_place_in_list(words_list, correct_place_in_list)
    second_filter = filter_appear_in_list(first_filter, appear_in_list)
    third_filter = filter_not_in_list(second_filter, not_in_list)
    suggestion = suggested_best_words(third_filter)

    print(f"Proponowane wyrazy: {suggestion} ")
    print("Wszystkie możliwe wyrazy (ilość) < 50: ")
    print(third_filter[:50])

    while True:
        char = input("\nWpisz żółtą literę do wykluczenia z pozycji: ").lower()
        if char == 'exit' or not char:
            break
            
        try:
            idx = int(input(f"Na której pozycji (1-5) litera '{char}' jest żółta: ")) - 1
            if 0 <= idx <= 4:
                fourth_filter = last_correction(third_filter, char, idx)
                
                new_suggestions = suggested_best_words(fourth_filter)
                print(f"\nZaktualizowane propozycje: {new_suggestions}")
                print(f"Pozostało słów: {len(fourth_filter)}")
                print(fourth_filter[:50])
            else:
                print("Indeks musi być w zakresie 1-5")
        except ValueError:
            print("Podaj poprawną liczbę jako indeks")




main()

                   
