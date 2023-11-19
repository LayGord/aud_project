from django import forms


class PostForm(forms.Form):
    location = forms.CharField(max_length=255, required=True, label='Текущая погода в...') #
