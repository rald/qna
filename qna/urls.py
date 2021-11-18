from django.urls import path

from . import views

app_name = 'qna'

urlpatterns = [
    path('register', views.register_request, name='register'),
    path('login', views.login_request, name='login'),
    path('logout', views.logout_request, name='logout'),
    path('', views.homepage, name='homepage'),
    path('subjects/', views.subjects, name='subjects'),
    path('questions/<int:subject_id>/', views.questions, name='questions'),
    path('update_user/', views.update_user_request, name='update_user'),
]
