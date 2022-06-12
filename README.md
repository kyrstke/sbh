# Sequencing by Hybridization

## Problem klasycznego sbh z błędami negatywnymi i pozytywnymi
### Opis problemu
Przedstawione rozwianie rozwiązuje problem klasycznego sbh z błędami negatywnymi i pozytywnymi. Program ma na celu znalezienia pierwotnego łańcucha DNA na podstawie danych dostarczoncyh poprzez sewkwencjonowanie materiału genetycznego.

### Opis rozwiązania
#### Wczytywanie danych
Program opiera się na implementacji klasy `sbhAlgorithm`, która wykonuje domyślną metodę `main`. Metoda ta odczytuje dane z pliku za pomoca innej metody `readfile`. Plik zawiera części składowe łańcucha DNA dostarczone przez sekwencjonowanie materiału genetycznego, dane te sa czytane z pliku i zapisywane do tablicy, następnie przekształcane przy uzyciu metody `match` do postaci macierzy sasiedztwa. Metoda ta sprawdza podobieństwo pomiędzy dwoma łańcuchami znaków, w tym przypadku pomiędzy dwoma fragmentami sekwencji DNA. Dane te reprezentuja odległośc pomiedzy konkretnymi wierzchołkami (sekwencjami) w grafie.  
#### ant colony search
Algorytm zaczyna od ustawienia wartości parametrów dla mrówek oraz określenia maksymalnego czasu działania algorytmu. Następnie rozpoczynany jest algorytm mrówkowy. Rozpoczyna sie petla szukajaca jak najlepszego rozwiazania poprzez kazda swoja interację starajac się je polepszyc. Na wczesniej stworzonym grafie sa umieszczane mrowki. **Sa ony dytrbuowane losowo**. Kazda mrowka idzie sciezka zostawiajac za soba feromon. Wybiera nastepnie kolejny wierzcholek w oparciu o feromon z tablicy feromonów oraz macierzy siedztwa. W trakcie swojej drogi za kazdym razem sprawdza, czy czasem nie pogroszy dlugosci trasy wybierajac nastepny wierzchołek. Jeśli wszędzie jest dalej niz maksymalna dlugosc sciezki, dana mrówka kończy drogę. Nastepnie feromon jest dodawany do ogolnej mapy feromonow. Wszystkie mrowki po przejsciu grafu i zmodyfikowaniu tablicy feromonów zaczynaja kolejna iteracje programu. Koncza gdy skonczy sie czas lub znajda idealna sciezke.
#### wynik
Koncowa ściezka jest analizowana przez metodę `printNicely` i wypisywana w postaci końcowego łańcucha DNA.

### Testy

---
<p align="center">© Created by Konrad Romański & Krystian Jakusik</p>
