from django import forms
from .models import Contact,Comment


class AttendForm(forms.ModelForm):
   


    class Meta:
        model=Contact
        fields=[
            'email',
            'message',
        ]

class CommentForm(forms.ModelForm):

    class Meta:
        model=Comment
        fields=[
            'name',
            'email',
            'comment',

]         
