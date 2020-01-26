from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User


class Artikel(models.Model):
	judul 		= models.CharField(max_length=255)
	content 	= RichTextUploadingField()
	LIST_CATEGORY = (
		('Blog','Blog'),
		('Jurnal','Jurnal'),
		('Berita','Berita')
		)
	kategori = models.CharField(max_length=20,choices=LIST_CATEGORY,default = 'Blog')
	published	= models.DateTimeField(auto_now_add=True)
	updated	 	= models.DateTimeField(auto_now=True)
	slug 		= models.SlugField(blank=True,editable=False)
	author	    = models.ForeignKey(User, null=True)

	def save(self):
		self.slug = slugify(self.judul)
		super().save()

	def get_absolute_url(self):
		url_slug = {'slug':self.slug}
		return reverse('blog:detail',kwargs=url_slug)

	def __str__(self):
		return "{}.{}".format(self.id,self.judul)

