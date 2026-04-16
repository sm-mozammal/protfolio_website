from django.contrib import admin
from .models import (
    Portfolio,
    Skill,
    Experience,
    Project,
    Education,
    Testimonial,
    Service,
    SocialLink,
)


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ["name", "professional_title", "user", "email", "updated_at"]
    search_fields = ["name", "email", "user__username"]
    list_filter = ["created_at", "updated_at"]
    fieldsets = (
        (
            "User & Basic Info",
            {"fields": ("user", "name", "professional_title", "email")},
        ),
        (
            "Content",
            {"fields": ("bio", "tagline", "profile_image", "background_image")},
        ),
        ("Contact", {"fields": ("phone", "location")}),
        (
            "Social Links",
            {"fields": ("github_url", "linkedin_url", "twitter_url", "portfolio_url")},
        ),
        (
            "Stats",
            {"fields": ("years_experience", "projects_completed", "happy_clients")},
        ),
    )


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "category",
        "proficiency",
        "proficiency_percentage",
        "portfolio",
    ]
    list_filter = ["category", "proficiency", "portfolio"]
    search_fields = ["name", "portfolio__name"]
    ordering = ["portfolio", "category", "order"]


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = [
        "job_title",
        "company_name",
        "is_current",
        "start_date",
        "portfolio",
    ]
    list_filter = ["is_current", "employment_type", "start_date", "portfolio"]
    search_fields = ["job_title", "company_name", "portfolio__name"]
    fieldsets = (
        (
            "Job Info",
            {"fields": ("portfolio", "job_title", "company_name", "company_url")},
        ),
        (
            "Employment Details",
            {"fields": ("employment_type", "location", "is_current")},
        ),
        ("Duration", {"fields": ("start_date", "end_date")}),
        ("Description", {"fields": ("description", "highlights")}),
        ("Media", {"fields": ("company_logo",)}),
    )


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["title", "status", "featured", "start_date", "portfolio"]
    list_filter = ["status", "featured", "start_date", "portfolio"]
    search_fields = ["title", "portfolio__name"]
    prepopulated_fields = {"slug": ("title",)}
    fieldsets = (
        (
            "Project Info",
            {"fields": ("portfolio", "title", "slug", "short_description")},
        ),
        ("Content", {"fields": ("description", "thumbnail", "images")}),
        ("Details", {"fields": ("status", "technologies", "start_date", "end_date")}),
        ("Links", {"fields": ("github_url", "live_url")}),
        ("Display", {"fields": ("featured", "order")}),
    )


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ["degree", "institution", "is_current", "start_date", "portfolio"]
    list_filter = ["is_current", "start_date", "portfolio"]
    search_fields = ["degree", "institution", "portfolio__name"]


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ["client_name", "rating", "featured", "portfolio"]
    list_filter = ["featured", "rating", "portfolio"]
    search_fields = ["client_name", "portfolio__name"]
    fieldsets = (
        (
            "Client Info",
            {
                "fields": (
                    "portfolio",
                    "client_name",
                    "client_title",
                    "client_company",
                    "client_image",
                )
            },
        ),
        ("Testimonial", {"fields": ("content", "rating")}),
        ("Display", {"fields": ("featured", "order")}),
    )


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ["title", "portfolio", "order"]
    list_filter = ["portfolio", "created_at"]
    search_fields = ["title", "portfolio__name"]
    ordering = ["portfolio", "order"]


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ["platform", "url", "portfolio", "order"]
    list_filter = ["platform", "portfolio"]
    search_fields = ["platform", "url", "portfolio__name"]
    ordering = ["portfolio", "order"]
