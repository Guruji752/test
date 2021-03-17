from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title', 'author','body','image')
        widget={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'author':forms.Select(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'})
        }

class UpdateForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','body','image')
        widget={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            #'author':forms.Select(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'})
        }

'''class EmailPostForm(forms.Form):
    name =forms.CharField(max_length=25)
    email=forms.EmailField()
    to=forms.EmailField()
    comments=forms.CharField(required=False,widget=forms.Textarea)
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('name','email','body')'''