# Django REST API ToDo App

A full-stack ToDo List web application built using **Django REST Framework**, **MySQL**, and **JWT authentication** with a clean Bootstrap frontend. Users can register, log in, and manage their tasks with full CRUD functionality.


🚀 Features

- 🔐 JWT-based user authentication
- ➕ Create new tasks
- ✅ Mark tasks as complete
- 🗑️ Delete tasks
- 📆 Add due dates
- 📊 Task priority (Low, Medium, High)
- 🧾 Bootstrap-styled UI
- ⚡ Auto-refresh task list after actions



# Tech Stack

| Layer       | Technology                         |
|-------------|------------------------------------|
| Backend     | Django, Django REST Framework      |
| Frontend    | HTML, CSS, Bootstrap 5             |
| Auth        | JWT via `rest_framework_simplejwt` |
| Database    | MySQL                              |
| Icons       | Font Awesome                       |

---

# Installation

```bash
git clone https://github.com/devaroopan/django-todo-api.git
cd django-todo-api
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
