from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('', views.home, name='home'),
    path('profile', views.profile, name='profile'),
    path('projects', views.projects, name='projects'),
    path('project/<str:name>', views.single_project, name='single_project'),
    path('articles/', views.articles, name='articles'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
