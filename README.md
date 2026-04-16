# 🎯 Dynamic Portfolio Management System

## 📋 Overview

A **complete, production-ready portfolio management system** built with Django REST Framework with both a powerful admin dashboard and beautiful public portfolio website. Transform your static portfolio into a dynamic, data-driven platform where you can manage all your professional information.

---

## ✨ Key Features

### 🔐 **Admin Dashboard** 
- **Login Page**: Beautiful, secure authentication
- **Dashboard**: Tabbed interface with sidebar navigation
- **Profile Management**: Update your professional information
- **Skills Manager**: Add skills with proficiency levels
- **Experience Tracker**: Manage work history
- **Projects Showcase**: Add completed projects
- **Education**: List academic credentials
- **Testimonials**: Manage client feedback
- **Services**: Define what you offer
- **Statistics**: Display career achievements
- **Mobile Responsive**: Works on all devices

### 🌐 **Public Portfolio Website**
- **Hero Section**: Professional introduction with stats
- **About Section**: Your bio and highlights
- **Skills Display**: Visual skill cards with progress bars
- **Experience Timeline**: Beautiful work history timeline
- **Projects Grid**: Showcase your projects
- **Education Timeline**: Academic background
- **Testimonials**: Client feedback section
- **Contact Info**: Email and social links
- **Theme Toggle**: Dark/Light mode support
- **Fully Responsive**: Perfect on any device

### 🔌 **REST API**
- Full CRUD endpoints for all data types
- JSON responses for easy integration
- Pagination and filtering support
- Image upload capabilities
- Nested data serialization

### 📱 **Authentication & Security**
- Secure login/logout system
- Session-based authentication
- User isolation (each user sees their own data)
- CSRF protection on all forms
- Permission-based access control

---

## 🚀 Quick Start

### 1. Prerequisites
- Python 3.8+
- pip (Python package manager)

### 2. Setup Virtual Environment
```bash
cd /Users/limerickdev/myproject/portfolio_project
```

### 3. Create Admin Account
```bash
/Users/limerickdev/myproject/venv/bin/python manage.py createsuperuser
# Follow prompts to create your admin account
```

### 4. Start Server
```bash
/Users/limerickdev/myproject/venv/bin/python manage.py runserver
```

Server runs at: `http://127.0.0.1:8000/`

### 5. Access Your Portfolio

| Component | URL |
|-----------|-----|
| **Public Portfolio** | http://127.0.0.1:8000/portfolio/ |
| **Admin Login** | http://127.0.0.1:8000/portfolio/admin/login/ |
| **Admin Dashboard** | http://127.0.0.1:8000/portfolio/admin/dashboard/ |
| **REST API** | http://127.0.0.1:8000/portfolio/api/ |
| **Django Admin** | http://127.0.0.1:8000/admin/ |

---

## 📖 Usage Guide

### Adding Portfolio Content

#### 1. Login to Dashboard
- Visit http://127.0.0.1:8000/portfolio/admin/login/
- Enter your superuser credentials

#### 2. Update Your Profile
1. Click "Profile" in sidebar
2. Fill in your information:
   - Name, Professional Title, Bio
   - Contact info (Email, Phone, Location)
   - Social media links
   - Professional statistics
3. Click "Save Changes"

#### 3. Add Skills
1. Click "Skills" in sidebar
2. Fill in "Add New Skill" form:
   - Skill name (e.g., "Python", "React")
   - Category (Frontend, Backend, Mobile, etc.)
   - Proficiency level and percentage
3. Click "Add Skill"

#### 4. Add Experience
1. Click "Experience" in sidebar
2. Fill in the form:
   - Job title, Company, Location
   - Employment type, Start/End dates
   - Description
3. Click "Add Experience"

#### 5. Add Projects
1. Click "Projects" in sidebar
2. Create project:
   - Title, Description, Status
   - GitHub/Live links
   - Technologies used
3. Click "Add Project"

#### 6. Add Education
1. Click "Education" in sidebar
2. Add details:
   - School, Degree, Field of Study
   - Graduation year, Description
3. Click "Add Education"

#### 7. Add Testimonials
1. Click "Testimonials" in sidebar
2. Fill in:
   - Client name and company
   - Testimonial text
   - Rating (1-5 stars)
   - Mark as featured
3. Click "Add Testimonial"

#### 8. Add Services
1. Click "Services" in sidebar
2. Add:
   - Service name and description
   - Icon (Font Awesome class)
3. Click "Add Service"

---

## 📁 Project Structure

## 🚀 Quick Start

### Step 1: Install Dependencies
```bash
pip install djangorestframework djangorestframework-simplejwt django-cors-headers Pillow
```

### Step 2: Apply Migrations
```bash
cd portfolio_project
python manage.py migrate
```

### Step 3: Create Admin User
```bash
python manage.py createsuperuser
```

### Step 4: Start Server
```bash
python manage.py runserver
```

### Step 5: Access Services
- **Admin Panel**: http://localhost:8000/admin/
- **API Root**: http://localhost:8000/portfolio/api/
- **Browsable API**: http://localhost:8000/portfolio/api/portfolios/

---

## 📚 API Documentation

### Authentication

#### Register New User
```
POST /portfolio/api/auth/register/register/
Content-Type: application/json

{
  "username": "johndoe",
  "email": "john@example.com",
  "password": "securepass123"
}

Response:
{
  "user": {...},
  "access": "eyJhbGciOiJIUzI1NiIs...",
  "refresh": "eyJhbGciOiJIUzI1NiIs...",
  "message": "Registration successful"
}
```

#### Login
```
POST /portfolio/api/auth/login/login/
Content-Type: application/json

{
  "username": "johndoe",
  "password": "securepass123"
}

Response:
{
  "user": {...},
  "access": "...",
  "refresh": "...",
  "message": "Login successful"
}
```

### Portfolio Management

#### Get My Full Portfolio
```
GET /portfolio/api/portfolios/my_portfolio/
Authorization: Bearer {access_token}

Response:
{
  "id": 1,
  "name": "John Doe",
  "professional_title": "Full Stack Developer",
  "bio": "...",
  "skills": [...],
  "experience": [...],
  "projects": [...],
  "education": [...],
  "testimonials": [...],
  "services": [...]
}
```

#### Update Portfolio
```
PATCH /portfolio/api/portfolios/update_my_portfolio/
Authorization: Bearer {access_token}
Content-Type: application/json

{
  "name": "John Doe",
  "professional_title": "Senior Full Stack Developer",
  "years_experience": 6
}
```

### Skills Management

#### Create Skill
```
POST /portfolio/api/skills/
Authorization: Bearer {access_token}
Content-Type: application/json

{
  "name": "Python",
  "category": "backend",
  "proficiency": "expert",
  "proficiency_percentage": 95,
  "order": 1
}
```

#### List Skills
```
GET /portfolio/api/skills/
```

#### Update Skill
```
PUT /portfolio/api/skills/{id}/
Authorization: Bearer {access_token}
```

#### Delete Skill
```
DELETE /portfolio/api/skills/{id}/
Authorization: Bearer {access_token}
```

### Experience Management

#### Create Experience
```
POST /portfolio/api/experience/
Authorization: Bearer {access_token}

{
  "job_title": "Senior Developer",
  "company_name": "Tech Corp",
  "company_url": "https://techcorp.com",
  "employment_type": "fulltime",
  "location": "San Francisco",
  "is_current": true,
  "start_date": "2022-01-15",
  "description": "Led development of...",
  "highlights": "Achievement 1\nAchievement 2"
}
```

### Projects Management

#### Create Project
```
POST /portfolio/api/projects/
Authorization: Bearer {access_token}
Content-Type: multipart/form-data

{
  "title": "E-Commerce Platform",
  "slug": "ecommerce-platform",
  "description": "Full e-commerce platform...",
  "short_description": "Modern e-commerce",
  "thumbnail": (image file),
  "status": "completed",
  "technologies": ["Python", "Django", "React"],
  "start_date": "2023-01-01",
  "end_date": "2023-12-31",
  "github_url": "https://github.com/...",
  "live_url": "https://project.com",
  "featured": true
}
```

#### Get Project by Slug
```
GET /portfolio/api/projects/{slug}/
```

### Additional Endpoints
- **Education**: `/portfolio/api/education/`
- **Testimonials**: `/portfolio/api/testimonials/`
- **Services**: `/portfolio/api/services/`
- **Social Links**: `/portfolio/api/social-links/`

---

## 🗂️ Database Models

```
Portfolio (Main Profile)
├── id, user_id, name, professional_title
├── bio, tagline, profile_image, background_image
├── email, phone, location
├── github_url, linkedin_url, twitter_url
└── years_experience, projects_completed, happy_clients

Skill
├── portfolio_id, name, category
├── proficiency, proficiency_percentage
└── icon_url, order

Experience
├── portfolio_id, job_title, company_name
├── employment_type, is_current
├── start_date, end_date
└── description, highlights, company_logo

Project
├── portfolio_id, title, slug
├── description, short_description
├── thumbnail, images (JSON)
├── status, technologies (JSON)
├── start_date, end_date
├── github_url, live_url
└── featured, order

Education
├── portfolio_id, institution, degree
├── field_of_study, is_current
├── start_date, end_date
└── description, grade, institution_logo

Testimonial
├── portfolio_id, client_name
├── client_title, client_company, client_image
├── content, rating (1-5)
└── featured, order

Service
├── portfolio_id, title, description
└── icon_url, order

SocialLink
├── portfolio_id, platform, url
└── icon_class, order
```

---

## 💻 Frontend Integration Examples

### JavaScript/Fetch API

```javascript
const API_URL = 'http://localhost:8000/portfolio/api';

// Register
async function register(username, email, password) {
  const response = await fetch(`${API_URL}/auth/register/register/`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ username, email, password })
  });
  return response.json();
}

// Login
async function login(username, password) {
  const response = await fetch(`${API_URL}/auth/login/login/`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ username, password })
  });
  const data = await response.json();
  localStorage.setItem('access_token', data.access);
  return data;
}

// Get Portfolio
async function getPortfolio() {
  const token = localStorage.getItem('access_token');
  const response = await fetch(`${API_URL}/portfolios/my_portfolio/`, {
    headers: { 'Authorization': `Bearer ${token}` }
  });
  return response.json();
}

// Add Skill
async function addSkill(skillData) {
  const token = localStorage.getItem('access_token');
  const response = await fetch(`${API_URL}/skills/`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${token}`
    },
    body: JSON.stringify(skillData)
  });
  return response.json();
}

// Add Project
async function addProject(formData) {
  const token = localStorage.getItem('access_token');
  const response = await fetch(`${API_URL}/projects/`, {
    method: 'POST',
    headers: { 'Authorization': `Bearer ${token}` },
    body: formData  // Use FormData for file uploads
  });
  return response.json();
}
```

### React Example

```jsx
import { useState, useEffect } from 'react';

function Portfolio() {
  const [portfolio, setPortfolio] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchPortfolio = async () => {
      const token = localStorage.getItem('access_token');
      const response = await fetch(
        'http://localhost:8000/portfolio/api/portfolios/my_portfolio/',
        { headers: { 'Authorization': `Bearer ${token}` } }
      );
      const data = await response.json();
      setPortfolio(data);
      setLoading(false);
    };
    fetchPortfolio();
  }, []);

  if (loading) return <div>Loading...</div>;

  return (
    <div>
      <h1>{portfolio.name}</h1>
      <h2>{portfolio.professional_title}</h2>
      <p>{portfolio.bio}</p>
      {/* Render skills, experience, projects, etc. */}
    </div>
  );
}
```

---

## 🎨 Admin Interface Features

1. **Portfolio Section**
   - Edit name, title, bio, tagline
   - Upload profile and background images
   - Manage contact information
   - Configure social links
   - Update statistics

2. **Skills Section**
   - Add technical skills
   - Set proficiency levels (1-100%)
   - Categorize by type (frontend, backend, etc.)
   - Reorder skills

3. **Experience Section**
   - Add work history
   - Mark current position
   - Include company logo
   - Add achievements and highlights

4. **Projects Section**
   - Create project showcase
   - Upload images and galleries
   - Add technology stack
   - Link to GitHub and live demo
   - Feature projects on homepage

5. **Education Section**
   - Add degrees and certifications
   - Include institution logo
   - Track current studies

6. **Testimonials Section**
   - Add client feedback
   - 5-star ratings
   - Feature testimonials
   - Include client photos

---

## 🔧 Configuration

### CORS Settings
Edit `portfolio_project/settings.py`:
```python
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",    # React
    "http://localhost:8080",    # Vue
    "http://localhost:4200",    # Angular
    "https://yourdomain.com",   # Production
]
```

### JWT Settings
```python
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
}
```

### Media Files
```python
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
```

---

## 📊 Project Structure

```
portfolio_project/
├── portfolio/
│   ├── models.py              # 8 models
│   ├── serializers.py         # 10+ serializers
│   ├── views.py               # ViewSets for API
│   ├── admin.py               # Admin configuration
│   ├── urls.py                # API routes
│   ├── migrations/
│   └── templates/
│       └── portfolio/
│           └── display_example.html
├── portfolio_project/
│   ├── settings.py            # Updated with REST/JWT/CORS
│   ├── urls.py                # Main routes
│   └── wsgi.py
├── manage.py
├── db.sqlite3
├── PORTFOLIO_API.md           # Full API docs
├── SETUP_SUMMARY.md           # Setup guide
└── quickstart.sh              # Quick start script
```

---

## 🐛 Troubleshooting

### Issue: "No module named 'rest_framework'"
**Solution**: Install dependencies
```bash
pip install djangorestframework djangorestframework-simplejwt django-cors-headers
```

### Issue: Migrations not applied
**Solution**: 
```bash
python manage.py makemigrations portfolio
python manage.py migrate
```

### Issue: Images not uploading
**Solution**: Check media folder permissions and DEBUG=True

### Issue: CORS errors
**Solution**: Add your frontend URL to CORS_ALLOWED_ORIGINS

### Issue: 401 Unauthorized
**Solution**: Include valid JWT token in Authorization header

---

## ✅ Deployment Checklist

- [ ] Change DEBUG = False
- [ ] Update ALLOWED_HOSTS
- [ ] Set CORS_ALLOWED_ORIGINS to production domain
- [ ] Use environment variables for secrets
- [ ] Configure static files serving
- [ ] Set up database backup
- [ ] Enable HTTPS
- [ ] Configure email for password reset
- [ ] Set up error logging
- [ ] Run security checks: `python manage.py check --deploy`

---

## 📝 Next Steps

1. **Populate Data**
   - Create superuser account
   - Add your portfolio information via admin
   - Upload profile image and projects

2. **Build Frontend**
   - Create login/register pages
   - Build portfolio display page
   - Create admin dashboard UI
   - Implement form validation

3. **Enhance Features**
   - Add email notifications
   - Implement search functionality
   - Add analytics dashboard
   - Create blog section
   - Add contact form

---

## 📚 Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [JWT Documentation](https://django-rest-framework-simplejwt.readthedocs.io/)
- [Django CORS](https://github.com/adamchainz/django-cors-headers)

---

## 📞 Support

For issues or questions:
1. Check the documentation files
2. Review API examples
3. Check Django logs
4. Verify database migrations

---

## 📄 License

MIT License - Feel free to use this system for personal or commercial projects.

---

## 🎉 You're All Set!

Your dynamic portfolio management system is ready to use. Start by:

1. Running `python manage.py runserver`
2. Creating a superuser account
3. Adding your portfolio information via admin
4. Integrating the API with your frontend

**Happy building! 🚀**
