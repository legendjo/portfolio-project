from django.urls import path
from . import views

urlpatterns = [
    path('', views.bloghome, name='bloghome'),
    path('<int:blogpost_id>/', views.blogpostdetails, name='blogpostdetails'),
]
