def main():
    slownik_correct = []

    with open("slowa.txt", "r", encoding="utf-8") as f:
        slownik = f.read().splitlines()
    
    for slowo in slownik:
        if len(slowo) == 5:
            slownik_correct.append(slowo)
        else:
            continue

    with open("slowa_correct.txt", "w", encoding="utf-8") as f:
        for slowo in slownik_correct:
            f.write(f"{slowo}\n")
    print(slownik_correct)

main()