
from django.urls import path
from . import views

app_name="sitepages"

urlpatterns = [
    path('', views.index, name="index"),
    path('custom-user-model', views.article1, name="article1"),
    path('user-upload-form', views.article2, name="article2"),
]
