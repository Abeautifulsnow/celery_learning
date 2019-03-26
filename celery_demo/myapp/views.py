import json, time
from django.shortcuts import render
from django.http import HttpResponse

from myapp.models import Blog
from myapp.tasks import send_email
# Create your views here.

def home(request):
    send_email.delay('test@test.com')

    data = list(Blog.objects.values('caption'))
    return HttpResponse(json.dumps(data), content_type='applicaton/json')
