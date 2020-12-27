from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Submit
from django import forms
from .models import Snippet,ExamQ,ExamV,Profile
from django.core.validators import RegexValidator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User





class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('first_name','last_name','username','email','password')

class ExamQt(forms.ModelForm):
    class Meta():
        model = ExamQ
        fields =('q1','q2','q3','q4')

class ExamVt(forms.ModelForm):
    class Meta():
        model = ExamV
        fields =('q1','q2','q3','q4')


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']




#---------------------- not realy usefull =-----------------------------------
class NameWidget(forms.MultiWidget):

    def __init__(self, attrs=None):
        super().__init__([
            forms.TextInput(),
            forms.TextInput()
        ],attrs)

    def decompress(self,value):
        if value:
            return value.split(' ')
        return ['', '']
#---------------------- not realy usefull =-----------------------------------
class NameField(forms.MultiValueField):

    widget = NameWidget

    def __init__(self,*args,**kwargs):

        fields = (
            forms.CharField(validators=[
                RegexValidator(r'[a-zA-Z]+','enter a valid name ()')
            ]),
            forms.CharField(validators=[
                RegexValidator(r'[a-zA-Z]+','enter a valid name ()')
            ])
        )

        super().__init__(fields,*args,**kwargs)
    def compress(self,data_list):
        return f'{data_list[0]} {data_list[1]}'
#--------------------------For practice ------------------------------------
class ContactForm(forms.Form):
    name = NameField()
    email = forms.EmailField(label='E-Mail')
    #category = forms.ChoiceField(choices[('question','Question'),('other','Other')])
    subject = forms.CharField(required=False)
    body = forms.CharField(widget=forms.Textarea)

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.helper = FormHelper
        self.helper.form_method = 'POST'

        self.helper.layout = Layout(
            'name',
            'email',
            'subject',
            'body',
            Submit('submit','Submit',css_class='btn-success')
        )
#--------------------------For practice ------------------------------------
class SnippetForm(forms.ModelForm):

    class Meta:
        model = Snippet
        fields = ('name','body')


#---------------------not in use in Views-----------------------------
class SignUpForm(UserCreationForm): 
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ( 'first_name', 'last_name', 'email', 'password' )
    def __init__ (self, *args, **kwargs):
        super(SignUpForm,self).__init__(*args, **kwargs)
        #remove what you like...
        self.fields.pop ('password1')
        self.fields.pop ('password2')

#---------------------not in use in Views-----------------------------
class CustomUserCreationForm(forms.Form): 
    first_name = forms.CharField( min_length=4, max_length=150)
    last_name = forms.CharField( min_length=4, max_length=150)
    email = forms.EmailField(label='Enter email')
    password = forms.CharField(label='Enter password', widget=forms.PasswordInput)


    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise  ValidationError("Email already exists")
        return email


    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['first_name'],
            self.cleaned_data['last_name'],
            self.cleaned_data['email'],
            self.cleaned_data['password']
        )
        return user


