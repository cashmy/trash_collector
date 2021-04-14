from django.urls import path

from . import views

# TODO: Determine what distinct pages are required for the customer user stories, add a path for each in urlpatterns

app_name = "employees"
urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create, name='create_new_employee'),
    path('confirm/<int:customer_id>', views.completed_pickup, name='confirmation'),
    path('preview/<int:day>', views.preview, name='preview')
]
