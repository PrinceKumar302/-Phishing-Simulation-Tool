from flask import Flask, render_template, request, redirect, url_for, flash, session
import smtplib
import sqlite3
from email.mime.text import MIMEText

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Database setup
def init_db():
    conn = sqlite3.connect('database/users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    email TEXT NOT NULL,
                    clicked BOOLEAN DEFAULT 0
                )''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_email', methods=['POST'])
def send_email():
    recipient = request.form['email']
    phishing_link = url_for('phishing_page', _external=True)

    msg = MIMEText(f"Click here to update your account: {phishing_link}")
    msg['Subject'] = 'Important Security Update'
    msg['From'] = 'security@example.com'
    msg['To'] = recipient

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login('your_email@gmail.com', 'your_password')
            server.sendmail(msg['From'], [msg['To']], msg.as_string())
        flash('Phishing email sent!', 'success')
    except Exception as e:
        flash(f'Failed to send email: {e}', 'danger')

    # Store recipient in DB
    conn = sqlite3.connect('database/users.db')
    c = conn.cursor()
    c.execute('INSERT INTO users (email) VALUES (?)', (recipient,))
    conn.commit()
    conn.close()

    return redirect(url_for('index'))

@app.route('/phishing')
def phishing_page():
    # Simulate click tracking (Note: In real case, you should identify the user uniquely)
    conn = sqlite3.connect('database/users.db')
    c = conn.cursor()
    c.execute('UPDATE users SET clicked = 1 WHERE email = ?', ("example@domain.com",))  # Static for demo
    conn.commit()
    conn.close()

    return render_template('phishing_email.html')

@app.route('/admin')
def admin_dashboard():
    conn = sqlite3.connect('database/users.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users')
    users = c.fetchall()
    conn.close()
    return render_template('dashboard.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)
