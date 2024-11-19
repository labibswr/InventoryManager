"""
URL configuration for InventoryWebApp project.

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
from django.urls import path, include
from user import views as user_view
from user.views import LoginPage, LogoutPage
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static

# All url paths in this list here
urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', include('dashboard.urls')),
    path('registration/', user_view.register, name='user-registration'),
    path('profile/', user_view.profile, name='user-profile'),
    path('profile/edit/', user_view.edit, name='change-profile'),
    path('', LoginPage.as_view(), name='user-login'),
    path('logout/', LogoutPage.as_view(), name='user-logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

