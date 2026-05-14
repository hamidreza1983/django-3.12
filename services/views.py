from django.shortcuts import render, get_object_or_404
from .models import Services
from accounts.models import UserModel
from django.views.generic import ListView, DetailView

# Create your views here.

class ServicesView(ListView):
    model = Services
    template_name = "services/services.html"
    context_object_name = 'services'
    #queryset = Services.objects.filter(status=True)
    
    def get_queryset(self):
        if self.kwargs.get("category"):
            services = Services.objects.filter(category__name=self.kwargs.get("category"), status=True)
        elif self.kwargs.get("tag"):
            services = Services.objects.filter(tags__title=self.kwargs.get("tag"), status=True)
        elif self.request.GET.get("search"):
            services = Services.objects.filter(short_content__contains=self.request.GET.get("search"), status=True)
        else:
            services = Services.objects.filter(status=True)
        return services
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['user'] = UserModel.objects.get(email="admin@test.com")
        return context
    
    


#def services(request, *args, **kwargs):
    #if request.GET.get("cat"):
    #    services = Services.objects.filter(category__name=request.GET.get("cat"), status=True)
    #else:
    #    services = Services.objects.filter(status=True)
    #===============================================================
    #if kwargs.get("category"):
    #    services = Services.objects.filter(category__name=kwargs.get("category"), status=True)
    #if kwargs.get("tag"):
    #    services = Services.objects.filter(tags__title=kwargs.get("tag"), status=True)
    #elif request.GET.get("search"):
    #    services = Services.objects.filter(short_content__contains=request.GET.get("search"), status=True)
    #else:
    #    services = Services.objects.filter(status=True)
    #context = {
    #    'services' : services
    #}
    #return render(request, "services/services.html", context=context)

#def service_detail(request, id):
##   id = request.GET.get("id")
##    try:
##        service = Services.objects.get(id=id)
##    except:
##        return render(request, "services/404.html")#

#    service = get_object_or_404(Services, id=id)
#    context = {
#        "service" : service
#                }
#    return render(request, "services/service-details.html", context=context)

class ServicesDetailView(DetailView):
    model = Services
    template_name = "services/service-details.html"
    context_object_name = "service"
    #without def get_queryset ----> model.object.get(pk=pk)

    def get_queryset(self):
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['user'] = UserModel.objects.get(email="admin@test.com")
        return context