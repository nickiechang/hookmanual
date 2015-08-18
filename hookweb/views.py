from django.shortcuts import render
from django.http import HttpResponse

import os

# Create your views here.

def home(request):
    print 'home'
   
    os.system("[ -d /tmp/haproxyweb-manual ] && rm -fR /tmp/haproxyweb-manual")
    os.system("cd /tmp && git clone git@172.16.18.91:nick_chang/haproxyweb-manual.git")
    os.system("gitbook build /tmp/haproxyweb-manual")
    os.system("[ -d /tmp/haproxyweb-manual/_book ] && sudo rm -fr /var/www/html/_book")
    os.system("sudo cp -r /tmp/haproxyweb-manual/_book /var/www/html/")
    
    return HttpResponse('home')
