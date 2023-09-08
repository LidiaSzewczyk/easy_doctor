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
* dodawanie, edycja, usuwanie pacjentów; wyświetlanie widoku wszystkich pacjentów i widoku szczegółowego pacjenta również z odbytymi wizytami
* dodawanie wizyty do danego pacjenta, edycja, usuwanie wizyty, wyświetlanie listy wizyt, widoku szegółowego wizyty
* logowanie/wylogowywanie

### TO DO

* generowanie pdf z wizyty
* pacjent  wyszukiwanie, poprawić formularz- daty, validacja, 
* pracownik- dostęp tylko do pacjentów których miał na wizycie
* wysyłanie mailem zaleceń /całej wizyty
* podpis elektronczny
* rejestracja
* przypisanie tekstów do określonych grup/użytkownikóœ
* filtrowanie, sortowanie, wyszukiwanie rozpoznań
* do modelu pacjent dodać pola is_child, płeć
* dodawanie z admina tekstów na homepage
*  dodać do login.html <p><a class="turquoise" href="{% url 'password_reset' %}">Nie pamiętasz hasła?</a></p> i dorobić templatkę
* 


### Teksty
* Używamy plików cookies, aby ułatwić Ci korzystanie z naszego serwisu oraz do celów statystycznych. Jeśli nie blokujesz tych plików, to zgadzasz się na ich użycie oraz zapisanie w pamięci urządzenia. Pamiętaj, że możesz samodzielnie zarządzać cookies, zmieniając ustawienia przeglądarki. Więcej informacji w naszej polityce prywatności.