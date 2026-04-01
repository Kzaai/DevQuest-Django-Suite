# 🚀 TaskMaster Pro - Workflow Management System

A professional task and project management system built with **Django**, designed to handle complex relational data and streamline business workflows.

---

## 💡 The Evolution (Pivot from FastAPI)
This project originally started as "UserFlow" using FastAPI. However, to better handle **Enterprise-grade relational data** and leverage the power of a **Robust ORM**, I decided to migrate the core architecture to **Django**. 

This transition allowed for:
* **Structured Data:** Better management of Project-Task relationships.
* **Security:** Built-in protection against common web vulnerabilities.
* **Efficiency:** Rapid development using the Django Admin interface and MVT pattern.

---

## 🛠️ Tech Stack
* **Backend:** Python 3.9+, Django 5.x
* **Database:** SQLite (Development) / PostgreSQL (Planned for Production)
* **Architecture:** MVT (Model-View-Template)

---

## 📈 Current Features
- [x] **Relational Schema:** Implemented `ForeignKey` relationships between Projects and Tasks.
- [x] **Status Workflow:** Integrated `STATUS_CHOICES` (To Do, In Progress, Done) for task tracking.
- [x] **Advanced Admin Panel:** Custom Django Admin with list filters, search fields, and editable statuses.
- [x] **Clean Code:** Adhering to Django best practices and modular app structure.
- [x] **Dynamic Frontend:** Responsive Project Dashboard built with **Bootstrap 5**.

- [x] **Relational Linking:** Implemented dynamic "Detail Views" connecting projects to their specific tasks via Primary Keys (PK).

- [x] **Navigation System:** Global navigation bar for seamless switching between modules.

---

## 🗺️ Roadmap
- [ ] **Public Dashboard:** Creating frontend views to display project progress.
- [ ] **User Authentication:** Implementing multi-user access and task assignment.
- [ ] **REST API:** Adding Django Rest Framework (DRF) for external integrations.
- [ ] **Automated Testing:** Writing UnitTests for core business logic.

---

## ⚙️ Installation
1. Clone the repo: `git clone https://github.com/Kzaai/DevQuest-Django-Suite.git`
2. Create virtualenv: `python -m venv venv`
3. Install dependencies: `pip install -r requirements.txt`
4. Run migrations: `python manage.py migrate`
5. Start server: `python manage.py runserver`