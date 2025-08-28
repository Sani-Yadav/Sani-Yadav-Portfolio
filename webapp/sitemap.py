from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from django.utils import timezone

class StaticViewSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9
    lastmod = timezone.now()

    def items(self):
        # List of all URL names from webapp/urls.py
        return [
            'home',
            'resume',
            'contact',
            'about',
            'skills',
            'services',
            'portfolio',
            'portfolio_details',
            'quicksupport',
            'project2',
            'project04',
            'project4',
            'project05',
            'project06',
            'service_details',
            'job',
        ]

    def location(self, item):
        return reverse(item)

    def priority(self, item):
        # Higher priority for important pages
        if item in ['home', 'about', 'portfolio', 'resume']:
            return 1.0
        return 0.8

    def changefreq(self, item):
        # More frequent updates for important pages
        if item in ['home', 'portfolio']:
            return 'daily'
        return 'weekly'
