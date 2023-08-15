from django.middleware.csrf import get_token
from django import forms
from django.http import JsonResponse
from user.utils.encrypt import md5
from user.models import UserInfo, UserPWD

class LoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput())
    
    def clean_password(self):
        pwd = self.cleaned_data.get('password')
        return md5(pwd)
    

def userLogin(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            
            # check if user exists
            user_email = form.cleaned_data.get('email')
            user_instance = UserInfo.objects.filter(email=user_email).first()
            if user_instance == None:
                return JsonResponse({'success': False, 'message': 'user does not exist.'})
            
            # check if user is active (email verified)
            if user_instance.is_active == False:
                return JsonResponse({'success': False, 'message': 'please verify your email.'})
                
            # check password correction
            user_pwd_instance = UserPWD.objects.get(user=user_instance)
            if form.cleaned_data.get('password') != user_pwd_instance.password:
                return JsonResponse({'success': False, 'message': 'wrong password.'})
            
            # add to session
            request.session['info'] = {
                'user_id': user_instance.pk,
                'name': user_instance.name,
            }
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'message': form.errors})
    
    # Get
    # Get the CSRF token
    csrf_token = get_token(request)
        
    return JsonResponse({'csrf_token': csrf_token})
