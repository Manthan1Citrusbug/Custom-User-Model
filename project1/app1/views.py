from app1.forms import user_form
from app1.models import UserModel
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.

class home(View):
    template_name = "home.html"
    form = user_form
    success_url = 'home/'
    def get(self, request):
        return render(request, self.template_name,{'form':self.form})
    def post(self, request):
        form = user_form(request.POST)
        # print("----------------form------------------------------------",form.clean_password())
        if form.is_valid():
            user_data = User.objects.create_user(form['email'].value(), form['name'].value(), form['password'].value())
            return HttpResponse(user_data)
        return render(request, self.template_name, {'form':form})
            
