from django.urls import path 
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    # path for home page
    path('create_poll/',views.create_poll,name='create'),
    path('list_polls/',views.list_of_polls,name='list'),
    path('vote/',views.vote_poll,name='vote')
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 