from django.urls import path 
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    # path for home page
    path('classify',views.classify,name='classify'),
    path('result/',views.result,name='respos'),
    path('resultn/',views.resultn,name='resneg'),
    path('create_poll/',views.create_poll,name='create'),
    path('list_polls/',views.list_of_polls,name='list'),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 