from django.contrib.auth.models import User
from django import forms
from .models import DefUser, Bb, AdditionalImage, FORSTATUS
from django.forms import inlineformset_factory
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.contrib.messages import constants as messages


class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={'placeholder': 'Имя пользователя'}))
    fio = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={'placeholder': 'Фио'}),validators=[RegexValidator('([А-ЯЁ][а-яё]+[\-\s]?){3,}', message='ФИО введено не верно')])
    email = forms.EmailField(required=True, label='', widget=forms.TextInput(attrs={'placeholder': 'Адрес электронной почты'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Повторите пароль'}))
    send_messages = forms.BooleanField(label='Согласие на обработку персональных данных', required=True)
    class Meta:
        model = DefUser
        fields = ('username', 'email', 'fio', 'password', 'password2', 'send_messages')
    #доделать
   # def fie_check(self):
       # fi = self.cleaned_data['fio']
       # check = [i for i in 'йцукенгшщзхъфывапролджэячсмитьбю ']
      #  for fi in check:
            #    if fi in check:
               #     raise forms.ValidationError('Только кириллица')
   #     return fi
    # доделать

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не соответствуют.')
        return cd['password2']


class CreateDesignForm(forms.ModelForm):
    title = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'placeholder': 'Название'}))
    description = forms.CharField(required=True, label="", widget=forms.Textarea(attrs={'placeholder': 'Описание'}))
    image = forms.ImageField(required=True, label="Изображение")
    class Meta:
        model = Bb
        fields = '__all__'
        widgets = {
                   'status': forms.HiddenInput,
                   'author': forms.HiddenInput,
                   'created': forms.HiddenInput,
                   }
AIFormSet = inlineformset_factory(Bb, AdditionalImage, fields='__all__')


class BbAdminForm(forms.ModelForm):
    def clean(self):
       status = self.cleaned_data['status']
       if (self.instance.status != status) and status == 'Новая':
           raise ValidationError("Вы не можете поменять статус")
       if (self.instance.status == 'Выполнено'):
           raise ValidationError("Вы не можете поменять статус")
       if (self.instance.status == 'Принято в работу'):
           raise ValidationError("Вы не можете поменять статус")


