from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

# Define a User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

# Home route
@app.route("/")
def index():
    users = User.query.all()
    return render_template("index.html", users=users)

# Add user route
@app.route("/add", methods=["POST"])
def add_user():
    name = request.form.get("name")
    new_user = User(name=name)
    db.session.add(new_user)
    db.session.commit()
    return redirect("/")

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
