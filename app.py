from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import date, time
import uuid

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tickets.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Model bazy danych
class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    match_name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    available_tickets = db.Column(db.Integer, nullable=False)
    slug = db.Column(db.String(100), unique=True, nullable=False)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=False)
    is_used = db.Column(db.Boolean, default=False)  # Nowe pole: czy bilet został użyty
    ticket_code = db.Column(db.String(50), unique=True, nullable=False)  # Unikalny kod biletu
    
    def __repr__(self):
        return f"<Ticket {self.match_name}, Available: {self.available_tickets}>"

@app.route('/')
def home():
    # Pobierz wszystkie bilety z bazy danych
    tickets = Ticket.query.all()
    return render_template('index.html', tickets=tickets)  # Przekaż dane do szablonu

@app.route('/match/<slug>')
def match_details(slug):
    ticket = Ticket.query.filter_by(slug=slug).first_or_404()

    # Calculate sector prices
    price_a = round(ticket.price * 1.25, 2)  # 125% za sektor A
    price_b = ticket.price                   # Bazowa cena za sektor B
    price_c = ticket.price                   # Bazowa cena za sektor C
    price_d = round(ticket.price * 1.25, 2)  # 125% za sektor D

    return render_template(
        'match_details.html',
        ticket=ticket,
        price_a=price_a,
        price_b=price_b,
        price_c=price_c,
        price_d=price_d
    )

@app.route('/api/tickets/<int:ticket_id>/buy', methods=['POST'])
def buy_ticket(ticket_id):
    ticket = Ticket.query.get_or_404(ticket_id)
    if ticket.available_tickets > 0:
        ticket.available_tickets -= 1
        ticket.ticket_code = str(uuid.uuid4())  # Generuj unikalny kod biletu
        db.session.commit()
        return jsonify({
            'message': 'Bilet zakupiony pomyślnie!',
            'ticket_code': ticket.ticket_code,  # Zwróć kod biletu
            'available_tickets': ticket.available_tickets
        })
    else:
        return jsonify({'message': 'Brak dostępnych biletów.'}), 400

@app.route('/api/tickets/verify', methods=['POST'])
def verify_ticket():
    data = request.get_json()
    ticket_code = data.get('ticket_code')  # Pobierz kod biletu z żądania

    if not ticket_code:
        return jsonify({'message': 'Brak kodu biletu.'}), 400

    ticket = Ticket.query.filter_by(ticket_code=ticket_code).first()

    if not ticket:
        return jsonify({'message': 'Nieprawidłowy kod biletu.'}), 404

    if ticket.is_used:
        return jsonify({'message': 'Bilet został już wykorzystany.'}), 400

    # Oznacz bilet jako użyty
    ticket.is_used = True
    db.session.commit()

    return jsonify({
        'message': 'Bilet jest ważny.',
        'match_name': ticket.match_name,
        'date': ticket.date.isoformat(),
        'time': ticket.time.isoformat(),
    })

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Tworzy tabele w bazie danych, jeśli jeszcze nie istnieją
    app.run(debug=True)