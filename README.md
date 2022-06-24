# Sekwencjonowanie przez hybrydyzację (Sequencing by Hybridization)

## Problem klasycznego sbh z błędami negatywnymi i pozytywnymi
### Opis problemu
Przedstawione rozwianie rozwiązuje problem klasycznego sbh z błędami negatywnymi i pozytywnymi. Program ma na celu znalezienie pierwotnego łańcucha DNA na podstawie danych dostarczonych poprzez sekwencjonowanie materiału genetycznego.

### Opis rozwiązania
#### Wczytywanie danych
Program opiera się na implementacji klasy `sbhAlgorithm`, która wykonuje domyślną metodę `main`. Metoda ta odczytuje dane z pliku za pomocą metody `readfile`. Plik zawiera części składowe łańcucha DNA pozyskane dzięki sekwencjonowaniu materiału genetycznego, dane te są czytane z pliku i zapisywane do tablicy, następnie przekształcane przy użyciu metody `match` do postaci macierzy sąsiedztwa. Metoda ta sprawdza podobieństwo między dwoma łańcuchami znaków, w tym przypadku, dwoma fragmentami sekwencji DNA. Dane te reprezentują odległość między konkretnymi wierzchołkami (sekwencjami) w grafie.  
#### Ant colony search
Algorytm zaczyna od ustawienia wartości parametrów dla mrówek oraz określenia maksymalnego czasu działania. Działanie algorytmu rozpoczyna pętla, w której poszukiwane jest jak najlepsze rozwiązanie, stopniowo ulepszane lub  niezmieniane w  każdej iteracji. Na wcześniej stworzonym grafie umieszczane są mrówki. Swoją podróz zaczynają z wierzchołka reprezentujacego pierwszy nukleotyd. Każda mrówka podąża ścieżką zostawiajac za soba feromon. Następny jest wybór kolejnego wierzchołka w oparciu o tablicę feromonów oraz macierzy sąsiedztwa. Mrówka oblicza dla każdego wierzchołka, który nie jest w scieżce i nie pogorszy wyniku, prawdopodobieństwo pójścia do niego i wybiera jeden z nich na następce. W trakcie swojej drogi za każdym razem sprawdza, czy czasem nie pogorszy długości trasy, wybierając następny kolejny punkt podróży. Jeśli wszędzie jest dalej, niż maksymalna długość ścieżki, mrówka kończy drogę. Następnie jej feromon jest dodawany do ogólnej mapy feromonów. Wszystkie mrówki, po przejściu grafu i zmodyfikowaniu ogólnej tablicy feromonów o nową, wspólnie wyznaczoną, pomnożoną przez określoną wcześniej liczbę `p`, zaczynają kolejną iteracje programu. Kończą, gdy skończy się czas lub znajdzie się idealna ścieżka.
#### Wynik
Końcowa ścieżka jest analizowana przez metodę `print_results` i wypisywana w postaci końcowego, znalezionego łańcucha DNA.

### Testy

#### Testowanie parametrow algorytmu
##### Tabela
|id próby|n|n obliczone| % zgodności|czas dzialania|alfa|beta|p|mrówki na wierzchołek|
|-|-|-|-|-|-|-|-|-|
|1|209|207|--|--|10|10|0.3|40
##### Wykresy

#### Testowanie sekwencjonowania
##### Tabela
|id próby|n|n obliczone| % zgodności|długośc oligonukleotydów|% błędów wynikajacych<br>z powtórzeń| % błędów negatywnych| % błędów pozytywnych|
|-|-|-|-|-|-|-|-|
|1|209|207|--|--|--|--|--|

##### Wykresy

### Wnioski [POTRZEBNE?]

### Uruchamianie
#### Program
##### Schemat
```sh
py sbh.py n filename algorithm
```
Opis parametrów:
|parametr|opis|przykład|
|-|-|-|
|`n`|domyślna długość sekwencji|`209`|
|`filename`|nazwa pliku z danymi|`nucleotides_with_errors.txt`|
|`algorithm`|nazwa algorytmu|- `ACO`<br>- `antColonySearch`<br>- `antColonySearchSW`|
##### Przykład
```sh
py sbh.py 209 nucleotides.txt antColonySearchSW
```
#### Generator
##### Schemat
```sh
py generator.py n nucleotides errors
```
Opis parametrów:
|parametr|opis|przykład|
|-|-|-|
|`n`|domyślna długość sekwencji|`209`|
|`nucleotides`|długość nukleotydów|`10`|
|`errors`|opcje błędów rozdzielone `,`,<br>kolejnośc dowolna<br>`:` jako  separator skrótu i liczby<br>`x`, `y`, `z` jako liczby błędów |- usunięcie: `r:x`<br>- insercja: `i:y`<br>- duplikacja: `d:z`|
##### Przykład
```sh
py generator.py 209 10 r:10,i:5,d:20
```
#### Uruchamianie generatora, algorytmu i analizatora wyników (automatyzacja)
##### Schemat
```sh
py main.py sequence_length nucleotide_length n_remove n_insert n_duplicate filename algorithm
```
Opis parametrów:
|parametr|opis|przykład|
|-|-|-|
|`sequence_length`|domyślna długość sekwencji|`209`|
|`nucleotide_length`|długość nukleotydów|`10`|
|`n_remove`|liczba usuniętych nukleotydów|`0`|
|`n_insert`|liczba dodanych nukleotydów|`0`|
|`n_duplicate`|liczba powtórzeń|`0`|
|`filename`|nazwa pliku z danymi|`nucleotides_with_errors.txt`|
|`algorithm`|nazwa algorytmu|- `ACO`<br>- `antColonySearch`<br>- `antColonySearchSW`|
---
<p align="center">© Created by Konrad Romański & Krystian Jakusik</p>

