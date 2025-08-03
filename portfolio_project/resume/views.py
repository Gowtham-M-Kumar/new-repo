from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from main.decorators import admin_required
from .models import ResumeSection
from .forms import ResumeSectionForm

def resume_view(request):
    """Display resume with all active sections"""
    education = ResumeSection.objects.filter(section_type='education', is_active=True)
    experience = ResumeSection.objects.filter(section_type='experience', is_active=True)
    skills = ResumeSection.objects.filter(section_type='skills', is_active=True)

    context = {
        'education': education,
        'experience': experience,
        'skills': skills,
    }
    return render(request, 'resume/resume_view.html', context)

@admin_required
def resume_section_create(request):
    """Create a new resume section"""
    if request.method == 'POST':
        form = ResumeSectionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Resume section created successfully!')
            return redirect('resume:resume_view')
    else:
        form = ResumeSectionForm()
    
    return render(request, 'resume/resume_section_form.html', {
        'form': form,
        'title': 'Add New Resume Section',
        'action': 'Create'
    })

@admin_required
def resume_section_update(request, pk):
    """Update an existing resume section"""
    section = get_object_or_404(ResumeSection, pk=pk)
    if request.method == 'POST':
        form = ResumeSectionForm(request.POST, instance=section)
        if form.is_valid():
            form.save()
            messages.success(request, 'Resume section updated successfully!')
            return redirect('resume:resume_view')
    else:
        form = ResumeSectionForm(instance=section)
    
    return render(request, 'resume/resume_section_form.html', {
        'form': form,
        'section': section,
        'title': 'Edit Resume Section',
        'action': 'Update'
    })

@admin_required
def resume_section_delete(request, pk):
    """Delete a resume section"""
    section = get_object_or_404(ResumeSection, pk=pk)
    if request.method == 'POST':
        section.delete()
        messages.success(request, 'Resume section deleted successfully!')
        return redirect('resume:resume_view')
    
    return render(request, 'resume/resume_section_confirm_delete.html', {'section': section})

@admin_required
def resume_manage(request):
    """Admin view to manage all resume sections"""
    resume_sections = ResumeSection.objects.all()
    return render(request, 'resume/resume_manage.html', {'resume_sections': resume_sections})
