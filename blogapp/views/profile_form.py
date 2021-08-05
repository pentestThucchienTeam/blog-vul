from blogapp.models.Userprofile import Userprofile
from django import forms

class ProfileForm(forms.ModelForm):
	class Meta:
		model = Userprofile
		fields = [
			'first_name',
			'last_name',
			'phone',
			'address',
			'facebook',
			'github',
			'twitter',
			'avatar',
		]