from user.utils.tokens import account_activation_token
from django.middleware.csrf import get_token
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from user.userForm import UserForm
from user.models import UserInfo
from sparkpost import SparkPost
from django.http import HttpResponseRedirect


"""
    includes email activation
    returns json
"""
def registerUser(request):
    if request.method == "POST":
        form = UserForm(data=request.POST)
        # validation checks
        if form.is_valid():
            print(form.cleaned_data)
           
            user = form.save(commit=False)
            return sendEmailActivateLink(request, user)
        else:
            # Return invalid message as JSON
            return JsonResponse({'success': False, 'message': form.errors})
    
    # Get the CSRF token
    csrf_token = get_token(request)
        
    return JsonResponse({'csrf_token': csrf_token})


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = UserInfo.objects.get(pk=uid)
    except:
        user = None
    
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        
        return HttpResponseRedirect('http://localhost:3000/')
    return JsonResponse({'success': False, 'message': 'Activation invalid.'})

def sendEmailActivateLink(request, user):
    mail_subject = "Please activate your user account."
    message = render_to_string('activate_account.html',
        {
            'user': user.name,
            'domain': get_current_site(request).domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
            'protocol': 'https' if request.is_secure() else 'http',
        }
    )
    print("message", message)

    try: 
        # 你的SparkPost API密钥
        sp = SparkPost('0cce3a0b7ea7d58f4ca86f19425774b37d79cf6c')
        
        response = sp.transmissions.send(
            use_sandbox=False,  # 如果你要在SparkPost的沙盒环境中测试，设为True
            recipients=[user.email],
            html=message,
            from_email='dkdh_test@paradx.dev',  # 您的发件人地址
            subject=mail_subject
        )

        if response['total_accepted_recipients'] > 0:
            return JsonResponse({'success': True, 'message': 'please activate your email.'})
        else:
            return JsonResponse({'success': False, 'message': 'Failed to send email.'})
    except Exception as e:
        error_message = str(e)
        return JsonResponse({'success': False, 'message': error_message})