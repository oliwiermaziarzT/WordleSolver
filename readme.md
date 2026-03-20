# Wordle PL

Wordle w terminalu w języku polskim wraz z silnikiem do rozwiązywania zagadek.

---

## Pliki

| Plik | Opis |
|---|---|
| `createwords.py` | Filtruje słownik do słów 5-literowych |
| `main.py` | Główna gra Wordle w terminalu |
| `wordleengine.py` | Silnik odgadujący wyraz |

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
