from django.shortcuts import redirect

def auth_middleware(get_respone):
    # one configuration and intialization 

    def middleware(request):
        print(request.session.get('customer'))
        returnUrl = request.META['PATH_INFO']
        print(request.META['PATH_INFO'])
        if not request.session.get('customer'):
            return redirect(f'login?returnUrl')
        
        response = get_respone(request)
        return response
    return middleware
