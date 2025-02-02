# Dokumentacja projektu: System sprzedaży biletów na mecze

## Spis treści
1. Opis projektu
2. Wymagania techniczne
3. Instalacja
4. Struktura projektu
5. Uruchomienie aplikacji
6. Endpointy API
7. Baza danych
8. Szablony HTML
9. Stylizacja CSS

---

## Opis projektu
Projekt to aplikacja webowa napisana w Flasku, która umożliwia sprzedaż i weryfikację biletów na mecze piłki ręcznej. Główne funkcjonalności to:
- Wyświetlanie listy dostępnych biletów.
- Szczegóły meczu z podziałem na sektory i ceny.
- Zakup biletu z generowaniem unikalnego kodu.
- Weryfikacja ważności biletu.

---

## Wymagania techniczne
- Python 3.8+
- Flask
- Flask-SQLAlchemy
- SQLite (lub inna baza danych obsługiwana przez SQLAlchemy)
- Biblioteki pomocnicze: `uuid`, `datetime`

---

## Instalacja
1. Utwórz wirtualne środowisko:
   ```
   python -m venv venv
2. Aktywuj wirtualne środowisko:
   ```
   .\venv\Scripts\activatet
3. Uruchom skrypt inicjalizujący bazę danych:
   ```
   python baza.py
## Uruchomienie aplikacji
1. Uruchom aplikację:
   ```
   python app.py
2. Otwórz przeglądarke i przejdź do:
   ```
   http://127.0.0.1:5000/
## Endpointy API
1. Strona główna:
   ```
   URL: /
   Metoda: GET
   Opis: Wyświetla listę dostępnych biletów.
2. Szczegóły meczu:
   ```
   URL: /match/<slug>
   Metoda: GET
   Opis: Wyświetla szczegóły meczu, w tym ceny biletów dla różnych sektorów.
3. Zakup biletu:
   ```
   URL: /api/tickets/<int:ticket_id>/buy
   Metoda: POST
   Opis: Kupuje bilet i generuje unikalny kod biletu.
4. Weryfikacja biletu:
   ```
   URL: /api/tickets/verify
   Metoda: POST
   Opis: Sprawdza ważność biletu na podstawie kodu.
## Struktura folderów
Pliki projektu zostały podzielone na podfoldery:
- app.py -                 Główny plik aplikacji Flask
- baza.py -                Skrypt inicjalizujący bazę danych
- requierements.txt -      Lista zależności
- static/
    - css/ 
        - style.css -      Główny plik CSS
    - images -             Obrazy (logo, partnerzy)
- templates -              Szablony HTML
    - index.html -         Strona główna
    - match_details.html - Szczegóły meczu	
- README.md -              Dokumentacja projektu
## Baza danych
### Tickets
| Pole  | Opis |
| ------------- | ------------- |
| id | Unikalny identyfikator biletu |
| match_name | Nazwa meczu |
| price | Cena biletu |
| available_tickets |  Liczba dostępnych biletów |
| slug | Unikalny identyfikator URL |
| date | Data meczu |
| time | Godzina meczu |

### PurchasedTicket:
| Pole  | Opis |
| ------------- | ------------- |
| id | Unikalny identyfikator biletu |
| match_name | Powiązanie z tabelą Ticket |
| ticket_code | Unikalny kod biletu |

## Szablony HTML
1. index.html
   Wyświetla listę dostępnych biletów w formie tabeli.
   Zawiera sekcję z logo i partnerami.
2. match_details.html
   Wyświetla szczegóły meczu, w tym ceny biletów dla różnych sektorów.
   Zawiera interaktywne sektory na boisku.
## Stylizacja CSS
Funkcje:
- Stylizacja tabeli z biletami.
- Efekty hover dla sektorów na boisku.
- Responsywność strony.
- Style dla okien dialogowych i przycisków.
