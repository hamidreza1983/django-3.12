from django.shortcuts import render, redirect
from .models import Skills, Agent , Star, Testimonial, ContactUs
from services.models import Services
from .forms import ContactUsForm
from django.contrib import messages


def home(request):
    services = Services.objects.filter(status=True)[:6]
    agents = Agent.objects.filter(status=True).order_by('-created_at')[:3]
    testinonials = Testimonial.objects.filter(status=True)
    context = {
        "agents": agents,
        "testimonials": testinonials,
        "services" : services,
    }
    return render(request, "root/index.html", context=context)

def contact(request):
    if request.method == "GET":
        return render(request, "root/contact.html")
    elif request.method == "POST":
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "form saved successfully")
            return redirect("/")
        else:
            messages.error(request, "invalid input data")
            return redirect(request.path_info)


        #    name = form.cleaned_data['name']
        #    email = form.cleaned_data['email']
        #    subject = form.cleaned_data['subject']
        #    message = form.cleaned_data['message']
        #    contact = ContactUs(name=name, email=email, subject=subject, message=message)
        #    contact.save()
        #    context = {
        #        "message" : "form saved successfully"
        #    }
        #    return render(request, "root/contact.html", context=context)  .
        #else:
        #    context = {
        #        "message" : "invalid input data"
        #    }
        #    return render(request, "root/contact.html", context=context) 


        #name = request.POST.get("name")
        #if len(name) >= 100 :
        #    return render(request, "root/contact.html")
        #email = request.POST.get("email")
        #if "@" not in email or "." not in email:
        #    return render(request, "root/contact.html")
        #subject = request.POST.get("subject")    
        #message = request.POST.get("message")
        #contact = ContactUs()
        #contact.name = name
        #contact.email = email
        #contact.subject = subject
        #contact.message = message
        #contact.save()
        #return render(request, "root/contact.html")

def about(request):
    return render(request, "root/about.html")

def agent(request):
    agents = Agent.objects.filter(status=True)
    context = {
        "agents": agents
    }
    return render(request, "root/agents.html", context=context)

# Create your views here.
