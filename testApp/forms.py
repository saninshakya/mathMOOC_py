from django import forms


class testAppForm(forms.Form):
	test = forms.CharField(label="Test app Label",
	required=True, 
	widget=forms.Textarea(attrs={'placeholder':'Write Your Review'}
	))

