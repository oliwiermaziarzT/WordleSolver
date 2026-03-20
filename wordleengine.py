import os
from collections import Counter
import time

def filter_not_in_list(words_list, chars):
    return [word for word in words_list if not any(char in word for char in chars)]

def filter_appear_in_list(words_list, chars):
    return [word for word in words_list if all(char in word for char in chars)]

def filter_correct_place_in_list(words_list, pattern):
    filtered_list = []
    for word in words_list:
        if len(pattern) > len(word): continue 
        match = True
        for i, char in enumerate(pattern):
            if char != " " and word[i] != char:
                match = False
                break
        if match:
            filtered_list.append(word)
    return filtered_list

def get_letter_frequencies(words_list):
    all_letters = "".join(words_list)
    return Counter(all_letters)

def score_word(word, frequencies):
    return sum(frequencies.get(char, 0) for char in set(word))

def suggested_best_words(words_list):
    if not words_list:
        return []
    freqs = get_letter_frequencies(words_list)
    scored_list = [(word, score_word(word, freqs)) for word in words_list]
    scored_list.sort(key=lambda x: x[1], reverse=True)
    return [word for word, score in scored_list[:5]]

def last_correction(words_list, char, index):
    return [word for word in words_list if char in word and word[index] != char]

def basic_menu(words_list):
    while True:
        os.system('clear' if os.name == 'posix' else 'cls')
        print("--- Basic Filtering ---")
        print("Tip: Use spaces for unknown letters")
        
        not_in = input("Letters NOT in word: ").lower()
        if not_in == 'back': return words_list
        
        appear_in = input("Letters in word but WRONG spot: ").lower()
        if appear_in == 'back': return words_list
        
        correct_place = input("Letters in CORRECT spot (max 5): ").lower()
        if correct_place == 'back': return words_list

        inputs = [not_in, appear_in, correct_place]
        if not all(all(c.isalpha() or c.isspace() for c in i) for i in inputs):
            print("\nError: Only characters and spaces are allowed!")
            time.sleep(1.5)
            continue
        
        if len(correct_place) > 5:
            print("\nError: Pattern too long (max 5)!")
            time.sleep(1.5)
            continue

        filtered = words_list
        if correct_place.strip():
            filtered = filter_correct_place_in_list(filtered, correct_place)
        if appear_in.strip():
            filtered = filter_appear_in_list(filtered, appear_in.strip())
        if not_in.strip():
            filtered = filter_not_in_list(filtered, not_in.strip())
            
        suggestions = suggested_best_words(filtered)
        print(f"\nSuggestions: {suggestions}")
        print(f"Possible matches ({len(filtered)}): {filtered[:20]}...")
        
        ans = input("\nPress Enter to apply filters or type 'back' to discard: ").lower()
        if ans == 'back':
            return words_list 
        else:
            return filtered 

def main():
    with open("slowa_correct.txt", "r", encoding="utf-8") as f:
        words_list = f.read().splitlines()

    while True:
        os.system('clear' if os.name == 'posix' else 'cls')
        print("*** Welcome to WordleSolver ***\n")
        print("1. 'filter' - update possible words")
        print("2. 'refine' - exclude yellow letter from specific position")
        print("3. 'exit'   - quit\n")
        
        choice = input("Choice: ").strip().lower()

        if choice == "exit":
            break
        elif choice == "filter":
            words_list = basic_menu(words_list)
        elif choice == "refine":
            refine_menu(words_list)

def refine_menu(current_list):
    if not current_list:
        print("List is empty")
        time.sleep(1)
        return

    while True:
        os.system('clear' if os.name == 'posix' else 'cls')
        print(f"--- Refine List (Remaining: {len(current_list)}) ---")
        suggestions = suggested_best_words(current_list)
        print(f"Suggestions: {suggestions}")
        print(f"Matches: {current_list[:15]}...\n")

        char = input("Which letter to exclude from a specific position? (or 'back'): ").lower().strip()
        
        if char == 'back': 
            break
        
        if not char.isalpha() or len(char) != 1:
            print("Please enter a single letter.")
            time.sleep(1)
            continue
        
        try:
            pos_input = input(f"At which position (1-5) is '{char}' wrong? ")
            if pos_input.lower() == 'back': break
            
            pos = int(pos_input) - 1
            
            if 0 <= pos <= 4:
                new_list = last_correction(current_list, char, pos)
                if not new_list:
                    print(f"\nAction cancelled")
                    time.sleep(2)
                else:
                    current_list.clear()
                    current_list.extend(new_list)
            else:
                print("Invalid position! Use numbers 1-5.")
                time.sleep(1)
        except ValueError:
            print("Invalid input! Please enter a number.")
            time.sleep(1)

if __name__ == "__main__":
    main()