from django.db import models

# Create your models here.

class ContactInfo(models.Model):
    email = models.EmailField()
    linkedin_url = models.URLField()
    github_url = models.URLField()
    instagram_url = models.URLField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Contact Info - {self.email}"

    class Meta:
        verbose_name = "Contact Information"
        verbose_name_plural = "Contact Information"

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"
