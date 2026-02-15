"""
URL configuration for portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib.sitemaps.views import sitemap
from webapp import views
from webapp.sitemap import StaticViewSitemap
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.base import TemplateView


# Sitemap configuration
sitemaps = {
    'static': StaticViewSitemap,
}

# Sitemap configuration uses the default SITE_ID from settings
# Site domain configuration should be done via Django admin or management command
# NOT at module import time to avoid AppRegistryNotReady errors

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('webapp.urls')),
    path('project4.html', views.project4, name='project4'),
    
    # Sitemap URL with proper configuration
    path('sitemap.xml', sitemap, 
        {'sitemaps': sitemaps, 'template_name': 'sitemap.xml'}, 
        name='django.contrib.sitemaps.views.sitemap'
    ),
    
    # Robots.txt with template view for better control
    path('robots.txt', TemplateView.as_view(
        template_name='robots.txt', 
        content_type='text/plain'
    ), name='robots_file'),
]

# For serving static files in development and production
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
