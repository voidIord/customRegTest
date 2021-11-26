from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import GroupNames
from django.forms import ModelForm, TextInput

from .models import Account, Semester


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Required. Add a valid email address.')

    class Meta:
        model = Account
        fields = ('email', 'username', 'gender', 'phone_no', 'prof_img', 'password1', 'password2',)


class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid login")


class ImageForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('prof_img',)

    def clean_prof_img(self):
        prof_img = self.cleaned_data['prof_img']
        return prof_img


class AccountUpdateForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('email', 'username', 'gender', 'phone_no', 'prof_img')

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
        except Account.DoesNotExist:
            return email
        raise forms.ValidationError('Email "%s" is already in use.' % account)

    def clean_username(self):
        username = self.cleaned_data['username']
        return username

    def clean_gender(self):
        gender = self.cleaned_data['gender']
        return gender

    def clean_phone_no(self):
        phone_no = self.cleaned_data['phone_no']
        return phone_no

    def clean_prof_img(self):
        prof_img = self.cleaned_data['prof_img']
        return prof_img


class GroupForm(ModelForm):
    class Meta:
        model = GroupNames
        fields = ['GroupName']

        widgets = \
        {
            "GroupName": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название Группы',
            }),
        }


class TableUpdateForm(forms.ModelForm):
    class Meta:
        model = Semester
        fields = ('Sem', 'Week1', 'Week2', 'Week3', 'Week4', 'Week5', 'Week6', 'Week7', 'Week8',
                  'Week9', 'Week10', 'Week11', 'Week12', 'Week13', 'Week14', 'Week15', 'Week16')

    widgets = \
        {
            "Sem": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер семестра',
            }),

            "Week1": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 1',
            }),

            "Week2": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 2',
            }),

            "Week3": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 3',
            }),

            "Week4": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 4',
            }),

            "Week5": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 5',
            }),

            "Week6": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 6',
            }),

            "Week7": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 7',
            }),

            "Week8": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 8',
            }),

            "Week9": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 9',
            }),

            "Week10": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 10',
            }),

            "Week11": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 11',
            }),

            "Week12": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 12',
            }),

            "Week13": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 13',
            }),

            "Week14": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 14',
            }),

            "Week15": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 15',
            }),

            "Week16": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Неделя 16',
            }),
        }