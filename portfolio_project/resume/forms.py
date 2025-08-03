from django import forms
from .models import ResumeSection

class ResumeSectionForm(forms.ModelForm):
    class Meta:
        model = ResumeSection
        fields = ['section_type', 'title', 'subtitle', 'date_range', 'description', 'order', 'is_active']
        widgets = {
            'section_type': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            'subtitle': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter subtitle'}),
            'date_range': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., 2020 - 2024'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter description'}),
            'order': forms.NumberInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        } 