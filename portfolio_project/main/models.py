from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.email}"
    
    class Meta:
        ordering = ['-created_at']

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    live_link = models.URLField(blank=True, null=True)
    tags = models.CharField(max_length=500, help_text="Comma-separated tags")
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['order', '-created_at']

class ResumeSection(models.Model):
    SECTION_CHOICES = [
        ('education', 'Education'),
        ('experience', 'Experience'),
        ('skills', 'Skills'),
    ]
    
    section_type = models.CharField(max_length=20, choices=SECTION_CHOICES)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True)
    date_range = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.get_section_type_display()} - {self.title}"
    
    class Meta:
        ordering = ['section_type', 'order']

class AboutContent(models.Model):
    title = models.CharField(max_length=200, default="Why Hire Me?")
    content = models.TextField()
    skills = models.TextField(help_text="Comma-separated skills")
    image = models.ImageField(upload_to='about_images/', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

class ContactInfo(models.Model):
    email = models.EmailField()
    linkedin_url = models.URLField()
    github_url = models.URLField()
    instagram_url = models.URLField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Contact Info - {self.email}"

class Settings(models.Model):
    admin_password = models.CharField(max_length=128, help_text="Password for accessing settings page")
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return "Admin Settings"
