from django import forms
from .models import EmailAbonelik

class EmailAbonelikForm(forms.ModelForm):

    class Meta:
        model = EmailAbonelik
        fields = ('ad', 'soyad' , 'email',)

        widgets = {
            'ad':forms.TextInput(attrs={'class':'form-control','placeholder':'Joe'}),
            'soyad': forms.TextInput(attrs={'class': 'form-control','placeholder':'Doe'}),
            'email': forms.EmailInput(attrs={'class': 'form-control','placeholder':'name@example.com'}),
          }