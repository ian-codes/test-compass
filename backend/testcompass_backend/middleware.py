from django.utils.deprecation import MiddlewareMixin

class MyCustomMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        print("hello")
        self.get_response = get_response
        # Initialization code can go here

    def __call__(self, request):
        # Code to execute for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to execute for each request/response after
        # the view is called.

        return response