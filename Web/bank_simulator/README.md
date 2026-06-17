# 🏦 Bank Account Simulator

This is a simple **Bank Simulator Web Application** built using **Flask and MySQL**.
It allows users to perform basic banking operations like creating accounts, depositing, withdrawing, and viewing transactions.

---

## 📌 Features

* 🔐 User Registration and Login
* 🏦 Create Multiple Bank Accounts
* 💰 Deposit Money
* 💸 Withdraw Money (with T-PIN verification)
* 📜 View Transaction History
* 📥 Export Transactions in CSV format

---

## 🛠️ Technologies Used

* Python (Flask)
* MySQL Database
* HTML, CSS
* Jinja2 Template Engine

---

## 📂 Project Structure

```text
Bank_simulator/
│
├── app.py
├── .env
├── .gitignore
├── requirements.txt
├── README.md
│
├── static/
│   └── css/
│       ├── create_account.css
│       ├── dashboard.css
│       ├── deposit.css
│       ├── login.css
│       ├── main.css
│       ├── register.css
│       ├── transactions.css
│       └── withdraw.css
│
├── templates/
│   ├── create_account.html
│   ├── dashboard.html
│   ├── deposit.html
│   ├── login.html
│   ├── register.html
│   ├── transactions.html
│   └── withdraw.html
│
└── venv/
```

---

## ⚙️ How to Run

1. Clone the repository

```bash
git clone <your-repo-link>
cd bank-simulator
```

2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Create `.env` file

```text
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=yourpassword
DB_NAME=bank_db
```

5. Run the project

```bash
python app.py
```

6. Open in browser

```
http://127.0.0.1:5000
```

---

## 🗄️ Database Tables

### Users

* user_id (Primary Key)
* name
* mobile
* email
* aadhaar
* pan
* address
* password

### Accounts

* acc_no (Primary Key)
* user_id (Foreign Key)
* type
* balance
* t_pin

### Transactions

* txn_id (Primary Key)
* acc_no
* amount
* type
* timestamp
* user_id

---

## ⚠️ Note

* This project is for **learning purpose only**
* Passwords are not encrypted
* Not for real banking use

---

## 👨‍💻 Authors

* Rohit Kumar

---
