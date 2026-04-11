from django.core.cache import cache

from .models import Blog


def latest_blogs(request):
    cache_key = 'latest_published_blogs_3'
    blogs = cache.get(cache_key)
    if not blogs:
        blogs = Blog.objects.filter(
            publication_attribute=True,
        ).order_by('-created_at')[:3]
        cache.set(cache_key, blogs, 30)
    return {'latest_blogs': blogs}
