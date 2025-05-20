from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static'

# Sample book data with descriptions
books = [
    {
        'title': 'The Alchemist',
        'author': 'Paulo Coelho',
        'price': 300,
        'rent_price': 50,
        'image': 'alchemist.jpg',
        'description': 'A philosophical story about a shepherd boy following his dreams.'
    },
    {
        'title': 'Atomic Habits',
        'author': 'James Clear',
        'price': 400,
        'rent_price': 70,
        'image': 'atomichabits.webp',
        'description': 'An easy and proven way to build good habits and break bad ones.'
    },
    {
        'title': 'Wings of Fire',
        'author': 'A.P.J. Abdul Kalam',
        'price': 350,
        'rent_price': 60,
        'image': 'wings_of_fire.jpg',
        'description': 'The inspiring autobiography of one of India’s most revered leaders.'
    }
]

@app.route("/", methods=["GET", "POST"])
def index():
    filtered_books = books
    if request.method == "POST":
        keyword = request.form.get("search", "").lower()
        filtered_books = [book for book in books if keyword in book["title"].lower()]
    return render_template("index.html", books=filtered_books)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Dummy login handler
        username = request.form["username"]
        password = request.form["password"]
        return redirect(url_for("index"))
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Dummy register handler
        username = request.form["username"]
        password = request.form["password"]
        return redirect(url_for("login"))
    return render_template("register.html")

@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        bookname = request.form["bookname"]
        image = request.files["image"]

        if image:
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
            image.save(image_path)

            # Add the uploaded book to the list
            books.append({
                "title": bookname,
                "author": "Unknown",
                "price": 250,
                "rent_price": 40,
                "image": image.filename,
                "description": "Newly added book!"
            })
            return redirect(url_for("index"))
    return render_template("upload.html")

@app.route("/buy")
def buy():
    return render_template("buy.html")

@app.route("/rent")
def rent():
    return render_template("rent.html")

@app.route("/nearby")
def nearby():
    return render_template("nearby.html")

if __name__ == "__main__":
    app.run(debug=True)
