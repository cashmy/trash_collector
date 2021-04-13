from django.urls import path

from . import views

# TODO: Determine what distinct pages are required for the customer user stories, add a path for each in urlpatterns

app_name = "customers"
urlpatterns = [
    # Customer use views:
    path('', views.index, name="index"),
    # Employee use views:
    path('delete/<int:customer_id>', views.delete, name='delete'),
    path('update/<int:customer_id>', views.update, name='update'),
    path('detail/<int:customer_id>', views.detail, name='detail'),
    path('create/', views.create, name='create_new_customer'),
    path('table/', views.table, name='table'),
    path('index/', views.index, name='index')
]
