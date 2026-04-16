from django.db import models
from django.core.validators import URLValidator, MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User


class Portfolio(models.Model):
    """Main portfolio/profile information"""

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="portfolio"
    )
    name = models.CharField(max_length=200)
    professional_title = models.CharField(
        max_length=200, help_text="e.g., Flutter & Django Developer"
    )
    bio = models.TextField(help_text="Short professional bio")
    tagline = models.CharField(max_length=500, help_text="Your professional tagline")
    profile_image = models.ImageField(upload_to="portfolio/", blank=True, null=True)
    background_image = models.ImageField(
        upload_to="portfolio/backgrounds/", blank=True, null=True
    )

    # Contact & Social
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=200, blank=True)

    # Links
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    portfolio_url = models.URLField(blank=True)

    # Stats
    years_experience = models.IntegerField(default=1, validators=[MinValueValidator(1)])
    projects_completed = models.IntegerField(
        default=0, validators=[MinValueValidator(0)]
    )
    happy_clients = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}'s Portfolio"

    class Meta:
        ordering = ["-updated_at"]


class Skill(models.Model):
    """Skills & expertise"""

    SKILL_CATEGORY_CHOICES = (
        ("frontend", "Frontend"),
        ("backend", "Backend"),
        ("mobile", "Mobile"),
        ("database", "Database"),
        ("devops", "DevOps"),
        ("other", "Other"),
    )

    PROFICIENCY_CHOICES = (
        ("beginner", "Beginner"),
        ("intermediate", "Intermediate"),
        ("advanced", "Advanced"),
        ("expert", "Expert"),
    )

    portfolio = models.ForeignKey(
        Portfolio, on_delete=models.CASCADE, related_name="skills"
    )
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=SKILL_CATEGORY_CHOICES)
    proficiency = models.CharField(
        max_length=20, choices=PROFICIENCY_CHOICES, default="intermediate"
    )
    proficiency_percentage = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    icon_url = models.URLField(blank=True, help_text="Optional icon URL")
    order = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.category}"

    class Meta:
        ordering = ["category", "order", "-created_at"]


class Experience(models.Model):
    """Work experience"""

    EMPLOYMENT_TYPE = (
        ("fulltime", "Full-time"),
        ("parttime", "Part-time"),
        ("contract", "Contract"),
        ("freelance", "Freelance"),
        ("internship", "Internship"),
    )

    portfolio = models.ForeignKey(
        Portfolio, on_delete=models.CASCADE, related_name="experience"
    )
    job_title = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    company_url = models.URLField(blank=True)
    employment_type = models.CharField(
        max_length=20, choices=EMPLOYMENT_TYPE, default="fulltime"
    )
    location = models.CharField(max_length=200, blank=True)
    is_current = models.BooleanField(default=False)

    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    description = models.TextField(help_text="Job description and responsibilities")
    highlights = models.TextField(
        blank=True, help_text="Key achievements (one per line)"
    )

    company_logo = models.ImageField(upload_to="companies/", blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.job_title} at {self.company_name}"

    class Meta:
        ordering = ["-is_current", "-start_date"]


class Project(models.Model):
    """Portfolio projects"""

    STATUS_CHOICES = (
        ("completed", "Completed"),
        ("in_progress", "In Progress"),
        ("archived", "Archived"),
    )

    portfolio = models.ForeignKey(
        Portfolio, on_delete=models.CASCADE, related_name="projects"
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    short_description = models.CharField(max_length=300)

    # Media
    thumbnail = models.ImageField(upload_to="projects/")
    images = models.JSONField(default=list, blank=True, help_text="List of image URLs")

    # Details
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="completed"
    )
    technologies = models.JSONField(default=list, help_text="List of technologies used")
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    # Links
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)

    # SEO & Display
    featured = models.BooleanField(default=False)
    order = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-featured", "-order", "-start_date"]


class Education(models.Model):
    """Education & certifications"""

    portfolio = models.ForeignKey(
        Portfolio, on_delete=models.CASCADE, related_name="education"
    )
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    field_of_study = models.CharField(max_length=200)

    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    is_current = models.BooleanField(default=False)

    description = models.TextField(blank=True)
    grade = models.CharField(max_length=10, blank=True)

    institution_logo = models.ImageField(
        upload_to="institutions/", blank=True, null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.degree} from {self.institution}"

    class Meta:
        ordering = ["-is_current", "-start_date"]


class Testimonial(models.Model):
    """Client/colleague testimonials"""

    portfolio = models.ForeignKey(
        Portfolio, on_delete=models.CASCADE, related_name="testimonials"
    )
    client_name = models.CharField(max_length=200)
    client_title = models.CharField(max_length=200, blank=True)
    client_company = models.CharField(max_length=200, blank=True)
    client_image = models.ImageField(upload_to="testimonials/", blank=True, null=True)

    content = models.TextField()
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)], default=5
    )

    featured = models.BooleanField(default=False)
    order = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Testimonial from {self.client_name}"

    class Meta:
        ordering = ["-featured", "order", "-created_at"]


class Service(models.Model):
    """Services offered"""

    portfolio = models.ForeignKey(
        Portfolio, on_delete=models.CASCADE, related_name="services"
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon_url = models.URLField(blank=True)
    order = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["order", "created_at"]


class SocialLink(models.Model):
    """Social media links"""

    PLATFORM_CHOICES = (
        ("github", "GitHub"),
        ("linkedin", "LinkedIn"),
        ("twitter", "Twitter"),
        ("instagram", "Instagram"),
        ("facebook", "Facebook"),
        ("youtube", "YouTube"),
        ("other", "Other"),
    )

    portfolio = models.ForeignKey(
        Portfolio, on_delete=models.CASCADE, related_name="social_links"
    )
    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES)
    url = models.URLField()
    icon_class = models.CharField(
        max_length=100, blank=True, help_text="Font Awesome class or similar"
    )
    order = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.platform} - {self.url}"

    class Meta:
        ordering = ["order"]


class ContactMessage(models.Model):
    """Messages sent through the portfolio contact form"""

    STATUS_CHOICES = (
        ("new", "New"),
        ("read", "Read"),
        ("replied", "Replied"),
        ("archived", "Archived"),
    )

    portfolio = models.ForeignKey(
        Portfolio, on_delete=models.CASCADE, related_name="contact_messages"
    )
    sender_name = models.CharField(max_length=200)
    sender_email = models.EmailField()
    subject = models.CharField(max_length=500)
    message = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="new")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.subject} - {self.sender_email}"

    class Meta:
        ordering = ["-created_at"]
