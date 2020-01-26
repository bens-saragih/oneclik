from django.conf.urls import url 
from . import views

urlpatterns = [
	url(r'^detail/(?P<slug>[\w-]+)$',views.detail.as_view(),name='detail'),
	url(r'^kategori/(?P<kategori>[\w]+)/(?P<page>\d+)$',views.ArtikelKategoriListView.as_view(),name='kategori'),
	url(r'^(?P<page>\d+)$',views.ArtikelListView.as_view(),name='list'),
	url(r'^manage/$',views.ArtikelManageView.as_view(),name='manage'),
	url(r'^manage/update/(?P<pk>\d+)$',views.ArtikelUpdateView.as_view(),name='update'),
	url(r'^manage/delete/(?P<pk>\d+)$',views.ArtikelDeleteView.as_view(),name='delete'),
 	url(r'^create',views.CreateView.as_view(),name='create'),

]