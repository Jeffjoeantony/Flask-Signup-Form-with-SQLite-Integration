
# 🔐 Flask Signup Form with SQLite Integration

A simple, secure web-based signup form built using **Python Flask**. It collects user information (username, email, phone, and password), validates the data, and stores it in an **SQLite database**. Upon successful registration, users are redirected to a confirmation page.

---

## 🚀 Features

- Responsive signup form UI with background image
- Password confirmation check with error handling
- Flash messages for form validation feedback
- SQLite database integration
- Redirection to a success page on valid submission

---

## 📌 Technologies Used

- Python 3
- Flask
- SQLite
- HTML5 & CSS3
- VS Code

---

## 📁 Folder Structure

```
Flask-Signup-Form-with-SQLite-Integration/
│
├── app.py                     # Main Flask backend
├── users.db                   # SQLite database (auto-generated)
├── static/
│   └── blurred-abstract-background.jpg
│   └── success.png
├── templates/
│   ├── signup.html            # Signup form UI
│   └── success.html           # Success confirmation page
├── README.md
└── LICENSE
```

---

## 🛠️ Setup Instructions

1. **Clone the Repository**

```bash
git clone https://github.com/Jeffjoeantony/Flask-Signup-Form-with-SQLite-Integration.git
cd Flask-Signup-Form-with-SQLite-Integration
```

2. **(Optional) Create a Virtual Environment**

```bash
python -m venv venv
venv\Scripts\activate   # On Windows
```

3. **Install Flask**

```bash
pip install flask
```

4. **Run the App**

```bash
python app.py
```

Then go to `http://127.0.0.1:5000/` in your browser.

---

## ✍️ Author

**Jeff Joe Antony**  
Intern, Verveox Technologies  
GitHub: [@Jeffjoeantony](https://github.com/Jeffjoeantony)

---

## 📝 License

This project is licensed under the [MIT License](LICENSE).
