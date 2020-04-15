from django.urls import path, re_path, include
from .views import (home,
                    haha,
                    contact_mail,
                )
app_name = 'blog'
urlpatterns = [
    path('', home, name='home'),
    path('login/', haha, name='login'),
    path('logout/', haha, name='logout'),
    path('signup/', haha, name='signup'),
    path('contactus/', contact_mail, name='contactus'),
]
