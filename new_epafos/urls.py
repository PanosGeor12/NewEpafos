from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
    path('', include('accounts.urls')),
    path('', include('dashboard.urls', namespace='dashboard')),
    path('', include('core.urls', namespace='core')),
    path('', include('news.urls', namespace='news'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
