from django.shortcuts import render, redirect
from django.db import models
from django.contrib import admin
from django.core.mail import send_mail
from django.contrib import messages 

from .models import Profile, Resume, Portfolio, Summary, Education, Contact

# HOME
def index(request):
    smry=Summary.objects.all()
    education=Education.objects.all()
    
    
    profile_data = Profile.objects.values()
    context={'smry':smry,'profile': profile_data,'education':education}
    print(profile_data)
    return render(request, 'index.html',context)


def contact(request):
    if request.method == "POST":
        name = request.POST.get('user_name')    
        email = request.POST.get('user_email')  
        phone = request.POST.get('phone')  
        message = request.POST.get('message')

        # Save to database
        contact = Contact.objects.create(
            name=name,
            email=email,
            phone=phone,
            message=message,  # or use 'message=' if your model has 'message' field
        )

        # Send email (This must be BEFORE return)
        send_mail(
            subject=f"New Contact from {name}",
            message=f"Name: {name}\nEmail: {email}\nPhone: {phone}\n\nMessage:\n{message}",
            from_email="saniyadav7755@gmail.com",
            recipient_list=["sani228142@gmail.com"],
            fail_silently=False,
        )

        messages.success(request, "Your message has been sent successfully!")

        return redirect('/') 
    else:
        return render(request, 'contact.html')


# ABOUT US
def about_us(request):
    about_us = about_us.objects.values()
    return render(request, 'about_us.html', {'about': about_us})

# RESUME 
def resume(request):
    resume = Resume.objects.values()
    print(resume)
    return render(request, 'resume.html', {'resume': resume})


# SERVICES 
def services(request):
    services = services.objects.values()
    print(services)
    return render(request, 'home.html')
    

# PORTFOLIO 
def portfolio(request):
    portfolio = Portfolio.objects.values()
    print(portfolio)
    return render(request,'portfolio.html', {'portfolio': portfolio})

# PORTFOLIO DETAILS 
def portfolio_details(request):
    return render(request, 'portfolio-details.html')

# JOB PAGE
def job(request):
    return render(request, 'job.html')

# PROJECT 2 PAGE
def project2(request):
    return render(request, 'project2.html')

# PROJECT 04 PAGE
def project04(request):
    return render(request, 'project04.html')

# PROJECT4
def project4(request):
    return render(request, 'project4.html')

# SERVICE DETAILS PAGE
def service_details(request):
    service = request.GET.get('service', 'web') 
    context = {
        'service': service
    }
    return render(request, 'service-details.html', context)

# SKILLS PAGE
def skills(request):
    return render(request, 'skills.html')

# PROJECT05
def project05(request):
    return render(request, 'project05.html')

# PROJECT 06 PAGE
def project06(request):
    return render(request, 'project06.html')

# QUICKSUPPORT PAGE
def quicksupport(request):
    return render(request, 'quicksupport.html')

