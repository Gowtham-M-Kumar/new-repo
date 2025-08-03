from django.db import models

# Create your models here.

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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.get_section_type_display()} - {self.title}"

    class Meta:
        ordering = ['section_type', 'order']
        verbose_name = "Resume Section"
        verbose_name_plural = "Resume Sections"
