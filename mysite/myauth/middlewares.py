from django.http import HttpRequest, HttpResponseForbidden
from .models import Profile
from datetime import datetime
from django.core.exceptions import MultipleObjectsReturned


def set_useragent_on_request_middleware(get_response):
    def middleware(request: HttpRequest):
        #print(Profile.objects.filter(user=request.user.id).values('name')[0]['name'])
        response = get_response(request)

        return response

    return middleware
