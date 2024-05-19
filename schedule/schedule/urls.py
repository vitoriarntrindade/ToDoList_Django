"""
URL configuration for schedule project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views
from django.views.generic import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('schedule/', views.list_events, name='list_events'),
    path('schedule/list', views.json_list_event, name="list"),
    path('schedule/event/', views.event, name='event'),
    path('schedule/event/submit', views.submit_event, name='submit_event'),
    path('schedule/event/delete/<int:id_event>/', views.delete_event, name='delete_event'),
    path('', RedirectView.as_view(url='/schedule/'), name='home'),
    path('login/', views.login_user, name='login'),
    path('login/submit', views.submit_login, name='submit_login'),
    path('logout/', views.logout_user, name='logout'),
]
