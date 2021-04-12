from django.urls import path
from . import views

app_name = "addresses"
urlpatterns = [

    path('create/', views.create, name='create_new_address'),

]