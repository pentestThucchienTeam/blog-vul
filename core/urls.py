import re
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.views.static import serve


def static(prefix, view=serve, **kwargs):
    """
    Return a URL pattern for serving files in debug mode.
    from django.conf import settings
    from django.conf.urls.static import static
    urlpatterns = [
        # ... the rest of your URLconf goes here ...
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    """
    if not prefix:
        raise ImproperlyConfigured("Empty static prefix not permitted")
    return [
        re_path(r"^%s(?P<path>.*)$" % re.escape(prefix.lstrip("/")), view, kwargs=kwargs),
    ]


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("blogapp.urls")),
    path("ckeditor/", include("ckeditor_uploader.urls")),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
