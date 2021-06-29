from django import forms
from blogapp.models.Comment import Comment

class CommentForm(forms.ModelForm):
    
    def __init__(self,*args, **kwargs):
        self.author_id = kwargs.pop('author_id', None)
        self.post_id = kwargs.pop('post_id',None)
        self.email = kwargs.pop('email',None)
        super().__init__(*args, **kwargs)

    def save(self,commit=True):
        comment = super().save(commit=False)
        comment.author_id = self.author_id
        comment.post_id = self.post_id
        comment.email = self.email
        comment.save()

    class Meta:
        model=Comment
        fields=["content"]

class LoginForm(forms.Form):
    username = forms.CharField(
        label = ("Username"),
        widget = forms.TextInput(
            attrs = {
                'placeholder': 'username',
                'class': 'form-field'
            }
        )
    )

    password = forms.CharField(
        label = ("Password"),
        widget = forms.PasswordInput(
            attrs = {
                'placeholder': 'password',
                'class': 'form-field',
            }
        )
    )
