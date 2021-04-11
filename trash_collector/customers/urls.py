from django.urls import path

from . import views

# TODO: Determine what distinct pages are required for the customer user stories, add a path for each in urlpatterns

app_name = "customers"
urlpatterns = [
    # Customer use views:
    path('', views.index, name="index"),
    # path('FirstTimeCustomer', views.register, name='register'),
    # Employee use views:
    path('delete/<int:customers_id>', views.delete, name='delete'),
    path('update/<int:customers_id>', views.update, name='update'),
    path('create/', views.create, name='create_new_customer'),
    path('table/', views.table, name='table')
]
