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
    path('hood', views.neighbourhoods, name='hoods'),
    path('leave-neighbourhood/<int:id>', views.leave_neighbourhood, name='leave_neighbourhood'),
    path('join-neighbourhood/<int:id>', views.join_neighbourhood, name='join_neighbourhood'),
   
    path('business', views.business, name='new-business'),
    path('edit-business/<int:id>', views.editBusiness, name='edit-business'),
    # path('view-business/<int:id>', views.viewBusiness, name="view-busines"),
    path('view-post/<int:id>', views.viewPost, name="view-post"),
    path('edit-post/<int:id>', views.editPost, name='edit-post')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)