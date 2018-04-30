from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render
from datetime import datetime, timedelta
from django.conf import settings
from django.contrib import auth

class PageNFANDAutologout(MiddlewareMixin):
    def process_response(self, request, response):
        #json_data = json.loads(response.text)
        if (response.status_code == 404):
            return render(request,"page_not_found.html")
        else:
            return response
'''
    def process_request(self, request):
        if request.user.is_authenticated:
            try:
                
                if (datetime.now() - request.session['last_touch']) > (timedelta( 0, settings.AUTO_LOGOUT_DELAY * 60, 0)):
                    auth.logout(request)
                    del request.session['last_touch']
                    return None
                
            except KeyError:
                pass

        request.session['last_touch'] = datetime.now()
'''