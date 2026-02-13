from django.shortcuts import render
from .models import Skills, Agent , Star, Testimonial, ContactUs
from services.models import Services


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
        name = request.POST.get("name")
        if len(name) >= 100 :
            return render(request, "root/contact.html")
        email = request.POST.get("email")
        if "@" not in email or "." not in email:
            return render(request, "root/contact.html")
        subject = request.POST.get("subject")    
        message = request.POST.get("message")
        contact = ContactUs()
        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.message = message
        contact.save()
        return render(request, "root/contact.html")

def about(request):
    return render(request, "root/about.html")

def agent(request):
    agents = Agent.objects.filter(status=True)
    context = {
        "agents": agents
    }
    return render(request, "root/agents.html", context=context)

# Create your views here.
