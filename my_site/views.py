from django.views.generic import TemplateView
from blog.models import Artikel


class index(TemplateView):
	template_name = 'index.html'
	
	def get_context_data(self):
		artikels = Artikel.objects.filter(kategori='Home')
		context = {
		'artikels':artikels
		}
		return context