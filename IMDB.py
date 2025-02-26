"""
Zadanie: biblioteka filmów
A teraz coś z zupełnie innej beczki. Wyobraź sobie, że tworzysz system obsługujący
bibliotekę filmów i seriali. Wykorzystaj wiedzę na temat programowania obiektowego
i napisz program, który spełnia następujące założenia:

1. Jest w stanie przechowywać informacje na temat filmów, które znajdują się w systemie.
   Każdy film powinien mieć następujące atrybuty:
   - Tytuł
   - Rok wydania
   - Gatunek
   - Liczba odtworzeń  __DONE

2. Umożliwia przechowywanie informacji na temat seriali.
   Każdy serial powinien mieć następujące atrybuty:
   - Tytuł
   - Rok wydania
   - Gatunek
   - Numer odcinka
   - Numer sezonu
   - Liczba odtworzeń

3. Filmy i seriale mają metodę play, która zwiększa liczbę odtworzeń danego tytułu o 1.

4. Po wyświetleniu serialu jako string pokazują się informacje o konkretnym odcinku,
   np.: “The Simpsons S01E05” (gdzie po S pokazany jest numer sezonu w notacji dwucyfrowej,
   natomiast po E - numer odcinka, również w zapisie dwucyfrowym).

5. Po wyświetleniu filmu jako string widoczne są tytuł i rok wydania np. “Pulp Fiction (1994)”.

6. Przechowuje filmy i seriale w jednej liście.

DODATKOWO:

7. Napisz funkcje get_movies oraz get_series, które będą filtrować listę i zwracać
   odpowiednio tylko filmy oraz tylko seriale. Posortuj listę wynikową alfabetycznie.

8. Napisz funkcję search, która wyszukuje film lub serial po jego tytule.

9. Napisz funkcję generate_views, która losowo wybiera element z biblioteki,
   a następnie dodaje mu losową (z zakresu od 1 do 100) ilość odtworzeń.

10. Napisz funkcję, która uruchomi generate_views 10 razy.

11. Napisz funkcję top_titles(), która zwróci wybraną ilość najpopularniejszych
    tytułów z biblioteki. Dla chętnych: dodaj do funkcji parametr content_type,
    którym wybierzesz czy mają zostać pokazane filmy, czy seriale.


########## Zadania dla chętnych ##########
1. Napisz funkcję, która za pomocą pętli dodaje pełne sezony seriali do biblioteki.
   Funkcja powinna przyjmować parametry takie jak: tytuł serialu, rok wydania, gatunek,
   numer sezonu, liczba odcinków do dodania.

2. Do klasy reprezentującej serial, dopisz funkcję zewnętrzną,
   która wyświetla liczbę odcinków danego serialu dostępnych w bibliotece.

Niech program po uruchomieniu działa w następujący sposób:
 - Wyświetli na konsoli komunikat Biblioteka filmów.
 - Wypełni bibliotekę treścią.
 - Wygeneruje odtworzenia treści za pomocą funkcji generate_views.
 - Wyświetli na konsoli komunikat Najpopularniejsze filmy i seriale dnia <data>,
   gdzie <data> to bieżąca data w formacie DD.MM.RRRR.
 - Wyświetli listę top 3 najpopularniejszych tytułów.
"""


# Class creating instances of Movies
class Movie:
    def __init__(self, title, release_year, genre):
        self.title = title
        self.release_year = release_year
        self.genre = genre
        self.play_count = 0

    def play(self):
        self.play_count += 1


class Series(Movie):
    def __init__(self, title, release_year, genre, season, episode):
        super().__init__(title, release_year, genre)
        self.season = season
        self.episode = episode
