Wordle Toolset
Zestaw narzędzi w Pythonie do gry w Wordle: od gry terminalowej, po inteligentny algorytm podpowiadający najlepsze słowa.

Funkcje
Game Emulator: Klasyczna gra Wordle w terminalu z kolorowymi oznaczeniami (Zielony/Żółty/Czerwony).

Smart Solver: Filtrowanie bazy słów na podstawie trafień i sugestie oparte na częstotliwości występowania liter.

Dictionary Utility: Skrypt do automatycznego przygotowania bazy pięcioliterowych słów.

Struktura plików
main.py – Interaktywna gra Wordle.

wordleengine.py – Zaawansowany solver z filtrowaniem i punktacją słów.

createwords.py – Narzędzie do czyszczenia pliku slowa.txt i generowania slowa_correct.txt.

Instrukcja obsługi
1. Przygotowanie słownika
Upewnij się, że masz plik slowa.txt w folderze głównym, a następnie uruchom:

Bash
python createwords.py
2. Gra w Wordle
Uruchom grę i spróbuj zgadnąć wylosowane słowo w 5 próbach:

Bash
python main.py
3. Korzystanie z Solvera
Jeśli utkniesz w grze, użyj solvera, aby otrzymać sugestie:

Bash
python wordleengine.py
Filter: Wprowadź litery szare, żółte i zielone (użyj spacji dla nieznanych pól, np. a  e ).

Refine: Precyzyjnie wyklucz żółte litery z konkretnych pozycji.

Logika Solvera
Program ocenia słowa na podstawie częstotliwości występowania liter w pozostałej puli możliwości. Im więcej popularnych liter zawiera słowo, tym wyższy jest jego priorytet w sekcji "Suggestions".

Projekt stworzony w celach edukacyjnych.