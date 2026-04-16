# Dynamic Portfolio System - Complete Setup Guide

## 🎯 Overview

This is a fully dynamic portfolio management system built with Django REST API. Features include:

- ✅ User authentication with JWT tokens
- ✅ Complete portfolio CRUD operations
- ✅ Admin dashboard for managing portfolio content
- ✅ RESTful API for frontend integration
- ✅ Support for skills, experience, projects, education, testimonials, and services
- ✅ Image uploads for profile, projects, and testimonials
- ✅ CORS enabled for frontend frameworks

---

## 🚀 Quick Start

### 1. Database Setup
The migrations have been applied. Create a superuser:

```bash
cd portfolio_project
python manage.py createsuperuser
```

### 2. Run Development Server
```bash
python manage.py runserver
```

Access:
- **Admin Panel**: http://localhost:8000/admin/
- **Portfolio API**: http://localhost:8000/portfolio/api/
- **Browsable API**: http://localhost:8000/portfolio/api/portfolios/

---

## 🔐 Authentication

### Register
**POST** `/portfolio/api/auth/register/register/`

```json
{
  "username": "john_dev",
  "email": "john@example.com",
  "password": "securepassword123"
}
```

**Response**:
```json
{
  "user": {"id": 1, "username": "john_dev", "email": "john@example.com"},
  "access": "eyJhbGciOiJIUzI1NiIs...",
  "refresh": "eyJhbGciOiJIUzI1NiIs...",
  "message": "Registration successful"
}
```

### Login
**POST** `/portfolio/api/auth/login/login/`

```json
{
  "username": "john_dev",
  "password": "securepassword123"
}
```

---

## 📋 API Endpoints

### Portfolio Management

#### Get My Portfolio
**GET** `/portfolio/api/portfolios/my_portfolio/`

**Headers**:
```
Authorization: Bearer {access_token}
```

**Response**:
```json
{
  "id": 1,
  "user": {
    "id": 1,
    "username": "john_dev",
    "email": "john@example.com"
  },
  "name": "John Developer",
  "professional_title": "Full Stack Developer",
  "bio": "Passionate developer...",
  "tagline": "Building amazing things with code",
  "profile_image": "...",
  "email": "john@example.com",
  "years_experience": 5,
  "projects_completed": 20,
  "happy_clients": 15,
  "skills": [...],
  "experience": [...],
  "projects": [...]
}
```

#### Update My Portfolio
**PUT/PATCH** `/portfolio/api/portfolios/update_my_portfolio/`

```json
{
  "name": "John Developer",
  "professional_title": "Senior Full Stack Developer",
  "bio": "Updated bio...",
  "years_experience": 6
}
```

### Skills Management

#### List Skills
**GET** `/portfolio/api/skills/`

#### Create Skill
**POST** `/portfolio/api/skills/`

**Headers**:
```
Authorization: Bearer {access_token}
Content-Type: application/json
```

```json
{
  "name": "Python",
  "category": "backend",
  "proficiency": "expert",
  "proficiency_percentage": 95,
  "icon_url": "https://...",
  "order": 1
}
```

#### Update Skill
**PUT** `/portfolio/api/skills/{id}/`

#### Delete Skill
**DELETE** `/portfolio/api/skills/{id}/`

### Experience Management

#### Create Experience
**POST** `/portfolio/api/experience/`

```json
{
  "job_title": "Senior Developer",
  "company_name": "Tech Corp",
  "company_url": "https://techcorp.com",
  "employment_type": "fulltime",
  "location": "San Francisco",
  "is_current": true,
  "start_date": "2022-01-15",
  "end_date": null,
  "description": "Led development of...",
  "highlights": "Achievement 1\nAchievement 2"
}
```

### Projects Management

#### Create Project
**POST** `/portfolio/api/projects/`

```json
{
  "title": "E-Commerce Platform",
  "slug": "ecommerce-platform",
  "description": "Full description...",
  "short_description": "Brief description",
  "thumbnail": "...",
  "status": "completed",
  "technologies": ["Python", "Django", "React"],
  "start_date": "2023-01-01",
  "end_date": "2023-12-31",
  "github_url": "https://github.com/...",
  "live_url": "https://project.com",
  "featured": true,
  "order": 1
}
```

#### Get Project by Slug
**GET** `/portfolio/api/projects/{slug}/`

### Education Management

#### Create Education
**POST** `/portfolio/api/education/`

```json
{
  "institution": "University Name",
  "degree": "Bachelor of Science",
  "field_of_study": "Computer Science",
  "start_date": "2015-09-01",
  "end_date": "2019-06-01",
  "is_current": false,
  "description": "Completed coursework...",
  "grade": "4.0"
}
```

### Testimonials Management

#### Create Testimonial
**POST** `/portfolio/api/testimonials/`

```json
{
  "client_name": "Jane Doe",
  "client_title": "CEO",
  "client_company": "Startup Inc",
  "client_image": "...",
  "content": "John is an amazing developer!",
  "rating": 5,
  "featured": true,
  "order": 1
}
```

### Services Management

#### Create Service
**POST** `/portfolio/api/services/`

```json
{
  "title": "Web Development",
  "description": "Full stack web development services...",
  "icon_url": "https://...",
  "order": 1
}
```

### Social Links Management

#### Create Social Link
**POST** `/portfolio/api/social-links/`

```json
{
  "platform": "github",
  "url": "https://github.com/username",
  "icon_class": "fab fa-github",
  "order": 1
}
```

---

## 🎨 Admin Dashboard

Access the Django admin panel at:
```
http://localhost:8000/admin/
```

**Features:**
- Manage portfolio information
- Add/edit skills with proficiency levels
- Create experience records
- Manage projects with featured status
- Add education credentials
- Manage client testimonials
- Create services offered
- Manage social media links

---

## 📱 Frontend Integration Example

### JavaScript/React Example

```javascript
// Register
async function register(username, email, password) {
  const response = await fetch('http://localhost:8000/portfolio/api/auth/register/register/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ username, email, password })
  });
  const data = await response.json();
  localStorage.setItem('access_token', data.access);
  return data;
}

// Login
async function login(username, password) {
  const response = await fetch('http://localhost:8000/portfolio/api/auth/login/login/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ username, password })
  });
  const data = await response.json();
  localStorage.setItem('access_token', data.access);
  return data;
}

// Fetch Portfolio
async function getPortfolio() {
  const token = localStorage.getItem('access_token');
  const response = await fetch('http://localhost:8000/portfolio/api/portfolios/my_portfolio/', {
    headers: { 'Authorization': `Bearer ${token}` }
  });
  return response.json();
}

// Create Skill
async function createSkill(skillData) {
  const token = localStorage.getItem('access_token');
  const response = await fetch('http://localhost:8000/portfolio/api/skills/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${token}`
    },
    body: JSON.stringify(skillData)
  });
  return response.json();
}
```

---

## 🗂️ Database Models

### Portfolio
- name, professional_title, bio, tagline
- profile_image, background_image
- email, phone, location
- GitHub, LinkedIn, Twitter URLs
- years_experience, projects_completed, happy_clients

### Skill
- name, category (frontend/backend/mobile/database/devops)
- proficiency (beginner/intermediate/advanced/expert)
- proficiency_percentage, icon_url, order

### Experience
- job_title, company_name, company_url
- employment_type (fulltime/parttime/contract/freelance)
- location, is_current, start_date, end_date
- description, highlights, company_logo

### Project
- title, slug, description, short_description
- thumbnail, images (JSON array)
- status (completed/in_progress/archived)
- technologies (JSON array)
- start_date, end_date
- github_url, live_url
- featured, order

### Education
- institution, degree, field_of_study
- start_date, end_date, is_current
- description, grade
- institution_logo

### Testimonial
- client_name, client_title, client_company
- client_image
- content, rating (1-5)
- featured, order

### Service
- title, description
- icon_url, order

### SocialLink
- platform, url, icon_class, order

---

## 🔑 Key Features

✅ **JWT Authentication** - Secure token-based authentication
✅ **CORS Enabled** - Frontend integration ready
✅ **Image Uploads** - Support for profile, project, and testimonial images
✅ **Pagination** - API responses paginated (20 items per page)
✅ **Admin Interface** - Full Django admin for easy management
✅ **Nested Relationships** - Full portfolio with all related data in one request
✅ **Read-Only for Anonymous** - Protect sensitive data while allowing public portfolio viewing

---

## 📄 File Structure

```
portfolio_project/
├── portfolio/
│   ├── models.py          # 9 models for all portfolio data
│   ├── serializers.py     # 10+ serializers for API
│   ├── views.py           # ViewSets for API endpoints
│   ├── admin.py           # Django admin configuration
│   ├── urls.py            # API routes
│   └── migrations/
├── portfolio_project/
│   ├── settings.py        # Updated with REST, JWT, CORS
│   ├── urls.py            # Main URL config
│   └── wsgi.py
├── manage.py
└── db.sqlite3
```

---

## 🚨 Important Notes

1. **Media Files**: Upload folder is at `portfolio_project/media/`
2. **JWT Tokens**: Access tokens expire after 1 hour, use refresh token to get new access
3. **Permissions**: All endpoints require authentication except read-only portfolio viewing
4. **Slug Field**: Project slug must be unique and is used for URL lookups
5. **Image Validation**: Upload only supported image formats (JPG, PNG, GIF)

---

## 🔄 Workflow

1. **User Registration** → Creates portfolio automatically
2. **User Login** → Gets JWT tokens
3. **Add Portfolio Info** → Update via API or admin
4. **Add Skills** → Multiple skill entries with proficiency levels
5. **Add Experience** → Work history with achievements
6. **Add Projects** → Showcase completed work with images
7. **Add Education** → Credentials and certifications
8. **Add Testimonials** → Client/colleague feedback
9. **Add Services** → List of services offered
10. **Add Social Links** → Connect social profiles

---

## ✨ Next Steps

1. Create sample data via admin panel
2. Integrate with frontend framework (React/Vue/Angular)
3. Customize admin interface further
4. Add email notifications
5. Create portfolio viewing page templates
6. Add portfolio statistics/analytics

---

Happy portfolio building! 🎉
