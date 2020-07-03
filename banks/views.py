from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
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
        return JsonResponse(obj_data.data,safe=False)