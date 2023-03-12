from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()
	password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput)
	#agregar photo=forms.Imagefield

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
		help_texts = {k:"" for k in fields }

#  class PostForm(models.form)
# 	content = forms.CharField(label='', widget=forms.Textarea(attrs={'rows':2, 'placeholder': 'Publica tu receta ¡ incluye debajo una foto!'}), required=True)
#	image= forms.ImageField()
#	class Meta:
#		model = Post
#		fields = ['content','image']

class PostForm(forms.ModelForm):
	class Meta:
		model= Post
		fields=('title','content','image')
		labels= {
			 'content':'',
			 'image':'',
			 'title':''

		}
		widgets={
			'title':forms.TextInput(attrs={'placeholder':'Ponle un nombre '}),
			'content':forms.TextInput(attrs={'placeholder':'Publica una receta ¡No olvides la foto!'})
		}