from django import forms
from .models import Contact, ContactInfo

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Enter your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Enter your email'}),
            'message': forms.Textarea(attrs={'class': 'form-textarea', 'placeholder': 'Write your message...', 'rows': 5}),
        }

class ContactInfoForm(forms.ModelForm):
    class Meta:
        model = ContactInfo
        fields = ['email', 'linkedin_url', 'github_url', 'instagram_url']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'your.email@example.com'}),
            'linkedin_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://linkedin.com/in/username'}),
            'github_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://github.com/username'}),
            'instagram_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://instagram.com/username'}),
        } 