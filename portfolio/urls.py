from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# DRF Router
router = DefaultRouter()
router.register(r"auth/register", views.RegisterViewSet, basename="register")
router.register(r"auth/login", views.LoginViewSet, basename="login")
router.register(r"portfolios", views.PortfolioViewSet, basename="portfolio")
router.register(r"skills", views.SkillViewSet, basename="skill")
router.register(r"experience", views.ExperienceViewSet, basename="experience")
router.register(r"projects", views.ProjectViewSet, basename="project")
router.register(r"education", views.EducationViewSet, basename="education")
router.register(r"testimonials", views.TestimonialViewSet, basename="testimonial")
router.register(r"services", views.ServiceViewSet, basename="service")
router.register(r"social-links", views.SocialLinkViewSet, basename="social-link")

urlpatterns = [
    path("api/", include(router.urls)),
    path("api/send-message/", views.send_contact_message, name="send-message"),
    path("", views.portfolio_page, name="portfolio-home"),
    path("<str:username>/", views.portfolio_page, name="portfolio-user"),
    path("admin/login/", views.login_view, name="portfolio-login"),
    path("admin/logout/", views.logout_view, name="portfolio-logout"),
    path("admin/dashboard/", views.admin_dashboard, name="admin-dashboard"),
]
