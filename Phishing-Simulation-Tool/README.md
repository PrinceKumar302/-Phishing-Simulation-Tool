# 🛡️ Phishing Simulation Tool

A web-based phishing simulation platform designed to train and evaluate user awareness of phishing attacks. It sends realistic phishing emails, tracks user behavior, and delivers feedback and security training.

## 🚀 Features

- Simulated phishing email campaigns
- Real-time click and response tracking
- Admin dashboard with analytics
- Customizable email templates
- User feedback and training module
- Secure login and role-based access

## 🖼️ Demo

![Dashboard Screenshot](media/screenshots/dashboard.png)

[🎥 Watch Demo Video](media/demo_video.mp4)

## 🛠️ Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, Bootstrap
- **Database**: SQLite
- **Email Delivery**: SMTP (e.g., Gmail SMTP)
- **Hosting**: Local / Cloud

## 📂 Folder Structure

- `app/` – Core application logic (routes, templates, email sender)
- `database/` – SQLite DB or schema
- `media/` – Screenshots, demo video
- `docs/` – Architecture, documentation
- `requirements.txt` – Python dependencies

## 📊 Admin Dashboard

- Create & schedule campaigns
- Monitor user activity (clicks, reports)
- Export results as CSV

## 🔒 Email Security Awareness

- Teaches users to spot suspicious links, spoofed domains, and misleading sender names
- Includes instant feedback with tips after clicking a simulated phishing link

## 🏗️ Architecture

![Architecture Diagram](docs/architecture_diagram.png)

## ⚙️ Setup Instructions

```bash
# 1. Clone the repo
git clone https://github.com/yourusername/phishing-simulation-tool.git
cd phishing-simulation-tool

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python app/routes.py
