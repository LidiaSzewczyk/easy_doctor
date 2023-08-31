# EASY Doctor

### Przed uruchomieniem

* stworzyć plik envs/.env na bazie .env-default i uzupełnić

### Możliwości

* z panelu admina funkcjonalność dodawania tekstów z przypisaniem do danego rozpoznania i określonej części wizyty oraz
  określeniem sposobu wyświetlania  (text, radio, checkbox, ich kombinacje, ustalenie kolejności)
* wyświetlanie listy rozpoznań i każdego rozpoznania osobno
* w widoku szczegółowym rozpoznania, po wypełnieniu formularza z danej części wizyty (po stronie lewej) możliwość
  dodania (też usunięcia) go do całościowego formularza z wizyty danego pacjenta (po stronie prawej), zapisywanie w session storage, co
  umożliwia zachowanie danych przy przechodzeniu na inne endpointy np na endpointy np z innymi rozpoznaniami

### TO DO

* generowanie pdf z wizyty
* pacjent crud, lista, wyszukiwanie, policzyć wiek, poprawić formularz- daty, validacja, 
* pracownik- dostęp tylko do pacjentów których miał na wizycie
* wysyłanie mailem zaleceń /całej wizyty
* podpis elektronczny
* logowanie, rejestracja
* wizyta crud
* generowanie listy wizyt pacjenta z rozpoznaniami i datami
* przypisanie tekstów do określonych grup/użytkownikóœ
* filtrowanie, sortowanie, wyszukiwanie rozpoznań
* czyszczenie pojedynczych formularzy z wizyty, zapisywanie wizyty, model wizyty
* lista wizyt danego pacjenta, z danego dnia, z danym rozpoznaniem