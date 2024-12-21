from flask import Flask, request, render_template, Request, url_for, redirect
from flask_socketio import SocketIO, emit
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
app.config["SECRET_KEY"] = "abc"
db = SQLAlchemy()
socketio = SocketIO(app)

# This global dictionary will hold the latest sensor values.
sensor_data = {
    'sensor1': 'No data for sensor1',
    'sensor2': 'No data for sensor2',
    'sensor3': 'No data for sensor3'
}
login_manager = LoginManager()
login_manager.init_app(app)

class Users(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(250), unique=True, nullable=False)
	password = db.Column(db.String(250), nullable=False)

db.init_app(app)
with app.app_context():
	db.create_all()

@login_manager.user_loader
def loader_user(user_id):
	return Users.query.get(user_id)


@app.route('/register', methods=["GET", "POST"])
def register():
	if request.method == "POST":
		user = Users(username=request.form.get("username"),
					password=request.form.get("password"))
		db.session.add(user)
		db.session.commit()
		return redirect(url_for("login"))
	return render_template("sign_up.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    error = None  # Initialize error variable
    if request.method == "POST":
        user = Users.query.filter_by(username=request.form.get("username")).first()
        if user and user.password == request.form.get("password"):
            login_user(user)
            return redirect(url_for("display"))
        else:
            error = "Invalid username or password."  # Set error message
    return render_template("login.html", error=error)

@app.route("/logout")
def logout():
	logout_user()
	return redirect(url_for("index"))



@app.route('/data', methods=['POST'])
def post_data():
    data = request.json
    print("Received POST request with:", data)  # Debug print
    if data:
        global sensor_data
        sensor_data['sensor1'] = data.get('sensor1', 'No data for sensor1')
        sensor_data['sensor2'] = data.get('sensor2', 'No data for sensor2')
        sensor_data['sensor3'] = data.get('sensor3', 'No data for sensor3')
        print("Emitting data:", sensor_data)  # Debug print
        socketio.emit('sensor_update', sensor_data)
        return "Data Received", 200
    else:
        return "No JSON data received", 400
    
@app.route('/display')
def display():
      return render_template('display.html')

@app.route('/')
def index():
    return render_template('home.html')


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)