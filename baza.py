from app import app, db, Ticket
from datetime import datetime, timedelta
import uuid  # Do generowania unikalnych kodów biletów

# Tworzenie danych w ramach kontekstu aplikacji
with app.app_context():
    # Daty kolejnych weekendów lutego
    start_date = datetime(2025, 2, 1)  # Pierwszy weekend: 1 lutego 2025
    dates = [start_date + timedelta(weeks=i) for i in range(5)]  # 5 kolejnych weekendów

    # Przykładowe bilety z ustalonymi godzinami
    tickets = [
        Ticket(
            match_name="AZS AGH vs Wisła Kraków",
            price=50.00,
            available_tickets=200,
            slug="azs-agh-vs-wisla-krakow",
            date=dates[0].date(),  # Data pierwszego weekendu
            time=datetime.strptime("15:00", "%H:%M").time(),  # Godzina 15:00
            is_used=False,  # Domyślnie bilet nie jest użyty
            ticket_code=str(uuid.uuid4()),  # Generuj unikalny kod biletu
        ),
        Ticket(
            match_name="AZS AGH vs Cracovia",
            price=60.00,
            available_tickets=150,
            slug="azs-agh-vs-cracovia",
            date=dates[1].date(),  # Data drugiego weekendu
            time=datetime.strptime("16:00", "%H:%M").time(),  # Godzina 16:00
            is_used=False,  # Domyślnie bilet nie jest użyty
            ticket_code=str(uuid.uuid4()),  # Generuj unikalny kod biletu
        ),
        Ticket(
            match_name="AZS AGH vs Śląsk Wrocław",
            price=55.00,
            available_tickets=180,
            slug="azs-agh-vs-slask-wroclaw",
            date=dates[2].date(),  # Data trzeciego weekendu
            time=datetime.strptime("17:00", "%H:%M").time(),  # Godzina 17:00
            is_used=False,  # Domyślnie bilet nie jest użyty
            ticket_code=str(uuid.uuid4()),  # Generuj unikalny kod biletu
        ),
        Ticket(
            match_name="AZS AGH vs Górnik Zabrze",
            price=65.00,
            available_tickets=170,
            slug="azs-agh-vs-gornik-zabrze",
            date=dates[3].date(),  # Data czwartego weekendu
            time=datetime.strptime("15:30", "%H:%M").time(),  # Godzina 15:30
            is_used=False,  # Domyślnie bilet nie jest użyty
            ticket_code=str(uuid.uuid4()),  # Generuj unikalny kod biletu
        ),
        Ticket(
            match_name="AZS AGH vs Legia Warszawa",
            price=70.00,
            available_tickets=160,
            slug="azs-agh-vs-legia-warszawa",
            date=dates[4].date(),  # Data piątego weekendu
            time=datetime.strptime("16:30", "%H:%M").time(),  # Godzina 16:30
            is_used=False,  # Domyślnie bilet nie jest użyty
            ticket_code=str(uuid.uuid4()),  # Generuj unikalny kod biletu
        ),
    ]

    # Zapisanie danych w bazie
    db.session.add_all(tickets)
    db.session.commit()