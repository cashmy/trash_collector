from django.urls import path
from . import views

app_name = "addresses"
urlpatterns = [
    path('create/', views.create, name='create'),
    path('update/<int:address_id>', views.update, name='update'),
]

