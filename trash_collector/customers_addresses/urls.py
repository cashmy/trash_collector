from django.urls import path

from . import views

# TODO: Determine what distinct pages are required for the customer user stories, add a path for each in urlpatterns

app_name = "customers_addresses"
urlpatterns = [
    # Customer use views:
    path('reg/', views.create, name="create_new_custAddress"),
]