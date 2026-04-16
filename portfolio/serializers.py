from rest_framework import serializers
from django.contrib.auth.models import User
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


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "first_name", "last_name"]
        read_only_fields = ["id"]


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = "__all__"


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = "__all__"


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"


class SocialLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLink
        fields = "__all__"


class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = [
            "id",
            "sender_name",
            "sender_email",
            "subject",
            "message",
            "status",
            "created_at",
        ]
        read_only_fields = ["id", "status", "created_at"]


class PortfolioDetailSerializer(serializers.ModelSerializer):
    """Full portfolio with all related data"""

    skills = SkillSerializer(many=True, read_only=True)
    experience = ExperienceSerializer(many=True, read_only=True)
    projects = ProjectSerializer(many=True, read_only=True)
    education = EducationSerializer(many=True, read_only=True)
    testimonials = TestimonialSerializer(many=True, read_only=True)
    services = ServiceSerializer(many=True, read_only=True)
    social_links = SocialLinkSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Portfolio
        fields = "__all__"


class PortfolioSerializer(serializers.ModelSerializer):
    """Portfolio overview"""

    user = UserSerializer(read_only=True)

    class Meta:
        model = Portfolio
        fields = [
            "id",
            "user",
            "name",
            "professional_title",
            "bio",
            "tagline",
            "profile_image",
            "email",
            "location",
            "years_experience",
            "projects_completed",
            "happy_clients",
            "created_at",
            "updated_at",
        ]
