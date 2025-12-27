from django.shortcuts import render
from .models import Skills, Agent , Star, Testimonial


def home(request):
    agents = Agent.objects.filter(status=True).order_by('-created_at')[:3]
    testinonials = Testimonial.objects.filter(status=True)
    context = {
        "agents": agents,
        "testimonials": testinonials
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
