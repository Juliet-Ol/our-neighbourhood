from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views
from neighbourhoodwatch import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/register/', views.register, name='register'),
    path('profile', views.profile, name='profile'),
    path('edit-profile', views.editProfile, name='edit-profile'),
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)