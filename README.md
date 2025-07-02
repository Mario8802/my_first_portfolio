# Mario Showcase 🌟

**Live site:** [https://mario-showcase.onrender.com](https://mario-showcase.onrender.com)

## 📝 Description

This is my personal portfolio website, designed to showcase:
- 💻 My projects
- 🏆 My courses and certificates
- 🔗 My GitHub activity
- 📬 Contact form

Built with **Django** and deployed on **Render.com**.

---

## 🚀 Technologies

- Python 3.13
- Django 5.2.3
- Django REST Framework
- Gunicorn (for production server)
- Bootstrap + custom CSS
- AOS (Animate On Scroll)
- Render (hosting)
- GitHub Actions (CI/CD pipeline)

---

## ⚙️ Local setup

1️⃣ Clone the repository:

git clone https://github.com/Mario8802/my_first_portfolio.git
cd my_first_portfolio
2️⃣ Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows

3️⃣ Install dependencies:

pip install -r requirements.txt
4️⃣ Run migrations and collect static files:

python manage.py migrate
python manage.py collectstatic --noinput

5️⃣ Start the development server:

python manage.py runserver
🌐 Deployment
Deployment is handled on Render.com with:

Build command

pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput
Production server

gunicorn portfolio.wsgi:application
GitHub Actions CI/CD

yaml
curl -X POST ${{ secrets.RENDER_DEPLOY_HOOK_URL }}
🛡 ALLOWED_HOSTS
Configured via Render environment variables:


DJANGO_ALLOWED_HOSTS=mario-showcase.onrender.com
📁 Project structure

portfolio/
├── certificates/
├── contact/
├── github/
├── projects/
├── portfolio/  # Django config (settings, urls, wsgi, etc.)
├── static/
│   ├── books/
│   └── images/
├── templates/
└── .env (local only)


🤖 Uptime bot
The site is kept alive using UptimeRobot which pings the Render instance regularly to prevent it from idling.
