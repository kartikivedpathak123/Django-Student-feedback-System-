from django.urls import path
from feedbackapp import views

urlpatterns = [
    path('home', views.home),
    path('about', views.about),
    path('contact', views.contact),
    path('feedback', views.feedback),
    path('feedback_success', views.feedback_success),
    path('course', views.course),
    path('signup', views.signup),
    path('signin', views.signin),
    path('signout', views.signout),
]
