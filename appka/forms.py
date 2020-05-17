from django import forms



gender = ( ('MALE', 'Male'),('FEMALE','Female'))
city = (('WARSAW','Warsaw'),('POZNAN','Poznan'),('WROCLAW','Wroclaw'),('CRACOW','Cracow'))

class CourseForm(forms.Form):
    name = forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder': ' your name', 'class' : 'field'}))
    surname = forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder': ' your surname', 'class' : 'field'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': ' your email', 'class' : 'field'}))
    post_code = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Your post code in such format (12-345)', 'pattern': '[0-9]{2}-[0-9]{3}', 'class' : 'field'}))
    gender = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class' : 'select'}), choices=gender )
    city = forms.ChoiceField(widget=forms.Select(attrs={'class' : 'field'}), required=True, choices=city)
    etc = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'if you have any concerns pleases write them down here','class' : 'field'}), required=False )
