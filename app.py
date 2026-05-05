from flask import Flask
from config import Config
from models import db          # Corregido: sin prefijo sql.
from routes import register_routes # Corregido: sin prefijo sql.

app = Flask(__name__)
app.config.from_object(Config)

# Llave secreta para que funcionen los mensajes "flash"
app.secret_key = "123"

db.init_app(app)

with app.app_context():
    db.create_all()

register_routes(app)

if __name__ == "__main__":
    app.run(debug=True)