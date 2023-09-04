from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from abc import ABC, abstractmethod
import time



class FormManage:

    def authorization(request):
        
        return render(request, 'autorization.html')
        

    def end(request):
        return render(request,'end.html' )
