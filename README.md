# My Personal Website – Django Portfolio

A clean, modern personal/portfolio website built with Django.  
Currently includes a home page, about page, and a working contact form that sends emails via Gmail SMTP.

## Features

- Home page with dynamic date/time and example context data
- About page with contact details
- Fully functional contact form (with validation + real email sending)
- Base template (`base.html`) with navigation
- Named URLs (`name="home"`, `name="about"`, `name="contact"`)
- Ready for further extensions (blog, admin panel, etc.)

## Screenshots
*(Add screenshots later if you want – create a folder `screenshots/` and link them here)*

## How to run the project locally

```bash
# 1. Clone the repository
git clone https://github.com/TWOJ_LOGIN/TWOJA_NAZWA_REPO.git
cd TWOJA_NAZWA_REPO

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate          # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install django

# 4. Apply migrations
python manage.py migrate

# 5. Start the development server
python manage.py runserver

# 6. Available pages
http://127.0.0.1:8000/ → Home
http://127.0.0.1:8000/about → About
http://127.0.0.1:8000/contact → Contact form
http://127.0.0.1:8000/success → Thank-you page after submission

# 7. Email configuration (Gmail SMTP), The current configuration in moja_strona/settings.py: 
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "g.olczyk.priv@gmail.com"
EMAIL_HOST_PASSWORD = "your-16-char-app-password-here"   # ← NEVER commit the real password!
DEFAULT_FROM_EMAIL = "g.olczyk.priv@gmail.com"
NOTIFY_EMAIL = "g.olczyk@yahoo.com"

# 8. Project creation – step-by-step history
# Create the Django project
django-admin startproject moja_strona
# Initial migration & server test
python manage.py migrate
python manage.py runserver
# Create the app
python manage.py startapp olczyk_innowacje
# Templates folder + TEMPLATES['DIRS'] configuration
# Home page
templates/home.html
olczyk_innowacje/views.py → home_page_view()
Project-level routing via include("olczyk_innowacje.urls")
# About page – class-based AboutPageView(TemplateView) with context data
# Base templatetemplates/base.html with navigation and {% block content %}
# Named URLs (name="home", name="about", etc.) + {% url 'home' %} in templates
# Contact form
forms.py → ContactForm
ContactView(FormView) + SuccessView
Email sent with send_mail()
Templates: contact.html, success.html

# Gmail SMTP configuration (16-character app password)

# Author
# Grzegorz Olczyk
# Email: g.olczyk.priv@gmail.com

# 7. Setting background
 gravity.css / css data for twinkle stars and shooting star
 base.html / setting classes and styles