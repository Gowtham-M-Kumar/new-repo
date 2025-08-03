from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from main.decorators import admin_required
from .models import Project
from .forms import ProjectForm

def project_list(request):
    """Display all active projects"""
    projects = Project.objects.filter(is_active=True)
    
    # Process tags for each project
    for project in projects:
        if project.tags:
            project.tags_list = [tag.strip() for tag in project.tags.split(',') if tag.strip()]
        else:
            project.tags_list = []
    
    return render(request, 'projects/project_list.html', {'projects': projects})

@admin_required
def project_create(request):
    """Create a new project"""
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project created successfully!')
            return redirect('projects:project_list')
    else:
        form = ProjectForm()
    
    return render(request, 'projects/project_form.html', {
        'form': form,
        'title': 'Add New Project',
        'action': 'Create'
    })

@admin_required
def project_update(request, pk):
    """Update an existing project"""
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project updated successfully!')
            return redirect('projects:project_list')
    else:
        form = ProjectForm(instance=project)
    
    return render(request, 'projects/project_form.html', {
        'form': form,
        'project': project,
        'title': 'Edit Project',
        'action': 'Update'
    })

@admin_required
def project_delete(request, pk):
    """Delete a project"""
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.delete()
        messages.success(request, 'Project deleted successfully!')
        return redirect('projects:project_list')
    
    return render(request, 'projects/project_confirm_delete.html', {'project': project})

@admin_required
def project_manage(request):
    """Admin view to manage all projects"""
    projects = Project.objects.all()
    return render(request, 'projects/project_manage.html', {'projects': projects})
