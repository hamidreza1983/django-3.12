from django.shortcuts import render
from .models import Skills, Agent , Star, Testimonial
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
