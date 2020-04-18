from django.urls import path, re_path, include
from .views import (home,
                    logout_view,
                    contact_mail,
                    PostsList,
                    PostDetailView,
                    AuthorsList,
                    AuthorDetailView,

                    user_view,

                )

app_name = 'blog'

urlpatterns = [
    path('', home, name='home'),

    path('logout/', logout_view, name='logout'),

    path('user/', user_view, name='user'),

    path('posts/', PostsList.as_view(), name='posts'),
    path('post/<str:slug>/', PostDetailView.as_view(), name='post'),

    path('authors/', AuthorsList.as_view(), name='authors'),
    path('author/<str:slug>/', AuthorDetailView.as_view(), name='author'),

    path('contactus/', contact_mail, name='contactus'),

]
