from django.contrib.sitemaps import Sitemap
from .models import Blog
from django.shortcuts import reverse


class BlogSitemaps(Sitemap):
    changefreq = 'monthly'
    priority = 0.9

    def items(self):
        return self.get_active_blogs()

    def lastmod(self, obj):
        return obj.updated

    def location(self, item):
        return item.get_absolute_url()

    def get_active_blogs(self):
        return Blog.objects.filter(active=True)
