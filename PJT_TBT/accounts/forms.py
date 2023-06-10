from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.contrib.auth import get_user_model


class CustomCreationUserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ["username", "nickname", "email", "profile_image"]

        labels = {
            "username": "이름",
            "nickname": "닉네임",
            "email": "이메일",
            "profile_image": "프로필 사진",
        }


class CustomChangeUserForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = [
            "nickname",
            "last_name",
            "first_name",
            "email",
            "profile_image",
        ]

        labels = {
            "last_name": "성",
            "first_name": "이름",
            "nickname": "닉네임",
            "email": "이메일",
            "profile_image": "프로필 사진",
        }


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    username = UsernameField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "아이디",
            }
        ),
        label="",
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "비밀번호",
            }
        ),
        label="",
    )
