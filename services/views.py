from django.shortcuts import render, redirect
from django.views import View
from services.models import Service

# Create your views here.
class ServivesPage(View):
    def get (self,request):
        services = Service.objects.all().order_by('id')
        return render(request,'services.html',{"services" : services})