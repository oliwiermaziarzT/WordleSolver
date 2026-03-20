# Wordle PL

Konsolowa gra Wordle w języku polskim wraz z asystentem do rozwiązywania zagadek.

---

## Pliki

| Plik | Opis |
|---|---|
| `createwords.py` | Filtruje słownik do słów 5-literowych → `slowa_correct.txt` |
| `main.py` | Główna gra Wordle w terminalu |
| `wordleengine.py` | Asystent pomagający odgadnąć słowo |

---

## Wymagania

- Python 3.x
- Plik `slowa.txt` — słownik języka polskiego ze strony [https://sjp.pl/sl/growy/](https://sjp.pl/sl/growy/)

---

## Uruchomienie

```bash
# 1. Przygotuj słownik
python createwords.py

# 2. Zagraj
python main.py

# 3. Lub użyj silnika
python wordleengine.py
```

---
