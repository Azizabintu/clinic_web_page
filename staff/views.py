from django.shortcuts import render, redirect
from django.views import View
from staff.models import Worker

# Create your views here.
class StaffPage(View):
    def get (self,request):
        workers = Worker.objects.all().order_by('id')
        return render(request,'staff.html',{"workers" : workers})
