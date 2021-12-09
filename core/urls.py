from django import urls
from django.contrib import admin
from django.urls import path, include
from django.urls.conf import include
from .views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', HomeView.as_view(), name="home"),
    
    path('blog/', include('blog.urls', namespace='blog'))
]
