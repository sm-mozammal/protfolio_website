# 🏗️ PORTFOLIO SYSTEM ARCHITECTURE

## System Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                        PORTFOLIO SYSTEM v1.0                        │
└─────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────┐
│                          USER ACCESS LAYER                           │
├──────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  ┌──────────────────┐    ┌──────────────────┐   ┌──────────────┐   │
│  │  PUBLIC VISITOR  │    │  ADMIN USER      │   │   API CLIENT │   │
│  └────────┬─────────┘    └────────┬─────────┘   └──────┬───────┘   │
│           │                       │                     │            │
└───────────┼───────────────────────┼─────────────────────┼────────────┘
            │                       │                     │
            ▼                       ▼                     ▼
    ╔═══════════════╗    ╔═══════════════╗    ╔═════════════════╗
    ║ PORTFOLIO     ║    ║ ADMIN LOGIN   ║    ║  REST API       ║
    ║ WEBSITE       ║    ║ PAGE          ║    ║  ENDPOINTS      ║
    ║               ║    ║               ║    ║                 ║
    ║ /portfolio/   ║    ║ /admin/login/ ║    ║ /api/...        ║
    ╚═══════┬═══════╝    ╚═══════┬═══════╝    ╚────────┬────────╝
            │                    │                     │
            │                    ▼                     │
            │            ╔═══════════════╗             │
            │            ║ ADMIN         ║             │
            │            ║ DASHBOARD     ║             │
            │            ║               ║             │
            │            ║ /admin/       ║             │
            │            ║ dashboard/    ║             │
            │            ╚═══════┬═══════╝             │
            │                    │                     │
            └────────────────────┼─────────────────────┘
                                 │
                    ┌────────────┴────────────┐
                    │                         │
                    ▼                         ▼
            ╔═══════════════╗       ╔═══════════════╗
            ║  DJANGO FORMS │       ║   BROWSER     ║
            ║               ║       ║   (JavaScript)║
            ║  • Profile    ║       ║   (Axios API) ║
            ║  • Skills     ║       ║               ║
            ║  • Experience ║       │ Auto-fetches  │
            ║  • Projects   ║       │ data via API  ║
            ║  • Education  ║       │ in real-time  │
            ║  • etc...     ║       │               ║
            ╚═══════┬═══════╝       ╚═══════════════╝
                    │
                    ▼
        ┌───────────────────────┐
        │  DATABASE OPERATIONS  │
        │  (SQLite)             │
        └───────────┬───────────┘
                    │
                    ▼
┌──────────────────────────────────────────────────────────────────────┐
│                         DATA LAYER                                  │
├──────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐               │
│  │Portfolio │ │ Skill    │ │Experience│ │ Project  │ ...          │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘               │
│                                                                      │
│  All Models with proper relationships and validation                │
│                                                                      │
└──────────────────────────────────────────────────────────────────────┘
```

---

## Request Flow Diagram

### 1️⃣ Admin Adding Skills

```
Admin User
    │
    ├─→ Navigates to Dashboard
    │       │
    │       └─→ Admin Login Page (/portfolio/admin/login/)
    │               │
    │               └─→ Authentication Check
    │                       │
    │                       └─→ Session Created ✓
    │
    ├─→ Admin Dashboard (/portfolio/admin/dashboard/)
    │       │
    │       └─→ Clicks "Skills" Tab
    │               │
    │               └─→ Fills Form
    │                   • Skill Name
    │                   • Category
    │                   • Proficiency Level
    │                   • Percentage
    │
    ├─→ Clicks "Add Skill"
    │       │
    │       └─→ Form Submitted (POST)
    │               │
    │               └─→ Django Form Validation
    │                   │
    │                   └─→ Save to Database
    │
    └─→ Skill Appears in Grid
        │
        └─→ Auto-syncs to Public Portfolio (via API)
```

### 2️⃣ Public Visitor Viewing Portfolio

```
Public Visitor
    │
    ├─→ Opens Portfolio (/portfolio/)
    │       │
    │       └─→ HTML Page Loads
    │           (templates/index.html)
    │
    ├─→ JavaScript Runs (Axios)
    │       │
    │       ├─→ Fetches /portfolio/api/portfolios/
    │       ├─→ Fetches /portfolio/api/skills/
    │       ├─→ Fetches /portfolio/api/experience/
    │       ├─→ Fetches /portfolio/api/projects/
    │       ├─→ Fetches /portfolio/api/education/
    │       ├─→ Fetches /portfolio/api/testimonials/
    │       └─→ Fetches /portfolio/api/social-links/
    │
    ├─→ API Responses (JSON)
    │       │
    │       └─→ JavaScript Renders HTML
    │           • Hero Section
    │           • About Section
    │           • Skills Grid
    │           • Experience Timeline
    │           • Projects Grid
    │           • Testimonials
    │           • Contact Info
    │
    └─→ Beautiful Portfolio Displayed ✓
        (All data from admin dashboard)
```

---

## Technology Stack

```
┌────────────────────────────────────────────────────────────────┐
│                        TECH STACK                              │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  Backend:                                                      │
│  ├─ Django 4.2+                (Web Framework)                │
│  ├─ Django REST Framework       (API)                          │
│  ├─ Python 3.9+                (Language)                      │
│  └─ SQLite 3                   (Database)                      │
│                                                                │
│  Frontend:                                                     │
│  ├─ HTML5                      (Markup)                        │
│  ├─ CSS3                       (Styling)                       │
│  ├─ JavaScript (ES6+)          (Interactivity)                │
│  ├─ Axios                      (HTTP Client)                  │
│  └─ Font Awesome 6.5           (Icons)                        │
│                                                                │
│  Authentication:                                               │
│  ├─ Django Sessions            (Admin)                        │
│  ├─ CSRF Protection            (Security)                     │
│  └─ Login Required Decorator   (Access Control)              │
│                                                                │
│  Deployment:                                                  │
│  ├─ Development: Django runserver                            │
│  └─ Production: Gunicorn, uWSGI                             │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

---

## Data Models Relationship

```
┌─────────────────────────────────────────────────────────────────┐
│                    DATABASE SCHEMA                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│                        Portfolio (Main)                         │
│                        ┌──────────────┐                         │
│                        │ • user_id    │◄─── OneToOneField       │
│                        │ • name       │     User                │
│                        │ • email      │                         │
│                        │ • bio        │                         │
│                        │ • phone      │                         │
│                        │ • location   │                         │
│                        │ • profile_img│                         │
│                        │ • years_exp  │                         │
│                        │ • proj_done  │                         │
│                        │ • happy_cln  │                         │
│                        │ • created_at │                         │
│                        │ • updated_at │                         │
│                        └──────┬───────┘                         │
│                               │                                │
│                ┌──────────────┼──────────────┬─────────────┐  │
│                │              │              │             │  │
│                ▼              ▼              ▼             ▼  │
│        ┌───────────┐  ┌───────────┐ ┌───────────┐ ┌──────────┐
│        │  Skill    │  │Experience │ │ Project   │ │Education │
│        ├───────────┤  ├───────────┤ ├───────────┤ ├──────────┤
│        │ • name    │  │ • title   │ │ • title   │ │ • school │
│        │ • category│  │ • company │ │ • desc    │ │ • degree │
│        │ • prof_lvl│  │ • location│ │ • status  │ │ • field  │
│        │ • prof_%  │  │ • start_dt│ │ • git_url │ │ • year   │
│        │ • portfolio_id (FK)       │ • live_url │ │ • desc   │
│        └───────────┘  └───────────┘ │ • tech    │ └──────────┘
│                                      │ • portfolio_id (FK)
│                                      └───────────┘
│                                              │
│                                  ┌───────────┼──────────┐
│                                  │           │          │
│                                  ▼           ▼          ▼
│                            ┌──────────┐ ┌──────────┐ ┌────────┐
│                            │Testimonial  │ Service │ │Social  │
│                            ├──────────┤ ├──────────┤ ├────────┤
│                            │ • text   │ │ • name   │ │ • plat │
│                            │ • rating │ │ • desc   │ │ • url  │
│                            │ • client │ │ • icon   │ │ • portfolio_id
│                            │ • featured  │ • portfolio_id     
│                            └──────────┘ └──────────┘ └────────┘
│
└─────────────────────────────────────────────────────────────────┘
```

---

## File Structure

```
portfolio_project/
│
├── manage.py                           # Django CLI
├── db.sqlite3                          # Database
├── run_server.sh                       # Start script
│
├── portfolio/                          # Main App
│   ├── models.py                       # Database Models
│   ├── views.py                        # Views & ViewSets
│   ├── urls.py                         # App URLs
│   ├── serializers.py                  # DRF Serializers
│   ├── admin.py                        # Django Admin
│   ├── apps.py
│   │
│   └── templates/portfolio/
│       ├── login.html                  # Admin Login
│       ├── admin_dashboard.html        # Admin Dashboard
│       ├── index.html                  # Portfolio Display
│       └── display_example.html        # Alt Template
│
├── templates/
│   └── index.html                      # Main Portfolio
│
├── portfolio_project/                  # Project Config
│   ├── settings.py                     # Django Settings
│   ├── urls.py                         # Main URLs
│   ├── asgi.py
│   └── wsgi.py
│
├── static/                             # Static files
├── media/                              # User uploads
│
└── Documentation/
    ├── START_HERE.md                   # ⭐ Start here!
    ├── QUICK_REFERENCE.md
    ├── README.md
    ├── QUICKSTART.md
    ├── SETUP_GUIDE.md
    ├── IMPLEMENTATION_COMPLETE.md
    └── PORTFOLIO_API.md
```

---

## API Request/Response Example

### Request
```http
GET /portfolio/api/skills/
```

### Response
```json
{
  "count": 5,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "portfolio": 1,
      "name": "Python",
      "category": "backend",
      "proficiency": "expert",
      "proficiency_percentage": 95,
      "icon_url": "",
      "order": 0,
      "created_at": "2026-04-12T12:00:00Z"
    },
    {
      "id": 2,
      "portfolio": 1,
      "name": "React",
      "category": "frontend",
      "proficiency": "advanced",
      "proficiency_percentage": 85,
      "icon_url": "",
      "order": 1,
      "created_at": "2026-04-12T12:05:00Z"
    }
  ]
}
```

---

## Security Architecture

```
┌────────────────────────────────────────────────────┐
│            SECURITY LAYERS                        │
├────────────────────────────────────────────────────┤
│                                                    │
│  Layer 1: CSRF Protection                         │
│  └─ CSRF Token in all forms                       │
│  └─ Token validation on POST/PUT/DELETE           │
│                                                    │
│  Layer 2: Authentication                          │
│  └─ Login required for admin                      │
│  └─ Session-based auth                            │
│  └─ Secure password hashing                       │
│                                                    │
│  Layer 3: Authorization                           │
│  └─ User can only see own portfolio               │
│  └─ Permission classes on API                     │
│  └─ @login_required decorators                    │
│                                                    │
│  Layer 4: Data Validation                         │
│  └─ Django Form validation                        │
│  └─ DRF Serializer validation                     │
│  └─ Model-level constraints                       │
│                                                    │
│  Layer 5: SQL Injection Prevention                │
│  └─ ORM queries (no raw SQL)                      │
│  └─ Prepared statements                           │
│                                                    │
└────────────────────────────────────────────────────┘
```

---

## Deployment Architecture

```
Development:
  Developer Machine
  └─ Django runserver (port 8000)
  └─ SQLite Database
  └─ Hot reload

Production:
  Web Server
  ├─ Nginx (Reverse Proxy)
  └─ Gunicorn/uWSGI (Application)
      ├─ Django App
      ├─ PostgreSQL Database
      ├─ Static Files (Whitenoise)
      └─ Media Files (S3/Local)
```

---

## Summary

This architecture provides:

✅ **Separation of Concerns**
- Frontend, Backend, Database layers clearly separated
- Models, Views, Serializers properly organized

✅ **Security**
- Multiple authentication/authorization layers
- CSRF protection
- User data isolation

✅ **Scalability**
- API-first design
- Stateless API calls
- Database-agnostic models

✅ **Maintainability**
- Clear folder structure
- Documented code
- Standard Django patterns

✅ **Flexibility**
- Easy to add new sections
- Reusable components
- Frontend-agnostic API

---

**Architecture Version**: 1.0  
**Created**: April 12, 2026  
**Status**: ✅ Production Ready  
