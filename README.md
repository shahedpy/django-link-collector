# Link Collector

A simple Django app to collect and display links (scraper-based link collector).

---

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Database setup](#database-setup)
- [Run the development server](#run-the-development-server)
- [Running tests](#running-tests)
- [Common commands](#common-commands)
- [Project structure](#project-structure)

---

## Prerequisites ✅

- macOS (tested)
- Python 3.12+ (recommended)
- Git
- (Optional) pyenv for managing multiple Python versions

---

## Installation 🔧

1. Clone the repository:

```bash
git clone <repository-url>
cd link-collector
```

2. Create and activate a virtual environment (using builtin venv):

```bash
python3 -m venv venv
source venv/bin/activate
```

If you prefer pyenv:

```bash
pyenv install 3.11.6
pyenv virtualenv 3.11.6 link-collector
pyenv local link-collector
```

3. Install dependencies:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## Database setup 🗄️

This project uses SQLite by default for development.

Run migrations:

```bash
python manage.py migrate
```
---

## Run the development server ▶️

Start the dev server:

```bash
python manage.py runserver
```

Open your browser at http://127.0.0.1:8000/ to view the app.

The main template is located at `apps/scraper/templates/scraper/index.html`.

---

## Common commands 🧰

- Run shell: `python manage.py shell`
- Apply migrations: `python manage.py migrate`
- Create superuser: `python manage.py createsuperuser`
- Run tests: `python manage.py test`

---

## Project structure 📁

Key files and folders:

```
config/           - Django project configuration (settings, urls, wsgi, asgi)
apps/scraper/     - Scraper app with models, views, templates
manage.py         - Django management script
requirements.txt  - Python dependencies
db.sqlite3        - SQLite database (dev)
```
---

If you'd like, I can add sections for deploying, CI configuration, or environment variable management next. :sparkles:
