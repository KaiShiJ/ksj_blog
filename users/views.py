from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django import forms
from django.contrib.auth.forms import UserCreationForm
from.forms import RegisterForm


def register(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            new_user=form.save()
            return HttpResponseRedirect('/blog/')

    else:
        form=UserCreationForm()
    return render_to_response(("registration/register.html",{'form':form,}))


