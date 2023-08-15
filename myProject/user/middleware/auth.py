from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse

class AuthMiddleware(MiddlewareMixin):

    def process_request(self, request):
        
        print("request.path_info", request.path_info)
        # 0. the pages that need no authentication
        if request.path_info in ["/login/", "/activate/", "/register/", "/favicon.ico"]:
            print("return...")
            return

        # 1. read current user's session. If session exists, then the user is already logged in
        user_info = request.session.get("info")
        print("user_info", user_info)
        if user_info:
            return

        # 2. Block the user if it is not logged in
        return JsonResponse({'success': False, 'message': 'please login.'})
    