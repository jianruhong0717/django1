from django.http import HttpRequest

class UriPathMiddleware:
    def process_request(self, request):
        if request.path not in['/gaga/register/',
                               '/gaga/register_handle/',
                               '/gaga/register_valid',
                               '/gaga/login/',
                               '/gaga/login_handle/',
                               '/gaga/logout/']:
            request.session['url_path'] = request.get_full_path()
