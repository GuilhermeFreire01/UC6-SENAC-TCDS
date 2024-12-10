from django.contrib import admin
from django.urls import path, include

#from edge_tec import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('edge_tec.urls'))
]
