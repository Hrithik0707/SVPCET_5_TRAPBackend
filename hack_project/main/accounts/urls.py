from django.urls import path 
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    # path for home page
    path('',views.index,name='index'),
    # path for registration page
    path('register',views.register,name='register'),
    # path for login page
    path('login',views.login,name='login'),
    # path for loging out
    path('logout',views.logout,name='logout')

]

urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)