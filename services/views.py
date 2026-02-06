from django.shortcuts import render, get_object_or_404
from .models import Services

# Create your views here.


def services(request, category=None):
    #if request.GET.get("cat"):
    #    services = Services.objects.filter(category__name=request.GET.get("cat"), status=True)
    #else:
    #    services = Services.objects.filter(status=True)
    #===============================================================
    if category:
        services = Services.objects.filter(category__name=category, status=True)
    else:
        services = Services.objects.filter(status=True)
    context = {
        'services' : services
    }
    return render(request, "services/services.html", context=context)

def service_detail(request, id):
#   id = request.GET.get("id")
#    try:
#        service = Services.objects.get(id=id)
#    except:
#        return render(request, "services/404.html")

    service = get_object_or_404(Services, id=id)
    context = {
        "service" : service
                }
    return render(request, "services/service-details.html", context=context)