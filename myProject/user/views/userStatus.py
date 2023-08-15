from django.middleware.csrf import get_token
from django.http import JsonResponse
    

def userStatus(request):
    if request.method == "POST":
        # check user login status
        info = request.session.get('info')
        if info == None:
            return JsonResponse({'success': False, 'message': 'user does not login.'})
        else:
            return JsonResponse({'success': True, 'message': request.session.get('info')})
    
    # Get
    # Get the CSRF token
    csrf_token = get_token(request)
        
    return JsonResponse({'csrf_token': csrf_token})
