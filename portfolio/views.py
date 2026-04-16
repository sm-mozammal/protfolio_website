from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.utils.text import slugify
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

from .models import (
    Portfolio,
    Skill,
    Experience,
    Project,
    Education,
    Testimonial,
    Service,
    SocialLink,
    ContactMessage,
)
from .serializers import (
    PortfolioSerializer,
    PortfolioDetailSerializer,
    SkillSerializer,
    ExperienceSerializer,
    ProjectSerializer,
    EducationSerializer,
    TestimonialSerializer,
    ServiceSerializer,
    SocialLinkSerializer,
    ContactMessageSerializer,
    UserSerializer,
)


# Authentication Views
class RegisterViewSet(viewsets.ViewSet):
    """User registration"""

    permission_classes = [permissions.AllowAny]

    @action(detail=False, methods=["post"])
    def register(self, request):
        username = request.data.get("username")
        email = request.data.get("email")
        password = request.data.get("password")

        if not username or not email or not password:
            return Response(
                {"error": "Please provide username, email, and password"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if User.objects.filter(username=username).exists():
            return Response(
                {"error": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST
            )

        user = User.objects.create_user(
            username=username, email=email, password=password
        )

        # Create portfolio for user
        Portfolio.objects.create(user=user, name=username, email=email)

        # Get JWT tokens
        refresh = RefreshToken.for_user(user)

        return Response(
            {
                "user": UserSerializer(user).data,
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "message": "Registration successful",
            },
            status=status.HTTP_201_CREATED,
        )


class LoginViewSet(viewsets.ViewSet):
    """User login"""

    permission_classes = [permissions.AllowAny]

    @action(detail=False, methods=["post"])
    def login(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response(
                {"error": "Please provide username and password"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = authenticate(username=username, password=password)

        if not user:
            return Response(
                {"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
            )

        refresh = RefreshToken.for_user(user)

        return Response(
            {
                "user": UserSerializer(user).data,
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "message": "Login successful",
            },
            status=status.HTTP_200_OK,
        )


# Portfolio ViewSets
class PortfolioViewSet(viewsets.ModelViewSet):
    """Portfolio CRUD operations"""

    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.action == "retrieve":
            return PortfolioDetailSerializer
        return PortfolioSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Portfolio.objects.filter(user=user)
        return Portfolio.objects.all()

    @action(detail=False, methods=["get"])
    def my_portfolio(self, request):
        """Get current user's portfolio"""
        if not request.user.is_authenticated:
            return Response(
                {"error": "Authentication required"},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        portfolio = get_object_or_404(Portfolio, user=request.user)
        serializer = PortfolioDetailSerializer(portfolio)
        return Response(serializer.data)

    @action(detail=False, methods=["put", "patch"])
    def update_my_portfolio(self, request):
        """Update current user's portfolio"""
        if not request.user.is_authenticated:
            return Response(
                {"error": "Authentication required"},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        portfolio = get_object_or_404(Portfolio, user=request.user)
        serializer = PortfolioSerializer(portfolio, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SkillViewSet(viewsets.ModelViewSet):
    """Skill management"""

    serializer_class = SkillSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated and hasattr(user, "portfolio"):
            return Skill.objects.filter(portfolio=user.portfolio)
        return Skill.objects.all()

    def perform_create(self, serializer):
        portfolio = get_object_or_404(Portfolio, user=self.request.user)
        serializer.save(portfolio=portfolio)


class ExperienceViewSet(viewsets.ModelViewSet):
    """Experience management"""

    serializer_class = ExperienceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated and hasattr(user, "portfolio"):
            return Experience.objects.filter(portfolio=user.portfolio)
        return Experience.objects.all()

    def perform_create(self, serializer):
        portfolio = get_object_or_404(Portfolio, user=self.request.user)
        serializer.save(portfolio=portfolio)


class ProjectViewSet(viewsets.ModelViewSet):
    """Project management"""

    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = "slug"

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated and hasattr(user, "portfolio"):
            return Project.objects.filter(portfolio=user.portfolio)
        return Project.objects.filter(status="completed")

    def perform_create(self, serializer):
        portfolio = get_object_or_404(Portfolio, user=self.request.user)
        serializer.save(portfolio=portfolio)


class EducationViewSet(viewsets.ModelViewSet):
    """Education management"""

    serializer_class = EducationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated and hasattr(user, "portfolio"):
            return Education.objects.filter(portfolio=user.portfolio)
        return Education.objects.all()

    def perform_create(self, serializer):
        portfolio = get_object_or_404(Portfolio, user=self.request.user)
        serializer.save(portfolio=portfolio)


class TestimonialViewSet(viewsets.ModelViewSet):
    """Testimonial management"""

    serializer_class = TestimonialSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated and hasattr(user, "portfolio"):
            return Testimonial.objects.filter(portfolio=user.portfolio)
        return Testimonial.objects.filter(featured=True)

    def perform_create(self, serializer):
        portfolio = get_object_or_404(Portfolio, user=self.request.user)
        serializer.save(portfolio=portfolio)


class ServiceViewSet(viewsets.ModelViewSet):
    """Service management"""

    serializer_class = ServiceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated and hasattr(user, "portfolio"):
            return Service.objects.filter(portfolio=user.portfolio)
        return Service.objects.all()

    def perform_create(self, serializer):
        portfolio = get_object_or_404(Portfolio, user=self.request.user)
        serializer.save(portfolio=portfolio)


class SocialLinkViewSet(viewsets.ModelViewSet):
    """Social links management"""

    serializer_class = SocialLinkSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated and hasattr(user, "portfolio"):
            return SocialLink.objects.filter(portfolio=user.portfolio)
        return SocialLink.objects.all()

    def perform_create(self, serializer):
        portfolio = get_object_or_404(Portfolio, user=self.request.user)
        serializer.save(portfolio=portfolio)


# HTML Views for Frontend
def login_view(request):
    """Custom login page for admin dashboard"""
    if request.user.is_authenticated:
        return redirect("admin-dashboard")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("admin-dashboard")
        else:
            return render(
                request,
                "portfolio/login.html",
                {"error": "Invalid username or password"},
            )

    return render(request, "portfolio/login.html")


def logout_view(request):
    """Logout from admin dashboard"""
    logout(request)
    return redirect("portfolio-home")


@login_required(login_url="portfolio-login")
def admin_dashboard(request):
    """Admin dashboard - requires authentication"""
    portfolio = get_object_or_404(Portfolio, user=request.user)

    if request.method == "POST":
        action = request.POST.get("action", "")

        # =========================
        # Update profile
        # =========================
        if action == "update_profile" or action == "":
            portfolio.name = request.POST.get("name", portfolio.name)
            portfolio.professional_title = request.POST.get(
                "professional_title", portfolio.professional_title
            )
            portfolio.email = request.POST.get("email", portfolio.email)
            portfolio.phone = request.POST.get("phone", portfolio.phone)
            portfolio.location = request.POST.get("location", portfolio.location)
            portfolio.bio = request.POST.get("bio", portfolio.bio)
            portfolio.tagline = request.POST.get("tagline", portfolio.tagline)
            portfolio.github_url = request.POST.get("github_url", portfolio.github_url)
            portfolio.linkedin_url = request.POST.get(
                "linkedin_url", portfolio.linkedin_url
            )
            portfolio.twitter_url = request.POST.get(
                "twitter_url", portfolio.twitter_url
            )

            # handle profile image upload (optional)
            uploaded_profile_image = request.FILES.get("profile_image")
            if uploaded_profile_image:
                portfolio.profile_image = uploaded_profile_image

            years = request.POST.get("years_experience")
            if years not in (None, ""):
                try:
                    portfolio.years_experience = int(years)
                except ValueError:
                    pass

            projects = request.POST.get("projects_completed")
            if projects not in (None, ""):
                try:
                    portfolio.projects_completed = int(projects)
                except ValueError:
                    pass

            clients = request.POST.get("happy_clients")
            if clients not in (None, ""):
                try:
                    portfolio.happy_clients = int(clients)
                except ValueError:
                    pass

            portfolio.save()
            messages.success(request, "Profile updated.")

        # =========================
        # Add skill
        # =========================
        elif action == "add_skill":
            name = (request.POST.get("skill_name") or "").strip()
            category = (request.POST.get("skill_category") or "other").strip().lower()
            proficiency = (
                (request.POST.get("proficiency") or "intermediate").strip().lower()
            )
            proficiency_percentage = request.POST.get("proficiency_percentage")

            if not name:
                messages.error(request, "Skill name is required.")
            else:
                try:
                    pct = (
                        int(proficiency_percentage)
                        if proficiency_percentage not in (None, "")
                        else 70
                    )
                except ValueError:
                    pct = 70

                # Allow either choice keys (backend) or free text from legacy form.
                allowed_categories = {c[0] for c in Skill.SKILL_CATEGORY_CHOICES}
                if category not in allowed_categories:
                    category = "other"

                allowed_proficiency = {p[0] for p in Skill.PROFICIENCY_CHOICES}
                if proficiency not in allowed_proficiency:
                    proficiency = "intermediate"

                icon_url = (request.POST.get("skill_icon_url") or "").strip()
                uploaded_skill_icon = request.FILES.get("skill_icon")

                skill = Skill.objects.create(
                    portfolio=portfolio,
                    name=name,
                    category=category,
                    proficiency=proficiency,
                    proficiency_percentage=max(0, min(100, pct)),
                    icon_url=icon_url,
                )

                # If an icon file was uploaded, store its served URL in icon_url.
                if uploaded_skill_icon:
                    skill.icon_url = ""
                    skill.save()  # ensure it has an id
                    from django.core.files.storage import default_storage

                    rel_path = default_storage.save(
                        f"skills/{skill.id}/{uploaded_skill_icon.name}",
                        uploaded_skill_icon,
                    )
                    skill.icon_url = default_storage.url(rel_path)
                    skill.save(update_fields=["icon_url"])

                messages.success(request, "Skill added.")

        # =========================
        # Delete skill
        # =========================
        elif action == "delete_skill":
            skill_id = request.POST.get("skill_id")
            Skill.objects.filter(id=skill_id, portfolio=portfolio).delete()
            messages.success(request, "Skill deleted.")

        # =========================
        # Add experience
        # =========================
        elif action == "add_experience":
            job_title = (request.POST.get("job_title") or "").strip()
            company_name = (request.POST.get("company_name") or "").strip()
            start_date = request.POST.get("start_date")
            is_current = request.POST.get("is_current") == "on"
            end_date = request.POST.get("end_date") or None
            description = (request.POST.get("description") or "").strip()

            if not (job_title and company_name and start_date and description):
                messages.error(
                    request,
                    "Please fill job title, company, start date, and description.",
                )
            else:
                if is_current:
                    end_date = None
                Experience.objects.create(
                    portfolio=portfolio,
                    job_title=job_title,
                    company_name=company_name,
                    start_date=start_date,
                    end_date=end_date,
                    is_current=is_current,
                    description=description,
                    employment_type=(request.POST.get("employment_type") or "fulltime"),
                    location=(request.POST.get("exp_location") or ""),
                    company_url=(request.POST.get("company_url") or ""),
                    highlights=(request.POST.get("highlights") or ""),
                )
                messages.success(request, "Experience added.")

        # =========================
        # Add education
        # =========================
        elif action == "add_education":
            institution = (request.POST.get("institution") or "").strip()
            degree = (request.POST.get("degree") or "").strip()
            field_of_study = (request.POST.get("field_of_study") or "").strip()
            start_date = request.POST.get("edu_start_date")
            is_current = request.POST.get("edu_is_current") == "on"
            end_date = request.POST.get("edu_end_date") or None
            description = (request.POST.get("edu_description") or "").strip()

            if not (institution and degree and field_of_study and start_date):
                messages.error(
                    request,
                    "Please fill institution, degree, field of study, and start date.",
                )
            else:
                if is_current:
                    end_date = None
                Education.objects.create(
                    portfolio=portfolio,
                    institution=institution,
                    degree=degree,
                    field_of_study=field_of_study,
                    start_date=start_date,
                    end_date=end_date,
                    is_current=is_current,
                    description=description,
                    grade=(request.POST.get("grade") or ""),
                )
                messages.success(request, "Education added.")

        # =========================
        # Add project
        # =========================
        elif action == "add_project":
            title = (request.POST.get("project_title") or "").strip()
            short_description = (request.POST.get("short_description") or "").strip()
            description = (request.POST.get("project_description") or "").strip()
            start_date = request.POST.get("project_start_date")
            status_val = (request.POST.get("status") or "completed").strip()

            if not (title and short_description and description and start_date):
                messages.error(
                    request,
                    "Please fill title, short description, description, and start date.",
                )
            else:
                # Ensure unique slug
                base_slug = slugify(title) or "project"
                slug = base_slug
                i = 2
                while Project.objects.filter(slug=slug).exists():
                    slug = f"{base_slug}-{i}"
                    i += 1

                tech_raw = (request.POST.get("technologies") or "").strip()
                technologies = [t.strip() for t in tech_raw.split(",") if t.strip()]

                uploaded_thumbnail = request.FILES.get("thumbnail")
                if not uploaded_thumbnail:
                    messages.error(request, "Project thumbnail is required.")
                else:
                    Project.objects.create(
                        portfolio=portfolio,
                        title=title,
                        slug=slug,
                        short_description=short_description,
                        description=description,
                        status=status_val,
                        start_date=start_date,
                        end_date=request.POST.get("project_end_date") or None,
                        technologies=technologies,
                        github_url=(request.POST.get("github_url") or ""),
                        live_url=(request.POST.get("live_url") or ""),
                        images=[],
                        thumbnail=uploaded_thumbnail,
                    )
                    messages.success(request, "Project added.")

        # =========================
        # Delete experience
        # =========================
        elif action == "delete_experience":
            exp_id = request.POST.get("experience_id")
            Experience.objects.filter(id=exp_id, portfolio=portfolio).delete()
            messages.success(request, "Experience deleted.")

        # =========================
        # Delete project
        # =========================
        elif action == "delete_project":
            proj_id = request.POST.get("project_id")
            Project.objects.filter(id=proj_id, portfolio=portfolio).delete()
            messages.success(request, "Project deleted.")

        # =========================
        # Delete education
        # =========================
        elif action == "delete_education":
            edu_id = request.POST.get("education_id")
            Education.objects.filter(id=edu_id, portfolio=portfolio).delete()
            messages.success(request, "Education deleted.")

        # =========================
        # Update skill
        # =========================
        elif action == "update_skill":
            skill_id = request.POST.get("skill_id")
            skill = get_object_or_404(Skill, id=skill_id, portfolio=portfolio)

            name = (request.POST.get("skill_name") or "").strip()
            category = (
                (request.POST.get("skill_category") or skill.category).strip().lower()
            )
            proficiency = (
                (request.POST.get("proficiency") or skill.proficiency).strip().lower()
            )

            proficiency_percentage = request.POST.get("proficiency_percentage")
            try:
                pct = (
                    int(proficiency_percentage)
                    if proficiency_percentage not in (None, "")
                    else skill.proficiency_percentage
                )
            except ValueError:
                pct = skill.proficiency_percentage

            allowed_categories = {c[0] for c in Skill.SKILL_CATEGORY_CHOICES}
            if category not in allowed_categories:
                category = skill.category

            allowed_proficiency = {p[0] for p in Skill.PROFICIENCY_CHOICES}
            if proficiency not in allowed_proficiency:
                proficiency = skill.proficiency

            icon_url = (request.POST.get("skill_icon_url") or "").strip()
            uploaded_skill_icon = request.FILES.get("skill_icon")

            if not name:
                messages.error(request, "Skill name is required.")
            else:
                skill.name = name
                skill.category = category
                skill.proficiency = proficiency
                skill.proficiency_percentage = max(0, min(100, pct))
                if icon_url:
                    skill.icon_url = icon_url
                skill.save()

                if uploaded_skill_icon:
                    from django.core.files.storage import default_storage

                    rel_path = default_storage.save(
                        f"skills/{skill.id}/{uploaded_skill_icon.name}",
                        uploaded_skill_icon,
                    )
                    skill.icon_url = default_storage.url(rel_path)
                    skill.save(update_fields=["icon_url"])

                messages.success(request, "Skill updated.")

        # =========================
        # Update project
        # =========================
        elif action == "update_project":
            proj_id = request.POST.get("project_id")
            project = get_object_or_404(Project, id=proj_id, portfolio=portfolio)

            title = (request.POST.get("project_title") or "").strip()
            short_description = (request.POST.get("short_description") or "").strip()
            description = (request.POST.get("project_description") or "").strip()
            start_date = request.POST.get("project_start_date")
            status_val = (request.POST.get("status") or project.status).strip()

            if not (title and short_description and description and start_date):
                messages.error(
                    request,
                    "Please fill title, short description, description, and start date.",
                )
            else:
                if title != project.title:
                    base_slug = slugify(title) or "project"
                    slug = base_slug
                    i = 2
                    while (
                        Project.objects.filter(slug=slug)
                        .exclude(id=project.id)
                        .exists()
                    ):
                        slug = f"{base_slug}-{i}"
                        i += 1
                    project.slug = slug

                tech_raw = (request.POST.get("technologies") or "").strip()
                technologies = [t.strip() for t in tech_raw.split(",") if t.strip()]

                project.title = title
                project.short_description = short_description
                project.description = description
                project.status = status_val
                project.start_date = start_date
                project.end_date = request.POST.get("project_end_date") or None
                project.technologies = technologies
                project.github_url = request.POST.get("github_url") or ""
                project.live_url = request.POST.get("live_url") or ""

                uploaded_thumbnail = request.FILES.get("thumbnail")
                if uploaded_thumbnail:
                    project.thumbnail = uploaded_thumbnail

                project.save()
                messages.success(request, "Project updated.")

        # =========================
        # Update education
        # =========================
        elif action == "update_education":
            edu_id = request.POST.get("education_id")
            edu = get_object_or_404(Education, id=edu_id, portfolio=portfolio)

            institution = (request.POST.get("institution") or "").strip()
            degree = (request.POST.get("degree") or "").strip()
            field_of_study = (request.POST.get("field_of_study") or "").strip()
            start_date = request.POST.get("edu_start_date")
            end_date = request.POST.get("edu_end_date") or None

            if not (institution and degree and field_of_study and start_date):
                messages.error(
                    request,
                    "Please fill institution, degree, field of study, and start date.",
                )
            else:
                edu.institution = institution
                edu.degree = degree
                edu.field_of_study = field_of_study
                edu.start_date = start_date
                edu.end_date = end_date
                edu.grade = request.POST.get("grade") or ""
                edu.description = request.POST.get("edu_description") or ""
                edu.save()
                messages.success(request, "Education updated.")

    context = {
        "portfolio": portfolio,
        "skills": portfolio.skills.all(),
        "experience": portfolio.experience.all(),
        "projects": portfolio.projects.all(),
        "education": portfolio.education.all(),
        "testimonials": portfolio.testimonials.all(),
        "services": portfolio.services.all(),
    }

    return render(request, "portfolio/admin_dashboard_complete.html", context)


def portfolio_page(request, username=None):
    """Display portfolio page"""
    try:
        # Prefer showing the logged-in user's portfolio
        if username:
            user = get_object_or_404(User, username=username)
            portfolio = get_object_or_404(Portfolio, user=user)
        elif request.user.is_authenticated and hasattr(request.user, "portfolio"):
            portfolio = request.user.portfolio
        else:
            portfolio = Portfolio.objects.first()

        if not portfolio:
            context = {
                "portfolio": None,
                "skills": [],
                "experience": [],
                "projects": [],
                "education": [],
                "testimonials": [],
                "services": [],
            }
            return render(request, "portfolio/index.html", context)

        context = {
            "portfolio": portfolio,
            "skills": portfolio.skills.all(),
            "experience": portfolio.experience.all(),
            "projects": portfolio.projects.filter(status="completed"),
            "education": portfolio.education.all(),
            "testimonials": portfolio.testimonials.filter(featured=True),
            "services": portfolio.services.all(),
        }

        return render(request, "portfolio/index.html", context)
    except Exception as e:
        # Handle any errors gracefully
        context = {
            "portfolio": None,
            "skills": [],
            "experience": [],
            "projects": [],
            "education": [],
            "testimonials": [],
            "services": [],
            "error": str(e),
        }
        return render(request, "portfolio/index.html", context)


@csrf_exempt
@require_http_methods(["POST"])
def send_contact_message(request):
    """Handle contact form submission and send email"""
    try:
        portfolio_id = request.POST.get("portfolio_id")
        sender_name = request.POST.get("sender_name", "").strip()
        sender_email = request.POST.get("sender_email", "").strip()
        subject = request.POST.get("subject", "").strip()
        message_text = request.POST.get("message", "").strip()

        # Validation
        if not all([sender_name, sender_email, subject, message_text]):
            return JsonResponse(
                {"error": "All fields are required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Get portfolio
        portfolio = get_object_or_404(Portfolio, id=portfolio_id)

        # Create ContactMessage record
        contact_message = ContactMessage.objects.create(
            portfolio=portfolio,
            sender_name=sender_name,
            sender_email=sender_email,
            subject=subject,
            message=message_text,
        )

        # Send email to portfolio owner
        try:
            email_subject = f"New Message: {subject}"
            email_message = f"""
You have received a new message from your portfolio website.

From: {sender_name}
Email: {sender_email}

Subject: {subject}

Message:
{message_text}

---
This message was sent through your portfolio contact form.
"""
            send_mail(
                email_subject,
                email_message,
                settings.DEFAULT_FROM_EMAIL or sender_email,
                [portfolio.email],
                fail_silently=False,
            )
        except Exception as email_error:
            # Log the error but don't fail the request
            print(f"Error sending email: {email_error}")

        return JsonResponse(
            {
                "success": True,
                "message": "Your message has been sent successfully!",
            },
            status=status.HTTP_201_CREATED,
        )

    except Portfolio.DoesNotExist:
        return JsonResponse(
            {"error": "Portfolio not found"},
            status=status.HTTP_404_NOT_FOUND,
        )
    except Exception as e:
        return JsonResponse(
            {"error": f"Error sending message: {str(e)}"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
