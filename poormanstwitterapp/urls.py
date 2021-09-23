from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('tweets/', views.get_or_post_tweets, name="get_or_post_tweets"),
]
