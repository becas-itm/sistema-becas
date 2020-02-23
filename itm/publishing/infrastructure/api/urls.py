from django.urls import path

from . import views


urlpatterns = [
    path('scholarships/<scholarship_id>/approve/', views.approve),
]
