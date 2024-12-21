
# for class based views use .view_class

from django.urls import path
from . import views

urlpatterns = [
    path('', views.accept, name="accept"),
    path('<int:id>/', views.resume, name="resume"),
    path('list/', views.list, name="list"),
]
