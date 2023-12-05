from django.urls import path
from services.views import ServivesPage
app_name = 'services'
urlpatterns = [
    path("",ServivesPage.as_view(),name="services")
]

