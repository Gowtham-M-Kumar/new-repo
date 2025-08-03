from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from main.decorators import admin_required
from django.core.mail import send_mail
from django.conf import settings
from .models import Contact, ContactInfo
from .forms import ContactForm, ContactInfoForm

def contact_view(request):
    """Display contact page with form and contact info"""
    contact_info = ContactInfo.objects.first()
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            
            # Send email notification (optional)
            try:
                send_mail(
                    f'New Contact Message from {contact.name}',
                    f'Name: {contact.name}\nEmail: {contact.email}\nMessage: {contact.message}',
                    settings.DEFAULT_FROM_EMAIL,
                    [contact_info.email if contact_info else settings.DEFAULT_FROM_EMAIL],
                    fail_silently=True,
                )
            except:
                pass  # Email sending failed, but don't break the form submission
            
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact:contact_view')
    else:
        form = ContactForm()
    
    return render(request, 'contact/contact_view.html', {
        'form': form,
        'contact_info': contact_info
    })

@admin_required
def contact_info_edit(request):
    """Edit contact information"""
    contact_info = ContactInfo.objects.first()
    if not contact_info:
        contact_info = ContactInfo.objects.create(
            email='your.email@example.com',
            linkedin_url='https://linkedin.com/in/username',
            github_url='https://github.com/username'
        )
    
    if request.method == 'POST':
        form = ContactInfoForm(request.POST, instance=contact_info)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contact information updated successfully!')
            return redirect('contact:contact_view')
    else:
        form = ContactInfoForm(instance=contact_info)
    
    return render(request, 'contact/contact_info_form.html', {
        'form': form,
        'title': 'Edit Contact Information'
    })

@admin_required
def contact_messages(request):
    """View all contact messages (admin only)"""
    messages_list = Contact.objects.all()
    return render(request, 'contact/contact_messages.html', {'messages': messages_list})

@admin_required
def contact_message_detail(request, pk):
    """View a specific contact message"""
    message = get_object_or_404(Contact, pk=pk)
    return render(request, 'contact/contact_message_detail.html', {'message': message})

@admin_required
def contact_message_delete(request, pk):
    """Delete a contact message"""
    message = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        message.delete()
        messages.success(request, 'Message deleted successfully!')
        return redirect('contact:contact_messages')
    
    return render(request, 'contact/contact_message_confirm_delete.html', {'message': message})
