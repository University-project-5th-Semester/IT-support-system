from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve as mediaserve
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import re_path



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('xit.urls', namespace='xit')),
]

urlpatterns.append(re_path(f'^{settings.MEDIA_URL.lstrip("/")}(?P<path>.*)$',
                     mediaserve, {'document_root': settings.MEDIA_ROOT}))

urlpatterns += staticfiles_urlpatterns()


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, 
                                      document_root=settings.MEDIA_ROOT)
  
