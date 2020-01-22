from django.urls import path
from demo_app2 import views

urlpatterns=[
    path('index/', views.index)
]