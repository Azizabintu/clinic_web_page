
from django.shortcuts import render, redirect
from django.views import View
from landing_page.models import Company

# Create your views here.
class LandingPage(View):
    def get (self,request):
        #companies = Company.objects.all().order_by('id')
        company = Company.objects.get(id=1)
        return render(request,'landing.html',{"company" : company})