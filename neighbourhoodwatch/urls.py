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
    path('post', views.post, name='new-post'),
    path('post', views.post, name='new-post'),
    path('neighbourhood', views.Neighbourhood, name='hood-form'),
    path('business', views.business, name='business'),
    path('edit-business', views.editBusiness, name='edit-business'),
    path('view-post/<int:id>', views.viewPost, name="view-post"),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)