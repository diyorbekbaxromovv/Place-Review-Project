from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import settings
from . import views
urlpatterns = [
    path('', include('food.urls')),
    path('users/', include('users.urls')),
    path('admin/', admin.site.urls),
    path('home/', views.HomeView.as_view(), name='home'),
    
    
]
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)