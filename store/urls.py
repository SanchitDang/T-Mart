from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# superadmin, superadmin@superadmin.com, SuperAdmin@8810625561



admin.site.site_header = 'TelaVergeMart'
admin.site.site_title = 'TelaVergeMart'
admin.site.index_title = 'TelaVergeMart'

urlpatterns = [

    path('', include('products.urls')),
    path('recommender/', include('recommender.urls')),
    path('admin/',include('admin_panel.urls')),
    path('super-admin', admin.site.urls)

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
