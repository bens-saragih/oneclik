from django.views.generic import TemplateView
from blog.models import Artikel
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.shortcuts import render,redirect

class index(TemplateView):
	template_name = 'index.html'
	
	def get_context_data(self):
		artikels = Artikel.objects.filter(kategori='Home')
		context = {
		'artikels':artikels
		}
		return context


def PromotedIndex(request):
	s = request.user.groups.all()
	args = {
	'a':s
	}
	return render (request,'promoted.html',args)