
from newblog import views
from django.contrib import admin
from django.urls import include, path
# from views import home

urlpatterns = [
    path('home', views.home),
    path('blog/<slug:url>', views.posts),
    path('category/<slug:url>', views.category)
]
