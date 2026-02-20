from django.shortcuts import render, get_object_or_404
from .models import Services

# Create your views here.


def services(request, *args, **kwargs):
    #if request.GET.get("cat"):
    #    services = Services.objects.filter(category__name=request.GET.get("cat"), status=True)
    #else:
    #    services = Services.objects.filter(status=True)
    #===============================================================
    if kwargs.get("category"):
        services = Services.objects.filter(category__name=kwargs.get("category"), status=True)
    if kwargs.get("tag"):
        services = Services.objects.filter(tags__title=kwargs.get("tag"), status=True)
    elif request.GET.get("search"):
        services = Services.objects.filter(short_content__contains=request.GET.get("search"), status=True)
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