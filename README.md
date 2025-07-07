# Django Blog Application

A full-featured, responsive blog platform built using **Django** and **TailwindCSS**, featuring authentication, category-based filtering, search, and secure post management with user-based permissions.

---

## Features

### Core Features
- Custom User model with unique email address
- Blog post model with categories and author relationships
- Paginated home page (5 posts per page)
- Category filter (via dropdown)
- Case-insensitive search by post title or content
- Post detail view
- User authentication: Register, Login, Logout
- Global context processor for category data
- TailwindCSS (via CDN) for mobile-responsive styling

### Bonus Feature Implemented
- **Permissions**: Only authors can edit or delete their own posts (secured via `@login_required` and `PermissionDenied`)

---

## Tech Stack

- Django 5
- SQLite (default development database)
- TailwindCSS (CDN version)
- Python 3.12

---

## Setup Instructions

Follow the steps below to get the application running locally:

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO
```

### 2. Create and Activate a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser
```bash
python manage.py createsuperuser
```

### 6. Run the Development Server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

---

## Bonus Feature: Permissions

Users are required to be logged in to:
- Create new posts
- Edit their own posts
- Delete their own posts

If a user attempts to edit/delete another user's post, a `PermissionDenied` exception is raised and handled gracefully.

---

## Design Decisions

- ✅ `AbstractUser` used for custom user model
- ✅ Secure logout via POST request
- ✅ Reusable base template with Tailwind navigation bar
- ✅ Global category access via custom context processor
- ✅ Clean code separation via `views`, `forms`, and templates

---

## Project Structure (Simplified)

```
blog_project/
│
├── blog/                   # App folder
│   ├── models.py           # User, Category, BlogPost
│   ├── views.py            # Home, Post Detail, Auth, CRUD
│   ├── forms.py            # Post + Register forms
│   ├── urls.py             # Routes
│   ├── templates/blog/     # All HTML templates
│   └── context_processors.py  # Global category injection
│
├── blog_project/           # Project settings
│   ├── settings.py
│   └── urls.py
│
├── db.sqlite3
├── manage.py
└── README.md               # You're here!
```

---

## Submission Checklist

- [x] Core features implemented
- [x] One bonus feature added: Permissions
- [x] TailwindCSS styling applied
- [x] Category context processor included
- [x] GitHub repo created
- [x] Collaborator `alcuin2` added
- [x] README written

---

## Questions?

If you have questions or suggestions, feel free to open an issue or reach out through GitHub.

---

**Thanks for reviewing my blog platform!**
