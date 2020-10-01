from django import forms
from .models import Usuario


class PostForm(forms.ModelForm):


      class Meta:
            # Modelo base
            model = Usuario

            fields = (
                  'nome',
                  'sobrenome',
                  'senha',

            )

class LoginForm(forms.ModelForm):
      class Meta:
            model=Usuario
            fields=(
                  'nome',
                  'senha'
            )



