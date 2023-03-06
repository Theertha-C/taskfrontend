from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'bapp'

urlpatterns = [
    path("", views.index, name="index"),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),


]
