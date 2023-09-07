from django import forms
from .models import PostModel,comment

class PostModelForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={"rows": 4, "cols": 30})) 
    title = forms.CharField(widget=forms.TextInput(attrs={"size": 30}))  # TextInput widget for title

    class Meta:
        model=PostModel
        fields=("title","content")
    
class PostUpdateForm(forms.ModelForm):
    class Meta:
        model=PostModel
        fields=["title","content"]

class CommentForm(forms.ModelForm):
    content = forms.CharField(label='',widget=forms.TextInput(attrs={"placeholder": "Add comment here...."})) 

    class Meta:
        model=comment
        fields=["content"]



