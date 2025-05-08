from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('create-event/', views.create_event, name='create_event'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('new-event-page/', views.new_event_page_view, name='new_event_page'),


]
