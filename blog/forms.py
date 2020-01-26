from django.forms import ModelForm
from .models import Artikel
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

class ArtikelForm(ModelForm):
	content = forms.CharField(widget=CKEditorUploadingWidget())
	class Meta:
		model = Artikel
		fields = [
			'judul',
			'content',
			'kategori'
		]