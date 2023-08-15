from django.core.exceptions import ValidationError
from django import forms
from user.models import UserInfo, UserPWD
from django import forms
from user.utils.encrypt import md5

class UserForm(forms.Form):
    # Fields from UserInfoModelForm
    name = forms.CharField(max_length=64)
    email = forms.EmailField()
    title = forms.CharField(max_length=64)
    company = forms.CharField(max_length=64)
    
    # Fields from UserPWDModelForm
    password = forms.CharField(widget=forms.PasswordInput(render_value=True))
    confirm_password = forms.CharField(
        label = "confirm password",
        widget = forms.PasswordInput(render_value=True),
    )
    
    agree_to_terms = forms.BooleanField(
        label = "I agree to the terms of use",
        required = True,
        widget = forms.CheckboxInput(),
        initial = False,  # Set the initial value to False (unchecked)
        error_messages = {'required': 'You must agree to the terms of use.'}
    )

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if UserInfo.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already in use.")
        return email
    
    def clean_password(self):
        password = self.cleaned_data.get("password")
        return md5(password)
    
    def clean_confirm_password(self):  # self: form
        print("check password and confirm password")
        password = self.cleaned_data.get("password")  # already encrypted
        confirm = md5(self.cleaned_data.get("confirm_password"))
        if confirm != password:
            raise ValidationError("Password Not Match")
        # 返回值为写入数据库的值
        return confirm
    
    def save(self, commit=True):
        if commit:
            activated_email = self.cleaned_data["email"],
            
            # Save data to the respective models and tables
            user_info_instance = UserInfo.objects.filter(email=activated_email).update(is_active=True)
        else:
            # Separate the data for each model
            user_info_data = {
                "name": self.cleaned_data["name"],
                "email": self.cleaned_data["email"],
                "title": self.cleaned_data["title"],
                "company": self.cleaned_data["company"],
                "is_active": False
            }

            user_pwd_data = {
                "password": self.cleaned_data["password"],
            }
            
            # Save data to the respective models and tables
            user_info_instance = UserInfo.objects.create(**user_info_data)
            user_pwd_instance = UserPWD.objects.create(user=user_info_instance, **user_pwd_data)
        
        return user_info_instance
