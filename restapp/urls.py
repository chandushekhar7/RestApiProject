from django.urls import path
from restapp import views

urlpatterns = [
    path('home/',views.home),
    path('rest/',views.Restapi),

]
