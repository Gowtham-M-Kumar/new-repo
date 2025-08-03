from django import forms
from .models import Contact, Project, ResumeSection, AboutContent, ContactInfo

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Enter your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Enter your email'}),
            'message': forms.Textarea(attrs={'class': 'form-textarea', 'placeholder': 'Write your message...', 'rows': 5}),
        }

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'image', 'github_link', 'live_link', 'tags', 'order', 'is_active']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'github_link': forms.URLInput(attrs={'class': 'form-control'}),
            'live_link': forms.URLInput(attrs={'class': 'form-control'}),
            'tags': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Django, Python, REST API'}),
            'order': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class ResumeSectionForm(forms.ModelForm):
    class Meta:
        model = ResumeSection
        fields = ['section_type', 'title', 'subtitle', 'date_range', 'description', 'order', 'is_active']
        widgets = {
            'section_type': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'subtitle': forms.TextInput(attrs={'class': 'form-control'}),
            'date_range': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'order': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class AboutContentForm(forms.ModelForm):
    class Meta:
        model = AboutContent
        fields = ['title', 'content', 'skills', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'skills': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Python, Django, HTML, CSS'}),
        }

class ContactInfoForm(forms.ModelForm):
    class Meta:
        model = ContactInfo
        fields = ['email', 'linkedin_url', 'github_url', 'instagram_url']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'linkedin_url': forms.URLInput(attrs={'class': 'form-control'}),
            'github_url': forms.URLInput(attrs={'class': 'form-control'}),
            'instagram_url': forms.URLInput(attrs={'class': 'form-control'}),
        }

class SettingsPasswordForm(forms.Form):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter admin password'}),
        label='Admin Password'
    ) 