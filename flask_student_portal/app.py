from flask import Flask
from config import Config
from models import db, Teacher
from flask_login import LoginManager
from routes.auth import auth
from routes.student import student
from flask import redirect, url_for

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Initialize extensions
db.init_app(app)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

# Flask-Login: Load teacher by ID
@login_manager.user_loader
def load_user(user_id):
    return Teacher.query.get(int(user_id))

# Register Blueprints
app.register_blueprint(auth)
app.register_blueprint(student)

# ✅ Instead of @before_first_request
with app.app_context():
   db.create_all()

@app.route("/")
def index():
    return redirect(url_for('auth.login'))

# Run app
if __name__ == "__main__":
    app.run(debug=True)
