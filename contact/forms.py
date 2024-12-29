from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Adınız", widget=forms.TextInput(attrs={
        'placeholder': 'Adınızı girin...',
        'class': 'form-control'
    }))
    email = forms.EmailField(label="E-posta Adresiniz", widget=forms.EmailInput(attrs={
        'placeholder': 'E-posta adresinizi girin...',
        'class': 'form-control'
    }))
    message = forms.CharField(label="Mesajınız", widget=forms.Textarea(attrs={
        'placeholder': 'Mesajınızı yazın...',
        'class': 'form-control',
        'rows': 5
    }))