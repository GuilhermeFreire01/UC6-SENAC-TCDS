from django.contrib import admin
from django.urls import path
from edge_tec import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name= "home")
]
