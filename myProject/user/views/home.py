from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse


def home(request):
    # check user login status
    info = request.session.get('info')
    if info == None:
        return JsonResponse({'success': False, 'message': 'user does not login.'})
    
    
    return HttpResponse('welcome')