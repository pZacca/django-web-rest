from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.views import View

# Create your views here.
class Home(View):
    def get(self, request: HttpRequest):
        print('aq foi get')

        return render(request, 'HOMEZADA')
    
    def post(self, request: HttpRequest):
        print('aq foi post')

        return redirect('/')