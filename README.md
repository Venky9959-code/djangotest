# Django Blog API

A Django REST Framework application for managing blog posts, created for Full Stack Development.

## Features

- **Post Model**: Stores blog posts with title, content, and creation timestamp.
- **REST API Endpoints**:
  - List all posts: `GET /api/posts/`
  - Retrieve single post: `GET /api/posts/<id>/`
- **Django Admin Interface**: Admin management for blog posts at `/admin/`.
- **Unit Tests**: Test suite verifying models and REST API endpoints.

## Tech Stack

- **Python 3.10+**
- **Django 5.2**
- **Django REST Framework**
- **SQLite**

## Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/Venky9959-code/djangotest.git
```

### 2. Set up Virtual Environment

Create and activate virtual environment:

**Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\activate
```

**Linux / macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Database Migrations

```bash
python manage.py migrate
```

*(Note: Ensure your virtual environment is activated before running `python manage.py migrate` to prevent `ModuleNotFoundError: No module named 'rest_framework'`)*

### 5. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 6. Run Development Server

```bash
python manage.py runserver
```

Access the API at `http://127.0.0.1:8000/api/posts/` and the admin panel at `http://127.0.0.1:8000/admin/`.

## Running Unit Tests

To run the automated test suite:

```bash
python manage.py test
```
