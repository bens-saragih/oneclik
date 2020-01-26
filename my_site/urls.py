from django.conf.urls import url,include
from django.contrib import admin
from . import views
from django.conf.urls.static import static
from django.conf import settings
from ckeditor_uploader import views as uploader_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^artikel/',include('blog.urls',namespace='blog')),
    url(r'^ckeditor/',include('ckeditor_uploader.urls')),
    url(r'^$',views.index.as_view(),name='index'),
    url(r'^account/',include('account.urls',namespace='account')),
 
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
