from django.shortcuts import render
from django.http import JsonResponse,HttpRequest
from .serializers import BanksSerializer
from django.views import View
from .models import Banks
# Create your views here.

class DetailView(View):
    def get(self,request,ifsc):
        obj=Banks.objects.get(ifsc=ifsc)
        obj_data=BanksSerializer(obj)
        return JsonResponse(obj_data.data,safe=False)

class BranchView(View):
    def get(self,request,city,bankname):
        obj=Banks.objects.filter(city=city,bank_name=bankname)
        obj_data=BanksSerializer(obj,many=True)
        if len(obj_data.data)==0:
            return HttpRequest(request,'<h3>Check the url entered</h3>')
        print(obj_data.data)
        return JsonResponse(obj_data.data,safe=False)