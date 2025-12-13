from django.shortcuts import render
from .models import Skills


def home(request):
    skills = Skills.objects.filter(status=True)
    context = {
        "skills": skills
    }
    return render(request, "root/index.html", context=context)
def contact(request):
    return render(request, "root/contact.html")

def about(request):
    return render(request, "root/about.html")

def agent(request):
    return render(request, "root/agents.html")

# Create your views here.
