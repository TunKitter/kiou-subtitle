from django.urls import path
from . import views
urlpatterns = [
    path("subtitle",views.index)
]