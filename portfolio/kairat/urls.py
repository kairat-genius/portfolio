from django.urls import path

from kairat import views

urlpatterns = [
    path('', views.ContactFormView.as_view()),
]