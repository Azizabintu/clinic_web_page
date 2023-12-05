from django.urls import path
from landing_page.views import LandingPage
app_name = 'landing_page'
urlpatterns = [
    path("",LandingPage.as_view(),name="landing_page")
]