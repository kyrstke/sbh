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
##### Stałe parametry
|parametr|wartość|wartość procentowa|
|-|-|-|
|długość sekwencji|800|-|
|długość nukleotydów|10|-|
|usunięte nukleotydy|200|2.5%|
|dodane nukleotydy|200|2.5%|
|zduplikowane nukleotydy|0|0.0%|

##### Liczba mrówek
|id próby|n|n obliczone| % zgodności|czas działania|alfa|beta|p|mrówki|
|-|-|-|-|-|-|-|-|-|
|0|800|800|100.0|23.11|10|10|0.3|3|
|1|800|799|99.3|23.02|10|10|0.3|6|
|2|800|800|100.0|38.54|10|10|0.3|9|
|3|800|800|64.2|44.86|10|10|0.3|12|
|4|800|800|81.1|18.87|10|10|0.3|15|
|5|800|799|99.9|24.09|10|10|0.3|18|
|6|800|800|100.0|54.77|10|10|0.3|21|
|7|800|800|100.0|32.85|10|10|0.3|24|
|8|800|800|100.0|39.5|10|10|0.3|27|
|9|800|800|100.0|40.23|10|10|0.3|30|
|10|800|800|100.0|45.05|10|10|0.3|33|
|11|800|800|100.0|47.03|10|10|0.3|36|
|12|800|800|100.0|53.43|10|10|0.3|39|
|13|800|800|100.0|56.09|10|10|0.3|42|
|14|800|800|100.0|57.26|10|10|0.3|45|
|15|800|799|75.7|55.23|10|10|0.3|48|
|16|800|800|82.8|66.58|10|10|0.3|51|
|17|800|800|100.0|71.06|10|10|0.3|54|
|18|800|800|94.9|92.37|10|10|0.3|57|
|19|800|800|100.0|91.7|10|10|0.3|60|

Ustalona wartość parametru: 25 mrówek

##### Parametr p
|id próby|n|n obliczone| % zgodności|czas działania|alfa|beta|p|mrówki|
|-|-|-|-|-|-|-|-|-|
|0|800|800|100.0|35.56|10|10|0.05|25|
|1|800|799|99.9|35.73|10|10|0.1|25|
|2|800|800|98.9|30.23|10|10|0.15|25|
|3|800|800|100.0|33.01|10|10|0.2|25|
|4|800|800|91.0|32.86|10|10|0.25|25|
|5|800|800|100.0|34.44|10|10|0.3|25|
|6|800|800|100.0|34.73|10|10|0.35|25|
|7|800|793|99.3|33.5|10|10|0.4|25|
|8|800|800|100.0|36.51|10|10|0.45|25|
|9|800|800|100.0|34.2|10|10|0.5|25|
|10|800|799|99.9|36.77|10|10|0.55|25|
|11|800|800|77.0|34.42|10|10|0.6|25|
|12|800|800|100.0|35.4|10|10|0.65|25|
|13|800|800|100.0|34.09|10|10|0.70|25|
|14|800|799|99.9|34.64|10|10|0.751|25|
|15|800|798|99.9|33.36|10|10|0.8|25|
|16|800|799|99.9|34.72|10|10|0.85|25|
|17|800|795|81.3|29.09|10|10|0.9|25|
|18|800|800|100.0|31.19|10|10|0.95|25|
|19|800|800|100.0|34.37|10|10|1|25|

Ustalona wartość parametru: p = 0.45

##### Parametr alfa
|id próby|n|n obliczone| % zgodności|czas działania|alfa|beta|p|mrówki|
|-|-|-|-|-|-|-|-|-|
|0|800|800|100.0|31.86|1|10|0.45|25|
|1|800|800|100.0|34.19|2|10|0.45|25|
|2|800|795|99.7|32.88|3|10|0.45|25|
|3|800|799|99.9|33.04|4|10|0.45|25|
|4|800|800|93.9|33.47|5|10|0.45|25|
|5|800|800|100.0|33.76|6|10|0.45|25|
|6|800|800|100.0|32.74|7|10|0.45|25|
|7|800|800|100.0|35.26|8|10|0.45|25|
|8|800|800|67.6|31.86|9|10|0.45|25|
|9|800|800|100.0|32.9|10|10|0.45|25|
|10|800|800|100.0|34.31|11|10|0.45|25|
|11|800|799|99.9|32.06|12|10|0.45|25|
|12|800|800|100.0|32.75|13|10|0.45|25|
|13|800|800|100.0|33.59|14|10|0.45|25|
|14|800|800|100.0|34.5|15|10|0.45|25|
|15|800|800|100.0|34.44|16|10|0.45|25|
|16|800|796|99.7|34.19|17|10|0.45|25|
|17|800|799|99.9|34.17|18|10|0.45|25|
|18|800|800|100.0|34.31|19|10|0.45|25|
|19|800|798|99.9|33.29|20|10|0.45|25|

Ustalona wartość parametru: alfa = 12

##### Parametr beta
|id próby|n|n obliczone| % zgodności|czas działania|alfa|beta|p|mrówki|
|-|-|-|-|-|-|-|-|-|
|0|800|800|66.1|3.19|12|1|0.45|25|
|1|800|800|66.7|12.12|12|2|0.45|25|
|2|800|798|67.6|17.4|12|3|0.45|25|
|3|800|798|66.2|10.59|12|4|0.45|25|
|4|800|796|67.5|17.67|12|5|0.45|25|
|5|800|798|90.1|60.84|12|6|0.45|25|
|6|800|799|99.9|63.4|12|7|0.45|25|
|7|800|800|100.0|33.25|12|8|0.45|25|
|8|800|800|91.4|35.77|12|9|0.45|25|
|9|800|800|100.0|40.34|12|10|0.45|25|
|10|800|800|100.0|48.47|12|11|0.45|25|
|11|800|800|100.0|47.98|12|12|0.45|25|
|12|800|799|99.9|43.0|12|13|0.45|25|
|13|800|800|100.0|53.1|12|14|0.45|25|
|14|800|800|100.0|58.25|12|15|0.45|25|
|15|800|800|100.0|38.28|12|16|0.45|25|
|16|800|799|99.9|45.62|12|17|0.45|25|
|17|800|798|99.9|63.28|12|18|0.45|25|
|18|800|800|85.1|33.76|12|19|0.45|25|
|19|800|800|100.0|37.56|12|20|0.45|25|

Ustalona wartość parametru: beta = 12

##### Wykresy

#### Testowanie sekwencjonowania
##### Parametry
|parametr|wartość|
|-|-|
|p|0.45|
|alfa|12|
|beta|12|
|mrówki|25|
|błędy pozytywne|2.5%|
|błędy negatywne|2.5%|

##### Tabela
|id próby|n|n obliczone| % zgodności|czas działania|długość oligonukleotydów|% błędów wynikajacych<br>z powtórzeń| % błędów negatywnych| % błędów pozytywnych|
|-|-|-|-|-|-|-|-|-|
|0|100|100|100.0|0.18|10|0.0|2.5|2.5|
|1|100|100|100.0|0.15|10|0.0|2.5|2.5|
|2|100|100|100.0|0.14|10|0.0|2.5|2.5|
|3|100|98|99.0|0.17|10|0.0|2.5|2.5|
|4|100|100|100.0|0.17|10|0.0|2.5|2.5|
|5|200|200|100.0|1.06|10|0.0|2.5|2.5|
|6|200|200|100.0|0.93|10|0.0|2.5|2.5|
|7|200|200|100.0|0.91|10|0.0|2.5|2.5|
|8|200|199|99.7|0.95|10|0.0|2.5|2.5|
|9|200|198|99.5|0.93|10|0.0|2.5|2.5|
|10|300|300|100.0|3.0|10|0.0|2.5|2.5|
|11|300|300|100.0|3.64|10|0.0|2.5|2.5|
|12|300|299|99.8|3.28|10|0.0|2.5|2.5|
|13|300|300|100.0|3.2|10|0.0|2.5|2.5|
|14|300|300|100.0|2.97|10|0.0|2.5|2.5|
|15|400|400|100.0|6.61|10|0.0|2.5|2.5|
|16|400|400|100.0|6.34|10|0.0|2.5|2.5|
|17|400|400|100.0|6.41|10|0.0|2.5|2.5|
|18|400|400|100.0|6.23|10|0.0|2.5|2.5|
|19|400|400|100.0|6.29|10|0.0|2.5|2.5|
|20|500|500|100.0|11.88|10|0.0|2.5|2.5|
|21|500|500|100.0|11.79|10|0.0|2.5|2.5|
|22|500|500|100.0|11.65|10|0.0|2.5|2.5|
|23|500|500|100.0|11.54|10|0.0|2.5|2.5|
|24|500|500|100.0|11.76|10|0.0|2.5|2.5|
|25|600|600|100.0|19.85|10|0.0|2.5|2.5|
|26|600|600|100.0|20.28|10|0.0|2.5|2.5|
|27|600|600|100.0|19.95|10|0.0|2.5|2.5|
|28|600|600|100.0|19.82|10|0.0|2.5|2.5|
|29|600|600|100.0|19.43|10|0.0|2.5|2.5|
|30|700|700|100.0|35.13|10|0.0|2.5|2.5|
|31|700|700|100.0|39.73|10|0.0|2.5|2.5|
|32|700|700|100.0|39.68|10|0.0|2.5|2.5|
|33|700|700|100.0|39.2|10|0.0|2.5|2.5|
|34|700|700|100.0|38.81|10|0.0|2.5|2.5|
|35|800|800|100.0|57.81|10|0.0|2.5|2.5|
|36|800|800|100.0|57.39|10|0.0|2.5|2.5|
|37|800|800|100.0|58.19|10|0.0|2.5|2.5|
|38|800|800|100.0|56.4|10|0.0|2.5|2.5|
|39|800|800|100.0|57.4|10|0.0|2.5|2.5|
|40|900|900|100.0|79.58|10|0.0|2.5|2.5|
|41|900|900|100.0|81.63|10|0.0|2.5|2.5|
|42|900|900|100.0|73.08|10|0.0|2.5|2.5|
|43|900|900|100.0|73.06|10|0.0|2.5|2.5|
|44|900|900|100.0|75.7|10|0.0|2.5|2.5|
|45|1000|999|99.9|96.93|10|0.0|2.5|2.5|
|46|1000|999|99.9|92.72|10|0.0|2.5|2.5|
|47|1000|1000|100.0|93.73|10|0.0|2.5|2.5|
|48|1000|1000|100.0|90.75|10|0.0|2.5|2.5|
|49|1000|1000|100.0|92.88|10|0.0|2.5|2.5|

##### Parametry
|parametr|wartość|
|-|-|
|p|0.45|
|alfa|12|
|beta|12|
|mrówki|25|
|błędy pozytywne|5%|
|błędy negatywne|5%|

##### Tabela
|id próby|n|n obliczone| % zgodności|czas działania|długość oligonukleotydów|% błędów wynikajacych<br>z powtórzeń| % błędów negatywnych| % błędów pozytywnych|
|-|-|-|-|-|-|-|-|-|
|0|100|99|99.5|0.15|10|0.0|5.0|5.0|
|1|100|99|99.5|0.13|10|0.0|5.0|5.0|
|2|100|100|100.0|0.12|10|0.0|5.0|5.0|
|3|100|99|99.5|0.15|10|0.0|5.0|5.0|
|4|100|99|99.5|0.13|10|0.0|5.0|5.0|
|5|200|200|100.0|0.93|10|0.0|5.0|5.0|
|6|200|200|100.0|0.91|10|0.0|5.0|5.0|
|7|200|198|99.5|0.85|10|0.0|5.0|5.0|
|8|200|200|85.5|0.82|10|0.0|5.0|5.0|
|9|200|198|99.5|0.84|10|0.0|5.0|5.0|
|10|300|300|100.0|2.6|10|0.0|5.0|5.0|
|11|300|300|100.0|2.79|10|0.0|5.0|5.0|
|12|300|300|100.0|2.67|10|0.0|5.0|5.0|
|13|300|300|100.0|2.83|10|0.0|5.0|5.0|
|14|300|300|100.0|2.92|10|0.0|5.0|5.0|
|15|400|400|100.0|6.43|10|0.0|5.0|5.0|
|16|400|400|100.0|6.19|10|0.0|5.0|5.0|
|17|400|400|100.0|6.09|10|0.0|5.0|5.0|
|18|400|400|100.0|6.05|10|0.0|5.0|5.0|
|19|400|400|100.0|5.92|10|0.0|5.0|5.0|
|20|500|500|100.0|12.5|10|0.0|5.0|5.0|
|21|500|499|99.9|10.76|10|0.0|5.0|5.0|
|22|500|499|99.9|11.37|10|0.0|5.0|5.0|
|23|500|499|99.9|11.23|10|0.0|5.0|5.0|
|24|500|500|100.0|11.51|10|0.0|5.0|5.0|
|25|600|600|100.0|18.87|10|0.0|5.0|5.0|
|26|600|600|100.0|19.41|10|0.0|5.0|5.0|
|27|600|600|100.0|19.44|10|0.0|5.0|5.0|
|28|600|600|100.0|19.73|10|0.0|5.0|5.0|
|29|600|600|100.0|18.96|10|0.0|5.0|5.0|
|30|700|700|100.0|30.09|10|0.0|5.0|5.0|
|31|700|700|100.0|30.8|10|0.0|5.0|5.0|
|32|700|700|100.0|30.45|10|0.0|5.0|5.0|
|33|700|700|100.0|32.03|10|0.0|5.0|5.0|
|34|700|700|100.0|30.75|10|0.0|5.0|5.0|
|35|800|800|100.0|45.47|10|0.0|5.0|5.0|
|36|800|800|100.0|44.98|10|0.0|5.0|5.0|
|37|800|800|100.0|44.51|10|0.0|5.0|5.0|
|38|800|800|100.0|45.72|10|0.0|5.0|5.0|
|39|800|800|100.0|45.22|10|0.0|5.0|5.0|
|40|900|900|100.0|61.32|10|0.0|5.0|5.0|
|41|900|900|100.0|64.21|10|0.0|5.0|5.0|
|42|900|899|99.9|64.63|10|0.0|5.0|5.0|
|43|900|900|100.0|62.52|10|0.0|5.0|5.0|
|44|900|900|100.0|63.35|10|0.0|5.0|5.0|
|45|1000|1000|100.0|85.16|10|0.0|5.0|5.0|
|46|1000|1000|100.0|84.49|10|0.0|5.0|5.0|
|47|1000|1000|100.0|89.35|10|0.0|5.0|5.0|
|48|1000|1000|100.0|85.38|10|0.0|5.0|5.0|
|49|1000|1000|100.0|85.61|10|0.0|5.0|5.0|

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

