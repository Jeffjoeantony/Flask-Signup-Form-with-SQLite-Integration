from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'error'  

def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username'] 
        email = request.form['email']
        phone = request.form['phone']
        password = request.form['pass']
        cpassword = request.form['cpass']

        if not (username and email and phone and password and cpassword):
            flash("All fields are required!")
            return redirect(url_for('signup'))

        if password != cpassword:
            flash("Passwords do not match!")
            return redirect(url_for('signup'))

        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, email, phone, password) VALUES (?, ?, ?, ?)",
                       (username, email, phone, password))
        conn.commit()
        conn.close()

        return redirect(url_for('success'))

    return render_template('signup.html')

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
