from django.urls import path
from staff.views import StaffPage
app_name = 'staff'
urlpatterns = [
    path("",StaffPage.as_view(),name="staff")
]