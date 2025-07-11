from flask import Flask, render_template, request, redirect, url_for, flash
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = "secret_key"  # For flash messages

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["resultdb"]
users_collection = db["users"]
students_collection = db["students"]

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # Check user credentials
        user = users_collection.find_one({"username": username, "password": password})

        if user:
            roll_no = user["roll_no"]
            return redirect(url_for("result", roll_no=roll_no))
        else:
            flash("Invalid username or password!", "error")
            return redirect(url_for("login"))
    return render_template("login.html")


@app.route("/result/<roll_no>")
def result(roll_no):
    student = students_collection.find_one({"roll_no": roll_no})
    if student:
        return render_template("result.html", student=student)
    else:
        return "Student result not found", 404

if __name__ == "__main__":
    app.run(debug=True)
