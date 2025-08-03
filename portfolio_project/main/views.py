from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse
from .forms import AboutContentForm, SettingsPasswordForm
from .models import AboutContent, Settings
from projects.models import Project
from resume.models import ResumeSection
from contact.models import Contact, ContactInfo
from contact.forms import ContactForm

# Create your views here.

def base(request):
    return render(request, 'main/base.html')

def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the contact message
            contact = form.save()
            
            # Send email notification
            try:
                send_mail(
                    subject=f'New Contact Message from {contact.name}',
                    message=f'''
Name: {contact.name}
Email: {contact.email}
Message: {contact.message}
                    ''',
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.DEFAULT_FROM_EMAIL],  # Send to yourself
                    fail_silently=False,
                )
                messages.success(request, 'Thank you! Your message has been sent successfully.')
            except Exception as e:
                # If email fails, still save the message but show a different message
                messages.warning(request, 'Message saved but there was an issue sending the email notification.')
            
            return redirect('home')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()
    
    # Fetch projects from database
    projects = Project.objects.filter(is_active=True).order_by('order', '-created_at')
    
    # Process tags for each project
    for project in projects:
        if project.tags:
            project.tags_list = [tag.strip() for tag in project.tags.split(',') if tag.strip()]
        else:
            project.tags_list = []
    
    # Fetch resume sections from database
    education = ResumeSection.objects.filter(section_type='education', is_active=True).order_by('order', '-created_at')
    experience = ResumeSection.objects.filter(section_type='experience', is_active=True).order_by('order', '-created_at')
    skills = ResumeSection.objects.filter(section_type='skills', is_active=True).order_by('order', '-created_at')
    
    # Fetch about content from database
    about_content = AboutContent.objects.first()
    
    # Process skills for about content
    if about_content and about_content.skills:
        about_content.skills_list = [skill.strip() for skill in about_content.skills.split(',') if skill.strip()]
    else:
        about_content.skills_list = []
    
    # Fetch contact info from database
    contact_info = ContactInfo.objects.first()
    
    return render(request, 'main/home.html', {
        'contact_form': form,
        'projects': projects,
        'education': education,
        'experience': experience,
        'skills': skills,
        'about_content': about_content,
        'contact_info': contact_info
    })

def about(request):
    about_content = AboutContent.objects.first()
    return render(request, 'main/about.html', {'about_content': about_content})

def projects(request):
    projects_list = Project.objects.filter(is_active=True)
    return render(request, 'main/projects.html', {'projects': projects_list})

def resume(request):
    education = ResumeSection.objects.filter(section_type='education', is_active=True)
    experience = ResumeSection.objects.filter(section_type='experience', is_active=True)
    skills = ResumeSection.objects.filter(section_type='skills', is_active=True)
    
    context = {
        'education': education,
        'experience': experience,
        'skills': skills,
    }
    return render(request, 'main/resume.html', context)

def contact(request):
    contact_info = ContactInfo.objects.first()
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the contact message
            contact = form.save()
            
            # Send email notification
            try:
                send_mail(
                    subject=f'New Contact Message from {contact.name}',
                    message=f'''
Name: {contact.name}
Email: {contact.email}
Message: {contact.message}
                    ''',
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.DEFAULT_FROM_EMAIL],  # Send to yourself
                    fail_silently=False,
                )
                messages.success(request, 'Thank you! Your message has been sent successfully.')
            except Exception as e:
                # If email fails, still save the message but show a different message
                messages.warning(request, 'Message saved but there was an issue sending the email notification.')
            
            return redirect('contact:contact_view')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()
    
    return render(request, 'main/contact.html', {'contact_form': form, 'contact_info': contact_info})

# Settings Views
def settings_login(request):
    if request.method == 'POST':
        form = SettingsPasswordForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            settings_obj, created = Settings.objects.get_or_create(id=1)
            
            if created:
                # First time setup - set the password
                settings_obj.admin_password = make_password(password)
                settings_obj.save()
                messages.success(request, 'Admin password set successfully!')
            
            if check_password(password, settings_obj.admin_password):
                request.session['admin_authenticated'] = True
                return redirect('settings_dashboard')
            else:
                messages.error(request, 'Invalid password!')
    else:
        form = SettingsPasswordForm()
    
    return render(request, 'main/settings_login.html', {'form': form})

def settings_dashboard(request):
    if not request.session.get('admin_authenticated'):
        return redirect('settings_login')
    
    projects = Project.objects.all()
    resume_sections = ResumeSection.objects.all()
    about_content = AboutContent.objects.first()
    contact_info = ContactInfo.objects.first()
    
    # Calculate counts for the dashboard
    total_projects = projects.count()
    active_projects = projects.filter(is_active=True).count()
    education_sections = resume_sections.filter(section_type='education').count()
    experience_sections = resume_sections.filter(section_type='experience').count()
    skills_sections = resume_sections.filter(section_type='skills').count()
    
    context = {
        'projects': projects,
        'resume_sections': resume_sections,
        'about_content': about_content,
        'contact_info': contact_info,
        'total_projects': total_projects,
        'active_projects': active_projects,
        'education_sections': education_sections,
        'experience_sections': experience_sections,
        'skills_sections': skills_sections,
    }
    return render(request, 'main/settings_dashboard.html', context)

def settings_logout(request):
    request.session.pop('admin_authenticated', None)
    messages.success(request, 'Logged out successfully!')
    return redirect('settings_login')

# Project Management
def manage_projects(request):
    if not request.session.get('admin_authenticated'):
        return redirect('settings_login')
    
    projects = Project.objects.all()
    
    context = {
        'projects': projects,
        'title': 'Manage Projects'
    }
    return render(request, 'main/manage_projects.html', context)

def add_project(request):
    if not request.session.get('admin_authenticated'):
        return redirect('settings_login')
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project added successfully!')
            return redirect('settings_dashboard')
    else:
        form = ProjectForm()
    
    return render(request, 'main/settings_form.html', {
        'form': form,
        'title': 'Add New Project',
        'action': 'add_project'
    })

def edit_project(request, project_id):
    if not request.session.get('admin_authenticated'):
        return redirect('settings_login')
    
    project = get_object_or_404(Project, id=project_id)
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project updated successfully!')
            return redirect('settings_dashboard')
    else:
        form = ProjectForm(instance=project)
    
    return render(request, 'main/settings_form.html', {
        'form': form,
        'title': 'Edit Project',
        'action': 'edit_project',
        'object': project
    })

def delete_project(request, project_id):
    if not request.session.get('admin_authenticated'):
        return redirect('settings_login')
    
    project = get_object_or_404(Project, id=project_id)
    project.delete()
    messages.success(request, 'Project deleted successfully!')
    return redirect('settings_dashboard')

# Resume Section Management
def manage_resume_sections(request):
    if not request.session.get('admin_authenticated'):
        return redirect('settings_login')
    
    resume_sections = ResumeSection.objects.all()
    
    context = {
        'resume_sections': resume_sections,
        'title': 'Manage Resume Sections'
    }
    return render(request, 'main/manage_resume_sections.html', context)

def add_resume_section(request):
    if not request.session.get('admin_authenticated'):
        return redirect('settings_login')
    
    if request.method == 'POST':
        form = ResumeSectionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Resume section added successfully!')
            return redirect('settings_dashboard')
    else:
        form = ResumeSectionForm()
    
    return render(request, 'main/settings_form.html', {
        'form': form,
        'title': 'Add Resume Section',
        'action': 'add_resume_section'
    })

def edit_resume_section(request, section_id):
    if not request.session.get('admin_authenticated'):
        return redirect('settings_login')
    
    section = get_object_or_404(ResumeSection, id=section_id)
    
    if request.method == 'POST':
        form = ResumeSectionForm(request.POST, instance=section)
        if form.is_valid():
            form.save()
            messages.success(request, 'Resume section updated successfully!')
            return redirect('settings_dashboard')
    else:
        form = ResumeSectionForm(instance=section)
    
    return render(request, 'main/settings_form.html', {
        'form': form,
        'title': 'Edit Resume Section',
        'action': 'edit_resume_section',
        'object': section
    })

def delete_resume_section(request, section_id):
    if not request.session.get('admin_authenticated'):
        return redirect('settings_login')
    
    section = get_object_or_404(ResumeSection, id=section_id)
    section.delete()
    messages.success(request, 'Resume section deleted successfully!')
    return redirect('settings_dashboard')

# About Content Management
def edit_about(request):
    if not request.session.get('admin_authenticated'):
        return redirect('settings_login')
    
    about_content, created = AboutContent.objects.get_or_create(id=1)
    
    if request.method == 'POST':
        form = AboutContentForm(request.POST, request.FILES, instance=about_content)
        if form.is_valid():
            form.save()
            messages.success(request, 'About content updated successfully!')
            return redirect('settings_dashboard')
    else:
        form = AboutContentForm(instance=about_content)
    
    return render(request, 'main/settings_form.html', {
        'form': form,
        'title': 'Edit About Content',
        'action': 'edit_about'
    })

# Contact Info Management
def edit_contact_info(request):
    if not request.session.get('admin_authenticated'):
        return redirect('settings_login')
    
    contact_info, created = ContactInfo.objects.get_or_create(id=1)
    
    if request.method == 'POST':
        form = ContactInfoForm(request.POST, instance=contact_info)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contact information updated successfully!')
            return redirect('settings_dashboard')
    else:
        form = ContactInfoForm(instance=contact_info)
    
    return render(request, 'main/settings_form.html', {
        'form': form,
        'title': 'Edit Contact Information',
        'action': 'edit_contact_info'
    })