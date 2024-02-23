from django import forms
from testapp.models import feedback

class feedback_form(forms.ModelForm):
    class Meta:
        model = feedback
        # fields = ['name', 'email','message']
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Full Name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Email Address',
            }),

            'message' : forms.Textarea(attrs={
 
                'class': 'form-control',
                'placeholder': 'Please share your feedback',
            }),
        }