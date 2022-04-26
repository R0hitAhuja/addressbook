from django.urls import path
from app import views
from django.urls import include, re_path

app_name = "app"

urlpatterns = [
    path('', views.index, name="index"),
    path('home', views.home, name="home"),
    path('customers', views.employees, name="employees"),
    path('search_employees', views.search_employees, name='search_employees'),
    path('Delete/<int:id>', views.delrec, name = "delete_customer"),
]
